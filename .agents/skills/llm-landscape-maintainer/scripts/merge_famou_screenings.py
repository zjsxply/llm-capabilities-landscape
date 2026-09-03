#!/usr/bin/env python3
"""Merge parallel famou screening outputs into one canonical decision file.

The source landscape is a useful recall set, not a taxonomy.  This utility
normalizes DOI/arXiv identifiers, joins worker decisions to the enriched
inventory, resolves duplicate worker rows deterministically, and applies
explicit parent overrides.  It never writes landscape Markdown.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ARXIV_RE = re.compile(r"(?:arxiv(?:\.org/(?:abs|pdf)/|:)|doi\.org/10\.48550/arxiv\.)(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
ARXIV_ID_RE = re.compile(r"^\d{4}\.\d{4,5}(?:v\d+)?$", re.I)
DOI_RE = re.compile(r"10\.\d{4,9}/[A-Za-z0-9][A-Za-z0-9._;()/:+\-]*", re.I)

WORKER_DECISIONS = {
    "include_research": "include",
    "route_math": "include",
    "route_deep_research": "include",
    "route_creativity": "include",
    "include": "include",
    "included": "include",
    "reject_vertical": "rejected",
    "reject_other": "rejected",
    "reject": "rejected",
    "keep_elsewhere": "route_elsewhere",
    "route_elsewhere": "route_elsewhere",
    "evidence_insufficient": "rejected",
}

RESEARCH_TARGETS = {
    "Survey": "docs/en/03-downstream-applications/02-research/02-survey.md",
    "Bench": "docs/en/03-downstream-applications/02-research/03-bench.md",
    "Model": "docs/en/03-downstream-applications/02-research/04-model.md",
    "Agent Harness": "docs/en/03-downstream-applications/02-research/05-agent-harness.md",
    "Skill": "docs/en/03-downstream-applications/02-research/06-skill.md",
}


def canonical_identifier(raw: Any) -> str:
    value = str(raw or "").strip()
    arxiv = ARXIV_RE.search(value)
    if arxiv:
        return f"arXiv:{arxiv.group(1)}"
    if ARXIV_ID_RE.fullmatch(value):
        return f"arXiv:{re.sub(r'v\d+$', '', value, flags=re.I)}"
    doi = DOI_RE.search(value)
    if doi:
        # Markdown link punctuation and adjacent CJK text can be captured
        # after a DOI.  Strip only terminal delimiters; preserve the DOI path.
        normalized = doi.group(0).lower().rstrip(".,;:)]}）】》」』")
        if normalized.startswith("10.48550/arxiv."):
            return f"arXiv:{normalized.split('.', 2)[-1]}"
        return f"DOI:{normalized}"
    return value


def stable_url(identifier: str, item: dict[str, Any]) -> str:
    if identifier.lower().startswith("arxiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    if identifier.lower().startswith("doi:"):
        return f"https://doi.org/{identifier.split(':', 1)[1]}"
    return str(item.get("paper_url") or item.get("url") or "").strip()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def rows_from_worker(path: Path) -> list[dict[str, Any]]:
    data = read_json(path)
    if isinstance(data, dict):
        for key in ("decisions", "records", "items", "papers"):
            if isinstance(data.get(key), list):
                return [row for row in data[key] if isinstance(row, dict)]
    if isinstance(data, list):
        return [row for row in data if isinstance(row, dict)]
    raise SystemExit(f"Expected worker list or decisions/records object: {path}")


def section_for(row: dict[str, Any]) -> str:
    value = str(row.get("section") or row.get("destination") or "").strip()
    aliases = {
        "02-survey": "Survey",
        "03-bench": "Bench",
        "04-model": "Model",
        "05-agent-harness": "Agent Harness",
        "06-skill": "Skill",
    }
    for key, label in aliases.items():
        if key in value:
            return label
    return value if value in RESEARCH_TARGETS else ""


def normalize_target_doc(value: Any) -> str:
    """Normalize worker paths from old flat-tree exports to docs/en paths."""
    target = str(value or "").strip().replace("\\", "/")
    if not target:
        return ""
    if target.startswith("docs/en/"):
        return target
    if target.startswith("docs/zh/"):
        return target.replace("docs/zh/", "docs/en/", 1)
    if target.startswith(("01-", "02-", "03-", "04-")):
        return f"docs/en/{target}"
    return target


def normalized_worker_row(row: dict[str, Any], source: Path) -> dict[str, Any] | None:
    identifier = canonical_identifier(row.get("identifier") or row.get("id") or row.get("paper_url"))
    if not identifier:
        return None
    raw_decision = str(row.get("decision") or row.get("status") or "").strip().lower()
    decision = WORKER_DECISIONS.get(raw_decision)
    if not decision:
        raise SystemExit(f"Unknown worker decision {raw_decision!r} for {identifier} in {source}")
    item = dict(row)
    item.update(
        {
            "identifier": identifier,
            "worker_decision": raw_decision,
            "decision": decision,
            "section": section_for(row),
            "target_doc": normalize_target_doc(row.get("target_doc") or row.get("target_docs") or row.get("docs")),
            "en_tldr": str(row.get("en_tldr") or row.get("tldr_en") or "").strip(),
            "zh_tldr": str(row.get("zh_tldr") or row.get("tldr_zh") or "").strip(),
            "source_worker": source.name,
        }
    )
    return item


def evidence_rank(row: dict[str, Any]) -> tuple[int, int, int]:
    decision = str(row.get("decision"))
    has_tldr = bool(row.get("en_tldr") and row.get("zh_tldr"))
    concrete = len(str(row.get("en_tldr") or "")) + len(str(row.get("zh_tldr") or ""))
    # Parent overrides are applied later.  A concrete include is stronger than
    # a title-only or evidence-insufficient row, and an explicit rejection is
    # stronger than an unresolved row.
    return (
        4 if decision == "include" and has_tldr else 3 if decision == "include" else 2 if decision == "rejected" else 1,
        1 if row.get("evidence") or row.get("evidence_source") or row.get("evidence_basis") else 0,
        concrete,
    )


def merge(args: argparse.Namespace) -> list[dict[str, Any]]:
    inventory_rows = read_json(args.inventory)
    if not isinstance(inventory_rows, list):
        raise SystemExit("Inventory must be a JSON list")
    inventory: dict[str, dict[str, Any]] = {}
    for row in inventory_rows:
        if not isinstance(row, dict):
            continue
        identifier = canonical_identifier(row.get("identifier"))
        metadata = row.get("metadata") if isinstance(row.get("metadata"), dict) else {}
        inventory[identifier] = {
            "identifier": identifier,
            "title": metadata.get("title") or row.get("title") or "",
            "published": metadata.get("published") or row.get("published") or "",
            "url": metadata.get("url") or stable_url(identifier, row),
            "abstract": metadata.get("abstract") or "",
            "occurrences": row.get("occurrences") or [],
            "metadata_found": bool(row.get("metadata_found")),
        }

    candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in args.workers:
        for raw in rows_from_worker(path):
            row = normalized_worker_row(raw, path)
            if row:
                candidates[row["identifier"]].append(row)

    overrides: dict[str, dict[str, Any]] = {}
    if args.overrides:
        raw_overrides = read_json(args.overrides)
        if isinstance(raw_overrides, list):
            raw_overrides = {str(row.get("identifier")): row for row in raw_overrides if isinstance(row, dict)}
        if not isinstance(raw_overrides, dict):
            raise SystemExit("Overrides must be an object or list")
        overrides = {canonical_identifier(key): value for key, value in raw_overrides.items() if isinstance(value, dict)}

    output: list[dict[str, Any]] = []
    missing_decisions = sorted(set(inventory) - set(candidates))
    unexpected = sorted(set(candidates) - set(inventory))
    if unexpected:
        print(f"Warning: worker identifiers outside inventory: {len(unexpected)}")

    for identifier in sorted(inventory):
        base = dict(inventory[identifier])
        rows = candidates.get(identifier, [])
        chosen = max(rows, key=evidence_rank) if rows else {}
        item = {**base, **chosen, "identifier": identifier, "worker_rows": len(rows)}
        override = overrides.get(identifier, {})
        item.update(override)
        item["identifier"] = identifier
        item["decision"] = str(item.get("decision") or "").lower()
        if item["decision"] not in {"include", "rejected", "route_elsewhere", "already_included"}:
            raise SystemExit(f"Unresolved decision for {identifier}; add a parent override")
        if item["decision"] == "include":
            item["section"] = section_for(item)
            if not item["section"] or not item.get("en_tldr") or not item.get("zh_tldr"):
                raise SystemExit(f"Included item lacks section or bilingual TLDR: {identifier}")
            item["target_doc"] = normalize_target_doc(item.get("target_doc")) or RESEARCH_TARGETS.get(item["section"], "")
            if not item["target_doc"]:
                raise SystemExit(f"Included item lacks target_doc: {identifier}")
        item["url"] = stable_url(identifier, item)
        output.append(item)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = Counter(item["decision"] for item in output)
    print(f"Inventory identifiers: {len(inventory)}")
    print(f"Worker decision rows: {sum(len(rows) for rows in candidates.values())}")
    print(f"Missing worker decisions before overrides: {len(missing_decisions)}")
    print(f"Canonical decisions: {dict(counts)}")
    print(f"Wrote {args.out}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--workers", type=Path, nargs="+", required=True)
    parser.add_argument("--overrides", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    merge(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
