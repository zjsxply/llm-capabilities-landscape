#!/usr/bin/env python3
"""Audit landscape Markdown for generic or template TLDR lines."""

from __future__ import annotations

import argparse
import glob
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from landscape_paths import default_markdown_files
except Exception:  # pragma: no cover - fallback for copied standalone use.
    default_markdown_files = None


@dataclass(frozen=True)
class PatternSpec:
    name: str
    regex: str
    flags: int = re.IGNORECASE
    batch: str = "Manual review"
    section: str | None = None


BATCH_BY_SECTION = {
    "02-survey.md": "Survey placeholder rewrite",
    "03-bench.md": "Bench placeholder rewrite",
    "04-model.md": "Model placeholder rewrite",
    "05-agent-harness.md": "Agent Harness placeholder rewrite",
    "06-skill.md": "Skill placeholder rewrite",
}


PATTERNS: tuple[PatternSpec, ...] = (
    PatternSpec(
        "en_survey_methods_evidence_landscape",
        r"\bSurveys? [^\n:]+ methods, evidence, and open problems relevant to the landscape\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_survey_methods_risks_boundaries",
        r"\bSurveys? [^\n:]+ methods, risks, or evaluation boundaries relevant to the landscape\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_survey_methods_risks_datasets",
        r"\bSurveys? [^\n:]+ methods, risks, datasets, or deployment patterns relevant to the landscape\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_survey_taxonomy_synthesis",
        r"\bSurveys? [^\n:]+ and provides a useful taxonomy or synthesis for the landscape\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_adds_survey_synthesis_coverage",
        r"\bAdds a survey or synthesis entry for [^\n.]+ coverage\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_adds_survey_reference_for",
        r"\bAdds a survey reference for [^\n.]+\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_survey_candidate_parent_review",
        r"\bSurvey candidate for parent review[^\n.]*\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_adds_survey_entry_for",
        r"\bAdds a survey entry for [^\n.]+\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_surveys_research_workflow_automation",
        r"\bSurveys research workflow automation and organizes [^\n.]+\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_surveys_taxonomizes_or_positions",
        r"\bSurveys, taxonomizes, or positions [^\n.]+\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_surveys_methods_risks_evaluation_practices",
        r"\bSurveys methods, risks, evaluation practices,? or classification frameworks [^\n.]*\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_surveys_or_systematizes_research_automation",
        r"\bSurveys or systematizes research automation, research evaluation, and scientific-literature workflows[^\n.]*\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_surveys_reviews_taxonomizes_research_workflows",
        r"\bSurveys, reviews, or taxonomizes research workflows[^\n.]*\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_surveys_recent_methods_risks_open_problems",
        r"\bSurveys recent methods, risks, and open problems for [^\n.]+\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_surveys_agent_capability_recent_map",
        r"\bSurveys [^\n.]+ capability, adding a recent map of methods, benchmarks, risks, or open problems\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_maps_recent_work_open_issues_coverage",
        r"\bMaps recent work and open issues for [^\n.]+ coverage\.?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "en_benchmark_coverage",
        r"\b(?:Benchmarks or evaluates|Evaluates|Adds a benchmark|Adds an evaluation|Provides a benchmark|Benchmarks) [^\n.]+(?:adding coverage for|for [A-Z][A-Za-z -]+ coverage|capability coverage)[^\n.]*\.?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "en_benchmarks_or_evaluates_capability",
        r"\bBenchmarks or evaluates [^\n,]+ capability, adding coverage for [^\n.]+\.?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "en_adds_benchmark_dataset_metric",
        r"\bAdds an? (?:evaluation )?(?:benchmark|target|dataset|protocol|metric)[^\n.]+(?:coverage|capability)[^\n.]*\.?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "en_provides_dataset_for_measuring_capability",
        r"\bProvides a (?:dataset, benchmark, metric, or evaluation protocol|benchmark, dataset, or evaluation protocol) for measuring [^\n.]+ capabilities\.?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "en_provides_benchmark_dataset_protocol_short",
        r"\bProvides a (?:benchmark, dataset, challenge, or evaluation protocol|benchmark, dataset, or evaluation protocol|benchmark, dataset, or evaluation protocol for [a-z -]+ capability|dataset and evaluation framework) for [^\n.]+\.?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "en_model_side_generic",
        r"\b(?:Adds|Introduces) (?:a )?model-side (?:method|methods), training recipe, architecture, data method, reward model, verifier, or inference-scaling method for [^\n.]+ coverage\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_side_capability_coverage",
        r"\bIntroduces model-side methods for [^\n]+ capability, adding coverage for [^\n.]+\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_side_through_title",
        r"\bAdds a model-side (?:method|contribution), (?:architecture, )?(?:training recipe, )?(?:or )?(?:data-generation route|data method|reward modeling|synthetic data|post-training|world-model machinery) for [^\n.]+ through [^\n.]+\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_side_fitting_section",
        r"\bIntroduces a model-side method, architecture, training recipe, or adaptation signal for [^\n,]+, fitting the [^\n.]+ section\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_side_stated_contribution",
        r"\bContributes a model-side method for [^\n.]+ through the paper's stated contribution\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_side_generic_inventory",
        r"\b(?:Adds|Contributes|Introduces) (?:a )?model-side (?:work|contribution|method|methods)[^\n.]*\b(?:such as|including|covering|adding) (?:training|architecture|post-training|adaptation|alignment|reward|verifier|world model|world-model|synthetic data|synthetic-data|inference-scaling|generation)[^\n.]*\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_reusable_title_signal",
        r"\bAdds a model reference for [^\n,]+, with a reusable contribution signaled by the title rather than a narrow application-only result\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_candidate_covering_title",
        r"\bAdds a [^\n.]+ model candidate covering [^\n.]+\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_introduces_or_analyzes_generic",
        r"\bIntroduces or analyzes a model-side method for [^\n]+ capability, adding (?:training|architecture|alignment|verifier|synthetic-data|generation|coverage)[^\n.]*\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_around_generic_axes",
        r"\b[A-Za-z0-9][^\n:]{0,100} adds a [^\n.]+ model around control, editing, motion synthesis, world modeling, or authenticity\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_relevant_capabilities_only",
        r"\bIntroduces a model-side method relevant to [^\n.]+ capabilities\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_training_inventory",
        r"\bIntroduces model-side training, architecture, (?:post-training, reinforcement learning, synthetic data, reward modeling, generation, or adaptation|alignment, generation, adaptation, or reward-modeling) work for [^\n.]+\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_candidate_covering_title_family",
        r"\bAdds a [^\n.]+ model candidate covering [^\n.]+\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_core_around_title_generic",
        r"\bCore idea:?(?: [^\n.]{0,80})? (?:centers on|is built around|focuses on) [A-Z][^\n.]{12,220}\.?",
        batch="Title-signal placeholder rewrite",
    ),
    PatternSpec(
        "en_model_develops_with_targeting",
        r"\bDevelops [^\n.]{8,220} with [^\n.]{3,180}, targeting [^\n.]+\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_this_work_studies_generic",
        r"\bThis work studies [^\n.]{8,220}\.?$",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_model_adds_route_or_lens_generic",
        r"\b(?:adds|adding|complementing|strengthening) (?:a )?(?:model-side )?(?:route|lens|reference|safeguard|model entry|model line|coverage) (?:for|to|on) [^\n.]+\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_off_axis_pure_model_note",
        r"\bOff-axis for a pure model entry; [^\n.]+\.?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "en_agent_workflow_tool_mediated",
        r"\bBuilds an agent workflow or tool-mediated system for [^\n.]+ tasks\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_harness_expose_workflow_logic",
        r"\bA harness for [^\n.]+\. Core idea: expose workflow logic outside the base model so planning, tool use, memory, verification, recovery, or orchestration can be studied and reused\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_workflow_orchestration_short",
        r"\bBuilds an agent workflow or orchestration pattern for [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_harness_list_adds",
        r"\bAdds an agent harness, workflow, planner, tool loop, memory loop, or orchestration pattern for [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_external_workflow",
        r"\b(?:Contributes|Adds) an external workflow, tool, memory, retrieval, orchestration, or agent loop for [^\n.]+ capabilities\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_workflow_orchestration_runtime",
        r"\b(?:contributes|contribute|adds|Adds|Introduces|Contributes) an? agent workflow, orchestration pattern, tool loop, or runtime harness for [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_workflow_tool_loop_memory_control_runtime",
        r"\b(?:Contributes|Adds|Introduces) an? agent workflow, orchestration pattern, tool loop, memory or control mechanism, or runtime harness for [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agentic_workflow_generation_optimization",
        r"\bAdds an agentic workflow for generating and optimizing [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_workflow_planning_tool",
        r"\b[^:]{0,160}\badds an agent workflow, orchestration pattern, planning loop, or tool-use harness for [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_workflow_tool_loop_memory",
        r"\bAdds an agent workflow, orchestration pattern, tool loop, memory mechanism, or multi-agent harness for [^\n.]+ coverage\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_builds_workflow_tool_loop",
        r"\bBuilds a workflow, tool loop, retrieval pipeline, multi-agent process, simulator, or execution scaffold for [^\n.]+ tasks\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_presents_workflow_retrieval_tool",
        r"\bPresents a workflow, retrieval/tool loop, verification method, prompting strategy, or orchestration harness for [^\n.]+ capability\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_capability_taxonomy_harness",
        r"\b[A-Z][A-Za-z0-9_.: -]{1,120} adds a capability-taxonomy agent-harness\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_candidate_title_signal",
        r"\bAdds a[n]? agent[- ]harness entry for [^\n,]+, (?:centered on|focusing on) [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_harness_entry_focusing_title",
        r"\bAdds an? agent harness entry for [^\n,]+, focusing on [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_workflow_or_scaffold",
        r"\bBuilds an agent, workflow, tool, or system scaffold for [^\n,]+, making it an Agent Harness candidate rather than a pure model entry\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_agent_reusable_orchestration",
        r"\bAdds reusable orchestration, prompting, planning, tool-use, memory, or environment-management logic for [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_around_title_external_layer",
        r"\bBuilds an external workflow, retrieval, tool-use, memory, or orchestration layer around [^\n.]+\.?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "en_adds_skill_suitable_generic",
        r"\bis suitable for [^\n.]+(?:coverage|tasks|workflows|analysis|management)[^\n.]*\.?",
        batch="Skill placeholder rewrite",
        section="06-skill.md",
    ),
    PatternSpec(
        "en_relevant_to_landscape",
        r"\brelevant to the landscape\.?",
        batch="Generic landscape phrasing",
    ),
    PatternSpec(
        "en_capability_signal_stated_in_title",
        r"\bfocusing on the capability signal stated in the title\.?",
        batch="Title-signal placeholder rewrite",
    ),
    PatternSpec(
        "zh_survey_generic",
        r"(?:\u8865\u5145|\u68b3\u7406|\u7cfb\u7edf\u68b3\u7406|\u9762\u5411)[^\n\u3002]*(?:\u7efc\u8ff0|survey|research landscape|\u8109\u7edc\u68b3\u7406)[^\n\u3002]*(?:\u8986\u76d6|\u8865\u5145|\u4f5c\u4e3a|\u65b9\u5411|\u80fd\u529b)[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_parent_review_survey_generic",
        r"(?:\u5efa\u8bae\u7236\u7ea7\u590d\u6838|\u540e\u7eed\u7236\u7ea7\u590d\u6838|\u4f9b\u7236\u7ea7\u590d\u6838)[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_title_shows_contribution",
        r"\u6807\u9898\u663e\u793a\u5176\u8d21\u732e[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_adds_research_survey_entry",
        r"\u8865\u5145\u79d1\u7814\u7684 Survey \u6761\u76ee[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_research_workflow_automation_parent_review",
        r"\u7efc\u8ff0\u7814\u7a76\u5de5\u4f5c\u6d41\u81ea\u52a8\u5316[^\n\u3002]*(?:\u7236\u7ea7\u590d\u6838|\u65b9\u6cd5|\u8bc1\u636e|\u5f00\u653e\u95ee\u9898)[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_taxonomizes_positions_capability_direction",
        r"\u68b3\u7406\u3001\u5206\u7c7b\u6216\u5b9a\u4f4d\u8be5\u80fd\u529b\u65b9\u5411[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_research_workflow_methods_risks",
        r"\u68b3\u7406(?:\u79d1\u7814|\u7814\u7a76)\u5de5\u4f5c\u6d41[^\n\u3002]*(?:\u65b9\u6cd5|\u98ce\u9669|\u8bc4\u6d4b\u5b9e\u8df5|\u5206\u7c7b\u6846\u67b6|\u6570\u636e\u96c6)[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_surveys_recent_methods_risks_open_problems",
        r"\u68b3\u7406[^\n\u3002]*(?:\u76f8\u5173|\u8fd1\u671f)?\u65b9\u6cd5\u3001\u98ce\u9669\u4e0e\u5f00\u653e\u95ee\u9898\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_surveys_agent_capability_recent_map",
        r"\u7efc\u8ff0[^\n\u3002]*(?:\u80fd\u529b|\u81ea\u52a8\u53d1\u73b0)[^\n\u3002]*(?:\u65b9\u6cd5|\u57fa\u51c6|\u98ce\u9669|\u5f00\u653e\u95ee\u9898)\u8109\u7edc\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_around_title_supplement_generic_survey",
        r"\u56f4\u7ed5[^\n\u3002]{4,220}(?:\u8865\u5145|\u68b3\u7406)[^\n\u3002]*(?:survey|Survey|\u7efc\u8ff0|\u5206\u7c7b|\u8109\u7edc|\u6761\u76ee|\u5019\u9009|\u80fd\u529b)[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_supplements_viewpoint_background_generic_survey",
        r"(?:\u4e3a|\u7ed9|\u5411|\u5bf9|\u56f4\u7ed5)[^\n\u3002]{2,160}\u8865\u5145[^\n\u3002]*(?:\u89c6\u89d2|\u80cc\u666f|\u56fe\u8c31|\u8def\u7ebf|\u7ebf\u7d22|\u6848\u4f8b|\u53c2\u8003|\u8986\u76d6|\u6761\u76ee|\u8109\u7edc)[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_around_title_builds_generic_survey",
        r"\u56f4\u7ed5[^\n\u3002]{4,220}\u6784\u5efa[^\n\u3002]*(?:survey|Survey|\u7efc\u8ff0|\u5206\u7c7b|\u8109\u7edc|\u7814\u7a76\u56fe\u8c31|\u98ce\u9669\u6846\u67b6|\u65b9\u6cd5\u8c31\u7cfb|\u80fd\u529b)[^\n\u3002]*\u3002?",
        batch="Survey placeholder rewrite",
        section="02-survey.md",
    ),
    PatternSpec(
        "zh_landscape_generic",
        r"(?:\u4e3a|\u9762\u5411)[^\n\u3002]*(?:landscape|\u80fd\u529b\u56fe\u8c31|\u80fd\u529b\u5206\u7c7b)[^\n\u3002]*(?:\u8865\u5145|\u8986\u76d6)[^\n\u3002]*\u3002?",
        batch="Generic landscape phrasing",
    ),
    PatternSpec(
        "zh_agent_workflow_tool_loop",
        r"(?:\u6784\u5efa|\u8865\u5145|\u63d0\u4f9b|\u63d0\u51fa|\u8d21\u732e|\u4e3a)[^\n\u3002]*(?:\u5de5\u4f5c\u6d41|\u667a\u80fd\u4f53\u6d41\u7a0b|\u7f16\u6392\u6a21\u5f0f|\u5de5\u5177\u5faa\u73af|\u68c0\u7d22\u7ba1\u7ebf|\u591a\u667a\u80fd\u4f53\u6d41\u7a0b|\u6267\u884c\u811a\u624b\u67b6|\u8fd0\u884c\u65f6\u6846\u67b6|\u667a\u80fd\u4f53\u6846\u67b6|Agent Harness)[^\n\u3002]*(?:\u4efb\u52a1|\u80fd\u529b|\u81ea\u52a8\u9a7e\u9a76|Autonomous Driving|coverage|\u5019\u9009)[^\n\u3002]*\u3002?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "zh_agent_harness_type_core_value",
        r"\u7c7b\u578b\uff1aagent harness/\u53ef\u590d\u7528\u6267\u884c\u6846\u67b6\u3002\u6838\u5fc3\u4ef7\u503c\uff1a\u4e3a [^\n\u3002]+\u8865\u5145\u53ef\u590d\u7528\u7684\u6267\u884c\u6d41\u7a0b\u3001\u5de5\u5177\u7f16\u6392\u3001\u8bb0\u5fc6\u7ba1\u7406\u6216\u591a agent \u534f\u4f5c\u673a\u5236\u3002?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "zh_agent_workflow_tool_loop_memory_control_runtime",
        r"\u4e3a[^\n\u3002]{2,120}\u8865\u5145\u667a\u80fd\u4f53\u5de5\u4f5c\u6d41\u3001\u7f16\u6392\u6a21\u5f0f\u3001\u5de5\u5177\u5faa\u73af\u3001\u8bb0\u5fc6\u6216\u63a7\u5236\u673a\u5236\u3001\u8fd0\u884c\u65f6\u6846\u67b6\u3002?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "zh_agent_capability_taxonomy_harness",
        r"\u8865\u5145\u80fd\u529b\u5206\u7c7b\u667a\u80fd\u4f53\u6846\u67b6\u3002?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "zh_around_title_supplement_generic_bench",
        r"\u56f4\u7ed5[^\n\u3002]{4,220}\u8865\u5145[^\n\u3002]*(?:benchmark|\u57fa\u51c6|\u6570\u636e\u96c6|\u8bc4\u6d4b|\u6307\u6807|\u534f\u8bae|\u80fd\u529b)[^\n\u3002]*\u3002?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "zh_around_title_builds_generic_bench",
        r"\u56f4\u7ed5[^\n\u3002]{4,220}\u6784\u5efa[^\n\u3002]*(?:benchmark|\u57fa\u51c6|\u6570\u636e\u96c6|\u8bc4\u6d4b|\u6307\u6807|\u534f\u8bae|\u80fd\u529b)[^\n\u3002]*\u3002?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "zh_around_title_supplement_generic_model",
        r"\u56f4\u7ed5[^\n\u3002]{4,220}\u8865\u5145[^\n\u3002]*(?:\u6a21\u578b|\u8bad\u7ec3|\u67b6\u6784|\u5bf9\u9f50|\u540e\u8bad\u7ec3|\u6570\u636e|\u9002\u914d|Model)[^\n\u3002]*\u3002?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "zh_supplement_one_for_bench_generic",
        r"(?:\u8865\u5145\u4e00\u4e2a|\u4e3a[^\n\u3002]{2,80}\u8865\u5145\u4e00\u4e2a|\u8865\u5145[^\n\u3002]{0,40}\u7684 Bench \u6761\u76ee)[^\n\u3002]*(?:\u57fa\u51c6|\u6570\u636e\u96c6|\u8bc4\u6d4b|\u6307\u6807|\u534f\u8bae|\u6761\u76ee|\u5019\u9009|\u8986\u76d6)[^\n\u3002]*\u3002?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "zh_supplement_one_for_model_generic",
        r"(?:\u8865\u5145\u4e00\u4e2a|\u4e3a[^\n\u3002]{2,80}\u8865\u5145\u4e00\u4e2a)[^\n\u3002]*(?:\u6a21\u578b|\u6a21\u578b\u4fa7|\u8bad\u7ec3|\u67b6\u6784|\u540e\u8bad\u7ec3|\u6570\u636e|\u9002\u914d|Model|\u6761\u76ee|\u5019\u9009|\u8986\u76d6)[^\n\u3002]*\u3002?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "zh_supplement_one_for_agent_generic",
        r"(?:\u8865\u5145\u4e00\u4e2a|\u4e3a[^\n\u3002]{2,80}\u8865\u5145\u4e00\u4e2a)[^\n\u3002]*(?:agent|Agent|Agent Harness|\u667a\u80fd\u4f53|\u5de5\u4f5c\u6d41|\u7f16\u6392|\u5de5\u5177|\u68c0\u7d22|\u8bb0\u5fc6|\u6761\u76ee|\u5019\u9009|\u8986\u76d6)[^\n\u3002]*\u3002?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "zh_around_title_supplement_generic_agent",
        r"\u56f4\u7ed5[^\n\u3002]{4,220}\u8865\u5145[^\n\u3002]*(?:agent|Agent|Agent Harness|\u667a\u80fd\u4f53|\u5de5\u4f5c\u6d41|\u7f16\u6392|\u5de5\u5177|\u68c0\u7d22|\u8bb0\u5fc6|\u89c4\u5212|\u591a\u667a\u80fd\u4f53)[^\n\u3002]*\u3002?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "zh_around_title_builds_generic_agent",
        r"\u56f4\u7ed5[^\n\u3002]{4,220}\u6784\u5efa[^\n\u3002]*(?:agent|Agent|Agent Harness|\u667a\u80fd\u4f53|\u5de5\u4f5c\u6d41|\u7f16\u6392|\u5de5\u5177|\u68c0\u7d22|\u8bb0\u5fc6|\u89c4\u5212|\u591a\u667a\u80fd\u4f53|\u5916\u90e8\u5de5\u4f5c\u6d41)[^\n\u3002]*\u3002?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "zh_around_title_supplement_generic_skill",
        r"\u56f4\u7ed5[^\n\u3002]{4,220}\u8865\u5145[^\n\u3002]*(?:skill|Skill|\u6280\u80fd|\u4efb\u52a1\u5305|\u811a\u672c|\u6a21\u677f)[^\n\u3002]*\u3002?",
        batch="Skill placeholder rewrite",
        section="06-skill.md",
    ),
    PatternSpec(
        "zh_around_title_builds_generic_skill",
        r"\u56f4\u7ed5[^\n\u3002]{4,220}\u6784\u5efa[^\n\u3002]*(?:skill|Skill|\u6280\u80fd|\u4efb\u52a1\u5305|\u811a\u672c|\u6a21\u677f)[^\n\u3002]*\u3002?",
        batch="Skill placeholder rewrite",
        section="06-skill.md",
    ),
    PatternSpec(
        "zh_proposes_for_bench_generic",
        r"\u63d0\u51fa\u9762\u5411[^\n\u3002]{2,160}\u7684(?:benchmark|\u57fa\u51c6|\u6570\u636e\u96c6|\u8bc4\u6d4b|\u6307\u6807|\u534f\u8bae)[^\n\u3002]*\u3002?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "zh_provides_for_measuring_capability",
        r"\u63d0\u4f9b\u7528\u4e8e\u8861\u91cf[^\n\u3002]{2,120}\u80fd\u529b\u7684(?:\u6570\u636e\u96c6|\u57fa\u51c6|\u6307\u6807|\u8bc4\u6d4b\u534f\u8bae|\u57fa\u51c6\u3001\u6570\u636e\u96c6|\u6570\u636e\u96c6\u3001\u57fa\u51c6)[^\n\u3002]*\u3002?",
        batch="Bench placeholder rewrite",
        section="03-bench.md",
    ),
    PatternSpec(
        "zh_proposes_for_model_generic",
        r"\u63d0\u51fa\u9762\u5411[^\n\u3002]{2,160}\u7684(?:\u6a21\u578b\u4fa7|\u6a21\u578b|\u8bad\u7ec3|\u67b6\u6784|\u540e\u8bad\u7ec3|\u6570\u636e|\u5bf9\u9f50|\u751f\u6210|\u9002\u914d|\u5956\u52b1\u5efa\u6a21)[^\n\u3002]*\u3002?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "zh_proposes_for_agent_generic",
        r"\u63d0\u51fa\u9762\u5411[^\n\u3002]{2,160}\u7684(?:agent|Agent|Agent Harness|\u667a\u80fd\u4f53|\u5de5\u4f5c\u6d41|\u7f16\u6392|\u5de5\u5177\u5faa\u73af|\u6267\u884c\u6846\u67b6|\u591a\u667a\u80fd\u4f53)[^\n\u3002]*\u3002?",
        batch="Agent Harness placeholder rewrite",
        section="05-agent-harness.md",
    ),
    PatternSpec(
        "zh_publishes_title_generic",
        r"\u53d1\u5e03[^\n\u3002]{2,180}(?:\u8fd9\u4e00|\u4f5c\u4e3a[^\n\u3002]{0,80}\u6761\u76ee|\u8865\u5145[^\n\u3002]{0,80}\u6761\u76ee|\u80fd\u529b\u6761\u76ee|\u6761\u76ee\u5019\u9009)[^\n\u3002]*\u3002?",
        batch="Generic landscape phrasing",
    ),
    PatternSpec(
        "zh_focus_title_brackets_generic",
        r"\u91cd\u70b9\u662f\u300a[^\n\u300b]{4,220}\u300b\u3002?",
        batch="Title-signal placeholder rewrite",
    ),
    PatternSpec(
        "zh_capability_signal_title",
        r"\u5173\u6ce8\u6807\u9898\u6240\u793a\u7684\u53ef\u590d\u7528\u80fd\u529b\u3001\u65b9\u6cd5\u6216\u8bc4\u6d4b\u4fe1\u53f7\u3002?",
        batch="Title-signal placeholder rewrite",
    ),
    PatternSpec(
        "zh_model_side_generic",
        r"(?:\u8865\u5145|\u5f15\u5165|\u4f5c\u4e3a)[^\n\u3002]*(?:Model \u6761\u76ee\u5019\u9009|\u6a21\u578b\u4fa7\u65b9\u6cd5|\u8bad\u7ec3\u914d\u65b9|\u67b6\u6784|\u6570\u636e\u65b9\u6cd5|reward model|verifier|inference-scaling)[^\n\u3002]*\u3002?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "zh_model_supplement_route_clue_generic",
        r"(?:\u8865\u5145|\u4e3a[^\n\u3002]{1,120}\u8865\u5145)[^\n\u3002]*(?:\u6a21\u578b\u8def\u7ebf|\u6a21\u578b\u7ebf\u7d22|\u6a21\u578b\u4efb\u52a1\u7ebf\u7d22|\u6a21\u578b\u65b9\u6cd5|\u6a21\u578b\u4fa7\u53c2\u8003|\u6a21\u578b\u4fa7\u8def\u7ebf|\u6a21\u578b\u4fa7\u4fdd\u969c|\u6a21\u578b\u5206\u6790\u89c6\u89d2|\u8986\u76d6)[^\n\u3002]*\u3002?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "zh_model_supplement_capability_title_generic",
        r"\u8865\u5145\u9762\u5411[^\n\u3002]{2,120}\u7684\u6a21\u578b\u4fa7\u5de5\u4f5c\uff0c\u91cd\u70b9\u662f[^\n\u3002]+\u3002?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "zh_model_general_method_inventory_generic",
        r"\u63d0\u51fa\u9762\u5411[^\n\u3002]{2,120}\u7684\u6a21\u578b\u4fa7(?:\u65b9\u6cd5|\u8bad\u7ec3|\u67b6\u6784|\u540e\u8bad\u7ec3|\u5f3a\u5316\u5b66\u4e60|\u5408\u6210\u6570\u636e|\u5956\u52b1\u5efa\u6a21|\u751f\u6210|\u9002\u914d)[^\n\u3002]*\u3002?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "zh_model_title_signal",
        r"(?:\u4f5c\u4e3a|\u8865\u5145|\u5f15\u5165)[^\n\u3002]*(?:\u6a21\u578b\u5019\u9009|\u6a21\u578b\u6761\u76ee)[^\n\u3002]*(?:\u6807\u9898\u6240\u793a|\u53ef\u590d\u7528\u80fd\u529b|\u65b9\u6cd5\u6216\u8bc4\u6d4b\u4fe1\u53f7)[^\n\u3002]*\u3002?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "zh_model_around_builds_targets",
        r"\u56f4\u7ed5[^\n\u3002]{6,220}\u6784\u5efa[^\n\u3002]{2,180}\u9762\u5411[^\n\u3002]+\u3002?",
        batch="Model placeholder rewrite",
        section="04-model.md",
    ),
    PatternSpec(
        "zh_as_section_candidate_generic",
        r"\u4f5c\u4e3a (?:Survey|Bench|Model|Agent Harness|Skill) \u6761\u76ee\u5019\u9009\u3002?",
        batch="Section-candidate placeholder rewrite",
    ),
    PatternSpec(
        "zh_adds_facing_section_focus_generic",
        r"\u8865\u5145\u4e00\u4e2a\u9762\u5411[^\n\u3002]{2,120}\u7684(?:\u7efc\u8ff0|Survey|\u57fa\u51c6|Bench|\u6a21\u578b|Model|\u667a\u80fd\u4f53\u6846\u67b6|Agent Harness|\u6280\u80fd|Skill)\u6761\u76ee[^\n\u3002]*(?:\u5173\u6ce8|focus)[^\n\u3002]*\u3002?",
        batch="Section placeholder rewrite",
    ),
    PatternSpec(
        "zh_around_capability_adds_title_candidate",
        r"\u56f4\u7ed5[^\n\u3002]{2,80}\u80fd\u529b\u8865\u5145\u300a[^\n\u3002]{6,220}\u300b[^\n\u3002]*(?:\u4f5c\u4e3a|Model \u6761\u76ee\u5019\u9009|Survey \u6761\u76ee\u5019\u9009|Bench \u6761\u76ee\u5019\u9009)[^\n\u3002]*\u3002?",
        batch="Title-signal placeholder rewrite",
    ),
    PatternSpec(
        "zh_core_around_title_generic",
        r"\u6838\u5fc3\u56f4\u7ed5[^\n\u3002]{6,220}\u3002?",
        batch="Title-signal placeholder rewrite",
    ),
)


COMPILED_PATTERNS = tuple((spec, re.compile(spec.regex, spec.flags)) for spec in PATTERNS)
BULLET_RE = re.compile(r"^-\s+\[([^\]]+)\]\([^)]+\)(?::|\uff1a)\s*(.*)$")


def repo_relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def default_docs_files() -> list[Path]:
    if default_markdown_files is not None:
        return [
            path
            for path in default_markdown_files(Path.cwd(), include_readme=False)
            if "/docs/en/" in f"/{path.as_posix()}" or "/docs/zh/" in f"/{path.as_posix()}"
        ]
    files: list[Path] = []
    for doc_root in ("docs/en", "docs/zh"):
        files.extend(sorted((Path.cwd() / doc_root).rglob("*.md")))
    return unique_files(files)


def unique_files(paths: list[Path]) -> list[Path]:
    seen: set[Path] = set()
    result: list[Path] = []
    for path in paths:
        if not path.is_file():
            continue
        key = path.resolve()
        if key in seen:
            continue
        seen.add(key)
        result.append(path)
    return sorted(result, key=lambda item: repo_relative(item))


def expand_paths(args: list[str]) -> list[Path]:
    if not args:
        return default_docs_files()
    paths: list[Path] = []
    for item in args:
        matches = [Path(match) for match in glob.glob(item, recursive=True)]
        if not matches:
            matches = [Path(item)]
        for match in matches:
            if match.is_dir():
                paths.extend(sorted(match.rglob("*.md")))
            elif match.is_file():
                paths.append(match)
    return unique_files(paths)


def language_for(path: Path) -> str:
    path_text = f"/{path.as_posix()}"
    if "/docs/en/" in path_text:
        return "en"
    if "/docs/zh/" in path_text:
        return "zh"
    return "unknown"


def clean_line(line: str) -> str:
    return line.rstrip("\n")


def normalize_title_text(text: str) -> str:
    text = text.strip()
    if text.startswith("\u300a") and "\u300b" in text[:160]:
        text = text[1 : text.index("\u300b")] + text[text.index("\u300b") + 1 :]
    text = re.sub(r"^[\"'`]+|[\"'`]+$", "", text)
    text = text.lower()
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[\W_]+", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()


def title_repeated_pattern(line: str, lang: str) -> str | None:
    match = BULLET_RE.match(line)
    if not match:
        return None
    title = normalize_title_text(match.group(1))
    summary = normalize_title_text(match.group(2)[:240])
    if len(title) >= 12 and summary.startswith(title):
        if lang == "zh":
            return "zh_title_repeated_after_colon"
        return "en_title_repeated_after_colon"
    return None


def pattern_allowed_for_path(spec: PatternSpec, path: Path) -> bool:
    """Keep section-specific placeholder families from firing in unrelated docs."""
    return spec.section is None or path.name == spec.section


def section_batch(path: Path, pattern_names: list[str]) -> str:
    section = path.name
    if section in BATCH_BY_SECTION:
        return BATCH_BY_SECTION[section]
    if pattern_names:
        first = pattern_names[0]
        for spec in PATTERNS:
            if spec.name == first:
                return spec.batch
    return "Manual review"


def scan_file(path: Path) -> list[dict[str, Any]]:
    lang = language_for(path)
    text = path.read_text(encoding="utf-8")
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        patterns = [
            spec.name
            for spec, regex in COMPILED_PATTERNS
            if pattern_allowed_for_path(spec, path) and regex.search(line)
        ]
        repeated = title_repeated_pattern(line, lang)
        if repeated:
            patterns.append(repeated)
        if not patterns:
            continue
        rows.append(
            {
                "path": repo_relative(path),
                "line": line_number,
                "lang": lang,
                "section": path.name,
                "patterns": sorted(set(patterns)),
                "batch": section_batch(path, patterns),
                "text": clean_line(line),
            }
        )
    return rows


def top_files(matches: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    counts = Counter(match["path"] for match in matches)
    result: list[dict[str, Any]] = []
    for path, count in counts.most_common(limit):
        section = Path(path).name
        result.append(
            {
                "path": path,
                "matches": count,
                "section": section,
                "batch": BATCH_BY_SECTION.get(section, "Manual review"),
            }
        )
    return result


def representative_examples(matches: list[dict[str, Any]], max_examples: int) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for match in matches:
        for pattern in match["patterns"]:
            if len(grouped[pattern]) >= max_examples:
                continue
            grouped[pattern].append(
                {
                    "path": match["path"],
                    "line": match["line"],
                    "text": match["text"],
                }
            )
    return dict(sorted(grouped.items()))


TITLE_REPEAT_PATTERNS = {"en_title_repeated_after_colon", "zh_title_repeated_after_colon"}


def is_format_only(match: dict[str, Any]) -> bool:
    return all(pattern in TITLE_REPEAT_PATTERNS for pattern in match["patterns"])


def pair_key(path: str) -> str:
    return re.sub(r"^docs/(en|zh)/", "docs/<lang>/", path)


def pair_summary(matches: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "matches": 0,
            "semantic": 0,
            "format_only": 0,
            "title_repeat_any": 0,
            "en": 0,
            "zh": 0,
            "section": "",
            "batch": "Manual review",
        }
    )
    for match in matches:
        key = pair_key(match["path"])
        row = grouped[key]
        row["matches"] += 1
        row["section"] = match["section"]
        row["batch"] = BATCH_BY_SECTION.get(match["section"], match["batch"])
        if is_format_only(match):
            row["format_only"] += 1
        else:
            row["semantic"] += 1
        if any(pattern in TITLE_REPEAT_PATTERNS for pattern in match["patterns"]):
            row["title_repeat_any"] += 1
        if match["lang"] in ("en", "zh"):
            row[match["lang"]] += 1
    rows = [
        {"pair": key, **value}
        for key, value in grouped.items()
    ]
    return sorted(rows, key=lambda row: (row["semantic"], row["matches"]), reverse=True)[:limit]


def build_report(
    files: list[Path],
    matches: list[dict[str, Any]],
    max_examples: int,
    top_limit: int,
    scope_inputs: list[str],
) -> dict[str, Any]:
    matches_by_language = Counter(match["lang"] for match in matches)
    matches_by_section = Counter(match["section"] for match in matches)
    matches_by_pattern: Counter[str] = Counter()
    for match in matches:
        matches_by_pattern.update(match["patterns"])
    semantic_matches = [match for match in matches if not is_format_only(match)]
    format_only_matches = [match for match in matches if is_format_only(match)]
    scope_paths = scope_inputs if scope_inputs else ["docs/en/**/*.md", "docs/zh/**/*.md"]
    return {
        "scope": {
            "paths": scope_paths,
            "files_scanned": len(files),
        },
        "patterns_used": {spec.name: spec.regex for spec in PATTERNS}
        | {
            "en_title_repeated_after_colon": "Markdown bullet parser: title after '- [Title](URL):' repeats at the start of the summary.",
            "zh_title_repeated_after_colon": "Markdown bullet parser: title after '- [Title](URL):' or full-width colon repeats at the start of the summary.",
        },
        "summary": {
            "total_matching_lines": len(matches),
            "semantic_template_lines": len(semantic_matches),
            "format_only_title_repetition_lines": len(format_only_matches),
            "files_with_matches": len({match["path"] for match in matches}),
            "matches_by_language": dict(sorted(matches_by_language.items())),
            "matches_by_section_file": dict(sorted(matches_by_section.items())),
            "matches_by_pattern": dict(matches_by_pattern.most_common()),
            "recommended_cleanup_batches": dict(Counter(match["batch"] for match in matches).most_common()),
        },
        "top_files_by_match_count": top_files(matches, top_limit),
        "top_pairs_by_semantic_count": pair_summary(matches, top_limit),
        "representative_examples_by_phrase": representative_examples(matches, max_examples),
        "matches": matches,
    }


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    widths = [max(len(row[index]) for row in rows) for index in range(len(rows[0]))]
    lines = []
    for row_index, row in enumerate(rows):
        lines.append("| " + " | ".join(value.ljust(widths[index]) for index, value in enumerate(row)) + " |")
        if row_index == 0:
            lines.append("| " + " | ".join("-" * widths[index] for index in range(len(row))) + " |")
    return "\n".join(lines)


def render_markdown(report: dict[str, Any], *, max_matches: int) -> str:
    summary = report["summary"]
    scope_text = ", ".join(f"`{item}`" for item in report["scope"]["paths"])
    lines = [
        "# Generic TLDR Audit",
        "",
        f"Scope: {scope_text}. Official docs were not modified.",
        "",
        "## Summary",
        "",
        f"- Files scanned: {report['scope']['files_scanned']}",
        f"- Files with matches: {summary['files_with_matches']}",
        f"- Matching lines: {summary['total_matching_lines']}",
        f"- Semantic/template lines requiring review: {summary['semantic_template_lines']}",
        f"- Format-only title repetitions: {summary['format_only_title_repetition_lines']}",
        f"- English matching lines: {summary['matches_by_language'].get('en', 0)}",
        f"- Chinese matching lines: {summary['matches_by_language'].get('zh', 0)}",
        "",
        "## Regex / Patterns Used",
        "",
    ]
    for name, regex in report["patterns_used"].items():
        lines.append(f"- `{name}`: `{regex}`")

    lines.extend(["", "## Top Files By Match Count", ""])
    rows = [["Rank", "Matches", "File", "Cleanup batch"]]
    for index, item in enumerate(report["top_files_by_match_count"], start=1):
        rows.append([str(index), str(item["matches"]), f"`{item['path']}`", item["batch"]])
    lines.append(markdown_table(rows) if len(rows) > 1 else "No matches.")

    lines.extend(["", "## Top EN/ZH Pairs By Semantic Match Count", ""])
    pair_rows = [["Rank", "Semantic", "Total", "Format-only", "EN", "ZH", "Pair", "Cleanup batch"]]
    for index, item in enumerate(report["top_pairs_by_semantic_count"], start=1):
        pair_rows.append(
            [
                str(index),
                str(item["semantic"]),
                str(item["matches"]),
                str(item["format_only"]),
                str(item["en"]),
                str(item["zh"]),
                f"`{item['pair']}`",
                item["batch"],
            ]
        )
    lines.append(markdown_table(pair_rows) if len(pair_rows) > 1 else "No matches.")

    lines.extend(["", "## Representative Line Examples Grouped By Phrase", ""])
    examples = report["representative_examples_by_phrase"]
    if not examples:
        lines.append("No matches.")
    for pattern, items in examples.items():
        count = summary["matches_by_pattern"].get(pattern, 0)
        lines.extend([f"### `{pattern}` ({count} matched lines)", ""])
        for item in items:
            lines.append(f"- `{item['path']}:{item['line']}` {item['text']}")
        lines.append("")

    lines.extend(["## All Matches", ""])
    if not report["matches"]:
        lines.append("No matches.")
    else:
        for match in report["matches"][:max_matches]:
            pattern_text = ", ".join(match["patterns"])
            lines.append(f"- `{match['path']}:{match['line']}` [{pattern_text}] {match['text']}")
        remaining = len(report["matches"]) - max_matches
        if remaining > 0:
            lines.append(f"- ... {remaining} additional matches omitted from Markdown output. Use JSON for the full list.")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Optional Markdown files, directories, or glob patterns. Defaults to docs/en and docs/zh.")
    parser.add_argument("--out", type=Path, help="Write the Markdown report to this path. Otherwise print it to stdout.")
    parser.add_argument("--json-out", type=Path, help="Write the full JSON report to this path.")
    parser.add_argument("--max-examples", type=int, default=6, help="Representative examples per pattern in Markdown and JSON.")
    parser.add_argument("--max-matches", type=int, default=500, help="Maximum detailed matches included in Markdown output.")
    parser.add_argument("--top", type=int, default=25, help="Number of top matching files to show.")
    parser.add_argument("--fail-on-match", action="store_true", help="Exit with status 1 if any generic TLDR lines are found.")
    args = parser.parse_args()

    files = expand_paths(args.paths)
    matches: list[dict[str, Any]] = []
    for path in files:
        matches.extend(scan_file(path))

    report = build_report(files, matches, args.max_examples, args.top, args.paths)
    markdown = render_markdown(report, max_matches=args.max_matches)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(markdown, encoding="utf-8")
    else:
        print(markdown, end="")
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 1 if args.fail_on_match and matches else 0


if __name__ == "__main__":
    raise SystemExit(main())
