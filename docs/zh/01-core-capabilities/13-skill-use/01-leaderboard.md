# 1.13.1 Leaderboard

- [SkillsBench Leaderboard](https://www.skillsbench.ai/leaderboard)：当前最直接的 skill-use 持续榜单。
  它按 `no skill / curated skill / self-generated skill` 等条件对比 agent，适合判断 skill 是否真正改善任务成功率，而不是只比较底层模型能力。
- [PinchBench](https://pinchbench.com/about)：OpenClaw 生态中的真实任务榜单/评测入口。
  它不是纯 skill benchmark，但任务集中包含 ClawHub skill 安装、skill 搜索和 skill 使用相关场景，适合作为产品化 skill 生态的实践补充。
- [Claw-Eval-Live](https://claw-eval-live.github.io/)：持续 workflow agent 榜单，显式使用 ClawHub skill 信号构造任务。
  它更适合观察 agent 在动态 workflow 中能否发现、安装、调用和验证 skills，而不是只在理想给定 skill 条件下比较 pass rate。
