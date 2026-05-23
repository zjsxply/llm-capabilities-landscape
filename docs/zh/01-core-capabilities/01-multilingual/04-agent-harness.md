# 1.1.4 Agent Harness

- [ReAct](https://arxiv.org/abs/2210.03629)（[开源代码](https://github.com/ysymyth/ReAct)）：通用 `think -> act -> observe` 框架；在多语场景更像“可控的跨语工作流骨架”，便于把 `语种检测 -> 翻译/回译 -> 检索/查证 -> 输出` 显式化，而不是把跨语处理隐含在一次回答里。
- [Reflexion](https://arxiv.org/abs/2303.11366)（[开源代码](https://github.com/noahshinn024/reflexion)）：通过失败反思与记忆回写迭代改进回答；在多语任务里可用于跨轮修复“术语错译、约束遗漏、实体错配”等错误。
- [DSPy](https://arxiv.org/abs/2310.03714)（[开源代码](https://github.com/stanfordnlp/dspy)）：把 `翻译 -> 检索 -> 作答 -> 校验` 组织为可编排 program；在多语任务里适合固化跨语检索与证据一致性约束。
- [MAATS](https://arxiv.org/abs/2505.14848)：基于 MQM 评估的多智能体自动翻译框架。核心思路：把翻译、质量分析和修订拆分为协作角色，使多语言生成能够按照显式标准改进和审计。
- [EfficientXLang](https://arxiv.org/abs/2507.00246)（[开源代码](https://github.com/microsoft/EfficientXLang)）：跨语言 test-time reasoning harness；核心思想是把同一推理任务路由到更 token-efficient 的语言执行，再检查准确率与语言一致性是否保持，适合做多语推理成本/质量权衡实验。
