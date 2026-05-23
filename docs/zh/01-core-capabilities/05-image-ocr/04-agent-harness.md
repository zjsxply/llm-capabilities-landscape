# 1.5.4 Agent Harness

- [VisProg](https://arxiv.org/abs/2211.11559)（[开源代码](https://github.com/allenai/visprog)）：把视觉任务转成“生成可执行程序 + 执行回填”的可复用 harness，弱化单模型端到端幻觉风险。
- [Visual ChatGPT](https://arxiv.org/abs/2303.04671)（[开源代码](https://github.com/microsoft/visual-chatgpt)）：多视觉工具协作的通用视觉 agent harness；典型闭环是 `plan -> call tools -> verify -> refine`。
- [ViperGPT](https://arxiv.org/abs/2303.08128)（[开源代码](https://github.com/cvlab-columbia/viper)）：以 Python 执行作为中间层的视觉推理 harness，把模型输出约束为可执行 API 组合。
- [MM-REACT](https://arxiv.org/abs/2303.11381)（[开源代码](https://github.com/microsoft/MM-REACT)）：多模态 ReAct 工作流；把视觉感知、推理与动作（工具调用）组织成可复用的提示控制流。
- [HuggingGPT](https://arxiv.org/abs/2303.17580)（[开源代码](https://github.com/microsoft/JARVIS)）：把多模态任务路由到工具/模型并编排执行的通用 agent 框架（包含视觉任务路由与组合）。
- [MDocAgent](https://arxiv.org/abs/2503.13964)（[开源代码](https://github.com/aiming-lab/MDocAgent)）：面向文档问答的多模态多 agent RAG 框架；把 text agent、image agent、critical agent、summary agent 等角色组合起来做跨模态证据整合。
- [ChartAgent](https://arxiv.org/abs/2507.06157)（开源代码：暂未见稳定公开官方仓库）：面向图表问答的 agentic workflow，常见做法是 `读图/OCR -> 表格化/结构化 -> 计算/校验 -> 作答` 的分阶段编排。
- [PyVision](https://arxiv.org/abs/2507.07998)（[项目页](https://agent-x.space/pyvision/)；[开源代码](https://github.com/agents-x-project/PyVision)）：面向视觉推理的动态工具 harness；让模型按任务生成、执行和修正 Python 图像处理工具，而不是依赖固定 toolset。
- [VProChart](https://arxiv.org/abs/2507.17209)（开源代码：暂未见稳定公开官方仓库）：面向图表推理的流程化方法，更强调把图表理解与计算/验证模块化以降低图表 hallucination。
- [Doc-Researcher](https://arxiv.org/abs/2510.21603)（开源代码：暂未见稳定公开官方仓库）：面向多模态文档 deep research 的多 agent 系统；把解析、分层检索、问题分解、证据累积和跨文档综合连接成迭代式 workflow。
- [DocAgent](https://aclanthology.org/2025.emnlp-main.893/)（[开源代码](https://github.com/lisun-ai/DocAgent)）：面向多模态长上下文文档理解的 agentic framework；强调记忆与 reviewer 机制，把文本、版面、图表、表格和图像证据统一到长文档推理链中。
- [ARIAL](https://arxiv.org/abs/2511.18192)（开源代码：暂未见稳定公开官方仓库）：面向 Document VQA 与答案定位的 agentic framework；通过 planner 编排 OCR、语义检索、答案生成和文本到区域对齐，同时输出答案与 bounding box 证据。
- [DocDancer](https://arxiv.org/abs/2601.05163)（开源代码：论文称开源，暂未确认稳定公开仓库）：把 DocQA 建模成工具驱动的信息寻求过程，显式区分 document exploration 与 answer synthesis，并用合成轨迹训练开放式文档 agent。
- [OCR-Agent](https://arxiv.org/abs/2602.21053)（[开源代码](https://github.com/AIGeeksGroup/OCR-Agent)）：面向 OCR/文档理解的专门 agent；强调 `OCR -> 结构化解析 -> 校验 -> 回填` 的迭代式工作流。
- [Doc-V*](https://arxiv.org/abs/2604.13731)（开源代码：暂未见稳定公开官方仓库）：面向多页 Document VQA 的 coarse-to-fine 交互式视觉推理 harness；核心思想是用页面级检索、区域级放大、证据验证和答案生成闭环替代一次性全页阅读。
