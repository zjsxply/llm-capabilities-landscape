#!/usr/bin/env python3
"""Finalize chunk reviews with complete parent QA into apply and registry ledgers."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


FINAL_ACTIONS = {"include", "keep", "reject", "reclassify", "alias"}
QA_OVERRIDE_FIELDS = {
    "title",
    "url",
    "year",
    "target_doc",
    "target_doc_en",
    "section",
    "tldr_en",
    "tldr_zh",
    "en_tldr",
    "zh_tldr",
    "alias_of",
}
SECTION_BY_FILE = {
    "02-survey.md": "Survey",
    "03-bench.md": "Bench",
    "04-model.md": "Model",
    "05-agent-harness.md": "Agent Harness",
    "06-skill.md": "Skill",
}


def read_list(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"Expected a JSON list: {path}")
    return [row for row in data if isinstance(row, dict)]


def canonical(value: Any) -> str:
    text = str(value or "").strip()
    if text.lower().startswith("arxiv:"):
        return "arXiv:" + re.sub(r"v\d+$", "", text.split(":", 1)[1], flags=re.I)
    if text.lower().startswith("doi:10.48550/arxiv."):
        match = re.fullmatch(r"doi:10\.48550/arxiv\.(\d{4}\.\d{4,5})(?:v\d+)?", text, re.I)
        if match:
            return "arXiv:" + match.group(1)
    if text.lower().startswith("doi:"):
        return "DOI:" + text.split(":", 1)[1].lower()
    return text


def load_chunks(directory: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(directory.glob("chunk-[0-9][0-9][0-9].json")):
        rows.extend(read_list(path))
    return rows


def stable_url(row: dict[str, Any], identifier: str) -> str:
    if identifier.startswith("arXiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    if identifier.startswith("DOI:"):
        return f"https://doi.org/{identifier.split(':', 1)[1]}"
    return str(row.get("url") or "").strip()


def clean_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().rstrip("。. ")


def bullet(title: str, url: str, text: str, *, zh: bool) -> str:
    title = title.replace("[", "(").replace("]", ")")
    return f"- [{title}]({url}){'：' if zh else ': '}{clean_text(text)}{'。' if zh else '.'}"


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


def apply_qa_overrides(row: dict[str, Any], decision: dict[str, Any]) -> None:
    """Carry evidence-backed corrections from the latest QA stage forward."""
    target = decision.get("target_doc") or decision.get("target_doc_en")
    if target:
        row["target_doc"] = target
        row["target_doc_en"] = target
    for field in QA_OVERRIDE_FIELDS:
        if field in {"target_doc", "target_doc_en"}:
            continue
        value = decision.get(field)
        if value not in (None, ""):
            row[field] = value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--candidates",
        type=Path,
        help="Canonical candidate JSON array. When supplied, its identifiers must exactly match the review set.",
    )
    parser.add_argument("--review-dir", type=Path, required=True)
    parser.add_argument("--qa", type=Path, action="append", default=[])
    parser.add_argument("--strict-qa", type=Path, action="append", default=[])
    parser.add_argument("--reclass-map", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--source", default="research-citation-closure-parent-qa")
    args = parser.parse_args()

    reviews = load_chunks(args.review_dir)
    review_by_id = index_unique(reviews, "reviews")
    candidate_by_id = index_unique(read_list(args.candidates), "candidates") if args.candidates else {}
    if candidate_by_id and set(candidate_by_id) != set(review_by_id):
        raise SystemExit(
            f"Candidate/review coverage mismatch: missing={sorted(set(candidate_by_id) - set(review_by_id))[:20]} "
            f"extra={sorted(set(review_by_id) - set(candidate_by_id))[:20]}"
        )
    qa_rows: list[dict[str, Any]] = []
    for path in args.qa:
        qa_rows.extend(read_list(path))
    qa = index_unique(qa_rows, "parent QA")
    strict_rows: list[dict[str, Any]] = []
    for path in args.strict_qa:
        strict_rows.extend(read_list(path))
    strict_qa = index_unique(strict_rows, "strict parent QA") if strict_rows else {}
    reclass = json.loads(args.reclass_map.read_text(encoding="utf-8"))
    if not isinstance(reclass, dict):
        raise SystemExit("Reclassification map must be an object")

    proposed = {
        identifier
        for identifier, row in review_by_id.items()
        if str(row.get("decision") or "").lower() == "include"
    }
    if set(qa) != proposed:
        raise SystemExit(
            f"Parent QA coverage mismatch: missing={sorted(proposed - set(qa))[:20]} "
            f"extra={sorted(set(qa) - proposed)[:20]}"
        )

    first_pass_retained = {
        identifier
        for identifier, decision in qa.items()
        if str(decision.get("action") or "").lower() in {"include", "keep", "reclassify", "alias"}
    }
    if strict_qa and set(strict_qa) != first_pass_retained:
        raise SystemExit(
            f"Strict QA coverage mismatch: missing={sorted(first_pass_retained - set(strict_qa))[:20]} "
            f"extra={sorted(set(strict_qa) - first_pass_retained)[:20]}"
        )

    apply_rows: list[dict[str, Any]] = []
    terminal: list[dict[str, Any]] = []
    for identifier, row in review_by_id.items():
        row = dict(row)
        original = str(row.get("decision") or "").lower()
        reason = clean_text(row.get("reason_en") or row.get("reason") or row.get("note"))
        action = "reject"
        if original == "include":
            decision = qa[identifier]
            action = str(decision.get("action") or "").lower()
            if action not in FINAL_ACTIONS:
                raise SystemExit(f"Invalid parent action for {identifier}: {action!r}")
            apply_qa_overrides(row, decision)
            reason = clean_text(decision.get("reason_en") or decision.get("reason")) or reason
            if action == "reclassify":
                override = reclass.get(identifier)
                if not isinstance(override, dict):
                    raise SystemExit(f"Missing explicit reclassification target: {identifier}")
                apply_qa_overrides(row, override)
            if action in {"include", "keep", "reclassify", "alias"} and strict_qa:
                strict = strict_qa[identifier]
                strict_action = str(strict.get("action") or "").lower()
                if strict_action not in FINAL_ACTIONS:
                    raise SystemExit(f"Invalid strict parent action for {identifier}: {strict_action!r}")
                action = strict_action
                apply_qa_overrides(row, strict)
                reason = clean_text(strict.get("reason_en") or strict.get("reason")) or reason
                if action == "reclassify" and not (
                    row.get("target_doc") or row.get("target_doc_en")
                ):
                    raise SystemExit(f"Strict reclassification lacks target for {identifier}")
                if action == "reclassify" and not row.get("section"):
                    raise SystemExit(f"Strict reclassification lacks target for {identifier}")
            if action == "alias":
                alias_of = canonical(row.get("alias_of"))
                if not alias_of or alias_of == identifier or alias_of not in review_by_id:
                    raise SystemExit(f"Invalid alias target for {identifier}: {alias_of!r}")
                primary_decision = strict_qa.get(alias_of) or qa.get(alias_of)
                if not primary_decision or str(primary_decision.get("action") or "").lower() not in {
                    "include",
                    "keep",
                    "reclassify",
                }:
                    raise SystemExit(f"Alias target is not retained: {identifier} -> {alias_of}")
                primary = dict(review_by_id[alias_of])
                apply_qa_overrides(primary, qa[alias_of])
                if strict_qa:
                    apply_qa_overrides(primary, strict_qa[alias_of])
                target = str(primary.get("target_doc") or primary.get("target_doc_en") or "").strip()
                section = str(primary.get("section") or "").strip()
                if not target or not section:
                    raise SystemExit(f"Alias target lacks destination: {identifier} -> {alias_of}")
                terminal.append(
                    {
                        "identifier": identifier,
                        "status": "included",
                        "title": clean_text(row.get("title")),
                        "url": stable_url(row, identifier),
                        "section": section,
                        "target_doc": target,
                        "docs": [target, target.replace("docs/en/", "docs/zh/", 1)],
                        "alias_of": alias_of,
                        "note": reason or f"Alias of {alias_of}.",
                        "source": args.source,
                    }
                )
                continue
            if action in {"include", "keep", "reclassify"}:
                title = clean_text(row.get("title"))
                url = stable_url(row, identifier)
                target = str(row.get("target_doc") or row.get("target_doc_en") or "").strip()
                section = str(row.get("section") or "").strip()
                if not title or not url or not target or not section:
                    raise SystemExit(f"Incomplete include target for {identifier}")
                expected_section = SECTION_BY_FILE.get(Path(target).name)
                if expected_section != section:
                    raise SystemExit(
                        f"Section/target mismatch for {identifier}: "
                        f"section={section!r} target={target!r} expected={expected_section!r}"
                    )
                en = clean_text(row.get("tldr_en") or row.get("en_tldr"))
                zh = clean_text(row.get("tldr_zh") or row.get("zh_tldr"))
                if not en or not zh:
                    raise SystemExit(f"Missing bilingual TLDR for {identifier}")
                if not Path(target).is_file() or not Path(target.replace("docs/en/", "docs/zh/", 1)).is_file():
                    raise SystemExit(f"Missing paired target files for {identifier}: {target}")
                apply_rows.append(
                    {
                        "identifier": identifier,
                        "title": title,
                        "year": row.get("year"),
                        "decision": "included",
                        "section": section,
                        "target_doc": target,
                        "reason": reason,
                        "suggested_english_bullet": bullet(title, url, en, zh=False),
                        "suggested_chinese_bullet": bullet(title, url, zh, zh=True),
                    }
                )
                terminal.append(
                    {
                        "identifier": identifier,
                        "status": "included",
                        "title": title,
                        "url": url,
                        "section": section,
                        "target_doc": target,
                        "docs": [target, target.replace("docs/en/", "docs/zh/", 1)],
                        "note": reason,
                        "source": args.source,
                    }
                )
                continue

        title = clean_text(row.get("title"))
        url = stable_url(row, identifier)
        if not reason:
            reason = "Rejected by abstract-backed review and parent taxonomy QA."
        terminal.append(
            {
                "identifier": identifier,
                "status": "rejected",
                "title": title,
                "url": url,
                "docs": [],
                "note": reason,
                "source": args.source,
            }
        )

    expected = set(candidate_by_id) if candidate_by_id else set(review_by_id)
    if len(terminal) != len(expected) or {row["identifier"] for row in terminal} != expected:
        raise SystemExit("Terminal ledger does not exactly cover the canonical candidate set")
    apply_rows.sort(key=lambda row: (row["target_doc"], row.get("year") or 9999, row["title"].lower()))
    terminal.sort(key=lambda row: row["identifier"].lower())
    args.out_dir.mkdir(parents=True, exist_ok=True)
    apply_dir = args.out_dir / "apply"
    apply_dir.mkdir(parents=True, exist_ok=True)
    (apply_dir / "chunk-001.json").write_text(
        json.dumps(apply_rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (args.out_dir / "terminal.json").write_text(
        json.dumps(terminal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    counts = Counter(row["status"] for row in terminal)
    section_counts = Counter(row["section"] for row in apply_rows)
    report = [
        "# Parent QA Round Finalization",
        "",
        f"- Reviews: {len(reviews)}",
        f"- Parent-QA rows: {len(qa)}",
        f"- Strict-QA rows: {len(strict_qa)}",
        f"- Included: {counts['included']}",
        f"- Primary bullets: {len(apply_rows)}",
        f"- Included aliases: {counts['included'] - len(apply_rows)}",
        f"- Rejected: {counts['rejected']}",
        "- Deferred: 0",
        "",
        "## Included by Section",
        "",
        *[f"- {key}: {value}" for key, value in sorted(section_counts.items())],
    ]
    (args.out_dir / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Reviews: {len(reviews)}")
    print(f"Included: {counts['included']}")
    print(f"Rejected: {counts['rejected']}")
    print("Deferred: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
