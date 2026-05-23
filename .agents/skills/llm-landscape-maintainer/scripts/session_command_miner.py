#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


TOKEN_RE = re.compile(r"[A-Za-z0-9_./:-]+|[^\s]")
NOISE_RE = re.compile(r"\s+")


@dataclass
class CommandHit:
    command: str
    source: Path
    timestamp: str

    @property
    def token_count(self) -> int:
        return len(TOKEN_RE.findall(self.command))


def iter_jsonl(paths: Iterable[Path]) -> Iterable[tuple[Path, dict[str, Any]]]:
    for path in paths:
        try:
            handle = path.open("r", encoding="utf-8", errors="ignore")
        except OSError:
            continue
        with handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(item, dict):
                    yield path, item


def parse_arguments(raw: Any) -> Any:
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {}
    return raw


def extract_exec_commands(item: dict[str, Any]) -> list[str]:
    payload = item.get("payload")
    if not isinstance(payload, dict):
        return []
    if payload.get("type") != "function_call":
        return []

    name = str(payload.get("name") or "")
    arguments = parse_arguments(payload.get("arguments"))
    commands: list[str] = []
    if name.endswith("exec_command") and isinstance(arguments, dict):
        cmd = arguments.get("cmd")
        if isinstance(cmd, str):
            commands.append(cmd)
    if name.endswith("parallel") and isinstance(arguments, dict):
        for use in arguments.get("tool_uses") or []:
            if not isinstance(use, dict):
                continue
            recipient = str(use.get("recipient_name") or "")
            params = use.get("parameters")
            if recipient.endswith("exec_command") and isinstance(params, dict):
                cmd = params.get("cmd")
                if isinstance(cmd, str):
                    commands.append(cmd)
    return commands


def discover_session_files(home: Path) -> list[Path]:
    roots = [
        home / ".codex" / "sessions",
        home / ".codex" / "archived_sessions",
    ]
    files: list[Path] = []
    for root in roots:
        if root.exists():
            files.extend(sorted(root.rglob("*.jsonl")))
    tui_log = home / ".codex" / "log" / "codex-tui.log"
    if tui_log.exists():
        files.append(tui_log)
    return files


def normalize_command(command: str) -> str:
    text = NOISE_RE.sub(" ", command.strip())
    text = re.sub(r"/data/panly/[^ '\"]+", "<project-path>", text)
    text = re.sub(r"/home/panly/[^ '\"]+", "<home-path>", text)
    text = re.sub(r"\.tmp/[^ '\"]+", ".tmp/<artifact>", text)
    text = re.sub(r"\b\d{4}\.\d{4,5}(?:v\d+)?\b", "<arxiv-id>", text)
    text = re.sub(r"\b\d{4}-\d{2}-\d{2}[T0-9:._-]*\b", "<timestamp>", text)
    text = re.sub(r"\b[0-9a-f]{16,}\b", "<hex>", text)
    return text


def mine(paths: list[Path], min_tokens: int, contains: str | None) -> list[CommandHit]:
    hits: list[CommandHit] = []
    for source, item in iter_jsonl(paths):
        timestamp = str(item.get("timestamp") or "")
        for command in extract_exec_commands(item):
            if contains and contains not in command:
                continue
            hit = CommandHit(command=command, source=source, timestamp=timestamp)
            if hit.token_count >= min_tokens:
                hits.append(hit)
    return hits


def write_report(path: Path, hits: list[CommandHit], top: int) -> None:
    pattern_counts = Counter(normalize_command(hit.command) for hit in hits)
    by_pattern: dict[str, list[CommandHit]] = defaultdict(list)
    for hit in hits:
        by_pattern[normalize_command(hit.command)].append(hit)

    longest = sorted(hits, key=lambda item: item.token_count, reverse=True)[:top]
    patterns = pattern_counts.most_common(top)
    lines = [
        "# Codex Session Long Command Report",
        "",
        f"- Generated: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"- Long commands: {len(hits)}",
        f"- Distinct normalized patterns: {len(pattern_counts)}",
        "",
        "## Frequent Patterns",
        "",
    ]
    if not patterns:
        lines.append("- None.")
    for pattern, count in patterns:
        example = by_pattern[pattern][0]
        lines.append(f"- count={count}; tokens={example.token_count}; source={example.source.name}; {pattern}")

    lines.extend(["", "## Longest Commands", ""])
    if not longest:
        lines.append("- None.")
    for hit in longest:
        command = hit.command.strip()
        if len(command) > 1200:
            command = command[:1200] + " ..."
        lines.append(f"### {hit.token_count} tokens | {hit.timestamp} | {hit.source.name}")
        lines.append("")
        lines.append("```bash")
        lines.append(command)
        lines.append("```")
        lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Mine Codex session JSONL files for long reusable shell commands.")
    parser.add_argument("paths", nargs="*", type=Path, help="Session JSONL/log files or directories. Defaults to ~/.codex sessions.")
    parser.add_argument("--min-tokens", type=int, default=300)
    parser.add_argument("--contains", help="Only include commands containing this substring.")
    parser.add_argument("--top", type=int, default=40)
    parser.add_argument("--out", type=Path, default=Path(".tmp/session_long_commands.md"))
    args = parser.parse_args()

    if args.paths:
        files: list[Path] = []
        for path in args.paths:
            if path.is_dir():
                files.extend(sorted(path.rglob("*.jsonl")))
            elif path.is_file():
                files.append(path)
    else:
        files = discover_session_files(Path.home())
    hits = mine(files, args.min_tokens, args.contains)
    write_report(args.out, hits, args.top)
    print(f"Scanned files: {len(files)}", flush=True)
    print(f"Long commands: {len(hits)}", flush=True)
    print(f"Wrote {args.out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
