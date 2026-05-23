#!/usr/bin/env python3
"""Collect first-pass evidence for GitHub seed repositories.

The script intentionally does not edit landscape Markdown. It normalizes GitHub
URLs, reuses the canonical /tmp clone path, records repository metadata, and
checks whether obvious aliases already appear in the paired docs.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path


GITHUB_RE = re.compile(
    r"(?:https?://)?github\.com/(?P<owner>[^/\s]+)/(?P<repo>[^/\s#?]+)"
)


def run(cmd: list[str], cwd: Path | None = None, check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=check,
    )


def parse_repo(value: str) -> tuple[str, str]:
    match = GITHUB_RE.search(value.strip())
    if not match:
        raise ValueError(f"not a GitHub repository URL: {value}")
    owner = match.group("owner").removesuffix(".git")
    repo = match.group("repo").removesuffix(".git")
    return owner, repo


def clone_or_pull(owner: str, repo: str, tmp_root: Path) -> tuple[Path, str]:
    dest = tmp_root / owner / repo
    url = f"https://github.com/{owner}/{repo}"
    if (dest / ".git").exists():
        proc = run(["git", "-C", str(dest), "pull", "--ff-only"])
        action = "pull"
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        proc = run(["git", "clone", url, str(dest)])
        action = "clone"
    status = proc.stdout.strip() or proc.stderr.strip() or "(no output)"
    return dest, f"{action}: {status}"


def github_api(owner: str, repo: str) -> dict[str, object] | None:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError):
        return None


def first_existing(paths: list[Path]) -> Path | None:
    for path in paths:
        if path.exists():
            return path
    return None


def read_head(path: Path, max_chars: int = 2200) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    return text[:max_chars].strip()


def file_sample(repo_dir: Path, limit: int = 80) -> list[str]:
    proc = run(["git", "-C", str(repo_dir), "ls-files"])
    files = [line for line in proc.stdout.splitlines() if line.strip()]
    return files[:limit]


def duplicate_hits(patterns: list[str], docs: list[Path]) -> list[str]:
    existing = [str(path) for path in docs if path.exists()]
    if not existing:
        return []
    query = "|".join(re.escape(p) for p in patterns if p)
    if not query:
        return []
    proc = run(["rg", "-n", query, *existing])
    return proc.stdout.splitlines()[:80]


def render_repo(repo_url: str, tmp_root: Path, docs: list[Path]) -> str:
    owner, repo = parse_repo(repo_url)
    repo_dir, clone_status = clone_or_pull(owner, repo, tmp_root)
    api = github_api(owner, repo) or {}
    readme = first_existing(
        [repo_dir / "README.md", repo_dir / "readme.md", repo_dir / "README.rst"]
    )
    aliases = [
        f"{owner}/{repo}",
        repo,
        str(api.get("name") or ""),
        str(api.get("full_name") or ""),
        str(api.get("description") or ""),
    ]
    hits = duplicate_hits([a for a in aliases if a and len(a) >= 4], docs)

    lines = [
        f"## {owner}/{repo}",
        "",
        f"- URL: https://github.com/{owner}/{repo}",
        f"- Canonical clone: `{repo_dir}`",
        f"- Clone status: {clone_status}",
    ]
    if api:
        lines.extend(
            [
                f"- Description: {api.get('description') or ''}",
                f"- Created: {api.get('created_at') or ''}",
                f"- Updated: {api.get('updated_at') or ''}",
                f"- Pushed: {api.get('pushed_at') or ''}",
                f"- Stars: {api.get('stargazers_count') or 0}",
                f"- Forks: {api.get('forks_count') or 0}",
                f"- Language: {api.get('language') or ''}",
            ]
        )
    lines.append("")
    lines.append("### File Sample")
    lines.extend(f"- `{path}`" for path in file_sample(repo_dir))
    lines.append("")
    lines.append("### README Head")
    if readme:
        lines.extend(["```markdown", read_head(readme), "```"])
    else:
        lines.append("- No README file found.")
    lines.append("")
    lines.append("### Duplicate Hits")
    if hits:
        lines.extend(f"- `{hit}`" for hit in hits)
    else:
        lines.append("- No hits in target docs for obvious aliases.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repos", nargs="+", help="GitHub repository URLs")
    parser.add_argument("--out", default=".tmp/github_seed_intake.md")
    parser.add_argument("--tmp-root", default="/tmp/github-repos")
    parser.add_argument(
        "--docs",
        nargs="*",
        default=[
            "docs/en/03-downstream-applications/02-research/README.md",
            "docs/en/03-downstream-applications/02-research/05-agent-harness.md",
            "docs/en/03-downstream-applications/02-research/06-skill.md",
            "docs/zh/03-downstream-applications/02-research/README.md",
            "docs/zh/03-downstream-applications/02-research/05-agent-harness.md",
            "docs/zh/03-downstream-applications/02-research/06-skill.md",
        ],
    )
    args = parser.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    docs = [Path(path) for path in args.docs]
    tmp_root = Path(args.tmp_root)

    chunks = ["# GitHub Seed Intake", ""]
    for repo_url in args.repos:
        try:
            chunks.append(render_repo(repo_url, tmp_root, docs))
        except Exception as exc:  # keep intake reports recoverable across many seeds
            chunks.extend([f"## {repo_url}", "", f"- Error: {exc}", ""])

    out.write_text("\n".join(chunks).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
