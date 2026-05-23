#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
CHECK_URLS = SCRIPT_DIR / "check_urls.py"


def run_git(args: list[str]) -> list[str]:
    result = subprocess.run(["git", *args], check=False, text=True, capture_output=True)
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def existing_markdown(paths: list[str]) -> list[Path]:
    seen: set[Path] = set()
    files: list[Path] = []
    for item in paths:
        path = Path(item)
        if path.suffix.lower() != ".md" or not path.is_file():
            continue
        key = path.resolve()
        if key in seen:
            continue
        seen.add(key)
        files.append(path)
    return files


def changed_markdown(base: str, include_untracked: bool) -> list[Path]:
    names: list[str] = []
    names.extend(run_git(["diff", "--name-only", "--diff-filter=ACMRTUXB", base, "--"]))
    names.extend(run_git(["diff", "--cached", "--name-only", "--diff-filter=ACMRTUXB", "--"]))
    if include_untracked:
        names.extend(run_git(["ls-files", "--others", "--exclude-standard"]))
    return existing_markdown(names)


def all_docs_markdown() -> list[Path]:
    files: list[Path] = []
    for pattern in ["README.md", "README.zh.md", "docs/en/*.md", "docs/zh/*.md"]:
        files.extend(sorted(Path.cwd().glob(pattern)))
    return [path for path in files if path.is_file()]


def write_noop_report(path: Path, files: list[Path]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# URL Accessibility Report",
        "",
        "No Markdown files selected for URL checking.",
        "",
        "## Candidate Files",
        "",
    ]
    if files:
        lines.extend(f"- {file}" for file in files)
    else:
        lines.append("- None.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run check_urls.py on changed Markdown files.")
    parser.add_argument("files", nargs="*", help="Extra Markdown files to check.")
    parser.add_argument("--base", default="HEAD", help="Git revision/base for changed-file discovery.")
    parser.add_argument("--no-untracked", action="store_true", help="Do not include untracked Markdown files.")
    parser.add_argument("--all-docs", action="store_true", help="Check README and docs Markdown files instead of git changes.")
    parser.add_argument("--out", type=Path, default=Path(".tmp/url_check_changed.md"))
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--cache-path", type=Path, default=Path(".tmp/landscape-maintainer/url-check-cache.json"))
    parser.add_argument("--cache-ttl-days", type=float, default=30.0)
    parser.add_argument("--refresh-cache", action="store_true", help="Ignore fresh cache entries and re-check URLs.")
    parser.add_argument("--no-cache", action="store_true", help="Disable reading and writing the URL check cache.")
    parser.add_argument("--fail-on-broken", action="store_true")
    parser.add_argument("--print-files", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = all_docs_markdown() if args.all_docs else changed_markdown(args.base, not args.no_untracked)
    files.extend(existing_markdown(args.files))
    files = existing_markdown([str(path) for path in files])

    if args.print_files:
        for path in files:
            print(path)
    if args.dry_run:
        return 0 if files else 1
    if not files:
        write_noop_report(args.out, files)
        print(f"Wrote {args.out}", flush=True)
        return 0

    cmd = [
        sys.executable,
        str(CHECK_URLS),
        "--out",
        str(args.out),
        "--timeout",
        str(args.timeout),
        "--workers",
        str(args.workers),
        "--cache-path",
        str(args.cache_path),
        "--cache-ttl-days",
        str(args.cache_ttl_days),
    ]
    if args.json_out:
        cmd.extend(["--json-out", str(args.json_out)])
    if args.refresh_cache:
        cmd.append("--refresh-cache")
    if args.no_cache:
        cmd.append("--no-cache")
    if args.fail_on_broken:
        cmd.append("--fail-on-broken")
    cmd.extend(str(path) for path in files)
    print(f"Checking URLs in {len(files)} Markdown files.", flush=True)
    return subprocess.run(cmd, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
