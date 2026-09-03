# 1.11.1 Leaderboard

- [BFCL / Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)：持续榜单，适合作为纯 function calling 的主参考。
  它重点隔离工具选择、参数填充、schema 遵循和多轮调用准确性，因此更适合比较模型/agent 的结构化调用能力，而不是完整软件工程执行能力。
- [ToolBench / ToolEval Leaderboard](https://openbmb.github.io/ToolBench/)：OpenBMB 面向 ToolBench 和 ToolEval 的官方榜单。
  它用 pass-rate 和 win-rate 风格指标评估多步 API 使用轨迹，是 function-calling benchmark 与真实 API 工具使用之间的重要过渡。
- [MTU-Bench](https://mtu-bench-team.github.io/)：面向多粒度工具使用评测的官方静态榜单。
  其 normal 和 hard 划分适合检查模型是否能处理超出单次函数选择的工具使用难度。
- [GTA / General Tool Agents](https://open-compass.github.io/GTA/)：OpenCompass 面向通用工具 agent 评测的官方榜单。
  它通过更广泛的工具使用任务补充 BFCL 和 ToolBench，而不只比较 schema 约束下的函数调用。
- [τ-bench / τ²-Bench](https://www.taubench.com/)（[τ²-Bench 提交说明](https://github.com/sierra-research/tau2-bench/blob/main/docs/leaderboard-submission.md)）：面向带状态 API 的多轮工具使用榜单/提交流程。
  它的价值在于把客服、业务规则、数据库状态和工具返回串成可执行任务，适合筛选能处理真实 API orchestration 的 agent scaffold。
- [LiveMCPBench](https://icip-cas.github.io/LiveMCPBench/)：面向大规模 MCP 工具空间中检索、路由与组合的官方项目和榜单入口。
  它尤其适合比较 agent 在多个 MCP server 和数百个工具上的工具发现与工具组合能力。
- [MCP-Universe](https://mcp-universe.github.io/)：Salesforce AI Research 的 MCP-Universe 官方榜单页。
  它提供 overall、LLM、function-call 和 agent tracks，适合区分基础模型工具调用质量与真实 MCP 环境中的完整 agent 执行能力。
- [MCP-Bench](https://github.com/Accenture/mcp-bench)：MCP-Bench 官方仓库，其 README 中包含公开榜单表。
  该榜单托管在仓库而非独立网站上，重点比较带调用轨迹记录和任务评分的可复现 MCP agent 运行。
- [Tool Decathlon（Toolathlon）](https://toolathlon.xyz/)：面向跨应用、多工具、长链路任务的公开榜单。
  相比 BFCL 的函数签名预测，它更接近 MCP/真实应用工具链场景，适合观察 agent 是否能在大量工具、跨应用状态和专用检查脚本下稳定完成任务。
- [MCP-Atlas](https://labs.scale.com/leaderboard/mcp_atlas)：Scale AI 面向真实 MCP server 多步工具编排的公开榜单。
  它适合比较 agent 在工具发现、参数对齐、失败恢复和 claims-based scoring 下的表现，而不只比较合成函数签名上的调用正确性。
- [MCPMark](https://mcpmark.ai/leaderboard/mcp)：MCP server 能力和任务覆盖的官方榜单。
  该页面按 MCP server 排名，并展示综合性、状态性 MCP 任务如何暴露 agent 所依赖工具面的缺失或不稳定。
- [VitaBench](https://vitabench.github.io/)：面向真实应用工具链中多步工具调用的官方榜单。
  它适合比较 agent 能否在可执行 workflow 中组合工具并验证结果，而不只是预测单次函数调用。
- [HAL / Holistic Agent Leaderboard](https://hal.cs.princeton.edu/)：一个常用的公开 agent 综合榜单，其中包含 τ-bench 等工具介导任务，也覆盖 web、computer-use 和软件任务。
  它不是某一个 benchmark 的官方页，但适合检查 tool-use 增益是否能迁移到单一 function-calling 协议之外。
- [Claw-Eval-Live](https://claw-eval-live.github.io/)：持续更新的 workflow agent 榜单，覆盖终端、文件、网页、服务和 skill 相关任务。
  它不是纯 function-calling 榜单，但适合作为 tool-use、terminal-use 和 skill-use 的交叉参照，尤其适合观察 agent harness 在动态真实 workflow 上的迁移性。
