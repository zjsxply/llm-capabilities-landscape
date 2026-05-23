# 4.4.5 Agent Harness

- [Drive Like A Human](https://arxiv.org/abs/2307.07162)（[开源代码](https://github.com/PJLab-ADG/DriveLikeAHuman)）：早期 HighwayEnv 中的闭环 LLM driving harness，可作为后续带记忆和反思的自动驾驶 agent 前身。
- [DiLu](https://arxiv.org/abs/2309.16292)（[开源代码](https://github.com/PJLab-ADG/DiLu)）：闭环 self-evolving driving framework，包含 environment、reasoning、reflection 和 memory modules，通过显式 agent loop 做驾驶决策，而不是单个 perception model。
- [Agent-Driver](https://arxiv.org/abs/2311.10813)（[开源代码](https://github.com/physical-superintelligence-lab/Agent-Driver)；[项目页](https://usc-gvl.github.io/Agent-Driver/)）：面向自动驾驶的 LLM cognitive agent，包含 function-call tools、cognitive memory、reasoning、task planning、motion planning 和 self-reflection。
- [Parallel Actor-Reasoner Framework](https://arxiv.org/abs/2503.00502)：LLM 驱动的自动驾驶交互 harness。核心思路是把较慢的 Reasoner 与交互记忆驱动的 Actor 分离，使车辆能表达意图并改进交互决策，而不必每个动作都依赖实时 LLM 推理。
- [LangCoop](https://arxiv.org/abs/2504.13406)：面向自动驾驶的语言协作 harness。核心思路是把车车协作信息压缩成简洁自然语言消息，并用结构化视觉语言推理，使联网驾驶 Agent 能以更低带宽协调。
- [AgentThink](https://arxiv.org/abs/2505.15298)：面向自动驾驶 VLM 的工具增强推理 harness。核心思路是构建驾驶工具库和结构化自验证推理数据，使 Agent 能在链式推理式的驾驶感知与决策任务中动态调用工具。
- [AGENTS-LLM](https://arxiv.org/abs/2507.13729)：用于生成挑战性交通场景的 agentic LLM framework。核心思想：用 LLM 驱动的场景增广为自动驾驶 agent 构造比固定场景库更困难、更多样的交通情形。
- [MTRDrive](https://arxiv.org/abs/2509.20843)：面向自动驾驶 corner case 的推理型 agent 框架，把程序化驾驶经验记忆检索和动态工具调用结合起来。核心思想：在驾驶经验、工具调用和主动决策之间形成闭环，让分布外场景按 agent 轨迹处理，而不是只做静态感知。
- [SafeCoop](https://arxiv.org/abs/2510.18123)：面向自然语言协同驾驶的 Agentic 防御 harness。核心思路是结合语义防火墙、语言-感知一致性检查、多源共识和空间坐标转换，检测并缓解针对 V2X 语言通信的攻击。
- [SimScale](https://arxiv.org/abs/2511.23369)：用于规模化学习驾驶的真实世界仿真 harness。核心思想是用大规模重建驾驶仿真让自动驾驶智能体接触更多样的情境，并在固定日志回放之外评估行为。
- [Dream2Drive](https://doi.org/10.1109/IJCNN64981.2025.11228910)：面向多任务驾驶的 LLM 车辆运动规划 agent。核心思想是组合 observation、short-term memory、long-term experience、planning 与 rethinking 模块，使驾驶决策能在真实规划任务中复用历史经验。
- [Agentic Fast-Slow Planning](https://arxiv.org/abs/2604.01681)：把慢速大模型推理与快速控制解耦的自动驾驶 agent harness。核心思想：先将场景压缩为自车中心拓扑，再映射成符号驾驶指令，并将指令接入实时 MPC 式控制，避免让语言模型直接生成脆弱轨迹。
