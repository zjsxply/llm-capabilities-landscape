#!/usr/bin/env python3
"""Apply reviewed bilingual keep, reject, and reclassification fixes by primary URL."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


KEEP = {"keep", "keep_and_add_counterpart"}


def read_rows(paths: list[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, list) or not all(isinstance(row, dict) for row in value):
            raise SystemExit(f"Expected an array of objects: {path}")
        rows.extend(value)
    return rows


def paired(path: Path) -> Path:
    value = path.as_posix()
    if not value.startswith("docs/en/"):
        raise SystemExit(f"Expected an English documentation path: {path}")
    return Path(value.replace("docs/en/", "docs/zh/", 1))


def primary_url(line: str) -> str:
    if not line.startswith("- "):
        return ""
    match = re.search(r"https?://[^)\s]+", line)
    return match.group(0).rstrip("/") if match else ""


def replace_primary(path: Path, url: str, bullet: str | None) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    needle = url.rstrip("/")
    matches = [index for index, line in enumerate(lines) if primary_url(line) == needle]
    if len(matches) > 1:
        raise SystemExit(f"Duplicate primary URL in {path}: {url}")
    if matches:
        if bullet:
            lines[matches[0]] = bullet.rstrip()
        else:
            del lines[matches[0]]
    elif bullet:
        lines.append(bullet.rstrip())
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-en", type=Path, required=True)
    parser.add_argument("--input", type=Path, action="append", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    source_zh = paired(args.source_en)
    touched = {args.source_en, source_zh}
    rows = read_rows(args.input)
    for row in rows:
        action = str(row.get("action") or "")
        if action not in KEEP | {"reject_remove", "reclassify"}:
            raise SystemExit(f"Unsupported action: {action!r}")
        url = str(row.get("url") or "").strip()
        if not url:
            raise SystemExit("Decision row has no URL")
        if action in KEEP:
            destination_en = args.source_en
        elif action == "reclassify":
            destination_en = Path(str(row.get("target_doc") or ""))
            if not destination_en.as_posix().startswith("docs/en/"):
                raise SystemExit(f"Invalid reclassification target for {url}: {destination_en}")
        else:
            destination_en = None

        if not args.dry_run:
            replace_primary(args.source_en, url, None)
            replace_primary(source_zh, url, None)
            if destination_en is not None:
                en_bullet = str(row.get("en_bullet") or "").strip()
                zh_bullet = str(row.get("zh_bullet") or "").strip()
                if not en_bullet or not zh_bullet:
                    raise SystemExit(f"Missing bilingual bullet for {url}")
                destination_zh = paired(destination_en)
                touched.update({destination_en, destination_zh})
                replace_primary(destination_en, url, en_bullet)
                replace_primary(destination_zh, url, zh_bullet)

    print(json.dumps({"rows": len(rows), "touched": sorted(path.as_posix() for path in touched), "dry_run": args.dry_run}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
