#!/usr/bin/env python3
"""Enrich citation-closure candidates from local Semantic Scholar paper caches.

The batch-edge endpoint normally stores edge records without abstracts. This
helper joins candidates back to the paper cache produced with
``--include-abstracts`` and emits a compact, evidence-bearing review queue.
It deliberately does not make inclusion decisions or edit official docs.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def safe_name(identifier: str) -> str:
    if identifier.lower().startswith("arxiv:"):
        return identifier.split(":", 1)[1].replace("/", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", identifier).strip("_")
    return cleaned if 1 <= len(cleaned) <= 90 else ""


def candidate_cache_paths(cache_dir: Path, identifier: str) -> list[Path]:
    paths: list[Path] = []
    name = safe_name(identifier)
    if name:
        paths.append(cache_dir / "papers" / f"{name}.json")
    # Batch intake normalizes S2:<hash> to the bare paper hash before writing
    # its cache file, while older single-paper intake may retain the prefix.
    if identifier.lower().startswith("s2:"):
        paper_hash = identifier.split(":", 1)[1].strip().lower()
        if re.fullmatch(r"[0-9a-f]{40}", paper_hash):
            paths.append(cache_dir / "papers" / f"{paper_hash}.json")
    return paths


def load_paper(cache_dir: Path, identifier: str, by_external: dict[str, dict[str, Any]]) -> dict[str, Any]:
    for path in candidate_cache_paths(cache_dir, identifier):
        if path.exists():
            try:
                data = read_json(path)
            except json.JSONDecodeError:
                data = {}
            if isinstance(data, dict):
                return data
    return by_external.get(identifier.lower(), {})


def paper_external_keys(paper: dict[str, Any]) -> list[str]:
    external = paper.get("externalIds") or {}
    keys: list[str] = []
    if external.get("ArXiv"):
        keys.append(f"arxiv:{external['ArXiv']}".lower())
    if external.get("DOI"):
        keys.append(f"doi:{external['DOI']}".lower())
    return keys


def load_external_index(cache_dir: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for path in (cache_dir / "papers").glob("*.json"):
        try:
            paper = read_json(path)
        except json.JSONDecodeError:
            continue
        if not isinstance(paper, dict) or paper.get("_error"):
            continue
        for key in paper_external_keys(paper):
            index.setdefault(key, paper)
    return index


def canonical_identifier(identifier: str) -> str:
    value = identifier.strip()
    if value.lower().startswith("arxiv:"):
        return f"arxiv:{re.sub(r'v\\d+$', '', value.split(':', 1)[1])}".lower()
    if value.lower().startswith("doi:"):
        doi = value.split(":", 1)[1]
        arxiv_match = re.fullmatch(r"10\.48550/arxiv\.(\d{4}\.\d{4,5}(?:v\d+)?)", doi, flags=re.I)
        if arxiv_match:
            return f"arxiv:{re.sub(r'v\d+$', '', arxiv_match.group(1), flags=re.I)}".lower()
        return f"doi:{doi}".lower()
    return value.lower()


def best_official_url(paper: dict[str, Any], candidate: dict[str, Any]) -> str:
    external = paper.get("externalIds") or {}
    arxiv = str(external.get("ArXiv") or "")
    if arxiv:
        return f"https://arxiv.org/abs/{re.sub(r'v\d+$', '', arxiv, flags=re.I)}"
    doi = str(external.get("DOI") or "")
    arxiv_doi = re.fullmatch(r"10\.48550/arxiv\.(\d{4}\.\d{4,5}(?:v\d+)?)", doi, flags=re.I)
    if arxiv_doi:
        return f"https://arxiv.org/abs/{re.sub(r'v\d+$', '', arxiv_doi.group(1), flags=re.I)}"
    if doi:
        return f"https://doi.org/{doi}"
    return str(candidate.get("url") or paper.get("url") or "")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    candidates = read_json(args.candidates)
    if not isinstance(candidates, list):
        raise SystemExit(f"Expected a JSON list: {args.candidates}")
    external_index = load_external_index(args.cache_dir)
    enriched: list[dict[str, Any]] = []
    missing = 0
    for candidate in candidates:
        if not isinstance(candidate, dict) or not candidate.get("identifier"):
            continue
        identifier = str(candidate["identifier"])
        paper = load_paper(args.cache_dir, identifier, external_index)
        row = dict(candidate)
        row["identifier"] = identifier
        row["metadata_title"] = paper.get("title") or ""
        row["metadata_abstract"] = " ".join(str(paper.get("abstract") or "").split())
        row["metadata_year"] = paper.get("year")
        row["metadata_url"] = best_official_url(paper, candidate)
        row["metadata_external_ids"] = paper.get("externalIds") or {}
        row["metadata_source"] = "semantic_scholar_paper_cache" if paper else "missing"
        # Downstream triage consumes the canonical candidate fields. Preserve the
        # metadata-prefixed evidence fields for auditability while exposing the
        # enriched values through the shared candidate contract as well.
        if row["metadata_title"]:
            row["title"] = row["metadata_title"]
        if row["metadata_abstract"]:
            row["abstract"] = row["metadata_abstract"]
        if row["metadata_year"]:
            row["year"] = row["metadata_year"]
        if row["metadata_url"]:
            row["url"] = row["metadata_url"]
        if not row["metadata_abstract"]:
            missing += 1
        enriched.append(row)

    enriched.sort(key=lambda row: (-int(row.get("seedCount") or 0), -int(row.get("citationCount") or 0), str(row.get("identifier"))))
    write_json(args.out, enriched)
    lines = [
        "# Semantic Scholar Abstract Candidate Review",
        "",
        f"- Input candidates: {len(candidates)}",
        f"- Enriched candidates: {len(enriched)}",
        f"- Candidates with abstracts: {len(enriched) - missing}",
        f"- Candidates without abstracts: {missing}",
        f"- Source: local `papers/*.json` cache only; no network or official-doc edits.",
        "",
        "## Review Queue",
        "",
    ]
    for row in enriched:
        title = row.get("metadata_title") or row.get("title") or "UNKNOWN"
        abstract = row.get("metadata_abstract") or "ABSTRACT UNAVAILABLE"
        lines.append(
            f"- `{row['identifier']}` | year={row.get('metadata_year') or row.get('year')} | "
            f"seed_count={row.get('seedCount') or 0} | cites={row.get('citationCount') or 0} | {title}"
        )
        lines.append(f"  - URL: {row.get('metadata_url') or row.get('url') or ''}")
        lines.append(f"  - Abstract: {abstract}")
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Enriched candidates: {len(enriched)}", flush=True)
    print(f"With abstracts: {len(enriched) - missing}", flush=True)
    print(f"Without abstracts: {missing}", flush=True)
    print(f"Wrote {args.out}", flush=True)
    print(f"Wrote {args.report}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
