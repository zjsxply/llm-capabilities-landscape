# 1.14.4 Agent Harness

- [Self-Refine](https://arxiv.org/abs/2303.17651)（[开源代码](https://github.com/madaan/self-refine)）：`生成 -> 反馈 -> 修订` 的通用写作修订 loop；适合把一次性写作改造成可审稿、可迭代的长文生成流程。
- [Weaver](https://arxiv.org/abs/2401.17268)（开源代码：未找到稳定公开仓库）：创意写作 foundation model 与写作流程参考；虽然更偏模型工作，但它系统化处理设定、情节和叙事风格，是后续创意写作 agent 评测的重要基线。
- [STORM](https://arxiv.org/abs/2402.14207)（[开源代码](https://github.com/stanford-oval/storm)）：面向长篇百科式写作的 `检索 -> 多视角提问 -> 大纲 -> 成稿` harness；更接近报告/综述型长文生成而不是单轮作文。
- [LongWriter](https://arxiv.org/abs/2408.07055)（[开源代码](https://github.com/THUDM/LongWriter)）：长文本生成与扩展写作框架；核心思想是把超长输出拆成可控扩展和分段生成过程，适合作为长文输出稳定性的工程参考。
- [Heterogeneous Recursive Planning](https://arxiv.org/abs/2503.08275)（开源代码：未找到稳定公开仓库）：自适应长文写作规划 harness；核心思想：不只生成一次性大纲，而是递归拆分不同粒度的写作单元，并在生成过程中按内容需要调整规划深度。
- [BookWorld](https://arxiv.org/abs/2504.14538)：用于把小说构造成交互式 agent 社会以支持创意故事生成。核心思想：用角色 agent、社会模拟和故事世界状态，让叙事生成超出单轮写作。
- [Writing-Zero](https://arxiv.org/abs/2506.00103)（[开源代码](https://github.com/damoonsh/writing-zero)）：把非可验证写作任务转成可优化的 reward 流程；核心思想是用过程化反馈和可检查约束缩小主观写作质量与可训练信号之间的距离。
- [StoryWriter](https://arxiv.org/abs/2506.16445)（开源代码：未找到稳定公开仓库）：长篇故事生成多代理框架；核心思想：把角色设定、情节规划、章节写作和一致性检查拆给不同 agent，减少长故事中的人物漂移和情节断裂。
- [LongWriter-Zero](https://arxiv.org/abs/2506.18841)（开源代码：未找到稳定公开仓库；[数据集](https://huggingface.co/datasets/THU-KEG/Arena-Write)）：面向超长写作的 RL 框架；核心思想是用 `think before writing`、长度/质量 reward 和 Arena-Write 评测，让模型在 1 万词级输出中保持结构和连贯性。
- [ACE-RL](https://arxiv.org/abs/2509.04903)（开源代码：未找到稳定公开仓库）：WritingBench 引文网络中的代表性后续工作；核心思想：自动把写作指令分解为细粒度约束，并用约束满足度作为长文生成 RL reward，属于训练型写作系统而非纯交互式 agent。
- [Auto-Slides](https://arxiv.org/abs/2509.11062)：用于创建和定制研究演示文稿的交互式多 agent harness。核心思想：把幻灯片生成、编辑和用户引导式修改拆给不同 agent 角色，使 presentation writing 成为可迭代的工件工作流，而不是一次性文本生成。
- [MUSE](https://arxiv.org/abs/2602.03028)：一个面向开放式故事构思的多智能体 harness。核心思想：用闭环认知编排协调规划、生成与修订角色，支持开放叙事发展。
- [HiFlow](https://arxiv.org/abs/2603.04996)（开源代码：未找到稳定公开仓库）：约束长文生成的层级反馈优化框架；核心思想：按全局结构、段落质量和局部约束分层反馈，迭代修复长文中的约束遗漏和结构失衡。
- [PaperOrchestra](https://arxiv.org/abs/2604.05018)（开源代码：未找到稳定公开仓库）：自动 AI 研究论文写作的多代理框架；核心思想：把论文写作拆成 topic/context 分析、section drafting、交叉审阅和整体修订，对应 PaperWritingBench 的学术写作任务。
