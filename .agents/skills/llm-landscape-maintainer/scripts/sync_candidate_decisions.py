#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import checked_paper_registry as registry_mod


DEFAULT_BASE = Path(".tmp/candidate_closure_round2")
DEFAULT_DECISIONS = DEFAULT_BASE / "decisions"
DEFAULT_STATE = DEFAULT_BASE / "registry_synced_files.txt"
DEFAULT_OUT = DEFAULT_BASE / "new_decisions_for_registry.json"

INCLUDE_STATES = {"include", "included", "accept", "accepted"}
REJECT_STATES = {"reject", "rejected", "exclude", "excluded"}
DEFER_STATES = {"defer", "deferred", "already_included"}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def read_state(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def write_state(path: Path, names: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(sorted(names)) + ("\n" if names else ""), encoding="utf-8")


def raw_decision(item: dict[str, Any]) -> str:
    return str(item.get("decision") or item.get("status") or "").strip().lower()


def normalized_status(raw: str) -> str:
    if raw in REJECT_STATES:
        return "rejected"
    if raw in INCLUDE_STATES or raw in DEFER_STATES:
        return "deferred"
    return "deferred"


def note_for(item: dict[str, Any], status: str, raw: str) -> str:
    note = str(item.get("reason") or item.get("note") or "").strip()
    if status == "deferred" and raw in INCLUDE_STATES:
        prefix = "Pending parent review and document integration."
        if note:
            return f"{prefix} {note}"
        return prefix
    if raw == "already_included":
        prefix = "Subagent marked this as already included; parent should verify with docs-sync."
        if note:
            return f"{prefix} {note}"
        return prefix
    if raw == "":
        prefix = "No decision/status field found; kept deferred for parent review."
        if note:
            return f"{prefix} {note}"
        return prefix
    return note


def record_from_item(item: dict[str, Any], source: str) -> dict[str, Any]:
    raw = raw_decision(item)
    status = normalized_status(raw)
    return {
        "identifier": item.get("identifier"),
        "title": item.get("title") or "",
        "url": item.get("url") or "",
        "status": status,
        "docs": [],
        "note": note_for(item, status, raw),
        "source": source,
    }


def update_registry(path: Path, records: list[dict[str, Any]], *, timeout: float, wait: float) -> int:
    count = 0
    with registry_mod.locked_registry(path, write=True, timeout=timeout, wait=wait) as registry:
        papers = registry.setdefault("papers", {})
        for item in records:
            identifier = item.get("identifier")
            if not identifier:
                continue
            key = registry_mod.canonical_identifier(str(identifier))
            record = papers.setdefault(key, {})
            docs = sorted(set(record.get("docs") or []) | set(item.get("docs") or []))
            record.update(
                {
                    "status": item.get("status") or "deferred",
                    "checked_at": item.get("checked_at") or record.get("checked_at") or registry_mod.now(),
                    "updated_at": registry_mod.now(),
                    "title": item.get("title") or record.get("title", ""),
                    "url": item.get("url") or record.get("url", ""),
                    "docs": docs,
                    "note": item.get("note") or record.get("note", ""),
                    "source": item.get("source") or "subagent-decision-sync",
                }
            )
            count += 1
    return count


def select_files(decision_dir: Path, processed: set[str], resync: set[str], all_files: bool) -> list[Path]:
    paths = sorted(decision_dir.glob("chunk-*.json"))
    selected: list[Path] = []
    for path in paths:
        if all_files or path.name not in processed or path.name in resync or path.stem in resync:
            selected.append(path)
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normalize subagent citation-candidate decision files and optionally sync them into the registry."
    )
    parser.add_argument("--decision-dir", type=Path, default=DEFAULT_DECISIONS)
    parser.add_argument("--state-file", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--registry", type=Path, default=registry_mod.DEFAULT_REGISTRY)
    parser.add_argument("--source", default="round2-subagent-screen")
    parser.add_argument("--resync", action="append", default=[], help="Decision file name or stem to sync even if recorded.")
    parser.add_argument("--all", action="store_true", help="Sync every decision file in the directory.")
    parser.add_argument("--apply", action="store_true", help="Write normalized decisions into the checked-paper registry.")
    parser.add_argument("--lock-timeout", type=float, default=300)
    parser.add_argument("--lock-wait", type=float, default=0.1)
    parser.add_argument("--mark-state", action="store_true", help="Record selected decision files as synced.")
    args = parser.parse_args()

    processed = read_state(args.state_file)
    selected = select_files(args.decision_dir, processed, set(args.resync), args.all)

    records: list[dict[str, Any]] = []
    raw_counts: dict[str, int] = {}
    for path in selected:
        data = read_json(path)
        if not isinstance(data, list):
            raise SystemExit(f"Expected a JSON list in {path}")
        for item in data:
            if not isinstance(item, dict):
                continue
            raw = raw_decision(item)
            raw_counts[raw] = raw_counts.get(raw, 0) + 1
            records.append(record_from_item(item, args.source))

    write_json(args.out, records)
    print(f"Selected files: {len(selected)}", flush=True)
    print("Files: " + ", ".join(path.name for path in selected), flush=True)
    print(f"Records: {len(records)}", flush=True)
    print(f"Raw decisions: {json.dumps(raw_counts, ensure_ascii=False, sort_keys=True)}", flush=True)
    print(f"Wrote {args.out}", flush=True)

    if args.apply and records:
        count = update_registry(args.registry, records, timeout=args.lock_timeout, wait=args.lock_wait)
        print(f"Marked records: {count}", flush=True)
        print(f"Wrote {args.registry}", flush=True)

    if args.mark_state:
        processed.update(path.name for path in selected)
        write_state(args.state_file, processed)
        print(f"Synced files in state: {len(processed)}", flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
