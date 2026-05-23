# 2.8.4 Agent Harness

- [Reasoning and Tools for Human-Level Forecasting](https://arxiv.org/abs/2408.12036)（开源代码：未公开；早期 agentic forecasting scaffold；核心思想是把检索、分解、数值校准和 forecasting heuristics 接到同一推理工具链里，成为 BTF/FutureSearch 后续工作的直接引用基线）
- [TimeSeriesScientist](https://arxiv.org/abs/2510.01538)（[开源代码](https://github.com/Y-Research-SBU/TimeSeriesScientist)；通用时间序列预测 agent；核心思想是用 Curator、Planner、Forecaster、Reporter 四类代理把数据诊断、模型选择、验证集成和报告生成串成白盒 forecasting workflow）
- [AIA Forecaster](https://arxiv.org/abs/2511.07678)（开源代码：未公开；面向真实未来事件的 agentic forecaster；核心思想是用多轮网页研究、结构化预测提示和校准规则逼近人类 superforecaster，并暴露 live/pastcasting 评测中的信息泄漏风险）
- [OpenForecaster](https://arxiv.org/abs/2512.25070)（[开源代码](https://github.com/OpenForecaster/scaling-forecasting-training)；面向开放式未来事件的 forecasting agent/model 训练路线；核心思想是从新闻自动构造 OpenForesight 预测题，结合离线检索和 RL 训练来提升准确率、校准与长期一致性）
- [FutureSearch Forecasting Question Generator/Resolver](https://arxiv.org/abs/2601.22444)（开源代码：未公开；用 LLM 驱动的网页研究 agent 自动生成和兑现预测问题，既是评测题生产 harness，也能用题目分解策略改进 forecasting agent 的概率判断）
- MiroFish（[开源代码](https://github.com/666ghj/MiroFish)，[官方站点](https://mirofish.work/)；无独立论文）：把种子材料、知识图谱、多人格代理和社会演化拼成可交互的预测模拟引擎；适合把“预测”从静态问答变成可回放的 scenario simulation。
- FutureSearch ReAct Agent（[开源代码](https://github.com/futuresearch/futuresearch-python)；无独立 arXiv 论文）：BTF-2 论文引用的 FutureSearch 开源 agent 实现，提供 ReAct-style 系统提示、网页研究工具包和时间管理机制，适合作为 forecasting agent 的可复现实验 harness。
- [Milkyway](https://arxiv.org/abs/2604.15719)（开源代码：未找到稳定公开仓库）：把预解析信号写回持续更新的 future prediction harness。核心思想：对同一未决问题反复预测、提取 pre-resolution signal、更新 factor tracking / evidence gathering / uncertainty handling，再用已实现结果做回看检查，属于更直接的 harness evolution 路线。
- [Bayesian Linguistic Forecaster（BLF）](https://arxiv.org/abs/2604.18576)（开源代码：未公开；面向 ForecastBench 的 agentic forecaster；核心思想是把数值概率与自然语言证据摘要合成 linguistic belief state，并在迭代工具使用中做 sequential Bayesian updating、trial aggregation 与层级校准）
