#!/usr/bin/env python3
"""Find paired EN/ZH TLDR rows where only one side still looks generic."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from generic_tldr_audit import default_docs_files, repo_relative, scan_file


BULLET_RE = re.compile(r"^-\s+\[([^\]]+)\]\(([^)]+)\)(?::|\uff1a)\s*(.*)$")


@dataclass(frozen=True)
class Bullet:
    path: str
    line: int
    title: str
    url: str
    text: str
    generic: bool
    patterns: tuple[str, ...]


def infer_zh_path(en_path: Path) -> Path:
    text = en_path.as_posix()
    if "/docs/en/" in f"/{text}":
        return Path(text.replace("docs/en/", "docs/zh/", 1))
    raise ValueError(f"not an English docs path: {en_path}")


def changed_urls_from_git(path: Path) -> set[str]:
    urls: set[str] = set()
    for args in (["git", "diff", "--unified=0", "--", str(path)], ["git", "diff", "--cached", "--unified=0", "--", str(path)]):
        proc = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False)
        for line in proc.stdout.splitlines():
            if not line.startswith("+") or line.startswith("+++"):
                continue
            match = BULLET_RE.match(line[1:])
            if match:
                urls.add(match.group(2))
    return urls


def bullets_for(path: Path) -> list[Bullet]:
    generic_by_line: dict[int, tuple[str, ...]] = {
        row["line"]: tuple(row["patterns"])
        for row in scan_file(path)
    }
    bullets: list[Bullet] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        match = BULLET_RE.match(line)
        if not match:
            continue
        patterns = generic_by_line.get(line_number, ())
        bullets.append(
            Bullet(
                path=repo_relative(path),
                line=line_number,
                title=match.group(1),
                url=match.group(2),
                text=line,
                generic=bool(patterns),
                patterns=patterns,
            )
        )
    return bullets


def index_by_url(bullets: list[Bullet]) -> dict[str, list[Bullet]]:
    grouped: dict[str, list[Bullet]] = defaultdict(list)
    for bullet in bullets:
        grouped[bullet.url].append(bullet)
    return grouped


def pair_rows(en_path: Path, *, only_changed_en: bool) -> list[dict[str, Any]]:
    zh_path = infer_zh_path(en_path)
    if not zh_path.exists():
        return [
            {
                "status": "missing_zh_file",
                "en_path": repo_relative(en_path),
                "zh_path": repo_relative(zh_path),
            }
        ]
    en_by_url = index_by_url(bullets_for(en_path))
    zh_by_url = index_by_url(bullets_for(zh_path))
    changed_urls = changed_urls_from_git(en_path) if only_changed_en else set(en_by_url)
    rows: list[dict[str, Any]] = []
    for url in sorted(changed_urls):
        en_items = en_by_url.get(url, [])
        zh_items = zh_by_url.get(url, [])
        if not en_items or not zh_items:
            rows.append(
                {
                    "status": "unpaired_url",
                    "url": url,
                    "en_count": len(en_items),
                    "zh_count": len(zh_items),
                    "en_path": repo_relative(en_path),
                    "zh_path": repo_relative(zh_path),
                }
            )
            continue
        for index, en_item in enumerate(en_items):
            zh_item = zh_items[index] if index < len(zh_items) else zh_items[-1]
            if en_item.generic == zh_item.generic:
                continue
            status = "zh_still_generic" if not en_item.generic and zh_item.generic else "en_still_generic"
            rows.append(
                {
                    "status": status,
                    "url": url,
                    "en_path": en_item.path,
                    "en_line": en_item.line,
                    "en_title": en_item.title,
                    "en_patterns": list(en_item.patterns),
                    "zh_path": zh_item.path,
                    "zh_line": zh_item.line,
                    "zh_title": zh_item.title,
                    "zh_patterns": list(zh_item.patterns),
                }
            )
    return rows


def render_markdown(rows: list[dict[str, Any]]) -> str:
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row["status"]] += 1
    lines = [
        "# Bilingual TLDR Sync Audit",
        "",
        "## Summary",
        "",
        f"- Rows: {len(rows)}",
    ]
    for status, count in sorted(counts.items()):
        lines.append(f"- `{status}`: {count}")
    lines.extend(["", "## Rows", ""])
    if not rows:
        lines.append("No asymmetric generic TLDR rows found.")
    else:
        for row in rows:
            if row["status"] == "missing_zh_file":
                lines.append(f"- `missing_zh_file` `{row['en_path']}` -> `{row['zh_path']}`")
                continue
            if row["status"] == "unpaired_url":
                lines.append(
                    f"- `unpaired_url` `{row['url']}` EN={row['en_count']} ZH={row['zh_count']} "
                    f"for `{row['en_path']}`"
                )
                continue
            lines.append(
                f"- `{row['status']}` `{row['url']}` EN `{row['en_path']}:{row['en_line']}` "
                f"ZH `{row['zh_path']}:{row['zh_line']}`"
            )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="English docs files. Defaults to all docs/en Markdown files.")
    parser.add_argument("--only-changed-en", action="store_true", help="Only inspect URLs from changed English bullet rows in git diff.")
    parser.add_argument("--out", type=Path, help="Write Markdown report here.")
    parser.add_argument("--json-out", type=Path, help="Write JSON rows here.")
    parser.add_argument("--fail-on-match", action="store_true", help="Exit 1 if any asymmetric rows are found.")
    args = parser.parse_args()

    if args.paths:
        en_paths = [Path(item) for item in args.paths]
    else:
        en_paths = [path for path in default_docs_files() if "/docs/en/" in f"/{path.as_posix()}"]
    rows: list[dict[str, Any]] = []
    for path in en_paths:
        if not path.exists() or "/docs/en/" not in f"/{path.as_posix()}":
            continue
        rows.extend(pair_rows(path, only_changed_en=args.only_changed_en))

    markdown = render_markdown(rows)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(markdown, encoding="utf-8")
    else:
        print(markdown, end="")
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 1 if args.fail_on_match and rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
