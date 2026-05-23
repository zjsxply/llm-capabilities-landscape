# 2.1.3 Bench

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
