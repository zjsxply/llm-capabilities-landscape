# 1.13.4 Model

- [Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills](https://arxiv.org/abs/2402.03244)：从高奖励子轨迹中抽取子目标和指令，再剪除持续低效的技能，使 LLM actor 能在 NetHack 与 ScienceWorld 中通过上下文技能集改进行为。
- [Merge to Learn: Efficiently Adding Skills to Language Models with Model Merging](https://arxiv.org/abs/2410.12937)：先并行训练面向新技能的专门模型，再用 task-vector 式模型合并并回通用模型，降低反复重训新技能数据集的成本和遗忘风险。
- [From f(x) and g(x) to f(g(x))](https://arxiv.org/abs/2509.25123)：用合成字符串变换任务控制原子技能与组合技能，证明强化学习能让 LLM 学会未见过的技能组合，并把这种组合能力迁移到新任务。
- [Improving Procedural Skill Explanations via Constrained Generation: A Symbolic-LLM Hybrid Architecture](https://arxiv.org/abs/2511.20942)：Ivy 用 Task-Method-Knowledge 结构约束 LLM 生成，使程序性教学回答保留因果转移、目标层级和问题分解。
- [Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis](https://arxiv.org/abs/2601.03676)：STEPS 用结构信息理论构建层级技能 taxonomy，并通过受约束的信息最大化合成更难的技能组合数据用于后训练。
- [RAGShaper: Eliciting Sophisticated Agentic RAG Skills via Automated Data Synthesis](https://arxiv.org/abs/2601.08699)：通过数据合成诱导可复用的智能体 RAG 技能，将技能习得与检索工作流连接起来。
- [Skill-Pro](https://arxiv.org/abs/2602.01869)：从 episodic experience 中学习带显式激活、执行和终止条件的可复用程序性技能。
- [SkillRL](https://arxiv.org/abs/2602.08234)（[开源代码](https://github.com/aiming-lab/SkillRL)）：通过 recursive skill-augmented reinforcement learning 演化 agent，使 SkillBank 与 agent policy 共同演化。
- [AutoSkill](https://arxiv.org/abs/2603.01145)：通过 experience-driven lifelong skill self-evolution，从交互轨迹中抽取、维护并复用技能。
- [Trace2Skill](https://arxiv.org/abs/2603.25158)：通过并行轨迹分析与分层整合，把局部轨迹经验蒸馏成可迁移 agent skills。
- [SKILL0](https://arxiv.org/abs/2604.02268)：使用 in-context agentic reinforcement learning 内化技能，降低推理时对外部 skill 文本的依赖。
- [SkillX](https://arxiv.org/abs/2604.04804)（[开源代码](https://github.com/zjunlp/SkillX)）：从强 agent 轨迹中构建可复用 skill knowledge base，组织 strategy、functional skill 和 atomic skill 以支持迁移。
- [Skill Neologisms](https://arxiv.org/abs/2605.04970)：学习可组合的 soft skill tokens，而不更新模型权重，使 skill acquisition 成为模型侧 continual-learning 机制，而不只是外部 skill library。
- [Skill1](https://arxiv.org/abs/2605.06130)：通过强化学习训练统一 policy 来选择、使用并蒸馏技能。
- [Skill-R1: Agent Skill Evolution via Reinforcement Learning](https://arxiv.org/abs/2605.09359)：训练轻量 skill 生成器，根据 rollout 结果与可验证奖励迭代修订可复用 skill。
- [ReuseRL / Skill Reuse as Compression](https://arxiv.org/abs/2605.31509)：把 agentic reinforcement learning 中的 skill reuse 表述为压缩目标。核心思想：用 MDL-style skill dictionary 和 segmentation cost 正则化轨迹，并在 ALFWorld、TextWorld-Cooking 与 Countdown-Stepwise 上验证可复用 skill 如何塑造策略学习。
