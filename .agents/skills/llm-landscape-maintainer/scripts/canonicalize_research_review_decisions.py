#!/usr/bin/env python3
"""Canonicalize distributed closure decisions for the current split-tree.

Subagents often preserve historical README/目录 targets or invent a local
subheading.  This utility keeps their evidence and decisions, while mapping an
include recommendation to the real bilingual section file and one of the five
allowed section labels.  It does not decide relevance or apply documentation.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SECTIONS = {
    "01-leaderboard": ("Leaderboard", "01-leaderboard.md"),
    "02-survey": ("Survey", "02-survey.md"),
    "03-bench": ("Bench", "03-bench.md"),
    "04-model": ("Model", "04-model.md"),
    "05-agent-harness": ("Agent Harness", "05-agent-harness.md"),
    "06-skill": ("Skill", "06-skill.md"),
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def section_key(item: dict[str, Any]) -> str:
    # Inspect path-like fields independently.  Joining a path and a free-form
    # bilingual section label makes the slug look non-terminal (and used to
    # lose otherwise valid targets such as ``.../02-survey``).
    for raw_value in (
        item.get("target_doc"),
        item.get("target_doc_en"),
        item.get("target_en"),
        item.get("target"),
        item.get("docs"),
    ):
        values = raw_value if isinstance(raw_value, list) else [raw_value]
        for value in values:
            raw_target = str(value or "").replace("\\", "/").strip()
            for key in SECTIONS:
                if re.search(rf"(?:^|/){re.escape(key)}(?:\.md|/|$)", raw_target, re.I):
                    return key

    raw_section = str(item.get("section") or "").lower()
    aliases = (
        ("agent harness", "05-agent-harness"),
        ("harness", "05-agent-harness"),
        ("survey", "02-survey"),
        ("review", "02-survey"),
        ("bench", "03-bench"),
        ("benchmark", "03-bench"),
        ("model", "04-model"),
        ("training", "04-model"),
        ("architecture", "04-model"),
        ("skill", "06-skill"),
        ("software", "06-skill"),
    )
    for needle, key in aliases:
        if needle in raw_section:
            return key
    return ""


def topic_root(raw_target: str, key: str) -> str:
    target = raw_target.replace("\\", "/").strip()
    marker = re.search(rf"^(.*?/(?:02-research|04-deep-research))(?:/|$)", target)
    if marker:
        return marker.group(1)
    return ""


def canonical_target(item: dict[str, Any], key: str) -> str:
    raw_target = next(
        (
            str(item.get(name) or "").replace("\\", "/").strip()
            for name in ("target_doc", "target_doc_en", "target_en", "target", "docs")
            if str(item.get(name) or "").strip()
        ),
        "",
    )
    root = topic_root(raw_target, key)
    if not root:
        return ""
    return f"{root}/{SECTIONS[key][1]}"


def normalize_row(item: dict[str, Any]) -> dict[str, Any]:
    row = dict(item)
    decision = str(row.get("decision") or row.get("status") or "").lower()
    if decision not in {"include", "included", "accept", "accepted"}:
        return row
    key = section_key(row)
    target = canonical_target(row, key) if key else ""
    if not key or not target:
        row["decision"] = "defer"
        row["reason"] = (
            "Canonicalization failed: include recommendation has no resolvable "
            "Research or Deep Research split-tree target."
        )
        return row
    row["decision"] = "include"
    row["section"] = SECTIONS[key][0]
    row["target_doc"] = target
    row["target_en"] = target
    row["target_zh"] = target.replace("docs/en/", "docs/zh/", 1)
    return row


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for old in args.output_dir.glob("chunk-*.json"):
        old.unlink()

    counts = {"include": 0, "reject": 0, "defer": 0, "unresolved_include": 0}
    paths: dict[str, int] = {}
    for source in sorted(args.input_dir.glob("chunk-[0-9][0-9][0-9].json")):
        data = read_json(source)
        if not isinstance(data, list):
            raise SystemExit(f"Expected JSON list: {source}")
        out: list[dict[str, Any]] = []
        for raw in data:
            if not isinstance(raw, dict):
                raise SystemExit(f"Non-object row in {source}")
            row = normalize_row(raw)
            decision = str(row.get("decision") or row.get("status") or "").lower()
            counts[decision] = counts.get(decision, 0) + 1
            original = str(raw.get("decision") or raw.get("status") or "").lower()
            if original in {"include", "included", "accept", "accepted"} and decision == "defer":
                counts["unresolved_include"] += 1
            if decision == "include":
                path_key = f"{row['target_doc']}::{row['section']}"
                paths[path_key] = paths.get(path_key, 0) + 1
            out.append(row)
        (args.output_dir / source.name).write_text(
            json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    lines = [
        "# Canonicalized Research Closure Decisions",
        "",
        f"- Input chunks: {len(list(args.input_dir.glob('chunk-[0-9][0-9][0-9].json')))}",
        f"- Includes: {counts.get('include', 0)}",
        f"- Rejects: {counts.get('reject', 0)}",
        f"- Defers: {counts.get('defer', 0)}",
        f"- Unresolved original includes: {counts.get('unresolved_include', 0)}",
        "",
        "## Include Distribution",
        "",
    ]
    lines.extend(f"- `{path}`: {count}" for path, count in sorted(paths.items()))
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Canonicalized includes:", counts.get("include", 0))
    print("Canonicalization defers:", counts.get("defer", 0))
    print("Wrote:", args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
