# 2.1 竞赛编程

> 上级章节：2. 基础 Agent


## 2.1.1 Leaderboard

- [LiveCodeBench Leaderboard](https://livecodebench.github.io/leaderboard.html)：持续更新的代码生成公开榜单，适合作为抗污染 coding model/agent 横向对比入口。
- [CodeElo Leaderboard](https://codeelo-bench.github.io/)：把竞赛编程正确性转成 Elo 风格排序，适合观察不同模型在同一竞赛题协议下的相对强弱。
- [ALE-Bench Leaderboard](https://sakanaai.github.io/ALE-Bench-Leaderboard/)：面向 AtCoder heuristic/algorithm engineering 的长时程分数榜，能直接暴露 agent 是否能持续迭代优化而非一次性提交。
- [LiveCodeBench Pro Leaderboard](https://livecodebenchpro.com/)：LiveCodeBench 的高难竞赛题扩展榜，适合追踪 frontier coding agent 在更强判题压力下的上限。
- [Humanity's Last Code Exam Leaderboard](https://humanity-s-last-code-exam.github.io/website/)：以 ICPC World Finals 与 IOI 难题为核心的极难竞赛编程榜单，适合观察上限差距。
- [Holistic Agent Leaderboard](https://hal.cs.princeton.edu/)：跨任务 agent 榜单，包含 USACO 等编程子任务，并提供统一的 agent/harness 提交流程，适合把竞赛编程结果与其他 agent 任务一起比较。

## 2.1.2 Bench

- [HumanEval](https://arxiv.org/abs/2107.03374)：评什么：Python 函数级代码生成的可执行单元测试正确性。核心思想：用 docstring 提示和隐藏测试衡量 functional correctness，是后续代码生成评测与 pass@k 报告的基础参照。（[开源代码](https://github.com/openai/human-eval)）
- [CodeContests](https://github.com/google-deepmind/code_contests)：评什么：竞赛编程数据集与执行评测底座（题面、测试、正确/错误解等）。核心思想：把竞赛题落到可运行判题的格式，用于训练与评测更高难度的算法题代码生成。
- [LiveCodeBench v6](https://arxiv.org/abs/2403.07974)：评什么：持续更新、强调抗污染的代码评测（含来自竞赛平台的题源）。核心思想：用动态采样与污染控制提供更可信的“代码能力”对比基线。（[开源代码](https://github.com/LiveCodeBench/LiveCodeBench)）
- [USACO](https://arxiv.org/abs/2404.10952)：评什么：美国信息学奥林匹克题目上的竞赛编程推理与实现能力。核心思想：把题目、样例、隐藏测试与分级难度组织成可执行评测，用于观察 LLM 在 Olympiad-style programming 上的长程解题瓶颈。（[开源代码](https://github.com/princeton-nlp/USACO)）
- [CodeElo](https://arxiv.org/abs/2501.01257)：评什么：竞赛级代码生成的 Elo 风格可比对评分。核心思想：用更贴近“对战/排行”的评价协议，让模型表现具备更稳定的相对排序信号。
- [ProBench](https://arxiv.org/abs/2502.20868)：评什么：ICPC 启发的竞赛编程评测，题源来自 2024 年下半年的 Codeforces、洛谷和牛客。核心思想：用在线提交的真实判题结果、难度分层与算法标签，分析链式思考、错误类型和推理深度。
- [ICPC-Eval](https://arxiv.org/abs/2506.04894)（[开源代码](https://github.com/RUCAIBox/Slow_Thinking_with_LLMs)）：评什么：ICPC 风格竞赛题的推理与局部修复能力。核心思想：用更贴近真实 ICPC 场景的问题集和 Refine@K 评测，把多轮修正纳入指标。
- [ALE-Bench](https://arxiv.org/abs/2506.09050)：评什么：来自 AtCoder Heuristic Contest 的长时程、分数制算法工程任务。核心思想：从“AC/WA”转向连续得分和迭代优化，评估 agent 在路由、调度等无精确最优解问题上的长期试错能力。（[开源代码](https://github.com/SakanaAI/ALE-Bench)，[数据集](https://huggingface.co/datasets/SakanaAI/ALE-Bench)）
- [LiveCodeBench Pro](https://arxiv.org/abs/2506.11928)：评什么：更高难、以竞赛算法题为核心的污染控制代码生成评测。核心思想：在 LiveCodeBench 的动态题源思路上提高题目难度与判题强度，用于区分 frontier coding agent 的上限。（[开源代码](https://github.com/GavinZhengOI/LiveCodeBench-Pro)）
- [Humanity's Last Code Exam (HLCE)](https://arxiv.org/abs/2506.12713)：评什么：来自 ICPC World Finals 与 IOI 的极难题集合的可执行评测。核心思想：用更硬核的题源与严格执行评测拉开上限差距。（[开源代码](https://github.com/Humanity-s-Last-Code-Exam/HLCE)）
- [OJBench](https://arxiv.org/abs/2506.16395)（[开源代码](https://github.com/He-Ren/OJBench)）：评什么：NOI/ICPC 风格竞赛题的代码推理与执行正确性。核心思想：用 232 道竞赛题和中英双语评测，把竞赛级难题做成稳定基准。
- [COMPASS](https://arxiv.org/abs/2508.13757)：评什么：竞赛题代码生成的正确性、效率与代码质量。核心思想：不只看 AC，还把时间效率和实现质量纳入同一套评测。
- [AetherCode](https://arxiv.org/abs/2508.16402)：评什么：顶级编程竞赛胜负能力（更接近 IOI/ICPC 级别难题与评测）。核心思想：把“测试集是否足够区分正确/错误解”视为核心评测对象之一，避免只靠弱测试导致的假阳性。
- [LiveOIBench](https://arxiv.org/abs/2510.09595)：评什么：奥林匹克信息学风格任务上的长推理、算法设计与代码执行能力。核心思想：补足纯 ICPC/Codeforces 题源之外的 OI 难题分布，让竞赛编程评测覆盖更强的构造、数据结构与算法推理压力。
- [Holistic Agent Leaderboard（HAL）](https://arxiv.org/abs/2510.11977)（[开源代码](https://github.com/princeton-pli/hal-harness)）：评什么：跨 benchmark 的 agent 统一评测，其中包含 USACO 等竞赛编程子任务。核心思想：用统一 CLI、成本/时间记录和 leaderboard 提交流程，让竞赛编程结果可与 SWE、网页和现实任务一起比较。
- [Idea First, Code Later](https://arxiv.org/abs/2601.11332)：评什么：ICPC 风格题目中“算法思路”和“代码实现”的可分离能力。核心思想：引入 83 道带 gold editorial 和完整测试的题目，先评自然语言 editorial，再评代码实现，避免只用 AC 混合度量掩盖瓶颈。
- [VeriContest](https://arxiv.org/abs/2605.08553)：评什么：LeetCode 与 Codeforces 题源上的可验证代码生成。核心思想：把自然语言题面、专家验证形式化规格、AC Rust 代码、Verus 证明和正负测试组合起来，分别评估 specification、code、proof 与端到端 verified synthesis。

## 2.1.3 Agent Harness

- [USACO Episodic + Semantic](https://arxiv.org/abs/2404.10952)（[开源代码](https://github.com/princeton-nlp/USACO)）：USACO 竞赛编程 agent 配置；核心思想是用 episodic memory 与语义检索复用相似题经验，支撑 Olympiad 风格长推理题的多步求解。
- [MapCoder](https://arxiv.org/abs/2405.11403)（[开源代码](https://github.com/Md-Ashraful-Pramanik/MapCoder)）：多代理竞赛代码生成框架；核心思想是把 retrieval、planning、coding 与 debugging 显式拆成多角色协作，逼近人类竞赛编程循环。
- [CodeContests+](https://arxiv.org/abs/2506.05817)：面向竞赛题的高质量测试用例生成与验证流程。核心思想：把“测试集构造”显式 agent 化，以提升评测的判别力与鲁棒性。
- [ALE-Agent](https://arxiv.org/abs/2506.09050)（[开源代码](https://github.com/SakanaAI/ALE-Bench)）：面向 AtCoder heuristic contest 的长时程算法工程 agent；核心思想是把代码修改、试跑反馈、可视化分析与分数优化接成持续迭代闭环。
- [Holistic Agent Leaderboard](https://arxiv.org/abs/2510.11977)（[开源代码](https://github.com/princeton-pli/hal-harness)）：跨 benchmark 的 agent 评测 harness；核心思想是把 USACO、SWE-bench、SWE-Lancer 等任务统一到可提交、可复现实验协议中。
- [AutoCode](https://arxiv.org/abs/2510.12803)：面向竞赛编程的自动出题、解题与验题流程；核心思想是把 LLM 组织成 problem setter、solver 与 verifier，用于持续生成 LiveCodeBench Pro 风格的可执行新题。
- [SwiftSolve](https://arxiv.org/abs/2510.22626)：多代理竞赛解题框架；核心思想：把规划、编码、profiling、复杂度分析分工，专门压 TLE/MLE。
- [Agentic Verifier](https://arxiv.org/abs/2602.04254)：面向竞赛代码的执行式 verifier 与 reranker；核心思想：通过多轮执行交互主动搜索能区分候选程序的反例输入，而不是只做随机测试采样。
- [CodeHacker](https://arxiv.org/abs/2602.20213)：面向竞赛提交的 adversarial test generation agent；核心思想：模拟竞赛平台的 hack 机制，结合压力测试、反哈希和逻辑定向构造，暴露弱测试放过的错误解。

## 2.1.4 Skill

- [mcp-code-execution](https://skills.sh/athola/claude-night-market/mcp-code-execution) 适合把竞赛题求解接成“写代码 -> 运行样例/随机测试 -> 修复”的可执行循环。
- [e2b-sandbox](https://skills.sh/smithery.ai/e2b-sandbox) 适合在隔离执行环境里快速做样例回放与回归验证。
- [pytest](https://skills.sh/bobmatnyc/claude-mpm-skills/pytest) 更适合把“对拍/构造测试”沉淀为可复用的自动化检查。
- [pytest-advanced](https://skills.sh/laurigates/claude-plugins/pytest-advanced) 适合更复杂的测试组织与回归检查编排。
- [leetcode-teacher](https://skills.sh/jamesrochabrun/skills/leetcode-teacher) 可作为“算法题讲解/解题套路注入”的过程型 skill（更偏解法教学与思路组织，而非判题 runtime）。
