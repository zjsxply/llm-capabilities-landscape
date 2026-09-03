#!/usr/bin/env python3
"""Finalize a bounded Research closure candidate set.

Every candidate must receive a terminal ``included`` or ``rejected`` state.
The script deliberately treats candidates outside the abstract-backed review
window as rejected for this closure pass; it does not invent a paper summary.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical(value: str) -> str:
    value = str(value or "").strip()
    value = re.sub(r"[\s)\]}>，。；：,.;:]+$", "", value)
    if re.match(r"^arxiv:", value, re.I):
        value = re.sub(r"^arxiv:", "arXiv:", value, flags=re.I)
        value = re.sub(r"v\d+$", "", value, flags=re.I)
        return value
    match = re.match(r"^doi:10\.48550/arxiv\.(\d{4}\.\d{4,5})$", value, re.I)
    if match:
        return "arXiv:" + match.group(1)
    if re.match(r"^doi:", value, re.I):
        return "DOI:" + value.split(":", 1)[1].lower()
    return value


def review_decision(value: str) -> str:
    value = str(value or "").strip().lower()
    if value in {"include", "included", "keep"}:
        return "included"
    return "rejected"


def reason_for_review(row: dict[str, Any], decision: str) -> str:
    if decision == "included":
        return str(row.get("reason_en") or row.get("rationale") or "Abstract-backed Research closure review.")
    return str(
        row.get("reason_en")
        or row.get("reason")
        or "The abstract review did not establish a Research artifact within the current taxonomy."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--keep", type=Path, required=True)
    parser.add_argument("--auto-reject", type=Path, required=True)
    parser.add_argument("--review-dir", type=Path, required=True)
    parser.add_argument("--included", type=Path, required=True)
    parser.add_argument("--qa", type=Path, action="append", default=[])
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    candidates: dict[str, dict[str, Any]] = {}
    for path in (args.keep, args.auto_reject):
        rows = load(path)
        if not isinstance(rows, list):
            raise SystemExit(f"Expected a JSON list: {path}")
        for raw in rows:
            if not isinstance(raw, dict) or not raw.get("identifier"):
                continue
            key = canonical(raw["identifier"])
            candidates[key] = {**raw, "identifier": key}

    reviews: dict[str, dict[str, Any]] = {}
    review_paths = [
        path
        for path in sorted(args.review_dir.glob("*.json"))
        if path.name.startswith(("ranks-", "chunk-")) and not path.name.startswith(".")
    ]
    for path in review_paths:
        rows = load(path)
        if not isinstance(rows, list):
            continue
        for raw in rows:
            if not isinstance(raw, dict) or not raw.get("identifier"):
                continue
            key = canonical(raw["identifier"])
            # The wide rank files are canonical; retain the first row after
            # sorting to avoid old overlapping worker files changing a result.
            reviews.setdefault(key, {**raw, "identifier": key})

    included: dict[str, dict[str, Any]] = {}
    for raw in load(args.included):
        if isinstance(raw, dict) and raw.get("identifier"):
            included[canonical(raw["identifier"])] = raw

    qa: dict[str, dict[str, Any]] = {}
    for path in args.qa:
        rows = load(path)
        if not isinstance(rows, list):
            continue
        for raw in rows:
            if isinstance(raw, dict) and raw.get("identifier"):
                qa[canonical(raw["identifier"])] = raw

    ledger: list[dict[str, Any]] = []
    for key, candidate in sorted(candidates.items()):
        row: dict[str, Any] = {
            "identifier": key,
            "title": candidate.get("title") or "",
            "url": candidate.get("url") or "",
            "year": candidate.get("year"),
            "status": "rejected",
            "source": "research-closure-20260831",
            "docs": candidate.get("docs") or [],
        }
        if key in included:
            approved = included[key]
            row.update(
                {
                    "status": "included",
                    "section": approved.get("section"),
                    "target_doc": approved.get("target_doc"),
                    "reason": approved.get("reason") or "Abstract-backed Research closure review.",
                }
            )
        elif key in reviews:
            review = reviews[key]
            decision = review_decision(review.get("decision"))
            row["status"] = decision
            row["reason"] = reason_for_review(review, decision)
            if decision == "included":
                row["status"] = "rejected"
                row["reason"] = "The parent merge rejected this proposed inclusion because it failed a section, duplicate, or scope gate."
        elif candidate.get("status") == "rejected":
            row["reason"] = candidate.get("note") or "Rejected by the automated pre-screen; no Research signal passed the bounded review gate."
        else:
            row["reason"] = "Not selected for abstract-backed review in this bounded closure pass; no sufficient evidence was established for Research inclusion."

        override = qa.get(key)
        if override:
            action = str(override.get("action") or "").strip().lower()
            if action == "reject":
                row["status"] = "rejected"
            elif action == "reclassify" and row["status"] == "included" and override.get("section"):
                row["section"] = override["section"]
                if override.get("target_doc"):
                    row["target_doc"] = override["target_doc"]
                row["reason"] = override.get("reason_en") or row.get("reason")
            if override.get("reason_en"):
                row["reason"] = override["reason_en"]

        # A row is terminal by construction; fail loudly if a future edit
        # accidentally introduces a temporary state.
        if row["status"] not in {"included", "rejected"}:
            raise SystemExit(f"Non-terminal status for {key}: {row['status']}")
        ledger.append(row)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    counts = {state: sum(row["status"] == state for row in ledger) for state in ("included", "rejected")}
    print(f"Candidates: {len(ledger)}")
    print(f"Included: {counts['included']}")
    print(f"Rejected: {counts['rejected']}")
    print(f"Reviews used: {len(reviews)}")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
