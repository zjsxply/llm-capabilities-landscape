# 4.4 自动驾驶

> 上级章节：4. 多模态

说明：本页收纳自动驾驶、交通场景、车载座舱、车内助手以及驾驶视频 world model 相关评测。一般机器人操作和导航仍保留在 [2.11 具身与 VLA Agent](02-11-embodied-vla.md)。

## 4.4.1 Leaderboard

- [NAVSIM Public Leaderboard](https://huggingface.co/spaces/AGC2025/e2e-driving-navhard)：面向 NAVSIM 场景的公开端到端驾驶规划榜单。
- [CARLA Autonomous Driving Leaderboard](https://leaderboard.carla.org/)：面向仿真中自动驾驶 agent 的公开闭环基准榜单。

## 4.4.2 Survey

- [A Survey on Multimodal Large Language Models for Autonomous Driving](https://arxiv.org/abs/2311.12320)：关于感知、推理、规划、数据集与基准的基础综述。
- [A Survey for Foundation Models in Autonomous Driving](https://arxiv.org/abs/2402.01105)：回顾基础模型在感知、预测、规划、仿真与评测中的使用。
- [A Survey of World Models for Autonomous Driving](https://arxiv.org/abs/2501.11260)：综述用于预测、仿真、规划与评测的驾驶 world model。
- [Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances](https://arxiv.org/abs/2502.16804)：回顾通信、协作、场景推理与决策支持。
- [A Survey on Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2506.24044)：连接感知、语言支撑推理与动作生成。

## 4.4.3 Bench

- [A Comprehensive LLM-powered Framework for Driving Intelligence Evaluation](https://arxiv.org/abs/2503.05164)：评测复杂交通环境中的 driving behavior intelligence。核心思想是用专业驾驶员和乘客构建的自然语言评价数据，在低层感知指标之外衡量自动驾驶行为。
- [SCD-Bench](https://arxiv.org/abs/2503.06497)：评测自动驾驶 VLM 的安全认知能力。核心思路是把交互式驾驶场景、半自动专家修订标注和自动评分流程结合起来，使安全关键推理不再只由普通感知准确率衡量。
- [Capability-Driven Scenario Understanding Evaluation](https://arxiv.org/abs/2503.11400)：评估多模态大模型的自动驾驶场景理解能力。核心思路：按能力维度组织驾驶场景理解评测，从而区分感知、上下文推理和决策相关理解中的失败。
- [AutoDrive-QA](https://arxiv.org/abs/2503.15778)：用多项选择问答评测城市自动驾驶场景中的视觉语言模型。核心思想：把开放式驾驶问答转为标准化选择题，并用驾驶域误解、传感器误读、逻辑错误、计算疏漏与歧义构造干扰项。
- [RealEngine](https://arxiv.org/abs/2505.16902)：提供用于评测自动驾驶 Agent 的真实感仿真框架。核心思路是结合多模态感知、真实场景渲染、闭环轨迹、多样交通场景、多 Agent 交互和可扩展执行，使驾驶 Agent 评测更可控也更接近真实环境。
- [Drive4C](https://doi.org/10.1109/CVPRW67362.2025.00371)：面向语言引导自动驾驶的闭环基准，用于检验基础模型能力能否转化为实际驾驶行为。
- [DriveAction](https://arxiv.org/abs/2506.05667)：评测 VLA models 的类人驾驶决策。核心思想是基于多样真实驾驶场景构造 action-driven QA，并用驾驶员行为中的离散动作标签显式衡量决策偏好和场景覆盖。
- [STSBench](https://arxiv.org/abs/2506.06218)：评什么：自动驾驶场景中多模态大语言模型的时空场景理解。核心思想：检查模型是否能围绕动态驾驶场景和时间关系推理，而不只是分类静态道路图像。
- [AD^2-Bench](https://arxiv.org/abs/2506.09557)：评什么：恶劣条件下自动驾驶场景中的多模态大语言模型。核心思想：用层级 chain-of-thought 式任务检查模型是否能推理受损驾驶场景，而不只是处理干净视觉输入。
- [PDB-Eval](https://arxiv.org/abs/2507.18447)：评测多模态模型对个性化驾驶行为的描述与解释能力。核心思想：用解释和 QA 组件测试时序驾驶行为理解，补充一般驾驶场景感知基准。
- [Bench2ADVLM](https://arxiv.org/abs/2508.02028)：面向自动驾驶视觉语言模型的闭环基准。核心思路：在闭环中评估与驾驶相关的感知、推理和决策行为，而不只评分静态场景理解。
- [DriveQA](https://arxiv.org/abs/2508.21824)：通过文本和视觉问题评测 LLM 与 MLLM 的驾驶知识。核心思路是系统覆盖交通规则、标志、路权、数值推理和空间布局，使驾驶 Agent 在普通场景理解数据集中少见的边界情况上接受测试。
- [DriveE2E](https://arxiv.org/abs/2509.23922)：通过 real-to-simulation 场景迁移构建的端到端自动驾驶闭环基准。核心思想：在 CARLA 式评测中回放真实路口交通，使驾驶 agent 面对真实动态场景，而不是手工脚本化场景。
- [ODVBench](https://arxiv.org/abs/2509.24871)：作为 StreamForest 工作的一部分，评测自动驾驶场景中的在线视频理解。核心思想：用驾驶视频测试模型在时间状态、场景变化和持久事件记忆下的泛化能力。
- [Evaluating Video Models as Simulators of Multi-Person Pedestrian Trajectories](https://arxiv.org/abs/2510.20182)：评测视频模型能否模拟多人行人轨迹。核心思想：把社会运动和轨迹一致性作为评测目标，使视频生成不只按视觉逼真度打分，而是按是否可作为模拟器来判断。
- [VehicleWorld](https://aclanthology.org/2025.findings-emnlp.23/)：评什么：智能车舱交互中的 API agent。核心思想：提供可执行车辆模块、API、属性和实时状态，使 agent 必须在紧耦合子系统中建立环境认知并从工具调用错误中恢复。
- [AIGV-Bench](https://arxiv.org/abs/2512.06376)：评测 AI 生成驾驶视频是否足以支撑自动驾驶训练与评估；核心思想是诊断视觉伪影、不合理运动和交通语义违规，并衡量这些问题对下游感知任务的影响。
- [Intention-Drive](https://arxiv.org/abs/2512.12302)：评测从高层人类意图到端到端自动驾驶动作的能力。核心思想：把复杂自然语言意图与传感器数据配对，并用 Imagined Future Alignment 衡量语义目标是否被满足，而不只看几何轨迹精度。
- [DrivingGen](https://arxiv.org/abs/2601.01528)：评测自动驾驶场景中的生成式视频 world model。核心思想：用驾驶场景动态与可控性要求检验生成未来是否能服务具身规划，而不只是视觉上逼真。
- [AutoDriDM](https://arxiv.org/abs/2601.14702)：面向自动驾驶中 VLM 决策的可解释 benchmark。核心思想：评估视觉语言模型是否能产生有 grounding 且可解释的驾驶决策，而不只是输出感知标签。
- [AgentDrive](https://arxiv.org/abs/2601.16964)：用 LLM 生成的驾驶场景评测自主系统中的 agentic reasoning；核心思想是以开放场景数据测试 agent 对自主系统情境的推理能力，而不只是对静态驾驶场景做分类。
- [ScenePilot-4K](https://arxiv.org/abs/2601.19582)：评测第一视角自动驾驶场景中的 vision-language model。核心思想：用大规模 egocentric driving 数据和 benchmark 任务，测试模型是否能从车辆视角理解与驾驶相关的场景证据。
- [DriveCombo](https://arxiv.org/abs/2603.01637)：评测自动驾驶中的组合式交通规则推理。核心思路是用五级认知阶梯测试模型从单规则理解到多规则整合与冲突消解的能力，覆盖文本和视觉驾驶场景。
- [VehicleMemBench](https://arxiv.org/abs/2603.23840)：评什么：车载 agent 中多用户长期记忆。核心思想：让记忆影响模拟车载助手中的可执行工具状态结果，暴露偏好冲突和按用户绑定的召回失败。

## 4.4.4 Agent Harness

- [Drive Like A Human](https://arxiv.org/abs/2307.07162)（[开源代码](https://github.com/PJLab-ADG/DriveLikeAHuman)）：早期 HighwayEnv 中的闭环 LLM driving harness，可作为后续带记忆和反思的自动驾驶 agent 前身。
- [DiLu](https://arxiv.org/abs/2309.16292)（[开源代码](https://github.com/PJLab-ADG/DiLu)）：闭环 self-evolving driving framework，包含 environment、reasoning、reflection 和 memory modules，通过显式 agent loop 做驾驶决策，而不是单个 perception model。
- [Agent-Driver](https://arxiv.org/abs/2311.10813)（[开源代码](https://github.com/physical-superintelligence-lab/Agent-Driver)；[项目页](https://usc-gvl.github.io/Agent-Driver/)）：面向自动驾驶的 LLM cognitive agent，包含 function-call tools、cognitive memory、reasoning、task planning、motion planning 和 self-reflection。
- [Parallel Actor-Reasoner Framework](https://arxiv.org/abs/2503.00502)：LLM 驱动的自动驾驶交互 harness。核心思路是把较慢的 Reasoner 与交互记忆驱动的 Actor 分离，使车辆能表达意图并改进交互决策，而不必每个动作都依赖实时 LLM 推理。
- [AgentThink](https://arxiv.org/abs/2505.15298)：面向自动驾驶 VLM 的工具增强推理 harness。核心思路是构建驾驶工具库和结构化自验证推理数据，使 Agent 能在链式推理式的驾驶感知与决策任务中动态调用工具。
- [AGENTS-LLM](https://arxiv.org/abs/2507.13729)：用于生成挑战性交通场景的 agentic LLM framework。核心思想：用 LLM 驱动的场景增广为自动驾驶 agent 构造比固定场景库更困难、更多样的交通情形。
- [MTRDrive](https://arxiv.org/abs/2509.20843)：面向自动驾驶 corner case 的推理型 agent 框架，把程序化驾驶经验记忆检索和动态工具调用结合起来。核心思想：在驾驶经验、工具调用和主动决策之间形成闭环，让分布外场景按 agent 轨迹处理，而不是只做静态感知。
- [SafeCoop](https://arxiv.org/abs/2510.18123)：面向自然语言协同驾驶的 Agentic 防御 harness。核心思路是结合语义防火墙、语言-感知一致性检查、多源共识和空间坐标转换，检测并缓解针对 V2X 语言通信的攻击。
- [Dream2Drive](https://doi.org/10.1109/IJCNN64981.2025.11228910)：面向多任务驾驶的 LLM 车辆运动规划 agent。核心思想是组合 observation、short-term memory、long-term experience、planning 与 rethinking 模块，使驾驶决策能在真实规划任务中复用历史经验。
- [Agentic Fast-Slow Planning](https://arxiv.org/abs/2604.01681)：把慢速大模型推理与快速控制解耦的自动驾驶 agent harness。核心思想：先将场景压缩为自车中心拓扑，再映射成符号驾驶指令，并将指令接入实时 MPC 式控制，避免让语言模型直接生成脆弱轨迹。

## 4.4.5 Skill

- [RoboSafe-Lab AD Safety Research Skills](https://github.com/RoboSafe-Lab/ad-safety-research-skills) 提供面向自动驾驶安全研究的 Claude Code skills，覆盖 AD foundation models、scenario analysis、experiment design 和 generative-model workflows；这些是 agent-readable research skills，而不是 learned driving policy primitives。
