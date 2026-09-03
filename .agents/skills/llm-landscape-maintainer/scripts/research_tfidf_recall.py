#!/usr/bin/env python3
"""Recall citation candidates lexically similar to existing Research entries."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


TOKEN_RE = re.compile(r"[a-z][a-z0-9-]{2,}")
STOP = {
    "the", "and", "for", "with", "from", "that", "this", "into", "using", "use",
    "uses", "used", "their", "its", "are", "was", "were", "has", "have", "had",
    "paper", "work", "study", "method", "methods", "model", "models", "results",
    "approach", "propose", "proposes", "introduce", "introduces", "show", "shows",
    "based", "across", "than", "also", "can", "our", "these", "such", "which",
    "via", "over", "between", "more", "new", "large", "data", "analysis",
}


def tokens(text: str) -> list[str]:
    return [token for token in TOKEN_RE.findall(text.lower()) if token not in STOP]


def load_rows(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"Expected a JSON list: {path}")
    return [row for row in data if isinstance(row, dict)]


def title_from_bullet(line: str) -> str:
    match = re.match(r"^- \[([^]]+)\]", line)
    return match.group(1) if match else ""


def vector(text: str, idf: dict[str, float]) -> dict[str, float]:
    counts = Counter(tokens(text))
    values = {term: (1.0 + math.log(count)) * idf.get(term, 0.0) for term, count in counts.items()}
    norm = math.sqrt(sum(value * value for value in values.values()))
    return {term: value / norm for term, value in values.items() if norm and value}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--decisions", type=Path, action="append", default=[])
    parser.add_argument("--reference", type=Path, action="append", required=True)
    parser.add_argument("--top", type=int, default=200)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    references: list[tuple[str, str]] = []
    for path in args.reference:
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("- ["):
                references.append((title_from_bullet(line), line))
    if not references:
        raise SystemExit("No reference bullets found")

    document_frequency: Counter[str] = Counter()
    for _, text in references:
        document_frequency.update(set(tokens(text)))
    count = len(references)
    idf = {term: math.log((count + 1) / (freq + 1)) + 1.0 for term, freq in document_frequency.items()}

    ref_vectors = [vector(text, idf) for _, text in references]
    postings: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for index, values in enumerate(ref_vectors):
        for term, value in values.items():
            postings[term].append((index, value))

    excluded: set[str] = set()
    for path in args.decisions:
        for row in load_rows(path):
            if str(row.get("decision") or "").lower() == "include":
                excluded.add(str(row.get("identifier") or ""))

    recalled: list[dict[str, Any]] = []
    for row in load_rows(args.candidates):
        identifier = str(row.get("identifier") or "")
        if not identifier or identifier in excluded:
            continue
        text = f"{row.get('title') or ''} {row.get('abstract') or ''}"
        candidate = vector(text, idf)
        scores: dict[int, float] = defaultdict(float)
        for term, weight in candidate.items():
            for index, ref_weight in postings.get(term, []):
                scores[index] += weight * ref_weight
        if not scores:
            continue
        nearest, score = max(scores.items(), key=lambda item: item[1])
        enriched = dict(row)
        enriched["similarity_score"] = round(score, 6)
        enriched["nearest_existing_title"] = references[nearest][0]
        recalled.append(enriched)

    recalled.sort(
        key=lambda row: (
            float(row.get("similarity_score") or 0),
            int(row.get("seedCount") or 0),
            int(row.get("citationCount") or 0),
        ),
        reverse=True,
    )
    recalled = recalled[: max(0, args.top)]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(recalled, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Reference bullets: {len(references)}")
    print(f"Excluded title includes: {len(excluded)}")
    print(f"Recalled candidates: {len(recalled)}")
    if recalled:
        print(f"Score range: {recalled[-1]['similarity_score']:.6f}..{recalled[0]['similarity_score']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
