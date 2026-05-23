# 1.11.4 Agent Harness

- [ReAct](https://arxiv.org/abs/2210.03629)（[开源代码](https://github.com/ysymyth/ReAct)）是工具调用最常见的通用 agent loop 基线：`reasoning -> action -> observation`。在 τ2-Bench、VitaBench 这类“多步工具链”任务上，核心差异更多来自 runtime（参数校验、重试、回退、状态管理）而非专用 solver。
- [ToolLLM](https://arxiv.org/abs/2307.16789)（[开源代码](https://github.com/OpenBMB/ToolBench)）：在大规模真实 API 集合上执行工具检索、参数对齐与多步调用，是 tool-use solver agent 的代表性实现。
- [Factored Agents](https://arxiv.org/abs/2503.22931)：面向工具使用的 agent 架构，将高层规划与 in-context learning 同工具格式记忆拆开。核心思想：用专门组件减少格式错误、字段缺失和 API 字段幻觉，同时保留动态环境中的适应性。
- [AgentDNS](https://arxiv.org/abs/2505.22368)：面向 LLM agent 的服务发现与命名协议。核心思想：为 agent 提供 root-domain 机制，用于跨厂商发现、解析并安全调用第三方 agent 和工具，补足 MCP 与 A2A 周边的互操作缺口。
- [Gradientsys](https://arxiv.org/abs/2507.06520)：带有 ReAct 式编排的多智能体 LLM 调度器。核心思想：通过调度与反馈协调专门化 agent，使多步骤工具或 workflow 执行被显式管理，而不是交给单一大 prompt。
- [MCP-Universe](https://arxiv.org/abs/2508.14704)（[开源代码](https://github.com/SalesforceAIResearch/MCP-Universe)）：更像工具生态层的 agent harness，不只是 benchmark 数据集；它把 MCP server、任务、执行器、UI 和评测记录组织到同一运行环境，适合复现实验和对比不同 tool-use scaffold。
- [ToolGate](https://arxiv.org/abs/2601.04688)：面向 LLM 工具使用的契约约束与可验证执行 harness；核心思想是用符号状态表示可信世界信息，并通过 Hoare-style contracts 决定工具结果是否可提交，从而给工具调用提供可检查的安全与状态演化保证。
- mcp-use（[开源代码](https://github.com/mcp-use/mcp-use)；[文档](https://mcp-use.com/docs)）：无独立论文，但提供 MCP server、MCP app、Inspector 和部署链路，适合作为工程侧 MCP tool-use harness，特别是把工具定义、调试、观测和发布合在一个 SDK 中。
- mcp-agent（[开源代码](https://github.com/lastmile-ai/mcp-agent)；[文档](https://docs.mcp-agent.com/)）：MCP-native agent SDK，把 server 生命周期管理、路由、orchestrator/evaluator-optimizer 模式和 durable execution 做成可复用的工具使用 harness 组件。
- OpenAI Agents SDK（[开源代码](https://github.com/openai/openai-agents-python)；[文档](https://openai.github.io/openai-agents-python/)）：开源 workflow SDK，核心抽象包含 tools、MCP、handoffs、guardrails、sessions 和 tracing，可作为工程化 tool-using agents 的实用基线，而不只是 benchmark scaffold。
- [ATLAS-RTC](https://arxiv.org/abs/2603.27905)：面向 LLM 智能体输出的 token 级运行时控制层。核心思想：在解码过程中依据输出合约监测生成，并在结构化输出或工具调用格式出错前施加偏置、掩码或回滚。
- [Meta-Agent-Workflow](https://doi.org/10.1145/3701716.3715247)：面向工具使用的 agent harness，通过构造、检索和细化可复用 workflow 来支持 LLM agent。核心思想：把反复出现的工具调用轨迹沉淀成 workflow 资产，让后续任务复用并调整结构化执行计划，而不是每次从一次性 ReAct 循环开始。
- [SkillGraph](https://arxiv.org/abs/2604.19793)：面向工具序列推荐的图先验框架；核心思想是从成功工具调用轨迹中挖掘执行转移规律，并把候选检索与排序拆开，使 agent 能规划数据依赖的 API 链路，而不是只依赖语义相似度。
- [DADL](https://arxiv.org/abs/2605.05247)：面向企业工具库的 LLM 智能体声明式描述语言。核心思想：一次性描述 REST API、认证、分页、响应裁剪和访问分类，再由执行层暴露大规模工具目录，而不是为每个包装器部署一个 MCP server。
- [Planning Horizon in Data-Centric Tool Calling](https://arxiv.org/abs/2605.08477)：研究面向数据任务的工具调用 agent 是否需要显式逐步规划；核心思想是在工具调用流程中比较不同规划跨度，帮助 agent scaffold 判断细粒度分解何时有益、何时反而影响执行。
- [RubricRefine](https://arxiv.org/abs/2605.09730)：训练前的工具调用可靠性修复层；核心思想：先生成任务/注册表特定 rubric，再在执行前修正 inter-tool contract 错误。
- [AOP](https://www.semanticscholar.org/paper/2dccab11b1feb5424437a79f047c8a91c1818634)：面向复杂查询回答的自动化、交互式 LLM pipeline 编排 harness；核心思想是让系统组合、检查并修订多步 LLM pipeline，而不是把复杂查询压成单个 prompt 或固定流程。
- [Toolbelt-MCP](https://doi.org/10.1007/978-3-032-11442-6_38)：面向关系数据库工具使用的 MCP proof-of-concept harness。核心思想：把 SQL 执行与基于图的表关系路径发现封装为工具，使 LLM 能通过 MCP 动作探索复杂数据库 schema 并回答数据问题。
