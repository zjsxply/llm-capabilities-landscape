# 2.11.6 Skill

- [ROSBag MCP Server: Analyzing Robot Data with LLMs for Agentic Embodied AI Applications](https://arxiv.org/abs/2511.03497)：可作为具身与 VLA Agent方向的可复用 Agent 工具或技能基础设施贡献候选；其主题直接落在该能力页范围内，归入 `Skill` 轨道。
- [computer-vision-opencv](https://skills.sh/mindrally/skills/computer-vision-opencv) 适合模拟具身环境中的感知侧预处理与视觉诊断。
- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) 适合需要隔离运行时的具身或游戏环境搭建。
- [vla-evaluation-harness skills](https://github.com/allenai/vla-evaluation-harness/tree/main/.claude/skills) 提供新增 benchmark adapter、新增 model server 和运行 VLA 评测的可复用工作流，使 benchmark integration 本身成为 agent-readable skill surface。
- [AgenticROS](https://github.com/agenticros/agenticros) 把 ROS2、OpenClaw、MCP、Gazebo/RViz 和机器人控制 adapter 暴露成面向 agent 的运行时层，适合把具身 skills 接到机器人中间件，而不是停留在 learned policy primitives。
