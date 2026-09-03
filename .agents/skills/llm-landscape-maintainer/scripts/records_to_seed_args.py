#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def iter_records(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    if isinstance(value, dict):
        for key in ("records", "items", "papers", "data"):
            nested = value.get(key)
            if isinstance(nested, list):
                return [item for item in nested if isinstance(item, dict)]
        return [value]
    return []


def load_records(paths: list[Path]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in paths:
        records.extend(iter_records(json.loads(path.read_text(encoding="utf-8"))))
    return records


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract de-duplicated paper identifiers from applied/rejected record JSON files."
    )
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--status", action="append", help="Keep only records with this status; may be repeated.")
    parser.add_argument("--ids-out", type=Path, required=True)
    parser.add_argument("--args-out", type=Path, required=True)
    args = parser.parse_args()

    allowed = {str(status).strip().lower() for status in (args.status or [])}
    identifiers: list[str] = []
    for record in load_records(args.inputs):
        state = str(record.get("status") or record.get("decision") or "").strip().lower()
        if allowed and state not in allowed:
            continue
        identifier = str(record.get("identifier") or "").strip()
        if identifier and identifier not in identifiers:
            identifiers.append(identifier)

    args.ids_out.parent.mkdir(parents=True, exist_ok=True)
    args.args_out.parent.mkdir(parents=True, exist_ok=True)
    args.ids_out.write_text("\n".join(identifiers) + ("\n" if identifiers else ""), encoding="utf-8")
    args.args_out.write_text("\n".join(f"--id {identifier}" for identifier in identifiers) + ("\n" if identifiers else ""), encoding="utf-8")

    print(f"Input files: {len(args.inputs)}", flush=True)
    print(f"Identifiers: {len(identifiers)}", flush=True)
    print(f"Wrote {args.ids_out}", flush=True)
    print(f"Wrote {args.args_out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
