# 1.13.5 Agent Harness

- [SkillFlow](https://arxiv.org/abs/2504.06188)：多阶段 agent skill retrieval pipeline；核心思想：把 skill acquisition 建模成信息检索，在约 36K 个社区 `SKILL.md` 定义上串联 dense retrieval、cross-encoder reranking 和 LLM selection。
- [COALESCE](https://arxiv.org/abs/2506.01900)：研究自治 LLM agent 团队中基于技能的任务外包所带来的经济与安全动态。核心思想是把技能委托建模为类似市场的协作问题，考察 agent 如何在成本、信任和对抗风险之间选择是否外包能力。
- [CUA-Skill](https://arxiv.org/abs/2601.21123)（[项目页](https://microsoft.github.io/cua_skill/)）：面向 computer-use agents 的结构化 skill base 与 CUA-Skill Agent；核心思想：把 GUI 操作知识封装成带参数化执行和组合图的 skills，再通过检索、参数实例化和记忆化失败恢复调用。
- [SkillOrchestra](https://arxiv.org/abs/2602.19672)：skill-aware agent routing harness。核心思想：通过 skill transfer 路由 agents，把技能的可迁移性变成显式编排信号。
- [TARSE](https://arxiv.org/abs/2603.01241)：为 reasoning agents 检索 skills 与 experience 的 test-time adaptation harness。
  核心思想：在每个推理步骤选择可复用过程知识和先前经验，让 skill 复用成为在线适配的一部分。
- [AgentSkillOS](https://arxiv.org/abs/2603.02176)（[开源代码](https://github.com/ynulihao/AgentSkillOS)）：代表 skill retrieval + orchestration 的 OS 化路线；把 skill 调用拆成 `capability tree 检索 -> DAG 编排 -> artifact-rich 输出评测`。
  核心思想：在 200 到 200K skills 的生态规模下，比较“平铺直接调用”与“结构化检索 + DAG 组合”；论文同时给出 30 个跨五类的 artifact-rich 任务，说明 skill 调用的关键不只是找到 skill，而是把多 skill 组织成可执行 pipeline。
- [XSkill](https://arxiv.org/abs/2603.12056)：持续学习型多模态 agent skill harness。核心思想：同时保留视觉 experience 与结构化 reusable skill，让后续任务既能利用 episodic evidence，也能利用程序性抽象。
- [Memento-Skills](https://arxiv.org/abs/2603.18743)（[开源代码](https://github.com/Memento-Teams/Memento-Skills)）：把 reusable skills 当作持久化、可演化 memory 的 generalist agent 系统。
  核心思想：通过 read-write reflective learning 选择、更新和扩展 Markdown skill 文件，让 agent 在不更新模型参数的情况下持续改造 task-specific agents。
- [Semantic Tool Discovery for Large Language Models: A Vector-Based Approach to MCP Tool Selection](https://arxiv.org/abs/2603.20313)：用基于向量的语义发现选择 MCP 工具，补足原始工具与可复用技能之间的技能选择层。
- [AdaSkill](https://arxiv.org/abs/2604.01608)：判断何时可用单个 skill-augmented agent 替代 multi-agent system 的 skill distillation harness。
  核心思想：只有在 metric-free 诊断显示蒸馏有益时，才从多代理轨迹中抽取工具、知识和结构。
- [SkVM](https://arxiv.org/abs/2604.03088)（[开源代码](https://github.com/SJTU-IPADS/SkVM)）：skill 编译与运行时；核心思想：把 skill 当可编译工件做能力绑定、并发抽取和 JIT 固化，提升跨 harness 可移植性。
- [SkillFoundry](https://arxiv.org/abs/2604.03964)（[开源代码](https://github.com/ma-compbio-lab/SkillFoundry)）：从异构科学/工程资源中构建自演化 skill libraries。
  核心思想：把文档、仓库、脚本、notebooks、数据库和论文中的 procedural knowledge 抽取成带输入输出、执行步骤、环境假设、来源和测试的 skill packages，再闭环扩展、修复、合并和剪枝。
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
