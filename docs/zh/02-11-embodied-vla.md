# 2.11 具身与 VLA Agent

> 上级章节：2. 基础 Agent

说明：本类覆盖具身智能与 vision-language-action 场景，模型需要在交互式物理、模拟、游戏或机器人环境中把感知、语言、规划与动作连接起来。纯 GUI 计算机操作仍放在 [2.5 计算机操作](02-05-computer-use-gui.md)，被动空间/视频理解则保留在对应基础能力页。

## 2.11.1 Leaderboard

- [VideoGameBench Leaderboard](https://vgbench.com/#leaderboard)：视频游戏环境中的具身 agent 感知、导航、操作与规划持续榜单；适合跟踪能在可执行视觉世界中行动的模型与 scaffold，而不是只看静态截图。

## 2.11.2 Bench

- [CALVIN](https://arxiv.org/abs/2112.03227)：评测语言条件下的长程机器人操作。核心思想：用模拟桌面环境和语言指令测试 agent 是否能在长时程中组合操作技能。
- [MineDojo](https://arxiv.org/abs/2206.08853)：评测 Minecraft 中的开放式具身 agent，并引入互联网规模知识资源。核心思想：用丰富、长程的 sandbox 环境测试语言目标下的探索、工具使用、合成、导航和任务完成。
- [VIMA-Bench](https://arxiv.org/abs/2210.03094)：评测多模态提示下的通用机器人操作。核心思想：用文本、图像和对象引用组合描述操作任务，比纯语言条件控制更贴近 vision-language-action grounding。
- [LIBERO](https://arxiv.org/abs/2306.03310)：评测终身机器人学习中的知识迁移。核心思想：把机器人操作任务组织成多个 suite，测试 agent 是否能跨对象、布局和任务族复用技能并适应变化。
- [VideoGameBench](https://vgbench.com/#leaderboard)：评测视频游戏环境中的具身感知、导航、操作与规划。核心思想：把空间理解放进可行动的游戏世界中，用任务完成与轨迹质量评估 agent 是否能把视觉空间关系转成动作。
- [WorldModelBench](https://arxiv.org/abs/2502.20694)：评测视频生成模型是否具备可用 world model 能力。核心思想：用人工标注的 violation 和学习型评判器测试指令遵循与物理一致性，面向机器人和自动驾驶等应用域。
- [OvercookedV2](https://arxiv.org/abs/2503.17821)：在 Overcooked 风格的具身多智能体环境中评测 zero-shot coordination。核心思想：压力测试 agent 是否能推断队友行为、分工协作，并在可执行协作任务中从配合失败中恢复。
- [WorldScore](https://arxiv.org/abs/2504.00983)：提供统一的世界生成评测基准。核心思路是从任务相关的一致性与动力学角度比较生成世界，使世界生成质量能够面向下游具身应用进行衡量。
- [EWMBench](https://arxiv.org/abs/2505.09694)：从场景一致性、运动正确性和语义对齐评测 embodied world model。核心思想：用 curated dataset 和评测工具检查生成动态是否满足具身任务所需的物理 grounding 与动作一致性。
- [Orak](https://arxiv.org/abs/2506.03610)：评测并支持训练跨 12 类视频游戏的 LLM agent。核心思想：用 MCP-based 接口、游戏轨迹、leaderboard、battle arena 和 agent module 消融研究可执行游戏 agent。
- [WorldPrediction](https://arxiv.org/abs/2506.04363)：评测高层 world modeling 与长程程序化规划。核心思想：检验 agent 能否预测抽象未来状态并跨较长 horizon 组织流程，补充更偏生成动态一致性的视频 world-model benchmark。
- [RoboAfford](https://doi.org/10.1145/3746027.3758209)：评测机器人操作中的物体与空间 affordance learning。核心思想：把可行动 affordance 作为目标，检验具身模型能否从视觉空间语境中推断物体如何被使用和操作。
- [RoboAfford++](https://arxiv.org/abs/2511.12436)：评测机器人操作与导航中的多模态 affordance learning。核心思想：用生成式 AI 增强数据扩展 affordance 监督，使 agent 能连接物体、空间语境、可行动作以及导航/操作决策。
- [Target-Bench](https://arxiv.org/abs/2511.17792)：评估视频世界模型能否支持面向语义目标的无地图路径规划。核心思路是让模型在没有显式地图的情况下推理朝目标移动所需的前瞻信息。
- [DrivingGen](https://arxiv.org/abs/2601.01528)：评测自动驾驶场景中的生成式视频 world model。核心思想：用驾驶场景动态与可控性要求检验生成未来是否能服务具身规划，而不只是视觉上逼真。
- [Wow, wo, val!](https://arxiv.org/abs/2601.04137)：用图灵测试式协议评测具身世界模型。核心思想：把生成动态与交互世界行为对比，判断感知保真度与动作一致性。
- [AutoDriDM](https://arxiv.org/abs/2601.14702)：面向自动驾驶中 VLM 决策的可解释 benchmark。核心思想：评估视觉语言模型是否能产生有 grounding 且可解释的驾驶决策，而不只是输出感知标签。
- [VisGym](https://arxiv.org/abs/2601.16973)：在 17 个多步视觉交互环境中评测多模态 agent。核心思想：通过可调难度、时程、反馈与观测形式，测试谜题、真实图像任务、导航和操作中的感知、记忆、规划与行动。
- [WorldBench](https://arxiv.org/abs/2601.21282)：诊断世界模型中的物理保真度。核心思想：拆分物理因素，定位与具身规划相关的动力学、因果和物体交互失败。
- [EmboCoach-Bench](https://arxiv.org/abs/2601.21570)：评测 AI agent 开发具身机器人的能力。核心思想：把机器人开发工作流转化为带明确协议和评分方式的可比较任务。
- [P2Maze](https://doi.org/10.1109/SoutheastCon63549.2026.11476499)：在配对仿真与真实协议下评测机器人迷宫导航。核心思想：用匹配的迷宫任务衡量具身导航策略的零样本迁移和少样本适应。
- [SCOPE](https://doi.org/10.1145/3757279.3785641)：用 sim-to-real benchmark 评测自然语言 PTZ 摄像机 agent。核心思想：测试视觉语言 agent 能否在边缘运行约束下把语言目标映射为 pan-tilt-zoom 动作。
- [Out of Sight, Out of Mind?](https://arxiv.org/abs/2603.13215)：评估视频世界模型中的状态演化。核心思路是诊断模型能否在时间推进中维持被遮挡或暂时不可见的状态，这是具身规划的重要要求。
- [Beyond Binary Success](https://arxiv.org/abs/2603.13616)：评什么：硬件 rollout 受限条件下样本高效、统计严谨的机器人策略比较。核心思想：用覆盖二元、部分得分和连续机器人指标的 sequential anytime-valid 检验，替代脆弱的二元成功率平均。
- [PokeAgent Challenge](https://arxiv.org/abs/2603.15563)：在 Pokemon 对战和 RPG 速通环境中评测具身决策。核心思想：在可执行游戏环境里结合部分可观测、竞争式多 agent 推理、长程规划和标准化 baseline。
- [Omni-WorldBench](https://arxiv.org/abs/2603.22212)：评测以交互为中心的 4D world model。核心思想：结合交互提示套件和 agent-based 指标，衡量动作如何因果影响最终结果和中间状态轨迹。
- [Spatial-Gym](https://arxiv.org/abs/2604.09338)：评测 agent 能否把空间推理转成连续动作。核心思想：用 Gymnasium 风格交互 benchmark 覆盖 pathfinding、backtracking 与 action-level scoring，而不是只做被动空间问答。
- [RoboWM-Bench](https://arxiv.org/abs/2604.19092)：评估机器人操作场景中的世界模型。核心思路是检查预测动力学和状态变化是否真正有助于操作规划，而不只是生成视觉上合理的视频延续。
- [WorldMark](https://arxiv.org/abs/2604.21686)：在标准化控制条件下评测交互式 image-to-video world model。核心思想：把统一的 WASD 式动作词表映射到不同模型的原生接口，再在相同场景与轨迹上比较视觉质量、控制对齐和世界一致性。
- [Minedojo-Verified](https://github.com/ByteDance-Seed/Seed2.0)：Seed2.0 model card 报告的 embodied-agent 视觉任务 verified 子集；目前未确认有独立公开版本。核心思想：跟踪前沿多模态 agent 是否能在交互环境中完成感知 grounding、规划和动作执行，而不只是在静态截图上答题。
- [iWorld-Bench](https://arxiv.org/abs/2605.03941)：用统一的动作生成框架评估交互式世界模型。核心思路是检验世界模型能否支持动作条件下的交互，而不只是被动视频预测。

## 2.11.3 Agent Harness

- MineDojo、CALVIN、VIMA 和 LIBERO 本身也是 benchmark-side harness：它们定义环境、观测、动作空间、任务重置和成功检查。可复用设计模式是 `观察多模态状态 -> 解析语言目标 -> 计划/子目标 -> 行动 -> 验证环境状态 -> 恢复`。
- [PORTAL](https://arxiv.org/abs/2503.13356)：为大量 3D 游戏中的 agent 提供语言引导的 policy-generation harness。核心思想：生成行为树 policy，并用游戏指标和视觉语言反馈迭代改进，使可执行游戏环境中的执行循环可复用。
- [Cogito, Ergo Ludo](https://arxiv.org/abs/2509.25052)：面向游戏学习的推理与规划 agent。核心思想：用显式推理、规划和反馈包裹游戏交互，使 agent 在可执行环境中获得策略，而不只是回答静态游戏问题。
- [Current Agents Fail to Leverage World Model as Tool for Foresight](https://arxiv.org/abs/2601.03905)：评测 agent 将世界模型作为前瞻工具的能力。核心思想：显式呈现围绕世界模型的规划循环，测试 agent 能否在行动前模拟未来结果。
- [VLAgents](https://arxiv.org/abs/2601.11250)：为高效 VLA 推理提供 policy-server runtime。核心思想：通过服务层暴露 VLA policy，使具身 agent 执行循环和环境 harness 可以复用。
- [From Knowing to Doing Precisely](https://arxiv.org/abs/2602.01811)：为 VLA 模型提供自纠错和终止框架。核心思想：在动作执行外包裹纠错与停止检查，避免长程操作在错误累积后继续执行。
- [SAGE: Scalable Agentic 3D Scene Generation](https://arxiv.org/abs/2602.10116)：为具身 agent 评测提供可扩展 3D 场景生成。核心思想：合成带行动约束的场景，使机器人或模拟 agent 能在多样可行动环境中测试，而不是依赖少量固定地图。
- [HELM: Harness-Enhanced Long-horizon Memory](https://arxiv.org/abs/2604.18791)：面向长程 VLA 操作的模型无关 harness。核心思想：在 VLA policy 外加入外部记忆、验证和恢复，使长任务中的执行失败可以被诊断并纠正。
- [Continual Harness](https://arxiv.org/abs/2605.09998)：为长程具身任务中的自改进 foundation agent 提供在线适应 harness。核心思想：把适应循环放在基座模型外部，使任务反馈能在长时交互中更新行为。
- [Think Twice, Act Once](https://arxiv.org/abs/2605.12620)：为具身 agent 提供 verifier-guided action-selection wrapper。核心思想：在测试时采样候选动作，并用训练过的 verifier 选择更可靠的动作，而不改动基础 policy。

## 2.11.4 Skill

- [computer-vision-opencv](https://skills.sh/mindrally/skills/computer-vision-opencv) 适合模拟具身环境中的感知侧预处理与视觉诊断。
- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) 适合需要隔离运行时的具身或游戏环境搭建。
