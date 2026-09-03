# 1.13.5 Agent Harness

- [On the (In)Security of LLM App Stores](https://arxiv.org/abs/2407.08422)：补充技能使用方向可复用的编排、提示、规划、工具使用、记忆或环境管理逻辑。
- [Agent Skill Acquisition for Large Language Models via CycleQD](https://arxiv.org/abs/2410.14735)：补充一个面向技能使用的智能体框架条目，关注agent skill acquisition or skill-use contribution。
- [LLM Agents Making Agent Tools](https://arxiv.org/abs/2502.11705)：研究 agent 为后续任务创建可用工具；核心思想是把一次性工具调用推进到可选择、可调用、可改进的复用工具/技能资产。
- [SkillFlow](https://arxiv.org/abs/2504.06188)：多阶段 agent skill retrieval pipeline；核心思想：把 skill acquisition 建模成信息检索，在约 36K 个社区 `SKILL.md` 定义上串联 dense retrieval、cross-encoder reranking 和 LLM selection。
- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)：面向通过发现和打磨技能实现 web agent 自我改进的 harness；核心思想是把规划、工具调用、记忆、验证、环境交互或编排逻辑外置到模型之外。
- [Rethinking Agent Design: From Top-Down Workflows to Bottom-Up Skill Evolution](https://arxiv.org/abs/2505.17673)：类型：skill 机制或技能生成/编排框架。核心价值：补充 agent skill 的发现、生成、选择或组合机制，突出可复用能力沉淀。
- [COALESCE](https://arxiv.org/abs/2506.01900)：研究自治 LLM agent 团队中基于技能的任务外包所带来的经济与安全动态。核心思想是把技能委托建模为类似市场的协作问题，考察 agent 如何在成本、信任和对抗风险之间选择是否外包能力。
- [Automated Skill Discovery for Language Agents through Exploration and Iterative Feedback](https://arxiv.org/abs/2506.04287)：通过环境探索与迭代反馈发现 agent skill，而不是依赖人工收集轨迹。
- [MetaAgent: Toward Self-Evolving Agent via Tool Meta-Learning](https://arxiv.org/abs/2508.00271)：当 agent 遇到能力缺口时生成求助请求并学习新的工具化专长。
- [HERAKLES: Hierarchical Skill Compilation for Open-ended LLM Agents](https://arxiv.org/abs/2508.14751)：为 open-ended LLM agents 编译层次化技能；核心思想是把可复用技能组织成更高层结构，使 agent 能组合能力完成开放任务。
- [Empowering LLMs with Parameterized Skills for Adversarial Long-Horizon Planning](https://arxiv.org/abs/2509.13127)：面向对抗环境的 skill-use harness。核心思想是把可复用高层行为表示为参数化 skill，再把它们落地成长程规划。
- [Metacognitive Reuse: Turning Recurring LLM Reasoning Into Concise Behaviors](https://arxiv.org/abs/2509.13237)：补充智能体技能使用与可复用行为方向的外部编排或执行框架。
- [ARM: Discovering Agentic Reasoning Modules for Generalizable Multi-Agent Systems](https://arxiv.org/abs/2510.05746)：类型：agent harness/可复用执行框架。核心价值：为 1.13.3 Agent Harness 补充可复用的执行流程、工具编排、记忆管理或多 agent 协作机制。
- [ALLOY: Generating Reusable Agent Workflows from User Demonstration](https://arxiv.org/abs/2510.10049)：从用户示范生成可复用 agent 工作流；核心思想是把示范过程蒸馏为 workflow artifact，供 agent 回放、适配和复用。
- [PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction](https://arxiv.org/abs/2510.15863): 通过把技能的抽象目标与具体实现解耦，学习可泛化、可组合的 agent 技能，并提升跨网站复用能力。
- [Alita-G: Self-Evolving Generative Agent for Agent Generation](https://arxiv.org/abs/2510.23601)：通过从轨迹生成、抽象和筛选 MCP 工具，把通用 agent 演化为领域专家。
- [Procedural Knowledge Improves Agentic LLM Workflows](https://arxiv.org/abs/2511.07568)：显式研究 procedural knowledge 对 agentic workflows 的增益，贴合 skill/procedural-knowledge harness 线。
- [Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory](https://arxiv.org/abs/2512.23760)：把通过 replay verifier、接口和 contract 检查的技能晋升到可审计 skill graph。
- [CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution](https://arxiv.org/abs/2512.23880): 提出可自我演化的累计 skill creation agent，通过 meta-skill、记忆巩固和 SciSkillBench 科学任务积累可执行技能。
- [Deploy-Master: Automating the Deployment of 50,000+ Agent-Ready Scientific Tools in One Day](https://arxiv.org/abs/2601.03513)：自动化部署大规模 agent-ready scientific tools。核心思想是减少人工封装成本，把大量科学工具转化为可部署 agent 能力。
- [Yunjue Agent](https://arxiv.org/abs/2601.18226)：面向开放任务的 zero-start in-situ self-evolving agent system。核心思想：把短期执行反馈沉淀为长期可复用能力，并把 tool evolution 作为扩展 agent 技能边界的关键路径。
- [CUA-Skill](https://arxiv.org/abs/2601.21123)（[项目页](https://microsoft.github.io/cua_skill/)）：面向 computer-use agents 的结构化 skill base 与 CUA-Skill Agent；核心思想：把 GUI 操作知识封装成带参数化执行和组合图的 skills，再通过检索、参数实例化和记忆化失败恢复调用。
- [AutoRefine](https://arxiv.org/abs/2601.22758)：面向持续 agent 的 trajectory-to-expertise harness。核心思想：把成功与失败轨迹蒸馏为可复用过程经验库，供后续运行检索和修订。
- [MemSkill](https://arxiv.org/abs/2602.02474)：面向自演化 agent 的 memory skill 学习与演化 harness。核心思想：把反复出现的记忆操作转成可选择、可更新并可跨任务携带的可复用 skill。
- [Agentic Proposing](https://arxiv.org/abs/2602.03279)：面向 agentic reasoning 的组合式 skill synthesis harness。核心思想：从子问题提出可复用 skill，使后续推理任务可以组合使用而不是从零开始。
- [Evolutionary Context Search](https://arxiv.org/abs/2602.16113)：基于 context search 的自动 skill acquisition harness。核心思想：演化候选上下文资源，并保留真正提升任务执行的内容，而不是只选择语义相似材料。
- [Agent Skill Framework: Perspectives on the Potential of Small Language Models in Industrial Environments](https://arxiv.org/abs/2602.16653)：讨论工业环境中小语言模型可用的 agent skill framework；核心思想是把工业操作包装成可复用 skill 能力，而不是依赖单次大模型调用。
- [SkillOrchestra](https://arxiv.org/abs/2602.19672)：skill-aware agent routing harness。核心思想：通过 skill transfer 路由 agents，把技能的可迁移性变成显式编排信号。
- [TARSE](https://arxiv.org/abs/2603.01241)：为 reasoning agents 检索 skills 与 experience 的 test-time adaptation harness。
  核心思想：在每个推理步骤选择可复用过程知识和先前经验，让 skill 复用成为在线适配的一部分。
- [AgentSkillOS](https://arxiv.org/abs/2603.02176)（[开源代码](https://github.com/ynulihao/AgentSkillOS)）：代表 skill retrieval + orchestration 的 OS 化路线；把 skill 调用拆成 `capability tree 检索 -> DAG 编排 -> artifact-rich 输出评测`。
  核心思想：在 200 到 200K skills 的生态规模下，比较“平铺直接调用”与“结构化检索 + DAG 组合”；论文同时给出 30 个跨五类的 artifact-rich 任务，说明 skill 调用的关键不只是找到 skill，而是把多 skill 组织成可执行 pipeline。
- [EvoSkill](https://arxiv.org/abs/2603.02766)：面向多 agent system 的自动 skill discovery harness。核心思想：从经验中演化可复用工作流和代码级 skill，使 agent 随时间扩展能力库。
- [ToolRosella](https://arxiv.org/abs/2603.09290)：面向科学 agent 的 repository-to-tool 转换 harness。核心思想：把已有代码仓库转成标准化可调用工具，避免 agent 在运行时临时摸索接口。
- [XSkill](https://arxiv.org/abs/2603.12056)：持续学习型多模态 agent skill harness。核心思想：同时保留视觉 experience 与结构化 reusable skill，让后续任务既能利用 episodic evidence，也能利用程序性抽象。
- [Memento-Skills](https://arxiv.org/abs/2603.18743)（[开源代码](https://github.com/Memento-Teams/Memento-Skills)）：把 reusable skills 当作持久化、可演化 memory 的 generalist agent 系统。
  核心思想：通过 read-write reflective learning 选择、更新和扩展 Markdown skill 文件，让 agent 在不更新模型参数的情况下持续改造 task-specific agents。
- [Semantic Tool Discovery for Large Language Models: A Vector-Based Approach to MCP Tool Selection](https://arxiv.org/abs/2603.20313)：用基于向量的语义发现选择 MCP 工具，补足原始工具与可复用技能之间的技能选择层。
- [ContractSkill](https://arxiv.org/abs/2603.20340)：面向多模态网页 agent 的可修复契约式 skill harness。核心思想：把 skill 绑定到显式 contract，使调用、失败诊断和修复成为 skill 生命周期的一部分。
- [SkillClone: Multi-Modal Clone Detection and Clone Propagation Analysis in the Agent Skill Ecosystem](https://arxiv.org/abs/2603.22447)：研究 agent skill ecosystem 中的多模态克隆检测与传播分析；核心思想是识别复制或传播的 skill，支持 skill library 的治理与审计。
- [SkillRouter](https://arxiv.org/abs/2603.22455)：面向 LLM agent 的大规模 skill routing harness。核心思想：在生态规模下把请求路由到相关 skill，使 agent 不必把所有 skill 描述塞进上下文。
- [D2Skill](https://arxiv.org/abs/2603.28716)：面向 agentic reinforcement learning 的动态双粒度 skill bank。核心思想：从经验中维护 task-level 和 step-level skills，按 hindsight utility 检索与剪枝，并在后续 rollout 中注入这些 skills 以复用 agent 行为。
- [SkillReducer](https://arxiv.org/abs/2603.29919)：面向 LLM-agent skill 的 token-efficiency harness。核心思想：压缩 skill 描述，同时保留可执行性、选择质量和有效指导。
- [AdaSkill](https://arxiv.org/abs/2604.01608)：判断何时可用单个 skill-augmented agent 替代 multi-agent system 的 skill distillation harness。
  核心思想：只有在 metric-free 诊断显示蒸馏有益时，才从多代理轨迹中抽取工具、知识和结构。
- [CoEvoSkills](https://arxiv.org/abs/2604.01687)：面向 self-evolving agent skill 的协同演化验证 harness。核心思想：让 agent 构造多文件可复用 skill，并通过任务与 skill 实现的配对演化进行验证。
- [SkVM](https://arxiv.org/abs/2604.03088)（[开源代码](https://github.com/SJTU-IPADS/SkVM)）：skill 编译与运行时；核心思想：把 skill 当可编译工件做能力绑定、并发抽取和 JIT 固化，提升跨 harness 可移植性。
- [SkillFoundry](https://arxiv.org/abs/2604.03964)（[开源代码](https://github.com/ma-compbio-lab/SkillFoundry)）：从异构科学/工程资源中构建自演化 skill libraries。
  核心思想：把文档、仓库、脚本、notebooks、数据库和论文中的 procedural knowledge 抽取成带输入输出、执行步骤、环境假设、来源和测试的 skill packages，再闭环扩展、修复、合并和剪枝。
  核心思想：把轨迹蒸馏成战略计划、功能技能和原子技能三层结构，并通过执行反馈迭代修正和主动扩展技能覆盖。
- [Graph of Skills](https://arxiv.org/abs/2604.05333)（[开源代码](https://github.com/davidliuk/graph-of-skills)）：依赖感知的 skill 结构检索；核心思想：把扁平 skill 列表改成带前置关系的结构化上下文，减少盲选。
- [SkillClaw](https://arxiv.org/abs/2604.08377)：面向 OpenClaw 式 agent 的集体 skill 演化 harness。核心思想：根据跨用户工作流的成功与失败更新共享的已部署 skill。
- [SkillForge](https://arxiv.org/abs/2604.08618)：面向云技术支持的领域自演化 skill-forging harness。核心思想：从领域轨迹生成、测试并修订支持 skill，使 skill 随运营反馈改进。
- [SkillMOO](https://arxiv.org/abs/2604.09297)：面向软件工程 agent skill 的多目标优化 harness。核心思想：优化 skill bundle，同时平衡任务成功率、token 成本和误导性指导风险。
- [Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents](https://arxiv.org/abs/2604.10674)：面向多轮 LLM agents 的 skill-conditioned self-distillation；核心思想是把蒸馏条件绑定到任务相关 skill 上，为长程 agent 提供更密集、可复用的监督。
- [WebXSkill](https://arxiv.org/abs/2604.13318)（[代码](https://github.com/aiming-lab/WebXSkill)）：web-agent skill-learning harness；核心思想是从网页轨迹中挖掘可复用动作片段，抽象成带自然语言指导的可执行参数化技能，并按 URL 上下文索引，在 grounded 或 guided 模式中调用。
- [Corpus2Skill](https://arxiv.org/abs/2604.14572)：面向企业 QA 与 RAG 的可导航 skill harness。核心思想：把语料蒸馏成层级 skill directory，让 agent 从摘要逐步导航到文档，而不是只消费一次性检索结果。
- [From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution](https://arxiv.org/abs/2604.15097)：补充skill use方向的agent harness，核心围绕《From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution》。
- [Bilevel Skill Optimization](https://arxiv.org/abs/2604.15709)：用 Monte Carlo Tree Search 优化 agent skill 的 harness。核心思想：联合搜索 skill 层选择和底层执行行为，使可复用 skill 能通过任务反馈改进。
- [AgentClick](https://arxiv.org/abs/2604.16520)：面向 terminal agent 的 skill-based human-in-the-loop review layer。核心思想：把高风险终端动作路由到 review skill，使人工批准成为执行工作流的一部分。
- [GraSP](https://arxiv.org/abs/2604.17870)：面向 LLM agent 的图结构 skill composition harness。核心思想：通过图结构组合聚焦 skill，使 agent 使用一致的 skill set，而不是依赖过载的扁平 prompt。
- [EvoAgent](https://arxiv.org/abs/2604.20133)：面向 skill learning 与 multi-agent delegation 的可演化 agent 框架。
  核心思想：把技能作为可学习、可复用单元，并根据演化中的技能状态在多代理之间委派任务。
- [Co-Evolving LLM Decision and Skill Bank Agents](https://arxiv.org/abs/2604.20987)：面向长程任务的 skill-bank harness。
  核心思想：让 decision agent 与 skill-bank agent 协同演化，使任务经验同时改造规划策略和可复用技能库存。
- [From Skills to Talent](https://arxiv.org/abs/2604.22446)：把异构 agent 组织成可移植的 Talents。核心思想：把 skills、tools 和 runtime configuration 打包成可招募的 agent 身份，再用 Explore-Execute-Review tree search 与 Talent Market 动态组装、执行并改进多代理组织。
- [RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents](https://arxiv.org/abs/2604.22888)：在执行前检测 skill poisoning；核心思想是用 response-conditioned attention 与 hidden-state alignment 信号识别合法 skill 中隐藏的恶意片段。
- [ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation](https://arxiv.org/abs/2604.23853)：ClawTrace 关注 skill distillation 的 tracing 成本和轨迹保留，适合 Skill Use harness。
- [From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills](https://arxiv.org/abs/2604.24026)：该工作把 skill text 转换为 scheduling-structural-logical representation，直接属于 skill-use harness。
- [Skill Retrieval Augmentation for Agentic AI](https://arxiv.org/abs/2604.24594)：面向 agentic AI 的 skill-retrieval augmentation 框架。核心思想是在运行时检索相关 skills，使 agent 能按当前任务调整能力集合。
- [Structured Security Auditing and Robustness Enhancement for Untrusted Agent Skills](https://arxiv.org/abs/2604.25109)：面向不可信 agent skill 的安全审计 harness。核心思想是在 agent 执行第三方 skill 前进行结构化检查与加固。
- [Skills-Coach: A Self-Evolving Skill Optimizer via Training-Free GRPO](https://arxiv.org/abs/2604.27488)：在不改动任务模型的情况下优化可复用 agent skill，提升 skill 覆盖与可靠性。
- [Ctx2Skill](https://arxiv.org/abs/2604.27660)：通过 Challenger、Reasoner 和 Judge 的自博弈，在没有人工 skill 标注和外部反馈的情况下构造上下文特定技能；失败案例会被转成定向 skill 更新，使长篇技术上下文能沉淀为可复用过程。
- [Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis](https://arxiv.org/abs/2605.00314)：通过 constraint-guided representation synthesis 审计 agent skills；核心思想是在 agent 复用 skill 之前检查其行为是否满足约束。
- [Neuro-Symbolic Skill Induction](https://arxiv.org/abs/2605.01293)：面向长程 agent 的程序化技能归纳框架。核心思想是把交互轨迹提升为带显式控制流、变量绑定和触发条件的逻辑化程序技能。
- [HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness](https://arxiv.org/abs/2605.02396)：把 heavy thinking 作为 agentic harness 的内部技能；核心思想是把深度推理流程封装成可按需调用的可复用技能。
- [FitText: Evolving Agent Tool Ecologies via Memetic Retrieval](https://arxiv.org/abs/2605.02411)：FitText 关注 agent tool ecologies 的 memetic retrieval 与演化，属于 skill/tool harness。
- [SkCC](https://arxiv.org/abs/2605.03353)：跨框架 skill 编译与安全加固；核心思想：用强类型中间表示 SkIR 解耦 Markdown skill 的语义与不同 agent framework 的提示格式，同时把权限、安全检查和可移植性纳入编译流程。
- [Sealing the Audit-Runtime Gap for LLM Skills](https://arxiv.org/abs/2605.05274)：封闭 LLM skills 的 audit-runtime gap；核心思想是把已审计 skill artifact 绑定到防篡改 registry 与可验证托管路径，确保运行时内容与批准内容一致。
- [From History to State: Constant-Context Skill Learning for LLM Agents](https://arxiv.org/abs/2605.05413)：Agent Harness 条目；核心思想：从交互历史中进行常量上下文技能学习；核心思想是把长 agent 轨迹转化为可复用状态和技能，而不扩张提示。
- [SkillScope](https://arxiv.org/abs/2605.05868)：面向 agent skills 的最小权限执行层。核心思想：对每个 skill 的权限做细粒度作用域限定，并在执行时强制检查，避免可复用 skill 静默扩大 agent 权限。
- [SkillOS](https://arxiv.org/abs/2605.06614)：面向 self-evolving agent 的 skill curation harness。核心思想：把冻结的技能检索与执行 agent 同可训练 curator 配对，由 curator 根据累积经验更新外部 SkillRepo，并用任务流中的延迟奖励学习长期技能维护策略。
- [Group of Skills: Group-Structured Skill Retrieval for Agent Skill Libraries](https://arxiv.org/abs/2605.06978)：Group of Skills 将 agent skill retrieval 做成组结构检索，适合 Skill Use harness。
- [SkillLens](https://arxiv.org/abs/2605.08386)：层次化 skill 复用与演化框架；核心思想：把 skills 组织成 policy、strategy、procedure 与 primitive 四层，在混合粒度上检索，并只重写局部不匹配的 subskills，以降低上下文与适配成本。
- [CoCoDA: Co-evolving Compositional DAG for Tool-Augmented Agents](https://arxiv.org/abs/2605.08399)：CoCoDA 共同演化 compositional DAG 与工具库，属于 tool/skill-augmented agent harness。
- [Skill-CMIB: Multimodal Agent Skill for Consistent Action via Conditional Multimodal Information Bottleneck](https://arxiv.org/abs/2605.08526)：类型：skill 机制或技能生成/编排框架。核心价值：补充 agent skill 的发现、生成、选择或组合机制，突出可复用能力沉淀。
- [MIND-Skill: Quality-Guaranteed Skill Generation via Multi-Agent Induction and Deduction](https://arxiv.org/abs/2605.08670)：类型：skill 机制或技能生成/编排框架。核心价值：补充 agent skill 的发现、生成、选择或组合机制，突出可复用能力沉淀。
- [SkillMaster](https://arxiv.org/abs/2605.08693)：自主 skill mastery 框架。
  核心思想：打通技能创建、修订和选择闭环，让 LLM agent 维护可复用能力，而不是只消费固定技能列表。
- [AgentPSO](https://arxiv.org/abs/2605.08704)（[开源代码](https://github.com/HYUNMIN-HWANG/AgentPSO/)）：用于演化 reasoning skill 的多智能体粒子群框架。核心思想：把每个 agent 的自然语言技能视为粒子状态，并结合个体最优、全局最优和同伴轨迹方向更新技能，使技能能在任务和骨干模型之间迁移而不更新参数。
- [Ace-Skill: Bootstrapping Multimodal Agents with Prioritized and Clustered Evolution](https://arxiv.org/abs/2605.08887)：面向面向多模态 agent 的优先级与聚类式技能演化的 harness；核心思想是把规划、工具调用、记忆、验证、环境交互或编排逻辑外置到模型之外。
- [SearchSkill: Teaching LLMs to Use Search Tools with Evolving Skill Banks](https://arxiv.org/abs/2605.09038)：用 evolving skill banks 教 LLM 使用搜索工具；核心思想是积累可复用搜索技能，而不是依赖一次性提示。
- [SPARK](https://arxiv.org/abs/2605.09192)（[开源代码](https://github.com/EtaYang10th/spark-skills)）：structured pipelines for autonomous runnable tasks；核心思想：把任务完成后的经验压缩成可运行技能流程，强调 posterior skill formation 与后续复用。
- [SkillMAS](https://arxiv.org/abs/2605.09341)：面向多 agent 系统的后部署 skill 演化 harness；核心思想：从可验证轨迹中做信用分配，在受控增长下更新可复用 procedures，并在失败暴露角色与 skill 不匹配时重构 agent 组织。
- [SkillRAE](https://arxiv.org/abs/2605.10114)：skill-based context compilation for retrieval-augmented execution；核心思想：把检索到的 skills 编译成紧凑、grounded、可执行的上下文，而不是直接把一组 Markdown skill 原文塞给 agent。
- [SkillEvolver](https://arxiv.org/abs/2605.10500)：online skill learning meta-skill；核心思想：把“写、部署、失败后修订 domain skill”的流程本身封装成 meta-skill，用 fresh-agent audit 避免只在当前 agent 上过拟合。
- [AI Workflow Store](https://arxiv.org/abs/2605.10907)：面向稳健个人 agent 的 workflow store 基础设施。核心思想：把可复用工作流封装成可检索、可改写、可执行的过程资产，使 agent 不必在每次会话中从零生成脆弱计划。
- [SLIM](https://arxiv.org/abs/2605.10923)：面向 agentic reinforcement learning 的动态 skill lifecycle management 框架。核心思想：估计每个外部技能的边际贡献，并在策略学习过程中动态加入、退休或合并技能，而不是假设技能只会单调累积或最终在推理时消失。
- [Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries](https://arxiv.org/abs/2605.10990)：Skill Drift 将 skill 库维护建模为 contract violation，适合 Skill Use 的维护 harness。
- [SkillGen](https://arxiv.org/abs/2605.10999)：带验证的 inference-time agent skill synthesis。
  核心思想：在推理时从轨迹中合成可审计的可复用技能，并把 verification 纳入技能生成流程。
- [Behavioral Integrity Verification for AI Agent Skills](https://arxiv.org/abs/2605.11770)：验证 AI agent skills 的声明能力与实际能力；核心思想是结合确定性代码分析和 LLM 辅助能力抽取，对描述-实现偏差分类。
- [CTA / Counterfactual Trace Auditing](https://arxiv.org/abs/2605.11946)：skill 影响的轨迹级审计框架；核心思想：把有 skill 与无 skill 的同任务轨迹分段对齐，标注 skill influence pattern，补足只看 pass rate 难以发现的行为改变。
- [SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs](https://arxiv.org/abs/2605.12039)：基于 evolving skill graphs 的 skill-augmented agent-learning harness。核心思想：把可复用 skill 表示为带依赖关系的图，而不是孤立语义条目，使 agent 能为组合任务检索、组合并维护 skill。
- [No Attack Required: Semantic Fuzzing for Specification Violations in Agent Skills](https://arxiv.org/abs/2605.13044)：用于发现 agent skills 规格违反的 semantic fuzzing framework；核心思想是把每条 skill guardrail 转成执行轨迹上的可达性检查，搜索能破坏声明契约的良性输入。
- [RS-Claw: Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents](https://arxiv.org/abs/2605.13391)：类型：skill 机制或技能生成/编排框架。核心价值：补充 agent skill 的发现、生成、选择或组合机制，突出可复用能力沉淀。
- [MMSkills](https://arxiv.org/abs/2605.13527)：面向视觉 agent 的多模态 skill 表示与调用框架；核心思想：把 procedure、状态卡和多视角关键帧封装成可复用 skill，从轨迹中生成后在临时分支中对齐现场环境，再压缩成主 agent 可用的执行指导。
- [SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems](https://arxiv.org/abs/2605.13716)：把 agent skill library 视为可自维护的软件生态；核心思想是识别并修复技能检索、组合、依赖漂移和长期复用中的 skill technical debt。
- [SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration](https://arxiv.org/abs/2605.14089)：SkillFlow 2605 版聚焦递归 skill evolution 与 orchestration，适合 Skill Use Agent Harness。
- [EvoLib](https://arxiv.org/abs/2605.14477)：带有自演化技能库和反思知识的 test-time learning harness。核心思想：从 agent 自身轨迹中抽取抽象经验，按即时价值和长期价值进行加权与合并，并在后续问题实例中复用而不更新参数。
- [SkillsVote](https://arxiv.org/abs/2605.18401)：面向外部 agent skill library 的治理框架。核心思想是先分析开放技能的环境要求与可验证性，执行前检索结构化技能上下文，再把轨迹结果归因到技能使用、探索和环境因素，并只把成功且可复用的发现通过证据门控写回技能库。
- [MASA / Model-Aware Skill Alignment](https://arxiv.org/abs/2605.30723)：在不改变模型权重的情况下，把程序性 skill 对齐到不同 agent backbone。核心思想：结合 skill evolution 与 model-conditioned skill rewriter，使同一能力可适配不同 agent 模型的执行习惯和失败模式。
- [Constraint-Consistent Skill Composition](https://doi.org/10.1109/ISBDAS69350.2026.11484408)：面向可靠性的 skill composition harness。
  核心思想：用一致性约束来组合技能，使 zero-shot 任务泛化遵守约束条件，而不是机会式拼接技能。
- [Inducing Programmatic Skills for Agentic Tasks](https://openreview.net/forum?id=lsAY6fWsog)：为 agentic 任务归纳可执行程序化技能，把重复动作模式沉淀为可复用过程，而不是一次性提示。
- [SkillAdaptor](https://arxiv.org/abs/2606.01311)：在 step 粒度从失败轨迹中适配外部 skill。核心思想是定位第一个可行动故障步骤，把责任归因到候选 skill，并只接受通过显式检查的定向修改，使 training-free skill 维护不再依赖粗粒度的整段会话改写。
- [MMG2Skill](https://arxiv.org/abs/2606.01993)：把野外多模态指南编译成可编辑 agent skills，并用轨迹级 root-cause feedback 继续修订。核心思想是 raw human guides 可能反而损害执行，因此把结构化 skill 构造、VLM agent 条件化、轨迹诊断和 analyzer-based early stopping 分成闭环 harness。
- [Statistical Priors for Implicit Preferences](https://arxiv.org/abs/2606.05828)：把个人 agent skill selection 中的本地统计偏好学习与语义意图解析解耦。核心思想：用本地 preference harness 调制远程 LLM 的 skill 选择，在不把整个路由决策都塞进提示的情况下保留轻量个性化。
- [Workflow-to-Skill](https://arxiv.org/abs/2606.06893)：用 RWSA 中间表示把 demonstrations、agent trajectories、tool traces 和 execution logs 转成可执行 skill。核心思想是保留 workflow 结构、运行语义、附件、验证、安全、回滚和证据置信度，而不是把 trace-to-skill 当作普通摘要任务。
- [SKILL.nb](https://arxiv.org/abs/2606.08049)：通过 selective formalization 和 gated execution 治理 durable agent workflows。核心思想：把可复用 workflow 封装成可审计、可版本化的 notebook，并加入 validation gates、fallback paths、多模态证据和显式生命周期控制。
- [Bayesian-Agent](https://arxiv.org/abs/2606.08348)：用 posterior-guided harness actions 演化 reusable skills 和 SOPs。核心思想：把 skills 视为关于冻结模型成功率的假设，维护 feature-conditioned posterior，并据此触发 patch、split、compress、retire 或 explore。
- [SkillHone](https://arxiv.org/abs/2606.08671)：通过 persistent decision history 持续细化 agent skills。核心思想：结合 practice probes、role-separated subagents 和结构化 revision evidence，使 skill 更新能跨 session 保留，而不是停留在单次提示改写。
