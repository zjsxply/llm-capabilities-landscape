# 1.14.5 Agent Harness

- [Self-Refine](https://arxiv.org/abs/2303.17651)（[开源代码](https://github.com/madaan/self-refine)）：`生成 -> 反馈 -> 修订` 的通用写作修订 loop；适合把一次性写作改造成可审稿、可迭代的长文生成流程。
- [STORM](https://arxiv.org/abs/2402.14207)（[开源代码](https://github.com/stanford-oval/storm)）：面向长篇百科式写作的 `检索 -> 多视角提问 -> 大纲 -> 成稿` harness；更接近报告/综述型长文生成而不是单轮作文。
- [Heterogeneous Recursive Planning](https://arxiv.org/abs/2503.08275)（开源代码：未找到稳定公开仓库）：自适应长文写作规划 harness；核心思想：不只生成一次性大纲，而是递归拆分不同粒度的写作单元，并在生成过程中按内容需要调整规划深度。
- [BookWorld](https://arxiv.org/abs/2504.14538)：用于把小说构造成交互式 agent 社会以支持创意故事生成。核心思想：用角色 agent、社会模拟和故事世界状态，让叙事生成超出单轮写作。
- [A Hybrid Multi-Agent Prompting Approach for Simplifying Complex Sentences](https://arxiv.org/abs/2506.11681)：使用混合多智能体提示工作流进行句子简化与修订。
- [StoryWriter](https://arxiv.org/abs/2506.16445)（开源代码：未找到稳定公开仓库）：长篇故事生成多代理框架；核心思想：把角色设定、情节规划、章节写作和一致性检查拆给不同 agent，减少长故事中的人物漂移和情节断裂。
- [Auto-Slides](https://arxiv.org/abs/2509.11062)：用于创建和定制研究演示文稿的交互式多 agent harness。核心思想：把幻灯片生成、编辑和用户引导式修改拆给不同 agent 角色，使 presentation writing 成为可迭代的工件工作流，而不是一次性文本生成。
- [MUSE](https://arxiv.org/abs/2602.03028)：一个面向开放式故事构思的多智能体 harness。核心思想：用闭环认知编排协调规划、生成与修订角色，支持开放叙事发展。
- [PaperOrchestra](https://arxiv.org/abs/2604.05018)（开源代码：未找到稳定公开仓库）：自动 AI 研究论文写作的多代理框架；核心思想：把论文写作拆成 topic/context 分析、section drafting、交叉审阅和整体修订，对应 PaperWritingBench 的学术写作任务。
