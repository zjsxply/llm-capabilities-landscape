#!/usr/bin/env python3
"""Apply parent taxonomy QA decisions to the abstract-backed inclusion chunk."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SECTION_FILES = {
    "leaderboard": "01-leaderboard.md",
    "survey": "02-survey.md",
    "bench": "03-bench.md",
    "model": "04-model.md",
    "agent harness": "05-agent-harness.md",
    "skill": "06-skill.md",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical(value: str) -> str:
    value = str(value or "").strip()
    if value.lower().startswith("arxiv:"):
        value = "arXiv:" + value.split(":", 1)[1]
        while value.lower().endswith(tuple(f"v{i}" for i in range(1, 10))):
            value = value[:-2]
        return value
    match = re.match(r"^doi:10\.48550/arxiv\.(\d{4}\.\d{4,5})$", value, re.I)
    if match:
        return "arXiv:" + match.group(1)
    if value.lower().startswith("doi:"):
        return "DOI:" + value.split(":", 1)[1].lower()
    return value


def replace_tldr(bullet: str, tldr: str, separator: str) -> str:
    match = re.match(r"^(- \[[^\]]+\]\([^)]+\))[:：].*$", bullet.strip())
    if not match:
        raise SystemExit(f"Cannot replace TLDR in malformed bullet: {bullet}")
    text = re.sub(r"\s+", " ", tldr.strip()).rstrip("。. ")
    return f"{match.group(1)}{separator} {text}{'。' if separator == '：' else '.'}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--qa", type=Path, action="append", default=[])
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    qa: dict[str, dict[str, Any]] = {}
    for path in args.qa:
        rows = load(path)
        if not isinstance(rows, list):
            continue
        for row in rows:
            if isinstance(row, dict) and row.get("identifier"):
                qa[canonical(row["identifier"])] = row

    output: list[dict[str, Any]] = []
    for raw in load(args.input):
        if not isinstance(raw, dict) or not raw.get("identifier"):
            continue
        row = dict(raw)
        key = canonical(row["identifier"])
        review = qa.get(key)
        if review:
            action = str(review.get("action") or "keep").lower()
            if action == "reject":
                continue
            section = str(review.get("section") or row.get("section") or "").strip()
            if action == "reclassify" and section:
                row["section"] = section
                row["target_doc"] = review.get("target_doc") or (
                    f"docs/en/03-downstream-applications/02-research/"
                    f"{SECTION_FILES[section.lower()]}"
                )
            if review.get("reason_en"):
                row["reason"] = review["reason_en"]
            if review.get("tldr_en"):
                row["suggested_english_bullet"] = replace_tldr(
                    str(row.get("suggested_english_bullet") or ""), str(review["tldr_en"]), ":"
                )
            if review.get("tldr_zh"):
                row["suggested_chinese_bullet"] = replace_tldr(
                    str(row.get("suggested_chinese_bullet") or ""), str(review["tldr_zh"]), "："
                )
        row["identifier"] = key
        output.append(row)

    output.sort(key=lambda row: (str(row.get("target_doc")), int(row.get("rank") or 10**9), str(row.get("identifier"))))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Input includes: {len(load(args.input))}")
    print(f"QA decisions: {len(qa)}")
    print(f"Final includes: {len(output)}")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
