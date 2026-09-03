#!/usr/bin/env python3
"""Convert evidence-backed review decisions into bilingual apply records."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


TOPIC_ROOTS = {
    "research": "docs/en/03-downstream-applications/02-research",
    "deep research": "docs/en/02-agent-capabilities/04-deep-research",
    "creativity": "docs/en/01-core-capabilities/17-creativity",
    "writing": "docs/en/01-core-capabilities/14-writing",
    "math": "docs/en/01-core-capabilities/08-math",
    "agent safety": "docs/en/02-agent-capabilities/09-agent-safety",
}
SECTION_FILES = {
    "survey": "02-survey.md",
    "bench": "03-bench.md",
    "model": "04-model.md",
    "agent harness": "05-agent-harness.md",
    "skill": "06-skill.md",
}


def load_rows(paths: list[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise SystemExit(f"Expected a JSON list: {path}")
        rows.extend(item for item in data if isinstance(item, dict))
    return rows


def destination(value: Any) -> tuple[str, str] | None:
    raw = re.sub(r"\s+", " ", str(value or "").strip())
    match = re.fullmatch(r"(.+?)\s*/\s*(Survey|Bench|Model|Agent Harness|Skill)", raw, flags=re.I)
    if not match:
        return None
    topic = match.group(1).lower()
    section = match.group(2).title()
    if section.lower() == "agent harness":
        section = "Agent Harness"
    root = TOPIC_ROOTS.get(topic)
    filename = SECTION_FILES.get(section.lower())
    return (section, f"{root}/{filename}") if root and filename else None


def stable_url(row: dict[str, Any]) -> str:
    identifier = str(row.get("identifier") or "").strip()
    arxiv_doi = re.fullmatch(r"DOI:10\.48550/arxiv\.(\d{4}\.\d{4,5})(?:v\d+)?", identifier, flags=re.I)
    if arxiv_doi:
        return f"https://arxiv.org/abs/{arxiv_doi.group(1)}"
    if identifier.lower().startswith("arxiv:"):
        return f"https://arxiv.org/abs/{re.sub(r'v\d+$', '', identifier.split(':', 1)[1], flags=re.I)}"
    if identifier.lower().startswith("doi:"):
        return f"https://doi.org/{identifier.split(':', 1)[1]}"
    return str(row.get("url") or row.get("evidence_url") or "").strip()


def bullet(title: str, url: str, tldr: str, separator: str) -> str:
    text = re.sub(r"\s+", " ", tldr.strip()).rstrip("。. ")
    suffix = "。" if separator == "：" else "."
    return f"- [{title}]({url}){separator}{text}{suffix}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--docs-root", type=Path, default=Path("docs"))
    args = parser.parse_args()

    docs_text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in args.docs_root.glob("**/*.md")
    ).lower()
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in load_rows(args.inputs):
        if str(row.get("decision") or row.get("status") or "").lower() not in {"include", "included", "accept", "accepted"}:
            continue
        routed = destination(row.get("section"))
        title = str(row.get("title") or "").strip()
        url = stable_url(row)
        en = str(row.get("tldr_en") or row.get("en_tldr") or "").strip()
        zh = str(row.get("tldr_zh") or row.get("zh_tldr") or "").strip()
        if not routed or not title or not url or not en or not zh:
            raise SystemExit(f"Included row lacks destination, title, URL, or bilingual TLDR: {row.get('identifier')}")
        if url.lower() in docs_text or title.lower() in docs_text or url.lower() in seen:
            continue
        seen.add(url.lower())
        section, target_doc = routed
        records.append(
            {
                "identifier": row.get("identifier") or "",
                "title": title,
                "decision": "included",
                "section": section,
                "target_doc": target_doc,
                "reason": row.get("reason_en") or "Evidence-backed parent review.",
                "suggested_english_bullet": bullet(title, url, en, ":"),
                "suggested_chinese_bullet": bullet(title, url, zh, "："),
            }
        )

    records.sort(key=lambda row: (row["target_doc"], row["title"].lower()))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Input rows: {len(load_rows(args.inputs))}")
    print(f"Apply records: {len(records)}")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
