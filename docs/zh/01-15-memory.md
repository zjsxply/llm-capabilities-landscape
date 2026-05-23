# 1.15 记忆

> 上级章节：1. 基础能力

说明：本节与 [1.10 长上下文](01-10-long-context.zh.md) 的边界是“是否跨交互持久化状态”。长上下文主要评估模型在一次 prompt 或一次任务窗口中读懂、定位、压缩和综合长输入的能力；记忆则评估 agent 是否能把事实、偏好、经验、程序性知识和失败轨迹写入外部或内部 memory，并在后续轮次、会话、任务或环境变化后正确检索、更新、合并和遗忘。

## 1.15.1 Leaderboard

- [LOCOMO](https://github.com/snap-research/locomo)：长期对话记忆评测入口，适合追踪多 session 对话事实、偏好与事件回忆能力。
- [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench)：面向增量交互式 agent memory 的公开代码与评测入口，适合比较外部 memory module、摘要 memory 与全上下文策略。
- [MemGUI-Bench](https://github.com/lgy0404/MemGUI-Bench)：移动 GUI agent 记忆评测入口，适合观察跨会话 GUI 任务中的 retention 与 cross-session learning。
- [EvoMemBench](https://github.com/DSAIL-Memory/EvoMemBench)：自演化记忆评测入口，适合比较 in-episode/cross-episode 与 knowledge/execution 两类记忆。

## 1.15.2 Bench

- [LOCOMO](https://arxiv.org/abs/2402.17753)（[开源代码](https://github.com/snap-research/locomo)）：评什么：极长程对话记忆。核心思想：把多 session 对话中的事实、偏好和事件作为检索对象，评估 agent 是否能长期一致地使用历史信息。
- [LongMemEval](https://arxiv.org/abs/2410.10813)：评什么：长对话与个人助理场景中的记忆问答。核心思想：把长历史拆成局部事实、全局偏好和跨时间推理问题，测试模型或 memory system 是否能从冗长交互中定位并组合相关记忆。
- [MemBench](https://arxiv.org/abs/2506.21605)（[开源代码](https://github.com/import-myself/Membench)）：评什么：LLM-based agent 的情节记忆、语义记忆与程序性记忆。核心思想：把“参与式记忆”和“观察式记忆”分开建模，并引入大规模噪声会话测试长期记忆检索。
- [MemoryAgentBench](https://arxiv.org/abs/2507.05257)（[开源代码](https://github.com/HUST-AI-HYZ/MemoryAgentBench)）：评什么：多轮增量交互中的 agent 记忆写入、更新与召回。核心思想：不把所有历史一次性塞进 prompt，而是按 interaction stream 逐步给信息，检验 memory module 是否能随状态演化。
- [MemGUI-Bench](https://arxiv.org/abs/2602.06075)（[开源代码](https://github.com/lgy0404/MemGUI-Bench)）：评什么：移动 GUI agent 的记忆能力。核心思想：用跨会话、跨应用和动态环境任务专门测 memory retention 与 cross-session learning，连接记忆能力与 GUI 行动可靠性。
- [MemoryArena](https://arxiv.org/abs/2602.16313)：评什么：多 session、相互依赖任务中的 agent memory。核心思想：把跨会话依赖、互相干扰的事实与后续行动绑定起来，评估 agent 能否在长期交互中稳定维护可用记忆。
- [YC-Bench](https://arxiv.org/abs/2604.01212)：评什么：长期规划与一致执行中的状态记忆。核心思想：让 agent 在持续经营类任务中反复使用历史目标、资源状态和中间决策，观察 context truncation、scratchpad 与 memory 策略的真实收益。
- [LongMemEval-V2](https://arxiv.org/abs/2605.12493)：评什么：面向“有经验同事”场景的长期 agent memory。核心思想：把长期交互记忆从问答 recall 推向工作场景中的经验复用、偏好保持和上下文迁移。
- [EvoMemBench](https://arxiv.org/abs/2605.18421)（[开源代码](https://github.com/DSAIL-Memory/EvoMemBench)）：评什么：agent 记忆的自演化能力。核心思想：按 `in-episode / cross-episode` × `knowledge / execution` 切分记忆任务，更系统地测记忆策略。
- [MINTEval](https://arxiv.org/abs/2605.18565)：评什么：长程、频繁更新、互相干扰的信息记忆。核心思想：用多目标干扰把静态 recall 压力升级到动态记忆与聚合推理。
- [MemGym](https://arxiv.org/abs/2605.20833)：评什么：长时程 agent memory 环境。核心思想：通过 Memory-Isolated Tasks 把记忆写入、保持和后续使用从普通任务能力中隔离出来，并用 MEMGYM-DR、MEMGYM-SWE 等场景连接 deep research 与软件任务。

## 1.15.3 Agent Harness

- [Reflexion](https://arxiv.org/abs/2303.11366)（[开源代码](https://github.com/noahshinn/reflexion)）：把失败轨迹转成语言反馈和 episodic memory，再用于下一轮尝试；它是“经验记忆提升 agent 反复尝试”的早期代表。
- [Generative Agents](https://arxiv.org/abs/2304.03442)（[开源代码](https://github.com/joonspk-research/generative_agents)）：把记忆流、反思和计划循环组合成长期行为代理，是后续 agent memory 论文的常见起点。
- [MemoryBank](https://arxiv.org/abs/2305.10250)（[开源代码](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)）：把长期记忆写入、检索和人格/偏好更新做成对话代理组件，适合追踪跨轮一致性。
- [Voyager](https://arxiv.org/abs/2305.16291)（[开源代码](https://github.com/MineDojo/Voyager)）：把探索经验沉淀为可调用 skill library 与长期记忆；虽然任务是 Minecraft，但它把“经验写入 -> 检索复用 -> 能力累积”做成了 agent harness 的经典形态。
- [MemGPT](https://arxiv.org/abs/2310.08560)（[开源代码](https://github.com/cpacker/MemGPT)）：把长上下文问题转化为显式 memory tier 与调度策略，形成可复用的长程代理 runtime。
- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429)（开源代码：未找到稳定公开仓库）：面向多步骤 agent 工作流的记忆机制；核心思想：让 agent 在任务执行中显式记录关键状态、工具结果和决策理由，后续步骤按需检索而非全量回灌。
- [Zep](https://arxiv.org/abs/2501.13956)（[开源代码](https://github.com/getzep/graphiti)）：面向 agent memory 的时间知识图谱架构；核心思想：把事件、实体、关系和时间演化组织成可查询图，服务长期个性化和跨会话召回。
- [A-MEM](https://arxiv.org/abs/2502.12110)（[开源代码](https://github.com/WujiangXu/A-mem)）：面向 agent 的动态记忆组织框架。核心思想：把记忆片段写成可链接、可演化的知识结构，支持后续检索、重组与反思。
- [Mem0](https://arxiv.org/abs/2504.19413)（[开源代码](https://github.com/mem0ai/mem0)）：面向生产 agent 的可扩展长期记忆层。核心思想：用自动抽取、更新和检索的 memory pipeline 降低全量历史上下文依赖。
- [MemoryOS](https://arxiv.org/abs/2506.06326)（[开源代码](https://github.com/BAI-LAB/MemoryOS)）：把 agent memory 拆成 storage、update、retrieve 与 consolidation 等 OS-like 操作；适合作为长期交互任务中的通用 memory runtime。
- [MemOS](https://arxiv.org/abs/2507.03724)（[开源代码](https://github.com/MemTensor/MemOS)）：把长期记忆、混合检索、跨任务经验复用和 token 节省做成 self-evolving memory OS，适合生产 agent 的 memory-first runtime。
- [MIRIX](https://arxiv.org/abs/2507.07957)（[开源代码](https://github.com/Mirix-AI/MIRIX)）：多代理记忆系统。核心思想：用专门的记忆管理 agent 维护短期、情景、语义与程序性记忆，服务长程任务中的跨会话调用。
- [Hindsight](https://arxiv.org/abs/2512.12818)（[开源代码](https://github.com/vectorize-io/hindsight)）：面向生产 agent 的 memory harness。核心思想：在任务后把执行轨迹沉淀为可检索经验，并在后续任务中通过 recall 与 reflection 复用。
- [UMA](https://arxiv.org/abs/2602.18493)：把记忆操作与问答统一到单一 policy。核心思想：用显式 Memory Bank 做 CRUD 写记忆，专治超长流式状态跟踪。
- [True Memory](https://arxiv.org/abs/2605.04897)：对“存储不等于记忆”的系统化回应。核心思想：把 memory system 的关键能力定义为抽取、组织、更新、检索、遗忘和行动绑定，而不只是把历史文本放进向量库。

## 1.15.4 Skill

- [deep-agents-memory](https://skills.sh/langchain-ai/langchain-skills/deep-agents-memory) 适合给 deep agent 接入可检索的长期记忆层。
- [remembering-conversations](https://skills.sh/obra/episodic-memory/remembering-conversations) 适合保存和回忆多轮对话中的用户事实与偏好。
- [memory-management](https://skills.sh/anthropics/knowledge-work-plugins/memory-management) 适合把知识工作中的长期偏好、项目状态和工作习惯显式维护起来。
- [agent-memory-systems](https://skills.sh/sickn33/antigravity-awesome-skills/agent-memory-systems) 适合设计 memory store、retriever、summarizer 和更新策略。
- [mem0-mcp](https://skills.sh/mem0ai/mem0/mem0-mcp) 适合通过 MCP 工具把 mem0 记忆接入 Claude Code、Codex、Cursor 等运行时。
- [mem0-codex](https://skills.sh/mem0ai/mem0/mem0-codex) 适合 Codex 风格任务中的自动记忆检索、关键学习写入和 session state 保存。
