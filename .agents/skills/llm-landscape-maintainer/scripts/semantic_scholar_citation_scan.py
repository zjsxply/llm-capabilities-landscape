#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import contextlib
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

try:
    import fcntl
except ImportError:  # pragma: no cover - this project runs on Linux.
    fcntl = None


API = "https://api.semanticscholar.org/graph/v1"
PAPER_FIELDS = ",".join(
    [
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
        "abstract",
        "openAccessPdf",
    ]
)
EDGE_FIELDS = ",".join(
    [
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
        "abstract",
        "openAccessPdf",
    ]
)
ARXIV_ID = r"\d{4}\.\d{4,5}(?:v\d+)?"
ARXIV_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(" + ARXIV_ID + r")", re.I)
ARXIV_TEXT_RE = re.compile(r"\barXiv:(" + ARXIV_ID + r")", re.I)
DOI_URL_RE = re.compile(r"https?://(?:dx\.)?doi\.org/([^\s<>)\]}\"']+)", re.I)
S2_PAPER_RE = re.compile(r"semanticscholar\.org/paper/(?:[^/\s]+/)?([0-9a-f]{40})", re.I)


def read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as exc:
        print(f"WARN malformed cache ignored: {path} ({exc})", file=sys.stderr, flush=True)
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
        print(f"Waiting for Semantic Scholar API lock: {path}", flush=True)
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            print(f"Acquired Semantic Scholar API lock: {path}", flush=True)
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
            print(f"Released Semantic Scholar API lock: {path}", flush=True)


def safe_name(identifier: str) -> str:
    if identifier.lower().startswith("arxiv:"):
        return identifier.split(":", 1)[1].replace("/", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", identifier).strip("_")
    if 1 <= len(cleaned) <= 90:
        return cleaned
    return hashlib.sha256(identifier.encode("utf-8")).hexdigest()[:24]


def normalize_identifier(raw: str) -> str | None:
    value = raw.strip().strip(".,;:)]}>\"'")
    if not value:
        return None
    arxiv_url = ARXIV_URL_RE.search(value)
    if arxiv_url:
        return f"arXiv:{arxiv_url.group(1).removesuffix('.pdf')}"
    if re.fullmatch(ARXIV_ID, value, flags=re.I):
        return f"arXiv:{value}"
    if value.lower().startswith("arxiv:"):
        arxiv = value.split(":", 1)[1]
        if re.fullmatch(ARXIV_ID, arxiv, flags=re.I):
            return f"arXiv:{arxiv}"
    doi_url = DOI_URL_RE.search(value)
    if doi_url:
        return f"DOI:{urllib.parse.unquote(doi_url.group(1).rstrip('.,;'))}"
    if value.lower().startswith("doi:"):
        return f"DOI:{urllib.parse.unquote(value.split(':', 1)[1].rstrip('.,;'))}"
    s2 = S2_PAPER_RE.search(value)
    if s2:
        return s2.group(1)
    if re.fullmatch(r"[0-9a-f]{40}", value, flags=re.I):
        return value
    if value.lower().startswith("corpusid:"):
        return f"CorpusId:{value.split(':', 1)[1]}"
    return None


def collect_identifiers(files: list[Path], direct_ids: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []

    def add(raw: str) -> None:
        item = normalize_identifier(raw)
        if item and item not in seen:
            seen.add(item)
            ordered.append(item)

    for raw in direct_ids:
        add(raw)
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in ARXIV_URL_RE.finditer(text):
            add(match.group(1))
        for match in ARXIV_TEXT_RE.finditer(text):
            add(match.group(1))
        for match in DOI_URL_RE.finditer(text):
            add(f"DOI:{match.group(1)}")
        for match in S2_PAPER_RE.finditer(text):
            add(match.group(1))
    return ordered


class S2Client:
    def __init__(
        self,
        *,
        min_delay: float,
        max_delay: float,
        delay_decrease: float,
        max_retries: int,
        refresh: bool,
        stale_on_error: bool,
    ) -> None:
        self.max_delay = max(0.0, min(max_delay, 30.0))
        self.min_delay = min(max(0.0, min_delay), self.max_delay)
        self.delay_decrease = max(0.0, delay_decrease)
        self.delay = min(self.max_delay, self.min_delay)
        self.max_retries = max_retries
        self.refresh = refresh
        self.stale_on_error = stale_on_error
        self.last_request = 0.0
        self.api_key = os.environ.get("S2_API_KEY") or os.environ.get("SEMANTIC_SCHOLAR_API_KEY")

    def _wait_turn(self) -> None:
        elapsed = time.monotonic() - self.last_request
        needed = self.delay - elapsed
        if needed > 0:
            time.sleep(needed)

    def _headers(self) -> dict[str, str]:
        headers = {"User-Agent": "llm-landscape-maintainer/1.0"}
        if self.api_key:
            headers["x-api-key"] = self.api_key
        return headers

    def _note_success(self) -> None:
        if self.delay <= self.min_delay or self.delay_decrease <= 0:
            return
        self.delay = max(self.min_delay, self.delay - self.delay_decrease)
        print(f"success: reducing delay to {self.delay:.1f}s", flush=True)

    def _note_rate_limit(self, retry_after: float) -> float:
        self.delay = min(
            self.max_delay,
            max(self.min_delay, self.delay * 2.0, retry_after),
        )
        wait = min(self.max_delay, max(self.delay, retry_after))
        print(f"429: doubling delay to {self.delay:.1f}s; wait={wait:.1f}s", flush=True)
        return wait

    def request_json(self, url: str, cache_path: Path) -> Any:
        cached = read_json(cache_path)
        if cached is not None and not self.refresh:
            return cached

        for attempt in range(self.max_retries + 1):
            self._wait_turn()
            try:
                req = urllib.request.Request(url, headers=self._headers())
                with urllib.request.urlopen(req, timeout=60) as response:
                    self.last_request = time.monotonic()
                    data = json.loads(response.read().decode("utf-8"))
                    write_json(cache_path, data)
                    self._note_success()
                    return data
            except urllib.error.HTTPError as exc:
                self.last_request = time.monotonic()
                if exc.code == 404:
                    data = {"_error": {"status": 404, "url": url}}
                    write_json(cache_path, data)
                    return data
                if exc.code == 429:
                    retry_after = exc.headers.get("Retry-After")
                    try:
                        retry_wait = float(retry_after) if retry_after else 0.0
                    except ValueError:
                        retry_wait = 0.0
                    wait = self._note_rate_limit(retry_wait)
                    time.sleep(wait)
                    continue
                if 500 <= exc.code < 600 and attempt < self.max_retries:
                    wait = min(self.max_delay, self.delay * (2**attempt))
                    print(f"HTTP {exc.code}: retry in {wait:.1f}s", flush=True)
                    time.sleep(wait)
                    continue
                if cached is not None and self.stale_on_error:
                    print(f"WARN using stale cache after HTTP {exc.code}: {cache_path}", file=sys.stderr)
                    return cached
                return {"_error": {"status": exc.code, "url": url}}
            except Exception as exc:  # noqa: BLE001 - keep script high-availability.
                self.last_request = time.monotonic()
                if attempt < self.max_retries:
                    wait = min(self.max_delay, self.delay * (2**attempt))
                    print(f"{type(exc).__name__}: retry in {wait:.1f}s", flush=True)
                    time.sleep(wait)
                    continue
                if cached is not None and self.stale_on_error:
                    print(f"WARN using stale cache after {type(exc).__name__}: {cache_path}", file=sys.stderr)
                    return cached
                return {"_error": {"type": type(exc).__name__, "message": str(exc), "url": url}}
        if cached is not None and self.stale_on_error:
            return cached
        return {"_error": {"status": 429, "url": url, "message": "retry budget exhausted"}}


def paper_cache_path(cache_dir: Path, identifier: str) -> Path:
    return cache_dir / "papers" / f"{safe_name(identifier)}.json"


def edge_cache_path(cache_dir: Path, identifier: str, edge: str) -> Path:
    return cache_dir / "edges" / f"{safe_name(identifier)}.{edge}.json"


def fetch_paper(client: S2Client, cache_dir: Path, identifier: str) -> dict[str, Any]:
    quoted = urllib.parse.quote(identifier, safe="")
    url = f"{API}/paper/{quoted}?fields={urllib.parse.quote(PAPER_FIELDS, safe=',')}"
    data = client.request_json(url, paper_cache_path(cache_dir, identifier))
    return data if isinstance(data, dict) else {"_error": {"message": "non-object response"}}


def legacy_edge_cache(cache_dir: Path, identifier: str, edge: str) -> Any | None:
    if edge != "citations" or not identifier.lower().startswith("arxiv:"):
        return None
    arxiv = identifier.split(":", 1)[1]
    legacy = cache_dir / "s2_citation_cache" / f"{arxiv}.json"
    data = read_json(legacy)
    if data is not None:
        return data
    return None


def fetch_edges(
    client: S2Client,
    cache_dir: Path,
    identifier: str,
    paper_id: str,
    edge: str,
    max_edges: int,
    page_size: int,
) -> dict[str, Any]:
    path = edge_cache_path(cache_dir, identifier, edge)
    cached = read_json(path)
    if cached is not None and not cached.get("_error") and not client.refresh:
        return cached
    legacy = legacy_edge_cache(cache_dir, identifier, edge)
    if legacy is not None and not client.refresh:
        write_json(path, legacy)
        return legacy

    collected: list[Any] = []
    offset = 0
    paper_field = "citingPaper" if edge == "citations" else "citedPaper"
    edge_fields = ",".join(f"{paper_field}.{field}" for field in EDGE_FIELDS.split(","))
    while len(collected) < max_edges:
        limit = min(page_size, max_edges - len(collected))
        quoted = urllib.parse.quote(paper_id, safe="")
        url = (
            f"{API}/paper/{quoted}/{edge}?fields={urllib.parse.quote(edge_fields, safe=',.')}"
            f"&limit={limit}&offset={offset}"
        )
        page_path = cache_dir / "pages" / f"{safe_name(identifier)}.{edge}.{offset}.json"
        page = client.request_json(url, page_path)
        if not isinstance(page, dict) or page.get("_error"):
            break
        data = page.get("data") or []
        collected.extend(data)
        write_json(path, {"offset": 0, "data": collected, "_partial": True})
        next_offset = page.get("next")
        if next_offset is None or not data:
            break
        offset = int(next_offset)
    result = {"offset": 0, "data": collected}
    write_json(path, result)
    return result


def fetch_edges_direct(
    client: S2Client,
    cache_dir: Path,
    identifier: str,
    edge: str,
    max_edges: int,
    page_size: int,
) -> dict[str, Any]:
    path = edge_cache_path(cache_dir, identifier, edge)
    cached = read_json(path)
    if cached is not None and not cached.get("_error") and not client.refresh:
        return cached
    legacy = legacy_edge_cache(cache_dir, identifier, edge)
    if legacy is not None and not client.refresh:
        write_json(path, legacy)
        return legacy

    collected: list[Any] = []
    offset = 0
    paper_field = "citingPaper" if edge == "citations" else "citedPaper"
    edge_fields = ",".join(f"{paper_field}.{field}" for field in EDGE_FIELDS.split(","))
    while len(collected) < max_edges:
        limit = min(page_size, max_edges - len(collected))
        quoted = urllib.parse.quote(identifier, safe="")
        url = (
            f"{API}/paper/{quoted}/{edge}?fields={urllib.parse.quote(edge_fields, safe=',.')}"
            f"&limit={limit}&offset={offset}"
        )
        page_path = cache_dir / "pages" / f"{safe_name(identifier)}.{edge}.{offset}.json"
        page = client.request_json(url, page_path)
        if not isinstance(page, dict) or page.get("_error"):
            write_json(path, page if isinstance(page, dict) else {"_error": {"message": "non-object response"}})
            return page if isinstance(page, dict) else {"_error": {"message": "non-object response"}}
        data = page.get("data") or []
        collected.extend(data)
        write_json(path, {"offset": 0, "data": collected, "_partial": True})
        next_offset = page.get("next")
        if next_offset is None or not data:
            break
        offset = int(next_offset)
    result = {"offset": 0, "data": collected}
    write_json(path, result)
    return result


def edge_paper(item: dict[str, Any], edge: str) -> dict[str, Any]:
    key = "citingPaper" if edge == "citations" else "citedPaper"
    paper = item.get(key)
    return paper if isinstance(paper, dict) else {}


def best_url(paper: dict[str, Any]) -> str:
    external = paper.get("externalIds") or {}
    if external.get("ArXiv"):
        return f"https://arxiv.org/abs/{external['ArXiv']}"
    if external.get("DOI"):
        return f"https://doi.org/{external['DOI']}"
    return paper.get("url") or ""


def make_report(
    records: list[dict[str, Any]],
    *,
    since_year: int,
    top: int,
    include_abstract: bool,
) -> str:
    lines = [
        "# Semantic Scholar Citation and Reference Scan",
        "",
        f"- Generated: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"- Since year: {since_year}",
        f"- Seeds: {len(records)}",
        "",
        "## Seed Summary",
        "",
    ]
    candidates: dict[str, dict[str, Any]] = {}
    for record in records:
        seed = record["identifier"]
        paper = record.get("paper") or {}
        title = paper.get("title") or "UNKNOWN"
        lines.append(
            f"- `{seed}`: {title}; year={paper.get('year')}; "
            f"citations={paper.get('citationCount')}; references={paper.get('referenceCount')}; {best_url(paper)}"
        )
        for edge in ("citations", "references"):
            for item in (record.get(edge) or {}).get("data") or []:
                candidate = edge_paper(item, edge)
                if not candidate:
                    continue
                year = candidate.get("year")
                if year is not None and year < since_year:
                    continue
                key = candidate.get("paperId") or candidate.get("title") or best_url(candidate)
                if not key:
                    continue
                entry = candidates.setdefault(
                    key,
                    {
                        "paper": candidate,
                        "relations": [],
                        "score": 0,
                    },
                )
                relation = "cites seed" if edge == "citations" else "seed references"
                entry["relations"].append(f"{relation}: `{seed}`")
                entry["score"] = max(entry["score"], candidate.get("citationCount") or 0)

    lines.extend(["", "## Candidate Related Work", ""])
    ranked = sorted(
        candidates.values(),
        key=lambda item: ((item["paper"].get("year") or 0), item["score"]),
        reverse=True,
    )
    for item in ranked[:top]:
        paper = item["paper"]
        external = paper.get("externalIds") or {}
        arxiv = f" arXiv:{external['ArXiv']}" if external.get("ArXiv") else ""
        venue = f"; {paper.get('venue')}" if paper.get("venue") else ""
        relations = "; ".join(sorted(set(item["relations"]))[:4])
        lines.append(
            f"- {paper.get('year')} | cites={paper.get('citationCount') or 0} |"
            f"{arxiv}{venue} | {paper.get('title')} | {best_url(paper)} | {relations}"
        )
        if include_abstract and paper.get("abstract"):
            abstract = " ".join(str(paper["abstract"]).split())
            lines.append(f"  - Abstract: {abstract[:600]}")
    if not ranked:
        lines.append("- No candidates found in the requested window.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan Semantic Scholar citations and references with cache and 429 backoff.")
    parser.add_argument("files", nargs="*", type=Path, help="Markdown or text files from which to extract arXiv/DOI/S2 identifiers.")
    parser.add_argument("--id", action="append", default=[], help="Explicit paper identifier: arXiv:2401.00000, DOI:..., CorpusId:..., or S2 paperId.")
    parser.add_argument("--cache-dir", type=Path, default=Path(".tmp/semantic_citation_cache"))
    parser.add_argument("--lock-file", type=Path, default=Path(".tmp/semantic_citation_cache/api.lock"))
    parser.add_argument("--no-lock", action="store_true", help="Disable the cross-process API lock.")
    parser.add_argument("--out", type=Path, default=Path(".tmp/semantic_citation_report.md"))
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--since-year", type=int, default=dt.date.today().year - 1)
    parser.add_argument("--top", type=int, default=120)
    parser.add_argument("--max-citations", type=int, default=300)
    parser.add_argument("--max-references", type=int, default=200)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--min-delay", type=float, default=0.1)
    parser.add_argument("--max-delay", type=float, default=30.0, help="Maximum inter-request delay; capped at 30 seconds.")
    parser.add_argument("--delay-decrease", type=float, default=1.0, help="Linear delay decrease after each successful network request.")
    parser.add_argument("--max-retries", type=int, default=10)
    parser.add_argument("--refresh", action="store_true", help="Ignore successful cache entries and refetch.")
    parser.add_argument("--no-stale-on-error", action="store_true")
    parser.add_argument("--include-abstract", action="store_true")
    parser.add_argument("--direct-edges", action="store_true", help="Fetch citations/references directly from identifiers before paper metadata lookup.")
    parser.add_argument("--citations-only", action="store_true", help="Fetch only citation edges. Useful for completing legacy citation coverage.")
    args = parser.parse_args()

    identifiers = collect_identifiers(args.files, args.id)
    if not identifiers:
        print("No paper identifiers found. Pass files or --id.", file=sys.stderr)
        return 2

    print(f"Scanning {len(identifiers)} paper identifiers with cache {args.cache_dir}", flush=True)
    records: list[dict[str, Any]] = []
    with file_lock(args.lock_file, enabled=not args.no_lock):
        client = S2Client(
            min_delay=args.min_delay,
            max_delay=args.max_delay,
            delay_decrease=args.delay_decrease,
            max_retries=args.max_retries,
            refresh=args.refresh,
            stale_on_error=not args.no_stale_on_error,
        )
        for index, identifier in enumerate(identifiers, 1):
            print(f"[{index}/{len(identifiers)}] {identifier}", flush=True)
            record: dict[str, Any] = {"identifier": identifier}
            if args.direct_edges:
                record["citations"] = fetch_edges_direct(
                    client,
                    args.cache_dir,
                    identifier,
                    "citations",
                    args.max_citations,
                    args.page_size,
                )
                if not args.citations_only:
                    record["references"] = fetch_edges_direct(
                        client,
                        args.cache_dir,
                        identifier,
                        "references",
                        args.max_references,
                        args.page_size,
                    )
                if args.citations_only:
                    record["paper"] = {}
                else:
                    paper = fetch_paper(client, args.cache_dir, identifier)
                    record["paper"] = paper
            else:
                paper = fetch_paper(client, args.cache_dir, identifier)
                record["paper"] = paper
                paper_id = paper.get("paperId") if isinstance(paper, dict) else None
                if paper_id:
                    record["citations"] = fetch_edges(
                        client,
                        args.cache_dir,
                        identifier,
                        paper_id,
                        "citations",
                        args.max_citations,
                        args.page_size,
                    )
                    if not args.citations_only:
                        record["references"] = fetch_edges(
                            client,
                            args.cache_dir,
                            identifier,
                            paper_id,
                            "references",
                            args.max_references,
                            args.page_size,
                        )
            records.append(record)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        make_report(records, since_year=args.since_year, top=args.top, include_abstract=args.include_abstract),
        encoding="utf-8",
    )
    if args.json_out:
        write_json(args.json_out, records)
    print(f"Wrote {args.out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
