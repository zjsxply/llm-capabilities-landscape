#!/usr/bin/env python3
"""Validate citation-closure chunk decisions before registry sync or inclusion."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


INCLUDE_STATES = {"include", "included", "accept", "accepted"}
REJECT_STATES = {"reject", "rejected", "exclude", "excluded"}
DEFER_STATES = {"defer", "deferred", "already_included"}
ALL_STATES = INCLUDE_STATES | REJECT_STATES | DEFER_STATES


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def identifier(item: dict[str, Any]) -> str:
    return str(item.get("identifier") or item.get("id") or "").strip()


def decision(item: dict[str, Any]) -> str:
    return str(item.get("decision") or item.get("status") or "").strip().lower()


def text_field(item: dict[str, Any], *names: str) -> str:
    for name in names:
        value = item.get(name)
        if value is None:
            continue
        if isinstance(value, list):
            value = "; ".join(str(part) for part in value if part)
        value = str(value).strip()
        if value:
            return value
    return ""


def is_placeholder_memo(text: str) -> bool:
    stripped = text.strip().lower()
    if not stripped:
        return True
    placeholders = ("todo", "pending", "placeholder", "tbd", "待补", "占位")
    return any(marker in stripped for marker in placeholders) and len(stripped) < 300


def validate_pair(
    chunk_path: Path,
    decision_path: Path,
    memo_path: Path | None,
    *,
    min_memo_chars: int,
) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    counts = {"include": 0, "reject": 0, "defer": 0, "unknown": 0}

    chunk_data = read_json(chunk_path)
    decision_data = read_json(decision_path)
    if not isinstance(chunk_data, list):
        errors.append(f"{chunk_path}: expected JSON list")
        chunk_data = []
    if not isinstance(decision_data, list):
        errors.append(f"{decision_path}: expected JSON list")
        decision_data = []

    chunk_ids = [identifier(item) for item in chunk_data if isinstance(item, dict)]
    decision_ids = [identifier(item) for item in decision_data if isinstance(item, dict)]
    if len(chunk_ids) != len(decision_ids):
        errors.append(f"{decision_path}: record count {len(decision_ids)} != chunk count {len(chunk_ids)}")
    if chunk_ids != decision_ids:
        first_diff = next(
            (
                index
                for index, (left, right) in enumerate(zip(chunk_ids, decision_ids), start=1)
                if left != right
            ),
            None,
        )
        if first_diff is None and len(chunk_ids) != len(decision_ids):
            first_diff = min(len(chunk_ids), len(decision_ids)) + 1
        errors.append(f"{decision_path}: identifier order differs from {chunk_path} at item {first_diff}")

    for index, item in enumerate(decision_data, start=1):
        if not isinstance(item, dict):
            errors.append(f"{decision_path}: item {index} is not an object")
            continue
        state = decision(item)
        if state in INCLUDE_STATES:
            counts["include"] += 1
            missing = []
            if not text_field(item, "target_doc", "target_docs", "docs"):
                missing.append("target_doc")
            if not text_field(item, "section"):
                missing.append("section")
            if not text_field(item, "suggested_english_bullet", "english_bullet", "english_draft"):
                missing.append("english_bullet")
            if not text_field(item, "suggested_chinese_bullet", "chinese_bullet", "chinese_draft"):
                missing.append("chinese_bullet")
            if not text_field(item, "reason", "rationale", "note"):
                missing.append("reason")
            if missing:
                errors.append(f"{decision_path}: include item {index} {identifier(item)} missing {', '.join(missing)}")
        elif state in REJECT_STATES:
            counts["reject"] += 1
            if not text_field(item, "reason", "rationale", "note"):
                errors.append(f"{decision_path}: reject item {index} {identifier(item)} missing reason")
        elif state in DEFER_STATES:
            counts["defer"] += 1
            if not text_field(item, "reason", "rationale", "note"):
                errors.append(f"{decision_path}: defer item {index} {identifier(item)} missing reason")
        else:
            counts["unknown"] += 1
            errors.append(f"{decision_path}: item {index} {identifier(item)} has invalid decision/status {state!r}")

    if memo_path is None or not memo_path.exists():
        errors.append(f"{decision_path}: missing memo/markdown companion")
    else:
        memo_text = memo_path.read_text(encoding="utf-8")
        if len(memo_text.strip()) < min_memo_chars:
            errors.append(f"{memo_path}: memo too short ({len(memo_text.strip())} chars < {min_memo_chars})")
        if is_placeholder_memo(memo_text):
            errors.append(f"{memo_path}: memo appears to be placeholder content")

    return errors, counts


def find_memo(decision_path: Path, memo_dir: Path | None) -> Path | None:
    candidates = []
    if memo_dir is not None:
        candidates.append(memo_dir / f"{decision_path.stem}.md")
    candidates.append(decision_path.with_suffix(".md"))
    for path in candidates:
        if path.exists():
            return path
    return candidates[0] if candidates else None


def write_report(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chunk-dir", type=Path, required=True, help="Directory containing chunk-*.json inputs.")
    parser.add_argument("--decision-dir", type=Path, required=True, help="Directory containing chunk-*.json decisions.")
    parser.add_argument("--memo-dir", type=Path, help="Optional directory containing chunk-*.md memos.")
    parser.add_argument("--out", type=Path, help="Optional Markdown validation report path.")
    parser.add_argument("--min-memo-chars", type=int, default=200)
    args = parser.parse_args()

    all_errors: list[str] = []
    totals = {"include": 0, "reject": 0, "defer": 0, "unknown": 0}
    checked = 0
    for decision_path in sorted(args.decision_dir.glob("chunk-*.json")):
        chunk_path = args.chunk_dir / decision_path.name
        if not chunk_path.exists():
            all_errors.append(f"{decision_path}: missing matching chunk input {chunk_path}")
            continue
        memo_path = find_memo(decision_path, args.memo_dir)
        errors, counts = validate_pair(
            chunk_path,
            decision_path,
            memo_path,
            min_memo_chars=args.min_memo_chars,
        )
        checked += 1
        all_errors.extend(errors)
        for key, value in counts.items():
            totals[key] += value

    if checked == 0:
        all_errors.append(f"{args.decision_dir}: no chunk-*.json decision files found")

    lines = [
        "# Candidate Decision Validation",
        "",
        f"- chunk_dir: `{args.chunk_dir}`",
        f"- decision_dir: `{args.decision_dir}`",
        f"- memo_dir: `{args.memo_dir or args.decision_dir}`",
        f"- checked_files: {checked}",
        f"- include: {totals['include']}",
        f"- defer: {totals['defer']}",
        f"- reject: {totals['reject']}",
        f"- unknown: {totals['unknown']}",
        f"- errors: {len(all_errors)}",
        "",
    ]
    if all_errors:
        lines.append("## Errors")
        lines.extend(f"- {error}" for error in all_errors)
    else:
        lines.append("Validation passed.")

    if args.out:
        write_report(args.out, lines)
        print(f"Wrote {args.out}", flush=True)
    else:
        print("\n".join(lines), flush=True)

    return 1 if all_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
