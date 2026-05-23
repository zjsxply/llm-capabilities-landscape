# 0.2 读 Harness 时重点看什么

> 上级章节：0. Harness 与 Skill Creator


- `工作流分解`：是单代理长链路，还是 `localize -> repair -> validate`、`search -> verify -> write` 这类显式阶段化流程。
- `环境接口`：它接的是 `CLI`、`browser-native action space`、`GUI abstraction`、`MCP`，还是 `Lean / Python / executor` 这类可验证工具。
- `上下文工程`：是否有 `memory bank`、`persistent notes`、`context pruning`、`summarization`、`retrieval routing`。
- `验证闭环`：是否有 `critic`、`judge`、`schema checker`、`self-check`、`rollback`、`checkpoint`。
- `可迁移性`：是 benchmark 私有脚本，还是可被别的任务族复用的 `runtime / scaffold / SDK / platform`。
- 受控关键词（便于把近义词归并到同一类设计点）：
  `工作流分解`（workflow/pipeline/phase/stage）、`多主体协作`（multi-agent/team/roles）、`控制流与调度`（orchestrator/FSM/DAG/scheduling）、`上下文工程`（memory/summarization/pruning/retrieval organization）、`结构化检索/导航`（RAG/graph navigation/evidence retrieval）、`工具与环境接口`（CLI/MCP/browser-native/ACI/sandbox/hooks）、`模块化平台`（SDK/platform/plugin/skill library/routing）、`搜索与 test-time scaling`（MCTS/DFS/parallel branches/replay）、`验证与恢复`（critic/self-check/rollback/checkpoint/failure recovery）。
代表性通用 harness / context engineering 参考读物与工作如下（多为可迁移工程方法论，不绑定某单一 bench）。
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)（workflow-first、tooling 与 context engineering 的工程拆解）
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)（长上下文与记忆/检索组织的工程总结）
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)（把 harness 作为长程 agent 的核心工程对象讨论）
- [The Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)（从控制流、状态、工具与 delegation 拆解 harness）
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)（产品化视角的上下文工程经验）
- [AutoHarness](https://arxiv.org/abs/2603.03329)（为 LLM agent 自动合成 code harness 的研究工作）
- [Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned](https://arxiv.org/abs/2603.05344)（终端 coding agent 的 scaffolding/harness/context engineering 系统化总结）
