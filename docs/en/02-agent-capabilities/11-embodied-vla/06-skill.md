# 2.11.6 Skill

- [ROSBag MCP Server: Analyzing Robot Data with LLMs for Agentic Embodied AI Applications](https://arxiv.org/abs/2511.03497): Candidate reusable agent-tool or skill infrastructure contribution for embodied and VLA agents; it directly targets this page's capability scope and belongs in the `Skill` track.
- [computer-vision-opencv](https://skills.sh/mindrally/skills/computer-vision-opencv) is useful for perception-side preprocessing and visual diagnostics in simulated embodied environments.
- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) is useful when embodied or game environments require isolated runtime setup.
- [vla-evaluation-harness skills](https://github.com/allenai/vla-evaluation-harness/tree/main/.claude/skills) provide reusable workflows for adding benchmark adapters, adding model servers, and running VLA evaluations, making benchmark integration itself an agent-readable skill surface.
- [AgenticROS](https://github.com/agenticros/agenticros) exposes ROS2, OpenClaw, MCP, Gazebo/RViz, and robot-control adapters as an agent-facing runtime layer, useful when embodied skills need to connect to robot middleware rather than stay as learned policy primitives.
