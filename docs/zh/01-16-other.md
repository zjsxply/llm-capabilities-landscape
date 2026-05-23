# 1.16 其它

> 上级章节：1. 基础能力

说明：本页收纳主轴较交叉、偏 meta-evaluation，或暂时还不足以单独形成一个稳定类别的 benchmark 与 harness。后续如果同类工作积累到足够密度，应再移入更具体的页面。

## 1.16.1 Leaderboard

## 1.16.2 Survey

- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432)：关于架构、规划、记忆、工具、多智能体交互与评测的基础综述。
- [Large Language Model Agent: A Survey on Methodology, Applications and Challenges](https://arxiv.org/abs/2503.21460)：面向难以归入更窄能力页面的 agent 工作的近期综合综述。
- [AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges](https://arxiv.org/abs/2505.10468)：提供概念分类以及广义应用与挑战地图。
- [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)：回顾任务设计、指标、可复现性、环境交互与榜单式评测。
- [A Survey on Agent Workflow - Status and Future](https://arxiv.org/abs/2508.01186)：综述通用 agent workflow 的设计与未来方向。

## 1.16.3 Bench

- [RoleMRC](https://arxiv.org/abs/2502.11387)：通过细粒度复合任务评测角色扮演与指令遵循；核心思想是检查角色型 agent 是否能在满足用户显式指令的同时保持 persona 约束。
- [STEER-ME](https://arxiv.org/abs/2502.13119)（数据集：[narunraman/steer_me](https://huggingface.co/datasets/narunraman/steer_me)）：评什么：LLM 的微观经济推理。核心思想：用非战略性经济决策设定诊断模型是否能推理激励、偏好和权衡，而不是只回答经济领域事实。
- [ThinkBench](https://arxiv.org/abs/2502.16268)（[开源代码](https://github.com/huangshulin123/ThinkBench)，[数据集](https://huggingface.co/datasets/jiuyinjiu/ThinkBench)）：评什么：动态分布外生成条件下的稳健 LLM 推理。核心思想：生成并评测新鲜 OOD 推理样本，降低答案泄漏和 benchmark 过拟合风险，并用同一协议比较 reasoning 与 non-reasoning 模型。
- [MMDT / Multimodal DecodingTrust](https://arxiv.org/abs/2503.14827)：评估多模态基础模型的安全性与可信度。核心思路是把有用性、公平性、隐私、鲁棒性和安全等维度纳入统一平台，避免只用通用任务准确率判断多模态系统。
- [CQ-Bench](https://arxiv.org/abs/2504.01127)：评测 LLM 是否理解隐含文化价值；核心思想是用相关价值未被直接说出的情境测试文化智能，为多语评测补充 culture reasoning 维度。
- [MMAU](https://aclanthology.org/2025.findings-naacl.267/)：评测跨多领域的综合 agent 能力。核心思想：把宽泛 agent 能力拆成可复用 benchmark suite，而不是强行归入网页、工具使用或代码类别。
- [AbsenceBench](https://arxiv.org/abs/2506.11440)（[开源代码](https://github.com/harvey-fin/absence-bench)，[数据集](https://huggingface.co/datasets/harveyfin/AbsenceBench)）：评什么：在长输入中发现被刻意删掉的信息。核心思想：用序列、诗歌和 GitHub pull request 中的“缺失项识别”补充 needle retrieval，暴露模型能找出现有事实但看不见遗漏的失败。
- [MultiAgentBench](https://aclanthology.org/2025.acl-long.421/)：评测 LLM agents 的协作与竞争。核心思想：在多智能体 benchmark 尚未足够密集到单独成页之前，先把交互协议和结果权衡作为明确可测对象记录下来。
- [SocialCC](https://aclanthology.org/2025.acl-long.1594/)：评什么：交互式 language agent 的文化能力。核心思想：把文化评测从静态问答推进到对话和互动场景，检查 agent 是否能适应社会语境和文化预期。
- [EffiEval](https://arxiv.org/abs/2508.09662)：通过基于能力覆盖的样本选择降低评测成本。核心思想：在只查询代表性 benchmark 样本的同时，尽量保持排名一致性与公平性。
- [Social Welfare Function Leaderboard](https://arxiv.org/abs/2510.01164)：评测 LLM agent 在稀缺社会资源分配中的决策；核心思想是用动态模拟同时比较集体效率与分配公平性，并以 ROI 和 Gini 类指标刻画权衡。
- [CorrectBench](https://arxiv.org/abs/2510.16062)（[项目页](https://correctbench.github.io/)，[数据集](https://huggingface.co/datasets/zeli2024/CorrectBench)）：评什么：LLM 推理的自我修正策略。核心思想：在多类推理任务上比较内在、外部和微调式修正设置，区分真正错误修复与重复错误或过度自信的错答。
- [Infinity-Chat](https://arxiv.org/abs/2510.22954)（[开源代码](https://github.com/liweijiang/artificial-hiveminds)，[数据集](https://huggingface.co/datasets/liweijiang/infinite-chats-taxonomy)）：评什么：开放式语言模型输出的多样性与同质化。核心思想：用包含大量合理答案空间的真实用户问题，衡量模型多次生成是否坍缩成相似的“蜂巢式”回答，而不是保持类似人类的表达差异。
- [InFerActive](https://arxiv.org/abs/2512.10234)：通过交互式推理树扩展人工评测。核心思想：让评审比较结构化行为路径，而不是逐条响应低效判断。
- [Auditing Multi-Agent Reasoning Trees](https://arxiv.org/abs/2602.09341)：审计多 agent 推理轨迹中的证据结构。核心思想：用围绕一致点与分歧点的局部验证，替代多数投票或通用 LLM-as-judge 聚合。
- [MEDLEY-BENCH](https://arxiv.org/abs/2604.16009)：评什么：AI 元认知能力，区分模型判断自身表现的能力与据此控制行为的能力。核心思想：检验规模化是否同时提升自我评估和决策控制，而不是只看置信度或最终正确率。
- [ProEval](https://arxiv.org/abs/2604.23099)：在有限评测预算下主动发现失败并估计生成式 AI 的 benchmark 表现。核心思想：用不确定性感知的迁移代理模型选择或合成高信息量测试样本。
- [DESBench](https://arxiv.org/abs/2605.13172)：评估事件驱动工业调度中的层级多智能体协作。核心思想：用共享离散事件环境、部分可观测状态、耦合约束和多时间尺度决策，检验层级协调何时有效、何时失效。
- [MMRole](https://www.semanticscholar.org/paper/4d567080294013a63149f3782ca67c4a9d346194)：评测多模态角色扮演 agent；核心思想是把 persona 构建、多模态交互和角色一致性评估连接起来，使角色型 agent 不只在纯文本对话中接受测试。
- [Mosaic](https://doi.org/10.1145/3772363.3798830)：提供观察和评估多智能体系统性能的多层级框架；核心思想是在系统、个体智能体和交互层面组织评测，避免把多智能体行为压缩成单一最终结果分数。

## 1.16.4 Agent Harness

- [AgentScope](https://arxiv.org/abs/2402.14034)（[开源代码](https://github.com/agentscope-ai/agentscope)；[文档](https://doc.agentscope.io/)）：通用开源多 agent 框架，包含 agents、tools、skills、memory、planning、MCP/A2A 支持、human-in-the-loop 组件和评测工具，适合作为 MultiAgentBench 类跨任务评测的 harness 侧补充。
- [UFO3](https://arxiv.org/abs/2511.11332)（开源代码：未找到稳定公开仓库）：面向桌面、移动设备、服务器和边缘端点的跨设备数字 agent 编排系统；设计关键词：分布式任务 DAG、异步编排、显式控制与数据依赖。
- [HACN](https://arxiv.org/abs/2511.17586)：面向协作式多 agent 系统的层级自适应共识 harness。核心思想：通过局部集群、基于置信度的投票和全局共识策略路由任务，使通信成本、可扩展性和收敛性可随任务与 agent 表现调整。
- [Agent-Kernel](https://arxiv.org/abs/2512.01610)：面向 LLM 社会模拟的微内核多 Agent 框架。核心思路是解耦核心系统功能、模拟逻辑、认知过程、物理环境和动作执行，使大规模模拟能更可靠地改变群体、画像和环境规则。
- [ProAgent](https://arxiv.org/abs/2512.06721)：利用按需感知上下文的主动式 Agent harness。核心思路是结合分层感知、上下文抽取和主动辅助，使 Agent 能持续关注用户环境，同时避免始终承担高成本感知。
- [PRISM](https://arxiv.org/abs/2602.01532)：把主动介入建模为成本敏感选择性行动的 proactive-agent deliberation harness；设计关键词：接受概率校准门控、不确定性感知推理、用户负担控制。
- CrewAI（[开源代码](https://github.com/crewAIInc/crewAI)；[文档](https://docs.crewai.com/)；[官方 skills](https://github.com/crewAIInc/skills)）：基于角色的多 agent 编排框架，包含 crews、flows、tools 与可复用官方 skills，可作为跨任务协作类场景的实用开源基线。
- [Forage V2](https://arxiv.org/abs/2604.19837)：面向开放式任务的自治智能体学习组织框架。核心思想：隔离评估者与规划者角色，同时跨运行积累可复用知识、在不同能力模型间迁移，并防止知识退化。
- [Agent Capsules](https://arxiv.org/abs/2605.00410)：面向多智能体 LLM 流水线的质量门控粒度控制运行时。核心思想：度量协作开销，选择合并执行模式，并在滚动质量信号下降时退回更细粒度的智能体调度。

## 1.16.5 Skill
