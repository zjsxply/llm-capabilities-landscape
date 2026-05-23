# 1.3.4 Agent Harness

- [HELM](https://arxiv.org/abs/2211.09110)（[开源代码](https://github.com/stanford-crfm/helm)）：通用评测 harness；在指令遵循任务中可复用 IFEval 场景与 strict accuracy 指标，把规则检查、模型调用和结果汇总标准化。
- [Reflexion](https://arxiv.org/abs/2303.11366)（[开源代码](https://github.com/noahshinn024/reflexion)）：把失败经验以文本记忆沉淀进下一轮执行，适合多轮约束任务的持续改进。
- [Self-Refine](https://arxiv.org/abs/2303.17651)（[开源代码](https://github.com/madaan/self-refine)）：`先生成 -> 自评 -> 自改` 的 repair loop，可作为复杂指令执行的通用自修复骨架。
- [Re5](https://arxiv.org/abs/2507.05598)：面向指令遵循的 self-review/revision harness；核心思想是先抽取任务与约束，再做结构评估、约束级内容评估和选择性修订，减少盲目多轮自改带来的质量退化。
- [NSVIF](https://arxiv.org/abs/2601.17789)：神经符号指令遵循验证框架；核心思想是把自然语言指令建模为逻辑与语义约束，并由统一求解器生成可解释反馈，可作为 agent 输出前的独立合规检查层。
- lm-evaluation-harness（[开源代码](https://github.com/EleutherAI/lm-evaluation-harness)）：通用语言模型评测执行框架；价值在于已经包含 `ifeval` 任务实现，适合把指令遵循规则检查接入可复现实验流水线。
