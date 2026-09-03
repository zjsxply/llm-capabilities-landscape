#!/usr/bin/env python3
"""Inventory paper URLs in famou research-landscape and compare them with docs.

This is intentionally an inventory tool, not an inclusion classifier.  It
preserves every source occurrence, extracts one stable paper identifier per
URL, and reports whether the identifier already occurs anywhere in the
landscape.  Parent review must still decide the destination category from the
paper artifact and abstract.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ARXIV_URL_RE = re.compile(r"https?://(?:export\.)?arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v[0-9]+)?(?:\.pdf)?", re.I)
ARXIV_TEXT_RE = re.compile(r"\barXiv[: ]+([0-9]{4}\.[0-9]{4,5})(?:v[0-9]+)?\b", re.I)
DOI_URL_RE = re.compile(r"https?://(?:dx\.)?doi\.org/([^\s<\]}\"']+)", re.I)
DOI_TEXT_RE = re.compile(r"\bdoi:\s*(10\.\d{4,9}/[^\s<\]}\"']+)", re.I)


def clean_doi(value: str) -> str:
    value = unquote(value)
    match = re.match(r"(10\.\d{4,9}/[A-Za-z0-9][A-Za-z0-9._;()/:+\-]*)", value)
    if match:
        value = match.group(1)
    value = value.rstrip(".,;:")
    while value.endswith(")") and value.count(")") > value.count("("):
        value = value[:-1]
    return value.lower()


def records_for_text(text: str, path: str, line_no: int) -> list[dict[str, str]]:
    found: dict[str, str] = {}
    for match in ARXIV_URL_RE.finditer(text):
        found[f"arXiv:{match.group(1)}"] = match.group(0)
    for match in ARXIV_TEXT_RE.finditer(text):
        found.setdefault(f"arXiv:{match.group(1)}", match.group(0))
    for match in DOI_URL_RE.finditer(text):
        doi = clean_doi(match.group(1))
        found[f"DOI:{doi}"] = match.group(0)
    for match in DOI_TEXT_RE.finditer(text):
        doi = clean_doi(match.group(1))
        found.setdefault(f"DOI:{doi}", match.group(0))
    return [
        {"identifier": identifier, "source_file": path, "source_line": str(line_no), "raw": raw}
        for identifier, raw in sorted(found.items())
    ]


def identifiers_in_docs(root: Path) -> set[str]:
    result: set[str] = set()
    for path in root.rglob("*.md"):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        for line_no, line in enumerate(lines, 1):
            result.update(item["identifier"] for item in records_for_text(line, str(path), line_no))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("docs", type=Path)
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--missing-out", type=Path, required=True)
    args = parser.parse_args()

    rows: list[dict[str, str | bool]] = []
    for path in sorted(args.source.rglob("*.md")):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        for line_no, line in enumerate(lines, 1):
            rows.extend(
                {**item, "in_docs": False}
                for item in records_for_text(line, str(path), line_no)
            )

    present = identifiers_in_docs(args.docs)
    unique: dict[str, dict[str, object]] = {}
    for row in rows:
        identifier = str(row["identifier"])
        item = unique.setdefault(
            identifier,
            {"identifier": identifier, "occurrences": [], "in_docs": identifier in present},
        )
        item["occurrences"].append({key: row[key] for key in ("source_file", "source_line", "raw")})

    output = sorted(unique.values(), key=lambda item: str(item["identifier"]).lower())
    missing = [item for item in output if not item["in_docs"]]
    for destination in (args.json_out, args.missing_out):
        destination.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.missing_out.write_text(json.dumps(missing, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"unique source identifiers: {len(output)}")
    print(f"already present anywhere in docs: {len(output) - len(missing)}")
    print(f"missing anywhere in docs: {len(missing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
