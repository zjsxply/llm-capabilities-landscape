#!/usr/bin/env python3
"""Move URL-identified Markdown bullet blocks between paired EN/ZH sections.

This is intentionally conservative: it moves only complete top-level bullet
blocks whose text contains one of the supplied markers and leaves all other
content untouched.  The destination is de-duplicated by URL before insertion;
chronology is repaired by the project's audit script afterwards.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def bullet_blocks(lines: list[str]) -> list[tuple[int, int, str]]:
    blocks: list[tuple[int, int, str]] = []
    start: int | None = None
    for index, line in enumerate(lines + ["# __end__\n"]):
        if line.startswith("- "):
            if start is not None:
                blocks.append((start, index, "".join(lines[start:index])))
            start = index
        elif start is not None and line.startswith("# "):
            blocks.append((start, index, "".join(lines[start:index])))
            start = None
    return blocks


def section_bounds(lines: list[str], label: str) -> tuple[int, int]:
    heading: tuple[int, int] | None = None
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        text = match.group(2).strip()
        if text == label or text.endswith(f" {label}") or text.lower().endswith(f" {label.lower()}"):
            heading = (index, len(match.group(1)))
            break
    if heading is None:
        raise RuntimeError(f"section not found: {label}")
    start, level = heading
    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = re.match(r"^(#{1,6})\s+", lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return start, end


def move_one(path: Path, markers: list[str], destination: Path | None, destination_section: str | None) -> int:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    blocks = bullet_blocks(lines)
    wanted = [block for block in blocks if any(marker in block[2] for marker in markers)]
    if not wanted:
        return 0

    moved_text = [block[2] for block in wanted]
    kept: list[str] = []
    cursor = 0
    for start, end, _ in wanted:
        kept.extend(lines[cursor:start])
        cursor = end
    kept.extend(lines[cursor:])
    path.write_text("".join(kept), encoding="utf-8")

    if destination is not None:
        dest_lines = destination.read_text(encoding="utf-8").splitlines(keepends=True)
        dest_text = "".join(dest_lines)
        additions = [text for text in moved_text if not any(url in dest_text for url in re.findall(r"https?://[^)\s]+", text))]
        if additions:
            _, end = section_bounds(dest_lines, destination_section or "")
            insert_at = end
            while insert_at > 0 and dest_lines[insert_at - 1].strip() == "":
                insert_at -= 1
            dest_lines[insert_at:insert_at] = [text if text.endswith("\n") else text + "\n" for text in additions]
            destination.write_text("".join(dest_lines), encoding="utf-8")
    return len(wanted)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-en", type=Path, required=True)
    parser.add_argument("--source-zh", type=Path, required=True)
    parser.add_argument("--destination-en", type=Path, required=True)
    parser.add_argument("--destination-zh", type=Path, required=True)
    parser.add_argument("--destination-section", default="")
    parser.add_argument("--destination-section-zh", default="")
    parser.add_argument("--skip-en", action="store_true", help="Use when the English move was completed before an interrupted run.")
    parser.add_argument("--marker", action="append", required=True)
    args = parser.parse_args()
    en = 0 if args.skip_en else move_one(args.source_en, args.marker, args.destination_en, args.destination_section)
    zh = move_one(args.source_zh, args.marker, args.destination_zh, args.destination_section_zh or args.destination_section)
    if not args.skip_en and en != zh:
        raise SystemExit(f"Bilingual move count mismatch: en={en}, zh={zh}")
    print(f"moved {en} bilingual bullet blocks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
