#!/usr/bin/env python3
"""Apply parent-reviewed Research semantic-audit moves and hard rejects.

The audit reports are issues-only.  This script resolves an entry from its
primary URL (or title), moves the complete bilingual bullet block, and leaves
entries not present in the reports untouched.  It intentionally does not
apply Bench rejects: empirical studies of AI performing a research action are
handled by a separate restoration review under the current taxonomy.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
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
DEEP_ROOT = Path("docs/en/02-agent-capabilities/04-deep-research")


def blocks(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    result: list[str] = []
    start: int | None = None
    for index, line in enumerate(lines + ["# __end__\n"]):
        if line.startswith("- "):
            if start is not None:
                result.append("".join(lines[start:index]).rstrip() + "\n")
            start = index
        elif start is not None and line.startswith("# "):
            result.append("".join(lines[start:index]).rstrip() + "\n")
            start = None
    return result


def primary_url(block: str) -> str:
    match = re.match(r"^- \[[^]]+\]\((https?://[^)]+)\)", block)
    return match.group(1).rstrip("/") if match else ""


def title(block: str) -> str:
    match = re.match(r"^- \[([^]]+)\]", block)
    return re.sub(r"\s+", " ", match.group(1)).strip() if match else ""


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def all_paths() -> list[Path]:
    return [ROOT / name for name in SECTION_FILES.values()]


def load_report(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if "high_confidence_changes" in payload:
        rows = payload["high_confidence_changes"]
        return [
            {
                "action": row.get("action"),
                "title": title_from_bullet(row.get("exact_current_bullet", "") or row.get("bullet", "")),
                "bullet": row.get("exact_current_bullet", "") or row.get("bullet", ""),
                "target": row.get("target_doc") or row.get("target"),
                "source_report": path.as_posix(),
            }
            for row in rows
        ]
    if "findings" in payload:
        return [
            {
                "action": row.get("action"),
                "title": row.get("title", ""),
                "url": row.get("url", ""),
                "bullet": row.get("bullet", ""),
                "target": row.get("target"),
                "source_report": path.as_posix(),
            }
            for row in payload["findings"]
        ]
    if "decisions" in payload:
        return [
            {
                "action": row.get("decision"),
                "title": row.get("title", ""),
                "url": row.get("url", ""),
                "target": row.get("destination"),
                "source_report": path.as_posix(),
            }
            for row in payload["decisions"]
        ]
    if "issues" in payload:
        return [
            {
                "action": row.get("decision"),
                "title": row.get("title", ""),
                "url": row.get("url", ""),
                "target": row.get("target_doc"),
                "source_report": path.as_posix(),
            }
            for row in payload["issues"]
        ]
    raise SystemExit(f"Unsupported audit report schema: {path}")


def url_from_bullet(bullet: str) -> str:
    match = re.search(r"https?://[^)\s]+", bullet)
    return match.group(0).rstrip("/") if match else ""


def title_from_bullet(bullet: str) -> str:
    match = re.match(r"^- \[([^]]+)\]", bullet.strip())
    return match.group(1).strip() if match else ""


def paired(path: Path) -> Path:
    return Path(str(path).replace("docs/en/", "docs/zh/", 1))


def matching(block_list: list[str], row: dict[str, Any]) -> list[str]:
    url = str(row.get("url") or "").rstrip("/")
    candidates = [block for block in block_list if url and primary_url(block) == url]
    if not candidates and row.get("title"):
        wanted = norm(str(row["title"]))
        candidates = [block for block in block_list if norm(title(block)) == wanted]
    return candidates


def rebuild(path: Path, remove: set[str]) -> None:
    old = path.read_text(encoding="utf-8")
    kept = [block for block in blocks(path) if block not in remove]
    heading = old.splitlines()[0]
    path.write_text(heading + "\n\n" + "".join(kept).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", action="append", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    reports = [row for path in args.report for row in load_report(path)]
    # A later report is allowed to override an earlier low-level report, but
    # duplicate rows with conflicting destinations are rejected explicitly.
    keyed: dict[tuple[str, str], dict[str, Any]] = {}
    for row in reports:
        action = str(row.get("action") or "").lower()
        if action not in {"reclassify", "reject", "remove_duplicate"}:
            continue
        key = (str(row.get("url") or "").rstrip("/"), norm(str(row.get("title") or "")))
        if not key[0] and not key[1]:
            raise SystemExit(f"Audit row has no identity: {row}")
        old = keyed.get(key)
        if old and (old.get("action"), old.get("target")) != (action, row.get("target")):
            raise SystemExit(f"Conflicting audit rows: {old} vs {row}")
        keyed[key] = row

    current: dict[Path, list[str]] = {path: blocks(path) for path in all_paths()}
    current_zh: dict[Path, list[str]] = {paired(path): blocks(paired(path)) for path in all_paths()}
    destinations: dict[Path, list[str]] = defaultdict(list)
    removals: dict[Path, set[str]] = defaultdict(set)
    moved = 0
    removed = 0
    unresolved: list[dict[str, Any]] = []
    for row in keyed.values():
        matches: list[tuple[Path, str]] = []
        for path, block_list in current.items():
            found = matching(block_list, row)
            matches.extend((path, block) for block in found)
        if not matches:
            unresolved.append(row)
            continue
        if len(matches) > 1:
            # Exact duplicate primary listings are removed as a unit only for
            # an explicit duplicate finding; moves must be unambiguous.
            if row["action"] not in {"remove_duplicate", "reject"}:
                raise SystemExit(f"Ambiguous audit identity: {row}; matches={len(matches)}")
        if row["action"] in {"reject", "remove_duplicate"}:
            for path, block in matches:
                removals[path].add(block)
                removed += 1
            continue
        target = Path(str(row.get("target") or ""))
        if target not in set(all_paths()) and not target.exists():
            raise SystemExit(f"Unsupported target in audit report: {target}")
        source_path, block = matches[0]
        removals[source_path].add(block)
        destinations[target].append(block)
        moved += 1

    if unresolved:
        details = "\n".join(f"- {row.get('title')} | {row.get('url')}" for row in unresolved)
        raise SystemExit(f"Unresolved audit rows ({len(unresolved)}):\n{details}")

    zh_destinations: dict[Path, list[str]] = defaultdict(list)
    for target, additions in destinations.items():
        zh_target = paired(target)
        for en_block in additions:
            key = (primary_url(en_block), norm(title(en_block)))
            source_zh_block = ""
            for source_path in current:
                for candidate in current_zh[paired(source_path)]:
                    if primary_url(candidate) == key[0] or norm(title(candidate)) == key[1]:
                        source_zh_block = candidate
                        break
                if source_zh_block:
                    break
            if source_zh_block:
                zh_destinations[zh_target].append(source_zh_block)
        existing = blocks(target)
        existing_keys = {(primary_url(block), norm(title(block))) for block in existing}
        for block in additions:
            key = (primary_url(block), norm(title(block)))
            if key not in existing_keys:
                existing.append(block)
                existing_keys.add(key)
        if not args.dry_run:
            heading = target.read_text(encoding="utf-8").splitlines()[0]
            target.write_text(heading + "\n\n" + "".join(existing).rstrip() + "\n", encoding="utf-8")

    if not args.dry_run:
        for path, remove in removals.items():
            rebuild(path, remove)
        # Apply the identical URL/title removals and additions to Chinese.
        for path, remove in list(removals.items()):
            zh_path = paired(path)
            zh_remove: set[str] = set()
            for block in remove:
                key_url, key_title = primary_url(block), norm(title(block))
                for candidate in blocks(zh_path):
                    if (key_url and primary_url(candidate) == key_url) or (key_title and norm(title(candidate)) == key_title):
                        zh_remove.add(candidate)
            rebuild(zh_path, zh_remove)
        # Chinese destination blocks were captured before source removal.
        for zh_target, zh_additions in zh_destinations.items():
            existing = blocks(zh_target)
            existing_keys = {(primary_url(block), norm(title(block))) for block in existing}
            for zh_block in zh_additions:
                key = (primary_url(zh_block), norm(title(zh_block)))
                if key not in existing_keys:
                    existing.append(zh_block)
                    existing_keys.add(key)
            heading = zh_target.read_text(encoding="utf-8").splitlines()[0]
            zh_target.write_text(heading + "\n\n" + "".join(existing).rstrip() + "\n", encoding="utf-8")

    print(json.dumps({"reports": len(args.report), "rows": len(keyed), "moved": moved, "removed": removed, "dry_run": args.dry_run}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
