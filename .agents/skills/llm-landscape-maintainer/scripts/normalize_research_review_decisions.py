#!/usr/bin/env python3
"""Normalize distributed Research-review decisions for bilingual insertion."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TARGETS = {
    "Survey": "02-survey.md",
    "Bench": "03-bench.md",
    "Model": "04-model.md",
    "Agent Harness": "05-agent-harness.md",
    "Skill": "06-skill.md",
}


def bullet(title: str, url: str, tldr: str, zh: bool) -> str:
    prefix = f"- [{title}]({url})"
    text = tldr.strip()
    if text.startswith("- "):
        text = text[2:].split(":", 1)[-1].split("：", 1)[-1].strip()
    return f"{prefix}{'：' if zh else ': '}" + text


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input-dir", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    args = p.parse_args()
    out: list[dict] = []
    for path in sorted(args.input_dir.glob("*.json")):
        for raw in json.loads(path.read_text(encoding="utf-8")):
            if str(raw.get("decision", "")).lower() not in {"include", "include recommendation"}:
                continue
            item = dict(raw)
            section = str(item.get("section") or "")
            for slug, label in {"02-survey": "Survey", "03-bench": "Bench", "04-model": "Model", "05-agent-harness": "Agent Harness", "06-skill": "Skill"}.items():
                if slug in section:
                    section = label
                    break
            if section not in TARGETS:
                target = str(item.get("target", ""))
                section = next((name for name in TARGETS if name.lower() in target.lower()), "")
            if not section:
                target_doc = str(item.get("target_doc") or item.get("target") or "")
                section = next(
                    (label for slug, label in {
                        "02-survey": "Survey", "03-bench": "Bench", "04-model": "Model",
                        "05-agent-harness": "Agent Harness", "06-skill": "Skill",
                    }.items() if slug in target_doc),
                    "",
                )
            if not section:
                raise SystemExit(f"Cannot infer section: {item.get('identifier')}")
            identifier = str(item.get("identifier") or "")
            url = str(item.get("url") or "")
            if not url and identifier.lower().startswith("arxiv:"):
                url = f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
            if not url and identifier.lower().startswith("doi:"):
                url = f"https://doi.org/{identifier.split(':', 1)[1]}"
            title = str(item.get("title") or "")
            en = str(item.get("en_tldr") or "")
            zh = str(item.get("zh_tldr") or "")
            if not all((url, title, en, zh)):
                # Historical title-only recall must not fabricate a TLDR or an
                # official inclusion. Keep it for a later evidence fetch.
                print(f"Skipped incomplete evidence: {item.get('identifier')}")
                continue
            item.update({
                "decision": "include",
                "section": section,
                "target_doc": f"docs/en/03-downstream-applications/02-research/{TARGETS[section]}",
                "suggested_english_bullet": bullet(title, url, en, False),
                "suggested_chinese_bullet": bullet(title, url, zh, True),
            })
            out.append(item)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "chunk-001.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Normalized includes: {len(out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
