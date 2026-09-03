#!/usr/bin/env python3
"""Compose a complete terminal ledger from a Research closure round.

This deliberately reads JSON arrays and JSONL review files, then keeps the
parent-approved inclusion set separate from all other candidate decisions.
Only rows in ``--apply-out`` are eligible for Markdown application; every
candidate must appear in the terminal ledger as included or rejected.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


SECTIONS = {"Survey", "Bench", "Model", "Agent Harness", "Skill"}
SECTION_FILES = {
    "Survey": "02-survey.md",
    "Bench": "03-bench.md",
    "Model": "04-model.md",
    "Agent Harness": "05-agent-harness.md",
    "Skill": "06-skill.md",
}


def canonical(value: Any) -> str:
    text = str(value or "").strip()
    if text.lower().startswith("arxiv:"):
        return "arXiv:" + re.sub(r"v\d+$", "", text.split(":", 1)[1], flags=re.I)
    if text.lower().startswith("doi:10.48550/arxiv."):
        match = re.search(r"(\d{4}\.\d{4,5})", text)
        if match:
            return "arXiv:" + match.group(1)
    if text.lower().startswith("doi:"):
        return "DOI:" + text.split(":", 1)[1].lower()
    return text


def rows_from_value(value: Any, path: Path) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [row for row in value if isinstance(row, dict)]
    if isinstance(value, dict):
        return [value]
    raise SystemExit(f"Expected JSON object or array: {path}")


def read_rows(path: Path) -> list[dict[str, Any]]:
    raw = path.read_text(encoding="utf-8")
    try:
        return rows_from_value(json.loads(raw), path)
    except json.JSONDecodeError:
        rows: list[dict[str, Any]] = []
        for line_number, line in enumerate(raw.splitlines(), 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSON/JSONL at {path}:{line_number}: {exc}") from exc
            if not isinstance(item, dict):
                raise SystemExit(f"JSONL row is not an object at {path}:{line_number}")
            rows.append(item)
        return rows


def read_dir(directory: Path, pattern: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    paths = sorted(directory.glob(pattern))
    if not paths:
        raise SystemExit(f"No files matching {pattern} in {directory}")
    for path in paths:
        rows.extend(read_rows(path))
    return rows


def index(rows: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in rows:
        key = canonical(row.get("identifier"))
        if not key:
            raise SystemExit(f"{label} contains a row without identifier")
        if key in out:
            raise SystemExit(f"{label} contains duplicate identifier: {key}")
        out[key] = {**row, "identifier": key}
    return out


def text(row: dict[str, Any], *keys: str) -> str:
    for key in keys:
        value = row.get(key)
        if isinstance(value, dict):
            value = value.get("en") or value.get("english") or value.get("zh") or value.get("chinese")
        if value is not None:
            result = re.sub(r"\s+", " ", str(value)).strip().rstrip("。. ")
            if result:
                return result
    return ""


def stable_url(row: dict[str, Any], identifier: str) -> str:
    if identifier.startswith("arXiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    if identifier.startswith("DOI:"):
        return f"https://doi.org/{identifier.split(':', 1)[1]}"
    return text(row, "url", "stable_url", "evidence_url")


def bullet(title: str, url: str, tldr: str, *, zh: bool) -> str:
    title = title.replace("[", "(").replace("]", ")")
    separator = "：" if zh else ": "
    suffix = "。" if zh else "."
    return f"- [{title}]({url}){separator}{tldr.rstrip('。. ')}{suffix}"


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--reviews", type=Path, required=True)
    parser.add_argument("--auto-reject", type=Path, required=True)
    parser.add_argument("--parent-qa", type=Path, required=True)
    parser.add_argument("--strict", type=Path, required=True)
    parser.add_argument("--overrides", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    candidates = index(read_rows(args.candidates), "candidates")
    reviews = index(read_dir(args.reviews, "*.json"), "reviews")
    automatic = index(read_rows(args.auto_reject), "automatic rejects")
    parent = index(read_dir(args.parent_qa, "*.json"), "parent QA")
    strict = index(read_dir(args.strict, "*.json"), "strict QA")
    overrides_raw = json.loads(args.overrides.read_text(encoding="utf-8"))
    if not isinstance(overrides_raw, dict):
        raise SystemExit("Overrides must be an object keyed by identifier")
    overrides = {canonical(key): value for key, value in overrides_raw.items() if isinstance(value, dict)}

    review_includes = {
        key for key, row in reviews.items() if str(row.get("decision") or row.get("status") or "").lower() in {"include", "included"}
    }
    parent_includes = {
        key for key, row in parent.items() if str(row.get("action") or row.get("decision") or "").lower() in {"include", "keep", "approve", "reclassify"}
    }
    if not review_includes <= set(parent):
        raise SystemExit(f"Parent QA misses reviewed includes: {sorted(review_includes - set(parent))[:20]}")
    if not parent_includes <= set(strict) | (set(parent_includes) & set(overrides)):
        missing = parent_includes - set(strict) - set(overrides)
        raise SystemExit(f"Strict QA misses parent includes: {sorted(missing)[:20]}")

    terminal: list[dict[str, Any]] = []
    apply: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    for identifier, candidate in candidates.items():
        base = {
            "identifier": identifier,
            "title": text(candidate, "title"),
            "url": stable_url(candidate, identifier),
            "year": candidate.get("year"),
        }
        override = overrides.get(identifier, {})
        if identifier in parent and identifier in parent_includes:
            parent_row = parent[identifier]
            strict_row = strict.get(identifier, {})
            action = str(override.get("action") or strict_row.get("final_action") or strict_row.get("action") or "reject").lower()
            reason = text(override, "reason_en", "reason") or text(strict_row, "reason_en", "reason") or text(parent_row, "reason_en", "reason")
            if action == "include":
                section = text(override, "section") or text(strict_row, "section") or text(parent_row, "section")
                target = text(override, "target_doc") or text(strict_row, "target_doc") or text(parent_row, "target_doc")
                if section not in SECTIONS:
                    raise SystemExit(f"Invalid section for {identifier}: {section}")
                expected = f"docs/en/03-downstream-applications/02-research/{SECTION_FILES[section]}"
                if target != expected:
                    raise SystemExit(f"Section/target mismatch for {identifier}: {section} -> {target}")
                en = text(override, "tldr_en", "en_tldr") or text(strict_row, "tldr_en", "revised_en_tldr", "en_tldr") or text(parent_row, "tldr_en", "en_tldr")
                zh = text(override, "tldr_zh", "zh_tldr") or text(strict_row, "tldr_zh", "revised_zh_tldr", "zh_tldr") or text(parent_row, "tldr_zh", "zh_tldr")
                if len(en) < 40 or len(zh) < 20 or not reason:
                    raise SystemExit(f"Include lacks concrete bilingual TLDR or reason: {identifier}")
                item = {
                    **base,
                    "status": "include",
                    "decision": "include",
                    "section": section,
                    "target_doc": target,
                    "reason": reason,
                    "suggested_english_bullet": bullet(base["title"], base["url"], en, zh=False),
                    "suggested_chinese_bullet": bullet(base["title"], base["url"], zh, zh=True),
                }
                apply.append(item)
                terminal.append({**item, "status": "included", "docs": [target, target.replace("docs/en/", "docs/zh/", 1)]})
                counts["included"] += 1
                continue
            if action not in {"reject", "reclassify"}:
                raise SystemExit(f"Invalid terminal action for {identifier}: {action}")
            terminal.append({**base, "status": "rejected", "docs": [], "reason": reason or "Rejected by strict Research taxonomy QA."})
            counts["rejected"] += 1
            continue

        if identifier in reviews:
            reason = text(reviews[identifier], "reason_en", "reason", "note")
        elif identifier in automatic:
            reason = text(automatic[identifier], "reason_en", "reason", "note")
        else:
            raise SystemExit(f"Candidate lacks a terminal decision: {identifier}")
        terminal.append({**base, "status": "rejected", "docs": [], "reason": reason or "Rejected by Research closure screening."})
        counts["rejected"] += 1

    if len(terminal) != len(candidates) or {row["identifier"] for row in terminal} != set(candidates):
        raise SystemExit("Terminal ledger does not exactly cover candidates")
    apply.sort(key=lambda row: (row["target_doc"], row.get("year") or 9999, row["title"].casefold()))
    terminal.sort(key=lambda row: row["identifier"].casefold())
    write_json(args.out_dir / "apply" / "chunk-001.json", apply)
    write_json(args.out_dir / "terminal.json", terminal)
    write_json(
        args.out_dir / "registry-payload.json",
        [{"identifier": row["identifier"], "status": row["status"], "title": row["title"], "url": row["url"], "docs": row["docs"], "note": row["reason"], "source": "research-closure-20260901-round-20"} for row in terminal],
    )
    report = [
        "# Research Closure Round 20 Finalization",
        "",
        f"- Candidates: {len(candidates)}",
        f"- Reviewed candidates: {len(reviews)}",
        f"- Automatic rejects: {len(automatic)}",
        f"- Parent QA records: {len(parent)}",
        f"- Strict QA records: {len(strict)}",
        f"- Included: {counts['included']}",
        f"- Rejected: {counts['rejected']}",
        "- Deferred/checking: 0",
    ]
    (args.out_dir / "report.md").parent.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report[2:]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
