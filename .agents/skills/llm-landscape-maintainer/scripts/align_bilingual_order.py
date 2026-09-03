#!/usr/bin/env python3
"""Align one Markdown document's bullet order with its bilingual pair.

The operation is deliberately content-preserving: it moves complete top-level
bullet blocks by the project's URL-based identity and refuses to run when the
two files do not contain the same identity multiset.
"""

from __future__ import annotations

import argparse
import collections
import importlib.util
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
CHRONOLOGY = SCRIPT_DIR / "chronology_order_audit.py"
spec = importlib.util.spec_from_file_location("chronology_order_audit", CHRONOLOGY)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot load {CHRONOLOGY}")
chronology = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = chronology
spec.loader.exec_module(chronology)


def reorder(target: Path, reference: Path) -> bool:
    target_lines = target.read_text(encoding="utf-8").splitlines(keepends=True)
    reference_lines = reference.read_text(encoding="utf-8").splitlines(keepends=True)
    target_sections = {section.heading: section for section in chronology.sections(target_lines)}
    reference_sections = {section.heading: section for section in chronology.sections(reference_lines)}
    changed = False

    for heading, target_section in target_sections.items():
        reference_section = reference_sections.get(heading)
        if reference_section is None:
            continue
        target_blocks = chronology.bullet_blocks(target_lines, target_section)
        reference_blocks = chronology.bullet_blocks(reference_lines, reference_section)
        target_by_id: dict[str, collections.deque[list[str]]] = collections.defaultdict(collections.deque)
        for block in target_blocks:
            target_by_id[chronology.identity(block.text)].append(target_lines[block.start:block.end])
        reference_ids = [chronology.identity(block.text) for block in reference_blocks]
        if collections.Counter(reference_ids) != collections.Counter(
            chronology.identity(block.text) for block in target_blocks
        ):
            raise SystemExit(f"identity multiset mismatch in {target} and {reference}: {heading}")
        ordered: list[list[str]] = []
        for identity in reference_ids:
            ordered.append(target_by_id[identity].popleft())
        if not target_blocks:
            continue
        start = target_blocks[0].start
        end = target_blocks[-1].end
        replacement = [line for block in ordered for line in block]
        if target_lines[start:end] != replacement:
            target_lines[start:end] = replacement
            changed = True

    if changed:
        target.write_text("".join(target_lines), encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--reference", type=Path, required=True)
    args = parser.parse_args()
    print(f"changed={reorder(args.target, args.reference)} target={args.target} reference={args.reference}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
