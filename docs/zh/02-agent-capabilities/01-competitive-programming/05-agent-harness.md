# 2.1.5 Agent Harness

- [USACO Episodic + Semantic](https://arxiv.org/abs/2404.10952)（[开源代码](https://github.com/princeton-nlp/USACO)）：USACO 竞赛编程 agent 配置；核心思想是用 episodic memory 与语义检索复用相似题经验，支撑 Olympiad 风格长推理题的多步求解。
- [MapCoder](https://arxiv.org/abs/2405.11403)（[开源代码](https://github.com/Md-Ashraful-Pramanik/MapCoder)）：多代理竞赛代码生成框架；核心思想是把 retrieval、planning、coding 与 debugging 显式拆成多角色协作，逼近人类竞赛编程循环。
- [SolSearch: An LLM-Driven Framework for Efficient SAT-Solving Code Generation](https://arxiv.org/abs/2502.14328)：面向竞赛编程与求解智能体的智能体框架、工作流、协议、运行时或编排方法候选。价值在于把控制、工具使用、协作或验证机制做成可复用的智能体侧能力。
- [HoarePrompt](https://arxiv.org/abs/2503.19599)：一种自然语言程序验证 harness，通过描述可达状态并借鉴 k-induction 判断程序是否满足需求。
- [LogiCase: Effective Test Case Generation from Logical Description in Competitive Programming](https://arxiv.org/abs/2505.15039)：Agent Harness 条目；核心思想：从逻辑描述生成竞赛编程测试用例。
- [CodeContests+](https://arxiv.org/abs/2506.05817)：面向竞赛题的高质量测试用例生成与验证流程。核心思想：把“测试集构造”显式 agent 化，以提升评测的判别力与鲁棒性。
- [ALE-Agent](https://arxiv.org/abs/2506.09050)（[开源代码](https://github.com/SakanaAI/ALE-Bench)）：面向 AtCoder heuristic contest 的长时程算法工程 agent；核心思想是把代码修改、试跑反馈、可视化分析与分数优化接成持续迭代闭环。
- [Solve it with EASE](https://arxiv.org/abs/2509.18108)：可作为algorithmic coding and competitive programming方向的 Agent Harness 候选；标题/摘要显示其提供模型外部工作流、工具编排、反馈循环、记忆机制或多智能体执行框架。
- [Holistic Agent Leaderboard](https://arxiv.org/abs/2510.11977)（[开源代码](https://github.com/princeton-pli/hal-harness)）：跨 benchmark 的 agent 评测 harness；核心思想是把 USACO、SWE-bench、SWE-Lancer 等任务统一到可提交、可复现实验协议中。
- [AutoCode](https://arxiv.org/abs/2510.12803)：面向竞赛编程的自动出题、解题与验题流程；核心思想是把 LLM 组织成 problem setter、solver 与 verifier，用于持续生成 LiveCodeBench Pro 风格的可执行新题。
- [SwiftSolve](https://arxiv.org/abs/2510.22626)：多代理竞赛解题框架；核心思想：把规划、编码、profiling、复杂度分析分工，专门压 TLE/MLE。
- [Agentic Verifier](https://arxiv.org/abs/2602.04254)：面向竞赛代码的执行式 verifier 与 reranker；核心思想：通过多轮执行交互主动搜索能区分候选程序的反例输入，而不是只做随机测试采样。
- [CodeHacker](https://arxiv.org/abs/2602.20213)：面向竞赛提交的 adversarial test generation agent；核心思想：模拟竞赛平台的 hack 机制，结合压力测试、反哈希和逻辑定向构造，暴露弱测试放过的错误解。
- [RefineRL / Skeptical-Agent](https://arxiv.org/abs/2604.00790)：competitive-programming self-refinement harness，使用本地执行工具对 public tests 验证候选解，并在表面通过后仍保持 skeptical repair。
- [Sketch-and-Verify](https://arxiv.org/abs/2605.08658)：面向竞赛代码的测试时工作流；先生成多样化程序草图，再补全候选程序，通过执行验证和输出聚类选择结果。
- [Leveraging Symmetry in Multi-Agent Code Generation: A Cross-Verification Collaboration Protocol for Competitive Programming](https://doi.org/10.3390/sym17101660)：CVCP 针对多阶段竞赛代码生成中的语义漂移和弱测试问题，把对称性检测、对称性引导的对抗测试、round-trip review 与异步投票结合起来，在 CodeELO hard problems 上验证改进。
