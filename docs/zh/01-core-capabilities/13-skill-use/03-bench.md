# 1.13.3 Bench

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
