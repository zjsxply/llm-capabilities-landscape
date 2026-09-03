#!/usr/bin/env python3
"""Merge terminal ledgers and build registry payloads with verified doc paths."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def load(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"Expected a JSON list: {path}")
    return [row for row in data if isinstance(row, dict)]


def appears_in_doc(row: dict[str, Any], path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    identifier = str(row.get("identifier") or "").strip()
    needle = identifier.split(":", 1)[1].lower() if ":" in identifier else identifier.lower()
    title = str(row.get("title") or "").strip().lower()
    url = str(row.get("url") or "").strip().lower()
    return bool((needle and needle in text) or (title and title in text) or (url and url in text))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--main", type=Path, required=True)
    parser.add_argument("--override", type=Path, action="append", default=[])
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--source", default="research-closure-registry-final")
    args = parser.parse_args()

    main_rows = load(args.main)
    if len(main_rows) != len({row.get("identifier") for row in main_rows}):
        raise SystemExit("Main ledger contains duplicate identifiers")

    overrides: dict[str, dict[str, Any]] = {}
    for path in args.override:
        for row in load(path):
            identifier = str(row.get("identifier") or "").strip()
            if not identifier:
                raise SystemExit(f"Override row lacks identifier: {path}")
            overrides[identifier] = row
    main_ids = {str(row.get("identifier") or "") for row in main_rows}
    unknown = sorted(set(overrides) - main_ids)
    if unknown:
        raise SystemExit(f"Overrides are absent from main ledger: {unknown[:20]}")

    terminal = [overrides.get(str(row.get("identifier") or ""), row) for row in main_rows]
    payload: list[dict[str, Any]] = []
    for row in terminal:
        identifier = str(row.get("identifier") or "").strip()
        status = str(row.get("status") or "").strip().lower()
        note = str(row.get("reason") or row.get("note") or "").strip()
        if status not in {"included", "rejected"} or not identifier or not note:
            raise SystemExit(f"Invalid terminal row: {identifier or row!r}")

        docs: list[str] = []
        if status == "included":
            target = Path(str(row.get("target_doc") or "").strip())
            zh_target = Path(str(target).replace("docs/en/", "docs/zh/", 1))
            if not target.is_file() or not zh_target.is_file():
                raise SystemExit(f"Included row lacks paired target docs: {identifier} -> {target}")
            for path in (target, zh_target):
                if not appears_in_doc(row, path):
                    raise SystemExit(f"Included row is absent from target doc: {identifier} -> {path}")
            docs = [str(target), str(zh_target)]

        payload.append(
            {
                "identifier": identifier,
                "status": status,
                "title": row.get("title") or "",
                "url": row.get("url") or "",
                "docs": docs,
                "note": note,
                "source": args.source,
            }
        )

    if len(payload) != len({row["identifier"] for row in payload}):
        raise SystemExit("Final payload contains duplicate identifiers")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "terminal.json": terminal,
        "registry-payload.json": payload,
        "registry-payload-included.json": [row for row in payload if row["status"] == "included"],
        "registry-payload-rejected.json": [row for row in payload if row["status"] == "rejected"],
    }
    for name, rows in outputs.items():
        (args.out_dir / name).write_text(
            json.dumps(rows, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    counts = Counter(row["status"] for row in payload)
    print(f"Terminal records: {len(payload)}")
    print(f"Included: {counts['included']}")
    print(f"Rejected: {counts['rejected']}")
    print(f"Verified included docs: {counts['included'] * 2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
