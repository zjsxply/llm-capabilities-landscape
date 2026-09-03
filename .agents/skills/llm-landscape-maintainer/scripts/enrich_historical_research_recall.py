#!/usr/bin/env python3
"""Attach cached Semantic Scholar evidence to a historical Research recall queue."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def identifiers(paper: dict) -> set[str]:
    result: set[str] = set()
    ext = paper.get("externalIds") or {}
    if ext.get("ArXiv"):
        result.add(f"arxiv:{ext['ArXiv']}")
    if ext.get("DOI"):
        result.add(f"doi:{str(ext['DOI']).lower()}")
    if paper.get("paperId"):
        result.add(f"s2:{str(paper['paperId']).lower()}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = json.loads(args.input.read_text(encoding="utf-8"))
    wanted = {str(row["identifier"]).lower(): row for row in rows}
    by_title = {norm(str(row.get("title") or "")): row for row in rows if row.get("title")}
    hits = 0
    for path in args.cache_dir.glob("papers/*.json"):
        try:
            paper = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        target = next((wanted[key] for key in identifiers(paper) if key in wanted), None)
        if target is None:
            target = by_title.get(norm(str(paper.get("title") or "")))
        if target is None or target.get("abstract"):
            continue
        target["abstract"] = paper.get("abstract") or ""
        target["year"] = paper.get("year")
        target["citation_count"] = paper.get("citationCount")
        target["cache_evidence"] = path.as_posix()
        hits += 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Rows: {len(rows)}; cached abstract matches: {hits}")


if __name__ == "__main__":
    main()
