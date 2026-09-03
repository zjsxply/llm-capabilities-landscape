#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from landscape_paths import default_markdown_files as shared_default_markdown_files
from landscape_paths import expand_markdown_args


SCRIPT_DIR = Path(__file__).resolve().parent
S2_SCRIPT = SCRIPT_DIR / "semantic_scholar_citation_scan.py"


def load_s2_module():
    spec = importlib.util.spec_from_file_location("semantic_scholar_citation_scan", S2_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {S2_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


S2 = load_s2_module()


@dataclass(frozen=True)
class EdgeStatus:
    identifier: str
    edge: str
    status: str
    path: Path | None
    count: int | None
    fetched_at: dt.datetime | None = None
    message: str = ""

    @property
    def needs_fetch(self) -> bool:
        return self.status in {"missing", "malformed", "partial", "error", "stale"}


def repo_root() -> Path:
    return Path.cwd()


def default_markdown_files(root: Path) -> list[Path]:
    return shared_default_markdown_files(root)


def expand_file_args(items: list[str]) -> list[Path]:
    return expand_markdown_args(items, default_to_docs=False)


def read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return "__MALFORMED__"


def parse_timestamp(value: Any) -> dt.datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip()
    if text.endswith("Z"):
        text = f"{text[:-1]}+00:00"
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def cache_fetched_at(path: Path, data: dict[str, Any]) -> dt.datetime | None:
    meta = data.get("_meta")
    if isinstance(meta, dict):
        fetched_at = parse_timestamp(meta.get("fetched_at"))
        if fetched_at is not None:
            return fetched_at
    try:
        return dt.datetime.fromtimestamp(path.stat().st_mtime, dt.timezone.utc)
    except FileNotFoundError:
        return None


def edge_path(cache_dir: Path, identifier: str, edge: str) -> Path:
    return cache_dir / "edges" / f"{S2.safe_name(identifier)}.{edge}.json"


def legacy_edge_path(cache_dir: Path, identifier: str, edge: str) -> Path | None:
    if edge != "citations" or not identifier.lower().startswith("arxiv:"):
        return None
    arxiv_id = identifier.split(":", 1)[1]
    return cache_dir / "s2_citation_cache" / f"{arxiv_id}.json"


def classify_payload(path: Path, data: Any, stale_days: float | None) -> tuple[str, int | None, dt.datetime | None, str]:
    if data == "__MALFORMED__":
        return "malformed", None, None, "JSON decode failed"
    if data is None:
        return "missing", None, None, ""
    if not isinstance(data, dict):
        return "malformed", None, None, f"Expected object, got {type(data).__name__}"
    if data.get("_error"):
        error = data.get("_error")
        return "error", None, cache_fetched_at(path, data), json.dumps(error, ensure_ascii=False, sort_keys=True)
    rows = data.get("data")
    if not isinstance(rows, list):
        return "malformed", None, cache_fetched_at(path, data), "Missing list field: data"
    if data.get("_partial"):
        return "partial", len(rows), cache_fetched_at(path, data), "Partial cache"
    fetched_at = cache_fetched_at(path, data)
    if stale_days is not None:
        if fetched_at is None:
            return "stale", len(rows), fetched_at, "Missing fetched_at metadata and file mtime"
        age = dt.datetime.now(dt.timezone.utc) - fetched_at
        if age >= dt.timedelta(days=stale_days):
            return "stale", len(rows), fetched_at, f"Fetched {age.days} days ago"
    return "ok", len(rows), fetched_at, ""


def classify_edge(cache_dir: Path, identifier: str, edge: str, stale_days: float | None) -> EdgeStatus:
    canonical = edge_path(cache_dir, identifier, edge)
    data = read_json(canonical)
    status, count, fetched_at, message = classify_payload(canonical, data, stale_days)
    if status != "missing":
        return EdgeStatus(identifier, edge, status, canonical, count, fetched_at, message)

    legacy = legacy_edge_path(cache_dir, identifier, edge)
    if legacy is None:
        return EdgeStatus(identifier, edge, "missing", canonical, None)
    legacy_data = read_json(legacy)
    legacy_status, legacy_count, legacy_fetched_at, legacy_message = classify_payload(legacy, legacy_data, stale_days)
    if legacy_status == "missing":
        return EdgeStatus(identifier, edge, "missing", canonical, None)
    return EdgeStatus(
        identifier,
        edge,
        f"legacy_{legacy_status}",
        legacy,
        legacy_count,
        legacy_fetched_at,
        legacy_message,
    )


def collect_identifiers(files: list[Path], direct_ids: list[str]) -> list[str]:
    return S2.collect_identifiers(files, direct_ids)


def audit(
    *,
    files: list[Path],
    direct_ids: list[str],
    cache_dir: Path,
    edges: list[str],
    retry_errors: bool,
    retry_partials: bool,
    stale_days: float | None,
) -> tuple[list[str], list[EdgeStatus], list[str]]:
    identifiers = collect_identifiers(files, direct_ids)
    statuses: list[EdgeStatus] = []
    missing_ids: list[str] = []
    for identifier in identifiers:
        edge_statuses = [classify_edge(cache_dir, identifier, edge, stale_days) for edge in edges]
        statuses.extend(edge_statuses)
        should_fetch = False
        for item in edge_statuses:
            if item.status == "missing":
                should_fetch = True
            elif item.status.endswith("stale"):
                should_fetch = True
            elif retry_errors and item.status.endswith("error"):
                should_fetch = True
            elif retry_partials and item.status.endswith("partial"):
                should_fetch = True
            elif item.status == "malformed":
                should_fetch = True
        if should_fetch:
            missing_ids.append(identifier)
    return identifiers, statuses, missing_ids


def write_lines(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(
    path: Path,
    *,
    files: list[Path],
    identifiers: list[str],
    statuses: list[EdgeStatus],
    missing_ids: list[str],
    cache_dir: Path,
    stale_days: float | None,
) -> None:
    counts: dict[str, int] = {}
    for item in statuses:
        counts[item.status] = counts.get(item.status, 0) + 1

    lines = [
        "# Semantic Scholar Citation Coverage Audit",
        "",
        f"- Generated: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"- Files: {len(files)}",
        f"- Unique identifiers: {len(identifiers)}",
        f"- Edge records checked: {len(statuses)}",
        f"- Cache directory: `{cache_dir}`",
        f"- Stale threshold days: {stale_days if stale_days is not None else 'disabled'}",
        f"- Identifiers needing fetch: {len(missing_ids)}",
        "",
        "## Status Counts",
        "",
    ]
    for status in sorted(counts):
        lines.append(f"- {status}: {counts[status]}")
    if not counts:
        lines.append("- None.")

    lines.extend(["", "## Needs Fetch", ""])
    if not missing_ids:
        lines.append("- None.")
    else:
        for identifier in missing_ids:
            lines.append(f"- `{identifier}`")

    lines.extend(["", "## Non-OK Edge Details", ""])
    details = [item for item in statuses if item.status != "ok"]
    if not details:
        lines.append("- None.")
    else:
        for item in details:
            count = "" if item.count is None else f"; count={item.count}"
            path_text = "" if item.path is None else f"; path={item.path}"
            fetched_at = "" if item.fetched_at is None else f"; fetched_at={item.fetched_at.isoformat(timespec='seconds')}"
            message = "" if not item.message else f"; {item.message}"
            lines.append(f"- `{item.identifier}` {item.edge}: {item.status}{count}{path_text}{fetched_at}{message}")

    write_lines(path, lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Semantic Scholar citation/reference cache coverage for Markdown files.")
    parser.add_argument("files", nargs="*", help="Markdown/text files or globs. Defaults to README and docs Markdown files.")
    parser.add_argument("--id", action="append", default=[], help="Explicit paper identifier to include.")
    parser.add_argument(
        "--ids-file",
        type=Path,
        help="Read one explicit arXiv/DOI/S2 identifier per line; do not parse this file as Markdown.",
    )
    parser.add_argument("--cache-dir", type=Path, default=Path(".tmp/semantic_citation_cache"))
    parser.add_argument("--edge", choices=["citations", "references"], action="append")
    parser.add_argument("--retry-errors", action="store_true", help="Treat cached API errors as needing fetch.")
    parser.add_argument("--retry-partials", action="store_true", help="Treat partial edge caches as needing fetch.")
    parser.add_argument(
        "--stale-days",
        type=float,
        help="Treat otherwise valid edge caches whose fetched_at metadata, or legacy file mtime, is at least this many days old as needing fetch.",
    )
    parser.add_argument("--out", type=Path, default=Path(".tmp/s2_citation_coverage.md"))
    parser.add_argument("--missing-out", type=Path, default=Path(".tmp/missing_s2_citation_ids.txt"))
    parser.add_argument("--args-out", type=Path, default=Path(".tmp/missing_s2_args.txt"))
    args = parser.parse_args()

    direct_ids = list(args.id)
    if args.ids_file:
        direct_ids.extend(
            line.strip()
            for line in args.ids_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )

    # An explicit ID audit is intentionally bounded. Scanning every Markdown
    # file here is both surprising and expensive for large split-tree docs.
    files = expand_file_args(args.files) if args.files else ([] if direct_ids else default_markdown_files(repo_root()))
    identifiers, statuses, missing_ids = audit(
        files=files,
        direct_ids=direct_ids,
        cache_dir=args.cache_dir,
        edges=list(dict.fromkeys(args.edge or ["citations", "references"])),
        retry_errors=args.retry_errors,
        retry_partials=args.retry_partials,
        stale_days=args.stale_days,
    )

    write_report(
        args.out,
        files=files,
        identifiers=identifiers,
        statuses=statuses,
        missing_ids=missing_ids,
        cache_dir=args.cache_dir,
        stale_days=args.stale_days,
    )
    write_lines(args.missing_out, missing_ids)
    write_lines(args.args_out, [f"--id {identifier}" for identifier in missing_ids])

    print(f"Identifiers: {len(identifiers)}", flush=True)
    print(f"Need fetch: {len(missing_ids)}", flush=True)
    print(f"Wrote {args.out}", flush=True)
    print(f"Wrote {args.missing_out}", flush=True)
    return 1 if missing_ids else 0


if __name__ == "__main__":
    raise SystemExit(main())
