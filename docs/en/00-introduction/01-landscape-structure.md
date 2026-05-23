# 0.1 Landscape Structure

> Parent chapter: 0. Introduction

This repository groups each capability topic with the same section vocabulary so entries remain comparable across domains:

- `Leaderboard`: public ranking, submission site, arena, or official results page that helps readers locate current systems and scores.
- `Survey`: review, tutorial, position, or taxonomy work that maps a capability area rather than only introducing one benchmark or method.
- `Bench`: task, dataset, protocol, metric, or evaluation suite for measuring a capability.
- `Agent Harness`: model-external execution logic such as workflow orchestration, tool use, memory, environment interaction, verification, rollback, search, or multi-agent collaboration.
- `Skill`: reusable agent capability packages, skill runtimes, skill benchmarks, skill creation tools, skill selection, portability, or safety infrastructure.

`Agent Harness` is separated from model-side work by asking where the main reusable contribution lives. If the gain mostly comes from new training data, pretraining, fine-tuning, reinforcement learning, model architecture, or reward design, classify it as model-side work in the relevant capability page rather than as an Agent Harness. If the gain comes from how an existing or replaceable model is wrapped into an executable loop, connected to tools or environments, given memory, verified, scheduled, or recovered after failure, classify it as Agent Harness.

## 0.1.1 What Is a Harness

- A `Harness` is a task runtime outside the model.
  It usually handles `task decomposition`, `tool wiring`, `context organization`, `environment execution`, `search/backtracking`, and `verification and recovery`, so the same base model can often be reused across multiple benchmarks.
- A `Harness` is not a training algorithm.
  Training answers "what the model has learned"; a harness answers "how the system turns capability into a stable executable workflow."
- To avoid mixing "training" and "harness", start with a three-way split when reading papers:
  `model training algorithms` (gains mainly come from parameter updates or training data/objectives), `external harnesses` (gains mainly come from task decomposition, control flow, context/memory, tool and environment interfaces, search and verification loops), and `hybrid work` (both are present).
- When reading an agent paper, first identify where the gain comes from.
  If it mainly comes from `SFT / RL / data scaling / pretraining`, it is model work; if it mainly comes from `planner-executor`, `tool loop`, `memory`, `validator`, `DAG/FSM`, or `skill library`, it is closer to harness work.

## 0.1.2 What to Look for When Reading Harnesses

- `Workflow decomposition`: whether it is a single-agent long chain or an explicit staged workflow such as `localize -> repair -> validate` or `search -> verify -> write`.
- `Environment interface`: whether it connects to `CLI`, `browser-native action space`, `GUI abstraction`, `MCP`, or verifiable tools such as `Lean / Python / executor`.
- `Context engineering`: whether it has a `memory bank`, `persistent notes`, `context pruning`, `summarization`, or `retrieval routing`.
- `Verification loop`: whether it has a `critic`, `judge`, `schema checker`, `self-check`, `rollback`, or `checkpoint`.
- `Transferability`: whether it is a benchmark-specific script or a `runtime / scaffold / SDK / platform` reusable by other task families.
- Controlled keywords, useful for grouping near-synonyms under the same design point:
  `workflow decomposition` (workflow/pipeline/phase/stage), `multi-agent collaboration` (multi-agent/team/roles), `control flow and scheduling` (orchestrator/FSM/DAG/scheduling), `context engineering` (memory/summarization/pruning/retrieval organization), `structured retrieval/navigation` (RAG/graph navigation/evidence retrieval), `tool and environment interfaces` (CLI/MCP/browser-native/ACI/sandbox/hooks), `modular platform` (SDK/platform/plugin/skill library/routing), `search and test-time scaling` (MCTS/DFS/parallel branches/replay), and `verification and recovery` (critic/self-check/rollback/checkpoint/failure recovery).
Representative general-purpose harness and context-engineering references include the following. Most are transferable engineering methods rather than work tied to a single benchmark.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (engineering decomposition of workflow-first design, tooling, and context engineering)
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (engineering summary of long context, memory, and retrieval organization)
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (discusses harnesses as the core engineering object for long-running agents)
- [The Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) (decomposes harnesses through control flow, state, tools, and delegation)
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) (context-engineering lessons from a product perspective)
- [AutoHarness](https://arxiv.org/abs/2603.03329) (research on automatically synthesizing code harnesses for LLM agents)
- [Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned](https://arxiv.org/abs/2603.05344) (systematic summary of scaffolding, harnesses, and context engineering for terminal coding agents)
