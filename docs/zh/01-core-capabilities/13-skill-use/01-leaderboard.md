# 1.13.1 Leaderboard

- [SkillsBench Leaderboard](https://www.skillsbench.ai/leaderboard)：当前最直接的 skill-use 持续榜单。
  它按 `no skill / curated skill / self-generated skill` 等条件对比 agent，适合判断 skill 是否真正改善任务成功率，而不是只比较底层模型能力。
- [PinchBench](https://pinchbench.com/about)：OpenClaw 生态中的真实任务榜单/评测入口。
  它不是纯 skill benchmark，但任务集中包含 ClawHub skill 安装、skill 搜索和 skill 使用相关场景，适合作为产品化 skill 生态的实践补充。
- [Letta Context-Bench Skills Suite](https://leaderboard.letta.com/)：包含 skill-suite 评测的公开榜单，面向 agentic context management。
  它的范围比 skill use 更宽，但其中的 skills 切片适合比较 agent 能否在任务场景中选择并应用 context package，而不只是消费预先附加的 skill 文件。
- [SkillTester](https://skilltester.ai/)：官方的 skill 效用与安全性排名页面。
  它可作为补充榜单，因为它同时评估 skill 是否改善执行，以及可复用 skill artifact 带来的安全风险。
- [SkillSafetyBench](https://jinchang1223.github.io/skill-safety-bench-website/)：面向 skill-facing attack surface 的官方项目和榜单/结果页面。
  它补充了偏效用的 skill benchmark，衡量第三方 skill、本地材料或本地 artifact 是否会诱导 agent 执行不安全行为。
- [Claw-Eval-Live](https://claw-eval-live.github.io/)：持续 workflow agent 榜单，显式使用 ClawHub skill 信号构造任务。
  它更适合观察 agent 在动态 workflow 中能否发现、安装、调用和验证 skills，而不是只在理想给定 skill 条件下比较 pass rate。
