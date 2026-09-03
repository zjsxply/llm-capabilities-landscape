#!/usr/bin/env python3
"""Join canonical include decisions to source abstracts and write bounded QA packets."""

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
    lower = text.lower()
    if lower.startswith("arxiv:"):
        return "arXiv:" + re.sub(r"v\d+$", "", text.split(":", 1)[1], flags=re.I)
    if lower.startswith("doi:10.48550/arxiv."):
        match = re.fullmatch(r"doi:10\.48550/arxiv\.(\d{4}\.\d{4,5})(?:v\d+)?", text, re.I)
        if match:
            return "arXiv:" + match.group(1)
    if lower.startswith("doi:"):
        return "DOI:" + text.split(":", 1)[1].lower()
    return text


def index_unique(rows: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for row in rows:
        identifier = canonical(row.get("identifier"))
        if not identifier:
            raise SystemExit(f"{label} contains a row without identifier")
        if identifier in indexed:
            raise SystemExit(f"{label} contains duplicate identifier: {identifier}")
        indexed[identifier] = row
    return indexed


def load_review_chunks(directory: Path) -> list[dict[str, Any]]:
    paths = sorted(directory.glob("chunk-[0-9][0-9][0-9].json"))
    if not paths:
        raise SystemExit(f"No review chunks found in {directory}")
    rows: list[dict[str, Any]] = []
    for path in paths:
        rows.extend(read_list(path))
    return rows


def write_list(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--review-dir", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--chunk-dir", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--chunk-size", type=int, default=15)
    parser.add_argument(
        "--state-field",
        default="decision",
        help="Review field containing terminal include/reject state (default: decision).",
    )
    args = parser.parse_args()
    if args.chunk_size < 1:
        raise SystemExit("--chunk-size must be positive")

    candidates = read_list(args.candidates)
    reviews = load_review_chunks(args.review_dir)
    candidate_index = index_unique(candidates, "candidates")
    review_index = index_unique(reviews, "reviews")
    if set(candidate_index) != set(review_index):
        raise SystemExit(
            "Candidate/review coverage mismatch: "
            f"missing={sorted(set(candidate_index) - set(review_index))[:20]} "
            f"extra={sorted(set(review_index) - set(candidate_index))[:20]}"
        )

    invalid = {
        identifier: row.get(args.state_field)
        for identifier, row in review_index.items()
        if str(row.get(args.state_field) or "").lower() not in {"include", "reject"}
    }
    if invalid:
        raise SystemExit(f"Reviews contain nonterminal decisions: {list(invalid.items())[:20]}")

    enriched: list[dict[str, Any]] = []
    for candidate in candidates:
        identifier = canonical(candidate.get("identifier"))
        review = review_index[identifier]
        if str(review.get(args.state_field) or "").lower() != "include":
            continue
        row = dict(candidate)
        row.update(review)
        row["identifier"] = identifier
        row["source_abstract"] = str(candidate.get("abstract") or "").strip()
        enriched.append(row)

    write_list(args.out, enriched)
    args.chunk_dir.mkdir(parents=True, exist_ok=True)
    for old in args.chunk_dir.glob("chunk-[0-9][0-9][0-9].json"):
        old.unlink()
    for index, start in enumerate(range(0, len(enriched), args.chunk_size), start=1):
        write_list(args.chunk_dir / f"chunk-{index:03d}.json", enriched[start : start + args.chunk_size])

    sections = Counter(str(row.get("section") or "<missing>") for row in enriched)
    with_abstract = sum(bool(row.get("source_abstract")) for row in enriched)
    summary = [
        "# Parent QA Packet Preparation",
        "",
        f"- Candidates: {len(candidates)}",
        f"- Terminal reviews: {len(reviews)}",
        f"- Proposed includes: {len(enriched)}",
        f"- Proposed includes with source abstracts: {with_abstract}",
        f"- Proposed includes without source abstracts: {len(enriched) - with_abstract}",
        f"- QA chunks: {(len(enriched) + args.chunk_size - 1) // args.chunk_size}",
        "",
        "## Proposed Includes by Section",
        "",
        *[f"- {section}: {count}" for section, count in sorted(sections.items())],
    ]
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text("\n".join(summary) + "\n", encoding="utf-8")
    print(f"Candidates: {len(candidates)}")
    print(f"Terminal reviews: {len(reviews)}")
    print(f"Proposed includes: {len(enriched)}")
    print(f"With source abstracts: {with_abstract}")
    print(f"QA chunks: {(len(enriched) + args.chunk_size - 1) // args.chunk_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
