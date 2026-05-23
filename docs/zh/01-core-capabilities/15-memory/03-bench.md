# 1.15.3 Bench

- [LOCOMO](https://arxiv.org/abs/2402.17753)（[开源代码](https://github.com/snap-research/locomo)）：评什么：极长程对话记忆。核心思想：把多 session 对话中的事实、偏好和事件作为检索对象，评估 agent 是否能长期一致地使用历史信息。
- [MemSim](https://arxiv.org/abs/2409.20163)（[开源代码](https://github.com/nuster1128/MemSim)）：评什么：LLM 个人助理的记忆行为。核心思想：用 Bayesian simulator 在受控交互历史下衡量记忆更新、检索和个性化助理行为。
- [LongMemEval](https://arxiv.org/abs/2410.10813)：评什么：长对话与个人助理场景中的记忆问答。核心思想：把长历史拆成局部事实、全局偏好和跨时间推理问题，测试模型或 memory system 是否能从冗长交互中定位并组合相关记忆。
- [MemBench](https://arxiv.org/abs/2506.21605)（[开源代码](https://github.com/import-myself/Membench)）：评什么：LLM-based agent 的情节记忆、语义记忆与程序性记忆。核心思想：把“参与式记忆”和“观察式记忆”分开建模，并引入大规模噪声会话测试长期记忆检索。
- [MemoryAgentBench](https://arxiv.org/abs/2507.05257)（[开源代码](https://github.com/HUST-AI-HYZ/MemoryAgentBench)）：评什么：多轮增量交互中的 agent 记忆写入、更新与召回。核心思想：不把所有历史一次性塞进 prompt，而是按 interaction stream 逐步给信息，检验 memory module 是否能随状态演化。
- [MemGUI-Bench](https://arxiv.org/abs/2602.06075)（[开源代码](https://github.com/lgy0404/MemGUI-Bench)）：评什么：移动 GUI agent 的记忆能力。核心思想：用跨会话、跨应用和动态环境任务专门测 memory retention 与 cross-session learning，连接记忆能力与 GUI 行动可靠性。
- [MemoryArena](https://arxiv.org/abs/2602.16313)：评什么：多 session、相互依赖任务中的 agent memory。核心思想：把跨会话依赖、互相干扰的事实与后续行动绑定起来，评估 agent 能否在长期交互中稳定维护可用记忆。
- [AMA-Bench](https://arxiv.org/abs/2602.22769)：评什么：agentic applications 中的长程记忆。核心思想：使用真实与合成 agent 轨迹，而不只用对话历史，并提供 AMA-Agent 作为 memory baseline。
- [AlpsBench](https://arxiv.org/abs/2603.26680)：评什么：真实对话记忆与偏好对齐中的个性化。核心思想：覆盖记忆生命周期中的抽取、更新、检索和使用。
- [BEHEMOTH](https://arxiv.org/abs/2604.11610)：评什么：跨异质任务的记忆抽取。核心思想：评分被抽取记忆是否能改善下游个性化、问题解决和 agentic task 表现。
- [Trojan Hippo](https://arxiv.org/abs/2605.01970)：评什么：持久记忆攻击与防御。核心思想：把 tool-call payload 植入 memory backend，测试后续检索是否导致数据外泄或触发不安全动作。
- [LongMemEval-V2](https://arxiv.org/abs/2605.12493)：评什么：面向“有经验同事”场景的长期 agent memory。核心思想：把长期交互记忆从问答 recall 推向工作场景中的经验复用、偏好保持和上下文迁移。
- [GroupMemBench](https://arxiv.org/abs/2605.14498)：评什么：多人对话中的 agent memory。核心思想：用图接地合成群聊和按提问者绑定的对抗查询，测试 speaker-grounded belief tracking、群体动态、受众适配词汇、多跳回忆、知识更新、歧义、时间推理和拒答。
- [EvoMemBench](https://arxiv.org/abs/2605.18421)（[开源代码](https://github.com/DSAIL-Memory/EvoMemBench)）：评什么：agent 记忆的自演化能力。核心思想：按 `in-episode / cross-episode` × `knowledge / execution` 切分记忆任务，更系统地测记忆策略。
- [MINTEval](https://arxiv.org/abs/2605.18565)：评什么：长程、频繁更新、互相干扰的信息记忆。核心思想：用多目标干扰把静态 recall 压力升级到动态记忆与聚合推理。
- [MemGym](https://arxiv.org/abs/2605.20833)：评什么：长时程 agent memory 环境。核心思想：通过 Memory-Isolated Tasks 把记忆写入、保持和后续使用从普通任务能力中隔离出来，并用 MEMGYM-DR、MEMGYM-SWE 等场景连接 deep research 与软件任务。
