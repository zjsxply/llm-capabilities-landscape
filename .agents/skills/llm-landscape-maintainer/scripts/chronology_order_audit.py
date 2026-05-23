#!/usr/bin/env python3
"""Audit and repair chronological order in landscape Markdown sections."""

from __future__ import annotations

import argparse
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from landscape_paths import default_markdown_files, is_english_doc, paired_zh_path


SECTION_MARKERS = ("Bench", "Agent Harness")


TITLE_OVERRIDES: tuple[tuple[str, tuple[int, int]], ...] = (
    (r"\bARC \(ARC-AGI-1\)|fchollet/ARC\b", (201909, 0)),
    (r"\bVPCT\b", (202502, 0)),
    (r"\bARC-AGI-2\b", (202502, 0)),
    (r"\bAIME 2024\b", (202402, 0)),
    (r"\bAIME 2025\b", (202502, 0)),
    (r"\bHMMT Feb 2025\b", (202502, 0)),
    (r"\bBeyondAIME\b", (202504, 0)),
    (r"\bMathArenaApex\b", (202505, 1)),
    (r"\bMathArena Kangaroo\b|MathKangaroo", (202505, 2)),
    (r"\bHMMT Nov 2025\b", (202511, 0)),
    (r"\bLiveMathBench\b", (202511, 0)),
    (r"\bAIME 2026\b", (202602, 0)),
    (r"\bHMMT Feb 2026\b", (202602, 1)),
    (r"\bProJudge\b", (202503, 6553)),
    (r"\bActionReasoningBench\b", (202505, 0)),
    (r"\bMTU-Bench\b", (202505, 0)),
    (r"\bConvCodeWorld\b", (202505, 0)),
    (r"\bCodeMMLU\b", (202505, 0)),
    (r"\bAgentHarm\b", (202505, 0)),
    (r"\bRobotouille\b", (202505, 0)),
    (r"\bManiSkill-HAB\b", (202505, 1)),
    (r"\bHASARD\b", (202505, 2)),
    (r"\bVBench\+\+", (202501, 0)),
    (r"\bVE-Bench\b", (202502, 0)),
    (r"\bDrive4C\b", (202506, 0)),
    (r"\bFiVE-Bench\b", (202510, 0)),
    (r"\bCVBench\b", (202512, 0)),
    (r"\bHAL Harness\b", (202510, 11977)),
    (r"\bSheetpedia\b", (202510, 0)),
    (r"\bEvidenceBench\b", (202510, 0)),
    (r"\bCRUST-Bench\b", (202510, 0)),
    (r"\bMapIQ\b", (202510, 0)),
    (r"\bMoSciBench\b", (202510, 0)),
    (r"\bTurnaboutLLM\b", (202511, 0)),
    (r"\bYourbench\b", (202512, 0)),
    (r"\bFluid Language Model Benchmarking\b", (202512, 0)),
    (r"\bEvalAgents\b", (202512, 0)),
    (r"\bAgentRewardBench\b", (202512, 0)),
    (r"\bMAC\b", (202512, 0)),
    (r"\bChemistry RAG Benchmark\b", (202512, 0)),
    (r"\bCGBench\b", (202512, 0)),
    (r"\bCrossWordBench\b", (202512, 0)),
    (r"\bENIGMATA-Eval\b", (202512, 0)),
    (r"\bLaborMarketplaceBenchmark\b", (202512, 0)),
    (r"\bNoReGeo\b", (202601, 0)),
    (r"\bFinMathBench\b", (202601, 0)),
    (r"\bMME-SCI\b", (202601, 0)),
    (r"\bLexInstructEval\b", (202601, 0)),
    (r"\bD-GARA\b", (202601, 0)),
    (r"\bAutomated Evaluation of Database Conversational Agents\b", (202601, 0)),
    (r"\bBioMysteryBench Verified\b|\bBioMysteryBench\b", (202605, 0)),
    (r"\bHLE-Rolling\b", (202605, 0)),
    (r"\bStructural biology benchmark\b|Structural biology benchmark", (202605, 0)),
    (r"\bUSAMO 2026\b", (202605, 0)),
    (r"\bAgent Red Teaming\b", (202605, 0)),
    (r"\bBioPipelineBench Verified\b", (202605, 0)),
    (r"\bHealthBench Consensus\b", (202605, 0)),
    (r"\bTroubleshootingBench\b", (202605, 0)),
    (r"\bProtocolQA Open-Ended\b", (202605, 0)),
    (r"OpenAI internal biology and chemistry risk evaluations|OpenAI .*biology.*chemistry", (202605, 0)),
    (r"OpenAI cybersecurity risk evaluations|OpenAI .*网络安全风险评测", (202605, 0)),
    (r"\bKITTEN\b", (202604, 0)),
    (r"\bVoxDialogue\b", (202605, 0)),
    (r"MineDojo, CALVIN, VIMA, and LIBERO|MineDojo、CALVIN、VIMA 和 LIBERO", (202306, 0)),
)


VENUE_PATTERNS: tuple[tuple[str, tuple[int, int]], ...] = (
    (r"CVPR2025|CVPR_2025", (202506, 0)),
    (r"ICCV2025|ICCV_2025", (202510, 0)),
    (r"proceedings\.mlr\.press/v267", (202507, 0)),
    (r"aclanthology\.org/2025\.(?:findings-)?naacl", (202505, 0)),
    (r"aclanthology\.org/2025\.(?:findings-)?acl", (202507, 0)),
    (r"aclanthology\.org/2025\.(?:findings-)?emnlp", (202511, 0)),
    (r"www\.ijcai\.org/proceedings/2025", (202508, 0)),
    (r"ojs\.aaai\.org/index\.php/AAAI/article/view/", (202601, 0)),
    (r"papers\.neurips\.cc/paper_files/paper/2025", (202512, 0)),
    (r"gpt-5-5|Claude Opus 4\.7|037f06850df7fbe|Evaluating-Claude-For-Bioinformatics", (202605, 0)),
    (r"ByteDance-Seed/Seed2\.0", (202605, 0)),
)


@dataclass
class Section:
    heading: str
    start: int
    end: int


@dataclass
class Bullet:
    start: int
    end: int
    text: str
    key: tuple[int, int] | None


def release_key(text: str) -> tuple[int, int] | None:
    for pattern, key in TITLE_OVERRIDES:
        if re.search(pattern, text, re.I):
            return key

    match = re.search(r"arxiv(?:\.org/abs/|\.)(\d{4})\.(\d{4,5})", text, re.I)
    if not match:
        match = re.search(r"arXiv:(\d{4})\.(\d{4,5})", text, re.I)
    if match:
        yymm = match.group(1)
        return (2000 + int(yymm[:2])) * 100 + int(yymm[2:]), int(match.group(2))

    match = re.search(
        r"(?:aclanthology\.org/|doi\.org/10\.18653/v1/)2025\.(?:findings-)?(naacl|acl|emnlp)(?:-[\w]+)?\.(\d+)",
        text,
        re.I,
    )
    if match:
        month_by_venue = {"naacl": 202505, "acl": 202507, "emnlp": 202511}
        return month_by_venue[match.group(1).lower()], int(match.group(2))

    match = re.search(r"www\.ijcai\.org/proceedings/2025/(\d+)", text, re.I)
    if match:
        return 202508, int(match.group(1))

    for pattern, key in VENUE_PATTERNS:
        if re.search(pattern, text, re.I):
            return key
    return None


def sections(lines: list[str]) -> list[Section]:
    found: list[Section] = []
    index = 0
    heading_re = re.compile(r"^(#{1,6})\s+(.+)$")
    while index < len(lines):
        match = heading_re.match(lines[index])
        if not match:
            index += 1
            continue
        level = len(match.group(1))
        heading = match.group(2).strip()
        start = index
        index += 1
        while index < len(lines):
            next_match = heading_re.match(lines[index])
            if next_match and len(next_match.group(1)) <= level:
                break
            index += 1
        if any(marker in heading for marker in SECTION_MARKERS):
            found.append(Section(heading, start, index))
    return found


def bullet_blocks(lines: list[str], section: Section) -> list[Bullet]:
    blocks: list[Bullet] = []
    index = section.start + 1
    current_start: int | None = None
    while index < section.end:
        line = lines[index]
        if line.startswith("- "):
            if current_start is not None:
                text = "\n".join(lines[current_start:index])
                blocks.append(Bullet(current_start, index, text, release_key(text)))
            current_start = index
        elif current_start is not None and not (line.startswith("  ") or line.strip() == ""):
            text = "\n".join(lines[current_start:index])
            blocks.append(Bullet(current_start, index, text, release_key(text)))
            current_start = None
        index += 1
    if current_start is not None:
        text = "\n".join(lines[current_start:section.end])
        blocks.append(Bullet(current_start, section.end, text, release_key(text)))
    return blocks


def title(text: str) -> str:
    first = text.split("\n", 1)[0]
    match = re.match(r"- \[([^\]]+)\]", first)
    if match:
        return match.group(1)
    return first[2:82] if first.startswith("- ") else first[:80]


def sort_known_bullets(lines: list[str], blocks: list[Bullet]) -> list[str]:
    known_slots = [index for index, block in enumerate(blocks) if block.key is not None]
    sorted_known = sorted((blocks[index] for index in known_slots), key=lambda block: (block.key, title(block.text)))
    replacements = {slot: sorted_known[offset].text.splitlines() for offset, slot in enumerate(known_slots)}

    new_lines: list[str] = []
    cursor = 0
    for index, block in enumerate(blocks):
        new_lines.extend(lines[cursor:block.start])
        new_lines.extend(replacements.get(index, block.text.splitlines()))
        cursor = block.end
    new_lines.extend(lines[cursor:])
    return new_lines


def ensure_blank_before_headings(lines: list[str]) -> list[str]:
    new_lines: list[str] = []
    for line in lines:
        if re.match(r"^#{1,6}\s+", line) and new_lines and new_lines[-1].strip():
            new_lines.append("")
        new_lines.append(line)
    return new_lines


def audit_file(path: Path, *, fix: bool) -> list[str]:
    original_text = path.read_text(encoding="utf-8")
    lines = original_text.splitlines()
    reports: list[str] = []
    for section in reversed(sections(lines)):
        blocks = bullet_blocks(lines, section)
        section_has_report = False
        previous_key: tuple[int, int] | None = None
        previous_title = ""
        previous_line = 0
        for block in blocks:
            if block.key is None:
                continue
            if previous_key is not None and block.key < previous_key:
                reports.append(
                    f"{path}:{block.start + 1}: {section.heading}: "
                    f"{title(block.text)} {block.key} after {previous_title} {previous_key} at line {previous_line}"
                )
                section_has_report = True
            previous_key = block.key
            previous_title = title(block.text)
            previous_line = block.start + 1
        if fix and section_has_report:
            lines = sort_known_bullets(lines, blocks)
    if fix:
        lines = ensure_blank_before_headings(lines)
        new_text = "\n".join(lines) + ("\n" if original_text.endswith("\n") else "")
        if new_text != original_text:
            path.write_text(new_text, encoding="utf-8")
    return reports


def identity(text: str) -> str:
    identity_overrides = (
        (r"^-?\s*Crux[:：]", "text:crux"),
        (r"CyberGym'?s execution stack|CyberGym 的执行栈", "text:cybergym-secbench-exploitbench-harnesses"),
        (r"MineDojo, CALVIN, VIMA, and LIBERO|MineDojo、CALVIN、VIMA 和 LIBERO", "text:minedojo-calvin-vima-libero-harnesses"),
    )
    for pattern, value in identity_overrides:
        if re.search(pattern, text, re.I):
            return value
    urls = re.findall(r"https?://[^\s)]+", text)
    if urls:
        for url in urls:
            if any(
                marker in url
                for marker in (
                    "arxiv.org",
                    "openreview.net",
                    "aclanthology.org",
                    "openaccess.thecvf.com",
                    "proceedings.mlr.press",
                    "ojs.aaai.org",
                    "papers.neurips.cc",
                    "doi.org",
                    "huggingface.co/datasets",
                    "deploymentsafety.openai.com",
                    "cdn.sanity.io",
                    "anthropic.com/research",
                    "agi.safe.ai",
                )
            ):
                return "url:" + url.rstrip("/").lower()
        return "url:" + urls[0].rstrip("/").lower()
    normalized = unicodedata.normalize("NFKC", title(text)).lower()
    normalized = re.sub(r"[\W_]+", "", normalized)
    return "text:" + normalized[:80]


def bilingual_mismatches(paths: list[Path]) -> list[str]:
    en_paths = [path for path in paths if is_english_doc(path)]
    reports: list[str] = []
    for en_path in sorted(en_paths):
        zh_path = paired_zh_path(en_path)
        if not zh_path.exists():
            continue
        en_lines = en_path.read_text(encoding="utf-8").splitlines()
        zh_lines = zh_path.read_text(encoding="utf-8").splitlines()
        en_sections = {section.heading: section for section in sections(en_lines)}
        zh_sections = {section.heading: section for section in sections(zh_lines)}
        for heading in sorted(set(en_sections) & set(zh_sections)):
            en_ids = [identity(block.text) for block in bullet_blocks(en_lines, en_sections[heading])]
            zh_ids = [identity(block.text) for block in bullet_blocks(zh_lines, zh_sections[heading])]
            if en_ids != zh_ids:
                reports.append(f"{en_path}: {heading}: English bullets={len(en_ids)}, Chinese bullets={len(zh_ids)}")
    return reports


def default_paths() -> list[Path]:
    return default_markdown_files(Path("."), include_readme=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files to audit. Defaults to recursive docs/en and docs/zh.")
    parser.add_argument("--fix", action="store_true", help="Sort known-date bullets within affected sections.")
    parser.add_argument("--bilingual", action="store_true", help="Also report bilingual bullet-order mismatches.")
    args = parser.parse_args()

    paths = args.paths or default_paths()
    all_reports: list[str] = []
    for path in paths:
        if path.exists():
            all_reports.extend(audit_file(path, fix=args.fix))
    for report in all_reports:
        print(report)
    print(f"chronology inversions: {len(all_reports)}")

    if args.bilingual:
        mismatches = bilingual_mismatches(paths)
        for report in mismatches:
            print(report)
        print(f"bilingual order mismatches: {len(mismatches)}")

    return 1 if all_reports and not args.fix else 0


if __name__ == "__main__":
    raise SystemExit(main())
