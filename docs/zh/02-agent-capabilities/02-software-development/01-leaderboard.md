# 2.2.1 Leaderboard

- [SWE-bench Leaderboard](https://www.swebench.com/)：SWE-bench、Lite、Verified 与 Multilingual 等官方结果入口，是 repo-level issue resolving 最核心的持续榜单。
- [SWE-bench Multimodal Leaderboard](https://www.swebench.com/multimodal.html)：面向视觉/前端问题陈述与 JavaScript 软件库的官方榜单，用于观察 agent 是否能从文本 Python 修复泛化到多模态软件任务。
- [SWE-Lancer Diamond Leaderboard](https://swelancer.github.io/leaderboard/)：OpenAI SWE-Lancer 的公开 Diamond 榜单，强调真实 freelance-style 软件任务和更接近经济价值的交付评估。
- [SWE-rebench Leaderboard](https://swe-rebench.com/leaderboard)：面向去污染、交互式 SWE 任务的持续榜单，适合观察新鲜 GitHub issue 上的泛化与执行反馈利用。
- [SWE-bench-Live Leaderboard](https://swe-bench-live.github.io/)：持续从近期 GitHub issue/PR 生成任务的 live 榜单，重点降低静态 benchmark 被记忆或过拟合的风险。
- [SWE-MERA Leaderboard](https://mera-evaluation.github.io/demo-swe-mera/)：支持按任务采集时间窗口查看结果的动态榜单，适合做 contamination-aware 的时间切片对比。
- [CodeClash Leaderboard](https://codeclash.ai/)：目标导向、多轮锦标赛式软件工程榜单，适合评估 agent 的长期代码维护、日志分析与自发策略改进能力。
- [Holistic Agent Leaderboard](https://hal.cs.princeton.edu/)：跨任务 agent 榜单，覆盖 SWE-bench Verified、SWE-bench Multimodal、SWE-Lancer Diamond 等任务，适合比较不同 agent harness 的通用性。
- [SWE-PolyBench Leaderboard](https://amazon-science.github.io/SWE-PolyBench/)：多编程语言 repository-level coding agent 榜单；价值在于提供数据、容器化评测和公开排名，补齐非 Python 代码代理评测。
- [Multi-SWE-Bench Leaderboard](https://multi-swe-bench.github.io/)：多编程语言真实 issue 修复榜单；这里的 multilingual 指编程语言，适合作为多语言 coding agent 评测的公开榜单参照。
- [Copilot Arena](https://gclef-cmu.org/research/2025copilotarena/)：真实 IDE 使用中的代码模型偏好 arena；价值在于补齐 SWE-bench 式离线测试通过率之外的开发者偏好、交互上下文和 in-the-wild 使用信号。
- [Aider Polyglot Leaderboard](https://aider.chat/docs/leaderboards/)：实践型多编程语言代码编辑榜单；虽然不是论文型基准，但任务和实现公开，适合快速比较多语言代码编辑能力。
