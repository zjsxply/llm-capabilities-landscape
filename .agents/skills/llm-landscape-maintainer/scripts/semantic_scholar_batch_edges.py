#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import importlib.util
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from landscape_paths import default_markdown_files

try:
    import fcntl
except ImportError:  # pragma: no cover - this project runs on Linux.
    fcntl = None


SCRIPT_DIR = Path(__file__).resolve().parent
S2_SCRIPT = SCRIPT_DIR / "semantic_scholar_citation_scan.py"
API = "https://api.semanticscholar.org/graph/v1"
BASE_FIELDS = [
    "paperId",
    "corpusId",
    "title",
    "year",
    "venue",
    "publicationDate",
    "citationCount",
    "referenceCount",
    "externalIds",
    "url",
]
RICH_FIELDS = [
    "abstract",
    "openAccessPdf",
]
EDGE_BASE_FIELDS = [
    "paperId",
    "corpusId",
    "title",
    "year",
    "venue",
    "publicationDate",
    "citationCount",
    "referenceCount",
    "externalIds",
    "url",
]
EDGE_RICH_FIELDS = [
    "abstract",
    "openAccessPdf",
]
SLIM_FIELDS = ",".join(
    BASE_FIELDS
    + [f"citations.{field}" for field in EDGE_BASE_FIELDS]
    + [f"references.{field}" for field in EDGE_BASE_FIELDS]
)
RICH_BATCH_FIELDS = ",".join(
    [
        *BASE_FIELDS,
        *RICH_FIELDS,
        *[f"citations.{field}" for field in EDGE_BASE_FIELDS],
        *[f"citations.{field}" for field in EDGE_RICH_FIELDS],
        *[f"references.{field}" for field in EDGE_BASE_FIELDS],
        *[f"references.{field}" for field in EDGE_RICH_FIELDS],
    ]
)


def load_s2_module():
    spec = importlib.util.spec_from_file_location("semantic_scholar_citation_scan", S2_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {S2_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


S2 = load_s2_module()


def read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


@contextlib.contextmanager
def file_lock(path: Path, enabled: bool):
    if not enabled or fcntl is None:
        yield
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def edge_cache_path(cache_dir: Path, identifier: str, edge: str) -> Path:
    return cache_dir / "edges" / f"{S2.safe_name(identifier)}.{edge}.json"


def paper_cache_path(cache_dir: Path, identifier: str) -> Path:
    return cache_dir / "papers" / f"{S2.safe_name(identifier)}.json"


def is_good_cache(path: Path) -> bool:
    data = read_json(path)
    return isinstance(data, dict) and not data.get("_error") and isinstance(data.get("data"), list)


def needs_fetch(cache_dir: Path, identifier: str, edges: list[str], refresh: bool) -> bool:
    if refresh:
        return True
    return any(not is_good_cache(edge_cache_path(cache_dir, identifier, edge)) for edge in edges)


def edge_payload(paper: dict[str, Any], edge: str) -> dict[str, Any]:
    key = "citingPaper" if edge == "citations" else "citedPaper"
    rows = [{key: item} for item in paper.get(edge) or [] if isinstance(item, dict)]
    return {"offset": 0, "data": rows}


def paper_payload(paper: dict[str, Any]) -> dict[str, Any]:
    excluded = {"citations", "references"}
    return {key: value for key, value in paper.items() if key not in excluded}


class BatchClient:
    def __init__(
        self,
        *,
        fields: str,
        min_delay: float,
        max_delay: float,
        delay_decrease: float,
        max_retries: int,
    ) -> None:
        self.fields = fields
        self.min_delay = max(0.0, min(min_delay, 30.0))
        self.max_delay = max(self.min_delay, min(max_delay, 30.0))
        self.delay_decrease = max(0.0, delay_decrease)
        self.delay = self.min_delay
        self.max_retries = max_retries
        self.last_request = 0.0
        self.api_key = os.environ.get("S2_API_KEY") or os.environ.get("SEMANTIC_SCHOLAR_API_KEY")

    def headers(self) -> dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "llm-landscape-maintainer/1.0",
        }
        if self.api_key:
            headers["x-api-key"] = self.api_key
        return headers

    def wait_turn(self) -> None:
        elapsed = time.monotonic() - self.last_request
        wait = self.delay - elapsed
        if wait > 0:
            time.sleep(wait)

    def note_success(self) -> None:
        if self.delay > self.min_delay and self.delay_decrease > 0:
            self.delay = max(self.min_delay, self.delay - self.delay_decrease)
            print(f"success: reducing delay to {self.delay:.1f}s", flush=True)

    def note_429(self, retry_after: float) -> float:
        self.delay = min(self.max_delay, max(self.min_delay, self.delay * 2.0, retry_after))
        wait = min(self.max_delay, max(self.delay, retry_after))
        print(f"429: doubling delay to {self.delay:.1f}s; wait={wait:.1f}s", flush=True)
        return wait

    def post_batch(self, identifiers: list[str]) -> tuple[int, list[Any]]:
        url = f"{API}/paper/batch?fields={urllib.parse.quote(self.fields, safe=',.')}"
        body = json.dumps({"ids": identifiers}).encode("utf-8")
        for attempt in range(self.max_retries + 1):
            self.wait_turn()
            req = urllib.request.Request(url, data=body, method="POST", headers=self.headers())
            try:
                with urllib.request.urlopen(req, timeout=90) as response:
                    self.last_request = time.monotonic()
                    data = json.loads(response.read().decode("utf-8"))
                    self.note_success()
                    return response.status, data if isinstance(data, list) else []
            except urllib.error.HTTPError as exc:
                self.last_request = time.monotonic()
                if exc.code == 429:
                    retry_after = exc.headers.get("Retry-After")
                    try:
                        retry_wait = float(retry_after) if retry_after else 0.0
                    except ValueError:
                        retry_wait = 0.0
                    time.sleep(self.note_429(retry_wait))
                    continue
                if 500 <= exc.code < 600 and attempt < self.max_retries:
                    wait = min(self.max_delay, max(self.delay, self.min_delay) * (2**attempt))
                    print(f"HTTP {exc.code}: retry in {wait:.1f}s", flush=True)
                    time.sleep(wait)
                    continue
                print(f"HTTP {exc.code}: batch failed for {len(identifiers)} ids", flush=True)
                return exc.code, []
            except Exception as exc:  # noqa: BLE001 - diagnostics script should keep going.
                self.last_request = time.monotonic()
                if attempt < self.max_retries:
                    wait = min(self.max_delay, max(self.delay, self.min_delay) * (2**attempt))
                    print(f"{type(exc).__name__}: retry in {wait:.1f}s", flush=True)
                    time.sleep(wait)
                    continue
                print(f"{type(exc).__name__}: batch failed for {len(identifiers)} ids", flush=True)
                return 0, []
        return 0, []


def write_error_edges(cache_dir: Path, identifier: str, edges: list[str], status: int, message: str) -> None:
    payload = {"_error": {"status": status, "message": message}}
    for edge in edges:
        write_json(edge_cache_path(cache_dir, identifier, edge), payload)


def write_paper_edges(cache_dir: Path, identifier: str, paper: dict[str, Any], edges: list[str]) -> None:
    write_json(paper_cache_path(cache_dir, identifier), paper_payload(paper))
    for edge in edges:
        write_json(edge_cache_path(cache_dir, identifier, edge), edge_payload(paper, edge))


def fetch_and_write(
    client: BatchClient,
    cache_dir: Path,
    identifiers: list[str],
    edges: list[str],
    *,
    allow_split: bool,
) -> tuple[int, int]:
    status, papers = client.post_batch(identifiers)
    if status == 200 and papers:
        fetched = 0
        missing = 0
        for identifier, paper in zip(identifiers, papers):
            if not isinstance(paper, dict):
                write_error_edges(cache_dir, identifier, edges, 404, "paper not found by batch")
                missing += 1
                continue
            write_paper_edges(cache_dir, identifier, paper, edges)
            fetched += 1
        if len(papers) < len(identifiers):
            for identifier in identifiers[len(papers) :]:
                write_error_edges(cache_dir, identifier, edges, 502, "batch response shorter than request")
                missing += 1
        return fetched, missing

    if status == 400 and allow_split and len(identifiers) > 1:
        mid = len(identifiers) // 2
        left = fetch_and_write(client, cache_dir, identifiers[:mid], edges, allow_split=allow_split)
        right = fetch_and_write(client, cache_dir, identifiers[mid:], edges, allow_split=allow_split)
        return left[0] + right[0], left[1] + right[1]

    message = "batch failed"
    for identifier in identifiers:
        write_error_edges(cache_dir, identifier, edges, status, message)
    return 0, len(identifiers)


def chunks(items: list[str], size: int) -> list[list[str]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def write_report(path: Path, *, identifiers: list[str], fetched: int, skipped: int, cache_dir: Path) -> None:
    lines = [
        "# Semantic Scholar Batch Edge Backfill",
        "",
        f"- Generated: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"- Identifiers: {len(identifiers)}",
        f"- Already cached/skipped: {skipped}",
        f"- Batch returned papers: {fetched}",
        f"- Cache directory: `{cache_dir}`",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Backfill S2 citation/reference edge caches using paper/batch.")
    parser.add_argument("files", nargs="*", type=Path, help="Markdown/text files from which to extract identifiers. Defaults to README and recursive docs.")
    parser.add_argument("--id", action="append", default=[], help="Explicit paper identifier.")
    parser.add_argument("--cache-dir", type=Path, default=Path(".tmp/semantic_citation_cache"))
    parser.add_argument("--lock-file", type=Path, default=Path(".tmp/semantic_citation_cache/api.lock"))
    parser.add_argument("--no-lock", action="store_true")
    parser.add_argument("--out", type=Path, default=Path(".tmp/semantic_batch_edges.md"))
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--edge", choices=["citations", "references"], action="append")
    parser.add_argument("--min-delay", type=float, default=0.1)
    parser.add_argument("--max-delay", type=float, default=30.0)
    parser.add_argument("--delay-decrease", type=float, default=0.2)
    parser.add_argument("--max-retries", type=int, default=10)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--no-split-400", action="store_true", help="Do not recursively split HTTP 400 batches.")
    parser.add_argument(
        "--include-abstracts",
        action="store_true",
        help="Request abstracts/openAccessPdf for seeds and edge papers. This is richer but can make large batches fail.",
    )
    args = parser.parse_args()

    edges = list(dict.fromkeys(args.edge or ["citations", "references"]))
    files = args.files or default_markdown_files(Path.cwd())
    identifiers = S2.collect_identifiers(files, args.id)
    targets = [identifier for identifier in identifiers if needs_fetch(args.cache_dir, identifier, edges, args.refresh)]
    skipped = len(identifiers) - len(targets)
    print(f"Identifiers: {len(identifiers)}; batch targets: {len(targets)}; skipped: {skipped}", flush=True)

    fetched = 0
    with file_lock(args.lock_file, enabled=not args.no_lock):
        client = BatchClient(
            fields=RICH_BATCH_FIELDS if args.include_abstracts else SLIM_FIELDS,
            min_delay=args.min_delay,
            max_delay=args.max_delay,
            delay_decrease=args.delay_decrease,
            max_retries=args.max_retries,
        )
        for index, batch in enumerate(chunks(targets, max(1, min(args.batch_size, 500))), 1):
            print(f"[batch {index}] {len(batch)} ids", flush=True)
            batch_fetched, batch_missing = fetch_and_write(
                client,
                args.cache_dir,
                batch,
                edges,
                allow_split=not args.no_split_400,
            )
            fetched += batch_fetched
            if batch_missing:
                print(f"batch missing/error ids: {batch_missing}", flush=True)

    write_report(args.out, identifiers=identifiers, fetched=fetched, skipped=skipped, cache_dir=args.cache_dir)
    print(f"Batch returned papers: {fetched}", flush=True)
    print(f"Wrote {args.out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
