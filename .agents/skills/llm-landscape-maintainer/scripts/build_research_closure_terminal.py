#!/usr/bin/env python3
"""Build and verify a parent-approved Research citation-closure ledger.

The script deliberately separates approval from inclusion.  In prepare mode it
creates a small bilingual apply queue, while verify mode marks a paper included
only after the English and Chinese bullets are both present in official docs.
Official Markdown is indexed line by line so large split-tree files are never
loaded into one in-memory string.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.parse
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


ALLOWED_ROOTS = (
    "docs/en/03-downstream-applications/02-research/",
    "docs/en/02-agent-capabilities/04-deep-research/",
)
SECTION_BY_FILE = {
    "02-survey.md": "Survey",
    "03-bench.md": "Bench",
    "04-model.md": "Model",
    "05-agent-harness.md": "Agent Harness",
    "06-skill.md": "Skill",
}
ACCEPT_ACTIONS = {"approve", "reclassify"}
STRICT_ACTIONS = {"include", "reject"}
GENERIC_TLDR_PATTERNS = (
    re.compile(r"\b(?:adds?|contributes?|provides?) (?:an? )?(?:research )?(?:bench|model|survey|agent harness) (?:entry|candidate)\b", re.I),
    re.compile(r"\b(?:contributes?|proposes?) (?:an? )?(?:model-side|agentic) (?:method|workflow) for\b", re.I),
    re.compile(r"\b(?:candidate|suitable) for (?:the )?(?:research|deep research)\b", re.I),
    re.compile(r"(?:围绕.+(?:补充|构建)|为.+补充(?:模型|基准|综述|智能体)|适合纳入.+(?:模型|基准|综述|智能体))"),
)
BIOMED_TITLE_RE = re.compile(
    r"\b(?:biomedical|clinical|medical|medicine|healthcare|patient|hospital|"
    r"disease|diagnosis|therapy|therapeutic|drug|pharma|cancer|tumou?r|"
    r"protein|genom(?:e|ic)|gene|omics|antibody|cellular|molecular|radiology|"
    r"pathology|nursing|surgery|surgical|pubmed|"
    r"dentistry|dental|ophthalm(?:ology|ic)|bioinformatics|life[- ]science|"
    r"biology|genetic|neuroscience|epidemiolog|pharmacolog|microbiolog|"
    r"immunolog|clinical trial)\b",
    re.I,
)


def load_list(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"Expected a JSON list: {path}")
    invalid = [index for index, row in enumerate(data) if not isinstance(row, dict)]
    if invalid:
        raise SystemExit(f"Expected every row to be an object in {path}; invalid indexes: {invalid[:20]}")
    return data


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def canonical(value: Any) -> str:
    value = str(value or "").strip()
    arxiv_doi = re.fullmatch(r"DOI:10\.48550/arxiv\.(\d{4}\.\d{4,5})(?:v\d+)?", value, re.I)
    if arxiv_doi:
        return f"arXiv:{arxiv_doi.group(1)}"
    if value.lower().startswith("arxiv:"):
        return "arXiv:" + re.sub(r"v\d+$", "", value.split(":", 1)[1], flags=re.I)
    if value.lower().startswith("doi:"):
        return "DOI:" + value.split(":", 1)[1].lower()
    return value


def normalize_title(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def normalize_url(value: Any) -> str:
    url = urllib.parse.unquote(str(value or "").strip()).replace("http://", "https://")
    url = re.sub(r"/+$", "", url).lower()
    arxiv = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", url)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv.group(1)}"
    return url


def stable_url(row: dict[str, Any]) -> str:
    identifier = canonical(row.get("identifier"))
    if identifier.startswith("arXiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    if identifier.startswith("DOI:"):
        doi = identifier.split(":", 1)[1]
        return f"https://doi.org/{urllib.parse.quote(doi, safe='/:')}"
    return str(row.get("url") or row.get("stable_url") or "").strip()


def validate_primary_url(url: str, identifier: str) -> None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SystemExit(f"Approved row lacks an HTTP(S) primary URL: {identifier}: {url}")
    if "semanticscholar.org" in parsed.netloc.lower():
        raise SystemExit(f"Approved row uses a Semantic Scholar URL: {identifier}")


def text_value(row: dict[str, Any], *keys: str, language: str | None = None) -> str:
    for key in keys:
        value = row.get(key)
        if value is None:
            continue
        if isinstance(value, dict):
            candidates = [language, "en" if language == "english" else None, "zh" if language == "chinese" else None]
            value = next((value.get(name) for name in candidates if name and value.get(name)), "")
        if isinstance(value, list):
            value = "; ".join(str(part) for part in value if part)
        value = re.sub(r"\s+", " ", str(value or "")).strip()
        if value:
            return value
    return ""


def reason(row: dict[str, Any]) -> str:
    return text_value(
        row,
        "reason",
        "reason_en",
        "rationale",
        "note",
        "concise_en",
        "evidence_en",
        "evidence_summary",
        "evidence",
        language="english",
    )


def description_from_bullet(value: Any) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return re.sub(r"^-\s*\[[^]]+\]\([^)]+\)\s*[:：]\s*", "", text).strip()


def tldr(row: dict[str, Any], *, zh: bool) -> str:
    if zh:
        value = text_value(
            row,
            "zh_tldr",
            "tldr_zh",
            "concise_zh",
            "suggested_chinese_bullet",
            "chinese_bullet",
            "tldr",
            language="chinese",
        )
    else:
        value = text_value(
            row,
            "en_tldr",
            "tldr_en",
            "concise_en",
            "suggested_english_bullet",
            "english_bullet",
            "tldr",
            language="english",
        )
    return description_from_bullet(value).rstrip("。. ")


def paired_zh(path: str) -> str:
    if not path.startswith("docs/en/"):
        raise SystemExit(f"Expected English split-tree path: {path}")
    return path.replace("docs/en/", "docs/zh/", 1)


def target_from(row: dict[str, Any]) -> str:
    raw = text_value(row, "target_doc_en", "target_doc", "target_docs", "docs")
    match = re.search(r"docs/en/[^\s;,)]*\.md", raw)
    return match.group(0) if match else raw


def allowed_target_paths(root: Path) -> set[str]:
    return {path.relative_to(root).as_posix() for path in iter_topic_docs(root)}


def require_target(root: Path, target: str) -> None:
    allowed = allowed_target_paths(root)
    if target not in allowed:
        raise SystemExit(f"Noncanonical or out-of-scope target: {target}")
    zh = paired_zh(target)
    if not (root / zh).is_file():
        raise SystemExit(f"Missing paired Chinese target: {zh}")
    expected = section_from_target(target).lower()
    for path in (root / target, root / zh):
        found = False
        with path.open(encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
                if match and section_label(match.group(1)) == expected:
                    found = True
                    break
        if not found:
            raise SystemExit(f"Expected section {expected!r} is missing from {path}")


def section_from_target(target: str) -> str:
    return SECTION_BY_FILE.get(Path(target).name, "")


def section_label(value: str) -> str:
    match = re.match(r"\d+(?:\.\d+)+\s+(.+)$", value.strip())
    label = match.group(1) if match else value
    return re.sub(r"\s+", " ", label).strip().lower()


def markdown_bullet(title: str, url: str, description: str, *, zh: bool) -> str:
    title = title.replace("[", "(").replace("]", ")")
    separator = "：" if zh else ": "
    suffix = "。" if zh else "."
    return f"- [{title}]({url}){separator}{description.rstrip('。. ')}{suffix}"


def generic_tldr(value: str) -> bool:
    return any(pattern.search(value) for pattern in GENERIC_TLDR_PATTERNS)


def normalize_description(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().rstrip("。. ")


def parse_bullet(value: str) -> tuple[str, str, str]:
    match = re.match(r"^-\s*\[([^]]+)\]\((https?://[^)]+)\)\s*[:：]\s*(.+?)\s*$", value.strip())
    if not match:
        raise SystemExit(f"Malformed approved bullet: {value[:200]}")
    title, url, description = match.groups()
    return normalize_title(title), normalize_url(url), normalize_description(description)


def bullet_present(path: Path, section: str, expected_bullet: str) -> bool:
    expected = parse_bullet(expected_bullet)
    wanted_label = section.lower()
    active = False
    active_level = 0
    with path.open(encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
            if heading:
                level = len(heading.group(1))
                label = section_label(heading.group(2))
                if label == wanted_label:
                    active = True
                    active_level = level
                elif active and level <= active_level:
                    active = False
                continue
            if not active or not line.startswith("- ["):
                continue
            try:
                actual = parse_bullet(line)
            except SystemExit:
                continue
            if actual == expected:
                return True
    return False


def iter_topic_docs(root: Path) -> Iterable[Path]:
    for prefix in ALLOWED_ROOTS:
        directory = root / prefix
        for filename in SECTION_BY_FILE:
            path = directory / filename
            if path.is_file():
                yield path


def markdown_index(root: Path) -> dict[str, dict[str, str]]:
    index = {"url": {}, "title": {}, "identifier": {}}
    bullet_re = re.compile(r"^- \[([^]]+)\]\((https?://[^)]+)\)")
    for path in iter_topic_docs(root):
        relative = path.relative_to(root).as_posix()
        with path.open(encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                match = bullet_re.match(line)
                if not match:
                    continue
                title, url = match.groups()
                index["title"].setdefault(normalize_title(title), relative)
                index["url"].setdefault(normalize_url(url), relative)
                arxiv = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url, re.I)
                doi = re.search(r"doi\.org/(10\.[^)\s]+)", url, re.I)
                if arxiv:
                    index["identifier"].setdefault(canonical(f"arXiv:{arxiv.group(1)}"), relative)
                if doi:
                    index["identifier"].setdefault(canonical(f"DOI:{urllib.parse.unquote(doi.group(1))}"), relative)
    return index


def existing_doc(row: dict[str, Any], index: dict[str, dict[str, str]]) -> str:
    checks = (
        ("identifier", canonical(row.get("identifier"))),
        ("url", normalize_url(stable_url(row))),
        ("title", normalize_title(row.get("title"))),
    )
    for kind, value in checks:
        if value and value in index[kind]:
            return index[kind][value]
    return ""


def is_biomedical(row: dict[str, Any]) -> bool:
    # This is only a conservative title gate. Transferable methods with a
    # biomedical case study are decided by the strict abstract review.
    title = str(row.get("title") or "")
    return bool(BIOMED_TITLE_RE.search(title))


def load_unique(rows: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        key = canonical(row.get("identifier"))
        if not key:
            raise SystemExit(f"{label} contains a row without identifier")
        if key in result:
            raise SystemExit(f"{label} contains duplicate identifier: {key}")
        result[key] = {**row, "identifier": key}
    return result


def load_decisions(directory: Path) -> dict[str, dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(directory.glob("chunk-[0-9][0-9][0-9].json")):
        rows.extend(load_list(path))
    return load_unique(rows, "decisions")


def load_qa(directory: Path) -> dict[str, dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(directory.glob("qa-*.json")):
        rows.extend(load_list(path))
    return load_unique(rows, "parent QA")


def load_chunk_dir(directory: Path, pattern: str, label: str) -> dict[str, dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    files = sorted(directory.glob(pattern))
    if not files:
        raise SystemExit(f"No {label} files found in {directory}")
    for path in files:
        rows.extend(load_list(path))
    return load_unique(rows, label)


def digest_paths(paths: Iterable[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths, key=lambda item: item.as_posix()):
        digest.update(path.as_posix().encode("utf-8"))
        digest.update(b"\0")
        with path.open("rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
        digest.update(b"\0")
    return digest.hexdigest()


def input_metadata(args: argparse.Namespace) -> dict[str, Any]:
    groups: dict[str, list[Path]] = {
        "candidates": [args.candidates],
        "auto_reject": [args.auto_reject],
        "decisions": sorted(args.decision_dir.glob("chunk-[0-9][0-9][0-9].json")),
        "parent_qa": sorted(args.qa_dir.glob("qa-*.json")),
    }
    if args.strict_chunk_dir or args.strict_decision_dir:
        if not args.strict_chunk_dir or not args.strict_decision_dir:
            raise SystemExit("--strict-chunk-dir and --strict-decision-dir must be supplied together")
        groups["strict_chunks"] = sorted(args.strict_chunk_dir.glob("chunk-*.json"))
        groups["strict_decisions"] = sorted(args.strict_decision_dir.glob("chunk-*.json"))
    if args.final_scope_chunk_dir or args.final_scope_decision_dir:
        if not args.final_scope_chunk_dir or not args.final_scope_decision_dir:
            raise SystemExit("--final-scope-chunk-dir and --final-scope-decision-dir must be supplied together")
        groups["final_scope_chunks"] = sorted(args.final_scope_chunk_dir.glob("chunk-*.json"))
        groups["final_scope_decisions"] = sorted(args.final_scope_decision_dir.glob("chunk-*.json"))
    empty = [name for name, paths in groups.items() if not paths]
    if empty:
        raise SystemExit(f"Missing input file groups: {empty}")
    return {
        "source": args.registry_source,
        "groups": {
            name: {"files": [path.as_posix() for path in paths], "sha256": digest_paths(paths)}
            for name, paths in groups.items()
        },
    }


def prepare(args: argparse.Namespace) -> int:
    metadata = input_metadata(args)
    candidates = load_unique(load_list(args.candidates), "candidates")
    automatic = load_unique(load_list(args.auto_reject), "auto rejects")
    decisions = load_decisions(args.decision_dir)
    qa = load_qa(args.qa_dir)
    strict_packets: dict[str, dict[str, Any]] = {}
    strict_decisions: dict[str, dict[str, Any]] = {}
    scope_packets: dict[str, dict[str, Any]] = {}
    scope_decisions: dict[str, dict[str, Any]] = {}
    if args.strict_chunk_dir:
        strict_packets = load_chunk_dir(args.strict_chunk_dir, "chunk-*.json", "strict QA packets")
        strict_decisions = load_chunk_dir(args.strict_decision_dir, "chunk-*.json", "strict QA decisions")
        if set(strict_packets) != set(strict_decisions):
            raise SystemExit(
                f"Strict QA coverage mismatch: packets={len(strict_packets)} decisions={len(strict_decisions)} "
                f"missing={len(set(strict_packets) - set(strict_decisions))} "
                f"extras={len(set(strict_decisions) - set(strict_packets))}"
            )
    if args.final_scope_chunk_dir:
        if not strict_decisions:
            raise SystemExit("Final scope QA requires strict QA inputs")
        scope_packets = load_chunk_dir(args.final_scope_chunk_dir, "chunk-*.json", "final scope QA packets")
        scope_decisions = load_chunk_dir(args.final_scope_decision_dir, "chunk-*.json", "final scope QA decisions")
        strict_includes = {
            key for key, row in strict_decisions.items() if str(row.get("final_action") or "").lower() == "include"
        }
        if set(scope_packets) != set(scope_decisions) or set(scope_decisions) != strict_includes:
            raise SystemExit(
                f"Final scope QA coverage mismatch: packets={len(scope_packets)} decisions={len(scope_decisions)} "
                f"strict_includes={len(strict_includes)}"
            )
    if set(automatic) & set(decisions):
        raise SystemExit("Automatic and reviewed decision sets overlap")
    invalid_auto = [key for key, row in automatic.items() if str(row.get("status") or "").lower() != "rejected"]
    if invalid_auto:
        raise SystemExit(f"Auto-reject rows lack status=rejected: {invalid_auto[:20]}")
    coverage = set(automatic) | set(decisions)
    if coverage != set(candidates):
        raise SystemExit(
            f"Decision coverage mismatch: covered={len(coverage)} candidates={len(candidates)} "
            f"missing={len(set(candidates) - coverage)} extras={len(coverage - set(candidates))}"
        )

    raw_includes = {key for key, row in decisions.items() if str(row.get("decision") or "").lower() == "include"}
    if set(qa) != raw_includes:
        raise SystemExit(
            f"QA coverage mismatch: qa={len(qa)} includes={len(raw_includes)} "
            f"missing={len(raw_includes - set(qa))} extras={len(set(qa) - raw_includes)}"
        )

    index = markdown_index(args.root)
    apply_rows: list[dict[str, Any]] = []
    approved: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    strict_consumed: set[str] = set()
    scope_consumed: set[str] = set()

    for key, candidate in candidates.items():
        base = {
            "identifier": key,
            "title": candidate.get("title") or "",
            "url": stable_url(candidate),
            "year": candidate.get("year"),
        }
        if key in automatic:
            note = reason(automatic[key]) or "Rejected by the abstract-aware Research scope pre-screen."
            ledger.append({**base, "status": "rejected", "reason": note, "source": "automatic_scope_reject"})
            counts["rejected"] += 1
            continue

        raw = decisions[key]
        if str(raw.get("decision") or "").lower() != "include":
            note = reason(raw)
            if not note:
                raise SystemExit(f"Rejected review row lacks a reason: {key}")
            ledger.append({**base, "status": "rejected", "reason": note, "source": "abstract_review"})
            counts["rejected"] += 1
            continue

        review = qa[key]
        action = str(review.get("action") or "").lower()
        if action not in ACCEPT_ACTIONS:
            note = reason(review) or "Rejected by parent taxonomy QA."
            ledger.append({**base, "status": "rejected", "reason": note, "source": "parent_qa"})
            counts["qa_rejected"] += 1
            continue

        has_strict_review = key in strict_decisions
        if has_strict_review:
            strict_consumed.add(key)
        if key in scope_decisions:
            scope_consumed.add(key)
        if is_biomedical(candidate):
            ledger.append(
                {
                    **base,
                    "status": "rejected",
                    "reason": "Excluded from this closure because the paper is biomedical, clinical, or life-science vertical work.",
                    "source": "parent_biomedical_exclusion",
                }
            )
            counts["biomedical_excluded"] += 1
            continue

        if has_strict_review:
            packet = strict_packets[key]
            target = text_value(packet, "current_target_doc")
            review_en_tldr = description_from_bullet(packet.get("current_english_bullet"))
            review_zh_tldr = description_from_bullet(packet.get("current_chinese_bullet"))
            review_reason = "Queued for strict abstract-backed parent review."
        else:
            target = target_from(review)
            review_en_tldr = tldr(review, zh=False)
            review_zh_tldr = tldr(review, zh=True)
            review_reason = text_value(review, "reason", "reason_en", "rationale", "note", language="english")
        if not target or not review_en_tldr or not review_zh_tldr or not review_reason:
            raise SystemExit(f"Accepted parent-QA row lacks its own target, bilingual TLDR, or rationale: {key}")
        if target not in allowed_target_paths(args.root):
            note = reason(review) or "Parent QA routed this paper outside Research and Deep Research."
            ledger.append(
                {
                    **base,
                    "status": "rejected",
                    "reason": f"Out of scope for this Research-only closure; routed to {target or 'another capability category'}. {note}",
                    "source": "parent_qa_route_elsewhere",
                }
            )
            counts["routed_elsewhere"] += 1
            continue
        require_target(args.root, target)

        en_tldr = review_en_tldr
        zh_tldr = review_zh_tldr
        final_reason = review_reason
        if strict_decisions:
            if key not in strict_decisions or key not in strict_packets:
                raise SystemExit(f"Provisionally approved row lacks strict QA: {key}")
            strict = strict_decisions[key]
            packet = strict_packets[key]
            final_action = str(strict.get("final_action") or "").lower()
            if final_action not in STRICT_ACTIONS:
                raise SystemExit(f"Invalid strict QA action for {key}: {final_action}")
            strict_reason = text_value(strict, "reason_en", "reason")
            if not strict_reason:
                raise SystemExit(f"Strict QA row lacks reason_en: {key}")
            if final_action == "reject":
                ledger.append({**base, "status": "rejected", "reason": strict_reason, "source": "strict_parent_qa"})
                counts["strict_qa_rejected"] += 1
                continue
            evidence = text_value(strict, "evidence_quote")
            abstract = str(candidate.get("abstract") or candidate.get("metadata_abstract") or "").strip()
            if len(evidence) < 20 or not abstract or evidence.lower() not in abstract.lower():
                raise SystemExit(f"Strict include lacks abstract evidence: {key}")
            target = target_from(strict)
            require_target(args.root, target)
            tldr_ok = strict.get("tldr_ok")
            if not isinstance(tldr_ok, bool):
                raise SystemExit(f"Strict include lacks boolean tldr_ok: {key}")
            if tldr_ok:
                en_tldr = description_from_bullet(packet.get("current_english_bullet"))
                zh_tldr = description_from_bullet(packet.get("current_chinese_bullet"))
            else:
                en_tldr = text_value(strict, "revised_en_tldr")
                zh_tldr = text_value(strict, "revised_zh_tldr")
            final_reason = strict_reason
            if scope_decisions:
                scope = scope_decisions[key]
                scope_action = str(scope.get("final_action") or "").lower()
                scope_reason = text_value(scope, "reason_en", "reason")
                if scope_action not in STRICT_ACTIONS or not scope_reason:
                    raise SystemExit(f"Invalid final scope QA row: {key}")
                if scope_action == "reject":
                    ledger.append({**base, "status": "rejected", "reason": scope_reason, "source": "final_scope_qa"})
                    counts["final_scope_rejected"] += 1
                    continue
                target = target_from(scope)
                require_target(args.root, target)
                final_reason = scope_reason
        if len(en_tldr) < 40 or len(zh_tldr) < 20:
            raise SystemExit(f"Approved row lacks a concrete bilingual TLDR: {key}")
        if generic_tldr(en_tldr) or generic_tldr(zh_tldr):
            raise SystemExit(f"Approved row contains a generic TLDR template: {key}")
        url = stable_url(candidate)
        validate_primary_url(url, key)
        section = section_from_target(target)
        approved_row = {
            **base,
            "url": url,
            "status": "approved",
            "decision": "include",
            "section": section,
            "target_doc": target,
            "reason": final_reason,
            "suggested_english_bullet": markdown_bullet(str(base["title"]), url, en_tldr, zh=False),
            "suggested_chinese_bullet": markdown_bullet(str(base["title"]), url, zh_tldr, zh=True),
        }
        found = existing_doc(approved_row, index)
        if found:
            if found != target:
                raise SystemExit(f"Approved row already exists in the wrong target: {key}: {found} != {target}")
            zh_path = paired_zh(target)
            if not bullet_present(args.root / target, section, approved_row["suggested_english_bullet"]):
                raise SystemExit(f"Existing English row does not match the approved bullet: {key}")
            if not bullet_present(args.root / zh_path, section, approved_row["suggested_chinese_bullet"]):
                raise SystemExit(f"Existing Chinese row does not match the approved bullet: {key}")
            approved_row["status"] = "included_existing"
            counts["included_existing"] += 1
        else:
            apply_rows.append({**approved_row, "status": "include", "decision": "include"})
            counts["pending_apply"] += 1
        approved.append(approved_row)
        ledger.append(approved_row)

    if strict_decisions and strict_consumed != set(strict_decisions):
        raise SystemExit(
            f"Strict QA does not match the provisional apply queue: consumed={len(strict_consumed)} "
            f"strict={len(strict_decisions)} extras={len(set(strict_decisions) - strict_consumed)}"
        )
    if scope_decisions and scope_consumed != set(scope_decisions):
        raise SystemExit(
            f"Final scope QA was not fully consumed: consumed={len(scope_consumed)} "
            f"scope={len(scope_decisions)} extras={len(set(scope_decisions) - scope_consumed)}"
        )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.out_dir / "preapply-ledger.json", ledger)
    write_json(args.out_dir / "parent-approved.json", approved)
    write_json(args.out_dir / "apply" / "chunk-001.json", apply_rows)
    write_json(args.out_dir / "run-metadata.json", metadata)
    report = [
        "# Research Closure Parent Finalization",
        "",
        f"- Candidates: {len(candidates)}",
        f"- Automatic rejects: {len(automatic)}",
        f"- Abstract-reviewed rows: {len(decisions)}",
        f"- Raw include recommendations: {len(raw_includes)}",
        f"- Parent QA rows: {len(qa)}",
        f"- Existing approved entries: {counts['included_existing']}",
        f"- New approved entries pending apply: {counts['pending_apply']}",
        f"- Parent-QA rejects: {counts['qa_rejected']}",
        f"- Strict parent-QA rejects: {counts['strict_qa_rejected']}",
        f"- Final scope-QA rejects: {counts['final_scope_rejected']}",
        f"- Routed outside Research/Deep Research: {counts['routed_elsewhere']}",
        f"- Biomedical/clinical exclusions after QA: {counts['biomedical_excluded']}",
        f"- Deferred/checking: 0",
    ]
    (args.out_dir / "prepare-report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(line[2:] for line in report if line.startswith("- ")))
    return 0


def verify(args: argparse.Namespace) -> int:
    metadata_path = args.out_dir / "run-metadata.json"
    stored_metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    current_metadata = input_metadata(args)
    if stored_metadata != current_metadata:
        raise SystemExit("Closure inputs changed after prepare; rerun prepare before verify")
    ledger = load_list(args.out_dir / "preapply-ledger.json")
    terminal: list[dict[str, Any]] = []
    missing: list[str] = []
    for row in ledger:
        status = str(row.get("status") or "")
        if status == "rejected":
            terminal.append({**row, "docs": []})
            continue
        target = str(row.get("target_doc") or "")
        require_target(args.root, target)
        section = str(row.get("section") or section_from_target(target))
        zh_path = paired_zh(target)
        if not bullet_present(args.root / target, section, str(row.get("suggested_english_bullet") or "")):
            missing.append(f"{row.get('identifier')} (English approved bullet mismatch)")
            continue
        if not bullet_present(args.root / zh_path, section, str(row.get("suggested_chinese_bullet") or "")):
            missing.append(f"{row.get('identifier')} (Chinese approved bullet mismatch)")
            continue
        terminal.append(
            {
                **row,
                "status": "included",
                "target_doc": target,
                "docs": [target, zh_path],
                "reason": reason(row) or "Included after parent QA and bilingual document verification.",
            }
        )
    if missing:
        raise SystemExit(f"Approved rows missing after apply ({len(missing)}): {missing[:20]}")
    if len(terminal) != len(ledger):
        raise SystemExit(f"Terminal ledger covers {len(terminal)} of {len(ledger)} rows")
    invalid = [row for row in terminal if row.get("status") not in {"included", "rejected"}]
    if invalid:
        raise SystemExit(f"Terminal ledger has {len(invalid)} nonterminal rows")
    write_json(args.out_dir / "terminal-ledger.json", terminal)
    payload = [
        {
            "identifier": row["identifier"],
            "status": row["status"],
            "title": row.get("title") or "",
            "url": row.get("url") or "",
            "docs": row.get("docs") or [],
            "note": reason(row),
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


def markdown_index_for_paths(root: Path, paths: Iterable[Path]) -> dict[str, dict[str, str]]:
    index = {"url": {}, "title": {}, "identifier": {}}
    bullet_re = re.compile(r"^- \[([^]]+)\]\((https?://[^)]+)\)")
    for path in paths:
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        with path.open(encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                match = bullet_re.match(line)
                if not match:
                    continue
                title, url = match.groups()
                index["title"].setdefault(normalize_title(title), relative)
                index["url"].setdefault(normalize_url(url), relative)
                arxiv = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url, re.I)
                doi = re.search(r"doi\.org/(10\.[^)\s]+)", url, re.I)
                if arxiv:
                    index["identifier"].setdefault(canonical(f"arXiv:{arxiv.group(1)}"), relative)
                if doi:
                    index["identifier"].setdefault(canonical(f"DOI:{urllib.parse.unquote(doi.group(1))}"), relative)
    return index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--auto-reject", type=Path, required=True)
    parser.add_argument("--decision-dir", type=Path, required=True)
    parser.add_argument("--qa-dir", type=Path, required=True)
    parser.add_argument("--strict-chunk-dir", type=Path)
    parser.add_argument("--strict-decision-dir", type=Path)
    parser.add_argument("--final-scope-chunk-dir", type=Path)
    parser.add_argument("--final-scope-decision-dir", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--registry-source", default="research-closure-20260831-iteration-3-final")
    parser.add_argument("--verify-applied", action="store_true")
    args = parser.parse_args()
    return verify(args) if args.verify_applied else prepare(args)


if __name__ == "__main__":
    raise SystemExit(main())
