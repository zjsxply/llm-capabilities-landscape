#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


INCLUDE_STATES = {"include", "included", "accept", "accepted"}
STRONG_SIGNAL = re.compile(
    r"\b("
    r"bench|benchmark|leaderboard|arena|suite|dataset|testbed|"
    r"agent|agentic|workflow|orchestrat|skill|memory|tool|gui|browser|computer-use|"
    r"swe|cyber|safety|red.?team|robot|embodied|vla"
    r")\b",
    re.I,
)
WEAK_MODEL_ONLY = re.compile(
    r"\b(technical report|survey|pretraining|post-training|distillation|fine-tuning|alignment|dataset for training)\b",
    re.I,
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def docs_text(paths: list[Path]) -> str:
    return "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in paths if path.exists())


def normalize_docs(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if item]
    return []


def raw_decision(item: dict[str, Any]) -> str:
    return str(item.get("decision") or item.get("status") or "").strip().lower()


def identifier_raw(identifier: str) -> str:
    if ":" in identifier:
        return identifier.split(":", 1)[1]
    return identifier


def score_item(item: dict[str, Any], docs: list[str], existing_text: str, priority_docs: list[str]) -> tuple[int, bool]:
    identifier = str(item.get("identifier") or "")
    raw = identifier_raw(identifier)
    already = bool((raw and raw in existing_text) or (identifier and identifier in existing_text))
    title = str(item.get("title") or "")
    reason = str(item.get("reason") or item.get("note") or "")
    section = str(item.get("section") or "")
    text = " ".join([title, reason, section])
    score = 0
    if STRONG_SIGNAL.search(text):
        score += 3
    if any(any(priority in doc for priority in priority_docs) for doc in docs):
        score += 2
    if int(item.get("year") or 0) >= 2026:
        score += 2
    if int(item.get("seedCount") or 0) >= 3:
        score += 1
    if int(item.get("citationCount") or 0) >= 5:
        score += 1
    if WEAK_MODEL_ONLY.search(text):
        score -= 3
    if already:
        score -= 10
    return score, already


def load_recommendations(decision_dir: Path, existing_text: str, priority_docs: list[str]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(decision_dir.glob("chunk-*.json")):
        data = read_json(path)
        if not isinstance(data, list):
            continue
        for item in data:
            if not isinstance(item, dict) or raw_decision(item) not in INCLUDE_STATES:
                continue
            docs = normalize_docs(item.get("target_docs") if "target_docs" in item else item.get("docs"))
            score, already = score_item(item, docs, existing_text, priority_docs)
            records.append(
                {
                    "score": score,
                    "chunk": path.name,
                    "identifier": item.get("identifier") or "",
                    "title": item.get("title") or "",
                    "url": item.get("url") or "",
                    "year": item.get("year"),
                    "citationCount": item.get("citationCount"),
                    "seedCount": item.get("seedCount"),
                    "docs": docs,
                    "section": item.get("section") or "",
                    "reason": item.get("reason") or item.get("note") or "",
                    "english_draft": item.get("english_draft") or "",
                    "chinese_draft": item.get("chinese_draft") or "",
                    "already_in_docs": already,
                }
            )
    records.sort(key=lambda item: (item["already_in_docs"], -item["score"], -(item.get("year") or 0), item["identifier"]))
    return records


def strict_records(records: list[dict[str, Any]], *, min_score: int, doc_cap: int, priority_doc_cap: int, priority_docs: list[str]) -> list[dict[str, Any]]:
    by_doc: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen: set[str] = set()
    for item in records:
        if item.get("already_in_docs") or int(item.get("score") or 0) < min_score:
            continue
        key = str(item.get("identifier") or "").lower()
        if key in seen:
            continue
        seen.add(key)
        docs = item.get("docs") or ["UNKNOWN"]
        by_doc[str(docs[0])].append(item)
    selected: list[dict[str, Any]] = []
    for doc, items in sorted(by_doc.items()):
        items.sort(key=lambda item: (-int(item.get("score") or 0), -(item.get("year") or 0), item["identifier"]))
        cap = priority_doc_cap if any(priority in doc for priority in priority_docs) else doc_cap
        selected.extend(items[:cap])
    selected.sort(key=lambda item: ((item.get("docs") or [""])[0], -int(item.get("score") or 0), item["identifier"]))
    return selected


def write_doc_splits(path: Path, records: list[dict[str, Any]]) -> None:
    path.mkdir(parents=True, exist_ok=True)
    for old in path.glob("*.json"):
        old.unlink()
    by_doc: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in records:
        docs = item.get("docs") or ["UNKNOWN"]
        by_doc[str(docs[0])].append(item)
    for doc, items in sorted(by_doc.items()):
        safe = doc.replace("/", "__").replace(".", "_")
        write_json(path / f"{safe}.json", items)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a parent-review shortlist from subagent candidate decisions.")
    parser.add_argument("--decision-dir", type=Path, default=Path(".tmp/candidate_closure_round2/decisions"))
    parser.add_argument("--all-out", type=Path, default=Path(".tmp/candidate_closure_round2/parent_review_shortlist.json"))
    parser.add_argument("--strict-out", type=Path, default=Path(".tmp/candidate_closure_round2/parent_review_candidates_strict.json"))
    parser.add_argument("--split-dir", type=Path, default=Path(".tmp/candidate_closure_round2/parent_review_by_doc"))
    parser.add_argument("--min-score", type=int, default=7)
    parser.add_argument("--doc-cap", type=int, default=8)
    parser.add_argument("--priority-doc-cap", type=int, default=25)
    parser.add_argument(
        "--priority-doc",
        action="append",
        default=["01-13-skill-use", "02-11-embodied-vla", "02-10-cybersecurity"],
    )
    parser.add_argument("docs", nargs="*", default=["README.md", "README.zh.md", "docs/en/*.md", "docs/zh/*.md"])
    args = parser.parse_args()

    doc_paths: list[Path] = []
    for pattern in args.docs:
        matches = sorted(Path().glob(pattern))
        if matches:
            doc_paths.extend(path for path in matches if path.is_file())
        elif Path(pattern).is_file():
            doc_paths.append(Path(pattern))

    records = load_recommendations(args.decision_dir, docs_text(doc_paths), args.priority_doc)
    strict = strict_records(
        records,
        min_score=args.min_score,
        doc_cap=args.doc_cap,
        priority_doc_cap=args.priority_doc_cap,
        priority_docs=args.priority_doc,
    )
    write_json(args.all_out, records)
    write_json(args.strict_out, strict)
    write_doc_splits(args.split_dir, strict)
    print(f"Recommendations: {len(records)}", flush=True)
    print(f"Strict shortlist: {len(strict)}", flush=True)
    print(f"Wrote {args.all_out}", flush=True)
    print(f"Wrote {args.strict_out}", flush=True)
    print(f"Wrote splits under {args.split_dir}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
