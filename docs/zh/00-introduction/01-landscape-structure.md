# 0.1 内容结构

> 上级章节：0. 引言

本仓库在每个能力主题下尽量使用同一套小节词表，方便跨方向比较：

- `Leaderboard`：公开榜单、提交站点、arena 或官方结果页，用来定位当前系统和分数。
- `Survey`：综述、教程、立场论文或 taxonomy 工作，重点是梳理一个能力方向，而不是只提出单个 benchmark 或方法。
- `Bench`：用于衡量某项能力的任务、数据集、协议、指标或评测套件。
- `Agent Harness`：模型外部的执行逻辑，例如 workflow 编排、工具调用、记忆、环境交互、验证、回滚、搜索或多 Agent 协作。
- `Skill`：可复用的 agent 能力包、skill runtime、skill benchmark、skill 创建工具、skill 选择、可移植性或安全基础设施。

区分 `Agent Harness` 与模型侧工作时，先看主要可复用贡献在哪里。如果增益主要来自新训练数据、预训练、微调、强化学习、模型结构或奖励设计，它更应归入相应能力页中的模型侧工作，而不是 Agent Harness。如果增益来自把一个现有或可替换模型包装成可执行闭环、接入工具或环境、配置记忆、验证、调度，或在失败后恢复，那么它更接近 Agent Harness。

## 0.1.1 什么是 Harness

- `Harness` 是模型外的任务运行时。
  它通常负责 `任务拆解`、`工具接线`、`上下文组织`、`环境执行`、`搜索/回溯`、`验证与恢复`，因此同一个底模常能复用到多个 benchmark。
- `Harness` 不等于训练算法。
  训练回答“模型学到了什么”，harness 回答“系统怎样把能力稳定变成可执行工作流”。
- 为避免把“训练”与“harness”混在一起，读论文时可先做三分法：
  `模型训练算法`（主要增益来自参数更新或训练数据/目标）、`外围 harness`（主要增益来自任务拆解、控制流、上下文/记忆、工具与环境接口、搜索与验证回路）、`混合型工作`（两者皆有）。
- 读一篇 agent 论文时，先看增益来自哪里。
  如果主要增益来自 `SFT / RL / data scaling / pretraining`，那是模型工作；如果主要增益来自 `planner-executor`、`tool loop`、`memory`、`validator`、`DAG/FSM`、`skill library`，那更接近 harness 工作。

## 0.1.2 读 Harness 时重点看什么

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
