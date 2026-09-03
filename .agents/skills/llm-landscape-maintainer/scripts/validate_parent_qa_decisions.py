#!/usr/bin/env python3
"""Validate bounded parent-QA decisions against their exact input packets."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


SECTION_BY_FILE = {
    "02-survey.md": "Survey",
    "03-bench.md": "Bench",
    "04-model.md": "Model",
    "05-agent-harness.md": "Agent Harness",
    "06-skill.md": "Skill",
}
GENERIC_PATTERNS = (
    re.compile(r"\badds? (?:an? )?(?:survey|bench|model|agent harness|skill) (?:item|entry)\b", re.I),
    re.compile(r"\b(?:relevant|suitable) (?:to|for) (?:this|the) (?:capability|category|area)\b", re.I),
    re.compile(r"(?:围绕.+(?:补充|构建)|为.+补充.+(?:工作|条目)|适合纳入)"),
)


def read_list(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise ValueError(f"expected a JSON array of objects: {path}")
    return data


def value(row: dict[str, Any], *keys: str) -> str:
    for key in keys:
        text = str(row.get(key) or "").strip()
        if text:
            return text
    return ""


def identifier(row: dict[str, Any]) -> str:
    return value(row, "identifier", "id")


def paired_zh(path: str) -> str:
    return path.replace("docs/en/", "docs/zh/", 1)


def validate_pair(
    packet_path: Path,
    decision_path: Path,
    memo_path: Path,
    *,
    state_field: str,
    min_memo_chars: int,
) -> tuple[list[str], Counter[str], list[str]]:
    errors: list[str] = []
    counts: Counter[str] = Counter()
    ids: list[str] = []
    try:
        packets = read_list(packet_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return [str(exc)], counts, ids
    try:
        decisions = read_list(decision_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return [str(exc)], counts, ids

    packet_ids = [identifier(row) for row in packets]
    decision_ids = [identifier(row) for row in decisions]
    ids.extend(decision_ids)
    if packet_ids != decision_ids:
        errors.append(f"{decision_path}: identifier count/order differs from {packet_path}")

    for index, (packet, decision) in enumerate(zip(packets, decisions), start=1):
        paper_id = identifier(decision) or f"item-{index}"
        for field in ("title", "url", "year"):
            if field in packet and decision.get(field) != packet.get(field):
                errors.append(f"{decision_path}: {paper_id} changed source field {field}")
        action = str(decision.get(state_field) or "").strip().lower()
        counts[action or "<missing>"] += 1
        if action not in {"include", "reject"}:
            errors.append(f"{decision_path}: {paper_id} has invalid {state_field}={action!r}")
            continue
        reason = value(decision, "reason_en", "reason", "note")
        if not reason:
            errors.append(f"{decision_path}: {paper_id} lacks reason_en")
        if action == "reject":
            continue

        section = value(decision, "section")
        target = value(decision, "target_doc", "target_doc_en")
        target_zh = value(decision, "target_doc_zh") or paired_zh(target)
        if not target.startswith("docs/en/") or not Path(target).is_file():
            errors.append(f"{decision_path}: {paper_id} has invalid English target {target!r}")
        if target_zh != paired_zh(target) or not Path(target_zh).is_file():
            errors.append(f"{decision_path}: {paper_id} has invalid paired Chinese target {target_zh!r}")
        expected_section = SECTION_BY_FILE.get(Path(target).name)
        if expected_section != section:
            errors.append(
                f"{decision_path}: {paper_id} section/target mismatch "
                f"section={section!r} expected={expected_section!r}"
            )
        en = value(decision, "tldr_en", "en_tldr", "revised_en_tldr")
        zh = value(decision, "tldr_zh", "zh_tldr", "revised_zh_tldr")
        if len(en) < 30 or len(zh) < 15:
            errors.append(f"{decision_path}: {paper_id} lacks substantive bilingual TLDRs")
        if any(pattern.search(en) or pattern.search(zh) for pattern in GENERIC_PATTERNS):
            errors.append(f"{decision_path}: {paper_id} contains a generic TLDR")

        evidence = value(decision, "evidence_quote")
        abstract = value(packet, "source_abstract", "abstract")
        if len(evidence) < 20:
            errors.append(f"{decision_path}: {paper_id} lacks a substantive evidence_quote")
        elif abstract and re.sub(r"\s+", " ", evidence).lower() not in re.sub(r"\s+", " ", abstract).lower():
            errors.append(f"{decision_path}: {paper_id} evidence_quote is not contiguous in the source abstract")

    if not memo_path.is_file():
        errors.append(f"{decision_path}: missing lessons memo {memo_path}")
    else:
        memo = memo_path.read_text(encoding="utf-8").strip()
        if len(memo) < min_memo_chars:
            errors.append(f"{memo_path}: memo too short ({len(memo)} < {min_memo_chars})")
    return errors, counts, ids


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet-dir", type=Path, required=True)
    parser.add_argument("--decision-dir", type=Path, required=True)
    parser.add_argument("--memo-dir", type=Path, required=True)
    parser.add_argument("--state-field", default="action")
    parser.add_argument("--min-memo-chars", type=int, default=200)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    packets = sorted(args.packet_dir.glob("chunk-[0-9][0-9][0-9].json"))
    decisions = sorted(args.decision_dir.glob("chunk-[0-9][0-9][0-9].json"))
    packet_names = {path.name for path in packets}
    decision_names = {path.name for path in decisions}
    errors = [f"missing decision file: {name}" for name in sorted(packet_names - decision_names)]
    errors.extend(f"extra decision file: {name}" for name in sorted(decision_names - packet_names))
    totals: Counter[str] = Counter()
    all_ids: list[str] = []
    for decision_path in decisions:
        packet_path = args.packet_dir / decision_path.name
        if not packet_path.is_file():
            continue
        pair_errors, counts, ids = validate_pair(
            packet_path,
            decision_path,
            args.memo_dir / f"{decision_path.stem}.md",
            state_field=args.state_field,
            min_memo_chars=args.min_memo_chars,
        )
        errors.extend(pair_errors)
        totals.update(counts)
        all_ids.extend(ids)
    duplicates = sorted({paper_id for paper_id in all_ids if all_ids.count(paper_id) > 1})
    if duplicates:
        errors.append(f"duplicate identifiers across decision chunks: {duplicates[:20]}")

    lines = [
        "# Parent QA Decision Validation",
        "",
        f"- Packet files: {len(packets)}",
        f"- Decision files: {len(decisions)}",
        f"- Decision rows: {sum(totals.values())}",
        f"- Include: {totals['include']}",
        f"- Reject: {totals['reject']}",
        f"- Errors: {len(errors)}",
        "",
    ]
    lines.extend(["Validation passed."] if not errors else ["## Errors", *[f"- {error}" for error in errors]])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Decision rows: {sum(totals.values())}")
    print(f"Include: {totals['include']}")
    print(f"Reject: {totals['reject']}")
    print(f"Errors: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
