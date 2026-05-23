# 2.7.1 Leaderboard

- [GAIA Leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard)：通用现实助理任务的长期公开榜单，覆盖推理、网页浏览、多模态和工具使用；它仍是比较“能否完成真实问题”而非单工具能力的重要入口。
- [TheAgentCompany Leaderboard](https://the-agent-company.com/#/leaderboard)：面向模拟软件公司数字员工任务的公开榜单；适合观察现实工作中网页、代码、文件和同事通信混合任务的端到端完成率。
- [HAL / Holistic Agent Leaderboard](https://hal.cs.princeton.edu/)（[开源 harness](https://github.com/princeton-pli/hal-harness)）：跨 GAIA、AssistantBench、tau-bench、Online Mind2Web、SWE-bench Verified 等任务报告 accuracy、cost、runtime 和 traces；价值在于把模型、agent scaffold 和评测成本一起公开比较。
- [GDPval Leaderboard](https://evals.openai.com/gdpval/leaderboard)：面向经济价值任务交付物的公开榜单；重点看 rubric 驱动的专业输出质量，并把模型能力、上下文和 scaffolding 的现实工作收益放到同一入口。
- [Remote Labor Index Leaderboard](https://labs.scale.com/leaderboard/rli)：围绕真实远程劳动项目的自动化率和交付质量持续比较 agent；与 GDPval 互补，强调可外包项目、经济信号和端到端交付。
- [APEX-Agents Leaderboard](https://www.mercor.com/apex/apex-agents-leaderboard/)：覆盖投行、咨询、公司法律等专业服务任务的公开榜单；它把文件、工具、rubric 和 gold outputs 作为现实白领工作交付物评估对象。
- [ClawBench Leaderboard](https://claw-bench.com/)：真实 live website 写操作任务榜单，记录 model、harness、trace、HTTP interception 和 reward；现实网页工作流中 agent 行为是否可审计是它的主要价值。
- [ClawMark Leaderboard](https://claw-mark.com/leaderboard)：多日历时间 coworker-agent 工作流榜单，适合跟踪能跨天等待、回忆和协同的真实工作 agent，而不是只完成单次会话任务。
