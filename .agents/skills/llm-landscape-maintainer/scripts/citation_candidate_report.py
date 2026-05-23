#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
from pathlib import Path
from typing import Any

from landscape_paths import default_markdown_files as shared_default_markdown_files
from landscape_paths import expand_markdown_args


SCRIPT_DIR = Path(__file__).resolve().parent
S2_SCRIPT = SCRIPT_DIR / "semantic_scholar_citation_scan.py"


def load_s2_module():
    spec = importlib.util.spec_from_file_location("semantic_scholar_citation_scan", S2_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {S2_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


S2 = load_s2_module()


def expand_file_args(items: list[str]) -> list[Path]:
    return expand_markdown_args(items, default_to_docs=False)


def default_markdown_files(root: Path) -> list[Path]:
    return shared_default_markdown_files(root)


def read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def edge_path(cache_dir: Path, identifier: str, edge: str) -> Path:
    return cache_dir / "edges" / f"{S2.safe_name(identifier)}.{edge}.json"


def legacy_edge_path(cache_dir: Path, identifier: str, edge: str) -> Path | None:
    if edge != "citations" or not identifier.lower().startswith("arxiv:"):
        return None
    arxiv_id = identifier.split(":", 1)[1]
    return cache_dir / "s2_citation_cache" / f"{arxiv_id}.json"


def load_edge_data(cache_dir: Path, identifier: str, edge: str) -> dict[str, Any] | None:
    paths: list[Path] = [edge_path(cache_dir, identifier, edge)]
    legacy = legacy_edge_path(cache_dir, identifier, edge)
    if legacy is not None:
        paths.append(legacy)
    for path in paths:
        data = read_json(path)
        if isinstance(data, dict) and not data.get("_error"):
            return data
    return None


def edge_paper(item: dict[str, Any], edge: str) -> dict[str, Any]:
    key = "citingPaper" if edge == "citations" else "citedPaper"
    paper = item.get(key)
    return paper if isinstance(paper, dict) else {}


def best_url(paper: dict[str, Any]) -> str:
    external = paper.get("externalIds") or {}
    if external.get("ArXiv"):
        return f"https://arxiv.org/abs/{external['ArXiv']}"
    if external.get("DOI"):
        return f"https://doi.org/{external['DOI']}"
    return paper.get("url") or ""


def candidate_key(paper: dict[str, Any]) -> str:
    external = paper.get("externalIds") or {}
    return (
        str(external.get("ArXiv") or "")
        or str(external.get("DOI") or "")
        or str(paper.get("paperId") or "")
        or str(paper.get("title") or "")
        or best_url(paper)
    )


def collect_candidates(
    *,
    identifiers: list[str],
    cache_dir: Path,
    edges: list[str],
    since_year: int,
    min_citations: int,
    require_arxiv: bool,
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    candidates: dict[str, dict[str, Any]] = {}
    missing_edges: list[str] = []
    for identifier in identifiers:
        for edge in edges:
            data = load_edge_data(cache_dir, identifier, edge)
            if not isinstance(data, dict):
                missing_edges.append(f"{identifier} {edge}")
                continue
            for item in data.get("data") or []:
                if not isinstance(item, dict):
                    continue
                paper = edge_paper(item, edge)
                if not paper:
                    continue
                year = paper.get("year") or 0
                if year < since_year:
                    continue
                citations = paper.get("citationCount") or 0
                if citations < min_citations:
                    continue
                external = paper.get("externalIds") or {}
                if require_arxiv and not external.get("ArXiv"):
                    continue
                key = candidate_key(paper)
                if not key:
                    continue
                entry = candidates.setdefault(
                    key,
                    {
                        "paper": paper,
                        "relations": set(),
                        "seed_count": 0,
                    },
                )
                relation = "cites seed" if edge == "citations" else "seed references"
                entry["relations"].add(f"{relation}: `{identifier}`")
                entry["seed_count"] = len(entry["relations"])
    return candidates, missing_edges


def write_report(
    path: Path,
    *,
    identifiers: list[str],
    candidates: dict[str, dict[str, Any]],
    missing_edges: list[str],
    since_year: int,
    top: int,
    include_abstract: bool,
) -> None:
    ranked = sorted(
        candidates.values(),
        key=lambda item: (
            item["paper"].get("year") or 0,
            item["seed_count"],
            item["paper"].get("citationCount") or 0,
        ),
        reverse=True,
    )
    lines = [
        "# Citation Candidates From Existing Cache",
        "",
        f"- Generated: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"- Seeds: {len(identifiers)}",
        f"- Since year: {since_year}",
        f"- Candidates: {len(ranked)}",
        f"- Missing/error edge caches: {len(missing_edges)}",
        "",
        "## Candidate Related Work",
        "",
    ]
    if not ranked:
        lines.append("- None.")
    for entry in ranked[:top]:
        paper = entry["paper"]
        external = paper.get("externalIds") or {}
        arxiv = f" arXiv:{external['ArXiv']}" if external.get("ArXiv") else ""
        venue = f"; {paper.get('venue')}" if paper.get("venue") else ""
        relations = "; ".join(sorted(entry["relations"])[:6])
        lines.append(
            f"- {paper.get('year')} | cites={paper.get('citationCount') or 0} |"
            f"{arxiv}{venue} | {paper.get('title')} | {best_url(paper)} | {relations}"
        )
        if include_abstract and paper.get("abstract"):
            abstract = " ".join(str(paper["abstract"]).split())
            lines.append(f"  - Abstract: {abstract[:600]}")

    lines.extend(["", "## Missing Or Error Edge Caches", ""])
    if not missing_edges:
        lines.append("- None.")
    else:
        for item in missing_edges[:300]:
            lines.append(f"- {item}")
        if len(missing_edges) > 300:
            lines.append(f"- ... {len(missing_edges) - 300} more")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a related-work candidate report from cached S2 edge files.")
    parser.add_argument("files", nargs="*", help="Markdown/text files or globs. Defaults to README and docs Markdown files.")
    parser.add_argument("--id", action="append", default=[], help="Explicit seed identifier.")
    parser.add_argument("--cache-dir", type=Path, default=Path(".tmp/semantic_citation_cache"))
    parser.add_argument("--edge", choices=["citations", "references"], action="append")
    parser.add_argument("--since-year", type=int, default=dt.date.today().year - 1)
    parser.add_argument("--top", type=int, default=200)
    parser.add_argument("--min-citations", type=int, default=0)
    parser.add_argument("--require-arxiv", action="store_true")
    parser.add_argument("--include-abstract", action="store_true")
    parser.add_argument("--out", type=Path, default=Path(".tmp/citation_candidates_existing_cache.md"))
    args = parser.parse_args()

    files = expand_file_args(args.files) if args.files else default_markdown_files(Path.cwd())
    identifiers = S2.collect_identifiers(files, args.id)
    candidates, missing_edges = collect_candidates(
        identifiers=identifiers,
        cache_dir=args.cache_dir,
        edges=list(dict.fromkeys(args.edge or ["citations"])),
        since_year=args.since_year,
        min_citations=args.min_citations,
        require_arxiv=args.require_arxiv,
    )
    write_report(
        args.out,
        identifiers=identifiers,
        candidates=candidates,
        missing_edges=missing_edges,
        since_year=args.since_year,
        top=args.top,
        include_abstract=args.include_abstract,
    )
    print(f"Seeds: {len(identifiers)}", flush=True)
    print(f"Candidates: {len(candidates)}", flush=True)
    print(f"Missing/error edge caches: {len(missing_edges)}", flush=True)
    print(f"Wrote {args.out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
