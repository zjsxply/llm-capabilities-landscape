# 1.7 空间

> 上级章节：1. 基础能力


## 1.7.1 Leaderboard

- [EASI Leaderboard Data](https://huggingface.co/datasets/lmms-lab-si/EASI-Leaderboard-Data/tree/main)：持续榜单数据：整合 SPAR-Bench、MMSI-Bench、OmniSpatial、ViewSpatial、VSI-Bench 等空间推理数据；适合作为空间 VLM 的统一横向比较入口。
- [PhysBench Leaderboard](https://physbench.github.io/#leaderboard)：持续榜单：物理世界理解与空间/因果推理；适合筛选既能处理空间关系又能处理物体运动、稳定性和交互结果预测的模型。
- [Ego3D-Bench Leaderboard](https://vbdi.github.io/Ego3D-Bench-webpage/#leaderboard)：持续榜单：第一视角三维空间理解；适合跟踪 egocentric 场景中的深度、方向、视角转换和空间记忆能力。
- [VLM4D Leaderboard](https://vlm4d.github.io/#leaderboard)：持续榜单：四维时空理解；适合比较模型在动态三维场景、对象运动与跨时间空间关系上的表现。
- [SpatialTree Leaderboard](https://spatialtree.github.io/#leaderboard)：持续榜单：树结构空间推理；适合观察模型能否把复杂空间关系拆成可组合、可追溯的层级推理。
- [VideoGameBench Leaderboard](https://vgbench.com/#leaderboard)：持续榜单：视频游戏环境中的具身 agent 感知、导航、操作与规划；适合寻找带可执行环境和空间行动闭环的 agent harness。

## 1.7.2 Bench

- `CountBench`（见 [Teaching CLIP to Count to Ten](https://arxiv.org/abs/2302.12066)）：评什么：视觉计数与数量概念的可靠性；核心思想：计数常是空间与组合推理的基础诊断项，可作为空间推理评测的辅助刻画维度。
- [BLINK](https://arxiv.org/abs/2404.12390)（[开源代码](https://github.com/zeyofu/BLINK_Benchmark)）：评什么：多模态模型的核心视觉感知与空间相关能力（如相对深度、对应关系、多视角一致性等）；核心思想：把经典 CV 感知任务改写成多选式 VQA，强调“看得见但不一定感知到”的能力缺口。
- `DA-2K`（[Depth Anything V2](https://arxiv.org/abs/2406.09414)）：评什么：单图深度/相对深度等与三维几何强相关的视觉能力；核心思想：用相对深度与几何一致性作为空间理解的“底座型”观测信号（但其任务更偏传统视觉评测，而非对话式推理）。
- [SPACE](https://arxiv.org/abs/2410.06468)（[开源代码](https://github.com/apple/ml-space-benchmark)）：评什么：前沿模型的空间认知，覆盖导航式大尺度空间、物体形状/布局和空间注意/记忆；核心思想：把认知科学中的经典空间任务改写成文本与视觉双呈现协议，用来区分语言记忆、视觉空间表征和具身导航能力。
- [3DSRBench](https://arxiv.org/abs/2412.07825)（[项目页](https://3dsrbench.github.io/)）：评什么：三维空间推理的综合能力；核心思想：把距离、方向、遮挡、视角转换等 3D 推理需求组织成系统化题型，是 SPAR-Bench 引用链中的强基线。
- [VSI-Bench](https://arxiv.org/abs/2412.14171)（[开源代码](https://github.com/vision-x-nyu/thinking-in-space)）：评什么：真实空间中的视觉空间记忆与回忆；核心思想：用场景观察、记忆保持和空间问答检验 MLLM 是否能形成稳定的空间表征，而不只是识别单帧内容。
- [4DWorldBench](https://arxiv.org/abs/2511.19836)：评估 3D 与 4D 世界生成模型。核心思路是同时考察生成世界的空间结构与时间演化，把空间评测从静态场景扩展到动态世界生成结果。
- [PhysBench](https://physbench.github.io/#leaderboard)：评什么：物理世界理解与空间/因果推理。核心思想：把空间关系、物体运动、稳定性和交互结果预测放进同一榜单协议，用于筛选具备物理 grounding 的空间推理模型。
- [MapEval](https://arxiv.org/abs/2501.00316)（[开源代码](https://github.com/MapEval/MapEval-API)）：评什么：地图/地理空间推理与路线、周边、地点信息检索；核心思想：把 map tool、异构地理上下文与组合推理放进同一评测协议。
- [Hypo3D](https://arxiv.org/abs/2502.00954)：评什么：三维 hypothetical reasoning；核心思想：让模型对“如果物体/视角/状态变化会怎样”的反事实空间问题作答，补足静态关系识别之外的想象式 3D 推理。
- [SPAR-Bench](https://arxiv.org/abs/2503.22976)（[开源代码](https://github.com/fudan-zvg/SPAR)）：评什么：VLM 的三维空间感知与推理，覆盖单视角和多视角输入；核心思想：从带三维真值的场景生成多层级空间问答，兼顾深度、距离、关系与想象式空间推理。
- [Compositional-ARC](https://arxiv.org/abs/2504.01445)：评什么：抽象空间推理中的系统泛化。核心思想：测试模型能否把平移、旋转等已知几何变换组合到未见过的新情形，而不是记忆单个 ARC 风格模式。
- [All-Angles](https://arxiv.org/abs/2504.15280)（[开源代码](https://github.com/Chenyu-Wang567/All-Angles-Bench)）：评什么：多视角（含 egocentric/exocentric）理解与跨视角一致推理；核心思想：同一场景不同视角下的对齐与推理是空间智能的关键难点，基准用多视角 QA 显式暴露这一点。
- [PointArena（PointBench）](https://arxiv.org/abs/2505.09990)（[开源代码](https://github.com/pointarena/pointarena)）：评什么：pointing / 指向能力（让模型在图上点选/定位目标或区域）；核心思想：把空间 grounding 从文本描述提升到可操作的“指点”输出，使定位误差可度量。
- [ViewSpatial-Bench](https://arxiv.org/abs/2505.21500)（[开源代码](https://github.com/ZJU-REAL/ViewSpatial-Bench)）：评什么：多视角空间定位与视角转换；核心思想：同时考察 camera-centered 和 human-centered 空间框架，暴露模型从自我中心推理泛化到异我中心推理时的性能断层。
- [MMSI-Bench](https://arxiv.org/abs/2505.23764)（[开源代码](https://github.com/OpenRobotLab/MMSI-Bench)）：评什么：多图输入下的空间智能（multi-image spatial intelligence），要求模型在多张图之间建立空间一致理解；核心思想：用“多视角/多帧”输入显式测试跨图融合与空间关系推理，而不仅是单图问答。
- [OmniSpatial](https://arxiv.org/abs/2506.03135)：评什么：综合空间推理，覆盖 dynamic reasoning、complex spatial logic、spatial interaction 与 perspective-taking；核心思想：以认知心理学能力轴组织 50 个细粒度子类，避免只测 left/right、near/far 等低层关系。
- [ERQA](https://github.com/embodiedreasoning/ERQA)：评什么：具身/物理环境相关的推理问答（embodied reasoning QA），包含空间关系、行动与物理常识等；核心思想：把“空间理解”放入具身语境，用更接近机器人场景的问答形式测试模型的物理与空间推断。
- [RefSpatial-Bench](https://arxiv.org/abs/2506.04308)（[开源代码](https://github.com/Zhoues/RoboRefer)）：评什么：空间指代与空间关系理解（referring + spatial relations），常面向机器人/具身场景；核心思想：把空间 referring 任务定义为可复现的 runtime，并更强调对三维/相对位置语义的精确落地。
- [Ego3D-Bench](https://vbdi.github.io/Ego3D-Bench-webpage/#leaderboard)：评什么：第一视角三维空间理解。核心思想：用 egocentric 观察中的深度、方向、视角转换和空间记忆任务检验模型是否能从自我中心视觉流中形成稳定三维表征。
- [VLM4D](https://vlm4d.github.io/#leaderboard)：评什么：四维时空理解。核心思想：把动态三维场景、对象运动和跨时间空间关系纳入统一评测，补足静态图像空间关系 benchmark 对时间维度覆盖不足的问题。
- [EASI Leaderboard Data](https://huggingface.co/datasets/lmms-lab-si/EASI-Leaderboard-Data/tree/main)：评什么：空间 VLM 多基准聚合榜单数据。核心思想：把 SPAR-Bench、MMSI-Bench、OmniSpatial、ViewSpatial、VSI-Bench 等空间推理结果放进统一数据入口，便于跨 benchmark 比较模型空间智能。
- [MARBLE](https://arxiv.org/abs/2506.22992)：评什么：多模态空间推理与规划；核心思想：用 M-Portal 和 M-Cube 两类任务考察模型在视觉、物理和空间约束下进行多步计划构造与理解的能力。
- [IR3D-Bench](https://arxiv.org/abs/2506.23329)（[项目页](https://ir3d-bench.github.io/)；[开源代码](https://github.com/LiuHengyu321/IR3D-Bench)；[数据集](https://huggingface.co/datasets/Piang/IR3D-Bench)）：评什么：不完整三维重建中的 3D scene graph generation。核心思想：把真实 3D 重建缺失、噪声和关系推断放进同一协议，检验模型能否在不完美空间证据下恢复场景关系。
- [PAC Bench](https://arxiv.org/abs/2506.23725)（[项目页](https://pacbench.github.io/)；[数据集](https://huggingface.co/datasets/lens-lab/pacbench)）：评什么：基础模型是否理解机器人操作策略的前置条件。核心思想：围绕物体属性、可供性和物理约束判断某个 manipulation policy 是否可执行，补足空间/具身任务中“能看见但不知道能不能做”的能力缺口。
- [TreeBench](https://arxiv.org/abs/2507.07999)（[开源代码](https://github.com/Haochen-Wang409/TreeVGR)）：评什么：视觉 grounded 推理的“可追溯证据链”与空间/关系推理可靠性；核心思想：把“回答正确”进一步约束为“能指认证据”，更强绑定到可验证的视觉证据组织。
- [SpatialTree](https://spatialtree.github.io/#leaderboard)：评什么：树结构空间推理。核心思想：要求模型把复杂空间关系拆成层级化、可追溯的结构，观察空间推理是否能从局部关系组合到全局判断。
- [DSI-Bench](https://arxiv.org/abs/2510.18873)：评什么：动态三维空间智能；核心思想：用近千个动态视频和九类 observer/object motion pattern，区分自运动、物体运动与相对空间关系推理。
- [DecompSR](https://arxiv.org/abs/2511.02627)：评什么：分解式组合多跳空间推理。核心思想：程序化生成并校验任务，同时独立控制 productivity、substitutivity、overgeneralization 和 systematicity，用来诊断空间泛化失败点。
- [SpatialBench](https://arxiv.org/abs/2511.21471)：评什么：MLLM 的层级化空间认知能力；核心思想：把空间智能拆成从基础观察到高层规划的五级框架，并用 15 类任务和能力导向指标衡量模型是否只会表面感知而缺少符号、因果和规划能力。
- [VideoGameBench](https://vgbench.com/#leaderboard)：评什么：视频游戏环境中的具身感知、导航、操作与规划。核心思想：把空间理解放进可行动的游戏环境中，用任务完成和轨迹质量评估 agent 是否能把视觉空间关系转成连续动作。
- [CartoMapQA](https://arxiv.org/abs/2512.03558)（[开源代码](https://github.com/ungquanghuy-kddi/CartoMapQA)）：评什么：制图地图理解与地理空间问答；核心思想：用符号识别、嵌入信息抽取、比例尺解释和路线推理等任务，暴露 VLM 在地图语义、OCR 与 geospatial reasoning 上的短板。
- [MMSI-Video-Bench](https://arxiv.org/abs/2512.10863)（[开源代码](https://github.com/InternRobotics/MMSI-Video-Bench)）：评什么：视频输入下的空间智能；核心思想：用 1,106 个专家标注问题覆盖感知、规划、预测和跨视频推理，测试模型能否在连续视觉流中保持空间布局、运动和视角一致性。
- [Grid Spatial Understanding（GSU）](https://arxiv.org/abs/2603.17333)：评什么：网格、具身参照系和坐标结构上的纯文本空间推理。核心思想：通过导航、目标定位和结构组合任务把空间推理从视觉感知中隔离出来。
- [See, Remember, Explore / S3-Bench](https://arxiv.org/abs/2603.23864)：评什么：带主动探索的流式空间问答。核心思想：要求 agent 只能使用特定时间点之前已观察到的信息作答，并在证据不足时采取探索动作补充观察，把空间推理从事后视频 QA 推进到在线记忆与感知问题。

## 1.7.3 Agent Harness

- [VLM-Grounder](https://arxiv.org/abs/2410.13860)（[开源代码](https://github.com/InternRobotics/VLM-Grounder)）面向零样本三维视觉 grounding；核心思想是让 VLM agent 调用三维场景工具和几何验证，把开放词汇目标落到具体 3D 区域。
- [RoboRefer](https://arxiv.org/abs/2506.04308)（[开源代码](https://github.com/Zhoues/RoboRefer)）面向机器人空间指代任务，采用显式空间 grounding 与执行反馈闭环来提升复杂空间关系求解稳定性。
- [MapAgent](https://arxiv.org/abs/2509.05933)（[开源代码](https://github.com/Hasebul/MapAgent)）面向 geospatial reasoning 的分层多 agent harness；核心思想是把复杂地图问题拆成规划、地图工具调用、证据抽取和答案生成模块，降低相似 geospatial API 带来的工具选择混淆。
- [SpaceTools](https://arxiv.org/abs/2512.04069)（[开源代码](https://github.com/spacetools/SpaceTools)）：面向空间推理的工具增强 harness；核心思想是把 segmentation、pointing、depth、3D box、grasp 等视觉/机器人工具纳入交互式执行链，并用工具反馈提升复杂空间任务的可验证性。
- [VULCAN](https://arxiv.org/abs/2512.22351)（开源代码：暂未见稳定公开官方仓库）：面向三维物体摆放的工具增强多 agent 框架；核心思想是通过 MCP 风格 API、三维场景工具、Planner/Executor/Evaluator 协作和反馈循环，把语言指令转成可验证的 3D 操作。
- [Think3D](https://arxiv.org/abs/2601.13029)（[开源代码](https://github.com/zhangzaibin/spagent)）面向三维空间推理的主动探索 harness；核心思想是让 VLM agent 调用 3D 操作工具形成交互式 spatial chain-of-thought，并用工具反馈改善多视角与视频空间推理。
- [Spatial-Agent](https://arxiv.org/abs/2601.16965)（开源代码：暂未见稳定公开官方仓库）面向地理空间问答的 GeoFlow 工作流；核心思想是把自然语言解析成可执行的空间变换图，再用计算与验证闭环抑制空间幻觉。
- [Think, Act, Build](https://arxiv.org/abs/2604.00528)（开源代码：暂未见稳定公开官方仓库）：面向零样本三维视觉 grounding 的 agentic framework；核心思想是把思考、三维动作和场景构建交替执行，用工具反馈逐步收敛目标定位。
- [MAG-3D](https://arxiv.org/abs/2604.09167)（开源代码：暂未见稳定公开官方仓库）：面向 3D understanding 的多 agent grounded reasoning；核心思想是将场景理解、空间关系判断和结果校验拆成协作角色，提升复杂三维推理的可验证性。
- [ViSRA](https://arxiv.org/abs/2605.10106)（开源代码：未确认公开）：training-free video-based spatial reasoning agent；核心思想是把 MLLM 推理接到显式空间专家输出上，使视频空间推理模块化、可迁移，而不是依赖特定空间 benchmark 的后训练。

## 1.7.4 Skill

- [computer-vision-opencv](https://skills.sh/mindrally/skills/computer-vision-opencv) 适合几何变换、透视校正、连通域与目标定位。
- [computer-vision-expert](https://skills.sh/sickn33/antigravity-awesome-skills/computer-vision-expert) 更偏“图像分析套路库”，适合空间推理前的视觉预处理。
