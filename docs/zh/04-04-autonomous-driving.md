# 4.4 自动驾驶

> 上级章节：4. 多模态

说明：本页收纳自动驾驶、交通场景、车载座舱、车内助手以及驾驶视频 world model 相关评测。一般机器人操作和导航仍保留在 [2.11 具身与 VLA Agent](02-11-embodied-vla.md)。

## 4.4.1 Bench

- [Capability-Driven Scenario Understanding Evaluation](https://arxiv.org/abs/2503.11400)：评估多模态大模型的自动驾驶场景理解能力。核心思路：按能力维度组织驾驶场景理解评测，从而区分感知、上下文推理和决策相关理解中的失败。
- [Drive4C](https://doi.org/10.1109/CVPRW67362.2025.00371)：面向语言引导自动驾驶的闭环基准，用于检验基础模型能力能否转化为实际驾驶行为。
- [STSBench](https://arxiv.org/abs/2506.06218)：评什么：自动驾驶场景中多模态大语言模型的时空场景理解。核心思想：检查模型是否能围绕动态驾驶场景和时间关系推理，而不只是分类静态道路图像。
- [AD^2-Bench](https://arxiv.org/abs/2506.09557)：评什么：恶劣条件下自动驾驶场景中的多模态大语言模型。核心思想：用层级 chain-of-thought 式任务检查模型是否能推理受损驾驶场景，而不只是处理干净视觉输入。
- [Bench2ADVLM](https://arxiv.org/abs/2508.02028)：面向自动驾驶视觉语言模型的闭环基准。核心思路：在闭环中评估与驾驶相关的感知、推理和决策行为，而不只评分静态场景理解。
- [ODVBench](https://arxiv.org/abs/2509.24871)：作为 StreamForest 工作的一部分，评测自动驾驶场景中的在线视频理解。核心思想：用驾驶视频测试模型在时间状态、场景变化和持久事件记忆下的泛化能力。
- [Evaluating Video Models as Simulators of Multi-Person Pedestrian Trajectories](https://arxiv.org/abs/2510.20182)：评测视频模型能否模拟多人行人轨迹。核心思想：把社会运动和轨迹一致性作为评测目标，使视频生成不只按视觉逼真度打分，而是按是否可作为模拟器来判断。
- [VehicleWorld](https://aclanthology.org/2025.findings-emnlp.23/)：评什么：智能车舱交互中的 API agent。核心思想：提供可执行车辆模块、API、属性和实时状态，使 agent 必须在紧耦合子系统中建立环境认知并从工具调用错误中恢复。
- [AIGV-Bench](https://arxiv.org/abs/2512.06376)：评测 AI 生成驾驶视频是否足以支撑自动驾驶训练与评估；核心思想是诊断视觉伪影、不合理运动和交通语义违规，并衡量这些问题对下游感知任务的影响。
- [DrivingGen](https://arxiv.org/abs/2601.01528)：评测自动驾驶场景中的生成式视频 world model。核心思想：用驾驶场景动态与可控性要求检验生成未来是否能服务具身规划，而不只是视觉上逼真。
- [AutoDriDM](https://arxiv.org/abs/2601.14702)：面向自动驾驶中 VLM 决策的可解释 benchmark。核心思想：评估视觉语言模型是否能产生有 grounding 且可解释的驾驶决策，而不只是输出感知标签。
- [AgentDrive](https://arxiv.org/abs/2601.16964)：用 LLM 生成的驾驶场景评测自主系统中的 agentic reasoning；核心思想是以开放场景数据测试 agent 对自主系统情境的推理能力，而不只是对静态驾驶场景做分类。
- [ScenePilot-4K](https://arxiv.org/abs/2601.19582)：评测第一视角自动驾驶场景中的 vision-language model。核心思想：用大规模 egocentric driving 数据和 benchmark 任务，测试模型是否能从车辆视角理解与驾驶相关的场景证据。
- [VehicleMemBench](https://arxiv.org/abs/2603.23840)：评什么：车载 agent 中多用户长期记忆。核心思想：让记忆影响模拟车载助手中的可执行工具状态结果，暴露偏好冲突和按用户绑定的召回失败。

## 4.4.2 Agent Harness

- [AGENTS-LLM](https://arxiv.org/abs/2507.13729)：用于生成挑战性交通场景的 agentic LLM framework。核心思想：用 LLM 驱动的场景增广为自动驾驶 agent 构造比固定场景库更困难、更多样的交通情形。
