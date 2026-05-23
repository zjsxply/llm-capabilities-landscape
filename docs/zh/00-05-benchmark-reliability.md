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
- [Statistical Uncertainty Quantification for Aggregate Performance Metrics](https://arxiv.org/abs/2501.04234)：研究聚合 benchmark 分数的不确定性估计。核心思想：使用 bootstrap、层级建模和任务权重可视化，使 benchmark 汇总报告排序不确定性，而不是把单一平均分当作定论。
- [Humanity's Last Exam](https://arxiv.org/abs/2501.14249) / [HLE-Rolling](https://agi.safe.ai/)（更新日志：[centerforaisafety/hle](https://github.com/centerforaisafety/hle/blob/main/hle-rolling-changes.txt)）：HLE 提供高难专家题，HLE-Rolling 通过持续修订、新题和 live submission 缓解公开题库污染、错误与饱和。
- [LLM-Safety Evaluations Lack Robustness](https://arxiv.org/abs/2503.02574)：审计 LLM 安全评测的鲁棒性；核心思想是检查扰动或评测设计选择如何改变安全评测结论，避免把不稳定分数直接当作可靠能力度量。
- [Know Thy Judge](https://arxiv.org/abs/2503.04474)：对 LLM safety judge 的鲁棒性做元评测。核心思想：通过扰动压力测试 judge 行为，避免安全 benchmark 分数在不知不觉中继承脆弱或有偏的 judge 决策。
- [Safer or Luckier?](https://arxiv.org/abs/2503.09347)：审计 LLM 安全评估器对数据伪迹的敏感性。核心思想：检验安全 judge 的分数究竟反映稳健风险判断，还是会被表层数据伪迹带偏，从而在信任 benchmark 结果之前暴露评估器脆弱性。
- [SPHERE](https://arxiv.org/abs/2504.07971)：面向 human-AI system 的 evaluation-card 框架；核心思想是记录系统语境、人类角色、指标、限制和部署假设，使人机系统评测可审计，而不是被压缩成单一分数。
- [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879)：审计 Chatbot Arena 类 leaderboard 的可靠性。核心思想：揭示私有测试、选择性披露、采样不均与模型移除策略如何偏置排名，说明 leaderboard 分数需要协议层面的审查。
- [SWE-rebench](https://arxiv.org/abs/2505.20411)（[Leaderboard](https://swe-rebench.com/leaderboard)）：自动收集并去污染 SWE 任务，强调新鲜 issue、可交互执行反馈与任务构造流水线。
- [SWE-bench-Live](https://arxiv.org/abs/2505.23419)（[开源代码](https://github.com/SWE-bench-Live/SWE-bench-Live)；[Leaderboard](https://swe-bench-live.github.io/)）：持续从近期 GitHub issue/PR 生成任务，重点降低静态软件工程 benchmark 被记忆或过拟合的风险。
- [Auto-Arena](https://aclanthology.org/2025.acl-long.223/)：通过 agent peer battles 和委员会讨论自动化 LLM 评测。核心思想：把成对辩论和多裁判讨论纳入评测协议，减少模型比较对单一静态提示词或单个 judge 的依赖。
- [SWE-MERA](https://arxiv.org/abs/2507.11059)：动态软件工程 agent 评测；核心思想是持续采集、执行和验证新任务，把 agentic SWE 评测从单次快照推进到滚动题库。
- [Multi-Agent-as-Judge](https://arxiv.org/abs/2507.21028)：将基于 LLM 智能体的自动评测与多维人工评测对齐。核心思路是用多个评审智能体和结构化维度降低单一裁判偏差，使自动评测更接近人工评审。
- [ConfProBench](https://arxiv.org/abs/2508.04576)：评测基于 MLLM 的过程裁判在步骤级置信度上的可靠性。核心思想：用同义替换、句法改写和图像扰动改变推理步骤，衡量置信度鲁棒性、敏感性和校准，而不只看判断正确性。
- [Beyond statistical significance](https://arxiv.org/abs/2509.22612)：量化多语言与多任务 NLP 评测中的不确定性和统计波动。核心思想：用重采样估计 benchmark 指标、排名和模型两两差异的复现不确定性，而不是把 leaderboard 分数视为固定值。
- [ProJudge](https://openaccess.thecvf.com/content/ICCV2025/html/Ai_ProJudge_A_Multi-Modal_Multi-Discipline_Benchmark_and_Instruction-Tuning_Dataset_for_MLLM-based_ICCV_2025_paper.html)（[项目页](https://projudge.github.io/)）：评测跨多模态学科的 MLLM 过程裁判。核心思想：把过程级评判能力本身作为 benchmark 目标，使 verifier 和 grader 质量能与基础任务求解能力分开衡量。
- [Detecting Silent Failures in Multi-Agentic AI Trajectories](https://arxiv.org/abs/2511.04032)：评测多 agent 轨迹中的异常检测。核心思想是为漂移、循环和细节遗漏等失败构建带标签轨迹数据集，使静默 agent 失败能在最终答案评分掩盖问题之前被发现。
- [Hidden Measurement Error in LLM Pipelines](https://arxiv.org/abs/2604.11581)：审计 LLM 标注和评测流水线中被隐藏的方差来源；核心思想是把评判模型选择、温度和提示措辞都视为测量误差来源，使基准结论包含普通抽样置信区间之外的不确定性。
- [Yourbench](https://openreview.net/forum?id=bkWERVKzuP)：用 LLM 生成动态评测集。核心思想：让 benchmark 构建者从私有或新鲜材料中实例化任务特定测试，避免只依赖公开静态题集。
- [Fluid Language Model Benchmarking](https://openreview.net/forum?id=mxcCg9YRqj)：研究语言模型评测中的 benchmark 流动性。核心思想：把评测集视为持续演化的对象，并在受控刷新和变化下检验评测结论是否稳健。
- [EvalAgents](https://openreview.net/forum?id=erGpkHCybv)：从 Web 中发现隐式评测标准。核心思想：用网页中抽取的标准让评测 rubric 更贴近任务，减少对手写通用打分表的依赖。
- [AgentRewardBench](https://openreview.net/forum?id=fQcUZMPIvu)：评测 Web agent 轨迹的自动评分质量。核心思想：检查 reward model 和自动裁判能否正确评价完整 agent 轨迹，而不是只看最终答案或单张截图。
- [Judge's Verdict](https://arxiv.org/abs/2510.09738)：评什么：LLM-as-a-judge 与人类判断的一致性。核心思想：把 judge 可靠性本身作为评估对象，暴露自动裁决何处与人工评审一致或分歧。
- [Auto-BenchmarkCard](https://arxiv.org/abs/2512.09577)：自动生成 benchmark 文档卡；适合在 benchmark 数量快速增长时快速暴露数据、指标和限制描述缺失。
- [RULERS](https://arxiv.org/abs/2601.08654)：为稳健 LLM 评估提供锁定评分规程和证据锚定打分。核心思路是将自然语言评分规程编译为可执行标准，使裁判行为减少提示敏感性并更易审计。
- [Rubric-Conditioned LLM Grading](https://arxiv.org/abs/2601.08843)：研究基于 rubric 的自动评分在对齐、不确定性和鲁棒性方面的表现；核心思想是把评分 rubric 本身纳入评测对象，从而显式衡量 judge 可靠性与不确定性。
- [The Judge Who Never Admits](https://arxiv.org/abs/2602.07996)：审计 LLM-as-judge 评测中的隐藏捷径。核心思想：注入受控元数据线索，并比较 verdict shift 与 cue acknowledgment，揭示裁判模型何时依赖无关信号却不在解释中承认。
- [SWE-rebench V2](https://arxiv.org/abs/2602.23866)：语言无关、规模更大的动态 SWE 任务构造与执行评测；延续去污染自动化采集路线，把可执行任务扩展到更多语言与仓库生态。
- [A Coin Flip for Safety](https://arxiv.org/abs/2603.06594)：审计 LLM-as-a-judge 在对抗鲁棒性评估中的可靠性。核心思路是在红队分布偏移下用人工验证标签对照评判器行为，避免安全分数继承不稳定的评测偏差。
- [CUBE](https://arxiv.org/abs/2603.15798)：提出基于 MCP 与 Gym 的 Common Unified Benchmark Environments 协议标准；适合降低 agent benchmark 快速增多后的集成税，并把 task、benchmark、package 和 registry 层职责拆清楚。
- [FACT-E](https://arxiv.org/abs/2604.10693)：通过因果扰动与步骤间依赖检查评测 chain-of-thought 的忠实性；适合区分“看似连贯但不支撑答案”的轨迹与真正支持答案的推理路径。
- [Terminal Wrench](https://arxiv.org/abs/2604.17596)（[开源代码](https://github.com/few-sh/terminal-wrench)）：评测终端 benchmark 是否可被 reward hacking 绕过；核心价值是把环境漏洞、评分捷径和轨迹操纵作为 benchmark 可靠性问题显式化。
- [QuickScope](https://arxiv.org/abs/2604.17842)：为动态 benchmark 中的难题做快速认证；核心思想是给“这题是否真的难、是否能区分模型”提供更低成本的预筛机制。
- [How Sensitive Are Safety Benchmarks to Judge Configuration Choices?](https://arxiv.org/abs/2604.24074)：审计安全基准分数如何随 LLM 裁判提示词和配置变化而波动。核心思路是把裁判设置视为评测变量，而不是实现细节，从而暴露安全基准中的分数和排名不稳定性。
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)（[项目页](https://claw-eval-live.github.io/)；[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：会随真实 workflow demand 变化的 live agent benchmark；其价值在于按季度刷新任务分布，同时保留 mock service、workspace fixture、trace 和 grader 以便复现。

## 0.5.3 使用建议

阅读新 benchmark 时，优先检查它是否说明了数据来源、采样时间、污染控制、题目刷新机制、失败样本审计、judge 校准、环境快照和排行榜提交协议。对于 agent benchmark，还要额外看是否保存完整轨迹、工具调用、环境状态、成本、运行时间和多次运行方差；否则 leaderboard 排名很容易混入 harness 工程、环境偶然性和评分捷径。
