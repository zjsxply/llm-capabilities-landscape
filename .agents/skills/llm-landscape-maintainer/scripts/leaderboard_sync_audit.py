#!/usr/bin/env python3
"""Audit benchmark rows whose explicit leaderboard links are missing from paired leaderboard pages."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
LEADERBOARD_LABEL_TERMS = (
    "leaderboard",
    "scoreboard",
    "arena/leaderboard",
    "browsergym leaderboard",
    "agentbeats leaderboard",
    "codesota leaderboard",
    "carla leaderboard",
    "deep research sota",
    "hal long-horizon tracks",
    "project page and leaderboard",
)
LEADERBOARD_URL_MARKERS = (
    "leaderboard",
    "/rank",
    "/scores",
)


@dataclass(frozen=True)
class Finding:
    bench_file: Path
    line_no: int
    label: str
    url: str
    line: str
    leaderboard_file: Path


@dataclass(frozen=True)
class ReviewCandidate:
    bench_file: Path
    line_no: int
    title: str
    url: str
    line: str
    leaderboard_file: Path


def markdown_links(text: str) -> list[tuple[str, str]]:
    return LINK_RE.findall(text)


def file_urls(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    return {url for _label, url in markdown_links(path.read_text(encoding="utf-8", errors="ignore"))}


def is_explicit_leaderboard_link(label: str, url: str) -> bool:
    label_lower = label.lower()
    url_lower = url.lower()
    return any(term in label_lower for term in LEADERBOARD_LABEL_TERMS) or any(
        marker in url_lower for marker in LEADERBOARD_URL_MARKERS
    )


def iter_bench_files(root: Path, paths: list[Path]) -> list[Path]:
    if paths:
        candidates: list[Path] = []
        for path in paths:
            if path.is_dir():
                candidates.extend(path.rglob("03-bench.md"))
            elif path.name == "03-bench.md":
                candidates.append(path)
            elif path.is_file():
                continue
        return sorted(set(candidates))
    return sorted((root / "docs/en").rglob("03-bench.md"))


def audit(root: Path, paths: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for bench_file in iter_bench_files(root, paths):
        leaderboard_file = bench_file.with_name("01-leaderboard.md")
        if not leaderboard_file.is_file():
            continue
        leaderboard_urls = file_urls(leaderboard_file)
        for line_no, line in enumerate(bench_file.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            links = markdown_links(line)
            # The first link is normally the paper or benchmark entry itself. Audit secondary artifact links.
            for label, url in links[1:]:
                if not is_explicit_leaderboard_link(label, url):
                    continue
                if url in leaderboard_urls:
                    continue
                findings.append(
                    Finding(
                        bench_file=bench_file,
                        line_no=line_no,
                        label=label,
                        url=url,
                        line=line,
                        leaderboard_file=leaderboard_file,
                    )
                )
    return findings


def normalized_key(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def primary_title_review(root: Path, paths: list[Path]) -> list[ReviewCandidate]:
    """Return noisy title-level candidates for manual review.

    This catches cases where the benchmark row itself is named "Leaderboard" or
    "Index" but does not expose a secondary leaderboard URL. Many hits are false
    positives because "index" can mean a metric and "leaderboard" can be only
    the object of a meta-evaluation paper.
    """
    title_terms = ("leaderboard", "index", "scoreboard", "sota")
    candidates: list[ReviewCandidate] = []
    for bench_file in iter_bench_files(root, paths):
        leaderboard_file = bench_file.with_name("01-leaderboard.md")
        if not leaderboard_file.is_file():
            continue
        leaderboard_text = leaderboard_file.read_text(encoding="utf-8", errors="ignore").lower()
        for line_no, line in enumerate(bench_file.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            links = markdown_links(line)
            if not links:
                continue
            title, url = links[0]
            if not any(term in title.lower() for term in title_terms):
                continue
            secondary = " ".join(f"{label} {link}" for label, link in links[1:]).lower()
            if any(term in secondary for term in ("leaderboard", "scoreboard", "sota", "results")):
                continue
            if any("leaderboard" in link.lower() or "/rank" in link.lower() or "/scores" in link.lower() for _label, link in links[1:]):
                continue
            key = normalized_key(title).split("  ")[0].strip()
            first_clause = normalized_key(title.split(":", 1)[0])
            if url.lower() in leaderboard_text or (first_clause and first_clause in leaderboard_text):
                continue
            candidates.append(
                ReviewCandidate(
                    bench_file=bench_file,
                    line_no=line_no,
                    title=title,
                    url=url,
                    line=line,
                    leaderboard_file=leaderboard_file,
                )
            )
    return candidates


def print_markdown(findings: list[Finding]) -> None:
    print(f"# Leaderboard Sync Audit\n")
    print(f"Findings: {len(findings)}\n")
    for finding in findings:
        print(f"## {finding.bench_file}:{finding.line_no}")
        print(f"- Missing from: `{finding.leaderboard_file}`")
        print(f"- Link: [{finding.label}]({finding.url})")
        print(f"- Row: `{finding.line}`\n")


def print_review_candidates(candidates: list[ReviewCandidate]) -> None:
    print(f"# Primary Title Leaderboard/Index Review\n")
    print(f"Candidates: {len(candidates)}\n")
    for candidate in candidates:
        print(f"## {candidate.bench_file}:{candidate.line_no}")
        print(f"- Candidate leaderboard file: `{candidate.leaderboard_file}`")
        print(f"- Title: [{candidate.title}]({candidate.url})")
        print(f"- Row: `{candidate.line}`\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Optional docs/en roots or 03-bench.md files.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root.")
    parser.add_argument("--no-fail", action="store_true", help="Return 0 even if findings are present.")
    parser.add_argument(
        "--primary-title-review",
        action="store_true",
        help="Print noisy manual-review candidates whose primary title contains Leaderboard, Index, Scoreboard, or SOTA.",
    )
    args = parser.parse_args()

    findings = audit(args.root, args.paths)
    print_markdown(findings)
    if args.primary_title_review:
        print()
        print_review_candidates(primary_title_review(args.root, args.paths))
    return 0 if args.no_fail or not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
