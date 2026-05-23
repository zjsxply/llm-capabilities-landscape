#!/usr/bin/env python3
"""Apply parent-approved candidate inclusion bullets to bilingual Markdown docs."""

from __future__ import annotations

import argparse
import json
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


def insert_bullets(path: Path, section: str, bullets: list[str], *, dry_run: bool) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    added = 0
    for bullet in sorted(bullets, key=release_key_from_text):
        url = first_url(bullet)
        if (url and url in text) or bullet in text:
            continue

        start, end = find_section_bounds(lines, section)
        key = release_key_from_text(bullet)
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
        added += 1

    if added and not dry_run:
        path.write_text("".join(lines), encoding="utf-8")
    return added


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
            english = str(
                override.get("suggested_english_bullet")
                or override.get("english_bullet")
                or item.get("suggested_english_bullet")
                or item.get("english_draft")
                or ""
            ).strip()
            chinese = str(
                override.get("suggested_chinese_bullet")
                or override.get("chinese_bullet")
                or item.get("suggested_chinese_bullet")
                or item.get("chinese_draft")
                or ""
            ).strip()
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
                    "english_bullet": english,
                    "chinese_bullet": chinese,
                }
            )
    return records


def apply_records(root: Path, records: list[dict[str, Any]], *, dry_run: bool) -> dict[str, int]:
    en_groups: dict[tuple[Path, str], list[str]] = {}
    zh_groups: dict[tuple[Path, str], list[str]] = {}
    for item in records:
        section = str(item["section"])
        en_doc = resolve_english_target_doc(str(item["target_doc"]), section)
        zh_doc = paired_zh_path(en_doc)
        en_groups.setdefault((en_doc, section), []).append(str(item["english_bullet"]))
        zh_groups.setdefault((zh_doc, section), []).append(str(item["chinese_bullet"]))

    totals: dict[str, int] = {}
    for (doc, section), bullets in sorted(en_groups.items()):
        path = root / doc
        count = insert_bullets(path, section, bullets, dry_run=dry_run)
        totals[str(doc)] = totals.get(str(doc), 0) + count
    for (doc, section), bullets in sorted(zh_groups.items()):
        path = root / doc
        count = insert_bullets(path, section, bullets, dry_run=dry_run)
        totals[str(doc)] = totals.get(str(doc), 0) + count
    return totals


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
    totals = apply_records(args.root, records, dry_run=args.dry_run)

    if args.included_out:
        write_json(args.included_out, records)

    print(f"include records: {len(records)}", flush=True)
    for doc, count in sorted(totals.items()):
        if count:
            print(f"{doc}: added {count}", flush=True)
    if args.dry_run:
        print("dry run: no files written", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
