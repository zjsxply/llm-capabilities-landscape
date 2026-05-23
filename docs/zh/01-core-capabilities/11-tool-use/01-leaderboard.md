# 1.11.1 Leaderboard

- [BFCL / Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)：持续榜单，适合作为纯 function calling 的主参考。
  它重点隔离工具选择、参数填充、schema 遵循和多轮调用准确性，因此更适合比较模型/agent 的结构化调用能力，而不是完整软件工程执行能力。
- [τ-bench / τ²-Bench](https://www.taubench.com/)（[τ²-Bench 提交说明](https://github.com/sierra-research/tau2-bench/blob/main/docs/leaderboard-submission.md)）：面向带状态 API 的多轮工具使用榜单/提交流程。
  它的价值在于把客服、业务规则、数据库状态和工具返回串成可执行任务，适合筛选能处理真实 API orchestration 的 agent scaffold。
- [Tool Decathlon（Toolathlon）](https://toolathlon.xyz/)：面向跨应用、多工具、长链路任务的公开榜单。
  相比 BFCL 的函数签名预测，它更接近 MCP/真实应用工具链场景，适合观察 agent 是否能在大量工具、跨应用状态和专用检查脚本下稳定完成任务。
- [Claw-Eval-Live](https://claw-eval-live.github.io/)：持续更新的 workflow agent 榜单，覆盖终端、文件、网页、服务和 skill 相关任务。
  它不是纯 function-calling 榜单，但适合作为 tool-use、terminal-use 和 skill-use 的交叉参照，尤其适合观察 agent harness 在动态真实 workflow 上的迁移性。
