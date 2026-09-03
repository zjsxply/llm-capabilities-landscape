#!/usr/bin/env python3
"""Apply terminal Research taxonomy decisions to paired section files.

The script consumes the bounded inventory chunks used for review and one
terminal review directory per section. It fails closed on unresolved or
identity-mismatched decisions, preserves the existing bilingual bullet text,
and moves only entries whose final section changed.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path("docs/en/03-downstream-applications/02-research")
SECTION_FILES = {
    "survey": "02-survey.md",
    "bench": "03-bench.md",
    "model": "04-model.md",
    "agent harness": "05-agent-harness.md",
    "skill": "06-skill.md",
}
FILE_SECTIONS = {name: section for section, name in SECTION_FILES.items()}
RESEARCH_PATHS = {section: ROOT / filename for section, filename in SECTION_FILES.items()}
DEEP_RESEARCH_ROOT = Path("docs/en/02-agent-capabilities/04-deep-research")
ALLOWED_DESTINATIONS = set(RESEARCH_PATHS.values()) | {
    DEEP_RESEARCH_ROOT / filename for filename in SECTION_FILES.values()
}
FINAL_DECISIONS = {"keep", "reclassify", "reject"}


def read_rows(directory: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    paths = sorted(directory.glob("chunk-[0-9][0-9][0-9].json"))
    if not paths:
        raise SystemExit(f"No review chunks found in {directory}")
    for path in paths:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, list) or not all(isinstance(row, dict) for row in value):
            raise SystemExit(f"Expected a JSON array of objects: {path}")
        rows.extend(value)
    return rows


def canonical(value: Any) -> str:
    text = str(value or "").strip()
    if text.lower().startswith("arxiv:"):
        return "arXiv:" + re.sub(r"v\d+$", "", text.split(":", 1)[1], flags=re.I)
    match = re.fullmatch(r"doi:10\.48550/arxiv\.(\d{4}\.\d{4,5})(?:v\d+)?", text, re.I)
    if match:
        return "arXiv:" + match.group(1)
    if text.lower().startswith("doi:"):
        return "DOI:" + text.split(":", 1)[1].lower()
    if text.lower().startswith("url:"):
        return "url:" + text.split(":", 1)[1].rstrip("/")
    return text


def path_from_target(value: Any) -> Path:
    raw = str(value or "").strip()
    path = Path(raw)
    if path in ALLOWED_DESTINATIONS:
        return path
    raise SystemExit(f"Unsupported taxonomy-rescreen target: {raw!r}")


def bullet_blocks(text: str) -> list[str]:
    lines = text.splitlines(keepends=True)
    blocks: list[str] = []
    start: int | None = None
    for index, line in enumerate(lines + ["# __end__\n"]):
        if line.startswith("- "):
            if start is not None:
                blocks.append("".join(lines[start:index]).rstrip() + "\n")
            start = index
        elif start is not None and re.match(r"^#{1,6}\s", line):
            blocks.append("".join(lines[start:index]).rstrip() + "\n")
            start = None
    return blocks


def first_url(block: str) -> str:
    match = re.search(r"https?://[^)\s]+", block)
    return match.group(0).rstrip("/") if match else ""


def first_title(block: str) -> str:
    match = re.match(r"^- \[([^]]+)\]\(", block)
    if match:
        return re.sub(r"\s+", " ", match.group(1)).strip()
    # Keep project-only bullets whose display name is intentionally unlinked.
    body = block[2:].splitlines()[0].strip() if block.startswith("- ") else ""
    body = re.split(r"\s+[（(]|\s*[:：]", body, maxsplit=1)[0]
    return re.sub(r"\s+", " ", body).strip()


def index_blocks(path: Path) -> dict[tuple[str, str], str]:
    indexed: dict[tuple[str, str], str] = {}
    for block in bullet_blocks(path.read_text(encoding="utf-8")):
        url = first_url(block)
        title = first_title(block)
        if not url or not title:
            raise SystemExit(f"Bullet without URL or title in {path}: {block[:120]!r}")
        key = (url, title)
        if key in indexed:
            # Historical imports can repeat an identical project bullet.
            # Keep the first block; the rebuilt output is de-duplicated.
            continue
        indexed[key] = block
    return indexed


def merge_english_snapshot(
    indexed: dict[str, dict[tuple[str, str], str]], snapshot: Path
) -> None:
    for raw_line in snapshot.read_text(encoding="utf-8").splitlines():
        if "\t" not in raw_line:
            continue
        location, block = raw_line.split("\t", 1)
        path_text, separator, _ = location.rpartition(":")
        if not separator or not block.startswith("- "):
            continue
        path = Path(path_text)
        section = FILE_SECTIONS.get(path.name)
        if section not in indexed or path.parent != ROOT:
            continue
        url = first_url(block)
        title = first_title(block)
        if url and title:
            indexed[section].setdefault((url, title), block.rstrip() + "\n")


def find_block(blocks: dict[tuple[str, str], str], url: str, title: str) -> str:
    exact = blocks.get((url, title))
    if exact:
        return exact
    # A malformed or manually repaired display title must not make a
    # bilingual paper disappear when its URL remains stable and unique.
    matches = [block for (block_url, _), block in blocks.items() if block_url == url]
    if len(matches) == 1:
        return matches[0]
    return ""


def clean_display_title(value: Any) -> str:
    title = re.sub(r"\s+", " ", str(value or "")).strip()
    malformed = re.fullmatch(r"\[(.+)]\.", title)
    return malformed.group(1) if malformed else title


def render_inventory_block(row: dict[str, Any], language: str) -> str:
    title = clean_display_title(row.get("title"))
    url = str(row.get("url") or "").rstrip("/")
    tldr = re.sub(r"\s+", " ", str(row.get(f"{language}_tldr") or "")).strip()
    if not title or not url or not tldr:
        raise SystemExit(
            f"Cannot rebuild {language} bullet for {row.get('identifier')}: "
            "missing title, URL, or TLDR"
        )
    separator = "：" if language == "zh" else ": "
    return f"- [{title}]({url}){separator}{tldr}\n"


def comparable_identity(row: dict[str, Any]) -> tuple[Any, str, str]:
    return row.get("index"), canonical(row.get("identifier")), str(row.get("title") or "")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--section",
        action="append",
        required=True,
        metavar="NAME=INVENTORY_DIR=DECISION_DIR",
        help="Repeat once per Research section.",
    )
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--english-snapshot-tsv", type=Path)
    parser.add_argument(
        "--allow-empty-section",
        action="store_true",
        help="Allow a previously nonempty section to become empty after review.",
    )
    parser.add_argument(
        "--render-dir",
        type=Path,
        help="Write the fully rendered bilingual candidates under this directory.",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    specs: list[tuple[str, Path, Path]] = []
    for raw in args.section:
        parts = raw.split("=", 2)
        if len(parts) != 3 or parts[0].strip().lower() not in SECTION_FILES:
            raise SystemExit(f"Invalid --section value: {raw!r}")
        specs.append((parts[0].strip().lower(), Path(parts[1]), Path(parts[2])))
    if len({section for section, _, _ in specs}) != len(specs):
        raise SystemExit("A Research section was supplied more than once")

    source_rows: dict[str, dict[str, Any]] = {}
    final_rows: dict[str, dict[str, Any]] = {}
    original_sections: dict[str, str] = {}
    duplicate_sources: defaultdict[str, list[str]] = defaultdict(list)
    for section, inventory_dir, decision_dir in specs:
        inventory = read_rows(inventory_dir)
        decisions = read_rows(decision_dir)
        if len(inventory) != len(decisions):
            raise SystemExit(
                f"Coverage mismatch for {section}: inventory={len(inventory)} decisions={len(decisions)}"
            )
        for position, (source, decision) in enumerate(zip(inventory, decisions), 1):
            if comparable_identity(source) != comparable_identity(decision):
                raise SystemExit(f"Identity/order mismatch for {section} at row {position}")
            identifier = canonical(source.get("identifier"))
            record_key = f"{section}::{source.get('index')}::{identifier}"
            duplicate_sources[identifier].append(section)
            if record_key in source_rows:
                raise SystemExit(f"Duplicate inventory record: {record_key}")
            source_rows[record_key] = source
            original_sections[record_key] = section
            final_rows[record_key] = decision

    placements: dict[str, Path] = {}
    counts: Counter[str] = Counter()
    record_actions: dict[str, str] = {}
    for record_key, decision in final_rows.items():
        identifier = record_key.rsplit("::", 1)[-1]
        action = str(decision.get("decision") or "").strip().lower()
        if action not in FINAL_DECISIONS:
            raise SystemExit(f"Nonterminal decision for {identifier}: {action!r}")
        counts[action] += 1
        record_actions[record_key] = action
        if action == "keep":
            placements[record_key] = RESEARCH_PATHS[original_sections[record_key]]
        elif action == "reclassify":
            placements[record_key] = path_from_target(decision.get("target_doc"))

    en_blocks = {section: index_blocks(ROOT / filename) for section, filename in SECTION_FILES.items()}
    if args.english_snapshot_tsv:
        merge_english_snapshot(en_blocks, args.english_snapshot_tsv)
    zh_root = Path(str(ROOT).replace("docs/en/", "docs/zh/", 1))
    zh_blocks = {section: index_blocks(zh_root / filename) for section, filename in SECTION_FILES.items()}
    output_en: defaultdict[Path, list[str]] = defaultdict(list)
    output_zh: defaultdict[Path, list[str]] = defaultdict(list)
    existing_destination_urls: defaultdict[Path, set[str]] = defaultdict(set)
    seen_output: set[tuple[Path, str, str]] = set()

    external_destinations = {
        destination for destination in placements.values() if destination not in set(RESEARCH_PATHS.values())
    }
    for destination in external_destinations:
        paired = Path(str(destination).replace("docs/en/", "docs/zh/", 1))
        if not destination.exists() or not paired.exists():
            raise SystemExit(f"Missing bilingual external destination: {destination}")
        en_existing = bullet_blocks(destination.read_text(encoding="utf-8"))
        zh_existing = bullet_blocks(paired.read_text(encoding="utf-8"))
        output_en[destination].extend(en_existing)
        output_zh[destination].extend(zh_existing)
        existing_destination_urls[destination].update(first_url(block) for block in en_existing)

    # A few project-only entries predate the paper inventory. Preserve them
    # instead of dropping them during the inventory-based rebuild.
    preserved_en: defaultdict[Path, list[str]] = defaultdict(list)
    preserved_zh: defaultdict[Path, list[str]] = defaultdict(list)
    inventory_urls = {
        str(row.get("url") or "").rstrip("/") for row in source_rows.values()
    }
    for section, filename in SECTION_FILES.items():
        for blocks, output in ((en_blocks[section], preserved_en[RESEARCH_PATHS[section]]),
                               (zh_blocks[section], preserved_zh[RESEARCH_PATHS[section]])):
            for key, block in blocks.items():
                if key[0] not in inventory_urls:
                    output.append(block)

    candidates: list[tuple[str, Path, str, str, str]] = []
    for record_key, source in source_rows.items():
        identifier = record_key.rsplit("::", 1)[-1]
        source_section = original_sections[record_key]
        url = str(source.get("url") or "").rstrip("/")
        title = re.sub(r"\s+", " ", str(source.get("title") or "")).strip()
        if not url:
            raise SystemExit(f"Inventory row lacks URL: {identifier}")
        en = find_block(en_blocks[source_section], url, title) or render_inventory_block(source, "en")
        zh = find_block(zh_blocks[source_section], url, title) or render_inventory_block(source, "zh")
        if record_key not in placements:
            continue
        candidates.append((record_key, placements[record_key], identifier, en, zh))

    grouped: defaultdict[tuple[Path, str], list[tuple[str, Path, str, str, str]]] = defaultdict(list)
    for item in candidates:
        grouped[(item[1], item[2])].append(item)
    merged_duplicates = 0
    for (destination, identifier), items in grouped.items():
        in_place = [
            item
            for item in items
            if record_actions[item[0]] == "keep"
            and RESEARCH_PATHS[original_sections[item[0]]] == destination
        ]
        selected = in_place if in_place else items
        merged_duplicates += len(items) - len(selected)
        for record_key, _, _, en, zh in selected:
            title = first_title(en)
            key = (destination, identifier, title)
            if key in seen_output:
                raise SystemExit(f"Duplicate output placement: {key}")
            if destination in external_destinations and first_url(en) in existing_destination_urls[destination]:
                merged_duplicates += 1
                continue
            seen_output.add(key)
            output_en[destination].append(en)
            output_zh[destination].append(zh)

    for destination, blocks in preserved_en.items():
        output_en[destination].extend(blocks)
    for destination, blocks in preserved_zh.items():
        output_zh[destination].extend(blocks)

    touched_paths = set(RESEARCH_PATHS.values()) | external_destinations
    rendered: dict[Path, tuple[str, str]] = {}
    for en_path in sorted(touched_paths):
        zh_path = Path(str(en_path).replace("docs/en/", "docs/zh/", 1))
        en_text = en_path.read_text(encoding="utf-8")
        zh_text = zh_path.read_text(encoding="utf-8")
        old_en_count = len(bullet_blocks(en_text))
        old_zh_count = len(bullet_blocks(zh_text))
        new_en_blocks = output_en[en_path]
        new_zh_blocks = output_zh[en_path]
        if len(new_en_blocks) != len(new_zh_blocks):
            raise SystemExit(
                f"Bilingual output-count mismatch for {en_path}: "
                f"en={len(new_en_blocks)} zh={len(new_zh_blocks)}"
            )
        if (
            not args.allow_empty_section
            and (old_en_count or old_zh_count)
            and not new_en_blocks
        ):
            raise SystemExit(
                f"Refusing to empty previously nonempty section {en_path}; "
                "pass --allow-empty-section only after reviewing the complete diff"
            )
        new_primary_keys = [
            (first_url(block), first_title(block)) for block in new_en_blocks
        ]
        duplicate_keys = [
            key for key, count in Counter(new_primary_keys).items() if all(key) and count > 1
        ]
        if duplicate_keys:
            raise SystemExit(
                f"Duplicate primary URL-title rows in rebuilt section {en_path}: "
                f"{duplicate_keys[:5]}"
            )
        en_heading = en_text.splitlines()[0]
        zh_heading = zh_text.splitlines()[0]
        new_en = en_heading + "\n\n" + "".join(new_en_blocks).rstrip() + "\n"
        new_zh = zh_heading + "\n\n" + "".join(new_zh_blocks).rstrip() + "\n"
        rendered[en_path] = (new_en, new_zh)

    # Validate every destination before changing any official file. This keeps
    # a late failure from leaving a partially rebuilt bilingual topic tree.
    if args.render_dir:
        for en_path, (new_en, new_zh) in rendered.items():
            zh_path = Path(str(en_path).replace("docs/en/", "docs/zh/", 1))
            rendered_en = args.render_dir / en_path
            rendered_zh = args.render_dir / zh_path
            rendered_en.parent.mkdir(parents=True, exist_ok=True)
            rendered_zh.parent.mkdir(parents=True, exist_ok=True)
            rendered_en.write_text(new_en, encoding="utf-8")
            rendered_zh.write_text(new_zh, encoding="utf-8")
    if not args.dry_run:
        for en_path, (new_en, new_zh) in rendered.items():
            zh_path = Path(str(en_path).replace("docs/en/", "docs/zh/", 1))
            en_path.write_text(new_en, encoding="utf-8")
            zh_path.write_text(new_zh, encoding="utf-8")

    report = [
        "# Research Taxonomy Rescreen",
        "",
        f"- Inventory rows: {len(source_rows)}",
        f"- Kept in place: {counts['keep']}",
        f"- Reclassified: {counts['reclassify']}",
        f"- Rejected: {counts['reject']}",
        f"- Merged duplicate reroutes: {merged_duplicates}",
        "- Unresolved: 0",
        f"- Dry run: {'yes' if args.dry_run else 'no'}",
        f"- Render directory: {args.render_dir or 'not written'}",
        "",
        "## Final Section Counts",
        "",
        *[f"- {path}: {len(output_en[path])}" for path in sorted(touched_paths)],
    ]
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({"inventory": len(source_rows), "decisions": counts, "dry_run": args.dry_run}, default=dict))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
