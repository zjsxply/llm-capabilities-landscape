# 1.7.5 Agent Harness

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
