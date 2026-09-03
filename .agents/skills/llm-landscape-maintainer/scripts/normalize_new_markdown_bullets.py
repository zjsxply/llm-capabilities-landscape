#!/usr/bin/env python3
"""Add the required Markdown list prefix to generated bare linked entries."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    changed = 0
    for path in args.files:
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        new_lines = []
        file_changed = False
        for line in lines:
            if line.startswith("[") and "](http" in line:
                line = "- " + line
                file_changed = True
            new_lines.append(line)
        if file_changed:
            path.write_text("".join(new_lines), encoding="utf-8")
            changed += 1
    print(f"Normalized files: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
