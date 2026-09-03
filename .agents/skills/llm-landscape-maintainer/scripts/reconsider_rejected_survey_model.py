#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any

from landscape_paths import CHAPTER_DIRS, expand_markdown_args, resolve_english_target_doc, split_section_filename


REJECT_STATES = {"reject", "rejected"}
SURVEY_RE = re.compile(
    r"\b(survey|systematic review|literature review|scoping review|meta-analysis|"
    r"comprehensive review|critical review|review of|review on|taxonomy|sok|"
    r"systematization|roadmap|overview|tutorial|landscape|frontiers?|"
    r"position paper|perspective|agenda|manifesto)\b",
    re.I,
)
MODEL_RE = re.compile(
    r"\b(model|models|architecture|pretrain|pre-training|post-train|post-training|"
    r"train(?:ing|ed)?|fine-tun|instruction tun|distill|reinforcement learning|"
    r"\brl\b|reward model|preference optimization|policy optimization|world model|"
    r"foundation model|large language model|llm|vlm|mllm|vla|vision-language-action|"
    r"diffusion|transformer|synthetic data|data synthesis|data generation|"
    r"alignment|reasoning model|speech language model|multimodal model)\b",
    re.I,
)
MODEL_STRONG_RE = re.compile(
    r"\b(model-only|training-only|model architecture|architecture|pretrain|pre-training|"
    r"post-train|post-training|train(?:ing|ed)?|fine-tun|instruction tun|distill|"
    r"reinforcement learning|\brl\b|reward model|preference optimization|policy optimization|"
    r"world model|foundation model|diffusion|transformer|synthetic data|data synthesis|"
    r"data generation|alignment|reasoning model|speech language model|multimodal model|"
    r"vision-language-action|vla)\b",
    re.I,
)
DOMAIN_RE = re.compile(
    r"\b(agent|agentic|tool|mcp|skill|memory|safety|security|cyber|jailbreak|"
    r"prompt injection|software|code|repository|gui|computer use|browser|web|"
    r"terminal|shell|research|scientific|science|review|paper|autonomous driving|"
    r"self-driving|vehicle|robot|robotics|embodied|vla|multilingual|speech|audio|"
    r"video|image|ocr|document|spatial|3d|math|reasoning|hallucination|long context|"
    r"forecast|benchmark|evaluation|leaderboard|workflow|protocol)\b",
    re.I,
)
BIOMED_RE = re.compile(
    r"\b(biomed|biomedical|clinical|clinic|medicine|medical|healthcare|patient|"
    r"hospital|drug|protein|gene|genomic|omics|cell|biology|bioinformatics|"
    r"disease|pathology|radiology|molecule|molecular|therapeutic|dental|dentistry|"
    r"otolaryngology|neurology|neural treatment|diagnos(?:is|es|tic)|treatment|"
    r"chest x-ray|x-ray report|mental health|well-being|pharmacist|pharmacy|"
    r"lesion|chronic diseases?|poultry farming)\b",
    re.I,
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def status_of(item: dict[str, Any]) -> str:
    return str(item.get("decision") or item.get("status") or "").strip().lower()


def text_of(item: dict[str, Any]) -> str:
    fields = [
        item.get("title") or "",
        item.get("abstract") or "",
        item.get("reason") or "",
        item.get("note") or "",
    ]
    return "\n".join(str(field) for field in fields)


def title_reason_text(item: dict[str, Any], rejections: list[dict[str, Any]]) -> str:
    rejection_reasons = [
        str(entry.get("reason") or "")
        for entry in rejections
        if not str(entry.get("reason") or "").startswith("Conservative automatic reject:")
    ]
    return "\n".join(
        [
            str(item.get("title") or ""),
            str(item.get("reason") or ""),
            str(item.get("note") or ""),
            "\n".join(rejection_reasons),
        ]
    )


def evidence_text(item: dict[str, Any], rejections: list[dict[str, Any]]) -> str:
    rejection_reasons = [
        str(entry.get("reason") or "")
        for entry in rejections
        if not str(entry.get("reason") or "").startswith("Conservative automatic reject:")
    ]
    return "\n".join([text_of(item), "\n".join(rejection_reasons)])


def stable_url(item: dict[str, Any], identifier: str) -> str:
    url = str(item.get("url") or "")
    if url and "semanticscholar.org" not in url.lower():
        return url
    if identifier.lower().startswith("arxiv:"):
        return f"https://arxiv.org/abs/{identifier.split(':', 1)[1]}"
    if identifier.lower().startswith("doi:"):
        return f"https://doi.org/{identifier.split(':', 1)[1]}"
    return ""


def display_name(title: str) -> str:
    title = re.sub(r"\s+", " ", title).strip()
    if ":" in title:
        head = title.split(":", 1)[0].strip()
        if 3 <= len(head) <= 80:
            return head
    return title[:90]


def section_doc(chapter: str, topic: str, slug: str, section: str) -> str:
    legacy = f"docs/en/{chapter}-{topic}-{slug}.md"
    return resolve_english_target_doc(legacy, section).as_posix()


def classify_target(text: str, kind: str) -> tuple[str, str]:
    lower = text.lower()
    section = "Survey" if kind == "survey" else "Model"

    if any(term in lower for term in ["benchmark reliability", "llm-as-judge", "judge", "evaluation protocol", "evaluate agentic ai systems"]):
        doc = "docs/en/00-introduction/03-evaluation-methodology.md"
    elif any(term in lower for term in ["multilingual", "low-resource", "korean", "arabic", "dialect", "language-specific", "translation"]):
        doc = section_doc("01", "01", "multilingual", section)
    elif any(term in lower for term in ["scientific knowledge", "scientific table", "science question", "scientific reasoning"]) and "research" not in lower:
        doc = section_doc("01", "02", "scientific-knowledge", section)
    elif any(term in lower for term in ["hallucination", "factuality", "rag", "retrieval-augmented"]):
        doc = section_doc("01", "04", "hallucination", section)
    elif any(term in lower for term in ["ocr", "document", "table understanding", "chart", "diagram"]):
        doc = section_doc("01", "05", "image-ocr", section)
    elif any(term in lower for term in ["video understanding", "video language"]):
        doc = section_doc("01", "06", "video", section)
    elif any(term in lower for term in ["spatial", "3d", "lidar", "point cloud"]):
        doc = section_doc("01", "07", "spatial", section)
    elif any(term in lower for term in ["math", "theorem", "proof", "olympiad"]):
        doc = section_doc("01", "08", "math", section)
    elif any(term in lower for term in ["reasoning model", "chain-of-thought", "general reasoning", "verifiable reasoning"]):
        doc = section_doc("01", "09", "general-reasoning", section)
    elif any(term in lower for term in ["long context", "context window"]):
        doc = section_doc("01", "10", "long-context", section)
    elif any(term in lower for term in ["tool", "mcp", "api", "function calling"]):
        doc = section_doc("01", "11", "tool-use", section)
    elif any(term in lower for term in ["terminal", "shell", "command line", "cli agent"]):
        doc = section_doc("01", "12", "terminal-use", section)
    elif re.search(r"\b(agent skills?|skill use|skill routing|skill repositor|skill librar|codex skill|claude skill)\b", lower):
        doc = section_doc("01", "13", "skill-use", section)
    elif any(term in lower for term in ["writing", "essay", "creative", "story", "screenwriting"]):
        doc = section_doc("01", "14", "writing", section)
    elif any(term in lower for term in ["memory", "episodic", "long-term", "cross-session"]):
        doc = section_doc("01", "15", "memory", section)
    elif any(term in lower for term in ["competitive programming", "programming contest"]):
        doc = section_doc("02", "01", "competitive-programming", section)
    elif any(term in lower for term in ["software", "code", "repository", "program repair", "vulnerability detection", "kernel"]):
        doc = section_doc("02", "02", "software-development", section)
    elif any(term in lower for term in ["web search", "search agent", "search engine"]):
        doc = section_doc("02", "03", "web-search", section)
    elif any(term in lower for term in ["deep research", "research agent", "literature search"]):
        doc = section_doc("02", "04", "deep-research", section)
    elif any(term in lower for term in ["computer use", "gui", "mobile agent", "os agent", "browser agent"]):
        doc = section_doc("02", "05", "computer-use-gui", section)
    elif any(term in lower for term in ["long-horizon", "long horizon", "long-running"]):
        doc = section_doc("02", "06", "long-running", section)
    elif any(term in lower for term in ["finance", "business", "manufacturing", "enterprise", "workflow", "process"]):
        doc = section_doc("02", "07", "real-world-work", section)
    elif any(term in lower for term in ["forecast", "prediction market", "future prediction"]):
        doc = section_doc("02", "08", "future-prediction", section)
    elif any(term in lower for term in ["prompt injection", "jailbreak", "safety", "alignment", "scheming", "deception", "risk", "guardrail", "red team"]):
        doc = section_doc("02", "09", "agent-safety", section)
    elif any(term in lower for term in ["cyber", "penetration", "malware", "ctf", "vulnerability", "security operations"]):
        doc = section_doc("02", "10", "cybersecurity", section)
    elif any(term in lower for term in ["robot", "robotics", "embodied", "manipulation", "navigation", "vla"]):
        doc = section_doc("02", "11", "embodied-vla", section)
    elif any(term in lower for term in ["environment setup", "container", "dependency", "reproducibility"]):
        doc = section_doc("03", "01", "environment-setup", section)
    elif any(term in lower for term in ["research", "scientific", "paper", "peer review", "novelty", "hypothesis"]):
        doc = section_doc("03", "02", "research", section)
    elif any(term in lower for term in ["image generation", "text-to-image", "diffusion", "image editing"]):
        doc = section_doc("04", "01", "image-generation-editing", section)
    elif any(term in lower for term in ["video generation", "movie", "foley"]):
        doc = section_doc("04", "02", "video-generation", section)
    elif any(term in lower for term in ["speech", "audio", "voice", "tts", "asr", "music"]):
        doc = section_doc("04", "03", "speech", section)
    elif any(term in lower for term in ["autonomous driving", "self-driving", "vehicle", "driving", "traffic"]):
        doc = section_doc("04", "04", "autonomous-driving", section)
    else:
        doc = section_doc("01", "16", "other", section)

    return doc, section


def reason_for(item: dict[str, Any], kind: str) -> str:
    title = item.get("title") or ""
    if kind == "survey":
        return f"Previously rejected under artifact-only criteria, but the new taxonomy has Survey sections and this appears to be a survey/review/taxonomy candidate: {title}"
    return f"Previously rejected as model/training/architecture/RL/data-synthesis work, but the new taxonomy has Model sections and this appears model-related: {title}"


def bullet(item: dict[str, Any], kind: str, lang: str) -> str:
    identifier = str(item.get("identifier") or "")
    url = stable_url(item, identifier)
    name = display_name(str(item.get("title") or identifier))
    abstract = " ".join(str(item.get("abstract") or "").split())
    if abstract:
        summary_en = abstract[:220].rstrip()
    else:
        summary_en = str(item.get("title") or identifier)
    if lang == "en":
        if kind == "survey":
            return f"- [{name}]({url}): Surveys {summary_en}"
        return f"- [{name}]({url}): A model-side contribution. Core idea: {summary_en}"
    if kind == "survey":
        return f"- [{name}]({url})：综述类相关工作。核心内容：{summary_en}"
    return f"- [{name}]({url})：模型侧相关工作。核心思路：{summary_en}"


def load_metadata(paths: list[Path], chunk_dirs: list[Path]) -> dict[str, dict[str, Any]]:
    meta: dict[str, dict[str, Any]] = {}
    for path in paths:
        if not path.exists():
            continue
        data = read_json(path)
        if not isinstance(data, list):
            continue
        for item in data:
            if isinstance(item, dict) and item.get("identifier"):
                meta.setdefault(str(item["identifier"]), {}).update(item)
    for directory in chunk_dirs:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("chunk-*.json")):
            data = read_json(path)
            if not isinstance(data, list):
                continue
            for item in data:
                if isinstance(item, dict) and item.get("identifier"):
                    meta.setdefault(str(item["identifier"]), {}).update(item)
    return meta


def collect_rejections(round_dirs: list[Path]) -> dict[str, dict[str, Any]]:
    rejected: dict[str, dict[str, Any]] = {}
    for directory in round_dirs:
        auto = directory / "auto_reject.json"
        if auto.exists():
            data = read_json(auto)
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and item.get("identifier"):
                        rec = rejected.setdefault(str(item["identifier"]), {"identifier": item["identifier"], "rejections": []})
                        rec["rejections"].append({"source": str(auto), "reason": item.get("note") or item.get("reason") or ""})
        decisions = directory / "decisions"
        if decisions.exists():
            for path in sorted(decisions.glob("chunk-*.json")):
                data = read_json(path)
                if not isinstance(data, list):
                    continue
                for item in data:
                    if not isinstance(item, dict) or not item.get("identifier"):
                        continue
                    if status_of(item) in REJECT_STATES:
                        rec = rejected.setdefault(str(item["identifier"]), {"identifier": item["identifier"], "rejections": []})
                        rec["rejections"].append({"source": str(path), "reason": item.get("reason") or item.get("note") or ""})
    return rejected


def docs_text(paths: list[Path]) -> str:
    return "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in paths if path.exists())


def already_in_docs(item: dict[str, Any], text: str) -> bool:
    identifier = str(item.get("identifier") or "")
    raw = identifier.split(":", 1)[1] if ":" in identifier else identifier
    url = stable_url(item, identifier)
    return bool((raw and raw in text) or (identifier and identifier in text) or (url and url in text))


def write_chunks(items: list[dict[str, Any]], chunk_dir: Path, chunk_size: int) -> None:
    chunk_dir.mkdir(parents=True, exist_ok=True)
    for old in chunk_dir.glob("chunk-*.json"):
        old.unlink()
    total = max(1, math.ceil(len(items) / max(1, chunk_size)))
    for index in range(total):
        chunk = items[index * chunk_size : (index + 1) * chunk_size]
        write_json(chunk_dir / f"chunk-{index + 1:03d}.json", chunk)


def main() -> int:
    parser = argparse.ArgumentParser(description="Reconsider rejected citation candidates for new Survey and Model sections.")
    parser.add_argument("--round-dir", action="append", type=Path, required=True)
    parser.add_argument("--candidate-json", action="append", type=Path, default=[])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--non-candidate-out", type=Path, required=True)
    parser.add_argument("--chunk-dir", type=Path, required=True)
    parser.add_argument("--chunk-size", type=int, default=120)
    parser.add_argument("docs", nargs="*", help="Markdown files or globs. Defaults to the recursive docs tree plus root README files.")
    args = parser.parse_args()

    chunk_dirs = [path / "chunks" for path in args.round_dir]
    meta = load_metadata(args.candidate_json, chunk_dirs)
    rejected = collect_rejections(args.round_dir)
    doc_paths = expand_markdown_args(args.docs)
    existing = docs_text(doc_paths)

    candidates: list[dict[str, Any]] = []
    non_candidates: list[dict[str, Any]] = []
    for identifier, reject_info in sorted(rejected.items()):
        item = dict(meta.get(identifier) or {})
        item.setdefault("identifier", identifier)
        item.setdefault("title", reject_info.get("title") or "")
        item["rejections"] = reject_info["rejections"]
        merged_text = evidence_text(item, item["rejections"])
        strong_text = title_reason_text(item, item["rejections"])
        if already_in_docs(item, existing):
            item["reconsider_status"] = "already_in_docs"
            non_candidates.append(item)
            continue
        if BIOMED_RE.search(merged_text):
            item["reconsider_status"] = "excluded_biomedical"
            non_candidates.append(item)
            continue
        kind = ""
        if SURVEY_RE.search(strong_text) and DOMAIN_RE.search(merged_text):
            kind = "survey"
        elif MODEL_STRONG_RE.search(strong_text) and DOMAIN_RE.search(merged_text):
            kind = "model"
        if not kind:
            item["reconsider_status"] = "still_rejected_not_survey_or_model"
            non_candidates.append(item)
            continue
        url = stable_url(item, identifier)
        if not url:
            item["reconsider_status"] = "defer_no_stable_url"
            non_candidates.append(item)
            continue
        target_doc, section = classify_target(merged_text, kind)
        resolved_doc = resolve_english_target_doc(target_doc, section)
        item.update(
            {
                "decision": "reconsider",
                "reconsider_kind": kind,
                "target_doc": resolved_doc.as_posix(),
                "section": section,
                "reason": reason_for(item, kind),
                "url": url,
                "suggested_english_bullet": bullet(item, kind, "en"),
                "suggested_chinese_bullet": bullet(item, kind, "zh"),
            }
        )
        candidates.append(item)

    candidates.sort(
        key=lambda item: (
            item.get("reconsider_kind") != "survey",
            str(item.get("target_doc") or ""),
            -(int(item.get("year") or 0)),
            str(item.get("identifier") or ""),
        )
    )
    write_json(args.out, candidates)
    write_json(args.non_candidate_out, non_candidates)
    write_chunks(candidates, args.chunk_dir, args.chunk_size)
    print(f"Rejected identifiers: {len(rejected)}", flush=True)
    print(f"Reconsider candidates: {len(candidates)}", flush=True)
    print(f"Still rejected/deferred: {len(non_candidates)}", flush=True)
    print(f"Wrote {args.out}", flush=True)
    print(f"Wrote {args.non_candidate_out}", flush=True)
    print(f"Wrote chunks under {args.chunk_dir}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
