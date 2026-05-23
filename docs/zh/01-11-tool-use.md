# 1.11 工具调用

> 上级章节：1. 基础能力

## 1.11.1 Leaderboard

- [BFCL / Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)：持续榜单，适合作为纯 function calling 的主参考。
  它重点隔离工具选择、参数填充、schema 遵循和多轮调用准确性，因此更适合比较模型/agent 的结构化调用能力，而不是完整软件工程执行能力。
- [τ-bench / τ²-Bench](https://www.taubench.com/)（[τ²-Bench 提交说明](https://github.com/sierra-research/tau2-bench/blob/main/docs/leaderboard-submission.md)）：面向带状态 API 的多轮工具使用榜单/提交流程。
  它的价值在于把客服、业务规则、数据库状态和工具返回串成可执行任务，适合筛选能处理真实 API orchestration 的 agent scaffold。
- [Tool Decathlon（Toolathlon）](https://toolathlon.xyz/)：面向跨应用、多工具、长链路任务的公开榜单。
  相比 BFCL 的函数签名预测，它更接近 MCP/真实应用工具链场景，适合观察 agent 是否能在大量工具、跨应用状态和专用检查脚本下稳定完成任务。
- [Claw-Eval-Live](https://claw-eval-live.github.io/)：持续更新的 workflow agent 榜单，覆盖终端、文件、网页、服务和 skill 相关任务。
  它不是纯 function-calling 榜单，但适合作为 tool-use、terminal-use 和 skill-use 的交叉参照，尤其适合观察 agent harness 在动态真实 workflow 上的迁移性。

## 1.11.2 Survey

- [What Are Tools Anyway? A Survey from the Language Model Perspective](https://arxiv.org/abs/2403.15452)：澄清工具、API、行动、外部资源与 skills 的边界。
- [Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935)：回顾工具发现、选择、调用、反馈、数据集与基准。
- [LLM With Tools: A Survey](https://arxiv.org/abs/2409.18807)：从系统视角梳理工具表示、规划、执行反馈与评测。
- [Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278)：回顾现代工具中间件中的 MCP 生态与安全问题。
- [The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration](https://arxiv.org/abs/2603.22862)：梳理多工具编排中的路由、组合、轨迹与协同。

## 1.11.3 Bench

- [API-Bank](https://arxiv.org/abs/2304.08244)（[开源代码](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank)）：评什么：tool-augmented LLM 的工具选择、参数填充与多步调用；核心思想：把工具集合与任务协议化，强调“可执行的调用轨迹”而非纯文本回答。
- [Gorilla](https://arxiv.org/abs/2305.15334)（[开源代码](https://github.com/ShishirPatil/gorilla)）：评什么：大规模 API 连接下的函数调用/工具调用能力；核心思想：强调“与海量 API 的对齐”和函数签名约束下的可执行调用。
- [ToolQA](https://arxiv.org/abs/2306.13304)（[开源代码](https://github.com/night-chen/ToolQA)）：评什么：通过外部工具回答问题的正确性（含多轮调用与工具返回利用）；核心思想：把“工具调用带来的信息增益”纳入评测协议，而不是只比较语言输出流畅性。
- [ToolBench](https://github.com/OpenBMB/ToolBench)（来源工作：[ToolLLM](https://arxiv.org/abs/2307.16789)）：评什么：在大规模真实 API 集合上进行工具调用与多步执行；核心思想：把“API 规模”与“可执行评测”作为压力来源，覆盖工具检索、参数对齐与执行反馈闭环。
- [BFCL / Berkeley Function-Calling Leaderboard](https://arxiv.org/abs/2409.00608)：评什么：函数调用（function calling）的准确性与鲁棒性（工具选择、参数对齐、schema 约束）。核心思想：用标准化函数签名与统一榜单，隔离“语言能力”与“调用正确性”。（[官方榜单](https://gorilla.cs.berkeley.edu/leaderboard)）
- [MTU-Bench](https://openreview.net/forum?id=6guG2OlXsr)：评什么：大语言模型的多粒度工具使用能力。核心思想：把工具使用难度拆到多个子任务粒度，避免只测单次函数选择或最终答案正确性。
- [ToolSandbox](https://aclanthology.org/2025.findings-naacl.65/)：评什么：有状态对话式工具使用。核心思想：结合用户模拟器、隐式工具状态依赖、中间里程碑和 on-policy 交互，让工具调用在变化环境中被评测，而不是只做无状态 API 调用。
- [MCP-RADAR](https://arxiv.org/abs/2505.16700)：评什么：MCP 框架下跨数学、搜索、邮件、日历、文件和终端六类任务的工具使用能力；核心思想：同时度量答案正确性、操作准确性、调用轮次和资源效率，把 MCP 从协议支持推进到可量化的执行评测。
- [τ-bench / τ²-Bench](https://arxiv.org/abs/2506.07982)：评什么：多轮工具使用与 API orchestration（选工具、填参、读返回、纠错与重试）。核心思想：把“工具链路的可执行正确性”做成可量化评测，而不是只看语言输出。
- [DICE-BENCH](https://arxiv.org/abs/2506.22853)：评什么：多轮、多方对话中的工具使用能力，尤其是函数名与参数线索分散在不同轮次和参与者时的调用正确性；核心思想：用 DICE-SCORE 度量工具相关信息分散度，再通过工具依赖图合成更贴近真实对话的 function-calling 场景。
- [ToolHop](https://aclanthology.org/2025.acl-long.150/)：评什么：围绕本地可执行工具的多跳工具使用。核心思想：用 query-driven 任务、工具依赖、执行反馈和可验证答案，测试 agent 能否跨工具链规划。
- [CONFETTI](https://aclanthology.org/2025.acl-long.394/)：评什么：turn-level interaction 中的对话式 function calling。核心思想：用人工模拟对话覆盖追问、目标修正、歧义目标和隐含约束，测试模型能否跨对话轮保持函数调用意图。
- [LiveMCPBench](https://arxiv.org/abs/2508.01780)（[项目页](https://icip-cas.github.io/LiveMCPBench)；[开源代码](https://github.com/icip-cas/LiveMCPBench)）：评什么：大规模、多 server MCP 工具空间中的检索、路由与组合。核心思想：提供 70 个 server 和 527 个工具，显式把“找得到工具”和“组合得对工具”作为 MCP agent 的主要瓶颈。
- [MCP-Universe](https://arxiv.org/abs/2508.14704)（[项目页](https://mcp-universe.github.io)；[开源代码](https://github.com/SalesforceAIResearch/MCP-Universe)）：评什么：真实 MCP servers 上的长程、多域工具使用；核心思想：用导航、仓库管理、金融分析、3D 设计、浏览器自动化和网页搜索等真实 server 组合，考察 unfamiliar tools 与长上下文压力下的执行式评分。
- [LiveMCP-101](https://arxiv.org/abs/2508.15760)：评什么：MCP-enabled agents 在真实多步查询上的压力测试与诊断。核心思想：用 101 个挑战性查询、执行计划和动态工具返回检查 MCP agent 的工具选择、调度、结果处理和失败恢复。
- [MCPVerse](https://arxiv.org/abs/2508.16260)：评什么：真实 MCP server 生态下的 agentic tool use；核心思想：用可执行的 MCP 工具集合替代静态函数签名，考察工具发现、参数绑定、状态追踪和多步恢复。
- [MCP-Bench](https://arxiv.org/abs/2508.20453)（[开源代码](https://github.com/Accenture/mcp-bench)）：评什么：复杂真实任务中的 MCP 工具调用 agent；核心思想：把 server/client 连接、调用轨迹记录与任务评分流程做成可复现 benchmark-side harness。
- [MCP-AgentBench](https://arxiv.org/abs/2509.09734)：评什么：MCP-mediated tools 下真实语言 agent 的任务表现；核心思想：把 MCP 作为工具中间层，检验 agent 对工具说明、返回值、环境状态和多轮计划的统一处理能力。
- [MCPMark](https://arxiv.org/abs/2509.24002)（[开源代码](https://github.com/eval-sys/mcpmark)）：评什么：真实、全面 MCP 使用的压力测试；核心思想：覆盖多服务器、多工具依赖、状态性任务和异常恢复，比单函数调用更贴近 MCP production workflow。
- [VitaBench](https://arxiv.org/abs/2509.26490)：评什么：更贴近“真实应用工具链”的多步调用能力（包含多工具组合与结果校验）。核心思想：把工具调用从“单次函数预测”提升为“可执行的多步工作流”。
- [TRAJECT-Bench](https://arxiv.org/abs/2510.04550)：评什么：agentic tool use 的完整调用轨迹质量，而不只是最终答案；核心思想：用可执行工具和细粒度指标检查工具选择、参数化、调用顺序、并行宽度和链路深度，定位“答案对但调用链错”的失败。
- [Tool Decathlon（Toolathlon）](https://arxiv.org/abs/2510.25726)：评什么：跨 32 个应用、604 个工具的长程真实任务执行。核心思想：大量工具来自 MCP server，且每个任务有专用执行检查脚本，强调跨应用状态、工具链长度和真实初始环境。
- [NESTFUL](https://aclanthology.org/2025.emnlp-main.1702/)：评什么：嵌套 API 调用序列。核心思想：专测一个工具调用结果需要继续作为更深层调用参数的规划模式，暴露扁平 function-calling benchmark 看不到的失败。
- [MCP-Atlas](https://arxiv.org/abs/2602.00933)（[开源代码](https://github.com/scaleapi/mcp-atlas)）：评什么：真实 MCP server 上的多步工具编排；核心思想：用 36 个 real MCP servers、容器化 harness 和 claims-based rubric 测工具发现、参数对齐与恢复。
- [τ³-Bench](https://sierra.ai/uk/resources/research/tau-3-bench)：评什么：把 tau 系列有状态工具调用扩展到知识检索和语音客服场景的 agentic customer-interaction 任务；核心思想：保留现实 policy、状态和工具约束，同时加入原始文本/API tau-bench 之外的知识与语音代理压力。
- [MCP misleading tool-description measurement](https://arxiv.org/abs/2602.03580)：评测 MCP 工具描述与实现不一致时 agent 的行为。核心思想是结合大规模 MCP server 一致性分析和 agent 行为测试，使工具使用评测覆盖语义层面的描述-代码错配，而不只看参数填写。
- [Agent-Diff](https://arxiv.org/abs/2602.11224)（[开源代码](https://github.com/agent-diff-bench/agent-diff)）：评什么：通过代码执行企业 API 任务，并在沙箱化服务副本上验证。核心思想：按预期状态差异而不是轨迹相似度判断成功，在保留真实 API 交互结构的同时让最终结果可确定、可复现。
- [CCTU](https://arxiv.org/abs/2603.15309)：评什么：复杂约束下的 LLM 工具使用；核心思想：把资源、行为、工具集和响应四类约束显式写入任务，考察模型在选工具、遵守约束和自我修正之间能否稳定折中。
- [WildToolBench](https://arxiv.org/abs/2604.06185)：评什么：真实用户行为下的多轮、多步工具使用；核心思想：把组合任务、跨轮隐含意图和指令切换纳入评测，避免只在人工规整任务上高估 tool-use 能力。
- [The Amazing Agent Race（AAR）](https://arxiv.org/abs/2604.10261)（[项目页](https://minnesotanlp.github.io/the-amazing-agent-race)；[开源代码](https://github.com/minnesotanlp/the-amazing-agent-race)）：评什么：DAG 化的多步工具、网页导航与算术推理；核心思想：把导航、工具调用与结果汇总拆开诊断，专测线性 benchmark 看不到的路径选择失败。
- [UniToolCall](https://arxiv.org/abs/2604.11557)：评什么：工具调用轨迹的统一表示、数据构造与评测。核心思想：把公开数据集和 benchmark 标准化成 Query-Action-Observation-Answer 格式，用兼容指标覆盖单轮、多轮、串行和并行工具调用结构。
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)（[项目页](https://claw-eval-live.github.io/)；[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：评什么：持续更新的真实 workflow agent 任务，覆盖终端、文件、网页、服务和 skill 相关工具链。核心思想：从公开 workflow-demand signals 与 ClawHub skill 信号生成带 fixture、service 和 grader 的任务快照，用可执行轨迹和产物验证评估 tool-use 迁移性。
- [AgentEscapeBench](https://arxiv.org/abs/2605.07926)：评什么：长程依赖下的域外工具接地推理。核心思想：用 escape-room 式任务、工具与物品依赖图、隐藏状态和确定性最终答案，测试 agent 能否推断新流程，而不是复读熟悉 API workflow。
- [When2Tool](https://arxiv.org/abs/2605.09252)（[开源代码](https://github.com/Trustworthy-ML-Lab/when2tool)）：评什么：agent 什么时候应该调用工具、什么时候应该直接回答；核心思想：把 tool necessity 显式做成评测边界，避免把“多调用工具”误判成更强的工具使用能力。
说明：这条线更像“能否正确选工具、填参数、处理多轮 API orchestration”，不只是函数调用准确率。
- [ComplexMCP](https://arxiv.org/abs/2605.10787)：评什么：动态、相互依赖、大规模 tool sandbox 中的 LLM agent；核心思想：把工具状态、跨工具依赖和环境变化一起纳入评分，专测 MCP 工具链在长链路执行中的脆弱点。

## 1.11.4 Agent Harness

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

## 1.11.5 Skill

- [mcp-builder](https://skills.sh/anthropics/skills/mcp-builder) 适合快速搭建 MCP server。
- [mcp-cli](https://skills.sh/github/awesome-copilot/mcp-cli) 适合 MCP 运行与命令行管理。
- [mcp-deploy-manage-agents](https://skills.sh/github/awesome-copilot/mcp-deploy-manage-agents) 适合 MCP 服务部署与代理生命周期管理。
- [mcporter](https://github.com/openclaw/openclaw/tree/main/skills/mcporter) 适合在 agent-readable 的命令行流程中列出、配置、认证、调用并检查 MCP server 与工具。
- [langchain4j-tool-function-calling-patterns](https://skills.sh/giuseppe-trisciuoglio/developer-kit/langchain4j-tool-function-calling-patterns) 适合把 function calling 接入工程框架。
- [skill-validator](https://skills.sh/daffy0208/ai-dev-standards/skill-validator) 可作为工具调用链路中的额外验证层。
