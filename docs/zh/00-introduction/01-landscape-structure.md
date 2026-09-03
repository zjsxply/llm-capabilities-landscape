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

- [Putting It All into Context: Simplifying Agents with LCLMs](https://arxiv.org/abs/2505.08120)：研究长上下文模型能否简化 agent 架构。核心思想是判断检索工具、多代理 scaffold 和手工编排何时仍然必要，何时可由上下文本身替代。
- [Pel, A Programming Language for Orchestrating AI Agents](https://arxiv.org/abs/2505.13453)：用于编排 AI agent 的编程语言；核心思想是把 agent 控制流、工具调用和协作显式为可编程构造，而不是零散 prompt。
- [HAWK: A Hierarchical Workflow Framework for Multi-Agent Collaboration](https://arxiv.org/abs/2507.04067)：面向多代理协作的分层 workflow 框架。核心思想是标准化接口、调度和状态共享，使异构代理更可靠地协作。
- [Exploring Agentic Artificial Intelligence Systems: Towards a Typological Framework](https://arxiv.org/abs/2508.00844)：可作为通用 agent harness的 Survey 候选：围绕 Exploring Agentic Artificial Intelligence Systems: Towards a Typological Framework 梳理背景、方法与开放问题。
- [Polymath: A Self-Optimizing Agent with Dynamic Hierarchical Workflow](https://arxiv.org/abs/2508.02959)：补充introduction方向的相关条目，核心围绕《Polymath: A Self-Optimizing Agent with Dynamic Hierarchical Workflow》。
- [LumiMAS: A Comprehensive Framework for Real-Time Monitoring and Enhanced Observability in Multi-Agent Systems](https://arxiv.org/abs/2508.12412)：面向多 agent 系统的监控与可观测性框架；核心思想是暴露实时 agent 状态、交互轨迹和诊断信号，便于检查与调试多 agent 工作流。
- [Prompt Orchestration Markup Language](https://arxiv.org/abs/2508.13948)：Agent Harness 条目；核心思想：用于 prompt orchestration 的标记语言，帮助把复杂 prompt 工作流显式化。
- [AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications](https://arxiv.org/abs/2508.16279)：可作为通用 agent harness的 Agent Harness 候选：围绕 AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications 提供可复用的 agent 工作流、编排、运行时或协议设计。
- [Symphony: A Decentralized Multi-Agent Framework for Scalable Collective Intelligence](https://arxiv.org/abs/2508.20019)：面向可扩展 collective intelligence 的去中心化多代理框架。核心思想是在没有单一中心控制器的情况下协调代理，强调分布式编排和通信设计。
- [XAgents: A Unified Framework for Multi-Agent Cooperation via IF-THEN Rules and Multipolar Task Processing Graph](https://arxiv.org/abs/2509.10054)：基于 IF-THEN rules 与 multipolar task-processing graph 的多 agent 协作框架；核心思想是显式化规划与执行依赖，让复杂任务能更可靠地在多个 agent 间路由。
- [AgentHub: A Registry for Discoverable, Verifiable, and Reproducible AI Agents](https://arxiv.org/abs/2510.03495)：面向可发现、可验证、可复现 AI agent 的 registry layer；核心思想是用规范 manifest、证据记录和生命周期日志支持 agent 复用与治理。
- [Open Agent Specification (Agent Spec): A Unified Representation for AI Agents](https://arxiv.org/abs/2510.04173)：AI agents 与 workflows 的统一声明式表示；核心思想是跨框架标准化 agent 定义、数据流语义和工具集成。
- [DMAS-Forge: A Framework for Transparent Deployment of AI Applications as Distributed Systems](https://arxiv.org/abs/2510.11872)：把 agentic AI 应用部署为分布式系统的框架；核心思想是让多 agent 角色、工具和记忆层在接近生产的基础设施中可测试、可透明审计。
- [The Gatekeeper Knows Enough](https://arxiv.org/abs/2510.14881)：面向有状态 agent 的上下文管理 harness；核心思想是加入 gatekeeper 层判断当前所需状态，减少 autonomous workflow 中的状态不同步与无效上下文膨胀。
- [Verification-Aware Planning for Multi-Agent Systems](https://arxiv.org/abs/2510.17109)：面向多 agent 系统的 verification-aware planning framework；核心思想是分解任务、编码子任务依赖，并为每个子任务附上 planner-defined verification functions，以提升交接和鲁棒性。
- [Socialized Learning and Emergent Behaviors in Multi-Agent Systems based on Multimodal Large Language Models](https://arxiv.org/abs/2510.18515)：可作为Agent 系统基础方向的外部工作流、编排、记忆或执行贡献候选；其主题直接落在该能力页范围内，归入 `Agent Harness` 轨道。
- [FlowMesh: A Service Fabric for Composable LLM Workflows](https://arxiv.org/abs/2510.26913)：面向可组合 LLM workflow 的 service fabric；核心思想是把包括 agent 交互在内的细粒度工作流阶段作为共享多租户基础设施执行和优化。
- [A2Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators](https://arxiv.org/abs/2511.20693)：补充introduction方向的相关条目，核心围绕《A2Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators》。
- [BAMAS: Structuring Budget-Aware Multi-Agent Systems](https://arxiv.org/abs/2511.21572)：预算感知的多 agent 系统设计框架；核心思想是在显式成本预算下组织协作，使多 agent harness 能有意识地权衡准确率、探索和开销。
- [An Empirical Study of Agent Developer Practices in AI Agent Frameworks](https://arxiv.org/abs/2512.01939)：关于 AI agent framework 开发者实践的实证研究。核心思想是分析框架抽象、编排组件和开发流程如何塑造真实 agent 实现。
- [VET Your Agent: Towards Host-Independent Autonomy via Verifiable Execution Traces](https://arxiv.org/abs/2512.15892)：通过 verifiable execution traces 支撑 host-independent autonomy 的 harness 方向；核心思想是记录可检查轨迹，让 agent 行为跨宿主环境可迁移、可审计。
- [LEAP & LEAN: Look-ahead Planning and Agile Navigation for LLM Agents](https://doi.org/10.18653/v1/2025.acl-industry.64)：面向 LLM agent 的前瞻规划与敏捷导航 harness；核心思想是分离未来状态规划和动作导航，使 agent 能在执行停滞前修正路线。
- [Towards a Graph-Based Agentic Workflow and Framework for Natural Language Directions](https://doi.org/10.1109/bigdata66926.2025.11401766)：可作为通用 agent harness的 Agent Harness 候选：围绕 Towards a Graph-Based Agentic Workflow and Framework for Natural Language Directions 提供可复用的 agent 工作流、编排、运行时或协议设计。
- [An Accountability-Based Architectural Tactic for Agent Cooperation in LLM-Based Multi-Agent Systems](https://doi.org/10.1109/bigdata66926.2025.11402340)：可作为通用 agent harness的 Agent Harness 候选：围绕 An Accountability-Based Architectural Tactic for Agent Cooperation in LLM-Based Multi-Agent Systems 提供可复用的 agent 工作流、编排、运行时或协议设计。
- [AgentDevel: Reframing Self-Evolving LLM Agents as Release Engineering](https://arxiv.org/abs/2601.04620)：把自进化 agent 重构为 release engineering harness。核心思想是用版本、审计和非回归检查管理 agent 改进，而不是依赖不透明的自修改循环。
- [Orchestrating Intelligence: Confidence-Aware Routing for Efficient Multi-Agent Collaboration across Multi-Scale Models](https://arxiv.org/abs/2601.04861)：面向多尺度模型协作的 confidence-aware routing harness。核心思想是按推理阶段的认知需求，把任务分配给不同规模的模型。
- [JudgeFlow: Agentic Workflow Optimization via Block Judge](https://arxiv.org/abs/2601.07477)：补充introduction方向的相关条目，核心围绕《JudgeFlow: Agentic Workflow Optimization via Block Judge》。
- [Adaptive Orchestration: Scalable Self-Evolving Multi-Agent Systems](https://arxiv.org/abs/2601.09742)：面向可扩展自演化多 agent 系统的编排框架；核心思想是在任务执行中动态调整角色、协作和工作流结构。
- [CASTER: Breaking the Cost-Performance Barrier in Multi-Agent Orchestration via Context-Aware Strategy for Task Efficient Routing](https://arxiv.org/abs/2601.19793)：面向多 agent 编排的上下文感知策略路由框架；核心思想是按任务上下文选择 agent 策略，改善成本与性能权衡。
- [Epistemic Context Learning](https://arxiv.org/abs/2601.21742)：面向 LLM-based multi-agent systems 的信任建模方法。核心思想：让 agent 评估同伴可靠性，而不是盲目服从其他 agent，从而缓解协作 harness 中的 sycophancy 和鲁棒性失败。
- [TodyComm: Task-Oriented Dynamic Communication for Multi-Round LLM-based Multi-Agent System](https://arxiv.org/abs/2602.03688)：面向多轮 LLM 多 agent 系统的任务导向动态通信机制；核心思想是随任务进展调整 agent 间通信内容。
- [Agent Primitives: Reusable Latent Building Blocks for Multi-Agent Systems](https://arxiv.org/abs/2602.03695)：定义多 agent 系统的可复用潜在构件。核心思想：通过组合可复用 primitives 减少任务特定角色与 prompt 工程。
- [Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents](https://arxiv.org/abs/2602.12662)：让 LLM agent 按步骤自适应认知深度。核心思想：在长程任务中按步骤调整推理深度，而不是每一步使用固定思考模式。
- [Guided Collaboration in Heterogeneous LLM-Based Multi-Agent Systems via Entropy-Based Understanding Assessment and Experience Retrieval](https://arxiv.org/abs/2602.13639)：用理解度评估和经验检索引导异构 LLM 多 agent 协作；核心思想是监控 agent 对任务的理解并复用既往协作经验。
- [PseudoAct](https://arxiv.org/abs/2602.23668)：通过 pseudocode synthesis 支撑 LLM agent planning 与 action control 的 harness。核心思想：把高层意图转成更灵活的程序化控制结构，减少长任务中纯反应式工具调用带来的冗余。
- [AI Runtime Infrastructure](https://arxiv.org/abs/2603.00495)：位于模型之上、应用之下的 execution-time layer。核心思想：在 agent 运行过程中观察、推理并干预执行，以优化成功率、延迟、token 效率、可靠性和安全性。
- [Turn: A Language for Agentic Computation](https://arxiv.org/abs/2603.08755)：Agent Harness 条目；核心思想：面向 agentic computation 的编译型 actor 语言；核心思想是把推理调用、schema、上下文边界和 policy 变成一等编程构件。
- [Language Model Teams as Distributed Systems](https://arxiv.org/abs/2603.12229)：从分布式系统角度理解 LLM teams。核心思想：分析什么情况下组队有用、通信应如何组织，以及协调和可靠性失败从何而来，适合作为多 agent harness 的通用参考。
- [Orla: A Library for Serving LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2603.13605)：面向 LLM-based multi-agent systems 的 serving library。核心思想：把 agent workflow requests、LLM serving、工具执行和异构基础设施分离，使多 agent 系统能运行在可复用 runtime layer 上。
- [IEMAS: An Incentive-Efficiency Routing Framework for Open Agentic Web Ecosystems](https://arxiv.org/abs/2603.17302)：面向开放 agentic web 生态的激励高效路由框架；核心思想是在开放 agent 网络中同时考虑任务路由、激励与效率。
- [Heddle: A Distributed Orchestration System for Agentic RL Rollout](https://arxiv.org/abs/2603.28101)：面向 agentic RL rollout 的分布式编排系统；核心思想是把 agent 环境执行、调度和 rollout 管理做成可复用的训练与评测基础设施。
- [Holos: A Web-Scale LLM-Based Multi-Agent System for the Agentic Web](https://arxiv.org/abs/2604.02334)：补充introduction方向的相关条目，核心围绕《Holos: A Web-Scale LLM-Based Multi-Agent System for the Agentic Web》。
- [Topaz](https://arxiv.org/abs/2604.03527)：面向 agentic workflow 的可审计模型路由框架。核心思想：用可解释 rationale 为子任务选择模型，把能力与成本取舍显式化，避免 workflow 中的模型选择退化成不可见的省钱策略。
- [EvolveRouter: Co-Evolving Routing and Prompt for Multi-Agent Question Answering](https://arxiv.org/abs/2604.05149)：面向多 agent QA 的 routing harness。核心思想是同时演化路由器和参与 agent 的 prompt，使协作能按问题动态选择 agent 数量与类型。
- [Qualixar OS: A Universal Operating System for AI Agent Orchestration](https://arxiv.org/abs/2604.06392)：面向 AI agent 编排的操作系统式框架；核心思想是为 agent 工作流提供通用调度、协同和执行服务。
- [How Much Heavy Lifting Can an Agent Harness Do?: Measuring the LLM's Residual Role in a Planning Agent](https://arxiv.org/abs/2604.07236)：面向 planning agents 的 harness ablation study。核心思想：外显 planning harness 并测量 LLM 的剩余贡献，区分性能来自 workflow 设计还是模型能力。
- ["Theater of Mind"for LLMs: A Cognitive Architecture Based on Global Workspace Theory](https://arxiv.org/abs/2604.08206)：补充introduction方向的相关条目，核心围绕《"Theater of Mind"for LLMs: A Cognitive Architecture Based on Global Workspace Theory》。
- [Three Roles, One Model: Role Orchestration at Inference Time to Close the Performance Gap Between Small and Large Agents](https://arxiv.org/abs/2604.11465)：补充introduction方向的相关条目，核心围绕《Three Roles, One Model: Role Orchestration at Inference Time to Close the Performance Gap Between Small and Large Agents》。
- [Modality-Native Routing in Agent-to-Agent Networks: A Multimodal A2A Protocol Extension](https://arxiv.org/abs/2604.12213)：扩展 agent-to-agent 协议，使多模态证据能以原生模态在 agent 间传递；核心思想是避免把图像、视频等信号过早压缩成纯文本交接。
- [Credo: Declarative Control of LLM Pipelines via Beliefs and Policies](https://arxiv.org/abs/2604.14401)：Agent Harness 条目；核心思想：通过 beliefs 和 policies 声明式控制 LLM pipeline；核心思想是用显式控制规则管理有状态决策，而不是把逻辑藏在提示中。
- [Architectural Design Decisions in AI Agent Harnesses](https://arxiv.org/abs/2604.18071)：梳理 AI agent harness 架构决策的元参考；核心思想是把控制流、状态、工具和验证选择显式化为设计维度。
- [ClawNet: Human-Symbiotic Agent Network for Cross-User Autonomous Cooperation](https://arxiv.org/abs/2604.19211)：面向跨用户自治协作的人机共生 agent 网络；核心思想是把 agent 组织成可跨用户协调工作的协作网络，而不是孤立助手。
- [AgentSim: A Platform for Verifiable Agent-Trace Simulation](https://arxiv.org/abs/2604.26653)：可验证 agent trace simulation 平台；核心思想是模拟并检查 agent 轨迹，使行为可复现、可验证。
- [In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks](https://arxiv.org/abs/2604.27891)：Agent Harness 条目；核心思想：对外部 agent 编排与上下文内过程提示进行受控比较；核心思想是识别何时可用更简单的系统提示替代编排层。
- [AAFLOW: Scalable Patterns for Agentic AI Workflows](https://arxiv.org/abs/2605.02162)：面向 agentic AI workflows 的可扩展执行模式框架。核心思想：用更可复现的执行模型组织检索、推理、记忆和工作流编排，而不是依赖临时串行链路。
- [Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation](https://arxiv.org/abs/2605.05007)：补充introduction方向的相关条目，核心围绕《Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation》。
- [A Self-Healing Framework for Reliable LLM-Based Autonomous Agents](https://arxiv.org/abs/2605.06737)：补充introduction方向的相关条目，核心围绕《A Self-Healing Framework for Reliable LLM-Based Autonomous Agents》。
- [Learning Agent Routing From Early Experience](https://arxiv.org/abs/2605.07180)：补充introduction方向的相关条目，核心围绕《Learning Agent Routing From Early Experience》。
- [LLM-X: A Scalable Negotiation-Oriented Exchange for Communication Among Personal LLM Agents](https://arxiv.org/abs/2605.11376)：面向个人 LLM agent 通信的协商式交换机制；核心思想是为个人 agent 提供可扩展的协商和协调协议层。
- [A Two-Dimensional Framework for AI Agent Design Patterns: Cognitive Function and Execution Topology](https://arxiv.org/abs/2605.13850)：Agent Harness 条目；核心思想：按认知功能和执行拓扑划分 agent design patterns；核心思想是区分单轴 taxonomy 下看似相同的架构。
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
- [A Closed-Loop Modular Language Agent with Step Verification and Local Correction for Multi-Step Task Solving](https://doi.org/10.3390/electronics15102011)：补充introduction方向的相关条目，核心围绕《A Closed-Loop Modular Language Agent with Step Verification and Local Correction for Multi-Step Task Solving》。
- [Beyond Prompt Chaining: The TB-CSPN Architecture for Agentic AI](https://doi.org/10.3390/fi17080363)：可作为通用 agent harness的 Agent Harness 候选：围绕 Beyond Prompt Chaining: The TB-CSPN Architecture for Agentic AI 提供可复用的 agent 工作流、编排、运行时或协议设计。
