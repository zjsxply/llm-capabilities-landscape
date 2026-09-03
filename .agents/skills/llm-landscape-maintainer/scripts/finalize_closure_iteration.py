#!/usr/bin/env python3
"""Merge one citation-closure iteration into a complete terminal decision ledger."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def read_list(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON list: {path}")
    return [row for row in data if isinstance(row, dict)]


def key(row: dict[str, Any]) -> str:
    return str(row.get("identifier") or row.get("id") or "").strip()


def index_unique(rows: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    duplicates: list[str] = []
    for row in rows:
        identifier = key(row)
        if not identifier:
            raise ValueError(f"{label} contains a row without an identifier")
        if identifier in out:
            duplicates.append(identifier)
        out[identifier] = row
    if duplicates:
        raise ValueError(f"{label} contains duplicate identifiers: {duplicates[:10]}")
    return out


def load_reviews(directory: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(directory.glob("chunk-*.json")):
        rows.extend(read_list(path))
    return rows


def write_json(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--unchecked", type=Path, required=True)
    parser.add_argument("--auto-reject", type=Path, required=True)
    parser.add_argument("--title-decisions", type=Path, required=True)
    parser.add_argument("--review-dir", type=Path, required=True)
    parser.add_argument("--out-ledger", type=Path, required=True)
    parser.add_argument("--out-rejections", type=Path, required=True)
    parser.add_argument("--out-includes", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--source", default="citation-closure-iteration")
    args = parser.parse_args()

    unchecked_rows = read_list(args.unchecked)
    unchecked = index_unique(unchecked_rows, "unchecked")
    automatic = index_unique(read_list(args.auto_reject), "auto-reject")
    title_rows = read_list(args.title_decisions)
    title_decisions = index_unique(title_rows, "title decisions")
    review_rows = load_reviews(args.review_dir)
    reviews = index_unique(review_rows, "abstract reviews")

    ledger: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    included: list[dict[str, Any]] = []
    errors: list[str] = []
    counts: Counter[str] = Counter()
    section_counts: Counter[str] = Counter()

    for identifier, candidate in unchecked.items():
        if identifier in reviews:
            source_row = reviews[identifier]
            decision = str(source_row.get("decision") or "").casefold()
            decision_source = "abstract_review"
            if decision not in {"include", "reject"}:
                errors.append(f"{identifier}: invalid abstract-review decision {decision!r}")
                continue
            final = {**candidate, **source_row, "decision_source": decision_source}
            # Review packets can repeat an automatic reject with only a terminal
            # decision. Preserve the stricter automatic rationale instead of
            # turning a complete rejection into an unexplained one.
            if decision == "reject" and not str(final.get("reason") or final.get("note") or final.get("reason_en") or final.get("reason_zh") or "").strip():
                automatic_reason = automatic.get(identifier, {}).get("note") or automatic.get(identifier, {}).get("reason")
                if automatic_reason:
                    final["reason"] = automatic_reason
        elif identifier in automatic:
            source_row = automatic[identifier]
            decision = "reject"
            decision_source = "automatic_scope_reject"
            final = {
                **candidate,
                "decision": decision,
                "reason": source_row.get("note") or source_row.get("reason") or "Automatic scope rejection.",
                "decision_source": decision_source,
            }
        elif identifier in title_decisions:
            source_row = title_decisions[identifier]
            decision = str(source_row.get("decision") or "").casefold()
            decision_source = "title_screen"
            if decision != "reject":
                errors.append(f"{identifier}: unreviewed non-reject title decision {decision!r}")
                continue
            final = {**candidate, **source_row, "decision_source": decision_source}
        else:
            errors.append(f"{identifier}: no terminal decision source")
            continue

        counts[decision] += 1
        final["identifier"] = identifier
        ledger.append(final)
        if decision == "include":
            section_counts[str(final.get("section") or "Unclassified")] += 1
            included.append(final)
        else:
            reason = str(final.get("reason") or final.get("note") or final.get("reason_en") or final.get("reason_zh") or "").strip()
            if not reason:
                errors.append(f"{identifier}: rejected without a reason")
            rejected.append(
                {
                    "identifier": identifier,
                    "title": final.get("title") or candidate.get("title") or "",
                    "url": final.get("url") or candidate.get("url") or "",
                    "status": "rejected",
                    "docs": [],
                    "note": reason,
                    "source": args.source,
                }
            )

    extras = (set(automatic) | set(title_decisions) | set(reviews)) - set(unchecked)
    if extras:
        errors.append(f"Decision sources contain {len(extras)} identifiers absent from unchecked set")
    if len(ledger) != len(unchecked):
        errors.append(f"Ledger covers {len(ledger)} of {len(unchecked)} unchecked candidates")

    write_json(args.out_ledger, ledger)
    write_json(args.out_rejections, rejected)
    write_json(args.out_includes, included)
    lines = [
        "# Closure Iteration Finalization",
        "",
        f"- Unchecked candidates: {len(unchecked)}",
        f"- Automatic-scope decisions: {len(automatic)}",
        f"- Title-screen decisions: {len(title_decisions)}",
        f"- Abstract-review decisions: {len(reviews)}",
        f"- Included recommendations: {counts['include']}",
        f"- Rejected: {counts['reject']}",
        f"- Deferred: 0",
        f"- Errors: {len(errors)}",
        "",
        "## Include Sections",
        "",
    ]
    lines.extend(f"- {section}: {count}" for section, count in sorted(section_counts.items()))
    if errors:
        lines.extend(["", "## Errors", ""] + [f"- {error}" for error in errors])
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Unchecked: {len(unchecked)}")
    print(f"Ledger: {len(ledger)}")
    print(f"Includes: {len(included)}")
    print(f"Rejects: {len(rejected)}")
    print(f"Errors: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
