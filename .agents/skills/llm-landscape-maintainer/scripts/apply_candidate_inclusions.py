#!/usr/bin/env python3
"""Apply parent-approved candidate inclusion bullets to bilingual Markdown docs."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

from landscape_paths import paired_zh_path, resolve_english_target_doc


INCLUDE_STATES = {"include", "included", "accept", "accepted"}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def release_key_from_text(text: str) -> tuple[int, int]:
    match = re.search(r"arxiv(?:\.org/abs/|\.)(\d{4})\.(\d{4,5})", text, re.I)
    if not match:
        match = re.search(r"arXiv:(\d{4})\.(\d{4,5})", text, re.I)
    if match:
        yymm = match.group(1)
        return (2000 + int(yymm[:2])) * 100 + int(yymm[2:]), int(match.group(2))
    venue_months = (
        (r"(?:CVPR|CVPRW)2025|CVPR_2025", 202506),
        (r"ICCV2025|ICCV_2025", 202510),
        (r"proceedings\.mlr\.press/v267", 202507),
        (r"aclanthology\.org/2025\.(?:findings-)?naacl", 202505),
        (r"aclanthology\.org/2025\.(?:findings-)?acl", 202507),
        (r"aclanthology\.org/2025\.(?:findings-)?emnlp", 202511),
    )
    for pattern, key in venue_months:
        if re.search(pattern, text, re.I):
            return key, 0
    match = re.search(r"\b(20\d{2})\b", text)
    if match:
        return int(match.group(1)) * 100 + 99, 0
    return 999999, 0


def release_key_from_record(record: dict[str, Any], bullet: str) -> tuple[int, int]:
    url_key = release_key_from_text(first_url(bullet) or "")
    if url_key[0] != 999999:
        return url_key
    raw_year = record.get("year")
    if isinstance(raw_year, int) or (isinstance(raw_year, str) and raw_year.isdigit()):
        year = int(raw_year)
        if 1900 <= year <= 2100:
            return year * 100 + 99, 0
    return 999999, 0


def first_url(markdown: str) -> str | None:
    match = re.search(r"\]\((https?://[^)]+)\)", markdown)
    return match.group(1) if match else None


def normalize_doc(raw: Any) -> str:
    if isinstance(raw, list):
        raw = next((str(item) for item in raw if item), "")
    raw = str(raw or "").strip()
    if ";" in raw:
        raw = raw.split(";", 1)[0].strip()
    match = re.search(r"docs/en/[^\s;,)]*\.md", raw)
    if match:
        return match.group(0)
    return raw


def normalize_section(raw: Any) -> str:
    section = str(raw or "").strip()
    section = re.sub(r"^#+\s*", "", section)
    return section


def normalize_bullet_spacing(markdown: str) -> str:
    return re.sub(r"(\]\(https?://[^)]+\))([:：])\s*", r"\1\2 ", markdown.strip(), count=1)


def section_label(section: str) -> str:
    match = re.match(r"\d+(?:\.\d+)+\s+(.+)$", section.strip())
    label = match.group(1) if match else section
    return re.sub(r"\s+", " ", label).strip().lower()


def status_of(item: dict[str, Any]) -> str:
    return str(item.get("decision") or item.get("status") or "").strip().lower()


def find_section_bounds(lines: list[str], section: str) -> tuple[int, int]:
    start: int | None = None
    start_level = 0
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line.rstrip("\n"))
        if match and match.group(2) == section:
            start = index
            start_level = len(match.group(1))
            break
    if start is None:
        wanted_label = section_label(section)
        if wanted_label in {"leaderboard", "survey", "bench", "model", "agent harness", "skill"}:
            for index, line in enumerate(lines):
                match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line.rstrip("\n"))
                if match and section_label(match.group(2)) == wanted_label:
                    start = index
                    start_level = len(match.group(1))
                    break
    if start is None:
        match = re.match(r"(\d+(?:\.\d+)+)\b", section)
        if match:
            heading_re = re.compile(rf"^(#{{1,6}})\s+{re.escape(match.group(1))}\s+")
            for index, line in enumerate(lines):
                heading_match = heading_re.match(line)
                if heading_match:
                    start = index
                    start_level = len(heading_match.group(1))
                    break
    if start is None:
        raise RuntimeError(f"section not found: {section}")

    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = re.match(r"^(#{1,6})\s+", lines[index])
        if match and len(match.group(1)) <= start_level:
            end = index
            break
    return start, end


def render_bullets(
    path: Path,
    section: str,
    records: list[dict[str, Any]],
    *,
    bullet_field: str,
) -> tuple[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    outcomes: dict[str, str] = {}
    ordered = sorted(records, key=lambda row: release_key_from_record(row, str(row[bullet_field])))
    for record in ordered:
        identifier = str(record.get("identifier") or "")
        bullet = str(record[bullet_field])
        bullet = bullet.strip()
        if not bullet.startswith("- "):
            bullet = f"- {bullet}"
        url = first_url(bullet)
        if bullet in text:
            outcomes[identifier] = "already_present"
            continue
        if url and url in text:
            raise RuntimeError(f"URL already exists with different content in {path}: {identifier}: {url}")

        start, end = find_section_bounds(lines, section)
        key = release_key_from_record(record, bullet)
        insert_at: int | None = None
        for index in range(start + 1, end):
            if not lines[index].startswith("- "):
                continue
            if release_key_from_text(lines[index]) > key:
                insert_at = index
                break
        if insert_at is None:
            insert_at = end
            while insert_at > start + 1 and lines[insert_at - 1].strip() == "":
                insert_at -= 1
        lines.insert(insert_at, bullet.rstrip("\n") + "\n")
        text = "".join(lines)
        outcomes[identifier] = "added"
    return "".join(lines), outcomes


def load_overrides(path: Path | None) -> dict[str, dict[str, Any]]:
    if path is None:
        return {}
    data = read_json(path)
    if isinstance(data, list):
        data = {str(item["identifier"]): item for item in data if isinstance(item, dict) and item.get("identifier")}
    if not isinstance(data, dict):
        raise SystemExit(f"Expected object or list in override file: {path}")

    overrides: dict[str, dict[str, Any]] = {}
    for key, value in data.items():
        if not isinstance(value, dict):
            raise SystemExit(f"Override for {key} must be an object")
        overrides[str(key)] = value
        overrides[str(key).lower()] = value
    return overrides


def override_for(item: dict[str, Any], overrides: dict[str, dict[str, Any]]) -> dict[str, Any]:
    identifier = str(item.get("identifier") or "")
    return overrides.get(identifier) or overrides.get(identifier.lower()) or {}


def collect_records(
    source_dir: Path,
    *,
    overrides: dict[str, dict[str, Any]],
    include_states: set[str],
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(source_dir.glob("chunk-*.json")):
        data = read_json(path)
        if not isinstance(data, list):
            raise SystemExit(f"Expected a JSON list in {path}")
        for item in data:
            if not isinstance(item, dict) or status_of(item) not in include_states:
                continue
            override = override_for(item, overrides)
            if override.get("skip"):
                continue

            target_doc = normalize_doc(
                override.get("target_doc")
                or item.get("target_doc")
                or item.get("target_docs")
                or item.get("docs")
            )
            section = normalize_section(override.get("section") or item.get("section") or "")
            english = normalize_bullet_spacing(str(
                override.get("suggested_english_bullet")
                or override.get("english_bullet")
                or item.get("suggested_english_bullet")
                or item.get("english_draft")
                or ""
            ))
            chinese = normalize_bullet_spacing(str(
                override.get("suggested_chinese_bullet")
                or override.get("chinese_bullet")
                or item.get("suggested_chinese_bullet")
                or item.get("chinese_draft")
                or ""
            ))
            if not target_doc or not section or not english or not chinese:
                raise SystemExit(
                    "Missing target_doc, section, or bilingual bullets for "
                    f"{item.get('identifier')} in {path}"
                )
            if not target_doc.startswith("docs/en/"):
                raise SystemExit(f"Expected English target doc for {item.get('identifier')}: {target_doc}")
            records.append(
                {
                    "identifier": item.get("identifier") or "",
                    "title": item.get("title") or "",
                    "source_file": path.name,
                    "target_doc": target_doc,
                    "section": section,
                    "year": item.get("year"),
                    "url": first_url(english) or "",
                    "english_bullet": english,
                    "chinese_bullet": chinese,
                }
            )
    identifiers = [str(row["identifier"]) for row in records]
    duplicates = sorted({identifier for identifier in identifiers if identifiers.count(identifier) > 1})
    if duplicates:
        raise SystemExit(f"Duplicate include identifiers: {duplicates[:20]}")
    return records


def apply_records(
    root: Path,
    records: list[dict[str, Any]],
    *,
    dry_run: bool,
) -> tuple[dict[str, int], list[dict[str, Any]]]:
    en_groups: dict[tuple[Path, str], list[dict[str, Any]]] = {}
    zh_groups: dict[tuple[Path, str], list[dict[str, Any]]] = {}
    for item in records:
        section = str(item["section"])
        en_doc = Path(str(item["target_doc"]))
        if not (root / en_doc).is_file():
            en_doc = resolve_english_target_doc(str(item["target_doc"]), section)
        zh_doc = paired_zh_path(en_doc)
        if not (root / en_doc).is_file() or not (root / zh_doc).is_file():
            raise RuntimeError(f"Missing bilingual target for {item['identifier']}: {en_doc}, {zh_doc}")
        en_groups.setdefault((en_doc, section), []).append(item)
        zh_groups.setdefault((zh_doc, section), []).append(item)

    totals: dict[str, int] = {}
    rendered: dict[Path, str] = {}
    per_language: dict[str, dict[str, str]] = {str(row["identifier"]): {} for row in records}
    ordered_groups = [
        *(('en', key, value) for key, value in sorted(en_groups.items())),
        *(('zh', key, value) for key, value in sorted(zh_groups.items())),
    ]
    for language, (doc, section), group_records in ordered_groups:
        path = root / doc
        if not os.access(path, os.W_OK):
            raise RuntimeError(f"Target is not writable: {path}")
        bullet_field = "english_bullet" if language == "en" else "chinese_bullet"
        new_text, outcomes = render_bullets(path, section, group_records, bullet_field=bullet_field)
        rendered[path] = new_text
        count = sum(value == "added" for value in outcomes.values())
        totals[str(doc)] = totals.get(str(doc), 0) + count
        for identifier, outcome in outcomes.items():
            per_language[identifier][language] = outcome

    if not dry_run:
        originals = {path: path.read_text(encoding="utf-8") for path in rendered}
        temp_paths: dict[Path, Path] = {}
        try:
            for path, text in rendered.items():
                temp = path.with_name(f".{path.name}.apply-{os.getpid()}.tmp")
                temp.write_text(text, encoding="utf-8")
                temp_paths[path] = temp
            for path in rendered:
                temp_paths[path].replace(path)
        except Exception:
            for path, text in originals.items():
                path.write_text(text, encoding="utf-8")
            raise
        finally:
            for temp in temp_paths.values():
                temp.unlink(missing_ok=True)

    results: list[dict[str, Any]] = []
    for row in records:
        identifier = str(row["identifier"])
        outcomes = per_language[identifier]
        if set(outcomes) != {"en", "zh"}:
            raise RuntimeError(f"Incomplete bilingual apply result for {identifier}: {outcomes}")
        if dry_run:
            status = "dry_run"
        elif all(value == "already_present" for value in outcomes.values()):
            status = "already_present"
        else:
            status = "included"
        results.append(
            {
                **row,
                "status": status,
                "docs": [str(row["target_doc"]), str(paired_zh_path(Path(str(row["target_doc"]))))],
                "english_result": outcomes["en"],
                "chinese_result": outcomes["zh"],
            }
        )
    return totals, results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True, help="Directory containing chunk-*.json decisions.")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--override-json", type=Path, help="Optional identifier-keyed target or bullet overrides.")
    parser.add_argument("--included-out", type=Path, help="Write the included records applied by this run.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--include-state",
        action="append",
        default=[],
        help="Accepted decision/status value. Defaults to include, included, accept, accepted.",
    )
    args = parser.parse_args()

    include_states = {state.lower() for state in args.include_state} or INCLUDE_STATES
    overrides = load_overrides(args.override_json)
    records = collect_records(args.source_dir, overrides=overrides, include_states=include_states)
    totals, results = apply_records(args.root, records, dry_run=args.dry_run)

    if args.included_out:
        write_json(args.included_out, results)

    print(f"include records: {len(records)}", flush=True)
    for doc, count in sorted(totals.items()):
        if count:
            print(f"{doc}: added {count}", flush=True)
    if args.dry_run:
        print("dry run: no files written", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
