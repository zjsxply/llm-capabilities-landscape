#!/usr/bin/env python3
"""Build an applyable bilingual queue and terminal decisions for a reviewed round.

The input is a canonical candidate-review directory plus an optional detail
directory containing richer TLDR fields.  A small, explicit override file is
authoritative for semantic rejects and reroutes; this keeps a path-canonical
review from silently becoming a documentation decision.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ALLOWED_SECTIONS = {"Survey", "Bench", "Model", "Agent Harness", "Skill"}


def load_rows(directory: Path) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for path in sorted(directory.glob("chunk-*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise SystemExit(f"Expected a JSON list: {path}")
        for row in data:
            if not isinstance(row, dict) or not row.get("identifier"):
                continue
            key = canonical(row["identifier"])
            rows.setdefault(key, {**row, "identifier": key})
    return rows


def canonical(value: Any) -> str:
    value = str(value or "").strip()
    if value.lower().startswith("arxiv:"):
        return "arXiv:" + re.sub(r"v\d+$", "", value.split(":", 1)[1], flags=re.I)
    if value.lower().startswith("doi:10.48550/arxiv."):
        match = re.fullmatch(r"doi:10\.48550/arxiv\.(\d{4}\.\d{4,5})(?:v\d+)?", value, re.I)
        if match:
            return "arXiv:" + match.group(1)
    if value.lower().startswith("doi:"):
        return "DOI:" + value.split(":", 1)[1].lower()
    return value


def stable_url(row: dict[str, Any]) -> str:
    identifier = canonical(row.get("identifier"))
    if identifier.startswith("arXiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    if identifier.startswith("DOI:"):
        return f"https://doi.org/{identifier.split(':', 1)[1]}"
    return str(row.get("stable_url") or row.get("url") or "").strip()


def value_for(row: dict[str, Any], *keys: str, language: str | None = None) -> str:
    for key in keys:
        value = row.get(key)
        if isinstance(value, dict):
            choices = [language, "en" if language == "en" else None, "zh" if language == "zh" else None]
            value = next((value.get(name) for name in choices if name and value.get(name)), "")
        if value is None:
            continue
        text = re.sub(r"\s+", " ", str(value)).strip()
        if text:
            return text
    return ""


def description(value: str) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    text = re.sub(r"^-\s*\[[^]]+\]\([^)]*\)\s*[:：]\s*", "", text)
    text = re.sub(r"^-\s+", "", text)
    return text.rstrip("。. ")


def tldr(primary: dict[str, Any], detail: dict[str, Any], *, zh: bool) -> str:
    if zh:
        keys = ("tldr_zh", "zh_tldr", "suggested_chinese_bullet", "chinese_bullet", "tldr")
        language = "zh"
    else:
        keys = ("tldr_en", "en_tldr", "suggested_english_bullet", "english_bullet", "tldr")
        language = "en"
    for row in (detail, primary):
        text = description(value_for(row, *keys, language=language))
        if text and not re.search(
            r"(?:adds? (?:an? )?(?:research )?(?:bench|model|survey|skill|agent harness) item|"
            r"补充该能力方向下的相关工作|适合纳入|相关工作条目)",
            text,
            flags=re.I,
        ):
            return text
    raise SystemExit(f"Missing concrete {'Chinese' if zh else 'English'} TLDR: {primary.get('identifier')}")


def bullet(title: str, url: str, text: str, *, zh: bool) -> str:
    title = title.replace("[", "(").replace("]", ")")
    separator = "：" if zh else ": "
    suffix = "。" if zh else "."
    return f"- [{title}]({url}){separator}{text.rstrip('。. ')}{suffix}"


def route(row: dict[str, Any], override: dict[str, Any]) -> tuple[str, str]:
    section = str(override.get("section") or row.get("section") or "").strip()
    target = str(override.get("target_doc") or row.get("target_doc") or row.get("target_en") or "").strip()
    if section not in ALLOWED_SECTIONS:
        raise SystemExit(f"Invalid section for {row.get('identifier')}: {section}")
    if not target.startswith("docs/en/") or not target.endswith(".md"):
        raise SystemExit(f"Invalid target for {row.get('identifier')}: {target}")
    return section, target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canonical-dir", type=Path, required=True)
    parser.add_argument("--detail-dir", type=Path, required=True)
    parser.add_argument("--override-json", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    primary = load_rows(args.canonical_dir)
    detail = load_rows(args.detail_dir)
    overrides = json.loads(args.override_json.read_text(encoding="utf-8"))
    if not isinstance(overrides, dict):
        raise SystemExit("Override JSON must be an object")

    apply_rows: list[dict[str, Any]] = []
    terminal: list[dict[str, Any]] = []
    for identifier, row in sorted(primary.items()):
        override = overrides.get(identifier, {})
        if not isinstance(override, dict):
            raise SystemExit(f"Override must be an object: {identifier}")
        original = str(row.get("decision") or row.get("status") or "").lower()
        action = str(override.get("action") or ("include" if original == "include" else "reject")).lower()
        url = stable_url(row)
        title = str(row.get("title") or "").strip()
        record = {
            "identifier": identifier,
            "title": title,
            "url": url,
            "year": row.get("year"),
            "source": "research-closure-20260901-round-01-final",
            "docs": [],
        }
        if action == "include":
            section, target = route(row, override)
            en = description(str(override.get("tldr_en") or tldr(row, detail.get(identifier, {}), zh=False)))
            zh = description(str(override.get("tldr_zh") or tldr(row, detail.get(identifier, {}), zh=True)))
            apply_rows.append(
                {
                    "identifier": identifier,
                    "title": title,
                    "decision": "included",
                    "section": section,
                    "target_doc": target,
                    "reason": str(override.get("reason") or row.get("reason") or "Abstract-backed closure review."),
                    "suggested_english_bullet": bullet(title, url, en, zh=False),
                    "suggested_chinese_bullet": bullet(title, url, zh, zh=True),
                    "year": row.get("year"),
                }
            )
            record.update({"status": "included", "section": section, "target_doc": target, "reason": str(override.get("reason") or row.get("reason") or "Abstract-backed closure review."), "docs": [target, target.replace("docs/en/", "docs/zh/", 1)]})
        else:
            record.update({"status": "rejected", "reason": str(override.get("reason") or row.get("reason") or "Rejected by the closure review.")})
        terminal.append(record)

    out_apply = args.out_dir / "apply"
    out_apply.mkdir(parents=True, exist_ok=True)
    (out_apply / "chunk-001.json").write_text(json.dumps(apply_rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.out_dir / "preapply-terminal-ledger.json").write_text(json.dumps(terminal, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    from collections import Counter

    counts = Counter(row["status"] for row in terminal)
    print(f"Review candidates: {len(primary)}")
    print(f"Applyable includes: {len(apply_rows)}")
    print(f"Terminal counts: {dict(counts)}")
    print(f"Wrote {out_apply / 'chunk-001.json'}")
    print(f"Wrote {args.out_dir / 'preapply-terminal-ledger.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
