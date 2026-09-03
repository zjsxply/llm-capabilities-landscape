#!/usr/bin/env python3
"""Build a high-signal Research recall queue from papers covered in other topics.

The checked-paper registry is global.  A paper already included under a core
capability is not therefore covered by downstream Research.  This script uses
the *target documentation paths* as the duplicate key, preserving the source
topic as provenance for a parent evidence review.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


RESEARCH_PATH = "/03-downstream-applications/02-research/"

# Require a task artifact, not merely the word "research" in a title.
AXES: list[tuple[str, re.Pattern[str]]] = [
    ("scholarly-production", re.compile(
        r"\b(peer[ -]?review|reviewer|rebuttal|manuscript|scholarly|academic paper|"
        r"research[- ]quality|research assessment|research evaluation|publication|"
        r"citation|bibliograph|scientometric|novelty (?:evaluation|assessment)|"
        r"paper[- ]?(?:to|2)[ -]?(?:code|slide|poster|web|video)|research proposal|"
        r"grant writing|patent (?:writing|generation|claim)|research software|"
        r"reproducib|replicat)", re.I)),
    ("scientific-workflow", re.compile(
        r"\b(ai scientist|science agent|scientific agent|research agent|"
        r"scientific discovery|research (?:idea|ideation|workflow|planning)|"
        r"hypothesis generation|experiment (?:design|planning|execution)|"
        r"automated data science|data science agent|scientific visuali[sz]ation|"
        r"scientific (?:workflow|methodology|writing|figure)|autonomous (?:science|research)|"
        r"research automation|research engineering)", re.I)),
    ("research-evaluation", re.compile(
        r"\b(scientific (?:benchmark|evaluation|testbed|challenge|arena)|"
        r"benchmark(?:ing)? (?:ai|llm|agent).*(?:science|research)|"
        r"(?:science|research).*(?:benchmark|evaluation|testbed|challenge|arena)|"
        r"researcherbench|discoverybench|re-?bench|mle-?bench|paperbench|"
        r"repro[- ]?bench|ideabench|innovatorbench|ablationbench)", re.I)),
]

# Biomedical and vertical work remains eligible only if the title clearly says
# it exports a general workflow.  Keep it in the queue but label it so reviewers
# can reject from evidence rather than through a hidden keyword exclusion.
VERTICAL = re.compile(
    r"\b(bio(?:medical|logy)?|medical|clinical|health|patient|drug|protein|gene|"
    r"molecular|chemistry|chemical|catalyst|material|battery|alloy|perovskite|"
    r"weather|climate|geospatial|agricultur|crop|reservoir|aerospace|"
    r"astronom|physics|earth science|soil|wireless|telecom|eda)\b", re.I)


def url_for(identifier: str, record: dict[str, Any]) -> str:
    if record.get("url"):
        return str(record["url"])
    if identifier.lower().startswith("arxiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    if identifier.lower().startswith("doi:"):
        return f"https://doi.org/{identifier.split(':', 1)[1]}"
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=Path(".tmp/landscape-maintainer/checked-papers.json"))
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--arxiv-only", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    papers = json.loads(args.registry.read_text(encoding="utf-8")).get("papers", {})
    rows: list[dict[str, Any]] = []
    for identifier, record in papers.items():
        if record.get("status") != "included":
            continue
        docs = [str(path) for path in record.get("docs") or []]
        if any(RESEARCH_PATH in path for path in docs):
            continue
        title = str(record.get("title") or "").strip()
        if not title:
            continue
        hit = next((name for name, pattern in AXES if pattern.search(title)), None)
        if not hit:
            continue
        if args.arxiv_only and not identifier.lower().startswith("arxiv:"):
            continue
        rows.append({
            "identifier": identifier,
            "title": title,
            "url": url_for(identifier, record),
            "source_docs": sorted(set(docs)),
            "axis": hit,
            "vertical_cue": bool(VERTICAL.search(title)),
            "registry_note": str(record.get("note") or ""),
        })
    # Scholarly-production items are easiest to verify and have the smallest
    # lexical spillover; retain a deterministic review order within each axis.
    order = {"scholarly-production": 0, "research-evaluation": 1, "scientific-workflow": 2}
    rows.sort(key=lambda item: (order[item["axis"]], item["vertical_cue"], item["title"].lower(), item["identifier"]))
    if args.limit:
        rows = rows[:args.limit]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"candidates: {len(rows)}")
    print("by axis:", dict(Counter(row["axis"] for row in rows)))
    print("arXiv:", sum(row["identifier"].lower().startswith("arxiv:") for row in rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
