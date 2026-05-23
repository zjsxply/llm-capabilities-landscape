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
- [Know Thy Judge](https://arxiv.org/abs/2503.04474)：对 LLM safety judge 的鲁棒性做元评测。核心思想：通过扰动压力测试 judge 行为，避免安全 benchmark 分数在不知不觉中继承脆弱或有偏的 judge 决策。
- [MPBench](https://arxiv.org/abs/2503.12505)：评测多模态推理中的过程错误识别；核心思想是同时测试步骤正确性、答案聚合和推理过程搜索，使 benchmark 分数能暴露多模态推理轨迹失败的位置。
- [SWE-rebench](https://arxiv.org/abs/2505.20411)（[Leaderboard](https://swe-rebench.com/leaderboard)）：自动收集并去污染 SWE 任务，强调新鲜 issue、可交互执行反馈与任务构造流水线。
- [SWE-bench-Live](https://arxiv.org/abs/2505.23419)（[开源代码](https://github.com/SWE-bench-Live/SWE-bench-Live)；[Leaderboard](https://swe-bench-live.github.io/)）：持续从近期 GitHub issue/PR 生成任务，重点降低静态软件工程 benchmark 被记忆或过拟合的风险。
- [SWE-MERA](https://arxiv.org/abs/2507.11059)：动态软件工程 agent 评测；核心思想是持续采集、执行和验证新任务，把 agentic SWE 评测从单次快照推进到滚动题库。
- [Multi-Agent-as-Judge](https://arxiv.org/abs/2507.21028)：将基于 LLM 智能体的自动评测与多维人工评测对齐。核心思路是用多个评审智能体和结构化维度降低单一裁判偏差，使自动评测更接近人工评审。
- [ConfProBench](https://arxiv.org/abs/2508.04576)：评测基于 MLLM 的过程裁判在步骤级置信度上的可靠性。核心思想：用同义替换、句法改写和图像扰动改变推理步骤，衡量置信度鲁棒性、敏感性和校准，而不只看判断正确性。
- [EffiEval](https://arxiv.org/abs/2508.09662)：通过基于能力覆盖的样本选择降低评测成本；核心价值是在只查询代表性 benchmark 样本的同时，尽量保持排名一致性与公平性。
- [Auto-BenchmarkCard](https://arxiv.org/abs/2512.09577)：自动生成 benchmark 文档卡；适合在 benchmark 数量快速增长时快速暴露数据、指标和限制描述缺失。
- [InFerActive](https://arxiv.org/abs/2512.10234)：通过交互式推理树扩展人工评测；核心思想是让评审比较结构化行为路径，而不是逐条响应进行低效判断。
- [The Judge Who Never Admits](https://arxiv.org/abs/2602.07996)：审计 LLM-as-judge 评测中的隐藏捷径。核心思想：注入受控元数据线索，并比较 verdict shift 与 cue acknowledgment，揭示裁判模型何时依赖无关信号却不在解释中承认。
- [Auditing Multi-Agent Reasoning Trees](https://arxiv.org/abs/2602.09341)：审计多 agent 推理轨迹中的证据结构；核心价值是用围绕一致点与分歧点的局部验证，替代多数投票或通用 LLM-as-judge 聚合。
- [SWE-rebench V2](https://arxiv.org/abs/2602.23866)：语言无关、规模更大的动态 SWE 任务构造与执行评测；延续去污染自动化采集路线，把可执行任务扩展到更多语言与仓库生态。
- [CUBE](https://arxiv.org/abs/2603.15798)：提出基于 MCP 与 Gym 的 Common Unified Benchmark Environments 协议标准；适合降低 agent benchmark 快速增多后的集成税，并把 task、benchmark、package 和 registry 层职责拆清楚。
- [FACT-E](https://arxiv.org/abs/2604.10693)：通过因果扰动与步骤间依赖检查评测 chain-of-thought 的忠实性；适合区分“看似连贯但不支撑答案”的轨迹与真正支持答案的推理路径。
- [Terminal Wrench](https://arxiv.org/abs/2604.17596)（[开源代码](https://github.com/few-sh/terminal-wrench)）：评测终端 benchmark 是否可被 reward hacking 绕过；核心价值是把环境漏洞、评分捷径和轨迹操纵作为 benchmark 可靠性问题显式化。
- [QuickScope](https://arxiv.org/abs/2604.17842)：为动态 benchmark 中的难题做快速认证；核心思想是给“这题是否真的难、是否能区分模型”提供更低成本的预筛机制。
- [ProEval](https://arxiv.org/abs/2604.23099)：在有限评测预算下主动发现失败并估计生成式 AI 的 benchmark 表现；核心思想是用不确定性感知的迁移代理模型选择或合成高信息量测试样本。
- [Claw-Eval](https://arxiv.org/abs/2604.06132)（[开源代码](https://github.com/claw-eval/claw-eval)）：真实软件环境中的多步骤 agent 工作流评测；通过细粒度 rubric、三次运行一致性和轨迹审计降低一次性通过率的偶然性。
- [ClawBench](https://arxiv.org/abs/2604.08523)（[项目页](https://claw-bench.com/)；[开源代码](https://github.com/reacher-z/ClawBench)）：真实 live website 写操作任务；通过 HTTP interception、payload judge 和审计轨迹减少真实网站评测的破坏性与不可复现性。
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)（[项目页](https://claw-eval-live.github.io/)；[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：会随真实 workflow demand 变化的 live agent benchmark；其价值在于按季度刷新任务分布，同时保留 mock service、workspace fixture、trace 和 grader 以便复现。

## 0.5.3 使用建议

阅读新 benchmark 时，优先检查它是否说明了数据来源、采样时间、污染控制、题目刷新机制、失败样本审计、judge 校准、环境快照和排行榜提交协议。对于 agent benchmark，还要额外看是否保存完整轨迹、工具调用、环境状态、成本、运行时间和多次运行方差；否则 leaderboard 排名很容易混入 harness 工程、环境偶然性和评分捷径。
