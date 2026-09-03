#!/usr/bin/env python3
"""Merge terminal rejection-recall decisions into canonical review chunks."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


def read_list(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise SystemExit(f"Expected a JSON array of objects: {path}")
    return data


def canonical(value: Any) -> str:
    text = str(value or "").strip()
    if text.lower().startswith("arxiv:"):
        return "arXiv:" + re.sub(r"v\d+$", "", text.split(":", 1)[1], flags=re.I)
    if text.lower().startswith("doi:"):
        return "DOI:" + text.split(":", 1)[1].lower()
    return text


def index_unique(rows: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        identifier = canonical(row.get("identifier"))
        if not identifier:
            raise SystemExit(f"{label} row lacks identifier")
        if identifier in result:
            raise SystemExit(f"{label} contains duplicate identifier: {identifier}")
        result[identifier] = row
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-dir", type=Path, required=True)
    parser.add_argument("--recall-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    review_paths = sorted(args.review_dir.glob("chunk-[0-9][0-9][0-9].json"))
    recall_paths = sorted(args.recall_dir.glob("chunk-[0-9][0-9][0-9].json"))
    if not review_paths or not recall_paths:
        raise SystemExit("Review and recall directories must both contain chunk JSON files")
    review_chunks = [(path, read_list(path)) for path in review_paths]
    reviews = [row for _, chunk in review_chunks for row in chunk]
    recalls = [row for path in recall_paths for row in read_list(path)]
    review_index = index_unique(reviews, "reviews")
    recall_index = index_unique(recalls, "recall")
    rejected = {
        identifier
        for identifier, row in review_index.items()
        if str(row.get("decision") or "").lower() == "reject"
    }
    if set(recall_index) != rejected:
        raise SystemExit(
            f"Recall coverage mismatch: missing={sorted(rejected - set(recall_index))[:20]} "
            f"extra={sorted(set(recall_index) - rejected)[:20]}"
        )
    invalid = {
        identifier: str(row.get("decision") or "")
        for identifier, row in recall_index.items()
        if str(row.get("decision") or "").lower() not in {"include", "reject"}
    }
    if invalid:
        raise SystemExit(f"Recall decisions must be terminal include/reject: {list(invalid.items())[:20]}")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for old in args.out_dir.glob("chunk-[0-9][0-9][0-9].json"):
        old.unlink()
    counts: Counter[str] = Counter()
    for path, chunk in review_chunks:
        output: list[dict[str, Any]] = []
        for original in chunk:
            identifier = canonical(original.get("identifier"))
            row = dict(original)
            if identifier in recall_index:
                recalled = recall_index[identifier]
                for field, value in recalled.items():
                    if value not in (None, ""):
                        row[field] = value
            decision = str(row.get("decision") or "").lower()
            if decision not in {"include", "reject"}:
                raise SystemExit(f"Canonical row is nonterminal: {identifier}: {decision}")
            counts[decision] += 1
            output.append(row)
        (args.out_dir / path.name).write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    recovered = sum(
        str(row.get("decision") or "").lower() == "include" for row in recall_index.values()
    )
    report = [
        "# Rejection Recall Merge",
        "",
        f"- Initial reviews: {len(reviews)}",
        f"- Initial rejects covered: {len(rejected)}",
        f"- Recovered includes: {recovered}",
        f"- Canonical includes: {counts['include']}",
        f"- Canonical rejects: {counts['reject']}",
        "- Deferred: 0",
    ]
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"reviews: {len(reviews)}")
    print(f"recall coverage: {len(rejected)}")
    print(f"recovered includes: {recovered}")
    print(f"canonical include: {counts['include']}")
    print(f"canonical reject: {counts['reject']}")
    print("deferred: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
