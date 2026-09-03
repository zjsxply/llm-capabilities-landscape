# 1.16 Agent Swarm

> Parent chapter: 1. Core Capabilities

Agent Swarm covers systems that flexibly spawn, route, prune, or coordinate multiple agents or subagents, usually to decompose a long or broad task into concurrent branches and then merge, verify, or revise the results. It is separate from ordinary multi-agent dialogue when the main contribution is dynamic decomposition, parallel execution, context isolation, role routing, or swarm-level cost and coherence control.

Long-context diagnostics such as [Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/) and [Context Rot](https://research.trychroma.com/context-rot) motivate this axis: simply expanding the prompt can degrade retrieval and reasoning, so swarm designs often use smaller task-local contexts plus explicit aggregation instead of stuffing all evidence into one monolithic context.

## Sections

- [1.16.1 Leaderboard](01-leaderboard.md)
- [1.16.2 Survey](02-survey.md)
- [1.16.3 Bench](03-bench.md)
- [1.16.4 Model](04-model.md)
- [1.16.5 Agent Harness](05-agent-harness.md)
- [1.16.6 Skill](06-skill.md)
