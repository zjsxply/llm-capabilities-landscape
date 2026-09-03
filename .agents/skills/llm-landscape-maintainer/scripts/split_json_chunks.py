#!/usr/bin/env python3
"""Split a JSON list into stable, bounded review chunks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--size", type=int, default=20)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("Expected a JSON list")
    if args.size <= 0:
        raise SystemExit("--size must be positive")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for old in args.out_dir.glob("chunk-*.json"):
        old.unlink()
    for index, start in enumerate(range(0, len(data), args.size), 1):
        path = args.out_dir / f"chunk-{index:03d}.json"
        path.write_text(
            json.dumps(data[start : start + args.size], ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"{path}: {len(data[start : start + args.size])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
