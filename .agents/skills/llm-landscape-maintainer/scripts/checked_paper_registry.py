#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import importlib.util
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

from landscape_paths import expand_markdown_args

try:
    import fcntl
except ImportError:  # pragma: no cover - this project runs on Linux.
    fcntl = None


SCRIPT_DIR = Path(__file__).resolve().parent
S2_SCRIPT = SCRIPT_DIR / "semantic_scholar_citation_scan.py"
DEFAULT_REGISTRY = Path(".tmp/landscape-maintainer/checked-papers.json")
STATUS_CHOICES = ["checking", "included", "rejected", "deferred"]


class RegistryLockTimeout(TimeoutError):
    pass


def load_s2_module():
    spec = importlib.util.spec_from_file_location("semantic_scholar_citation_scan", S2_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {S2_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


S2 = load_s2_module()
ARXIV_RE = re.compile(r"\d{4}\.\d{4,5}(?:v\d+)?")
ARXIV_DOI_RE = re.compile(r"10\.48550/arxiv\.(\d{4}\.\d{4,5}(?:v\d+)?)", re.I)


def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def strip_arxiv_version(arxiv_id: str) -> str:
    return re.sub(r"v\d+$", "", arxiv_id, flags=re.I)


def canonical_identifier(identifier: str) -> str:
    value = identifier.strip()
    normalized = S2.normalize_identifier(value) or value
    if normalized.lower().startswith("arxiv:"):
        return f"arXiv:{strip_arxiv_version(normalized.split(':', 1)[1])}"
    if normalized.lower().startswith("doi:"):
        doi = normalized.split(":", 1)[1]
        arxiv_match = ARXIV_DOI_RE.fullmatch(doi)
        if arxiv_match:
            return f"arXiv:{strip_arxiv_version(arxiv_match.group(1))}"
        return f"DOI:{doi.lower()}"
    if normalized.lower().startswith("corpusid:"):
        return f"CorpusId:{normalized.split(':', 1)[1]}"
    if re.fullmatch(r"[0-9a-f]{40}", normalized, flags=re.I):
        return f"S2:{normalized.lower()}"
    return normalized


def paper_identifier(paper: dict[str, Any]) -> str | None:
    external = paper.get("externalIds") or {}
    if external.get("ArXiv"):
        return f"arXiv:{strip_arxiv_version(str(external['ArXiv']))}"
    if external.get("DOI"):
        return f"DOI:{str(external['DOI']).lower()}"
    if paper.get("paperId"):
        return f"S2:{str(paper['paperId']).lower()}"
    return None


def best_url(paper: dict[str, Any], identifier: str | None = None) -> str:
    external = paper.get("externalIds") or {}
    if external.get("ArXiv"):
        return f"https://arxiv.org/abs/{strip_arxiv_version(str(external['ArXiv']))}"
    if identifier and identifier.lower().startswith("arxiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    if external.get("DOI"):
        doi = str(external["DOI"])
        arxiv_match = ARXIV_DOI_RE.fullmatch(doi)
        if arxiv_match:
            return f"https://arxiv.org/abs/{strip_arxiv_version(arxiv_match.group(1))}"
        return f"https://doi.org/{doi}"
    return paper.get("url") or ""


def load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": 1, "updated_at": None, "papers": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("schema_version", 1)
    data.setdefault("papers", {})
    return data


def save_registry(path: Path, registry: dict[str, Any]) -> None:
    registry["updated_at"] = now()
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


@contextlib.contextmanager
def locked_registry(path: Path, *, write: bool, timeout: float, wait: float):
    if fcntl is None:
        raise RuntimeError("fcntl is required for synchronized checked-paper registry operations.")
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(path.suffix + ".lock")
    with lock_path.open("w", encoding="utf-8") as handle:
        deadline = time.monotonic() + timeout
        while True:
            try:
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise RegistryLockTimeout(
                        f"Timed out after {timeout:g}s waiting for registry lock: {lock_path}"
                    )
                time.sleep(min(wait, remaining))
        try:
            registry = load_registry(path)
            yield registry
            if write:
                save_registry(path, registry)
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def expand_files(items: list[str]) -> list[Path]:
    return expand_markdown_args(items)


def collect_identifiers_with_docs(files: list[Path], direct_ids: list[str]) -> tuple[list[str], dict[str, set[str]]]:
    seen: set[str] = set()
    ordered: list[str] = []
    docs_by_key: dict[str, set[str]] = {}

    def add(raw: str, path: Path | None = None) -> None:
        normalized = S2.normalize_identifier(raw)
        if not normalized:
            return
        key = canonical_identifier(normalized)
        if key not in seen:
            seen.add(key)
            ordered.append(normalized)
        if path is not None:
            docs_by_key.setdefault(key, set()).add(str(path))

    for raw in direct_ids:
        add(raw)

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in S2.ARXIV_URL_RE.finditer(text):
            add(match.group(1), path)
        for match in S2.ARXIV_TEXT_RE.finditer(text):
            add(match.group(1), path)
        for match in S2.DOI_URL_RE.finditer(text):
            add(f"DOI:{match.group(1)}", path)
        for match in S2.S2_PAPER_RE.finditer(text):
            add(match.group(1), path)

    return ordered, docs_by_key


def sync_included(args: argparse.Namespace) -> int:
    files = expand_files(args.files)
    identifiers, docs_by_key = collect_identifiers_with_docs(files, args.id)
    added = 0
    with locked_registry(args.registry, write=True, timeout=args.lock_timeout, wait=args.lock_wait) as registry:
        for identifier in identifiers:
            key = canonical_identifier(identifier)
            record = registry["papers"].setdefault(key, {})
            if not record:
                added += 1
            docs = set(record.get("docs") or []) | docs_by_key.get(key, set())
            record.update(
                {
                    "status": "included",
                    "checked_at": record.get("checked_at") or now(),
                    "updated_at": now(),
                    "docs": sorted(docs),
                    "source": "docs-sync",
                }
            )
    print(f"Files: {len(files)}", flush=True)
    print(f"Identifiers in docs: {len(identifiers)}", flush=True)
    print(f"New registry records: {added}", flush=True)
    print(f"Wrote {args.registry}", flush=True)
    return 0


def read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def seed_from_edge_path(path: Path) -> str:
    name = path.name
    for suffix in [".citations.json", ".references.json"]:
        if name.endswith(suffix):
            raw = name[: -len(suffix)]
            return f"arXiv:{raw}" if ARXIV_RE.fullmatch(raw) else raw
    return path.stem


def edge_kind(path: Path) -> str:
    if path.name.endswith(".references.json"):
        return "references"
    return "citations"


def edge_paper(item: dict[str, Any], edge: str) -> dict[str, Any]:
    key = "citingPaper" if edge == "citations" else "citedPaper"
    paper = item.get(key)
    return paper if isinstance(paper, dict) else {}


def edge_seed_safe_name(path: Path) -> str:
    name = path.name
    for suffix in [".citations.json", ".references.json"]:
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return path.stem


def collect_cache_candidates(
    cache_dir: Path,
    since_year: int,
    *,
    seed_safe_names: set[str] | None = None,
) -> dict[str, dict[str, Any]]:
    candidates: dict[str, dict[str, Any]] = {}
    edge_paths = sorted((cache_dir / "edges").glob("*.citations.json"))
    edge_paths.extend(sorted((cache_dir / "edges").glob("*.references.json")))
    for path in edge_paths:
        if seed_safe_names is not None and edge_seed_safe_name(path) not in seed_safe_names:
            continue
        data = read_json(path)
        if not isinstance(data, dict) or data.get("_error"):
            continue
        edge = edge_kind(path)
        seed = seed_from_edge_path(path)
        for item in data.get("data") or []:
            if not isinstance(item, dict):
                continue
            paper = edge_paper(item, edge)
            if not paper:
                continue
            year = paper.get("year") or 0
            if year < since_year:
                continue
            identifier = paper_identifier(paper)
            if not identifier:
                continue
            key = canonical_identifier(identifier)
            entry = candidates.setdefault(
                key,
                {
                    "identifier": key,
                    "title": paper.get("title") or "",
                    "year": year,
                    "citationCount": paper.get("citationCount") or 0,
                    "url": best_url(paper, key),
                    "abstract": paper.get("abstract") or "",
                    "relations": [],
                    "seeds": set(),
                },
            )
            relation = "cites seed" if edge == "citations" else "seed references"
            entry["relations"].append(f"{relation}: {seed}")
            entry["seeds"].add(seed)
            if not entry.get("abstract") and paper.get("abstract"):
                entry["abstract"] = paper["abstract"]
    for entry in candidates.values():
        entry["seedCount"] = len(entry["seeds"])
        entry["seeds"] = sorted(entry["seeds"])
        entry["relations"] = sorted(set(entry["relations"]))
    return candidates


def matches_keywords(candidate: dict[str, Any], keywords: list[str]) -> bool:
    if not keywords:
        return True
    haystack = f"{candidate.get('title', '')}\n{candidate.get('abstract', '')}".lower()
    return any(keyword.lower() in haystack for keyword in keywords)


def write_candidates_markdown(path: Path, candidates: list[dict[str, Any]], *, include_abstract: bool, top: int) -> None:
    lines = [
        "# Unchecked Semantic Scholar Candidates",
        "",
        f"- Generated: {now()}",
        f"- Candidates: {len(candidates)}",
        "",
    ]
    for item in candidates[:top]:
        relations = "; ".join(item.get("relations", [])[:5])
        lines.append(
            f"- `{item['identifier']}` | {item.get('year')} | cites={item.get('citationCount', 0)} | "
            f"seed_count={item.get('seedCount', 0)} | {item.get('title')} | {item.get('url')} | {relations}"
        )
        if include_abstract and item.get("abstract"):
            abstract = " ".join(str(item["abstract"]).split())
            lines.append(f"  - Abstract: {abstract[:700]}")
    if not candidates:
        lines.append("- None.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_candidates_json(path: Path, candidates: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    serializable = []
    for item in candidates:
        serializable.append({key: value for key, value in item.items() if key != "abstract" or value})
    path.write_text(json.dumps(serializable, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def candidates_command(args: argparse.Namespace) -> int:
    files = expand_files(args.files) if args.files else []
    direct_ids = list(args.id)
    if args.ids_file:
        direct_ids.extend(
            line.strip()
            for line in args.ids_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )
    seed_ids = S2.collect_identifiers(files, direct_ids) if files or direct_ids else []
    seed_safe_names = {S2.safe_name(identifier) for identifier in seed_ids} if seed_ids else None
    candidates = collect_cache_candidates(args.cache_dir, args.since_year, seed_safe_names=seed_safe_names)
    with locked_registry(args.registry, write=False, timeout=args.lock_timeout, wait=args.lock_wait) as registry:
        checked = {canonical_identifier(key) for key in registry.get("papers", {})}
    filtered = [
        item
        for key, item in candidates.items()
        if key not in checked and matches_keywords(item, args.keyword or [])
    ]
    filtered.sort(
        key=lambda item: (
            item.get("year") or 0,
            item.get("seedCount") or 0,
            item.get("citationCount") or 0,
        ),
        reverse=True,
    )
    write_candidates_markdown(args.out, filtered, include_abstract=args.include_abstract, top=args.top)
    if args.json_out:
        write_candidates_json(args.json_out, filtered)
    if seed_safe_names is not None:
        print(f"Seed identifiers: {len(seed_ids)}", flush=True)
    print(f"Cache candidates: {len(candidates)}", flush=True)
    print(f"Checked registry records: {len(checked)}", flush=True)
    print(f"Unchecked candidates: {len(filtered)}", flush=True)
    print(f"Wrote {args.out}", flush=True)
    if args.json_out:
        print(f"Wrote {args.json_out}", flush=True)
    return 0


def write_claim_markdown(path: Path, candidates: list[dict[str, Any]], *, owner: str, include_abstract: bool) -> None:
    lines = [
        "# Claimed Semantic Scholar Candidates",
        "",
        f"- Generated: {now()}",
        f"- Owner: {owner}",
        f"- Candidates: {len(candidates)}",
        "",
    ]
    for item in candidates:
        relations = "; ".join(item.get("relations", [])[:5])
        lines.append(
            f"- `{item['identifier']}` | {item.get('year')} | cites={item.get('citationCount', 0)} | "
            f"seed_count={item.get('seedCount', 0)} | {item.get('title')} | {item.get('url')} | {relations}"
        )
        if include_abstract and item.get("abstract"):
            abstract = " ".join(str(item["abstract"]).split())
            lines.append(f"  - Abstract: {abstract[:700]}")
    if not candidates:
        lines.append("- None.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def claim_command(args: argparse.Namespace) -> int:
    candidates = collect_cache_candidates(args.cache_dir, args.since_year)
    filtered = [
        item
        for item in candidates.values()
        if matches_keywords(item, args.keyword or [])
    ]
    filtered.sort(
        key=lambda item: (
            item.get("year") or 0,
            item.get("seedCount") or 0,
            item.get("citationCount") or 0,
        ),
        reverse=True,
    )

    claimed: list[dict[str, Any]] = []
    with locked_registry(args.registry, write=True, timeout=args.lock_timeout, wait=args.lock_wait) as registry:
        papers = registry.setdefault("papers", {})
        for item in filtered:
            key = canonical_identifier(item["identifier"])
            if key in papers and not (args.reclaim_stale_hours and is_stale_claim(papers[key], args.reclaim_stale_hours)):
                continue
            record = papers.setdefault(key, {})
            record.update(
                {
                    "status": "checking",
                    "claimed_by": args.owner,
                    "claimed_at": now(),
                    "updated_at": now(),
                    "title": item.get("title", ""),
                    "url": item.get("url", ""),
                    "year": item.get("year"),
                    "citationCount": item.get("citationCount", 0),
                    "seedCount": item.get("seedCount", 0),
                    "relations": item.get("relations", []),
                    "source": "claim",
                }
            )
            claimed.append(item)
            if len(claimed) >= args.limit:
                break

    write_claim_markdown(args.out, claimed, owner=args.owner, include_abstract=args.include_abstract)
    if args.json_out:
        write_candidates_json(args.json_out, claimed)
    print(f"Claimed: {len(claimed)}", flush=True)
    print(f"Wrote {args.out}", flush=True)
    if args.json_out:
        print(f"Wrote {args.json_out}", flush=True)
    return 0 if claimed else 1


def is_stale_claim(record: dict[str, Any], hours: float) -> bool:
    if record.get("status") != "checking":
        return False
    claimed_at = record.get("claimed_at")
    if not claimed_at:
        return True
    try:
        timestamp = dt.datetime.fromisoformat(str(claimed_at))
    except ValueError:
        return True
    age = dt.datetime.now() - timestamp
    return age.total_seconds() > hours * 3600


def mark_command(args: argparse.Namespace) -> int:
    key = canonical_identifier(args.id)
    with locked_registry(args.registry, write=True, timeout=args.lock_timeout, wait=args.lock_wait) as registry:
        record = registry["papers"].setdefault(key, {})
        docs = set(record.get("docs") or [])
        for doc in args.doc or []:
            docs.add(doc)
        record.update(
            {
                "status": args.status,
                "checked_at": args.checked_at or record.get("checked_at") or now(),
                "updated_at": now(),
                "title": args.title or record.get("title", ""),
                "url": args.url or record.get("url", ""),
                "docs": sorted(docs),
                "note": args.note or record.get("note", ""),
                "source": args.source,
            }
        )
    print(f"Marked {key} as {args.status}", flush=True)
    return 0


def mark_from_json_command(args: argparse.Namespace) -> int:
    items = json.loads(args.input.read_text(encoding="utf-8"))
    count = 0
    with locked_registry(args.registry, write=True, timeout=args.lock_timeout, wait=args.lock_wait) as registry:
        for item in items:
            identifier = item.get("identifier")
            if not identifier:
                continue
            key = canonical_identifier(identifier)
            record = registry["papers"].setdefault(key, {})
            docs = sorted(set(record.get("docs") or []) | set(item.get("docs") or []))
            record.update(
                {
                    "status": item.get("status") or args.status,
                    "checked_at": item.get("checked_at") or record.get("checked_at") or now(),
                    "updated_at": now(),
                    "title": item.get("title") or record.get("title", ""),
                    "url": item.get("url") or record.get("url", ""),
                    "docs": docs,
                    "note": item.get("note") or record.get("note", ""),
                    "source": item.get("source") or args.source,
                }
            )
            count += 1
    print(f"Marked records: {count}", flush=True)
    print(f"Wrote {args.registry}", flush=True)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Maintain the persistent checked-paper registry for landscape updates.")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument(
        "--lock-timeout",
        type=float,
        default=300.0,
        help="Seconds to silently wait for the registry lock before failing (default: 300).",
    )
    parser.add_argument(
        "--lock-wait",
        type=float,
        default=0.25,
        help="Seconds between silent registry-lock attempts (default: 0.25).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync = subparsers.add_parser("sync-included", help="Mark papers already present in docs as included.")
    sync.add_argument("files", nargs="*", help="Markdown files or globs. Defaults to README and docs.")
    sync.add_argument("--id", action="append", default=[], help="Explicit identifier to include.")
    sync.set_defaults(func=sync_included)

    candidates = subparsers.add_parser("candidates", help="List S2 cache candidates absent from the registry.")
    candidates.add_argument("files", nargs="*", help="Optional Markdown files whose identifiers should be used as seed filters.")
    candidates.add_argument("--cache-dir", type=Path, default=Path(".tmp/semantic_citation_cache"))
    candidates.add_argument("--id", action="append", default=[], help="Explicit seed identifier to include in the filter.")
    candidates.add_argument(
        "--ids-file",
        type=Path,
        help="Read one explicit arXiv/DOI/S2 seed identifier per line; unlike positional files, this does not parse the file as Markdown.",
    )
    candidates.add_argument("--since-year", type=int, default=dt.date.today().year - 1)
    candidates.add_argument("--keyword", action="append", help="Filter candidates by title or abstract keyword.")
    candidates.add_argument("--top", type=int, default=300)
    candidates.add_argument("--include-abstract", action="store_true")
    candidates.add_argument("--out", type=Path, default=Path(".tmp/s2_unchecked_candidates.md"))
    candidates.add_argument("--json-out", type=Path)
    candidates.set_defaults(func=candidates_command)

    claim = subparsers.add_parser("claim", help="Atomically claim unchecked S2 candidates for one worker.")
    claim.add_argument("--cache-dir", type=Path, default=Path(".tmp/semantic_citation_cache"))
    claim.add_argument("--since-year", type=int, default=dt.date.today().year - 1)
    claim.add_argument("--keyword", action="append", help="Filter candidates by title or abstract keyword.")
    claim.add_argument("--limit", type=int, default=50)
    claim.add_argument("--owner", required=True)
    claim.add_argument("--reclaim-stale-hours", type=float)
    claim.add_argument("--include-abstract", action="store_true")
    claim.add_argument("--out", type=Path, required=True)
    claim.add_argument("--json-out", type=Path)
    claim.set_defaults(func=claim_command)

    mark = subparsers.add_parser("mark", help="Mark one paper as included, rejected, or deferred.")
    mark.add_argument("--id", required=True)
    mark.add_argument("--status", choices=STATUS_CHOICES, required=True)
    mark.add_argument("--title", default="")
    mark.add_argument("--url", default="")
    mark.add_argument("--doc", action="append")
    mark.add_argument("--note", default="")
    mark.add_argument("--source", default="manual")
    mark.add_argument("--checked-at")
    mark.set_defaults(func=mark_command)

    mark_json = subparsers.add_parser("mark-from-json", help="Bulk-mark records from a JSON list.")
    mark_json.add_argument("input", type=Path)
    mark_json.add_argument("--status", choices=STATUS_CHOICES, default="rejected")
    mark_json.add_argument("--source", default="manual-bulk")
    mark_json.set_defaults(func=mark_from_json_command)

    args = parser.parse_args()
    if args.lock_timeout <= 0:
        parser.error("--lock-timeout must be greater than zero")
    if args.lock_wait <= 0:
        parser.error("--lock-wait must be greater than zero")
    try:
        return args.func(args)
    except RegistryLockTimeout as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
