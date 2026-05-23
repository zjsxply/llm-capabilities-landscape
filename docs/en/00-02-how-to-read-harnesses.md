# 0.2 What to Look for When Reading Harnesses

> Parent chapter: 0. Harness and Skill Creator


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
