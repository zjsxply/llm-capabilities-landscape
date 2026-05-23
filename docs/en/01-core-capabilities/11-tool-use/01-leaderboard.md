# 1.11.1 Leaderboard

- [BFCL / Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html): A continuous leaderboard suitable as the main reference for pure function calling.
  It focuses on isolating tool selection, argument filling, schema following, and multi-turn call accuracy, making it more suitable for comparing structured invocation capability in models/agents than full software-engineering execution capability.
- [τ-bench / τ²-Bench](https://www.taubench.com/) ([τ²-Bench submission instructions](https://github.com/sierra-research/tau2-bench/blob/main/docs/leaderboard-submission.md)): A leaderboard/submission workflow for multi-turn tool use with stateful APIs.
  Its value lies in connecting customer service, business rules, database state, and tool returns into executable tasks, making it suitable for screening agent scaffolds that handle realistic API orchestration.
- [Tool Decathlon (Toolathlon)](https://toolathlon.xyz/): A public leaderboard for cross-application, multi-tool, long-chain tasks.
  Compared with BFCL's function-signature prediction, it is closer to MCP/real-application toolchain settings, making it suitable for observing whether agents can complete tasks reliably under many tools, cross-application state, and dedicated checking scripts.
- [Claw-Eval-Live](https://claw-eval-live.github.io/): A continuously updated workflow-agent leaderboard covering terminal, file, web, service, and skill-related tasks.
  It is not a pure function-calling leaderboard, but it is suitable as a cross-reference for tool-use, terminal-use, and skill-use, especially for observing transferability of agent harnesses on dynamic real workflows.
