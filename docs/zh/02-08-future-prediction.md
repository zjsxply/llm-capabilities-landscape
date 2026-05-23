# 2.8 未来预测

> 上级章节：2. 基础 Agent


说明：这条线关注 agent 能否在事件尚未发生前持续搜集信息、更新概率判断，并在时间推移中保持可追踪的预测过程。

## 2.8.1 Leaderboard

- [ForecastBench Leaderboard](http://www.forecastbench.org/)：持续动态生成并定期更新的真实未来事件预测榜单；适合比较模型在未兑现问题上的概率预测、校准和专家/人群对照。
- [Metaculus FutureEval](https://www.metaculus.com/futureeval/)：Metaculus 持续 AI forecasting leaderboard；按统一 log-score 每日更新，并把 AI 模型、Metaculus 社群和专业预测者放在同一视图中比较。
- [FutureSearch Evaluations](https://evals.futuresearch.ai/)：FutureSearch 官方评测入口，汇总 DRB 与 BTF-2；适合把 deep research agent 与 forecasting agent 的“研究-判断”能力放到同一可复现框架下追踪。
- [Prophet Arena](https://www.prophetarena.co/)：面向 LLM-as-a-Prophet 的实时预测竞技场；适合诊断事件回忆、数据源理解、近兑现信息聚合和概率校准等预测 pipeline 环节。
- [TemporalBench Leaderboard](https://huggingface.co/spaces/Melady/TemporalBench_Leaderboard)：TemporalBench 官方 Hugging Face 榜单；适合比较上下文驱动、事件驱动与时间序列式预测能力。
- [Echo](https://echo.unipat.ai/)：UniPat 的动态未来预测 leaderboard 与训练系统；适合观察多点对齐 Elo、Train-on-Future 与 AI-native prediction API 组合后的持续预测表现。
- [Impermanent Dashboard](https://impermanent.timecopilot.dev/)：TimeCopilot 的 live temporal generalization dashboard；适合跟踪时间序列预测模型在滚动数据流上的真实时间外推表现。

## 2.8.2 综述

说明：专门以“AI 预测未来”为题的综述不算多，最贴近的是事件预测和时间序列预测两条线。

- [A Survey on Event Prediction Methods from a Systems Perspective: Bringing Together Disparate Research Areas](https://arxiv.org/abs/2302.04018)：评什么：未来事件预测的系统性综述。核心思想：把分散在不同领域的 event prediction 方法放进统一系统视角，梳理需求、分类和研究缺口，是这条线最直接的入口。
- [Large Language Models for Time Series: A Survey](https://arxiv.org/abs/2402.01801)：评什么：LLM 在时间序列分析与预测中的方法综述。核心思想：总结把时序编码、对齐与适配到 LLM 的主流路线，适合看“用 AI 做时间序列预测”的总览。
- [Large Language Models for Forecasting and Anomaly Detection: A Systematic Literature Review](https://arxiv.org/abs/2402.10350)：评什么：LLM 参与 forecasting 与异常检测的系统综述。核心思想：专门总结 LLM 在预测任务里的应用、挑战和未来方向，比泛化到所有时序任务的综述更贴近“预测未来”这个问题。
- [How do large language models bring disruptive change to time series forecasting? A survey and framework](https://ideas.repec.org/a/taf/tjmaxx/v13y2026i1p17-42.html)：评什么：LLM 介入时间序列预测的综述与框架。核心思想：给出更偏实践的 pipeline 视角和协作模式，强调数据场景和工作流组织。
- [Leveraging Large Language Models for time series forecasting: A systematic literature review](https://www.sciencedirect.com/science/article/pii/S0950705126006647)：评什么：专门聚焦 LLM 驱动时间序列预测的系统综述。核心思想：按 PRISMA 筛出 78 篇研究，覆盖架构、tokenization、prompting、benchmark 和评估问题，是当前更偏 forecasting-only 的最新综述。

## 2.8.3 Bench

- [MIRAI](https://arxiv.org/abs/2407.01231)：评什么：国际事件预测中的 agentic forecasting。核心思想：让 agent 访问历史结构化事件库和新闻文本，通过代码接口调用领域 API，评估信息源整合、工具使用和跨时间推理，是 live future-prediction 路线更早的代表。
- [ForecastBench](https://arxiv.org/abs/2409.19839)（[Leaderboard](http://www.forecastbench.org/)）：评什么：动态生成、定期更新的真实未来事件预测。核心思想：只收录提交时尚未有答案的问题，并用专家、人群与 LLM 共同对照，专门压测模型在数据泄漏最小化条件下的概率预测能力。
- [Context is Key (CiK)](https://arxiv.org/abs/2410.18959)（[项目页](https://servicenow.github.io/context-is-key-forecasting/)）：评什么：带必要文本上下文的时间序列预测。核心思想：把数值历史与自然语言约束/背景知识绑定，让模型必须理解文本才能预测，适合检验“读上下文后预测”而非只做曲线外推。
- [FOReCAst](https://arxiv.org/abs/2502.19676)（[开源代码](https://github.com/MoyYuan/FOReCAst)，[数据集](https://huggingface.co/datasets/MoyYuan/FOReCAst)）：评什么：多领域真实预测任务的概率判断与置信度校准。核心思想：把 Boolean、timeframe 和 quantity 三类题型合在一起，同时评估预测准确率与 confidence，弥补只看最终答案而忽略校准的问题。
- [PROPHET](https://arxiv.org/abs/2504.01509)：评什么：可因果干预的未来事件预测。核心思想：把事件预测拆成可推断未来状态与干预后似然估计，补充 FutureX/Prophet Arena 之前的可解释 future-prediction 评测线。
- [Outcome-based RL Forecasting Dataset](https://arxiv.org/abs/2505.17989)：评什么：预测市场问题上的未来事件概率预测与校准。核心思想：把近期预测市场问题、新闻线索与延迟兑现的真实结果结合，用 outcome reward 训练/评估小模型，说明未来预测可以形成 RLVR 式闭环。
- [Bench to the Future（BTF）](https://arxiv.org/abs/2506.21558)：评什么：forecasting agent 的可复现 pastcasting。核心思想：给已知结局的历史预测题配套冻结网页语料，让 agent 在离线环境中像真实预测一样研究、给概率并留下推理轨迹，避免等待未来兑现和 live web 漂移。
- [Evaluating LLMs on Real-World Forecasting Against Expert Forecasters](https://arxiv.org/abs/2507.04562)：评什么：真实 Metaculus 预测题上的 LLM 概率预测。核心思想：把前沿模型和专家预测者放在同一批真实 forecasting questions 上比较 Brier score 与校准，补足只看模型间相对排名的评测。
- [FutureX](https://arxiv.org/abs/2508.11987)：评什么：面向未来事件预测的 live agent benchmark。核心思想：用实时更新、自动问题收集与答案采集减少数据污染，要求 agent 动态搜集信息、权衡不确定性并持续适应新趋势，贴近分析师/战略研究类现实工作。
- [Prophet Arena](https://arxiv.org/abs/2510.17638)（[项目页](https://www.prophetarena.co/)）：评什么：LLM-as-a-Prophet 的实时预测智能。核心思想：连续收集 live forecasting tasks，并把事件回忆、数据源理解、近兑现信息聚合与概率校准拆开分析，适合看“预测 pipeline 哪一段失败”。
- [KalshiBench](https://arxiv.org/abs/2512.16030)（[数据集](https://huggingface.co/datasets/2084Collective/kalshibench-v2)）：评什么：预测市场问题上的 epistemic calibration。核心思想：用 Kalshi 上已兑现、训练截止后才发生的真实事件，检查模型自报置信度是否匹配真实正确率。
- [FinDeepForecast](https://arxiv.org/abs/2601.05039)：评什么：金融预测场景中的 deep research agent。核心思想：把 live multi-agent research、金融事件预测和可追踪证据链放在同一评测里，连接 ForecastBench 的动态预测与 Deep Research Bench 的搜证式评估。
- [FutureX-Pro](https://arxiv.org/abs/2601.12259)：评什么：高价值垂直领域的未来预测，覆盖金融、零售、公共卫生、自然灾害与搜索。核心思想：继承 FutureX 的 live、contamination-free 管线，把预测任务推进到资本密集或安全关键行业，测试通用 agent 是否具备足够领域 grounding。
- [FutureOmni](https://arxiv.org/abs/2601.13836)：评什么：多模态上下文中的未来预测。核心思想：把文本、图像、视频和结构化线索放进同一未来事件判断任务，检查 agent 是否能从跨模态证据中形成概率预测。
- [Metaculus FutureEval](https://www.metaculus.com/futureeval/)（[方法说明](https://www.metaculus.com/futureeval/methodology/)）：评什么：Metaculus 于 2026-02 发布的持续未来事件预测榜单。核心思想：把开放 Metaculus 预测题持续喂给主流 AI 模型，并和 Metaculus 社群/专业预测者比较校准、覆盖率与随模型发布时间变化的真实预测表现；该线索可由 BTF-2 对 Metaculus AI Benchmarking Series 的引用继续展开得到。
- [TemporalBench](https://arxiv.org/abs/2602.13272)（[数据集](https://huggingface.co/datasets/Melady/TemporalBench)；[Leaderboard](https://huggingface.co/spaces/Melady/TemporalBench_Leaderboard)）：评什么：LLM agent 的上下文与事件驱动时间序列预测。核心思想：把任务分成历史结构解释、无上下文预测、上下文推理和事件条件预测四层，诊断模型是否真正利用外部事件而不是只拟合曲线。
- [Echo](https://echo.unipat.ai/)（[官方文章](https://unipat.ai/blog/Echo)）：评什么：动态未来预测 leaderboard 与训练系统，覆盖金融、政治、加密、体育和电竞等域。核心思想：用多点对齐 Elo、Train-on-Future 和 AI-native prediction API 组成完整预测闭环，解决不同模型预测时间点不齐与训练信号滞后问题。
- [Impermanent](https://arxiv.org/abs/2603.08707)（[开源代码](https://github.com/TimeCopilot/impermanent)；[Dashboard](https://impermanent.timecopilot.dev/)）：评什么：时间序列预测的 live temporal generalization。核心思想：用 GitHub 活动等持续变化的数据流滚动评分，考察模型是否能在开放世界时间漂移下维持预测稳定性。
- [YC-Bench](https://arxiv.org/abs/2604.01212)：评什么：长期规划与一致执行中的状态记忆。核心思想：让 agent 在持续经营类任务中反复使用历史目标、资源状态和中间决策，观察 context truncation、scratchpad 与 memory 策略的真实收益。
- [TimeSeek](https://arxiv.org/abs/2604.04220)：评什么：agentic forecaster 的时间可靠性。核心思想：按问题生命周期的多个时间点重放预测，比较无检索、web 检索与不同模型在临近兑现时的概率更新质量。
- [TFRBench](https://arxiv.org/abs/2604.05364)：评什么：预测系统的推理能力。核心思想：将 forecasting 拆成可诊断的 reasoning benchmark，关注信息选择、时序因果、约束解释与预测一致性，而不是只看最终误差。
- [Prediction Arena](https://arxiv.org/abs/2604.07355)：评什么：面向预测市场/未来事件的 live 模型对战评测。核心思想：用持续更新的问题与赛制比较模型预测，在答案兑现前后统一记录概率、理由与校准表现。
- [PolyBench](https://arxiv.org/abs/2604.14199)：评什么：基于 live prediction market data 的 LLM 预测与交易能力。核心思想：把 Polymarket 等市场中的概率判断、交易收益与校准联系起来，评估 agent 是否能把预测转化为可操作策略。
- [QuantSightBench](https://arxiv.org/abs/2604.15859)（[项目页](https://quantsightbench.com/)；[开源代码](https://github.com/aisa-group/quantsightbench)）：评什么：连续数值量的区间预测与不确定性校准。核心思想：要求模型给出 prediction intervals，而不是单点或二选一答案，专门暴露极端量级下的系统性过度自信。
- [Bench to the Future 2（BTF-2）](https://arxiv.org/abs/2604.26106)（[FutureSearch Evaluations](https://evals.futuresearch.ai/)）：评什么：forecasting agent 的战略推理与研究-判断分解。核心思想：用 1,417 个 pastcasting 问题、冻结的 1,500 万文档研究语料和完整推理轨迹，区分 agent 是输在信息研究、概率判断还是黑天鹅/激励建模。
- [FutureWorld](https://arxiv.org/abs/2604.26733)：评什么：面向未来预测的 live agentic RL 环境。核心思想：把预测、结果兑现与参数更新接成闭环，用延迟真实结果回填奖励并重放轨迹，研究“预测-兑现-再学习”的在线改进。
- [Foresight Arena](https://arxiv.org/abs/2605.00420)：评什么：大模型预测未来事件的开放式竞技场。核心思想：围绕动态问题、概率提交和后验兑现构建持续评测，和 ForecastBench/FutureX 一起构成“live forecasting eval”主线。
- [OracleProto](https://arxiv.org/abs/2605.03762)：评什么：LLM-native forecasting 的可复现 pastcasting。核心思想：用知识截止时间与时间遮罩构造可重复预测协议，专门诊断 hindsight leakage 和检索时序污染。
- [FutureSim](https://arxiv.org/abs/2605.15188)：评什么：按真实新闻与事件兑现时间线回放来评测自适应 agent。核心思想：让 agent 在知识截止时间之后、按时间顺序接收 2026 年 1 到 3 月新闻并预测事件，测试长时程适应、记忆、搜索和不确定性校准。

## 2.8.4 Agent Harness

- [Reasoning and Tools for Human-Level Forecasting](https://arxiv.org/abs/2408.12036)（开源代码：未公开；早期 agentic forecasting scaffold；核心思想是把检索、分解、数值校准和 forecasting heuristics 接到同一推理工具链里，成为 BTF/FutureSearch 后续工作的直接引用基线）
- [TimeSeriesScientist](https://arxiv.org/abs/2510.01538)（[开源代码](https://github.com/Y-Research-SBU/TimeSeriesScientist)；通用时间序列预测 agent；核心思想是用 Curator、Planner、Forecaster、Reporter 四类代理把数据诊断、模型选择、验证集成和报告生成串成白盒 forecasting workflow）
- [AIA Forecaster](https://arxiv.org/abs/2511.07678)（开源代码：未公开；面向真实未来事件的 agentic forecaster；核心思想是用多轮网页研究、结构化预测提示和校准规则逼近人类 superforecaster，并暴露 live/pastcasting 评测中的信息泄漏风险）
- [OpenForecaster](https://arxiv.org/abs/2512.25070)（[开源代码](https://github.com/OpenForecaster/scaling-forecasting-training)；面向开放式未来事件的 forecasting agent/model 训练路线；核心思想是从新闻自动构造 OpenForesight 预测题，结合离线检索和 RL 训练来提升准确率、校准与长期一致性）
- [FutureSearch Forecasting Question Generator/Resolver](https://arxiv.org/abs/2601.22444)（开源代码：未公开；用 LLM 驱动的网页研究 agent 自动生成和兑现预测问题，既是评测题生产 harness，也能用题目分解策略改进 forecasting agent 的概率判断）
- MiroFish（[开源代码](https://github.com/666ghj/MiroFish)，[官方站点](https://mirofish.work/)；无独立论文）：把种子材料、知识图谱、多人格代理和社会演化拼成可交互的预测模拟引擎；适合把“预测”从静态问答变成可回放的 scenario simulation。
- FutureSearch ReAct Agent（[开源代码](https://github.com/futuresearch/futuresearch-python)；无独立 arXiv 论文）：BTF-2 论文引用的 FutureSearch 开源 agent 实现，提供 ReAct-style 系统提示、网页研究工具包和时间管理机制，适合作为 forecasting agent 的可复现实验 harness。
- [Milkyway](https://arxiv.org/abs/2604.15719)（开源代码：未找到稳定公开仓库）：把预解析信号写回持续更新的 future prediction harness。核心思想：对同一未决问题反复预测、提取 pre-resolution signal、更新 factor tracking / evidence gathering / uncertainty handling，再用已实现结果做回看检查，属于更直接的 harness evolution 路线。
- [Bayesian Linguistic Forecaster（BLF）](https://arxiv.org/abs/2604.18576)（开源代码：未公开；面向 ForecastBench 的 agentic forecaster；核心思想是把数值概率与自然语言证据摘要合成 linguistic belief state，并在迭代工具使用中做 sequential Bayesian updating、trial aggregation 与层级校准）

## 2.8.5 Skill

- [time-series-forecaster](https://skills.sh/anton-abyzov/specweave/time-series-forecaster) 适合时间序列预测、趋势外推与置信区间输出。
