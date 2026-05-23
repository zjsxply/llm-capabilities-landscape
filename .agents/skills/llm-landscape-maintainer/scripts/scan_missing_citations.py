#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from citation_coverage_audit import audit, default_markdown_files, expand_file_args, write_report


SCRIPT_DIR = Path(__file__).resolve().parent
SCANNER = SCRIPT_DIR / "semantic_scholar_citation_scan.py"


def write_lines(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find Markdown papers without citation edge cache, then run the Semantic Scholar scanner."
    )
    parser.add_argument("files", nargs="*", help="Markdown/text files or globs. Defaults to README and docs Markdown files.")
    parser.add_argument("--id", action="append", default=[], help="Explicit paper identifier to include.")
    parser.add_argument("--cache-dir", type=Path, default=Path(".tmp/semantic_citation_cache"))
    parser.add_argument("--coverage-out", type=Path, default=Path(".tmp/s2_citation_coverage.md"))
    parser.add_argument("--missing-out", type=Path, default=Path(".tmp/missing_s2_citation_ids.txt"))
    parser.add_argument("--out", type=Path, default=Path(".tmp/missing_s2_citation_report.md"))
    parser.add_argument("--json-out", type=Path, default=Path(".tmp/missing_s2_citation_records.json"))
    parser.add_argument("--max-citations", type=int, default=100)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--min-delay", type=float, default=0.1)
    parser.add_argument("--max-delay", type=float, default=30.0)
    parser.add_argument("--delay-decrease", type=float, default=1.0)
    parser.add_argument("--max-retries", type=int, default=6)
    parser.add_argument("--retry-errors", action="store_true", help="Also refetch cached API errors.")
    parser.add_argument("--retry-partials", action="store_true", help="Also refetch partial edge caches.")
    parser.add_argument("--refresh", action="store_true", help="Pass --refresh to the scanner for selected IDs.")
    parser.add_argument("--dry-run", action="store_true", help="Only write coverage and missing-ID files.")
    args = parser.parse_args()

    files = expand_file_args(args.files) if args.files else default_markdown_files(Path.cwd())
    identifiers, statuses, missing_ids = audit(
        files=files,
        direct_ids=args.id,
        cache_dir=args.cache_dir,
        edges=["citations"],
        retry_errors=args.retry_errors,
        retry_partials=args.retry_partials,
    )
    write_report(
        args.coverage_out,
        files=files,
        identifiers=identifiers,
        statuses=statuses,
        missing_ids=missing_ids,
        cache_dir=args.cache_dir,
    )
    write_lines(args.missing_out, missing_ids)
    print(f"Identifiers: {len(identifiers)}", flush=True)
    print(f"Need citation fetch: {len(missing_ids)}", flush=True)
    print(f"Wrote {args.coverage_out}", flush=True)
    print(f"Wrote {args.missing_out}", flush=True)

    if not missing_ids:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text("# Semantic Scholar Missing Citation Scan\n\nNo missing citation edges.\n", encoding="utf-8")
        print(f"Wrote {args.out}", flush=True)
        return 0
    if args.dry_run:
        return 1

    cmd = [
        sys.executable,
        str(SCANNER),
        "--direct-edges",
        "--citations-only",
        "--cache-dir",
        str(args.cache_dir),
        "--max-citations",
        str(args.max_citations),
        "--page-size",
        str(args.page_size),
        "--min-delay",
        str(args.min_delay),
        "--max-delay",
        str(args.max_delay),
        "--delay-decrease",
        str(args.delay_decrease),
        "--max-retries",
        str(args.max_retries),
        "--out",
        str(args.out),
        "--json-out",
        str(args.json_out),
    ]
    if args.refresh:
        cmd.append("--refresh")
    for identifier in missing_ids:
        cmd.extend(["--id", identifier])
    print("Running Semantic Scholar scanner for missing citation edges.", flush=True)
    return subprocess.run(cmd, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
