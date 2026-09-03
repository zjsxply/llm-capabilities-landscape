#!/usr/bin/env python3
"""Verify finalized bilingual inclusion records after Markdown application."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from landscape_paths import paired_zh_path


def read_records(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise SystemExit(f"Expected a JSON array of objects: {path}")
    return data


def section_label(value: str) -> str:
    match = re.match(r"\d+(?:\.\d+)+\s+(.+)$", value.strip())
    return re.sub(r"\s+", " ", match.group(1) if match else value).strip().lower()


def section_lines(path: Path, section: str) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    wanted = section_label(section)
    start: int | None = None
    level = 0
    for index, line in enumerate(lines):
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading and section_label(heading.group(2)) == wanted:
            start = index + 1
            level = len(heading.group(1))
            break
    if start is None:
        raise RuntimeError(f"Section {section!r} not found in {path}")
    end = len(lines)
    for index in range(start, len(lines)):
        heading = re.match(r"^(#{1,6})\s+", lines[index])
        if heading and len(heading.group(1)) <= level:
            end = index
            break
    return lines[start:end]


def exact_count(path: Path, section: str, bullet: str) -> int:
    expected = re.sub(
        r"(\]\(https?://[^)]+\))([:：])\s*",
        lambda match: f"{match.group(1)}{match.group(2)}{' ' if match.group(2) == ':' else ''}",
        bullet.strip(),
        count=1,
    )
    return sum(line.strip() == expected for line in section_lines(path, section))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", type=Path, help="Finalized apply JSON array")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    records = read_records(args.records)
    identifiers: set[str] = set()
    errors: list[str] = []
    verified: list[dict[str, Any]] = []
    for row in records:
        identifier = str(row.get("identifier") or "").strip()
        if not identifier:
            errors.append("record without identifier")
            continue
        if identifier in identifiers:
            errors.append(f"duplicate record: {identifier}")
            continue
        identifiers.add(identifier)
        target = Path(str(row.get("target_doc") or ""))
        section = str(row.get("section") or "").strip()
        en_bullet = str(row.get("suggested_english_bullet") or "").strip()
        zh_bullet = str(row.get("suggested_chinese_bullet") or "").strip()
        if not target.as_posix().startswith("docs/en/") or not section or not en_bullet or not zh_bullet:
            errors.append(f"incomplete finalized record: {identifier}")
            continue
        en_path = args.root / target
        zh_rel = paired_zh_path(target)
        zh_path = args.root / zh_rel
        if not en_path.is_file() or not zh_path.is_file():
            errors.append(f"missing paired target: {identifier}: {target}, {zh_rel}")
            continue
        try:
            en_count = exact_count(en_path, section, en_bullet)
            zh_count = exact_count(zh_path, section, zh_bullet)
        except RuntimeError as error:
            errors.append(f"{identifier}: {error}")
            continue
        if en_count != 1 or zh_count != 1:
            errors.append(
                f"{identifier}: exact occurrences en={en_count} zh={zh_count}; expected one in each target"
            )
            continue
        verified.append(
            {
                "identifier": identifier,
                "section": section,
                "docs": [target.as_posix(), zh_rel.as_posix()],
                "english_occurrences": en_count,
                "chinese_occurrences": zh_count,
            }
        )

    report = {
        "records": len(records),
        "verified": len(verified),
        "errors": errors,
        "verified_records": verified,
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
    print(f"records: {len(records)}")
    print(f"verified: {len(verified)}")
    print(f"errors: {len(errors)}")
    for error in errors[:20]:
        print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
