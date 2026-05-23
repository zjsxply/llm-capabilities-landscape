#!/usr/bin/env python3
"""Compare URL sets in paired English and Chinese Markdown files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


URL_RE = re.compile(r"https?://[^\s<>)\"']+")


def urls(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return {match.group(0).rstrip(".,;:") for match in URL_RE.finditer(text)}


def infer_zh_path(en_path: Path) -> Path:
    parts = list(en_path.parts)
    try:
        index = parts.index("en")
    except ValueError as exc:
        raise ValueError(f"cannot infer Chinese pair for {en_path}: no 'en' path segment") from exc
    parts[index] = "zh"
    return Path(*parts)


def iter_pairs(paths: list[Path], infer_pairs: bool) -> list[tuple[Path, Path]]:
    if infer_pairs:
        return [(path, infer_zh_path(path)) for path in paths]
    if len(paths) % 2:
        raise ValueError("provide an even number of files, or use --infer-from-en")
    return [(paths[index], paths[index + 1]) for index in range(0, len(paths), 2)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="Paired files, or English files with --infer-from-en.")
    parser.add_argument("--infer-from-en", action="store_true", help="Infer docs/zh pairs from docs/en paths.")
    parser.add_argument("--show-common", action="store_true", help="Print common URL counts by pair.")
    parser.add_argument("--no-fail", action="store_true", help="Return 0 even when URL sets differ.")
    args = parser.parse_args()

    failed = False
    for left, right in iter_pairs(args.files, args.infer_from_en):
        if not left.is_file():
            raise FileNotFoundError(left)
        if not right.is_file():
            raise FileNotFoundError(right)
        left_urls = urls(left)
        right_urls = urls(right)
        only_left = sorted(left_urls - right_urls)
        only_right = sorted(right_urls - left_urls)
        common_count = len(left_urls & right_urls)

        print(f"{left} <-> {right}")
        print(f"  left={len(left_urls)} right={len(right_urls)} common={common_count}")
        if only_left:
            failed = True
            print("  only left:")
            for item in only_left:
                print(f"    {item}")
        if only_right:
            failed = True
            print("  only right:")
            for item in only_right:
                print(f"    {item}")
        if not only_left and not only_right:
            print("  URL sets match.")
        elif args.show_common:
            print("  common:")
            for item in sorted(left_urls & right_urls):
                print(f"    {item}")

    return 0 if args.no_fail or not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
