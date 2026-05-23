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
- [VLABench](https://arxiv.org/abs/2412.18194)：评测带长程推理任务的语言条件机器人操作。核心思想：提供多类操作任务和组合式指令，使 VLA 模型同时接受任务推理、grounding 与动作序列执行检验。
- [ECBench](https://arxiv.org/abs/2501.05031)（[开源代码](https://github.com/Rh-Dang/ECBench)）：评测多模态基础模型的第一视角具身认知。核心思想：从 agent-centered 视角测试自我认知、动态场景感知与幻觉，比静态图像问答更接近具身操作。
- [Text2World](https://arxiv.org/abs/2502.13092)：评测 LLM 生成符号世界模型的能力。核心思想：把自然语言环境描述转换为可执行的符号模型，从而检验模型是否能表示规划所需的状态、动作和动态规则。
- [Openfly](https://arxiv.org/abs/2502.18041)：评测空中视角的视觉语言导航 agent。核心思想：提供综合性的空中导航平台，使模型必须把视觉观察、语言目标、空间推理和飞行动作连接起来，而不是只回答静态导航问题。
- [EXPRESS-Bench](https://arxiv.org/abs/2503.11117)：评测探索感知的具身问答能力。核心思想：把 3D 探索轨迹与问答任务、探索感知指标结合起来，使 agent 同时接受证据收集和后续推理评估。
- [HA-VLN](https://arxiv.org/abs/2503.14229)：评什么：含动态多人互动的离散-连续环境中的 human-aware vision-language navigation。核心思想：结合真实验证和开放 leaderboard，让导航 agent 不只按路线完成度评分，也要看社会感知能力。
- [OvercookedV2](https://arxiv.org/abs/2503.17821)：在 Overcooked 风格的具身多智能体环境中评测 zero-shot coordination。核心思想：压力测试 agent 是否能推断队友行为、分工协作，并在可执行协作任务中从配合失败中恢复。
- [SHREC](https://arxiv.org/abs/2504.13898)：评测真实人机具身对话中的社会推理能力。核心思路是使用真实交互视频、社会错误标注、理由和纠正任务，使具身智能体不只按导航或操作成功率评测，也能暴露细微的对话与社会行为失效。
- [Robotouille](https://openreview.net/forum?id=OhUoTMxFIH)：评测具身任务设置中 LLM agent 的异步规划能力。核心思想：要求 agent 在延迟或异步执行条件下规划与协调，而不是假设单一即时动作循环。
- [ManiSkill-HAB](https://openreview.net/forum?id=6bKEWevgSd)：评测家居重排任务中的低层操作能力。核心思想：把家居重排目标连接到操作原语，测试具身 agent 是否能完成接地的物体处理，而不是只做高层导航。
- [HASARD](https://openreview.net/forum?id=5BRFddsAai)：评测具身 agent 的视觉安全强化学习。核心思想：把安全约束显式放进具身环境，使模型在完成任务的同时避开危险。
- [TPT-Bench](https://arxiv.org/abs/2505.07446)：评测机器人第一视角下的目标人物跟踪；核心思想是用长时段、拥挤且非结构化的场景测试具身 agent 能否在遮挡、干扰人物和视角变化下持续跟踪指定目标。
- [UAV-Flow Colosseo](https://arxiv.org/abs/2505.15725)：评测真实飞行场景中的语言条件 UAV 模仿学习。核心思路是把自然语言指令和空中轨迹对齐，使具身空中智能体接受落地飞行动作评测，而不只是被动理解场景。
- [TrackVLA / EVT-Bench](https://arxiv.org/abs/2505.23189)（[项目页](https://pku-epic.github.io/TrackVLA-web)）：评估合成与真实环境中的具身视觉跟踪。核心思路是要求自中心智能体在遮挡和高动态场景中同时识别目标并规划轨迹，把视觉跟踪从被动感知推进到具身 VLA 能力评测。
- [CheckManual](https://openaccess.thecvf.com/content/CVPR2025/html/Long_CheckManual_A_New_Challenge_and_Benchmark_for_Manual-based_Appliance_Manipulation_CVPR_2025_paper.html)：评测基于说明书的电器操作。核心思想：把文档/说明书理解绑定到物理动作规划，要求 agent 提取程序性知识并用于操作。
- [RoboTwin](https://openaccess.thecvf.com/content/CVPR2025/html/Mu_RoboTwin_Dual-Arm_Robot_Benchmark_with_Generative_Digital_Twins_CVPR_2025_paper.html)：评测带生成式数字孪生的双臂机器人操作。核心思想：用生成的交互式仿真场景和专家示范，在更多样的物体与布局条件下测试协同操作。
- [Orak](https://arxiv.org/abs/2506.03610)：评测并支持训练跨 12 类视频游戏的 LLM agent。核心思想：用 MCP-based 接口、游戏轨迹、leaderboard、battle arena 和 agent module 消融研究可执行游戏 agent。
- [WorldPrediction](https://arxiv.org/abs/2506.04363)：评测高层 world modeling 与长程程序化规划。核心思想：检验 agent 能否预测抽象未来状态并跨较长 horizon 组织流程，补充更偏生成动态一致性的视频 world-model benchmark。
- [HEAL](https://arxiv.org/abs/2506.15065)：评估 LLM 驱动具身智能体在场景与任务不一致时的幻觉。核心思路是构造与观察环境冲突的目标或条件，检验智能体在行动前是否真正完成环境 grounding。
- [EmbodiedBench](https://proceedings.mlr.press/v267/yang25f.html)（[开源代码](https://github.com/EmbodiedBench/EmbodiedBench)）：评测多模态大语言模型作为视觉驱动具身 agent 的能力。核心思想：把具身感知、规划和动作任务放进统一 benchmark，考察基于视觉观测操作的 VLM/LLM agent。
- [VLN-PE](https://arxiv.org/abs/2507.13019)：在更接近真实物理约束的机器人形态中评估视觉语言导航。核心思路是比较人形、四足和轮式机器人上的导航流程，使具身导航不再只依赖理想化运动假设。
- [UAV-ON](https://arxiv.org/abs/2508.00288)：评测空中 agent 的开放世界目标物体导航。核心思想：测试 UAV agent 能否结合视觉感知和空间探索在开放环境中找到目标物体，将具身导航从地面场景扩展到空中视角。
- [Follow-Bench](https://arxiv.org/abs/2509.10796)：评测具备社会感知的机器人跟随行人运动规划。核心思想：测试 embodied agent 能否在跟随目标的同时遵守社会导航约束，而不是只优化几何路径效率。
- [ConEQsA](https://arxiv.org/abs/2509.11663)：评测并发、异步的具身问题调度与回答。核心思想：把 EQA 从单问题扩展到不同到达时间和紧急度的多问题设置，要求 agent 结合共享记忆、优先级、探索与回答时机。
- [MoMa-Kitchen](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html)：评测移动操作中的 affordance-grounded 最后一段导航。核心思想：不仅看机器人是否接近目标，还看停止位置是否让后续操作可行。
- [VideoGameBench](https://vgbench.com/#leaderboard)：评测视频游戏环境中的具身感知、导航、操作与规划。核心思想：把空间理解放进可行动的游戏世界中，用任务完成与轨迹质量评估 agent 是否能把视觉空间关系转成动作。
- [SAGE-Bench](https://arxiv.org/abs/2510.21307)：在语义化且物理可执行的 3D Gaussian 环境中评测视觉语言导航。核心思想是为 3DGS 场景加入对象语义和碰撞感知执行接口，使导航智能体在逼真且可行动的空间中接受测试。
- [CityEQA](https://aclanthology.org/2025.emnlp-main.630/)：评测城市尺度空间中的 embodied question answering。核心思想：把语言 agent 放入层级城市环境，回答问题需要导航、空间推理和证据收集，而不是静态场景识别。
- [UAVBench](https://arxiv.org/abs/2511.11252)：用 LLM 生成的飞行场景评测自主和智能体式 UAV 系统。核心思路是通过场景生成扩展空中智能体任务，在多样飞行目标下测试感知、规划和控制。
- [RoboAfford](https://doi.org/10.1145/3746027.3758209)：评测机器人操作中的物体与空间 affordance learning。核心思想：把可行动 affordance 作为目标，检验具身模型能否从视觉空间语境中推断物体如何被使用和操作。
- [RoboAfford++](https://arxiv.org/abs/2511.12436)：评测机器人操作与导航中的多模态 affordance learning。核心思想：用生成式 AI 增强数据扩展 affordance 监督，使 agent 能连接物体、空间语境、可行动作以及导航/操作决策。
- [Embodied4C](https://arxiv.org/abs/2512.18028)：评测具身视觉语言导航中真正影响导航成功的关键能力。核心思路是在最终成功率之外，诊断导航代理在具身环境中的感知定位、上下文利用、常识判断和控制相关推理。
- [VLNVerse](https://arxiv.org/abs/2512.19021)：评测多样化具身仿真环境中的视觉语言导航；核心思想是结合真实感场景、具身导航任务与标准化评测，让 agent 在感知 grounding、空间推理和动作执行上接受测试，而不只是回答静态导航问题。
- [α3-Bench](https://arxiv.org/abs/2601.03281)：评估 6G 网络环境中的 LLM-based UAV agents。核心思想：联合衡量安全性、鲁棒性与效率，使空中智能体评价覆盖通信约束和运行可靠性，而不只看导航成功率。
- [AirNav](https://arxiv.org/abs/2601.03707)：用包含自然多样指令的大规模数据集评估 UAV vision-language navigation。核心思想：测试空中智能体能否把语言目标落到视觉观测中，并在真实指令变化下完成导航。
- [P2Maze](https://doi.org/10.1109/SoutheastCon63549.2026.11476499)：在配对仿真与真实协议下评测机器人迷宫导航。核心思想：用匹配的迷宫任务衡量具身导航策略的零样本迁移和少样本适应。
- [Autonomous UAV Visual Object Search in City Space](https://doi.org/10.1609/aaai.v40i22.38898)：评测城市尺度环境中的 UAV 视觉目标搜索。核心思路是把基准和智能体式搜索方法结合起来，衡量空中智能体的开放视觉找目标、探索和导航决策能力。
- [LMEE-Bench](https://arxiv.org/abs/2601.10744)：评测具身探索中的长期情景记忆。核心思想：结合多目标导航和基于记忆的问答，使 agent 同时在探索过程和后续经验利用上被评分。
- [VisGym](https://arxiv.org/abs/2601.16973)：在 17 个多步视觉交互环境中评测多模态 agent。核心思想：通过可调难度、时程、反馈与观测形式，测试谜题、真实图像任务、导航和操作中的感知、记忆、规划与行动。
- [EmboCoach-Bench](https://arxiv.org/abs/2601.21570)：评测 AI agent 开发具身机器人的能力。核心思想：把机器人开发工作流转化为带明确协议和评分方式的可比较任务。
- [Beyond Binary Success](https://arxiv.org/abs/2603.13616)：评什么：硬件 rollout 受限条件下样本高效、统计严谨的机器人策略比较。核心思想：用覆盖二元、部分得分和连续机器人指标的 sequential anytime-valid 检验，替代脆弱的二元成功率平均。
- [PokeAgent Challenge](https://arxiv.org/abs/2603.15563)：在 Pokemon 对战和 RPG 速通环境中评测具身决策。核心思想：在可执行游戏环境里结合部分可观测、竞争式多 agent 推理、长程规划和标准化 baseline。
- [HUGE-Bench](https://arxiv.org/abs/2603.19822)：评测高层 UAV vision-language-action 任务。核心思想：用简短操作指令、digital-twin 场景、过程型轨迹和安全感知评分，测试空中 agent 是否能执行复杂多阶段行为，而不只是跟随路线描述。
- [IndoorR2X](https://arxiv.org/abs/2603.20182)：评测结合 Robot-to-Everything 感知的 LLM 驱动室内多机器人规划。核心思想：把移动机器人观察与静态 IoT 传感器结合起来，测试 agent 能否在部分可观测和共享语义状态下协同。
- [CaP-X](https://arxiv.org/abs/2603.22435)：评测并改进面向机器人操作的编码智能体。核心思路是把代码生成、具身操作任务和执行反馈连接起来，使机器人控制智能体的比较不止停留在静态程序合成。
- [Urban Airspace Spatial Action Benchmark](https://arxiv.org/abs/2604.07973)：评测城市空域中的目标导向具身导航；核心思想是测试大型多模态模型能否把空间感知和语言目标转化为空中导航动作，而不只是回答被动空间问题。
- [SCOPE](https://doi.org/10.1145/3757279.3785641)：用 sim-to-real benchmark 评测自然语言 PTZ 摄像机 agent。核心思想：测试视觉语言 agent 能否在边缘运行约束下把语言目标映射为 pan-tilt-zoom 动作。
- [Spatial-Gym](https://arxiv.org/abs/2604.09338)：评测 agent 能否把空间推理转成连续动作。核心思想：用 Gymnasium 风格交互 benchmark 覆盖 pathfinding、backtracking 与 action-level scoring，而不是只做被动空间问答。
- [E3VS-Bench](https://arxiv.org/abs/2604.17969)：评测 3D Gaussian Splatting 场景中的视角依赖主动感知。核心思想：让具身 agent 通过 5-DoF 视角移动发现遮挡、容器内部或属性依赖证据，而不是只基于静态观察回答。
- [Capability-Oriented Failure Attribution for VLN Agents](https://arxiv.org/abs/2604.25161)：评测视觉语言导航 agent 在不同能力环节的失败来源。核心思想：结合自适应测试用例生成、能力专属 oracle 和反馈式归因，把导航失败定位到感知、记忆、规划或决策弱点，而不只看最终成功率。
- [Minedojo-Verified](https://github.com/ByteDance-Seed/Seed2.0)：Seed2.0 model card 报告的 embodied-agent 视觉任务 verified 子集；目前未确认有独立公开版本。核心思想：跟踪前沿多模态 agent 是否能在交互环境中完成感知 grounding、规划和动作执行，而不只是在静态截图上答题。
- [ESARBench](https://arxiv.org/abs/2605.01371)：评估无人机具身智能体的搜索与救援能力。核心思路是把空中智能体放入搜救场景中，同时考察感知、导航、任务规划和动作执行，而不是只评价静态视觉理解。
- [OmniNavBench](https://arxiv.org/abs/2605.09441)：评测跨技能、跨具身形态的通用具身导航。核心思想：用覆盖 PointNav、VLN、ObjectNav、SocialNav、跟随人类和 EQA 的复合指令，要求 agent 协调子技能并跨机器人形态泛化，而不是只解决孤立导航任务。
## 2.11.3 Agent Harness

MineDojo、CALVIN、VIMA 和 LIBERO 本身也是 benchmark-side harness：它们定义环境、观测、动作空间、任务重置和成功检查。可复用设计模式是 `观察多模态状态 -> 解析语言目标 -> 计划/子目标 -> 行动 -> 验证环境状态 -> 恢复`。
- [Voyager](https://arxiv.org/abs/2305.16291)（[开源代码](https://github.com/MineDojo/Voyager)；[项目页](https://voyager.minedojo.org/)）：经典开放式 Minecraft agent，包含自动课程、code-as-action、执行反馈和持续增长的技能库，直接对应 MineDojo 风格长程具身 agent 评测。
- [JARVIS-1](https://arxiv.org/abs/2311.05997)（[开源代码](https://github.com/CraftJarvis/JARVIS-1)；[项目页](https://craftjarvis.github.io/JARVIS-1/)）：开放世界 Minecraft 多任务 agent，包含多模态记忆和动作 grounding，可作为 Voyager 之外的历史性游戏 agent harness。
- [MineStudio](https://arxiv.org/abs/2403.12067)（[开源代码](https://github.com/CraftJarvis/MineStudio)）：开源 Minecraft agent 开发包，覆盖数据、训练、评测和轨迹工具，连接 MineDojo 与更新的游戏 agent benchmark。
- [UAV-VLA](https://arxiv.org/abs/2501.05014)：面向大规模空中任务生成的视觉-语言-动作系统。核心思路是把任务级语言和视觉上下文转化为 UAV 行动方案，使空中任务分解和执行成为智能体运行时的一部分。
- [Generalized Mission Planning for Heterogeneous Multi-Robot Teams](https://arxiv.org/abs/2501.16539)：面向异构多机器人任务规划的 LLM harness。核心思想：从语言目标构造层级任务树，让不同能力的机器人获得协同子任务并执行团队任务。
- [VL-Nav](https://arxiv.org/abs/2502.00931)：一种神经符号视觉语言导航 harness。核心思想是结合 VLM 推理、符号化 3D 场景图、图像记忆、任务分解、探索启发式和重规划，使机器人能在未知室内外环境中执行复杂指令。
- [MuJoCo Playground](https://arxiv.org/abs/2502.08844)：基于 MuJoCo 的可复用机器人学习环境套件。核心思想：打包仿真、任务和评测脚手架，使 embodied policies 能在标准化控制设置下开发与比较。
- [MapNav](https://arxiv.org/abs/2502.13451)：为基于 VLM 的视觉语言导航提供语义地图记忆表示。核心思想：把导航记忆标注在地图上，使具身 agent 能依据持久空间上下文选择路线。
- [Mem2Ego](https://arxiv.org/abs/2502.14254)：面向长程具身导航的全局到自中心记忆 harness。核心思路是维护以环境为中心的场景记忆，并把它转换回自中心行动上下文，使 VLM 导航智能体能够在长时间探索中利用历史观察。
- [ATLAS Navigator](https://arxiv.org/abs/2502.20386)：基于 language-embedded Gaussian Splatting 的主动导航 harness。核心思想：把 3D 场景表示、语言目标和任务驱动探索连接起来，使 embodied agent 能依托更丰富的空间记忆导航，而不只依赖当前第一视角观察。
- [General-Purpose Aerial Intelligent Agents](https://arxiv.org/abs/2503.08302)：面向开放世界空中任务执行的 LLM 驱动无人机智能体框架。核心思路是结合机载语言推理、机器人自主能力和软硬件协同，使空中智能体能够理解高层目标并在物理世界执行。
- [SmartWay](https://arxiv.org/abs/2503.10069)：结合增强路点预测和回溯机制的零样本视觉语言导航框架。核心思路是整合空间路点生成、多模态推理、历史信息和恢复行为，使智能体能适应连续三维导航环境。
- [PORTAL](https://arxiv.org/abs/2503.13356)：为大量 3D 游戏中的 agent 提供语言引导的 policy-generation harness。核心思想：生成行为树 policy，并用游戏指标和视觉语言反馈迭代改进，使可执行游戏环境中的执行循环可复用。
- [AirVista-II](https://arxiv.org/abs/2504.09583)：面向具身无人机动态场景语义理解的智能体系统。核心思路：把空中感知与推理组织为具身智能体流程，而不是被动图像或视频理解任务。
- [ApexNav](https://arxiv.org/abs/2504.14478)：结合自适应探索与目标中心语义融合的零样本目标导航 harness。核心思路是在语义线索和几何探索线索之间切换，并长期记忆目标及相似物体，以提升噪声检测下的导航可靠性。
- [RoboVerse](https://arxiv.org/abs/2504.18904)（[开源代码](https://github.com/RoboVerseOrg/RoboVerse)；[项目页](https://roboverseorg.github.io)）：开放机器人学习平台，包含任务、机器人、场景、MetaSim 资产，以及与 LIBERO、ManiSkill、RLBench、robosuite 和 SimplerEnv 的集成，可作为 robot/VLA 评测基础设施。
- [UAV-CodeAgents](https://arxiv.org/abs/2505.07236)：基于语言和卫星图像进行无人机任务规划的 multi-agent ReAct harness。核心思想：结合视觉接地点选、多 agent 轨迹生成和反应式目标修订，使空中 agent 能把高层指令转成可执行任务。
- [Air-Ground Collaboration for Language-Specified Missions](https://arxiv.org/abs/2505.09108)：面向未知环境语言任务的空地协作具身 harness。核心思想：协调空中与地面 agent，把自然语言目标分解、探索并执行到互补 embodiment 上。
- [FlightGPT](https://arxiv.org/abs/2505.12835)：基于视觉语言模型的 UAV 视觉语言导航框架。核心思路是连接视觉观测、语言目标和显式路线推理，使空中导航决策更具泛化性和可解释性。
- [VLM-RRT](https://arxiv.org/abs/2505.23267)：用视觉语言模型引导 RRT 搜索的无人机导航框架。核心思路：结合语言目标、视觉 grounding 与采样式规划，使空中智能体能把观测和目标转化为导航轨迹。
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](https://arxiv.org/abs/2506.07454)：一个具身多机器人规划 harness。核心思想：用语言 grounding 与 3D scene graph 状态协调多机器人分层任务规划和执行。
- [GRaD-Nav++](https://arxiv.org/abs/2506.14009)：面向视觉无人机导航的机载视觉语言动作框架。核心思路是结合语言指令 grounding、高斯辐射场仿真、可微动力学和实时机载执行，使空中智能体能在非结构化环境中跟随高层指令。
- [DyNaVLM](https://arxiv.org/abs/2506.15096)：带动态视角和自修正图记忆的 zero-shot vision-language navigation harness。核心思想：在探索过程中维护并修正导航图，使路线决策能利用累积空间证据，而不是只依赖单步观察。
- [RALLY](https://arxiv.org/abs/2507.01378)：一个面向 agentic UAV swarm 的 LLM 驱动 harness。核心思想：用角色自适应协调支持耦合导航，使多个空中智能体分担规划和执行职责。
- [SkyVLN](https://arxiv.org/abs/2507.06564)：面向城市环境的 UAV 视觉语言导航与 NMPC 控制框架。核心思路是把语言目标 grounding 与模型预测飞行控制结合起来，使空中智能体能在受约束城市场景中执行路线决策。
- [Enter the Mind Palace](https://arxiv.org/abs/2507.12846)：面向长时程 active embodied question answering 的推理与规划 harness。核心思想：把长期空间记忆和证据记忆外显化，使 embodied agent 能持续导航、收集观察并回答问题。
- [DISCOVERSE](https://arxiv.org/abs/2507.21981)：面向复杂高保真环境的机器人仿真基础设施；核心思想是提供高效模拟世界与接口，使 embodied agent 能在小规模固定场景之外开发和评测。
- [Mixture of Skill-Based Vision-and-Language Navigation Agents](https://arxiv.org/abs/2508.07642)：围绕分解技能构建的具身导航智能体 harness。核心思路：把 VLN 行为拆成类似技能的组件并组合用于导航决策，使技能组织成为 embodied-agent 运行时的一部分。
- [SpatialGPT](https://doi.org/10.1145/3748636.3762753)：一种以空间链式思考和结构化空间记忆为核心的零样本视觉语言导航框架。核心思路是外化空间状态，使路线决策建立在持续场景结构上，而不是只依赖单步视觉语言匹配。
- [DEXTER-LLM](https://arxiv.org/abs/2508.14387)：面向未知环境多机器人协同的动态可解释 LLM harness。核心思想：让机器人团队的任务分配与协同过程显式化，以支持重规划和人工检查。
- [Agentic UAVs](https://arxiv.org/abs/2509.13352)：一种集成工具调用的 LLM 驱动 UAV 自主性 harness。核心思想是组织感知、推理、行动、集成和学习层，使空中智能体能查询数据库、调用外部系统，并在模拟搜救场景中形成任务决策。
- [VLN-Zero](https://arxiv.org/abs/2509.18592)：一个用于零样本迁移的具身导航 harness。核心思想：结合快速探索、缓存经验和神经符号视觉语言规划，使机器人导航不依赖特定任务训练也能适应。
- [JanusVLN](https://arxiv.org/abs/2509.22548)：带有双隐式记忆的具身导航框架。核心思想：分离语义记忆与空间记忆，使视觉语言 agent 在连续导航决策中保持路径相关上下文。
- [See, Point, Fly](https://arxiv.org/abs/2509.22653)：面向无人机导航的免训练 VLM 框架；核心思路是把开放词汇目标转化为视觉指向与飞行动作步骤，使无人机智能体无需针对特定任务训练也能执行导航。
- [Advancing Audio-Visual Navigation Through Multi-Agent Collaboration in 3D Environments](https://arxiv.org/abs/2509.22698)：面向 3D 环境音视频导航的多智能体 harness；核心思想是把导航推理拆分给协作智能体，使视觉线索、声学线索与路径决策能在具身探索过程中协同起来。
- [Leave No Observation Behind](https://arxiv.org/abs/2509.23224)：面向 VLA action chunk 的实时纠错 harness。核心思想：利用持续到来的观察发现过期或失败的动作片段，并在线修正执行，使具身 agent 能在连续控制中恢复。
- [RAVEN](https://arxiv.org/abs/2509.23563)：使用开放集语义记忆和行为自适应的空中导航框架；核心思想是在变化或未见过的空中场景中维护环境记忆并调整导航行为，而不是把 VLN 只当作固定策略预测任务。
- [Prompting Robot Teams with Natural Language](https://arxiv.org/abs/2509.24575)：面向机器人团队的自然语言编排框架；核心思想是把人类语言指令转化为多机器人协同行为，将团队分工与具身执行纳入 agent 运行时。
- [Cogito, Ergo Ludo](https://arxiv.org/abs/2509.25052)：面向游戏学习的推理与规划 agent。核心思想：用显式推理、规划和反馈包裹游戏交互，使 agent 在可执行环境中获得策略，而不只是回答静态游戏问题。
- [GaussGym](https://arxiv.org/abs/2510.15352)：面向从像素学习 locomotion 的开源 real-to-sim 框架。核心思想：把 Gaussian-splatting 重建、仿真与策略评测连接起来，使视觉 grounding 的 locomotion agent 能在照片级 real-to-sim 环境中测试。
- [Next-Generation LLM for UAV](https://arxiv.org/abs/2510.21739)：基于 LLM 的 UAV 框架，用于把自然语言转化为自主飞行行为。核心思路是把语言理解、任务规划和飞行执行纳入同一个空中智能体闭环。
- [Running VLAs at Real-time Speed](https://arxiv.org/abs/2510.26742)（[代码](https://github.com/Dexmal/realtime-vla)）：面向实时 VLA 机器人控制的流式推理 harness。核心思路是削减多视角 VLA 策略周边的推理开销，使动作生成能够在消费级硬件上达到实时控制频率。
- [SPINE-HT](https://arxiv.org/abs/2510.26915)：面向非结构化环境中异构机器人协作的 grounded generative-intelligence harness。核心思想：把自然语言任务分解为可行子任务，按机器人能力分配，并利用在线感知反馈修正计划。
- [Isaac Lab](https://arxiv.org/abs/2511.04831)：面向机器人学习的 GPU 加速仿真框架。核心思想：提供可复用的多模态机器人环境、传感器和策略评测流程，使 embodied-agent harness 不必依赖一次性模拟器。
- [MindPower](https://arxiv.org/abs/2511.23055)：为基于 VLM 的具身智能体加入心智理论推理。核心思路是在具身决策循环中显式建模其他主体的信念与意图，使智能体能够在社交或协作不确定性下规划。
- [LEO-RobotAgent](https://arxiv.org/abs/2512.10605)：面向语言驱动具身操作的通用机器人智能体；核心思路是把语言目标、感知、规划和机器人动作组织成可复用的具身智能体执行闭环。
- [VLA-AN](https://arxiv.org/abs/2512.15258)：面向空中导航的机载视觉-语言-动作框架。核心思路是在复杂环境中以高效的无人机导航闭环组织感知、语言目标 grounding 与动作选择。
- [ImagineNav++](https://arxiv.org/abs/2512.17435)：一种具身导航 harness，引导视觉语言模型在动作选择前想象场景结构。核心思想：把生成的空间假设作为外部推理上下文，使导航 agent 不只依赖当前视野进行规划。
- [Genie Sim 3.0](https://arxiv.org/abs/2601.02078)：用于规模化数据采集和策略评测的高保真人形机器人仿真平台。核心思想：结合 LLM 辅助场景生成和统一操作环境，让具身 agent 能在多样、逼真的场景中接受测试。
- [Current Agents Fail to Leverage World Model as Tool for Foresight](https://arxiv.org/abs/2601.03905)：评测 agent 将世界模型作为前瞻工具的能力。核心思想：显式呈现围绕世界模型的规划循环，测试 agent 能否在行动前模拟未来结果。
- [SpatialNav](https://arxiv.org/abs/2601.06806)：一个基于空间场景图的零样本视觉语言导航框架。核心思路是先让智能体探索环境，构建全局空间与语义结构，再用以智能体为中心的地图支撑 grounded 导航决策。
- [VLingNav](https://arxiv.org/abs/2601.08665)：结合自适应推理与视觉辅助语言记忆的具身导航框架；核心思想是从视觉观察中维护语言化记忆，使连续导航决策能够利用持久路径上下文。
- [VLAgents](https://arxiv.org/abs/2601.11250)：为高效 VLA 推理提供 policy-server runtime。核心思想：通过服务层暴露 VLA policy，使具身 agent 执行循环和环境 harness 可以复用。
- [IROS](https://arxiv.org/abs/2601.21506)：面向实时 VLM 室内导航的双过程 harness。核心思想：把快速反应式控制与较慢的视觉语言推理分开，使室内 agent 能在持续行动时根据观察修订计划。
- [From Knowing to Doing Precisely](https://arxiv.org/abs/2602.01811)：为 VLA 模型提供自纠错和终止框架。核心思想：在动作执行外包裹纠错与停止检查，避免长程操作在错误累积后继续执行。
- [MerNav](https://arxiv.org/abs/2602.05467)：用于零样本目标物体导航的 Memory-Execute-Review 框架。核心思路：用记忆、执行与复查环节包装导航过程，使具身智能体在物体搜索中能够恢复并泛化。
- [Grounding Generative Planners in Verifiable Logic](https://arxiv.org/abs/2602.08373)：一种混合式具身 AI 规划 harness。核心思路：把生成式规划与可验证逻辑结合起来，使具身智能体能在行动前或行动中检查计划约束与可信性。
- [One Agent to Guide Them All](https://arxiv.org/abs/2602.15400)：围绕显式世界表征构建的视觉语言导航智能体。核心思路：把世界状态作为外部导航结构显式化，使 MLLM 的路线决策不只依赖一次性的视觉语言推断。
- [VLA-Perf](https://arxiv.org/abs/2602.18397)：面向实时 VLA 推理的性能分析框架。核心思想是建模 VLA 架构、长上下文视觉输入、硬件部署、边缘或云端执行与网络条件之间的时延权衡，使具身智能体运行时能围绕控制环约束设计。
- [RoboCritics](https://arxiv.org/abs/2603.06842)：用专家运动级评价器增强 LLM 机器人编程的框架。核心思路是检查执行轨迹中的碰撞、关节速度违规和不安全姿态，并把结构化修正反馈回编程循环。
- [OnFly](https://arxiv.org/abs/2603.10682)：面向机载无人机智能体的零样本空中视觉语言导航框架。核心思路是结合双智能体决策架构、混合轨迹记忆、语义-几何验证和滚动时域规划，稳定长程导航。
- [GoalVLM](https://arxiv.org/abs/2603.18210)：协作式多智能体 object-goal navigation harness。核心思想：把 VLM 语义评分、开放词表分割、空间推理与 frontier selection 放入决策闭环，使多个 agent 能围绕自由语言目标协同搜索。
- [ReMemNav](https://arxiv.org/abs/2603.26788)：面向零样本目标导航的记忆增强框架。核心思路是在具身导航中加入可复用记忆机制，使智能体在执行任务时能够恢复目标位置与探索上下文。
- [MetaNav](https://arxiv.org/abs/2604.02318)：一种具备元认知的视觉语言导航 harness。核心思想：结合持久 3D 语义记忆、历史感知规划和反思式修正，使免训练 VLN agent 能发现低效游走、调整探索策略并减少重复访问。
- [Speculative Verification for VLA](https://arxiv.org/abs/2604.02965)：一种结合开环动作块规划与轻量闭环验证的 VLA 控制 harness；核心思想是在保持高吞吐动作生成的同时在线检查观测，使具身智能体能在误差累积主导执行前发现过期或不安全的动作块。
- [StarVLA](https://arxiv.org/abs/2604.05014)（[开源代码](https://github.com/starVLA/starVLA)）：模块化 VLA 开发代码库，提供 benchmark-agnostic 的数据、模型、训练和评测组件，更适合作为 VLA agent 开放基础设施，而不是单个模型 checkpoint。
- [ABot-Claw](https://arxiv.org/abs/2604.10096)：面向持久、协作和自演化机器人的具身智能体运行框架。核心思路是在 OpenClaw 之上加入统一具身接口、跨具身多模态记忆、能力调度和基于 critic 的反馈，使自然语言目标能够闭环到物理机器人动作和重新规划。
- [FineCog-Nav](https://arxiv.org/abs/2604.16298)：一个面向无人机视觉语言导航的零样本智能体框架，采用细粒度认知模块。核心思路是用结构化协议协同语言、感知、注意力、记忆、想象、推理和决策模块，并通过 AerialVLN-Fine 诊断指令遵循和长程导航能力。
- [HELM: Harness-Enhanced Long-horizon Memory](https://arxiv.org/abs/2604.18791)：面向长程 VLA 操作的模型无关 harness。核心思想：在 VLA policy 外加入外部记忆、验证和恢复，使长任务中的执行失败可以被诊断并纠正。
- [Explore Like Humans](https://arxiv.org/abs/2604.19034)：一种带在线 SG-Memo 构建的具身智能体自主探索框架。核心思路是在探索过程中构建空间与语义记忆，使后续导航决策能够利用持续演化的环境模型。
- [AsyncShield](https://arxiv.org/abs/2604.24086)：面向异步云端 VLA 导航的即插即用边缘适配器。核心思想：通过延迟感知控制和安全过滤补偿网络抖动与过期视觉语言意图，使云端 VLA policy 更适合连续移动导航闭环。
- [GS-Playground](https://arxiv.org/abs/2604.25459)：面向视觉机器人学习的高吞吐照片级仿真基础设施。核心思想：结合 Gaussian Splatting 资产与多模态仿真接口，让具身策略能在视觉丰富环境中以更高吞吐训练和评测。
- [Embodied EvoAgent](https://doi.org/10.1145/3746027.3754880)：连接多模态大模型与世界模型的脑启发具身 agent 范式；核心思想是在感知、世界建模和动作之间构建 agent 框架，使具身系统围绕环境状态推理，而不是只依赖单个被动多模态模型。
- [Continual Harness](https://arxiv.org/abs/2605.09998)：为长程具身任务中的自改进 foundation agent 提供在线适应 harness。核心思想：把适应循环放在基座模型外部，使任务反馈能在长时交互中更新行为。
- [RIO](https://arxiv.org/abs/2605.11564)：面向跨 embodiment 机器人学习与部署的灵活 robot I/O 基础设施层。核心思想：标准化机器人控制、遥操作、传感器、数据格式与策略部署，使 embodied-agent runtime 能以更少的专用代码迁移到不同硬件。
- [Think Twice, Act Once](https://arxiv.org/abs/2605.12620)：为具身 agent 提供 verifier-guided action-selection wrapper。核心思想：在测试时采样候选动作，并用训练过的 verifier 选择更可靠的动作，而不改动基础 policy。
- vla-evaluation-harness（[开源代码](https://github.com/allenai/vla-evaluation-harness)；[leaderboard](https://allenai.github.io/vla-evaluation-harness/leaderboard/)）：统一 VLA 评测与部署 harness，连接 Dockerized benchmarks、model servers 和 evaluation jobs，覆盖 LIBERO、CALVIN、SimplerEnv、RoboCasa、VLABench、RoboTwin、RLBench、BEHAVIOR-1K、OpenVLA-style servers 等 policy stacks。

## 2.11.4 Skill

- [computer-vision-opencv](https://skills.sh/mindrally/skills/computer-vision-opencv) 适合模拟具身环境中的感知侧预处理与视觉诊断。
- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) 适合需要隔离运行时的具身或游戏环境搭建。
- [vla-evaluation-harness skills](https://github.com/allenai/vla-evaluation-harness/tree/main/.claude/skills) 提供新增 benchmark adapter、新增 model server 和运行 VLA 评测的可复用工作流，使 benchmark integration 本身成为 agent-readable skill surface。
- [AgenticROS](https://github.com/agenticros/agenticros) 把 ROS2、OpenClaw、MCP、Gazebo/RViz 和机器人控制 adapter 暴露成面向 agent 的运行时层，适合把具身 skills 接到机器人中间件，而不是停留在 learned policy primitives。
