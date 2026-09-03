# 1.16 Agent Swarm

> 上级章节：1. 基础能力

Agent Swarm 覆盖能够灵活启动、路由、裁剪或协调多个 agent 或 subagent 的系统，通常用于把长任务或宽任务拆成可并行执行的分支，再统一汇总、验证或修订结果。它区别于普通多智能体对话：这里的核心贡献是动态分解、并行执行、上下文隔离、角色路由，或 swarm 层面的成本与一致性控制。

[Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/) 和 [Context Rot](https://research.trychroma.com/context-rot) 这类长上下文诊断构成了这一能力轴的直接动机：单纯扩展 prompt 可能降低检索和推理质量，因此 swarm 设计常用更小的任务局部上下文和显式聚合，替代把全部证据塞进一个单体上下文。

## Sections

- [1.16.1 Leaderboard](01-leaderboard.md)
- [1.16.2 Survey](02-survey.md)
- [1.16.3 Bench](03-bench.md)
- [1.16.4 Model](04-model.md)
- [1.16.5 Agent Harness](05-agent-harness.md)
- [1.16.6 Skill](06-skill.md)
