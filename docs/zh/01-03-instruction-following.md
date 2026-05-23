# 1.3 指令遵循

> 上级章节：1. 基础能力


## 1.3.1 Leaderboard

- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)：包含 IFEval 的公开综合榜单；价值在于把可验证指令遵循纳入主流模型评测生态。
- [FollowBench Leaderboard](https://github.com/YJiangcm/FollowBench)：多层级复杂指令遵循榜单；价值在于按内容、情境、风格、格式和示例约束观察模型随复杂度增加的退化。
- [LiveBench](https://livebench.ai/)：包含 `instruction_following` 类别的动态公开榜单；价值在于用持续更新的数据降低静态基准污染，并提供可运行评测框架。
- [M-IFEval Leaderboard](https://github.com/lightblue-tech/M-IFEval)：多语言 IFEval 扩展榜单；价值在于沿用可验证约束协议，比较法语、日语、西班牙语等语言下的指令遵循差异。
- [AgentIF Leaderboard](https://github.com/THU-KEG/AgentIF)：agentic 场景指令遵循榜单；价值在于把长系统提示、工具说明和复杂约束纳入真实 agent 应用评测。
- [MathIF Leaderboard](https://github.com/TingchenFu/MathIF)：数学推理任务中的指令遵循榜单；价值在于评估模型在保持推理正确性的同时能否满足可程序验证约束。
- [IFBench Leaderboard](https://github.com/allenai/IFBench)：可验证指令遵循泛化榜单；价值在于用未见约束类型和多轮设置检查模型是否只过拟合 IFEval 风格模板。
- [IFScale Leaderboard](https://distylai.github.io/IFScale/)：指令数量压力测试榜单；价值在于用 10 到 500 条 simultaneous instructions 观察约束负载增加时的退化模式。

## 1.3.2 Bench

- [COLLIE](https://arxiv.org/abs/2307.08689)：评测受约束文本生成与复杂指令遵循；核心思想是把约束（格式、包含/排除、长度、集合约束等）做成可组合、可判定的诊断任务族。
- [FollowBench](https://arxiv.org/abs/2310.20410)：评测多层级、细粒度约束遵循；核心思想是把复杂用户指令拆成不同难度和类型的约束，定位模型是在整体任务、局部约束还是细节执行上失败。
- [IFEval](https://arxiv.org/abs/2311.07911)（数据集：[google/IFEval](https://huggingface.co/datasets/google/IFEval)；[Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) 中的指令遵循核心任务）：评测指令遵循（格式、约束、禁止项等）；核心思想是用可判定规则集自动化评测“是否按指令输出”，作为 Inverse IFEval 的直接参照。
- [InFoBench](https://arxiv.org/abs/2401.03601)：评测复杂指令的分解式要求遵循；核心思想是把 500 条多约束指令拆成 2,250 个可判定子要求，用 DRFR 指标衡量模型对每一项要求的满足程度。
- [LiveBench Instruction Following](https://arxiv.org/abs/2406.19314)（[开源代码](https://github.com/livebench/livebench)）：评测动态更新榜单中的指令遵循类别；核心思想是用持续更新、可自动评分的数据降低污染，并把 instruction following 放入更广泛的综合能力比较。
- [MultiChallenge](https://arxiv.org/abs/2501.17399)：评测更贴近真实多轮对话下的指令遵循与一致性；核心思想是把“多轮约束累积、角色/规则持续有效”作为难点，而不是单轮指令执行。
- [M-IFEval](https://arxiv.org/abs/2502.04688)（[开源代码](https://github.com/lightblue-tech/M-IFEval)）：评测多语言可验证指令遵循；核心思想是把 IFEval 风格规则扩展到法语、日语和西班牙语，检查约束检查器与模型行为是否跨语言稳定。
- [CodeIF](https://arxiv.org/abs/2502.19166)（[开源代码](https://github.com/lin-rany/codeIF)）：评测代码生成任务中的指令遵循；核心思想是覆盖函数合成、错误调试、算法重构和代码解释等场景，检查模型是否能在生成代码时同时满足任务目标与约束细节。
- [XIFBench](https://arxiv.org/abs/2503.07539)（[开源代码](https://github.com/zhenyuli801/XIFBench)）：评测多语言指令遵循；核心思想是在 6 种语言中设置内容、风格、情境、格式和数值约束，并用需求级语义锚点比较不同资源语言下的约束满足差异。
- [DeR2](https://arxiv.org/abs/2503.14443)：偏 context learning/长上下文评测，但也可反映复杂约束在长上下文执行中的“遗漏/漂移”；核心思想是用长上下文任务压力测试约束是否被持续执行。
- [MathIF](https://arxiv.org/abs/2505.14810)（[开源代码](https://github.com/TingchenFu/MathIF)）：评测数学推理中的指令遵循；核心思想是用可程序验证的数学任务约束检查模型是否在解题时同时满足格式、包含和过程性要求。
- [LIFEBENCH](https://arxiv.org/abs/2505.16234)（[开源代码](https://github.com/LIFEBench/LIFEBench)，[数据集](https://huggingface.co/datasets/LIFEBench/LIFEBench)）：评测长度指令遵循。核心思想：专测明确的长输出长度约束，例如词数或 token 数要求，暴露模型在本应很长但结构简单的输出中提前结束、严重短写或拒答的问题。
- [AgentIF](https://arxiv.org/abs/2505.16944)（[开源代码](https://github.com/THU-KEG/AgentIF)）：评测 agentic 场景下的长系统提示、工具说明和复杂约束遵循；核心思想是从真实工业与开源 agent 应用收集长指令，并为约束标注 code/LLM/hybrid 评测器。
- [MARS-Bench](https://arxiv.org/abs/2505.23810)（数据集：[LeeeeTX/MARS-Bench](https://huggingface.co/datasets/LeeeeTX/MARS-Bench)）：评测多轮真实场景对话下的指令遵循与对话质量；核心思想是用更贴近真实交互的 multi-turn 设定衡量约束执行的稳定性。
- [IFBench](https://arxiv.org/abs/2507.02833)：评测可验证指令遵循在未见约束上的泛化；核心思想是新增 58 类可程序验证的 out-of-domain 约束，避免只在 IFEval 风格的少量模板约束上过拟合。
- [IFScale](https://arxiv.org/abs/2507.11538)（[开源代码](https://github.com/DistylAI/distylai.github.io)）：评测指令数量扩展时的约束遵循退化；核心思想是把同时需要满足的关键词包含指令从 10 条扩到 500 条，观察模型在高约束负载下的失败模式。
- [Inverse IFEval](https://arxiv.org/abs/2509.04292)（数据集：[m-a-p/Inverse_IFEval](https://huggingface.co/datasets/m-a-p/Inverse_IFEval)）：评测模型在“反向指令”或去偏设置下是否仍能严格遵循指令；核心思想是通过逆向指令构造，测量模型对模板化输出惯性的抵抗与指令鲁棒性。
- [EvolIF](https://arxiv.org/abs/2511.03508)：评测动态演化多轮指令遵循；核心思想是用 query synthesis agent 与三层状态追踪机制模拟用户耐心耗尽前的连续约束追加、状态变化与失败恢复。
- [VIFBENCH](https://arxiv.org/abs/2601.17789)：评测指令遵循 verifier 的细粒度判定能力；核心思想是把输出是否遵循指令拆成带标签的 constraint satisfaction 判断，专测验证器而不只是生成模型。
- [CL-Bench](https://arxiv.org/abs/2602.03587)：同样偏 context learning，但对“规则是否被长期遵循”的诊断有参考价值；核心思想是用更系统的长上下文设置暴露指令跟随的边界。
- [SEQUOR](https://arxiv.org/abs/2605.06353)：评测长多轮对话中的现实约束遵循；核心思想是把新增、替换与冲突约束都放进同一协议，专测长对话漂移。

## 1.3.3 Agent Harness

- lm-evaluation-harness（[开源代码](https://github.com/EleutherAI/lm-evaluation-harness)）：通用语言模型评测执行框架；价值在于已经包含 `ifeval` 任务实现，适合把指令遵循规则检查接入可复现实验流水线。
- [HELM](https://arxiv.org/abs/2211.09110)（[开源代码](https://github.com/stanford-crfm/helm)）：通用评测 harness；在指令遵循任务中可复用 IFEval 场景与 strict accuracy 指标，把规则检查、模型调用和结果汇总标准化。
- [Reflexion](https://arxiv.org/abs/2303.11366)（[开源代码](https://github.com/noahshinn024/reflexion)）：把失败经验以文本记忆沉淀进下一轮执行，适合多轮约束任务的持续改进。
- [Self-Refine](https://arxiv.org/abs/2303.17651)（[开源代码](https://github.com/madaan/self-refine)）：`先生成 -> 自评 -> 自改` 的 repair loop，可作为复杂指令执行的通用自修复骨架。
- [Re5](https://arxiv.org/abs/2507.05598)：面向指令遵循的 self-review/revision harness；核心思想是先抽取任务与约束，再做结构评估、约束级内容评估和选择性修订，减少盲目多轮自改带来的质量退化。
- [NSVIF](https://arxiv.org/abs/2601.17789)：神经符号指令遵循验证框架；核心思想是把自然语言指令建模为逻辑与语义约束，并由统一求解器生成可解释反馈，可作为 agent 输出前的独立合规检查层。

## 1.3.4 Skill

- [json-schema-validator](https://skills.sh/dkyazzentwatwa/chatgpt-skills/json-schema-validator) 适合结构化输出检查。
- [schema-creator](https://skills.sh/oimiragieo/agent-studio/schema-creator) 适合先把模糊要求固化成可检验 schema。
- [validation](https://skills.sh/profpowell/vanilla-breeze/validation) 适合在输出阶段加一层规则审计。
- [prompt-engineering-outlines](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/ai-research/prompt-engineering-outlines) 适合把 `Pydantic / JSON Schema / constrained decoding` 直接接入提示工作流。
