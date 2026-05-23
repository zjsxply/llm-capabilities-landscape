# 0.5 Benchmark 可靠性与动态评测

> 上级章节：0. Harness 与 Skill Creator

## 0.5.1 为什么单列

随着模型和 agent 迭代加速，静态 benchmark 的主要风险不再只是题目太简单，而是题目泄漏、训练污染、leaderboard 过拟合、judge 漂移、评测协议不透明、动态环境不可复现，以及“高分但不可部署”的假象。可靠评测需要同时看四件事：任务是否仍然新鲜，指标是否可解释，评测过程是否可复现，leaderboard 是否能区分模型能力、harness 设计和环境状态变化。

## 0.5.2 代表工作与入口

- [DyVal](https://arxiv.org/abs/2309.17167)：动态生成推理任务，缓解固定题库污染；适合观察“按规则生成新题”的路线。
- [LatestEval](https://arxiv.org/abs/2312.12343)：用最新新闻与时间敏感材料构造阅读理解评测；核心价值是把“模型是否见过题”转成时间切片问题。
- [DARG](https://arxiv.org/abs/2406.17271)：用 adaptive reasoning graph 动态评估 LLM 推理；核心思想是根据模型回答路径生成后续问题，减少固定 prompt 模板被刷榜。
- [LiveBench](https://arxiv.org/abs/2406.19314)（[开源代码](https://github.com/LiveBench/LiveBench)；[Leaderboard](https://livebench.ai/)）：持续发布新题的综合榜单，覆盖数学、编码、语言、推理、数据分析与指令遵循，是“污染受限 live benchmark”的代表入口。
- [BenchmarkCards](https://arxiv.org/abs/2410.12974)（[开源代码](https://github.com/SokolAnn/BenchmarkCards)）：标准化 benchmark 文档化框架；读新 benchmark 时可用它检查任务目标、数据来源、指标、限制、风险和适用边界是否被说明清楚。
- [Humanity's Last Exam](https://arxiv.org/abs/2501.14249) / [HLE-Rolling](https://agi.safe.ai/)（更新日志：[centerforaisafety/hle](https://github.com/centerforaisafety/hle/blob/main/hle-rolling-changes.txt)）：HLE 提供高难专家题，HLE-Rolling 通过持续修订、新题和 live submission 缓解公开题库污染、错误与饱和。
- [SWE-rebench](https://arxiv.org/abs/2505.20411)（[Leaderboard](https://swe-rebench.com/leaderboard)）：自动收集并去污染 SWE 任务，强调新鲜 issue、可交互执行反馈与任务构造流水线。
- [SWE-bench-Live](https://arxiv.org/abs/2505.23419)（[开源代码](https://github.com/SWE-bench-Live/SWE-bench-Live)；[Leaderboard](https://swe-bench-live.github.io/)）：持续从近期 GitHub issue/PR 生成任务，重点降低静态软件工程 benchmark 被记忆或过拟合的风险。
- [SWE-MERA](https://arxiv.org/abs/2507.11059)：动态软件工程 agent 评测；核心思想是持续采集、执行和验证新任务，把 agentic SWE 评测从单次快照推进到滚动题库。
- [Auto-BenchmarkCard](https://arxiv.org/abs/2512.09577)：自动生成 benchmark 文档卡；适合在 benchmark 数量快速增长时快速暴露数据、指标和限制描述缺失。
- [SWE-rebench V2](https://arxiv.org/abs/2602.23866)：语言无关、规模更大的动态 SWE 任务构造与执行评测；延续去污染自动化采集路线，把可执行任务扩展到更多语言与仓库生态。
- [Terminal Wrench](https://arxiv.org/abs/2604.17596)（[开源代码](https://github.com/few-sh/terminal-wrench)）：评测终端 benchmark 是否可被 reward hacking 绕过；核心价值是把环境漏洞、评分捷径和轨迹操纵作为 benchmark 可靠性问题显式化。
- [QuickScope](https://arxiv.org/abs/2604.17842)：为动态 benchmark 中的难题做快速认证；核心思想是给“这题是否真的难、是否能区分模型”提供更低成本的预筛机制。
- [Claw-Eval](https://arxiv.org/abs/2604.06132)（[开源代码](https://github.com/claw-eval/claw-eval)）：真实软件环境中的多步骤 agent 工作流评测；通过细粒度 rubric、三次运行一致性和轨迹审计降低一次性通过率的偶然性。
- [ClawBench](https://arxiv.org/abs/2604.08523)（[项目页](https://claw-bench.com/)；[开源代码](https://github.com/reacher-z/ClawBench)）：真实 live website 写操作任务；通过 HTTP interception、payload judge 和审计轨迹减少真实网站评测的破坏性与不可复现性。
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)（[项目页](https://claw-eval-live.github.io/)；[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：会随真实 workflow demand 变化的 live agent benchmark；其价值在于按季度刷新任务分布，同时保留 mock service、workspace fixture、trace 和 grader 以便复现。

## 0.5.3 使用建议

阅读新 benchmark 时，优先检查它是否说明了数据来源、采样时间、污染控制、题目刷新机制、失败样本审计、judge 校准、环境快照和排行榜提交协议。对于 agent benchmark，还要额外看是否保存完整轨迹、工具调用、环境状态、成本、运行时间和多次运行方差；否则 leaderboard 排名很容易混入 harness 工程、环境偶然性和评分捷径。
