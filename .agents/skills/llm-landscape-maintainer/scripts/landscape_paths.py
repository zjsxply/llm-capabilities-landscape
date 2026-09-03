#!/usr/bin/env python3
"""Shared path helpers for the split landscape documentation tree."""

from __future__ import annotations

import glob
import re
import unicodedata
from pathlib import Path


README_FILES = ("README.md", "README.zh.md")
DOC_ROOTS = ("docs/en", "docs/zh")
CHAPTER_DIRS = {
    "00": "00-introduction",
    "01": "01-core-capabilities",
    "02": "02-agent-capabilities",
    "03": "03-downstream-applications",
    "04": "04-multimodal",
}


def unique_existing(paths: list[Path]) -> list[Path]:
    seen: set[Path] = set()
    result: list[Path] = []
    for path in paths:
        if not path.is_file():
            continue
        key = path.resolve()
        if key in seen:
            continue
        seen.add(key)
        result.append(path)
    return result


def default_markdown_files(root: Path = Path("."), *, include_readme: bool = True) -> list[Path]:
    files: list[Path] = []
    if include_readme:
        files.extend(root / name for name in README_FILES)
    for doc_root in DOC_ROOTS:
        files.extend(sorted((root / doc_root).rglob("*.md")))
    return unique_existing(files)


def expand_markdown_args(items: list[str], *, default_to_docs: bool = True) -> list[Path]:
    if not items and default_to_docs:
        return default_markdown_files(Path.cwd())

    files: list[Path] = []
    for item in items:
        matches = sorted(Path(match) for match in glob.glob(item, recursive=True))
        if matches:
            files.extend(path for path in matches if path.is_file())
            continue
        path = Path(item)
        if path.is_file():
            files.append(path)
    return unique_existing(files)


def is_english_doc(path: Path) -> bool:
    return "/docs/en/" in f"/{path.as_posix()}"


def paired_zh_path(en_path: Path) -> Path:
    return Path(str(en_path).replace("docs/en/", "docs/zh/", 1))


def slugify(text: str) -> str:
    value = text.strip().lower().replace("&", " and ")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "section"


def split_section_filename(section: str) -> str:
    standard = {
        "leaderboard": "01-leaderboard.md",
        "survey": "02-survey.md",
        "bench": "03-bench.md",
        "benchmark": "03-bench.md",
        "model": "04-model.md",
        "agent harness": "05-agent-harness.md",
        "harness": "05-agent-harness.md",
        "skill": "06-skill.md",
    }
    match = re.match(r"\s*\d+\.\d+\.(\d+)\s+(.+?)\s*$", section)
    if not match:
        simple = section.strip().lower()
        if simple in standard:
            return standard[simple]
        return f"00-{slugify(section)}.md"

    label = match.group(2).strip().lower()
    if label in standard:
        return standard[label]
    return f"{int(match.group(1)):02d}-{slugify(match.group(2))}.md"


def resolve_legacy_intro_doc(topic: str, slug: str, section: str = "") -> Path | None:
    base = Path("docs/en") / CHAPTER_DIRS["00"]
    mapping = {
        ("01", "what-is-harness"): base / "01-landscape-structure.md",
        ("02", "how-to-read-harnesses"): base / "01-landscape-structure.md",
        ("03", "skill-creator"): base / "04-other.md",
        ("04", "overall-leaderboards"): base / "02-overall-leaderboards.md",
    }
    direct = mapping.get((topic, slug))
    if direct and direct.is_file():
        return direct

    if (topic, slug) == ("05", "benchmark-reliability"):
        return base / "03-evaluation-methodology.md"
    return None


def resolve_english_target_doc(target_doc: str, section: str = "") -> Path:
    path = Path(target_doc)
    if path.name == "README.md" and section:
        sibling = path.with_name(split_section_filename(section))
        if sibling.is_file():
            return sibling
    if path.is_file():
        return path

    normalized = target_doc.replace("\\", "/").strip()
    split_match = re.match(r"docs/en/(\d{2}-[^/]+)/(\d{2})-(.+?)/([^/]+\.md)$", normalized)
    if split_match:
        chapter_dir, _topic, slug, filename = split_match.groups()
        chapter_base = Path("docs/en") / chapter_dir
        for moved_topic_base in sorted(chapter_base.glob(f"??-{slug}")):
            candidate = moved_topic_base / filename
            if candidate.is_file():
                return candidate
            if section:
                candidate = moved_topic_base / split_section_filename(section)
                if candidate.is_file():
                    return candidate
    old_match = re.match(r"docs/en/(\d{2})-(\d{2})-(.+)\.md$", normalized)
    if old_match:
        chapter, topic, slug = old_match.groups()
        if chapter == "00":
            legacy = resolve_legacy_intro_doc(topic, slug, section)
            if legacy and legacy.is_file():
                return legacy
        chapter_dir = CHAPTER_DIRS.get(chapter)
        if chapter_dir:
            topic_base = Path("docs/en") / chapter_dir / f"{topic}-{slug}"
            candidates = []
            if section:
                candidates.append(topic_base / split_section_filename(section))
            candidates.append(topic_base / "README.md")
            candidates.append(Path("docs/en") / chapter_dir / f"{topic}-{slug}.md")
            for candidate in candidates:
                if candidate.is_file():
                    return candidate
            chapter_base = Path("docs/en") / chapter_dir
            for moved_topic_base in sorted(chapter_base.glob(f"??-{slug}")):
                candidates = []
                if section:
                    candidates.append(moved_topic_base / split_section_filename(section))
                candidates.append(moved_topic_base / "README.md")
                for candidate in candidates:
                    if candidate.is_file():
                        return candidate

    return path
