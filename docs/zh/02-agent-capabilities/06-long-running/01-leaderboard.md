# 2.6.1 Leaderboard

- [AssistantBench Leaderboard](https://huggingface.co/spaces/AssistantBench/leaderboard)：公开真实耗时网页助理任务的提交入口；它把 test set 答案隐藏并用 Hugging Face portal 收集预测，适合跟踪 web agent 在长程浏览与信息转移任务上的持续进展。
- [METR Time Horizon Reports](https://github.com/METR/eval-analysis-public)：持续发布 time-horizon 版本化报告和可复现分析代码；它不是单一分数榜，而是把 agent 能完成的任务人类时长作为长期自治能力曲线来比较。
- [OSWorld-Human Efficiency Leaderboard](https://github.com/WukLab/osworld-human)：把 OSWorld 成功率和人类参考轨迹效率放在一起比较，特别适合发现长程 GUI agent 通过大量冗余步骤“勉强完成”的问题。
- [HAL Long-Horizon Tracks](https://hal.cs.princeton.edu/)：Princeton HAL 聚合 AssistantBench、GAIA、Online Mind2Web 等任务，并报告成本、运行时间和 pass rate；可作为跨 benchmark 比较 long-horizon agent harness 的元榜单。
- [ClawMark Leaderboard](https://claw-mark.com/leaderboard)：面向 1 到 3 天 timeline 的 coworker-agent 任务榜单，覆盖多模态输入、日历等待、消息协同和跨天状态维护，是比单会话长任务更接近 long-running autonomy 的公开入口。
