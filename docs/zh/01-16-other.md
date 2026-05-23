# 1.16 其它

> 上级章节：1. 基础能力

说明：本页收纳主轴较交叉、偏 meta-evaluation，或暂时还不足以单独形成一个稳定类别的 benchmark 与 harness。后续如果同类工作积累到足够密度，应再移入更具体的页面。

## 1.16.1 Bench

- [RoleMRC](https://arxiv.org/abs/2502.11387)：通过细粒度复合任务评测角色扮演与指令遵循；核心思想是检查角色型 agent 是否能在满足用户显式指令的同时保持 persona 约束。
- [STEER-ME](https://arxiv.org/abs/2502.13119)（数据集：[narunraman/steer_me](https://huggingface.co/datasets/narunraman/steer_me)）：评什么：LLM 的微观经济推理。核心思想：用非战略性经济决策设定诊断模型是否能推理激励、偏好和权衡，而不是只回答经济领域事实。
- [ThinkBench](https://arxiv.org/abs/2502.16268)（[开源代码](https://github.com/huangshulin123/ThinkBench)，[数据集](https://huggingface.co/datasets/jiuyinjiu/ThinkBench)）：评什么：动态分布外生成条件下的稳健 LLM 推理。核心思想：生成并评测新鲜 OOD 推理样本，降低答案泄漏和 benchmark 过拟合风险，并用同一协议比较 reasoning 与 non-reasoning 模型。
- [MMDT / Multimodal DecodingTrust](https://arxiv.org/abs/2503.14827)：评估多模态基础模型的安全性与可信度。核心思路是把有用性、公平性、隐私、鲁棒性和安全等维度纳入统一平台，避免只用通用任务准确率判断多模态系统。
- [CQ-Bench](https://arxiv.org/abs/2504.01127)：评测 LLM 是否理解隐含文化价值；核心思想是用相关价值未被直接说出的情境测试文化智能，为多语评测补充 culture reasoning 维度。
- [MMAU](https://aclanthology.org/2025.findings-naacl.267/)：评测跨多领域的综合 agent 能力。核心思想：把宽泛 agent 能力拆成可复用 benchmark suite，而不是强行归入网页、工具使用或代码类别。
- [AbsenceBench](https://arxiv.org/abs/2506.11440)（[开源代码](https://github.com/harvey-fin/absence-bench)，[数据集](https://huggingface.co/datasets/harveyfin/AbsenceBench)）：评什么：在长输入中发现被刻意删掉的信息。核心思想：用序列、诗歌和 GitHub pull request 中的“缺失项识别”补充 needle retrieval，暴露模型能找出现有事实但看不见遗漏的失败。
- [MultiAgentBench](https://aclanthology.org/2025.acl-long.421/)：评测 LLM agents 的协作与竞争。核心思想：在多智能体 benchmark 尚未足够密集到单独成页之前，先把交互协议和结果权衡作为明确可测对象记录下来。
- [SocialCC](https://doi.org/10.18653/v1/2025.acl-long.1594)：评什么：交互式 language agent 的文化能力。核心思想：把文化评测从静态问答推进到对话和互动场景，检查 agent 是否能适应社会语境和文化预期。
- [EffiEval](https://arxiv.org/abs/2508.09662)：通过基于能力覆盖的样本选择降低评测成本。核心思想：在只查询代表性 benchmark 样本的同时，尽量保持排名一致性与公平性。
- [Social Welfare Function Leaderboard](https://arxiv.org/abs/2510.01164)：评测 LLM agent 在稀缺社会资源分配中的决策；核心思想是用动态模拟同时比较集体效率与分配公平性，并以 ROI 和 Gini 类指标刻画权衡。
- [CorrectBench](https://arxiv.org/abs/2510.16062)（[项目页](https://correctbench.github.io/)，[数据集](https://huggingface.co/datasets/zeli2024/CorrectBench)）：评什么：LLM 推理的自我修正策略。核心思想：在多类推理任务上比较内在、外部和微调式修正设置，区分真正错误修复与重复错误或过度自信的错答。
- [Infinity-Chat](https://arxiv.org/abs/2510.22954)（[开源代码](https://github.com/liweijiang/artificial-hiveminds)，[数据集](https://huggingface.co/datasets/liweijiang/infinite-chats-taxonomy)）：评什么：开放式语言模型输出的多样性与同质化。核心思想：用包含大量合理答案空间的真实用户问题，衡量模型多次生成是否坍缩成相似的“蜂巢式”回答，而不是保持类似人类的表达差异。
- [InFerActive](https://arxiv.org/abs/2512.10234)：通过交互式推理树扩展人工评测。核心思想：让评审比较结构化行为路径，而不是逐条响应低效判断。
- [Auditing Multi-Agent Reasoning Trees](https://arxiv.org/abs/2602.09341)：审计多 agent 推理轨迹中的证据结构。核心思想：用围绕一致点与分歧点的局部验证，替代多数投票或通用 LLM-as-judge 聚合。
- [MEDLEY-BENCH](https://arxiv.org/abs/2604.16009)：评什么：AI 元认知能力，区分模型判断自身表现的能力与据此控制行为的能力。核心思想：检验规模化是否同时提升自我评估和决策控制，而不是只看置信度或最终正确率。
- [ProEval](https://arxiv.org/abs/2604.23099)：在有限评测预算下主动发现失败并估计生成式 AI 的 benchmark 表现。核心思想：用不确定性感知的迁移代理模型选择或合成高信息量测试样本。
- [MMRole](https://www.semanticscholar.org/paper/4d567080294013a63149f3782ca67c4a9d346194)：评测多模态角色扮演 agent；核心思想是把 persona 构建、多模态交互和角色一致性评估连接起来，使角色型 agent 不只在纯文本对话中接受测试。
- [Mosaic](https://doi.org/10.1145/3772363.3798830)：提供观察和评估多智能体系统性能的多层级框架；核心思想是在系统、个体智能体和交互层面组织评测，避免把多智能体行为压缩成单一最终结果分数。

## 1.16.2 Agent Harness

- [UFO3](https://arxiv.org/abs/2511.11332)（开源代码：未找到稳定公开仓库）：面向桌面、移动设备、服务器和边缘端点的跨设备数字 agent 编排系统；设计关键词：分布式任务 DAG、异步编排、显式控制与数据依赖。
- [PRISM](https://arxiv.org/abs/2602.01532)：把主动介入建模为成本敏感选择性行动的 proactive-agent deliberation harness；设计关键词：接受概率校准门控、不确定性感知推理、用户负担控制。
