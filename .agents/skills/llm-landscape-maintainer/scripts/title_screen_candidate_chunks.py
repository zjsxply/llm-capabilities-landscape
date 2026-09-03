#!/usr/bin/env python3
"""Generate conservative title-only decisions for citation-closure chunks.

This is a fallback for large S2 closure rounds where chunks contain no abstracts.
It is intentionally conservative: includes are only parent-review candidates, and
everything else is rejected with an auditable title-only reason rather than left
as an unresolved registry state.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


SECTION_FILES = {
    "Leaderboard": "01-leaderboard.md",
    "Survey": "02-survey.md",
    "Bench": "03-bench.md",
    "Model": "04-model.md",
    "Agent Harness": "05-agent-harness.md",
    "Skill": "06-skill.md",
}

SECTION_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    (
        "Survey",
        re.compile(
            r"\b(survey|review|taxonomy|tutorial|position|overview|"
            r"systematic literature|scoping review|state[- ]of[- ]the[- ]art|"
            r"landscape)\b",
            re.I,
        ),
    ),
    (
        "Bench",
        re.compile(
            r"\b(bench(?:mark)?|evaluation|evaluating|eval|dataset|suite|"
            r"arena|leaderboard|testbed|challenge|competition|metric)\b",
            re.I,
        ),
    ),
    (
        "Skill",
        re.compile(
            r"\b(agent skill|agentic skill|skill ecosystem|skill librar|"
            r"skill bank|skill graph|skill runtime|skill retrieval|"
            r"skill routing|skill composition|skill discovery|skill learning|"
            r"reusable skill|skills for agents|llm skill)\b",
            re.I,
        ),
    ),
    (
        "Agent Harness",
        re.compile(
            r"\b(agent|agents|agentic|multi-agent|workflow|orchestrat|"
            r"tool[- ]using|tool use|browser agent|web agent|computer use|"
            r"gui agent|mcp|planner|planning agent|autonomous agent)\b",
            re.I,
        ),
    ),
    (
        "Model",
        re.compile(
            r"\b(model|models|architecture|pretrain|pre-training|post-train|"
            r"training|finetun|fine-tun|reinforcement learning|\brl\b|grpo|"
            r"dpo|reward|verifier|critic|synthetic data|distill|"
            r"mixture of experts|moe|adapter|world model|reasoning model|"
            r"test-time|inference scaling)\b",
            re.I,
        ),
    ),
]

BIO_RE = re.compile(
    r"\b(biomedical|biomedicine|medical|clinical|clinic|healthcare|patient|"
    r"disease|diagnos(?:is|tic)|radiology|pathology|histology|mri|ct scan|"
    r"ultrasound|eeg|ecg|tumou?r|cancer|oncology|retina|dermatology|protein|"
    r"genomic|omics|gene|cell|drug|molecule|molecular|biology|ehr|nursing|"
    r"doctor|hospital|therapy|therapeutic|microscopy|fetal|surgery|surgical|"
    r"cardiac|kidney|liver|lung|alzheimer|diabetes)\b",
    re.I,
)

NARROW_VERTICAL_RE = re.compile(
    r"\b(food|crop|agricultur|battery|smart grid|power grid|construction|"
    r"tourism|fashion|sports|music|recommender|recommendation|chemistry|"
    r"chemical|geospatial|climate|weather|education|student|teacher|"
    r"legal|law|court)\b",
    re.I,
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def stable_url(item: dict[str, Any]) -> str:
    identifier = str(item.get("identifier") or "")
    url = str(item.get("url") or "")
    if identifier.lower().startswith("arxiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    doi_match = re.match(r"doi:(.+)$", identifier, re.I)
    if doi_match:
        doi = doi_match.group(1)
        arxiv = re.match(r"10\.48550/arxiv\.(\d{4}\.\d{4,5})", doi, re.I)
        if arxiv:
            return f"https://arxiv.org/abs/{arxiv.group(1)}"
        return f"https://doi.org/{doi}"
    return url


def choose_section(title: str) -> str | None:
    for section, pattern in SECTION_PATTERNS:
        if pattern.search(title):
            return section
    return None


def choose_topic(title: str) -> str | None:
    text = title.lower()
    if any(token in text for token in ("cyber", "vulnerability", "exploit", "malware", "intrusion", "ctf")):
        return "docs/en/02-agent-capabilities/10-cybersecurity"
    if any(
        token in text
        for token in (
            "safety",
            "safe",
            "jailbreak",
            "prompt injection",
            "red team",
            "guardrail",
            "threat",
            "risk",
            "privacy",
            "poison",
            "attack",
        )
    ):
        return "docs/en/02-agent-capabilities/09-agent-safety"
    if any(token in text for token in ("computer use", "gui", "mobile agent", "desktop", "ui agent", "browser")):
        return "docs/en/02-agent-capabilities/05-computer-use-gui"
    if any(token in text for token in ("software", "coding", "code ", "debug", "repository", "swe", "bug")):
        return "docs/en/02-agent-capabilities/02-software-development"
    if any(token in text for token in ("competitive programming", "programming contest", "olympiad")):
        return "docs/en/02-agent-capabilities/01-competitive-programming"
    if any(token in text for token in ("web search", "search agent", "web browsing", "browser agent")):
        return "docs/en/02-agent-capabilities/03-web-search"
    if any(
        token in text
        for token in (
            "literature",
            "citation",
            "survey generation",
            "deep research",
            "retrieval and synthesis",
            "scientific literature",
            "systematic review",
        )
    ):
        return "docs/en/02-agent-capabilities/04-deep-research"
    if any(
        token in text
        for token in (
            "scientific research",
            "science agent",
            "autonomous scientific",
            "research agent",
            "hypothesis",
            "experiment design",
            "laboratory",
            " lab",
        )
    ):
        return "docs/en/03-downstream-applications/02-research"
    if any(token in text for token in ("autonomous driving", "driving", "traffic scene")):
        return "docs/en/04-multimodal/04-autonomous-driving"
    if any(token in text for token in ("embodied", "robot", "robotic", "vla", "vision-language-action", "manipulation")):
        return "docs/en/02-agent-capabilities/11-embodied-vla"
    if "video" in text:
        return "docs/en/01-core-capabilities/06-video"
    if any(token in text for token in ("image", "ocr", "document understanding", "diagram", "chart")):
        return "docs/en/01-core-capabilities/05-image-ocr"
    if any(token in text for token in ("3d", "spatial", "scene", "world model")):
        return "docs/en/01-core-capabilities/07-spatial"
    if any(token in text for token in ("speech", "audio", "voice")):
        return "docs/en/04-multimodal/03-speech"
    if any(token in text for token in ("multilingual", "cross-lingual", "translation")):
        return "docs/en/01-core-capabilities/01-multilingual"
    if any(token in text for token in ("hallucination", "factual", "faithfulness")):
        return "docs/en/01-core-capabilities/04-hallucination"
    if any(token in text for token in ("long context", "long-context", "context window")):
        return "docs/en/01-core-capabilities/10-long-context"
    if any(token in text for token in ("memory", "long-term", "episodic")):
        return "docs/en/01-core-capabilities/15-memory"
    if any(token in text for token in ("tool", "function call", "api", "mcp")):
        return "docs/en/01-core-capabilities/11-tool-use"
    if "skill" in text:
        return "docs/en/01-core-capabilities/13-skill-use"
    if any(token in text for token in ("math", "mathematical", "theorem")):
        return "docs/en/01-core-capabilities/08-math"
    if any(token in text for token in ("reasoning", "planning")):
        return "docs/en/01-core-capabilities/09-general-reasoning"
    if any(token in text for token in ("forecast", "prediction")):
        return "docs/en/02-agent-capabilities/08-future-prediction"
    if any(token in text for token in ("long-horizon", "long running", "long-running")):
        return "docs/en/02-agent-capabilities/06-long-running"
    return None


def evidence_type(url: str) -> str:
    lower = url.lower()
    if "arxiv.org/abs/" in lower:
        return "arxiv"
    if "doi.org/" in lower:
        return "doi"
    if "semanticscholar.org" in lower:
        return "semantic_scholar_only"
    return "url"


def should_include(
    item: dict[str, Any],
    section: str | None,
    topic: str | None,
    *,
    min_seed_count: int,
    min_citations: int,
) -> bool:
    if not section or not topic:
        return False
    if int(item.get("seedCount") or 0) < min_seed_count and int(item.get("citationCount") or 0) < min_citations:
        return False
    if topic.endswith("/18-other"):
        return False
    return evidence_type(stable_url(item)) != "semantic_scholar_only"


def english_description(section: str, title: str) -> str:
    if section == "Survey":
        return f"Preliminary title-screen include: surveys or organizes {title}'s stated capability area; parent must verify the abstract before official inclusion."
    if section == "Bench":
        return f"Preliminary title-screen include: appears to define an evaluation, dataset, benchmark, arena, or metric; parent must verify the protocol before official inclusion."
    if section == "Model":
        return f"Preliminary title-screen include: appears to contribute a model-side method named in the title; parent must verify the mechanism before official inclusion."
    if section == "Agent Harness":
        return f"Preliminary title-screen include: appears to contribute an external agent workflow, scaffold, tool loop, memory, or orchestration harness; parent must verify the loop before official inclusion."
    if section == "Skill":
        return f"Preliminary title-screen include: appears to concern reusable agent skills, skill graphs, skill banks, or skill evaluation; parent must verify the artifact before official inclusion."
    return "Preliminary title-screen include; parent must verify evidence before official inclusion."


def chinese_description(section: str) -> str:
    if section == "Survey":
        return "标题级预筛认为该工作可能梳理或组织该能力方向；父级需先核对摘要再正式收录。"
    if section == "Bench":
        return "标题级预筛认为该工作可能定义评测、数据集、benchmark、arena 或指标；父级需先核对协议再正式收录。"
    if section == "Model":
        return "标题级预筛认为该工作可能提出模型侧方法；父级需先核对机制再正式收录。"
    if section == "Agent Harness":
        return "标题级预筛认为该工作可能提出外部 agent 工作流、脚手架、工具循环、记忆或编排 harness；父级需先核对执行逻辑再正式收录。"
    if section == "Skill":
        return "标题级预筛认为该工作可能涉及可复用 agent skill、skill graph、skill bank 或 skill 评测；父级需先核对具体工件再正式收录。"
    return "标题级预筛候选；父级需先核对证据再正式收录。"


def make_decision(item: dict[str, Any], *, min_seed_count: int, min_citations: int) -> dict[str, Any]:
    out = dict(item)
    title = str(item.get("title") or "")
    url = stable_url(item)
    section = choose_section(title)
    topic = choose_topic(title)
    if BIO_RE.search(title):
        out["decision"] = "reject"
        out["reason"] = "Title indicates biomedical, clinical, omics, drug, or patient-facing scope; rejected for this general LLM capability landscape closure."
        return out
    if NARROW_VERTICAL_RE.search(title) and not topic:
        out["decision"] = "reject"
        out["reason"] = "Title indicates a narrow vertical application without a clear reusable capability benchmark, model, harness, or skill signal."
        return out
    if should_include(item, section, topic, min_seed_count=min_seed_count, min_citations=min_citations):
        target_doc = f"{topic}/{SECTION_FILES[section]}"
        out.update(
            {
                "decision": "include",
                "target_doc": target_doc,
                "section": section,
                "stable_url": url,
                "suggested_english_bullet": f"- [{title}]({url}): {english_description(section, title)}",
                "suggested_chinese_bullet": f"- [{title}]({url})：{chinese_description(section)}",
                "reason": (
                    "High-seed title-screen candidate. This is not final inclusion evidence; "
                    "parent must reread the primary source and rewrite the bullet."
                ),
                "rg_en": "not_checked_by_fallback",
                "rg_zh": "not_checked_by_fallback",
                "evidence_url_type": evidence_type(url),
                "uncertainty": "medium_title_only",
            }
        )
    else:
        out["decision"] = "reject"
        if not section:
            out["reason"] = "Rejected by conservative title-only screen: no clear landscape section signal in title."
        elif not topic:
            out["reason"] = "Rejected by conservative title-only screen: section-like words appear, but no clear repository topic target is identifiable."
        elif evidence_type(url) == "semantic_scholar_only":
            out["reason"] = "Rejected by conservative title-only screen: no stable primary URL beyond Semantic Scholar in chunk metadata."
        else:
            out["reason"] = (
                "Rejected by conservative title-only screen: relevant words appear, but seed/citation signal is below "
                "the threshold for parent-review inclusion without an abstract."
            )
    return out


def chunk_number(path: Path) -> int:
    match = re.search(r"chunk-(\d+)\.json$", path.name)
    return int(match.group(1)) if match else -1


def write_memo(
    path: Path,
    *,
    chunk_path: Path,
    decision_path: Path,
    counts: Counter[str],
    min_seed_count: int,
    min_citations: int,
) -> None:
    lines = [
        f"# Title-Screen Memo for {chunk_path.name}",
        "",
        f"- Input file: `{chunk_path}`",
        f"- Output file: `{decision_path}`",
        "- Network called: no.",
        "- Semantic Scholar called: no.",
        "- Official docs edited: no.",
        f"- Counts: include={counts.get('include', 0)}, reject={counts.get('reject', 0)}, defer={counts.get('defer', 0)}.",
        f"- Include threshold: seedCount >= {min_seed_count} or citationCount >= {min_citations}, plus a stable non-S2 URL and an identifiable split-tree target.",
        "- Duplicate handling: this fallback did not run expensive per-title `rg`; parent review and existing-doc URL/title checks must downgrade already-present items.",
        "- Classification uncertainty: medium to high because the chunk metadata contains no abstracts. Include rows are parent-review candidates only; reject rows are conservative title-only decisions for closure bookkeeping.",
        "- Incomplete phase: source reading, URL replacement, bilingual prose rewriting, and official document edits remain parent-owned.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chunk-dir", type=Path, required=True)
    parser.add_argument("--decision-dir", type=Path, required=True)
    parser.add_argument("--memo-dir", type=Path, required=True)
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=999)
    parser.add_argument("--skip-existing", action="store_true")
    parser.add_argument("--min-include-seed-count", type=int, default=20)
    parser.add_argument("--min-include-citations", type=int, default=25)
    args = parser.parse_args()

    total = Counter()
    written = 0
    for chunk_path in sorted(args.chunk_dir.glob("chunk-*.json"), key=chunk_number):
        number = chunk_number(chunk_path)
        if number < args.start or number > args.end:
            continue
        decision_path = args.decision_dir / chunk_path.name
        memo_path = args.memo_dir / f"{chunk_path.stem}.md"
        if args.skip_existing and decision_path.exists() and memo_path.exists():
            continue
        data = read_json(chunk_path)
        if not isinstance(data, list):
            raise SystemExit(f"Expected JSON list: {chunk_path}")
        decisions = [
            make_decision(item, min_seed_count=args.min_include_seed_count, min_citations=args.min_include_citations)
            for item in data
            if isinstance(item, dict)
        ]
        counts = Counter(str(item.get("decision") or "") for item in decisions)
        total.update(counts)
        write_json(decision_path, decisions)
        write_memo(
            memo_path,
            chunk_path=chunk_path,
            decision_path=decision_path,
            counts=counts,
            min_seed_count=args.min_include_seed_count,
            min_citations=args.min_include_citations,
        )
        written += 1
        print(f"{chunk_path.name}: {dict(counts)}", flush=True)
    print(f"written chunks: {written}", flush=True)
    print(f"total decisions: {dict(total)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
