#!/usr/bin/env python3
"""Build and resolve parent-evidence queues for Research taxonomy audits."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


TERMINAL = {"keep", "reject", "reclassify"}


def read_rows(path: Path) -> list[dict[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or not all(isinstance(row, dict) for row in value):
        raise SystemExit(f"Expected a JSON array of objects: {path}")
    return value


def parse_named_path(value: str) -> tuple[str, Path]:
    try:
        name, raw_path = value.split("=", 1)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected NAME=PATH") from exc
    if not name.strip() or not raw_path.strip():
        raise argparse.ArgumentTypeError("expected nonempty NAME=PATH")
    return name.strip(), Path(raw_path)


def parse_section_spec(value: str) -> tuple[str, Path, Path, Path]:
    parts = value.split("=", 3)
    if len(parts) != 4 or not all(part.strip() for part in parts):
        raise argparse.ArgumentTypeError(
            "expected NAME=CHUNK_DIR=STRICT_DIR=TERMINAL_DIR"
        )
    return parts[0].strip(), *(Path(part.strip()) for part in parts[1:])


def identity(row: dict[str, Any]) -> tuple[Any, str, str]:
    return row.get("index"), str(row.get("identifier") or ""), str(row.get("title") or "")


def build(args: argparse.Namespace) -> int:
    rows: list[dict[str, Any]] = []
    for section, path in args.input:
        for row in read_rows(path):
            if row.get("decision") != "needs_parent_evidence":
                continue
            rows.append({"source_section": section, "source_merged": path.as_posix(), **row})

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for old in args.out_dir.glob("chunk-[0-9][0-9][0-9].json"):
        old.unlink()
    for offset in range(0, len(rows), args.chunk_size):
        number = offset // args.chunk_size + 1
        path = args.out_dir / f"chunk-{number:03d}.json"
        path.write_text(
            json.dumps(rows[offset : offset + args.chunk_size], ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    manifest = {
        "items": len(rows),
        "chunks": (len(rows) + args.chunk_size - 1) // args.chunk_size,
        "by_section": dict(Counter(str(row["source_section"]) for row in rows)),
    }
    (args.out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest))
    return 0


def finalize(args: argparse.Namespace) -> int:
    decisions: dict[tuple[str, tuple[Any, str, str]], dict[str, Any]] = {}
    for decisions_dir in args.decisions_dir:
        for path in sorted(decisions_dir.glob("chunk-[0-9][0-9][0-9].json")):
            for row in read_rows(path):
                section = str(row.get("source_section") or "")
                key = (section, identity(row))
                if key in decisions:
                    raise SystemExit(f"Duplicate parent decision for {key}: {path}")
                decision = str(row.get("decision") or "")
                if decision not in TERMINAL:
                    raise SystemExit(f"Nonterminal parent decision {decision!r} for {key}: {path}")
                target = str(row.get("target_doc") or "").strip()
                if decision == "reclassify" and not target:
                    raise SystemExit(f"Reclassification without target_doc for {key}: {path}")
                if decision != "reclassify" and target:
                    raise SystemExit(f"Unexpected target_doc for {decision} {key}: {path}")
                if not str(row.get("reason_en") or "").strip():
                    raise SystemExit(f"Empty reason_en for {key}: {path}")
                decisions[key] = row

    expected: set[tuple[str, tuple[Any, str, str]]] = set()
    terminal_counts: Counter[str] = Counter()
    for section, chunk_dir, strict_dir, terminal_dir in args.section:
        terminal_dir.mkdir(parents=True, exist_ok=True)
        for old in terminal_dir.glob("chunk-[0-9][0-9][0-9].json"):
            old.unlink()
        for chunk_path in sorted(chunk_dir.glob("chunk-[0-9][0-9][0-9].json")):
            strict_path = strict_dir / chunk_path.name
            source = read_rows(chunk_path)
            strict = read_rows(strict_path)
            if len(source) != len(strict):
                raise SystemExit(f"Count mismatch: {strict_path}")
            output: list[dict[str, Any]] = []
            for position, (source_row, row) in enumerate(zip(source, strict), 1):
                if identity(source_row) != identity(row):
                    raise SystemExit(f"Identity mismatch: {strict_path}:{position}")
                current = dict(row)
                key = (section, identity(current))
                if key in decisions:
                    expected.add(key)
                    override = decisions[key]
                    current.update(
                        {
                            "decision": override["decision"],
                            "target_doc": override.get("target_doc", ""),
                            "reason_en": override["reason_en"],
                            "evidence_basis": override.get("evidence_basis", "parent_evidence"),
                        }
                    )
                elif current.get("decision") == "needs_parent_evidence":
                    raise SystemExit(f"Missing parent decision for {key}")
                if current.get("decision") not in TERMINAL:
                    raise SystemExit(f"Unresolved decision: {strict_path}:{position}")
                terminal_counts[str(current["decision"])] += 1
                output.append(current)
            (terminal_dir / chunk_path.name).write_text(
                json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )

    extra = set(decisions) - expected
    if extra:
        raise SystemExit(f"Unexpected parent decisions: {sorted(extra)[:5]}")
    report = {
        "resolved_parent_items": len(expected),
        "decision_rows": len(decisions),
        "terminal_counts": dict(terminal_counts),
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--input", action="append", type=parse_named_path, required=True)
    build_parser.add_argument("--out-dir", type=Path, required=True)
    build_parser.add_argument("--chunk-size", type=int, default=12)
    build_parser.set_defaults(func=build)

    finalize_parser = subparsers.add_parser("finalize")
    finalize_parser.add_argument("--section", action="append", type=parse_section_spec, required=True)
    finalize_parser.add_argument("--decisions-dir", action="append", type=Path, required=True)
    finalize_parser.add_argument("--report", type=Path, required=True)
    finalize_parser.set_defaults(func=finalize)

    args = parser.parse_args()
    if getattr(args, "chunk_size", 1) <= 0:
        parser.error("--chunk-size must be positive")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
