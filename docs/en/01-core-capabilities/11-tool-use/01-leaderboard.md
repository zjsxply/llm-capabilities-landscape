# 1.11.1 Leaderboard

- [BFCL / Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html): A continuous leaderboard suitable as the main reference for pure function calling.
  It focuses on isolating tool selection, argument filling, schema following, and multi-turn call accuracy, making it more suitable for comparing structured invocation capability in models/agents than full software-engineering execution capability.
- [ToolBench / ToolEval Leaderboard](https://openbmb.github.io/ToolBench/): The official OpenBMB leaderboard for ToolBench and ToolEval.
  It is a useful bridge between function-calling benchmarks and real-API tool use because it reports pass-rate and win-rate style metrics over multi-step API-use trajectories.
- [MTU-Bench](https://mtu-bench-team.github.io/): An official static leaderboard for multi-granularity tool-use evaluation.
  Its normal and hard splits make it useful for checking whether models handle tool-use difficulty beyond single-call function selection.
- [GTA / General Tool Agents](https://open-compass.github.io/GTA/): An official OpenCompass leaderboard for general tool-agent evaluation.
  It complements BFCL and ToolBench by ranking agents across a broader set of tool-use tasks rather than only schema-constrained function calls.
- [τ-bench / τ²-Bench](https://www.taubench.com/) ([τ²-Bench submission instructions](https://github.com/sierra-research/tau2-bench/blob/main/docs/leaderboard-submission.md)): A leaderboard/submission workflow for multi-turn tool use with stateful APIs.
  Its value lies in connecting customer service, business rules, database state, and tool returns into executable tasks, making it suitable for screening agent scaffolds that handle realistic API orchestration.
- [LiveMCPBench](https://icip-cas.github.io/LiveMCPBench/): The official project and leaderboard entry point for retrieval, routing, and composition in a large MCP tool space.
  It is especially useful for comparing agents on tool discovery and tool combination across many MCP servers and hundreds of tools.
- [MCP-Universe](https://mcp-universe.github.io/): Salesforce AI Research's official MCP-Universe leaderboard page.
  It reports overall, LLM, function-call, and agent tracks, making it useful for separating base model tool-call quality from full agent execution in real MCP environments.
- [MCP-Bench](https://github.com/Accenture/mcp-bench): The official MCP-Bench repository, whose README includes a public leaderboard table.
  It is worth listing because the leaderboard is repository-hosted rather than on a separate site, and it focuses on reproducible MCP agent runs with call trajectory recording and task scoring.
- [Tool Decathlon (Toolathlon)](https://toolathlon.xyz/): A public leaderboard for cross-application, multi-tool, long-chain tasks.
  Compared with BFCL's function-signature prediction, it is closer to MCP/real-application toolchain settings, making it suitable for observing whether agents can complete tasks reliably under many tools, cross-application state, and dedicated checking scripts.
- [MCP-Atlas](https://labs.scale.com/leaderboard/mcp_atlas): Scale AI's public leaderboard for multi-step MCP tool orchestration on real MCP servers.
  It is useful for comparing agents on tool discovery, argument alignment, recovery, and claims-based scoring across realistic server-backed tasks rather than only synthetic function signatures.
- [MCPMark](https://mcpmark.ai/leaderboard/mcp): An official leaderboard for MCP server capability and task coverage.
  The page ranks MCP servers and highlights how comprehensive, stateful MCP task suites can expose missing or unreliable tool surfaces that downstream agents depend on.
- [VitaBench](https://vitabench.github.io/): An official leaderboard for multi-step tool invocation in real-application toolchains.
  It is useful for comparing whether agents can compose tools and verify results across executable workflows, not just predict a single function call.
- [HAL / Holistic Agent Leaderboard](https://hal.cs.princeton.edu/): A widely used public agent leaderboard that includes tool-mediated tasks such as τ-bench alongside web, computer-use, and software settings.
  It is not a single benchmark's official page, but it is a useful cross-benchmark ranking for checking whether tool-use gains transfer beyond one function-calling protocol.
- [Claw-Eval-Live](https://claw-eval-live.github.io/): A continuously updated workflow-agent leaderboard covering terminal, file, web, service, and skill-related tasks.
  It is not a pure function-calling leaderboard, but it is suitable as a cross-reference for tool-use, terminal-use, and skill-use, especially for observing transferability of agent harnesses on dynamic real workflows.
