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
- [Spatial-Gym](https://arxiv.org/abs/2604.09338)：评测 agent 能否把空间推理转成连续动作。核心思想：用 Gymnasium 风格交互 benchmark 覆盖 pathfinding、backtracking 与 action-level scoring，而不是只做被动空间问答。
- [Minedojo-Verified](https://github.com/ByteDance-Seed/Seed2.0)：Seed2.0 model card 报告的 embodied-agent 视觉任务 verified 子集；目前未确认有独立公开版本。核心思想：跟踪前沿多模态 agent 是否能在交互环境中完成感知 grounding、规划和动作执行，而不只是在静态截图上答题。

## 2.11.3 Agent Harness

- MineDojo、CALVIN、VIMA 和 LIBERO 本身也是 benchmark-side harness：它们定义环境、观测、动作空间、任务重置和成功检查。可复用设计模式是 `观察多模态状态 -> 解析语言目标 -> 计划/子目标 -> 行动 -> 验证环境状态 -> 恢复`。

## 2.11.4 Skill

- [computer-vision-opencv](https://skills.sh/mindrally/skills/computer-vision-opencv) 适合模拟具身环境中的感知侧预处理与视觉诊断。
- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) 适合需要隔离运行时的具身或游戏环境搭建。
