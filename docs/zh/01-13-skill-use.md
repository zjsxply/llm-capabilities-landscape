# 1.13 Skill 调用

> 上级章节：1. 基础能力


说明：这条线关注的不是“能否把某个 API 调对”，而是“能否检索、选择、组合并复用封装好的技能包/工作流模板”。
与 `1.11 工具调用` 相比，skill 调用多了一层 `技能发现 -> 适配 -> 编排 -> 持久复用` 的 runtime 责任。

## 1.13.1 Leaderboard

- [SkillsBench Leaderboard](https://www.skillsbench.ai/leaderboard)：当前最直接的 skill-use 持续榜单。
  它按 `no skill / curated skill / self-generated skill` 等条件对比 agent，适合判断 skill 是否真正改善任务成功率，而不是只比较底层模型能力。
- [PinchBench](https://pinchbench.com/about)：OpenClaw 生态中的真实任务榜单/评测入口。
  它不是纯 skill benchmark，但任务集中包含 ClawHub skill 安装、skill 搜索和 skill 使用相关场景，适合作为产品化 skill 生态的实践补充。
- [Claw-Eval-Live](https://claw-eval-live.github.io/)：持续 workflow agent 榜单，显式使用 ClawHub skill 信号构造任务。
  它更适合观察 agent 在动态 workflow 中能否发现、安装、调用和验证 skills，而不是只在理想给定 skill 条件下比较 pass rate。

## 1.13.2 Survey

- [Augmented Language Models: a Survey](https://arxiv.org/abs/2302.07842)：关于工具、检索、记忆与外部推理增强模型的基础综述。
- [What Are Tools Anyway? A Survey from the Language Model Perspective](https://arxiv.org/abs/2403.15452)：建立 tools 与可复用 skills 之间的概念边界。
- [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430)：回顾 skill 架构、获取流程、安全与未来方向。
- [Towards Secure Agent Skills: Architecture, Threat Taxonomy, and Security Analysis](https://arxiv.org/abs/2604.02837)：给出恶意 skill、供应链与沙箱的威胁分类。
- [A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications](https://arxiv.org/abs/2605.07358)：直接综述 agent skill 的定义、获取、组合、评测与应用。

## 1.13.3 Bench

- [LifelongAgentBench](https://arxiv.org/abs/2505.11942)：评什么：LLM agent 是否能在长期任务序列中学习、记住并复用技能。
  核心思想：把任务按 episode 串起来，让 agent 面对新任务时利用过去经验、工具操作模式和可迁移技能，而不是只在单次任务内做即时规划。
- [Single-Agent with Skills](https://arxiv.org/abs/2601.04748)：评什么：带 skills 的 single agent 何时能替代 multi-agent systems，何时会失败。
  核心思想：用对比式任务协议区分可复用技能带来的收益与必须依赖多代理分解的收益。
- [SkillsBench](https://arxiv.org/abs/2602.12670)（[开源代码](https://github.com/benchflow-ai/skillsbench)；[官网](https://www.skillsbench.ai/)）：评什么：agent 在使用人写或自生成 skills 时，任务成功率到底能否稳定提升。
  核心思想：把 skill 的价值变成 `no skill / curated skill / self-generated skill` 三条件对照；论文版覆盖 86 个任务、11 个领域，官网当前展示 84 个任务。
- [SkillJect](https://arxiv.org/abs/2602.14211)：评什么：编码智能体中通过技能文件触发的隐蔽提示注入。核心思想：利用执行轨迹做闭环迭代，针对真实编码智能体轨迹优化恶意技能，把技能安全评测从静态恶意指令扩展到可迭代优化的攻击。
- [SkillInject](https://arxiv.org/abs/2602.20156)：评什么：agent 是否容易受到 skill 文件中嵌入提示注入的攻击。核心思想：把可复用 skill 作为显式攻击面，衡量恶意指令是否会在执行时重定向 agent 行为。
- [SkillCraft](https://arxiv.org/abs/2603.00718)（[开源代码](https://github.com/shiqichen17/SkillCraft)；[项目页](https://skillcraft-website.github.io/page/)）：评什么：agent 能否把原子工具抽象成可复用 skill，并在长链路任务里缓存、跨任务复用。
  核心思想：通过 `quantitative scaling` 与 `structural scaling` 压力测试 skill abstraction；不仅看 instance-level success，也看 skill 复用带来的效率收益。
- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401)（[开源代码](https://github.com/GeniusHTX/SWE-Skills-Bench)；[数据集](https://huggingface.co/datasets/GeniusHTX/SWE-Skills-Bench)）：评什么：agent skills 在真实软件工程任务中是否真的带来收益。
  核心思想：把评价对象从“coding agent 能不能修代码”转成“给定 skill 是否改善软件工程 agent 的成功率、效率和行为质量”。
- [SkillTester](https://arxiv.org/abs/2603.28815)（[项目页](https://skilltester.ai/)；[开源代码](https://github.com/skilltester-ai/skilltester)）：评什么：agent skills 的效用与安全性。
  核心思想：比较 baseline 与 with-skill 两种执行，同时对 skill 做安全探测，把技能收益和技能风险放进同一个 benchmark。
- [Agentic Skills in the Wild](https://arxiv.org/abs/2604.04323)：评什么：真实技能生态中 agent 自行搜索、选择并使用不完全贴合任务的 skills 时，skill 是否仍然有帮助。
  核心思想：把“直接给定理想 skill”的设定放宽成检索、噪声和适配压力，评估 skill utility 在 realistic settings 下的掉点。
- [MM Claw skill-compliance suite](https://www.minimax.io/news/minimax-m27-en)（model-card-only；未确认有独立公开发布）：评什么：agent 在长程 OpenClaw 风格工作中，能否持续遵循并复用 40 多个复杂 skills。核心思想：把 skill adherence 本身作为评测信号，补足公开 skill search 与 skill injection benchmark 对“持续按 skill 做事”的覆盖。
- [SkillLearnBench](https://arxiv.org/abs/2604.20087)（[开源代码](https://github.com/cxcscmu/SkillLearnBench)）：评什么：连续技能学习与生成；核心思想：把 skill 质量、执行轨迹和任务结果三层一起测，观察能否稳定学到可复用技能。
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)（[项目页](https://claw-eval-live.github.io/)；[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：评什么：持续更新的真实 workflow agent 任务，其中显式使用 ClawHub skill 信号构造任务。核心思想：把 skill 发现、安装、调用和验证放进周期性刷新任务分布中，补足 SkillsBench 的静态对照。
- [SkillRet](https://arxiv.org/abs/2605.05726)：评什么：大规模 agent skill 库检索；核心思想：把 skill 选择当检索问题，测长查询、噪声库和 NDCG / 召回。
- [FORTIS](https://arxiv.org/abs/2605.09163)：评什么：agent skills 是否越过最小权限边界。
  核心思想：把评测拆成“是否选到最小充分 skill”和“执行时是否扩展到 skill 之外的工具/动作”，把 skill 层从组织抽象提升为可测的权限边界。
- [Dependency Steering](https://arxiv.org/abs/2605.09594)：评什么：恶意 skills 是否会诱导 coding agent 选择攻击者指定的依赖。
  核心思想：把持久化 skill 文件视为软件供应链攻击面，衡量 skill 内容如何改变编码工作流中的依赖选择。
- [Skill Description Deception Attack](https://arxiv.org/abs/2605.09889)：评估 Internet-of-Agents 场景中的任务路由是否会被欺骗性自声明技能描述操纵。核心思想：形式化 SDD 攻击并生成欺骗性描述，测量路由偏置和可靠性下降。
- [SkillSafetyBench](https://arxiv.org/abs/2605.12015)：评什么：skill-facing attack surface 下 agent 是否会被第三方 skill、局部材料或本地 artifact 诱导执行不安全动作。
  核心思想：把普通任务、风险域、恶意/良性 skill 材料和规则验证器放进可运行环境，说明 skill 安全不能只靠模型级对齐评测。
- [AgentTrap](https://arxiv.org/abs/2605.13940)（[开源代码](https://github.com/zhmzm/AgentTrap)；[数据集](https://huggingface.co/datasets/zhmzm/AgentTrap)）：评什么：第三方 skills 中恶意运行时行为是否会被 agent 盲目执行。
  核心思想：把普通用户任务、恶意或良性 skill 包和沙箱执行环境组合起来，按完整轨迹判断攻击成功、阻断、未触发和无证据等结果。
- [SkillGenBench](https://arxiv.org/abs/2605.18693)：评什么：LLM agent 的 skill generation pipeline；核心思想：不只看最终任务成功，还把 skill 提炼、可执行性、泛化与后续复用作为评测对象。
- [PinchBench](https://pinchbench.com/about)（[开源代码](https://github.com/pinchbench/skill)）：更适合当作 skill 调用的实践补充 benchmark，而不是纯学术“skills benchmark”。
  它本质上评测 OpenClaw agent 在真实任务中的整体执行，但任务集显式包含 `ClawHub skill 安装` 与 `skill 搜索/安装` 场景，因此能补足产品生态里的 skill 接入与调用能力。

## 1.13.4 Agent Harness

- [SkillFlow](https://arxiv.org/abs/2504.06188)：多阶段 agent skill retrieval pipeline；核心思想：把 skill acquisition 建模成信息检索，在约 36K 个社区 `SKILL.md` 定义上串联 dense retrieval、cross-encoder reranking 和 LLM selection。
- [CUA-Skill](https://arxiv.org/abs/2601.21123)（[项目页](https://microsoft.github.io/cua_skill/)）：面向 computer-use agents 的结构化 skill base 与 CUA-Skill Agent；核心思想：把 GUI 操作知识封装成带参数化执行和组合图的 skills，再通过检索、参数实例化和记忆化失败恢复调用。
- [Skill-Pro](https://arxiv.org/abs/2602.01869)：程序性 skill 学习 harness。核心思想：从 episodic experience 中学习带显式 activation、execution 和 termination condition 的可执行技能。
- [SkillRL](https://arxiv.org/abs/2602.08234)（[开源代码](https://github.com/aiming-lab/SkillRL)）：recursive skill-augmented reinforcement learning；核心思想：把经验总结成 reusable skills，并在后续 RL 迭代中继续读取、扩展和验证 skill bank。
- [SkillOrchestra](https://arxiv.org/abs/2602.19672)：skill-aware agent routing harness。核心思想：通过 skill transfer 路由 agents，把技能的可迁移性变成显式编排信号。
- [TARSE](https://arxiv.org/abs/2603.01241)：为 reasoning agents 检索 skills 与 experience 的 test-time adaptation harness。
  核心思想：在每个推理步骤选择可复用过程知识和先前经验，让 skill 复用成为在线适配的一部分。
- [AgentSkillOS](https://arxiv.org/abs/2603.02176)（[开源代码](https://github.com/ynulihao/AgentSkillOS)）：代表 skill retrieval + orchestration 的 OS 化路线；把 skill 调用拆成 `capability tree 检索 -> DAG 编排 -> artifact-rich 输出评测`。
  核心思想：在 200 到 200K skills 的生态规模下，比较“平铺直接调用”与“结构化检索 + DAG 组合”；论文同时给出 30 个跨五类的 artifact-rich 任务，说明 skill 调用的关键不只是找到 skill，而是把多 skill 组织成可执行 pipeline。
- [XSkill](https://arxiv.org/abs/2603.12056)：持续学习型多模态 agent skill harness。核心思想：同时保留视觉 experience 与结构化 reusable skill，让后续任务既能利用 episodic evidence，也能利用程序性抽象。
- [Memento-Skills](https://arxiv.org/abs/2603.18743)（[开源代码](https://github.com/Memento-Teams/Memento-Skills)）：把 reusable skills 当作持久化、可演化 memory 的 generalist agent 系统。
  核心思想：通过 read-write reflective learning 选择、更新和扩展 Markdown skill 文件，让 agent 在不更新模型参数的情况下持续改造 task-specific agents。
- [Trace2Skill](https://arxiv.org/abs/2603.25158)：trajectory-to-skill distillation harness。核心思想：并行分析执行轨迹，再分层整合局部经验，把它们沉淀成可迁移 agent skills。
- [AdaSkill](https://arxiv.org/abs/2604.01608)：判断何时可用单个 skill-augmented agent 替代 multi-agent system 的 skill distillation harness。
  核心思想：只有在 metric-free 诊断显示蒸馏有益时，才从多代理轨迹中抽取工具、知识和结构。
- [SkVM](https://arxiv.org/abs/2604.03088)（[开源代码](https://github.com/SJTU-IPADS/SkVM)）：skill 编译与运行时；核心思想：把 skill 当可编译工件做能力绑定、并发抽取和 JIT 固化，提升跨 harness 可移植性。
- [SkillFoundry](https://arxiv.org/abs/2604.03964)（[开源代码](https://github.com/ma-compbio-lab/SkillFoundry)）：从异构科学/工程资源中构建自演化 skill libraries。
  核心思想：把文档、仓库、脚本、notebooks、数据库和论文中的 procedural knowledge 抽取成带输入输出、执行步骤、环境假设、来源和测试的 skill packages，再闭环扩展、修复、合并和剪枝。
- [SkillX](https://arxiv.org/abs/2604.04804)（[开源代码](https://github.com/zjunlp/SkillX)）：自动构建 plug-and-play skill knowledge base。
  核心思想：把轨迹蒸馏成战略计划、功能技能和原子技能三层结构，并通过执行反馈迭代修正和主动扩展技能覆盖。
- [Graph of Skills](https://arxiv.org/abs/2604.05333)（[开源代码](https://github.com/davidliuk/graph-of-skills)）：依赖感知的 skill 结构检索；核心思想：把扁平 skill 列表改成带前置关系的结构化上下文，减少盲选。
- [EvoAgent](https://arxiv.org/abs/2604.20133)：面向 skill learning 与 multi-agent delegation 的可演化 agent 框架。
  核心思想：把技能作为可学习、可复用单元，并根据演化中的技能状态在多代理之间委派任务。
- [Co-Evolving LLM Decision and Skill Bank Agents](https://arxiv.org/abs/2604.20987)：面向长程任务的 skill-bank harness。
  核心思想：让 decision agent 与 skill-bank agent 协同演化，使任务经验同时改造规划策略和可复用技能库存。
- [From Skills to Talent](https://arxiv.org/abs/2604.22446)：把异构 agent 组织成可移植的 Talents。核心思想：把 skills、tools 和 runtime configuration 打包成可招募的 agent 身份，再用 Explore-Execute-Review tree search 与 Talent Market 动态组装、执行并改进多代理组织。
- [SkCC](https://arxiv.org/abs/2605.03353)：跨框架 skill 编译与安全加固；核心思想：用强类型中间表示 SkIR 解耦 Markdown skill 的语义与不同 agent framework 的提示格式，同时把权限、安全检查和可移植性纳入编译流程。
- [SkillScope](https://arxiv.org/abs/2605.05868)：面向 agent skills 的最小权限执行层。核心思想：对每个 skill 的权限做细粒度作用域限定，并在执行时强制检查，避免可复用 skill 静默扩大 agent 权限。
- [SkillMaster](https://arxiv.org/abs/2605.08693)：自主 skill mastery 框架。
  核心思想：打通技能创建、修订和选择闭环，让 LLM agent 维护可复用能力，而不是只消费固定技能列表。
- [SPARK](https://arxiv.org/abs/2605.09192)（[开源代码](https://github.com/EtaYang10th/spark-skills)）：structured pipelines for autonomous runnable tasks；核心思想：把任务完成后的经验压缩成可运行技能流程，强调 posterior skill formation 与后续复用。
- [SkillRAE](https://arxiv.org/abs/2605.10114)：skill-based context compilation for retrieval-augmented execution；核心思想：把检索到的 skills 编译成紧凑、grounded、可执行的上下文，而不是直接把一组 Markdown skill 原文塞给 agent。
- [SkillEvolver](https://arxiv.org/abs/2605.10500)：online skill learning meta-skill；核心思想：把“写、部署、失败后修订 domain skill”的流程本身封装成 meta-skill，用 fresh-agent audit 避免只在当前 agent 上过拟合。
- [AI Workflow Store](https://arxiv.org/abs/2605.10907)：面向稳健个人 agent 的 workflow store 基础设施。核心思想：把可复用工作流封装成可检索、可改写、可执行的过程资产，使 agent 不必在每次会话中从零生成脆弱计划。
- [SkillGen](https://arxiv.org/abs/2605.10999)：带验证的 inference-time agent skill synthesis。
  核心思想：在推理时从轨迹中合成可审计的可复用技能，并把 verification 纳入技能生成流程。
- [Constraint-Consistent Skill Composition](https://doi.org/10.1109/ISBDAS69350.2026.11484408)：面向可靠性的 skill composition harness。
  核心思想：用一致性约束来组合技能，使 zero-shot 任务泛化遵守约束条件，而不是机会式拼接技能。
- [CTA / Counterfactual Trace Auditing](https://arxiv.org/abs/2605.11946)：skill 影响的轨迹级审计框架；核心思想：把有 skill 与无 skill 的同任务轨迹分段对齐，标注 skill influence pattern，补足只看 pass rate 难以发现的行为改变。

## 1.13.5 Skill

- [SkillFortify](https://arxiv.org/abs/2603.00195)：面向 agentic skill 供应链的形式化分析框架。核心思想是建模 skill 生命周期中的恶意 skill，结合静态分析、capability sandbox 和审计证据，使 skill 生态获得强于启发式扫描的安全保证。
- [SkillNet](http://skillnet.openkg.cn)（论文：[SkillNet](https://arxiv.org/abs/2603.04448)；[开源代码](https://github.com/zjunlp/SkillNet)）更像 skill registry / ontology / marketplace 基础设施，覆盖 skill 创建、评估、连接与检索。
- [SkillSieve](https://arxiv.org/abs/2604.06550)：用于检测恶意 AI agent skill 的分层筛查框架。核心思想是结合快速静态检查、聚焦的 LLM 子分析，并只对可疑 skill 包做更深审查，使 skill 市场能同时筛查代码与 `SKILL.md` 自然语言攻击面。

这条线当前更成熟的是 `benchmark + retrieval/orchestration/runtime + registry`，而不是“专门服务于 skill 调用”的单个 skill。如果要落到工程实践，更值得回看 `0.3 Skill Creator` 里的 creator / validator / reviewer 路线；它们决定了 skill 是否可发现、可安装、可组合。
