# 2.6.5 Agent Harness

- AutoGPT（[开源代码](https://github.com/Significant-Gravitas/AutoGPT)）：持续运行式自治代理框架，把任务队列、工具调用、长期执行与结果回写组织成可反复迭代的 agent loop，是公开生态里最早一批强调 long-running autonomy 的实现。
- [Voyager](https://arxiv.org/abs/2305.16291)（[开源代码](https://github.com/MineDojo/Voyager)）以 Minecraft 为平台做“终身学习”式长时程代理，核心 harness 是 `自动课程生成 + skill library + 可执行反馈` 的长期自增量闭环。
- [MemGPT](https://arxiv.org/abs/2310.08560)（[开源代码](https://github.com/cpacker/MemGPT)）把长时运行的核心矛盾显式化为“记忆管理/上下文调度”问题，通过外部 memory 与检索将对话/任务状态从上下文窗口中外置。
- LangGraph（[开源代码](https://github.com/langchain-ai/langgraph)）把 long-running agent 的控制流显式化为 state graph，并提供 checkpointer 等机制，适合把 `checkpoint/rollback/分支恢复/可重复执行` 写进运行时。
- [SeePlanAct (SPA)](https://arxiv.org/abs/2407.15711)（[开源代码](https://github.com/oriyor/assistantbench)；AssistantBench 配套 web agent，在 SeeAct 之上加入显式 planning 与 memory 组件，用于长程网页任务中的阶段计划、信息传递和最终答案聚合）
- [Magentic-One](https://arxiv.org/abs/2411.04468)（[开源代码](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one)；[当前文档](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/magentic-one.html)）：通用多智能体 harness，包含 orchestrator、web surfer、file surfer、coder 和终端式执行 agent，适合长时程 web/file/code 任务以及 GAIA、AssistantBench 类工作流。
- [HomerAgent](https://arxiv.org/abs/2508.09124)（[开源代码](https://github.com/microsoft/OdysseyBench)）是 OdysseyBench 配套的长程办公 workflow agent，用显式记忆维护阶段结果，适合分析长期任务中的上下文遗忘、错误复用和阶段间依赖失败。
- [ARE](https://arxiv.org/abs/2509.17158)（[开源代码](https://github.com/facebookresearch/meta-agents-research-environments)）把 long-running harness 做成动态环境运行时，支持异步事件、状态演化、外部工具和评测日志，适合研究持续执行中的计划更新与上下文维护。
- Deep Agents（[开源代码](https://github.com/langchain-ai/deepagents)；[文档](https://docs.langchain.com/oss/python/deepagents/overview)）：batteries-included 长程 agent harness，包含 planning、subagents、filesystem state、上下文管理、shell access、持久记忆、人工审批、skills、tools 与 MCP 集成。
