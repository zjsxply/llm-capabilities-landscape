#!/usr/bin/env python3
"""Parent-review rejected-candidate recall decisions for Survey/Model sections."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
APPLY_SCRIPT = SCRIPT_DIR / "apply_candidate_inclusions.py"


def load_apply_module():
    spec = importlib.util.spec_from_file_location("apply_candidate_inclusions", APPLY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {APPLY_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


APPLY = load_apply_module()


BIO_TERMS = [
    "biomedical",
    "biomedicine",
    "clinical",
    "healthcare",
    "patient",
    "disease",
    "diagnosis",
    "radiology",
    "pathology",
    "histology",
    "mri",
    "ct scan",
    "ultrasound",
    "eeg",
    "ecg",
    "tumor",
    "tumour",
    "cancer",
    "oncology",
    "liver",
    "lung",
    "kidney",
    "retina",
    "dermatology",
    "protein",
    "genomic",
    "omics",
    "gene",
    "cell",
    "drug",
    "molecule",
    "molecular",
    "biology",
    "ehr",
    "mimic",
    "nursing",
    "doctor",
    "mental health",
    "caregiver",
    "pharma",
    "hospital",
    "therapy",
    "therapeutic",
    "microscopy",
]
BIO_RE = re.compile(r"\b(?:" + "|".join(re.escape(term) for term in BIO_TERMS) + r")\b", re.I)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def normalize_url(url: str) -> str:
    value = re.sub(r"/+$", "", url.strip()).replace("http://", "https://")
    return value.lower()


def arxiv_id_from(text: str) -> str:
    match = re.search(r"(?:arxiv:|arxiv\.org/abs/)(\d{4}\.\d{4,5})", text or "", re.I)
    return match.group(1) if match else ""


def stable_url(item: dict[str, Any]) -> str:
    url = str(item.get("stable_url") or item.get("url") or "").strip()
    identifier = str(item.get("identifier") or "").strip()
    if identifier.lower().startswith("arxiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    if not url and identifier.lower().startswith("doi:"):
        doi = identifier.split(":", 1)[1]
        return f"https://doi.org/{urllib.parse.quote(doi, safe='/:')}"
    doi_match = re.match(r"https?://doi\.org/(.+)$", url, re.I)
    if doi_match:
        return f"https://doi.org/{urllib.parse.quote(urllib.parse.unquote(doi_match.group(1)), safe='/:')}"
    return url


def source_rank(item: dict[str, Any]) -> int:
    url = stable_url(item).lower()
    identifier = str(item.get("identifier") or "").lower()
    if "arxiv.org/abs/" in url or identifier.startswith("arxiv:"):
        return 0
    if "openreview.net" in url:
        return 1
    if "proceedings.mlr.press" in url or "aclanthology.org" in url:
        return 2
    if "doi.org/10.48550/arxiv" in url or identifier.startswith("doi:10.48550/arxiv"):
        return 3
    if "doi.org/" in url:
        return 4
    return 5


def paired_zh(path: str) -> str:
    return path.replace("docs/en/", "docs/zh/", 1)


def section_exists(path: Path, section: str) -> bool:
    try:
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        APPLY.find_section_bounds(lines, section)
        return True
    except Exception:
        return False


def safe_title(title: str) -> str:
    value = re.sub(r"\s+", " ", title or "").strip()
    return value.replace("[", "(").replace("]", ")") or "Untitled"


def description_from_bullet(bullet: Any, *, zh: bool) -> str:
    text = str(bullet or "")
    markers = [")：" if zh else "):", "：", ":"]
    for marker in markers:
        if marker in text:
            return text.split(marker, 1)[1].strip()
    return ""


def clean_english_description(desc: str, item: dict[str, Any]) -> str:
    desc = re.sub(r"^include[:：]\s*", "", desc or "", flags=re.I)
    desc = re.sub(r"\s+", " ", desc).strip()
    if not desc:
        kind = "survey" if item.get("section") == "Survey" else "model-side contribution"
        desc = f"Adds a {kind} relevant to this capability area."
    if desc and desc[0].islower():
        desc = desc[0].upper() + desc[1:]
    return desc


def clean_chinese_description(desc: str) -> str:
    desc = re.sub(r"^include[:：]\s*", "", desc or "", flags=re.I)
    desc = re.sub(r"\s+", " ", desc).strip()
    return desc or "补充该能力方向下的综述或模型侧相关工作。"


def rewrite_bullets(item: dict[str, Any]) -> None:
    title = safe_title(str(item.get("title") or ""))
    url = stable_url(item)
    en_desc = clean_english_description(description_from_bullet(item.get("suggested_english_bullet"), zh=False), item)
    zh_desc = clean_chinese_description(description_from_bullet(item.get("suggested_chinese_bullet"), zh=True))
    item["stable_url"] = url
    item["suggested_english_bullet"] = f"- [{title}]({url}): {en_desc}"
    item["suggested_chinese_bullet"] = f"- [{title}]({url})：{zh_desc}"


def load_docs_text(root: Path) -> tuple[str, set[str]]:
    text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in sorted((root / "docs").glob("**/*.md"))
    )
    urls = {normalize_url(url) for url in re.findall(r"https?://[^)\s]+", text)}
    return text.lower(), urls


def load_decisions(decision_dir: Path) -> dict[str, list[dict[str, Any]]]:
    chunks: dict[str, list[dict[str, Any]]] = {}
    for path in sorted(decision_dir.glob("chunk-[0-9][0-9][0-9].json")):
        data = read_json(path)
        if not isinstance(data, list):
            raise SystemExit(f"Expected JSON list: {path}")
        chunks[path.name] = [item if isinstance(item, dict) else {} for item in data]
    if not chunks:
        raise SystemExit(f"No canonical chunk-*.json decision files found in {decision_dir}")
    return chunks


def duplicate_keep_keys(chunks: dict[str, list[dict[str, Any]]]) -> tuple[set[tuple[str, int]], list[tuple[dict[str, Any], dict[str, Any]]]]:
    by_title: dict[str, list[tuple[str, int, dict[str, Any]]]] = defaultdict(list)
    for chunk_name, rows in chunks.items():
        for index, item in enumerate(rows):
            if str(item.get("decision") or "").lower() == "include":
                title = normalize_title(str(item.get("title") or ""))
                if title:
                    by_title[title].append((chunk_name, index, item))

    keep: set[tuple[str, int]] = set()
    duplicates: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for rows in by_title.values():
        rows = sorted(rows, key=lambda entry: (source_rank(entry[2]), entry[0], entry[1]))
        keep.add((rows[0][0], rows[0][1]))
        for duplicate in rows[1:]:
            duplicates.append((duplicate[2], rows[0][2]))
    return keep, duplicates


def review(args: argparse.Namespace) -> tuple[list[dict[str, Any]], Counter[str], list[tuple[dict[str, Any], dict[str, Any]]]]:
    chunks = load_decisions(args.decision_dir)
    docs_lower, existing_urls = load_docs_text(args.root)
    keep_keys, duplicates = duplicate_keep_keys(chunks)
    reasons: Counter[str] = Counter()
    included: list[dict[str, Any]] = []

    for chunk_name, rows in chunks.items():
        reviewed: list[dict[str, Any]] = []
        for index, raw_item in enumerate(rows):
            item = dict(raw_item)
            decision = str(item.get("decision") or "").lower()
            if decision == "include":
                url = stable_url(item)
                target = str(item.get("target_doc") or item.get("target_en") or "").strip()
                section = str(item.get("section") or "").strip()
                zh_path = paired_zh(target) if target else ""
                if not target:
                    item["decision"] = "defer"
                    item["reason"] = "Parent downgrade: include item lacks current split-tree target_doc."
                    reasons["missing target_doc"] += 1
                elif not (args.root / target).exists():
                    item["decision"] = "defer"
                    item["reason"] = f"Parent downgrade: target_doc does not exist in current split tree: {target}"
                    reasons["missing target path"] += 1
                elif not (args.root / zh_path).exists():
                    item["decision"] = "defer"
                    item["reason"] = f"Parent downgrade: paired Chinese target does not exist for {target}"
                    reasons["missing zh path"] += 1
                elif section not in {"Survey", "Model"}:
                    item["decision"] = "defer"
                    item["reason"] = "Parent downgrade: reconsider pass only applies Survey or Model items."
                    reasons["not survey/model"] += 1
                elif not section_exists(args.root / target, section):
                    item["decision"] = "defer"
                    item["reason"] = f"Parent downgrade: target file does not contain a {section} section heading."
                    reasons["section missing in target"] += 1
                elif (chunk_name, index) not in keep_keys:
                    kept = next((kept for duplicate, kept in duplicates if duplicate is raw_item), None)
                    item["decision"] = "defer"
                    kept_id = kept.get("identifier") if kept else "another record"
                    item["reason"] = f"Parent downgrade: duplicate title; canonical entry kept as {kept_id}."
                    reasons["duplicate title"] += 1
                elif BIO_RE.search(
                    " ".join(
                        str(item.get(field) or "")
                        for field in ("title", "suggested_english_bullet", "suggested_chinese_bullet")
                    )
                ):
                    item["decision"] = "reject"
                    item["reason"] = "Parent reject: biomedical, clinical, drug, molecular, healthcare, or patient-facing scope is excluded for this task."
                    reasons["biomedical title/bullet"] += 1
                elif normalize_url(url) and normalize_url(url) in existing_urls:
                    item["decision"] = "defer"
                    item["reason"] = "Parent downgrade: stable URL already appears in current docs."
                    reasons["already url"] += 1
                elif arxiv_id_from(url) and arxiv_id_from(url) in docs_lower:
                    item["decision"] = "defer"
                    item["reason"] = "Parent downgrade: arXiv identifier already appears in current docs."
                    reasons["already arxiv id"] += 1
                elif str(item.get("identifier") or "").lower().startswith("doi:") and str(item["identifier"])[4:].lower() in docs_lower:
                    item["decision"] = "defer"
                    item["reason"] = "Parent downgrade: DOI already appears in current docs."
                    reasons["already doi"] += 1
                elif item.get("title") and str(item["title"]).lower() in docs_lower:
                    item["decision"] = "defer"
                    item["reason"] = "Parent downgrade: exact title already appears in current docs."
                    reasons["already title"] += 1
                else:
                    item["target_doc"] = target
                    item["target_en"] = target
                    item["target_zh"] = zh_path
                    rewrite_bullets(item)
                    included.append(item)
            reviewed.append(item)
        write_json(args.out_dir / chunk_name, reviewed)

    return included, reasons, duplicates


def write_report(path: Path, *, chunks: int, included: list[dict[str, Any]], reasons: Counter[str], duplicates: list[tuple[dict[str, Any], dict[str, Any]]]) -> None:
    by_target = Counter((item.get("target_doc"), item.get("section")) for item in included)
    lines = [
        "# Reconsidered Survey/Model Parent Review",
        "",
        f"- Canonical chunks: {chunks}",
        f"- Parent-approved includes: {len(included)}",
        "",
        "## Downgrade / Reject Reasons",
        "",
    ]
    if reasons:
        lines.extend(f"- {key}: {value}" for key, value in reasons.most_common())
    else:
        lines.append("- None.")
    lines.extend(["", "## Parent-Approved Include Distribution", ""])
    for (target, section), count in sorted(by_target.items(), key=lambda item: (str(item[0][0]), str(item[0][1]))):
        lines.append(f"- `{target}` {section}: {count}")
    lines.extend(["", "## Duplicate Title Downgrades", ""])
    if duplicates:
        for duplicate, kept in duplicates:
            lines.append(f"- `{duplicate.get('identifier')}` {duplicate.get('title')} -> kept `{kept.get('identifier')}`")
    else:
        lines.append("- None.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decision-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for path in args.out_dir.glob("chunk-*.json"):
        path.unlink()
    chunks = load_decisions(args.decision_dir)
    included, reasons, duplicates = review(args)
    write_report(args.report, chunks=len(chunks), included=included, reasons=reasons, duplicates=duplicates)
    print(f"Canonical chunks: {len(chunks)}", flush=True)
    print(f"Parent-approved includes: {len(included)}", flush=True)
    print(f"Wrote {args.out_dir}", flush=True)
    print(f"Wrote {args.report}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
