# 2.1.4 Agent Harness

- [USACO Episodic + Semantic](https://arxiv.org/abs/2404.10952)（[开源代码](https://github.com/princeton-nlp/USACO)）：USACO 竞赛编程 agent 配置；核心思想是用 episodic memory 与语义检索复用相似题经验，支撑 Olympiad 风格长推理题的多步求解。
- [MapCoder](https://arxiv.org/abs/2405.11403)（[开源代码](https://github.com/Md-Ashraful-Pramanik/MapCoder)）：多代理竞赛代码生成框架；核心思想是把 retrieval、planning、coding 与 debugging 显式拆成多角色协作，逼近人类竞赛编程循环。
- [CodeContests+](https://arxiv.org/abs/2506.05817)：面向竞赛题的高质量测试用例生成与验证流程。核心思想：把“测试集构造”显式 agent 化，以提升评测的判别力与鲁棒性。
- [ALE-Agent](https://arxiv.org/abs/2506.09050)（[开源代码](https://github.com/SakanaAI/ALE-Bench)）：面向 AtCoder heuristic contest 的长时程算法工程 agent；核心思想是把代码修改、试跑反馈、可视化分析与分数优化接成持续迭代闭环。
- [Holistic Agent Leaderboard](https://arxiv.org/abs/2510.11977)（[开源代码](https://github.com/princeton-pli/hal-harness)）：跨 benchmark 的 agent 评测 harness；核心思想是把 USACO、SWE-bench、SWE-Lancer 等任务统一到可提交、可复现实验协议中。
- [AutoCode](https://arxiv.org/abs/2510.12803)：面向竞赛编程的自动出题、解题与验题流程；核心思想是把 LLM 组织成 problem setter、solver 与 verifier，用于持续生成 LiveCodeBench Pro 风格的可执行新题。
- [SwiftSolve](https://arxiv.org/abs/2510.22626)：多代理竞赛解题框架；核心思想：把规划、编码、profiling、复杂度分析分工，专门压 TLE/MLE。
- [Agentic Verifier](https://arxiv.org/abs/2602.04254)：面向竞赛代码的执行式 verifier 与 reranker；核心思想：通过多轮执行交互主动搜索能区分候选程序的反例输入，而不是只做随机测试采样。
- [CodeHacker](https://arxiv.org/abs/2602.20213)：面向竞赛提交的 adversarial test generation agent；核心思想：模拟竞赛平台的 hack 机制，结合压力测试、反哈希和逻辑定向构造，暴露弱测试放过的错误解。
