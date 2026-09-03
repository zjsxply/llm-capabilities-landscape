#!/usr/bin/env python3
"""Replace bilingual Markdown bullet TLDRs by an exact paper URL."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def load_rows(paths: list[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise SystemExit(f"Expected a JSON list: {path}")
        rows.extend(row for row in data if isinstance(row, dict))
    return rows


def paper_url(row: dict[str, Any]) -> str:
    value = str(row.get("url") or row.get("stable_url") or "").strip()
    identifier = str(row.get("identifier") or row.get("arxiv_id") or "").strip()
    if not value and re.fullmatch(r"arxiv:\d{4}\.\d{4,5}(?:v\d+)?", identifier, re.I):
        value = f"https://arxiv.org/abs/{re.sub(r'^arxiv:', '', identifier, flags=re.I)}"
    if not value and re.fullmatch(r"doi:.+", identifier, re.I):
        value = f"https://doi.org/{identifier.split(':', 1)[1]}"
    value = re.sub(r"/+$", "", value)
    if not re.fullmatch(r"https?://[^\s)]+", value, re.I):
        raise SystemExit(f"Invalid paper URL: {value!r}")
    return value


def rewrite(path: Path, rows: list[dict[str, Any]], *, language: str) -> int:
    key = "tldr_en" if language == "en" else "tldr_zh"
    separator = ": " if language == "en" else "："
    suffix = "." if language == "en" else "。"
    replacements = {paper_url(row): str(row.get(key) or "").strip().rstrip("。. ") for row in rows}
    missing_text = sorted(url for url, value in replacements.items() if not value)
    if missing_text:
        raise SystemExit(f"Missing {key} for: {missing_text}")

    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    hits = {url: 0 for url in replacements}
    for index, line in enumerate(lines):
        for url, text in replacements.items():
            link_match = re.search(r"\]\((https?://[^)]+)\)", line, re.I)
            if not link_match or link_match.group(1).casefold() != url.casefold():
                continue
            actual_url = link_match.group(1)
            match = re.match(rf"^(- \[[^]]+\]\({re.escape(actual_url)}\))\s*[:：]\s*.*$", line.rstrip("\n"), re.I)
            if not match:
                raise SystemExit(f"Malformed target bullet in {path}:{index + 1}")
            lines[index] = f"{match.group(1)}{separator}{text}{suffix}\n"
            hits[url] += 1
    invalid = {url: count for url, count in hits.items() if count != 1}
    if invalid:
        raise SystemExit(f"Expected one match per identifier in {path}: {invalid}")
    path.write_text("".join(lines), encoding="utf-8")
    return sum(hits.values())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--en-doc", type=Path, required=True)
    parser.add_argument("--zh-doc", type=Path, required=True)
    args = parser.parse_args()
    rows = load_rows(args.inputs)
    urls = [paper_url(row) for row in rows]
    if len(urls) != len(set(urls)):
        raise SystemExit("Duplicate paper URLs in rewrite inputs")
    en = rewrite(args.en_doc, rows, language="en")
    zh = rewrite(args.zh_doc, rows, language="zh")
    print(f"Rows: {len(rows)}")
    print(f"English replacements: {en}")
    print(f"Chinese replacements: {zh}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
