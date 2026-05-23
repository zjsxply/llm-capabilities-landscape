# 1.16.5 Agent Harness

- [AgentScope](https://arxiv.org/abs/2402.14034)（[开源代码](https://github.com/agentscope-ai/agentscope)；[文档](https://doc.agentscope.io/)）：通用开源多 agent 框架，包含 agents、tools、skills、memory、planning、MCP/A2A 支持、human-in-the-loop 组件和评测工具，适合作为 MultiAgentBench 类跨任务评测的 harness 侧补充。
- [ACNBP](https://arxiv.org/abs/2506.13590)：面向异构 Agent 的能力协商与绑定协议。核心思路是把发现、候选筛选、安全协商、能力证明和绑定承诺结构化，使开放多 Agent 系统无需预设同质接口也能互操作。
- [UFO3](https://arxiv.org/abs/2511.11332)（开源代码：未找到稳定公开仓库）：面向桌面、移动设备、服务器和边缘端点的跨设备数字 agent 编排系统；设计关键词：分布式任务 DAG、异步编排、显式控制与数据依赖。
- [HACN](https://arxiv.org/abs/2511.17586)：面向协作式多 agent 系统的层级自适应共识 harness。核心思想：通过局部集群、基于置信度的投票和全局共识策略路由任务，使通信成本、可扩展性和收敛性可随任务与 agent 表现调整。
- [Agent-Kernel](https://arxiv.org/abs/2512.01610)：面向 LLM 社会模拟的微内核多 Agent 框架。核心思路是解耦核心系统功能、模拟逻辑、认知过程、物理环境和动作执行，使大规模模拟能更可靠地改变群体、画像和环境规则。
- [ProAgent](https://arxiv.org/abs/2512.06721)：利用按需感知上下文的主动式 Agent harness。核心思路是结合分层感知、上下文抽取和主动辅助，使 Agent 能持续关注用户环境，同时避免始终承担高成本感知。
- [PRISM](https://arxiv.org/abs/2602.01532)：把主动介入建模为成本敏感选择性行动的 proactive-agent deliberation harness；设计关键词：接受概率校准门控、不确定性感知推理、用户负担控制。
- CrewAI（[开源代码](https://github.com/crewAIInc/crewAI)；[文档](https://docs.crewai.com/)；[官方 skills](https://github.com/crewAIInc/skills)）：基于角色的多 agent 编排框架，包含 crews、flows、tools 与可复用官方 skills，可作为跨任务协作类场景的实用开源基线。
- [Forage V2](https://arxiv.org/abs/2604.19837)：面向开放式任务的自治智能体学习组织框架。核心思想：隔离评估者与规划者角色，同时跨运行积累可复用知识、在不同能力模型间迁移，并防止知识退化。
- [Agent Capsules](https://arxiv.org/abs/2605.00410)：面向多智能体 LLM 流水线的质量门控粒度控制运行时。核心思想：度量协作开销，选择合并执行模式，并在滚动质量信号下降时退回更细粒度的智能体调度。
