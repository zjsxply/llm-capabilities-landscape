# 1.13.6 Skill

- [Skill Discovery for Software Scripting Automation via Offline Simulations with LLMs](https://arxiv.org/abs/2504.20406)：可作为技能使用的Skill候选；核心关注“Skill Discovery for Software Scripting Automation via Offline Simulations with LLMs”。
- [Capability-Driven Skill Generation with LLMs: A RAG-Based Approach for Reusing Existing Libraries and Interfaces](https://arxiv.org/abs/2505.03295)：从能力描述出发检索相关库和接口，再把它们封装成可复用 skill wrapper，减少逐个手写工具 recipe 的成本。
- [ToolLibGen: Scalable Automatic Tool Creation and Aggregation for LLM Reasoning](https://arxiv.org/abs/2510.07768)：自动生成和聚合 LLM reasoning 所需工具库，符合 skill/tool creation 条目。
- [SkillWrapper](https://arxiv.org/abs/2511.18203)：面向任务级规划的 skill abstraction 机制。核心思想：把单次 skill execution 封装成发明出的 predicate，使长程 planner 能围绕可复用能力单元推理。
- [SkillFortify](https://arxiv.org/abs/2603.00195)：面向 agentic skill 供应链的形式化分析框架。核心思想是建模 skill 生命周期中的恶意 skill，结合静态分析、capability sandbox 和审计证据，使 skill 生态获得强于启发式扫描的安全保证。
- [SkillNet](http://skillnet.openkg.cn)（论文：[SkillNet](https://arxiv.org/abs/2603.04448)；[开源代码](https://github.com/zjunlp/SkillNet)）更像 skill registry / ontology / marketplace 基础设施，覆盖 skill 创建、评估、连接与检索。
- [Knowledge Activation](https://arxiv.org/abs/2603.14805)：面向 agentic 软件开发中机构知识的 skill 设计框架。核心思想：把流程、政策、部署手册和决策封装成带治理约束、agent 可消费的 skill 单元。
- [EffiSkill: Agent Skill Based Automated Code Efficiency Optimization](https://arxiv.org/abs/2603.27850)：可作为技能使用的Skill候选；核心关注“Agent Skill Based Automated Code Efficiency Optimization”。
- [Skill Supply-Chain Poisoning](https://arxiv.org/abs/2604.03081)：研究面向 coding-agent skill ecosystem 的供应链投毒攻击。核心思想：把第三方 skill 视为供应链依赖，其受信复用可能静默改变 agent 行为。
- [SkillAttack](https://arxiv.org/abs/2604.04989)：面向 agent skill 的自动化 red-teaming framework。核心思想：对 skill package 迭代修订攻击路径，使审计覆盖多步误用，而不只检查孤立 prompt。
- [SkillSieve](https://arxiv.org/abs/2604.06550)：用于检测恶意 AI agent skill 的分层筛查框架。核心思想是结合快速静态检查、聚焦的 LLM 子分析，并只对可疑 skill 包做更深审查，使 skill 市场能同时筛查代码与 `SKILL.md` 自然语言攻击面。

这条线当前更成熟的是 `benchmark + retrieval/orchestration/runtime + registry`，而不是“专门服务于 skill 调用”的单个 skill。如果要落到工程实践，更值得回看 `0.3 Skill Creator` 里的 creator / validator / reviewer 路线；它们决定了 skill 是否可发现、可安装、可组合。
- [BadSkill](https://arxiv.org/abs/2604.09378)：研究 model-in-skill poisoning 对 agent skill 的后门威胁。核心思想：把恶意行为藏进 skill 捆绑的模型 artifact 中，使 skill 在语义触发条件出现前看似良性。
- [Reasoning Skills](https://arxiv.org/abs/2604.21764)：用于 token-efficient inference 的可复用 reasoning-skill 层。核心思想：把长推理轨迹蒸馏为可检索 skill，引导后续代码和数学推理，而不是每次从零思考。
- [KG-First, LLM-Fallback: A Hybrid Microservice for Grounded Skill Search and Explanation](https://arxiv.org/abs/2605.01582)：补充面向技能使用、技能搜索与可复用技能基础设施的可复用技能搜索、技能解释或技能运行时基础设施。
- [Experience-RAG Skill](https://arxiv.org/abs/2605.03989)：用于经验驱动检索编排的可插拔 skill。核心思想：从既往经验中选择适合事实问答、多跳推理和科学验证任务的检索策略。
- [Proteus](https://arxiv.org/abs/2605.11891)：面向 agent skill ecosystem 的自演化 red team。核心思想：通过 audit-sandbox-oracle 循环反复改写 skill 来衡量 adaptive leakage，直到发现或阻断运行时危害。
- [HarnessAPI](https://arxiv.org/abs/2605.22733)：统一 streaming APIs 与 MCP tools 的 skill-first runtime framework。核心思想：把 typed skill folder 作为单一事实源，再从该 artifact 派生 SSE HTTP endpoint、OpenAPI UI 和 MCP tool。
- [SkillDAG: Self-Evolving Typed Skill Graphs for LLM Skill Selection at Scale](https://arxiv.org/abs/2606.03056)：将 skill 库建模为 typed directed graph，显式表示依赖、冲突、特化和重复关系，并把图邻域检索与 propose-then-commit 更新暴露为 agent 可调用的 skill selection 接口。
- [SkillAxe](https://arxiv.org/abs/2606.10546)：通过 evaluation-guided self-refinement 改进 LLM-authored agent skills。核心思想：在无监督条件下诊断 quality impact、trigger precision、instruction compliance 和 solution-path coverage，并在 SkillsBench 与 SpreadsheetBench 上提升 pass rate。
