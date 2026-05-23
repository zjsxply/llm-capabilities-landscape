#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any


SIGNAL_ANY = re.compile(
    r"\b("
    r"bench|benchmark|eval|evaluation|leaderboard|arena|testbed|dataset|suite|"
    r"agent|agents|agentic|multi-agent|workflow|orchestrat|tool|browser|web agent|computer use|gui|mcp|"
    r"skill|skills|memory|mem|episodic|long-term|cross-session|"
    r"safety|security|jailbreak|prompt injection|guardrail|red.?team|deception|scheming|risk|attack|vulnerability|"
    r"swe|software|coding|code|debug|repository|"
    r"scientific|science|research|discovery|robot|robotics|embodied|vla|vision-language-action|"
    r"video|spatial|math|multilingual|factual|hallucination|forecast|cyber"
    r")\b",
    re.I,
)

BIOMEDICAL_SCOPE = re.compile(
    r"\b("
    r"biomedical|biomedicine|medical|clinical|clinic|healthcare|patient|"
    r"disease|diagnos(?:is|tic)|radiology|pathology|histology|mri|ct scan|ultrasound|"
    r"eeg|ecg|tumou?r|cancer|oncology|liver|lung|kidney|brain|retina|dermatology|"
    r"protein|genomic|omics|gene|cell|drug|molecule|molecular|biology|ehr|ehrs|mimic-iv"
    r")\b",
    re.I,
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def haystack(item: dict[str, Any]) -> str:
    return f"{item.get('title') or ''}\n{item.get('abstract') or ''}"


def should_auto_reject(item: dict[str, Any], *, max_seed_count: int, max_citations: int) -> bool:
    seed_count = int(item.get("seedCount") or 0)
    citations = int(item.get("citationCount") or 0)
    if seed_count > max_seed_count or citations >= max_citations:
        return False
    return SIGNAL_ANY.search(haystack(item)) is None


def should_biomedical_reject(item: dict[str, Any]) -> bool:
    return BIOMEDICAL_SCOPE.search(haystack(item)) is not None


def registry_record(item: dict[str, Any], status: str, note: str, source: str) -> dict[str, Any]:
    return {
        "identifier": item.get("identifier"),
        "title": item.get("title") or "",
        "url": item.get("url") or "",
        "status": status,
        "docs": [],
        "note": note,
        "source": source,
    }


def compact_item(item: dict[str, Any], abstract_chars: int) -> dict[str, Any]:
    abstract = " ".join(str(item.get("abstract") or "").split())
    return {
        "identifier": item.get("identifier"),
        "title": item.get("title") or "",
        "url": item.get("url") or "",
        "year": item.get("year"),
        "citationCount": item.get("citationCount") or 0,
        "seedCount": item.get("seedCount") or 0,
        "relations": item.get("relations") or [],
        "abstract": abstract[:abstract_chars],
    }


def write_chunks(items: list[dict[str, Any]], chunk_dir: Path, chunk_size: int, abstract_chars: int) -> list[Path]:
    chunk_dir.mkdir(parents=True, exist_ok=True)
    for old in chunk_dir.glob("chunk-*.json"):
        old.unlink()
    paths: list[Path] = []
    total = max(1, math.ceil(len(items) / chunk_size))
    for index in range(total):
        chunk = items[index * chunk_size : (index + 1) * chunk_size]
        path = chunk_dir / f"chunk-{index + 1:03d}.json"
        write_json(path, [compact_item(item, abstract_chars) for item in chunk])
        paths.append(path)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Triage unchecked S2 citation candidates into auto-rejects and review chunks.")
    parser.add_argument("input", type=Path, help="JSON output from checked_paper_registry.py candidates.")
    parser.add_argument("--auto-reject-out", type=Path, default=Path(".tmp/citation_triage_auto_reject.json"))
    parser.add_argument("--keep-out", type=Path, default=Path(".tmp/citation_triage_keep.json"))
    parser.add_argument("--checking-out", type=Path, default=Path(".tmp/citation_triage_checking.json"))
    parser.add_argument("--chunk-dir", type=Path, default=Path(".tmp/citation_triage_chunks"))
    parser.add_argument("--chunk-size", type=int, default=400)
    parser.add_argument("--abstract-chars", type=int, default=500)
    parser.add_argument("--auto-reject-max-seed-count", type=int, default=1)
    parser.add_argument("--auto-reject-max-citations", type=int, default=10)
    parser.add_argument(
        "--exclude-biomedical",
        action="store_true",
        help="Auto-reject biomedical, clinical, omics, drug, and medical-imaging candidates before signal triage.",
    )
    parser.add_argument("--source", default="citation-triage")
    args = parser.parse_args()

    items = read_json(args.input)
    if not isinstance(items, list):
        raise SystemExit(f"Expected list in {args.input}")

    auto_rejects: list[dict[str, Any]] = []
    keep: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict) or not item.get("identifier"):
            continue
        if args.exclude_biomedical and should_biomedical_reject(item):
            note = (
                "Automatic reject: biomedical, clinical, omics, drug, or medical-imaging scope is out of scope "
                "for this task."
            )
            auto_rejects.append(registry_record(item, "rejected", note, args.source))
            continue
        if should_auto_reject(
            item,
            max_seed_count=args.auto_reject_max_seed_count,
            max_citations=args.auto_reject_max_citations,
        ):
            note = (
                "Conservative automatic reject: single low-citation graph relation and no title/abstract signal "
                "for this repository's benchmark, agent harness, skill, safety, memory, software, research, "
                "multimodal, or related capability taxonomy."
            )
            auto_rejects.append(registry_record(item, "rejected", note, args.source))
        else:
            keep.append(item)

    keep.sort(
        key=lambda item: (
            int(item.get("seedCount") or 0),
            int(item.get("citationCount") or 0),
            int(item.get("year") or 0),
        ),
        reverse=True,
    )
    checking = [
        registry_record(item, "checking", "Queued for parallel candidate screening.", args.source)
        for item in keep
    ]
    chunks = write_chunks(keep, args.chunk_dir, max(1, args.chunk_size), max(0, args.abstract_chars))

    write_json(args.auto_reject_out, auto_rejects)
    write_json(args.keep_out, keep)
    write_json(args.checking_out, checking)
    print(f"Input candidates: {len(items)}", flush=True)
    print(f"Auto rejects: {len(auto_rejects)}", flush=True)
    print(f"Review candidates: {len(keep)}", flush=True)
    print(f"Chunks: {len(chunks)}", flush=True)
    print(f"Wrote {args.auto_reject_out}", flush=True)
    print(f"Wrote {args.keep_out}", flush=True)
    print(f"Wrote {args.checking_out}", flush=True)
    print(f"Wrote chunks under {args.chunk_dir}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
