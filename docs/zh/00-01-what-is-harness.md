# 0.1 什么是 Harness

> 上级章节：0. Harness 与 Skill Creator


- `Harness` 是模型外的任务运行时。
  它通常负责 `任务拆解`、`工具接线`、`上下文组织`、`环境执行`、`搜索/回溯`、`验证与恢复`，因此同一个底模常能复用到多个 benchmark。
- `Harness` 不等于训练算法。
  训练回答“模型学到了什么”，harness 回答“系统怎样把能力稳定变成可执行工作流”。
- 为避免把“训练”与“harness”混在一起，读论文时可先做三分法：
  `模型训练算法`（主要增益来自参数更新或训练数据/目标）、`外围 harness`（主要增益来自任务拆解、控制流、上下文/记忆、工具与环境接口、搜索与验证回路）、`混合型工作`（两者皆有）。
- 读一篇 agent 论文时，先看增益来自哪里。
  如果主要增益来自 `SFT / RL / data scaling / pretraining`，那是模型工作；如果主要增益来自 `planner-executor`、`tool loop`、`memory`、`validator`、`DAG/FSM`、`skill library`，那更接近 harness 工作。
