# 1.13.3 Bench

- [LifelongAgentBench](https://arxiv.org/abs/2505.11942)：评什么：LLM agent 是否能在长期任务序列中学习、记住并复用技能。
  核心思想：把任务按 episode 串起来，让 agent 面对新任务时利用过去经验、工具操作模式和可迁移技能，而不是只在单次任务内做即时规划。
- [SkillVerse : Assessing and Enhancing LLMs with Tree Evaluation](https://arxiv.org/abs/2506.00319)：用树结构技能评测诊断语言模型；核心思想是在细粒度技能层面定位能力缺口，而不是只报告汇总 benchmark 分数。
- [StuLife / Experience-Driven Lifelong Learning](https://arxiv.org/abs/2508.19005)：评什么：自演化 agent 能否在动态长时程环境中学习、记住并迁移可复用 skill。核心思想：把探索、长期记忆、skill 抽象和后续验证放进同一连续协议。
- [EvoTest: Evolutionary Test-Time Learning for Self-Improving Agentic Systems](https://arxiv.org/abs/2510.13220)：类型：benchmark/评测协议。核心价值：为 1.13.2 Bench 补充一个任务边界清晰、可比较的评测入口；正式写入时可进一步压缩为一行 benchmark 条目。
- [In-Context Skill Composition](https://arxiv.org/abs/2510.22993)：评什么：语言模型能否在上下文中组合示例展示的基础 skill。核心思想：测试模型无需额外训练即可识别并组装可复用原子 skill。
- [Agent-Skill Prompt Injection](https://arxiv.org/abs/2510.26328)：评什么：通过持久化 agent-skill artifact 触发的 prompt injection。核心思想：把 skill 视为可执行上下文，可能把攻击指令带入后续 agent 运行。
- [Single-Agent with Skills](https://arxiv.org/abs/2601.04748)：评什么：带 skills 的 single agent 何时能替代 multi-agent systems，何时会失败。
  核心思想：用对比式任务协议区分可复用技能带来的收益与必须依赖多代理分解的收益。
- [Agent Skills in the Wild](https://arxiv.org/abs/2601.10338)：评什么：公开 agent skill 的大规模安全漏洞。核心思想：用覆盖 prompt injection、数据外泄、权限提升和供应链风险的漏洞分类扫描 skill marketplace。
- [Malicious Agent Skills in the Wild](https://arxiv.org/abs/2602.06547)：评什么：经过行为验证的第三方恶意 skill。核心思想：从社区注册表构建带标签的恶意 skill 数据集，并刻画攻击类型、kill chain 阶段和下架结果。
- [When Skills Lie: Hidden-Comment Injection in LLM Agents](https://arxiv.org/abs/2602.10498)：研究大模型智能体技能中的隐藏注释注入，把持久化技能文件视为后续运行中的攻击面。
- [SkillsBench](https://arxiv.org/abs/2602.12670)（[开源代码](https://github.com/benchflow-ai/skillsbench)；[官网](https://www.skillsbench.ai/)；[官方榜单](https://www.skillsbench.ai/leaderboard)）：评什么：agent 在使用人写或自生成 skills 时，任务成功率到底能否稳定提升。
  核心思想：把 skill 的价值变成 `no skill / curated skill / self-generated skill` 三条件对照；论文版覆盖 86 个任务、11 个领域，官网当前展示 84 个任务。
- [SkillJect](https://arxiv.org/abs/2602.14211)：评什么：编码智能体中通过技能文件触发的隐蔽提示注入。核心思想：利用执行轨迹做闭环迭代，针对真实编码智能体轨迹优化恶意技能，把技能安全评测从静态恶意指令扩展到可迭代优化的攻击。
- [SkillInject](https://arxiv.org/abs/2602.20156)：评什么：agent 是否容易受到 skill 文件中嵌入提示注入的攻击。核心思想：把可复用 skill 作为显式攻击面，衡量恶意指令是否会在执行时重定向 agent 行为。
- [SkillCraft](https://arxiv.org/abs/2603.00718)（[开源代码](https://github.com/shiqichen17/SkillCraft)；[项目页](https://skillcraft-website.github.io/page/)）：评什么：agent 能否把原子工具抽象成可复用 skill，并在长链路任务里缓存、跨任务复用。
  核心思想：通过 `quantitative scaling` 与 `structural scaling` 压力测试 skill abstraction；不仅看 instance-level success，也看 skill 复用带来的效率收益。
- [Clawdrain: Exploiting Tool-Calling Chains for Stealthy Token Exhaustion in OpenClaw Agents](https://arxiv.org/abs/2603.00902)：定义面向 OpenClaw 式智能体工具调用链的 token 耗尽攻击，补充技能与工具安全压力测试。
- [Tool-Genesis](https://arxiv.org/abs/2603.05578)：评什么：自演化 agent 的任务驱动工具创建能力。核心思想：测试 agent 能否从抽象任务需求推断接口、实现可执行逻辑，并使用新创建的工具。
- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401)（[开源代码](https://github.com/GeniusHTX/SWE-Skills-Bench)；[数据集](https://huggingface.co/datasets/GeniusHTX/SWE-Skills-Bench)）：评什么：agent skills 在真实软件工程任务中是否真的带来收益。
  核心思想：把评价对象从“coding agent 能不能修代码”转成“给定 skill 是否改善软件工程 agent 的成功率、效率和行为质量”。
- [Repository-Context Skill Classification](https://arxiv.org/abs/2603.16572)：评什么：结合仓库上下文的恶意/良性 skill 分类。核心思想：用代码和仓库证据判断 skill，而不是只看 marketplace 元数据。
- [SkillProbe](https://arxiv.org/abs/2603.21019)：评什么：新兴 agent skill marketplace 的安全风险。核心思想：用多 agent 审计检测语义-行为不一致和跨 skill 组合风险。
- ["Elementary, My Dear Watson."Detecting Malicious Skills via Neuro-Symbolic Reasoning across Heterogeneous Artifacts](https://arxiv.org/abs/2603.27204)：通过跨异构产物的神经符号推理检测恶意智能体技能，将技能安全评测从纯文本 manifest 扩展到更多证据面。
- [SkillTester](https://arxiv.org/abs/2603.28815)（[项目页](https://skilltester.ai/)；[开源代码](https://github.com/skilltester-ai/skilltester)）：评什么：agent skills 的效用与安全性。
  核心思想：比较 baseline 与 with-skill 两种执行，同时对 skill 做安全探测，把技能收益和技能风险放进同一个 benchmark。
- [Credential Leakage in Agent Skills](https://arxiv.org/abs/2604.03070)：评什么：LLM agent skill artifact 中的凭据泄漏。核心思想：审计 secret、不安全凭据处理和普通任务成功率无法发现的泄漏模式。
- [Agentic Skills in the Wild](https://arxiv.org/abs/2604.04323)：评什么：真实技能生态中 agent 自行搜索、选择并使用不完全贴合任务的 skills 时，skill 是否仍然有帮助。
  核心思想：把“直接给定理想 skill”的设定放宽成检索、噪声和适配压力，评估 skill utility 在 realistic settings 下的掉点。
- [SkillTrojan](https://arxiv.org/abs/2604.06811)：评什么：skill-based agent system 中的后门攻击。核心思想：把持久化 skill 视为可复用攻击面，测试隐藏行为如何在后续调用中延续。
- [STARS / SIA-Bench](https://arxiv.org/abs/2604.10286)：评什么：request-conditioned skill invocation safety。核心思想：在调用前联合用户请求、候选 skill 和运行时上下文打分，并用专门 invocation records 校准风险。
- [HarmfulSkillBench](https://arxiv.org/abs/2604.15415)：评什么：可在多个风险领域武器化 agent 的 harmful skills。核心思想：衡量开放 skill 生态中的 harmful skill 分布和 agent 误用途径，而不只扫描普通漏洞。
- [SkillFlow Lifelong Benchmark](https://arxiv.org/abs/2604.17308)：评什么：自治 agent 的终身 skill 发现、修复与演化。核心思想：让 agent 在连续任务族中从无 skill 开始，根据轨迹修补 skill，并把更新后的 skill library 带到后续任务。
- [SkillLearnBench](https://arxiv.org/abs/2604.20087)（[开源代码](https://github.com/cxcscmu/SkillLearnBench)）：评什么：连续技能学习与生成；核心思想：把 skill 质量、执行轨迹和任务结果三层一起测，观察能否稳定学到可复用技能。
- [MedSkillAudit](https://arxiv.org/abs/2604.20441)：评什么：医疗研究 agent skill 的安全性与可靠性。核心思想：在误用代价高的领域审计 domain skill 是否相关、安全且可靠。
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)（[项目页](https://claw-eval-live.github.io/)；[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：评什么：持续更新的真实 workflow agent 任务，其中显式使用 ClawHub skill 信号构造任务。核心思想：把 skill 发现、安装、调用和验证放进周期性刷新任务分布中，补足 SkillsBench 的静态对照。
- [SkillRet](https://arxiv.org/abs/2605.05726)：评什么：大规模 agent skill 库检索；核心思想：把 skill 选择当检索问题，测长查询、噪声库和 NDCG / 召回。
- [FORTIS](https://arxiv.org/abs/2605.09163)：评什么：agent skills 是否越过最小权限边界。
  核心思想：把评测拆成“是否选到最小充分 skill”和“执行时是否扩展到 skill 之外的工具/动作”，把 skill 层从组织抽象提升为可测的权限边界。
- [Dependency Steering](https://arxiv.org/abs/2605.09594)：评什么：恶意 skills 是否会诱导 coding agent 选择攻击者指定的依赖。
  核心思想：把持久化 skill 文件视为软件供应链攻击面，衡量 skill 内容如何改变编码工作流中的依赖选择。
- [Skill Description Deception Attack](https://arxiv.org/abs/2605.09889)：评估 Internet-of-Agents 场景中的任务路由是否会被欺骗性自声明技能描述操纵。核心思想：形式化 SDD 攻击并生成欺骗性描述，测量路由偏置和可靠性下降。
- [SkillSafetyBench](https://arxiv.org/abs/2605.12015)（[项目页](https://jinchang1223.github.io/skill-safety-bench-website/)；[开源代码](https://github.com/AI45Lab/skill-safety-bench)）：评什么：skill-facing attack surface 下 agent 是否会被第三方 skill、局部材料或本地 artifact 诱导执行不安全动作。
  核心思想：把普通任务、风险域、恶意/良性 skill 材料和规则验证器放进可运行环境，说明 skill 安全不能只靠模型级对齐评测。
- [Code-Backed Skill Description Audit](https://arxiv.org/abs/2605.12875)：评什么：code-backed skill 中未披露的安全相关行为。核心思想：把源代码级 security-property 证据与 skill 描述声明对照，发现隐藏行为。
- [AgentTrap](https://arxiv.org/abs/2605.13940)（[开源代码](https://github.com/zhmzm/AgentTrap)；[数据集](https://huggingface.co/datasets/zhmzm/AgentTrap)）：评什么：第三方 skills 中恶意运行时行为是否会被 agent 盲目执行。
  核心思想：把普通用户任务、恶意或良性 skill 包和沙箱执行环境组合起来，按完整轨迹判断攻击成功、阻断、未触发和无证据等结果。
- [Payload-less Skills](https://arxiv.org/abs/2605.14460)：评什么：通过 agent skill 发起的无载荷供应链攻击。核心思想：展示看似良性的合规指令可在运行时诱导 coding agent，即使没有显式恶意代码载荷。
- [SkillGenBench](https://arxiv.org/abs/2605.18693)：评什么：LLM agent 的 skill generation pipeline；核心思想：不只看最终任务成功，还把 skill 提炼、可执行性、泛化与后续复用作为评测对象。
- [Skill Availability and Presentation Granularity](https://arxiv.org/abs/2605.31408)：用 controlled SkillsBench study 隔离 skill 文档可用性与展示粒度对 agent 成功率的影响。核心思想：在固定的 30-task domain-balanced subset 上设置六种 skill conditions 和多次 trial，区分“有 skill”本身的价值与“如何呈现 skill”的影响。
- [MMG2Skill-Bench](https://arxiv.org/abs/2606.01993)：评什么：从野外多模态指南到 agent-executable skill 的 guide-to-skill learning。核心思想是测试 agent 能否把面向人的噪声指南转成可执行技能，在 GUI 控制、开放式游戏和策略卡牌任务中使用，并根据可观察轨迹而非 benchmark 分数继续修订技能。
- [R3-Skill / Skill Is Not Document](https://arxiv.org/abs/2606.03565)：用中英双语 R3-Skill benchmark 评测 query-conditioned agent skill routing。核心思想：评估用户 query 与候选 skill 的兼容性，而不是把 skill 当普通文档检索，并配套两阶段 retriever 做路由。
- [SkillResolve-Bench](https://arxiv.org/abs/2606.10388)：评测 agent skill retrieval 中的同能力混淆风险。核心思想：发布 661 对 helpful/risky skill pairs、7,982 个候选池和 HSR@K 等指标，使检索系统面对相近但风险不同的 skill，而不只处理明显相关项。
- [Letta Context-Bench Skills Suite](https://leaderboard.letta.com/)：评什么：agentic context-management 榜单中的 skill-suite 行为。核心思想是比较 agent 能否在任务中选择并应用 context package 或 skill，补充 SkillsBench 这类直接 skill-use benchmark。
- [MM Claw skill-compliance suite](https://www.minimax.io/news/minimax-m27-en)（model-card-only；未确认有独立公开发布）：评什么：agent 在长程 OpenClaw 风格工作中，能否持续遵循并复用 40 多个复杂 skills。核心思想：把 skill adherence 本身作为评测信号，补足公开 skill search 与 skill injection benchmark 对“持续按 skill 做事”的覆盖。
- [PinchBench](https://pinchbench.com/about)（[开源代码](https://github.com/pinchbench/skill)）：更适合当作 skill 调用的实践补充 benchmark，而不是纯学术“skills benchmark”。
  它本质上评测 OpenClaw agent 在真实任务中的整体执行，但任务集显式包含 `ClawHub skill 安装` 与 `skill 搜索/安装` 场景，因此能补足产品生态里的 skill 接入与调用能力。
