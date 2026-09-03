#!/usr/bin/env python3
"""Merge closure shortlists, enrich duplicate hints, and write bounded review packets."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit, urlunsplit


LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
ARXIV_RE = re.compile(r"(?:arxiv:|arxiv\.org/(?:abs|pdf)/)(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
DOI_RE = re.compile(r"(?:doi:|doi\.org/)(10\.\d{4,9}/[^\s?#]+)", re.I)
S2_RE = re.compile(r"(?:S2:|semanticscholar\.org/paper/)([0-9a-f]{40})", re.I)


def read_rows(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON list: {path}")
    return [row for row in data if isinstance(row, dict)]


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def normalize_url(value: str) -> str:
    value = unquote(value.strip())
    parts = urlsplit(value)
    host = parts.netloc.casefold().removeprefix("www.")
    path = parts.path.rstrip("/")
    return urlunsplit(("https", host, path, "", "")) if host else value.casefold()


def identity_keys(row: dict[str, Any]) -> set[str]:
    values = [str(row.get(key) or "") for key in ("identifier", "url")]
    keys: set[str] = set()
    for value in values:
        arxiv = ARXIV_RE.search(value)
        if arxiv:
            keys.add(f"arxiv:{arxiv.group(1)}")
        doi = DOI_RE.search(value)
        if doi:
            keys.add(f"doi:{doi.group(1).rstrip('.,;').casefold()}")
        s2 = S2_RE.search(value)
        if s2:
            keys.add(f"s2:{s2.group(1).casefold()}")
        if value.startswith(("http://", "https://")):
            keys.add(f"url:{normalize_url(value)}")
    title = normalize_text(str(row.get("title") or ""))
    if title:
        keys.add(f"title:{title}")
    return keys


def markdown_index(root: Path) -> dict[str, set[str]]:
    index: dict[str, set[str]] = defaultdict(set)
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for title, url in LINK_RE.findall(text):
            row = {"title": title, "url": url}
            for key in identity_keys(row):
                index[key].add(path.as_posix())
    return index


def merge_rows(rows: Iterable[dict[str, Any]]) -> dict[str, Any]:
    merged: dict[str, Any] = {}
    for row in rows:
        for key, value in row.items():
            if value not in (None, "", [], {}):
                merged[key] = value
    return merged


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--recall", type=Path, required=True)
    parser.add_argument("--docs-root", type=Path, default=Path("docs"))
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--chunk-dir", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--chunk-size", type=int, default=20)
    args = parser.parse_args()

    metadata_rows = read_rows(args.metadata)
    primary_rows = read_rows(args.primary)
    recall_rows = read_rows(args.recall)
    metadata = {str(row.get("identifier") or ""): row for row in metadata_rows}
    selected: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    for source, rows in (("title_include", primary_rows), ("similarity_recall", recall_rows)):
        for row in rows:
            identifier = str(row.get("identifier") or "")
            if identifier:
                selected[identifier].append((source, row))

    docs = markdown_index(args.docs_root)
    packets: list[dict[str, Any]] = []
    source_counts: dict[str, int] = defaultdict(int)
    for identifier, source_rows in selected.items():
        row = merge_rows([metadata.get(identifier, {})] + [item for _, item in source_rows])
        row["identifier"] = identifier
        sources = sorted({source for source, _ in source_rows})
        row["selection_sources"] = sources
        matches: set[str] = set()
        for key in identity_keys(row):
            matches.update(docs.get(key, set()))
        row["existing_doc_matches"] = sorted(matches)
        packets.append(row)
        for source in sources:
            source_counts[source] += 1

    packets.sort(
        key=lambda row: (
            0 if "title_include" in row["selection_sources"] else 1,
            -int(row.get("year") or 0),
            -int(row.get("citationCount") or 0),
            str(row.get("title") or "").casefold(),
        )
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(packets, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    args.chunk_dir.mkdir(parents=True, exist_ok=True)
    for old in args.chunk_dir.glob("chunk-*.json"):
        old.unlink()
    chunk_size = max(1, args.chunk_size)
    chunk_count = math.ceil(len(packets) / chunk_size)
    for index in range(chunk_count):
        chunk = packets[index * chunk_size : (index + 1) * chunk_size]
        path = args.chunk_dir / f"chunk-{index + 1:03d}.json"
        path.write_text(json.dumps(chunk, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with_abstract = sum(bool(row.get("abstract")) for row in packets)
    existing = sum(bool(row.get("existing_doc_matches")) for row in packets)
    lines = [
        "# Closure Review Packet Summary",
        "",
        f"- Primary shortlist: {len(primary_rows)}",
        f"- Similarity recall: {len(recall_rows)}",
        f"- Unique merged candidates: {len(packets)}",
        f"- Candidates with cached abstracts: {with_abstract}",
        f"- Candidates with existing-document hints: {existing}",
        f"- Chunk size: {chunk_size}",
        f"- Chunks: {chunk_count}",
    ]
    for source, count in sorted(source_counts.items()):
        lines.append(f"- Selected by {source}: {count}")
    args.summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Unique candidates: {len(packets)}")
    print(f"With abstracts: {with_abstract}")
    print(f"Existing-document hints: {existing}")
    print(f"Chunks: {chunk_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
