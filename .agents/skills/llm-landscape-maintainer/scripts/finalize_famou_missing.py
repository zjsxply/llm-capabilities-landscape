#!/usr/bin/env python3
"""Finalize a bounded famou missing-paper review into bilingual apply records."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.parse
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from build_research_closure_terminal import (
    SECTION_BY_FILE,
    bullet_present,
    generic_tldr,
    markdown_bullet,
    normalize_title,
    normalize_url,
    paired_zh,
    require_target,
)


TERMINAL_DECISIONS = {"include", "reject"}


def read_list(path: Path) -> list[dict[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or any(not isinstance(row, dict) for row in value):
        raise SystemExit(f"Expected a JSON list of objects: {path}")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def unique(rows: Iterable[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        key = str(row.get("identifier") or "").strip()
        if not key or key in result:
            raise SystemExit(f"{label} has a missing or duplicate identifier: {key}")
        result[key] = row
    return result


def load_dir(directory: Path, suffix: str, label: str) -> dict[str, dict[str, Any]]:
    paths = sorted(directory.glob(suffix))
    if not paths:
        raise SystemExit(f"No {label} files in {directory}")
    return unique((row for path in paths for row in read_list(path)), label)


def stable_url(identifier: str) -> str:
    if identifier.lower().startswith("arxiv:"):
        paper_id = re.sub(r"v\d+$", "", identifier.split(":", 1)[1], flags=re.I)
        return f"https://arxiv.org/abs/{paper_id}"
    if identifier.lower().startswith("doi:"):
        doi = identifier.split(":", 1)[1]
        return f"https://doi.org/{urllib.parse.quote(doi, safe='/:')}"
    raise SystemExit(f"No stable primary URL rule for {identifier}")


def release_year(identifier: str, candidate: dict[str, Any]) -> int | None:
    raw = candidate.get("year") or candidate.get("metadata_year")
    if isinstance(raw, int) or (isinstance(raw, str) and raw.isdigit()):
        return int(raw)
    arxiv = re.fullmatch(r"arXiv:(\d{2})(\d{2})\.\d{4,5}", identifier, flags=re.I)
    if arxiv:
        return 2000 + int(arxiv.group(1))
    preprint = re.search(r"preprints(20\d{2})", identifier, flags=re.I)
    return int(preprint.group(1)) if preprint else None


def evidence_text(candidate: dict[str, Any]) -> str:
    parts = [str(candidate.get("abstract") or candidate.get("metadata_abstract") or "")]
    parts.extend(str(value) for value in candidate.get("source_contexts") or [])
    return "\n".join(parts)


def doc_index(root: Path, paths: Iterable[str]) -> tuple[dict[str, str], dict[str, str]]:
    urls: dict[str, str] = {}
    titles: dict[str, str] = {}
    pattern = re.compile(r"^- \[([^]]+)\]\((https?://[^)]+)\)")
    for relative in paths:
        with (root / relative).open(encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                match = pattern.match(line)
                if match:
                    titles.setdefault(normalize_title(match.group(1)), relative)
                    urls.setdefault(normalize_url(match.group(2)), relative)
    return urls, titles


def digest(paths: Iterable[Path]) -> str:
    value = hashlib.sha256()
    for path in sorted(paths, key=lambda item: item.as_posix()):
        value.update(path.as_posix().encode())
        value.update(path.read_bytes())
    return value.hexdigest()


def prepare(args: argparse.Namespace) -> int:
    candidates = unique(read_list(args.candidates), "candidates")
    chunks = load_dir(args.chunk_dir, "chunk-*.json", "review chunks")
    decisions = load_dir(args.decision_dir, "chunk-*.json", "review decisions")
    overrides = json.loads(args.overrides.read_text(encoding="utf-8"))
    if set(candidates) != set(chunks) or set(chunks) != set(decisions):
        raise SystemExit(
            f"Coverage mismatch: candidates={len(candidates)} chunks={len(chunks)} decisions={len(decisions)}"
        )
    invalid = [key for key, row in decisions.items() if str(row.get("decision") or "").lower() not in TERMINAL_DECISIONS]
    if invalid:
        raise SystemExit(f"Nonterminal decisions: {invalid[:20]}")
    include_ids = {key for key, row in decisions.items() if str(row.get("decision")).lower() == "include"}
    if set(overrides) != include_ids:
        raise SystemExit(
            f"Parent override coverage mismatch: overrides={len(overrides)} includes={len(include_ids)} "
            f"missing={len(include_ids - set(overrides))} extras={len(set(overrides) - include_ids)}"
        )

    allowed_docs = sorted(
        {
            "docs/en/03-downstream-applications/02-research/02-survey.md",
            "docs/en/03-downstream-applications/02-research/03-bench.md",
            "docs/en/03-downstream-applications/02-research/04-model.md",
            "docs/en/03-downstream-applications/02-research/05-agent-harness.md",
            "docs/en/03-downstream-applications/02-research/06-skill.md",
            "docs/en/02-agent-capabilities/04-deep-research/02-survey.md",
            "docs/en/02-agent-capabilities/04-deep-research/03-bench.md",
            "docs/en/02-agent-capabilities/04-deep-research/04-model.md",
            "docs/en/02-agent-capabilities/04-deep-research/05-agent-harness.md",
            "docs/en/02-agent-capabilities/04-deep-research/06-skill.md",
        }
    )
    urls, titles = doc_index(args.root, [*allowed_docs, *(paired_zh(path) for path in allowed_docs)])
    ledger: list[dict[str, Any]] = []
    apply_rows: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    for identifier, candidate in candidates.items():
        decision = decisions[identifier]
        action = str(decision.get("decision") or "").lower()
        base = {
            "identifier": identifier,
            "title": candidate.get("title") or candidate.get("metadata_title") or "",
            "url": stable_url(identifier),
            "year": release_year(identifier, candidate),
        }
        if action == "reject":
            reason = str(decision.get("reason_en") or "").strip()
            if not reason:
                raise SystemExit(f"Rejected row lacks reason: {identifier}")
            ledger.append({**base, "status": "rejected", "reason": reason, "docs": []})
            counts["rejected"] += 1
            continue

        override = overrides[identifier]
        title = str(override.get("title") or base["title"]).strip()
        target = str(override.get("target_doc") or "").strip()
        require_target(args.root, target)
        if target not in allowed_docs:
            raise SystemExit(f"Out-of-scope target for {identifier}: {target}")
        en_tldr = re.sub(r"\s+", " ", str(decision.get("en_tldr") or "")).strip()
        zh_tldr = re.sub(r"\s+", " ", str(decision.get("zh_tldr") or "")).strip()
        if not title or len(en_tldr) < 40 or len(zh_tldr) < 20 or generic_tldr(en_tldr) or generic_tldr(zh_tldr):
            raise SystemExit(f"Included row lacks a concrete title or bilingual TLDR: {identifier}")
        quote = str(decision.get("evidence_quote") or "").strip()
        source = str(decision.get("evidence_source") or "").strip()
        if len(quote) < 20:
            raise SystemExit(f"Included row lacks evidence: {identifier}")
        packet = chunks[identifier]
        if "arxiv tex" not in source.lower() and quote.lower() not in evidence_text(packet).lower():
            raise SystemExit(f"Evidence quote is not in the bounded packet: {identifier}")
        url = base["url"]
        section = SECTION_BY_FILE[Path(target).name]
        row = {
            **base,
            "title": title,
            "status": "include",
            "decision": "include",
            "section": section,
            "target_doc": target,
            "reason": str(decision.get("reason_en") or "").strip(),
            "suggested_english_bullet": markdown_bullet(title, url, en_tldr, zh=False),
            "suggested_chinese_bullet": markdown_bullet(title, url, zh_tldr, zh=True),
        }
        existing = urls.get(normalize_url(url)) or titles.get(normalize_title(title))
        if existing:
            if not existing.startswith("docs/en/"):
                existing = existing.replace("docs/zh/", "docs/en/", 1)
            row.update(
                {
                    "status": "included_existing",
                    "target_doc": existing,
                    "section": SECTION_BY_FILE[Path(existing).name],
                    "docs": [existing, paired_zh(existing)],
                }
            )
            ledger.append(row)
            counts["included_existing"] += 1
            continue
        ledger.append(row)
        apply_rows.append(row)
        counts["pending_apply"] += 1

    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.out_dir / "preapply-ledger.json", ledger)
    write_json(args.out_dir / "apply" / "chunk-001.json", apply_rows)
    metadata_paths = [args.candidates, args.overrides, *sorted(args.chunk_dir.glob("chunk-*.json")), *sorted(args.decision_dir.glob("chunk-*.json"))]
    write_json(args.out_dir / "run-metadata.json", {"source": args.registry_source, "sha256": digest(metadata_paths)})
    print(f"Candidates: {len(candidates)}")
    print(f"Included pending apply: {counts['pending_apply']}")
    print(f"Included existing aliases: {counts['included_existing']}")
    print(f"Rejected: {counts['rejected']}")
    print("Deferred/checking: 0")
    return 0


def verify(args: argparse.Namespace) -> int:
    ledger = read_list(args.out_dir / "preapply-ledger.json")
    metadata_paths = [args.candidates, args.overrides, *sorted(args.chunk_dir.glob("chunk-*.json")), *sorted(args.decision_dir.glob("chunk-*.json"))]
    stored = json.loads((args.out_dir / "run-metadata.json").read_text(encoding="utf-8"))
    if stored != {"source": args.registry_source, "sha256": digest(metadata_paths)}:
        raise SystemExit("famou closure inputs changed after prepare")
    terminal: list[dict[str, Any]] = []
    missing: list[str] = []
    for row in ledger:
        if row.get("status") == "rejected":
            terminal.append(row)
            continue
        if row.get("status") == "included_existing":
            target = str(row["target_doc"])
            zh = paired_zh(target)
            _, en_titles = doc_index(args.root, [target])
            _, zh_titles = doc_index(args.root, [zh])
            title_key = normalize_title(row.get("title") or "")
            if title_key not in en_titles or title_key not in zh_titles:
                missing.append(f"{row['identifier']} existing bilingual title")
                continue
            terminal.append({**row, "status": "included", "docs": [target, zh]})
            continue
        target = str(row["target_doc"])
        section = str(row["section"])
        zh = paired_zh(target)
        if not bullet_present(args.root / target, section, str(row["suggested_english_bullet"])):
            missing.append(f"{row['identifier']} English")
            continue
        if not bullet_present(args.root / zh, section, str(row["suggested_chinese_bullet"])):
            missing.append(f"{row['identifier']} Chinese")
            continue
        terminal.append({**row, "status": "included", "docs": [target, zh]})
    if missing or len(terminal) != len(ledger):
        raise SystemExit(f"famou applied verification failed: {missing[:20]}")
    write_json(args.out_dir / "terminal-ledger.json", terminal)
    payload = [
        {
            "identifier": row["identifier"],
            "status": row["status"],
            "title": row.get("title") or "",
            "url": row.get("url") or "",
            "docs": row.get("docs") or [],
            "note": row.get("reason") or "",
            "source": args.registry_source,
        }
        for row in terminal
    ]
    write_json(args.out_dir / "registry-payload.json", payload)
    counts = Counter(row["status"] for row in terminal)
    print(f"Terminal records: {len(terminal)}")
    print(f"Included: {counts['included']}")
    print(f"Rejected: {counts['rejected']}")
    print("Deferred/checking: 0")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--chunk-dir", type=Path, required=True)
    parser.add_argument("--decision-dir", type=Path, required=True)
    parser.add_argument("--overrides", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--registry-source", default="famou-research-landscape-missing-20260901")
    parser.add_argument("--verify-applied", action="store_true")
    args = parser.parse_args()
    return verify(args) if args.verify_applied else prepare(args)


if __name__ == "__main__":
    raise SystemExit(main())
