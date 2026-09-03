#!/usr/bin/env python3
"""Merge bounded TLDR audit verdicts into authoritative QA JSON files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def canonical(value: Any) -> str:
    text = str(value or "").strip()
    if re.match(r"^arxiv:", text, re.I):
        return "arXiv:" + re.sub(r"v\d+$", "", text.split(":", 1)[1], flags=re.I)
    match = re.fullmatch(r"doi:10\.48550/arxiv\.(\d{4}\.\d{4,5})(?:v\d+)?", text, re.I)
    if match:
        return "arXiv:" + match.group(1)
    if re.match(r"^doi:", text, re.I):
        return "DOI:" + text.split(":", 1)[1].lower()
    return text


def load_list(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"Expected a JSON list: {path}")
    return [row for row in data if isinstance(row, dict)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", type=Path, action="append", required=True)
    parser.add_argument("--qa", type=Path, action="append", required=True)
    parser.add_argument("--parent-overrides", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    audits: dict[str, dict[str, Any]] = {}
    for path in args.audit:
        for raw in load_list(path):
            key = canonical(raw.get("identifier"))
            if not key or key in audits:
                raise SystemExit(f"Missing or duplicate audit identifier: {key or raw!r}")
            audits[key] = dict(raw)

    if args.parent_overrides:
        for raw in load_list(args.parent_overrides):
            key = canonical(raw.get("identifier"))
            if key not in audits:
                raise SystemExit(f"Parent override is absent from audits: {key}")
            audits[key].update(raw)

    qa_data = {path: load_list(path) for path in args.qa}
    locations: dict[str, list[tuple[Path, dict[str, Any]]]] = {}
    for path, rows in qa_data.items():
        for row in rows:
            locations.setdefault(canonical(row.get("identifier")), []).append((path, row))

    changed = 0
    verdict_counts: dict[str, int] = {}
    for key, audit in audits.items():
        verdict = str(audit.get("verdict") or "").strip().lower()
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1
        if verdict == "ok":
            continue
        matches = locations.get(key, [])
        if len(matches) != 1:
            raise SystemExit(f"Expected one authoritative QA row for {key}, found {len(matches)}")
        _, row = matches[0]
        if verdict in {"correct", "reclassify"}:
            for source, target in (("tldr_en", "tldr_en"), ("tldr_zh", "tldr_zh")):
                value = str(audit.get(source) or "").strip()
                if value:
                    row[target] = value
        if verdict == "reclassify":
            section = str(audit.get("section") or "").strip()
            target_doc = str(audit.get("target_doc") or "").strip()
            if not section or not target_doc:
                raise SystemExit(f"Reclassification lacks destination: {key}")
            row.update({"action": "reclassify", "section": section, "target_doc": target_doc})
        elif verdict == "reject":
            row["action"] = "reject"
        elif verdict != "correct":
            raise SystemExit(f"Unsupported verdict for {key}: {verdict}")

        for field in ("reason_en", "reason_zh"):
            value = str(audit.get(field) or "").strip()
            if value:
                row[field] = value
        changed += 1

    if not args.dry_run:
        for path, rows in qa_data.items():
            path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Audit rows: {len(audits)}")
    print(f"Verdicts: {json.dumps(verdict_counts, sort_keys=True)}")
    print(f"Changed QA rows: {changed}")
    if args.dry_run:
        print("Dry run: no files written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
