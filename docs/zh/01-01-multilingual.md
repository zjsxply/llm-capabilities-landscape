# 1.1 多语言

> 上级章节：1. 基础能力


## 1.1.1 Leaderboard

- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)：多语文本嵌入与检索能力的公开榜单；价值在于提供可复用的 embedding/RAG 前置能力评测入口，可与 MIRAGE-Bench、AfriMTEB 等多语 RAG/检索任务衔接。

## 1.1.2 Bench

- [XNLI](https://arxiv.org/abs/1809.05053)：评测跨语言自然语言推断（NLI）；核心思想是把推断题（蕴含/矛盾/中立）扩展到多语设置，测量跨语言语义对齐与推理一致性。
- [TyDi QA](https://arxiv.org/abs/2003.05002)：评测多语言问答（更强调“母语提问”的真实性与语言多样性）；核心思想是覆盖类型学更分散的语言，并以 QA 协议测量检索/理解在跨语言下的鲁棒性。
- [FLORES-200](https://arxiv.org/abs/2207.04672)（[开源代码](https://github.com/facebookresearch/flores)）：评测大规模多语机器翻译与跨语生成；核心思想是以高覆盖语言集合与标准化参考译文，衡量多语生成质量与跨语言迁移。
- [MMMLU](https://huggingface.co/datasets/openai/MMMLU)：评测多语环境下的通识与学科知识选择题能力；核心思想是把同类知识题迁移到多语输入，以统一的多选题协议对齐比较不同语言下的知识保持与理解鲁棒性。
- [Linguini](https://arxiv.org/abs/2409.12126)（[开源代码](https://github.com/facebookresearch/linguini)，[数据集](https://huggingface.co/datasets/facebook/linguini)）：评测 language-agnostic linguistic reasoning。核心思想：从国际语言学奥林匹克式题目出发，让模型在不知道目标语言的情况下从上下文归纳词法、句法和语义规律，补足多语言评测中过度依赖已见语种知识的问题。
- [MIRAGE-Bench](https://arxiv.org/abs/2410.13716)（[开源代码](https://github.com/vectara/mirage-bench)）：评测多语言 RAG 回答生成与裁判效率；核心思想是在 18 种语言的人类问题上结合启发式特征、LLM pairwise judge 和 surrogate judge，降低多语 RAG arena 评测成本。
- [MILU](https://arxiv.org/abs/2411.02538)：评测印度语言的多任务语言理解。核心思想：覆盖 10 种印度语言与英语，并纳入文化相关学科题，作为广义翻译版 MMLU 的垂直补充。
- [INCLUDE](https://arxiv.org/abs/2411.19799)：评测带区域知识的多语言理解。核心思想：从 44 种语言的区域学术和职业考试中取题，减少对英文翻译知识的偏置。
- [GMMLU / Global MMLU](https://arxiv.org/abs/2412.03304)：评测 42 种语言上的 MMLU 式知识理解。核心思想：在可比学科知识协议下比较高、中、低资源语言表现，暴露语言与文化资源差距。
- [MMTEB](https://arxiv.org/abs/2502.13595)（[开源代码](https://github.com/embeddings-benchmark/mteb)）：评测大规模多语文本嵌入；核心思想是在 250 多种语言和 500 多个质量控制任务上统一比较 embedding 的检索、分类、聚类和语义匹配能力。
- [MMLU-ProX](https://arxiv.org/abs/2503.10497)（数据集：[li-lab/MMLU-ProX](https://huggingface.co/datasets/li-lab/MMLU-ProX)）：评测更难的跨语言学科/专业知识（MMLU-Pro 风格的跨语扩展）；核心思想是用更高难度、更强调鲁棒性的专业题补齐“多语 + 专业知识”维度。
- [MultiLoKo](https://arxiv.org/abs/2504.10356)（[开源代码](https://github.com/facebookresearch/MultiLoKo)）：评测 31 种语言中的本地知识与跨语知识迁移；核心思想是同时提供语言本地题、人工翻译题和机器翻译题，区分“知道事实”和“能用目标语言稳定表达/检索事实”。
- [X-WebAgentBench](https://arxiv.org/abs/2505.15372)（[开源代码](https://github.com/WPENGxs/X-WebAgentBench)）：评测多语言交互式 Web agent 的规划与交互能力；核心思想是把 agentic web 任务扩展到多语言环境，检查跨语对齐方法是否真的能支撑全球化 agent 服务。
- [Trojsten Benchmark](https://doi.org/10.18653/v1/2025.emnlp-main.1779)：评什么：斯洛伐克语开放作答的 STEM 竞赛题求解，覆盖数学、物理和编程。核心思想：用低资源语言的原生题目和 rubric 评分暴露翻译题或英语中心 STEM 评测不容易发现的推理失效。
- [MAPS](https://aclanthology.org/2026.findings-eacl.42/)（数据集：[Fujitsu-FRE/MAPS](https://huggingface.co/datasets/Fujitsu-FRE/MAPS)）：评测多语 agent 的性能与安全性；核心思想是把 GAIA、MATH、SWE-bench 和 Agent Security Benchmark 等任务翻译到多种语言，观察能力退化与安全回归。
- [MultiNRC](https://arxiv.org/abs/2507.17476)：评测原生多语推理与文化相关常识；核心思想是用母语题而不是英译题，直接暴露词法、文化和语言游戏差异。
- [AfriMTEB](https://arxiv.org/abs/2510.23896)：评测非洲语言文本嵌入与检索/分类等表示能力；核心思想是在 59 种语言、14 类任务和 38 个数据集上扩展 MMTEB，补齐多语评测中非洲语言长期被低估的问题。
- [Global PIQA](https://arxiv.org/abs/2510.24081)（数据集：[mrlbenchmarks/global-piqa-nonparallel](https://huggingface.co/datasets/mrlbenchmarks/global-piqa-nonparallel)）：评测跨语言的物理常识与日常合理性判断（PIQA 风格）；核心思想是用常识可判定的对比选项题型，测量“语言变化”对常识推理稳定性的影响。
- [DiscoX（Disco-X）](https://arxiv.org/abs/2511.10984)：评测面向专家领域的 discourse-level 翻译与跨句一致性；核心思想是用更长语篇与领域术语约束，暴露“句内翻译正确但跨句不一致/指代错配”等多语难点。
- [AncientBench](https://arxiv.org/abs/2512.17756)：评什么：出土文献与传世古汉语语料的理解。核心思想：把古文字理解拆成字形、读音、词义和上下文任务，覆盖现代语言 benchmark 难以触及的历史中文材料。
- [GreekMMLU](https://arxiv.org/abs/2602.05150)：评测希腊语原生多任务语言理解；核心思想是用来自学术、职业和政府考试的希腊语题目替代英译题，检验模型是否真正覆盖目标语言的教育与文化语境。
- [Macaron](https://arxiv.org/abs/2602.10732)：评测多语多文化推理；核心思想是用人工编写的模板把推理类型和文化因素解耦，在 20 个国家/文化语境与 20 种语言/方言中比较英语题与本地语言题的差异。


## 1.1.3 Agent Harness

- [ReAct](https://arxiv.org/abs/2210.03629)（[开源代码](https://github.com/ysymyth/ReAct)）：通用 `think -> act -> observe` 框架；在多语场景更像“可控的跨语工作流骨架”，便于把 `语种检测 -> 翻译/回译 -> 检索/查证 -> 输出` 显式化，而不是把跨语处理隐含在一次回答里。
- [Reflexion](https://arxiv.org/abs/2303.11366)（[开源代码](https://github.com/noahshinn024/reflexion)）：通过失败反思与记忆回写迭代改进回答；在多语任务里可用于跨轮修复“术语错译、约束遗漏、实体错配”等错误。
- [DSPy](https://arxiv.org/abs/2310.03714)（[开源代码](https://github.com/stanfordnlp/dspy)）：把 `翻译 -> 检索 -> 作答 -> 校验` 组织为可编排 program；在多语任务里适合固化跨语检索与证据一致性约束。
- [EfficientXLang](https://arxiv.org/abs/2507.00246)（[开源代码](https://github.com/microsoft/EfficientXLang)）：跨语言 test-time reasoning harness；核心思想是把同一推理任务路由到更 token-efficient 的语言执行，再检查准确率与语言一致性是否保持，适合做多语推理成本/质量权衡实验。

## 1.1.4 Skill

- [translation-expertise](https://skills.sh/shino369/claude-code-personal-workspace/translation-expertise) 适合跨语言提示重写、术语对齐与高保真翻译。
- [sentence-transformers](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/ai-research/rag-sentence-transformers) 明确支持 multilingual embedding，适合跨语检索与跨语 RAG。
