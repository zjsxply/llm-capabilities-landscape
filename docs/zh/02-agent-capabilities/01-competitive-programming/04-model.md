# 2.1.4 Model

- [AlphaCode](https://arxiv.org/abs/2203.07814)：竞赛代码生成的里程碑模型系统，使用大规模代码预训练、海量采样、过滤、聚类和排序求解 Codeforces 风格题目。
- [Whodunit: Classifying Code as Human Authored or GPT-4 generated- A case study on CodeChef problems](https://arxiv.org/abs/2403.04013)：补充竞赛编程方向的模型侧工作，包括训练、架构、后训练、合成数据、奖励或验证器、世界模型等机制。
- [ACECODER](https://arxiv.org/abs/2502.01718)：通过自动合成测试用例提供可执行奖励，用强化学习训练代码模型。
- [rStar-Coder](https://arxiv.org/abs/2505.21297)：用大规模可验证数据集和训练流程扩展竞赛代码推理，面向带可执行测试的高难题。
- [ReVeal](https://arxiv.org/abs/2506.11442)：优化代码 agent 的可靠自验证行为，而不是只依赖最终结果奖励。
- [Teaching LLM to Reason: Reinforcement Learning from Algorithmic Problems without Code](https://arxiv.org/abs/2507.07498)：该方法从算法问题中训练 LLM 推理能力，而不依赖代码执行。
- [CodeRL+](https://arxiv.org/abs/2510.18471)：用执行语义对齐代码生成强化学习，缩小文本似然目标与功能正确性之间的差距。
- [AlphaCode 2 Technical Report](https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf)：围绕 Gemini 时代推理能力升级竞赛编程模型流程，重点在大规模生成、搜索、过滤和打分。
- [DRIVE: Data Curation Best Practices for Reinforcement Learning with Verifiable Reward in Competitive Code Generation](https://arxiv.org/abs/2511.06307)：总结竞争性代码生成中基于可验证奖励强化学习的数据策划实践。
- [Scaling Reasoning Tokens via RL and Parallel Thinking: Evidence From Competitive Programming](https://arxiv.org/abs/2604.01302)：通过强化学习训练与 parallel thinking 扩展竞赛编程的推理 token 预算。
- [GrandCode](https://arxiv.org/abs/2604.02721)：用 agentic reinforcement learning 与 Agentic GRPO 改进假设提出、求解、测试生成和总结等竞赛编程模块。
- [When Independent Sampling Outperforms Agentic Reasoning](https://arxiv.org/abs/2605.08478)：表明在固定成本下重复独立采样可超过 Codeforces 上的 agentic reasoning，为竞赛编程智能体提供强基线。
- [Solvita: Enhancing Large Language Models for Competitive Programming via Agentic Evolution](https://arxiv.org/abs/2605.15301)：把静态多代理解题改成可积累经验的竞赛编程 harness。核心思想是由 Planner、Solver、Oracle、Hacker 分工，并给每个角色配可训练的图结构知识网络，用通过/失败 verdict、测试认证质量和 Hacker 找到的对抗漏洞更新后续路由。
