# 1.9 通用推理（含视觉谜题）

> 上级章节：1. 基础能力


## 1.9.1 Leaderboard

- [LiveBench](https://livebench.ai/)（[开源代码](https://github.com/LiveBench/LiveBench)）：持续更新的综合 LLM 榜，推理、数学、编码、数据分析和语言任务按时间切片发布，适合作为通用推理模型的近时效对照。
- [ARC Prize Leaderboard](https://arcprize.org/leaderboard)（[社区榜](https://arcprize.org/leaderboard/community)）：ARC-AGI-2 与 ARC-AGI-3 的官方竞赛榜，尤其适合观察 `program synthesis + executor + search`、多 agent 试错和游戏环境交互式代理的实际效果。
- [Reasoning Gym Eval](https://github.com/open-thought/reasoning-gym-eval)：围绕 REASONING GYM 的开源评测榜与脚本，适合追踪可生成、可验证任务上的推理与 test-time scaling 方案。

## 1.9.2 Bench

- [ARC（ARC-AGI-1）](https://github.com/fchollet/ARC)：评什么：抽象推理与归纳（小网格变换/规律归纳）；核心思想：以极小数据与强分布外泛化为核心，迫使方法依赖程序归纳/规则抽取，而非语言模板。
- [BIG-Bench Hard](https://arxiv.org/abs/2210.09261)（[开源代码](https://github.com/suzgunmirac/BIG-Bench-Hard)）：评什么：BIG-Bench 中人工筛出的高难推理子任务；核心思想：作为 chain-of-thought 基线常用集合，覆盖符号、常识、算法与语言推断。
- [AGIEval](https://arxiv.org/abs/2304.06364)（[开源代码](https://github.com/ruixiangcui/AGIEval)）：评什么：来自标准化考试和人类能力测试的通用推理；核心思想：用更接近人类考试的题型补充合成任务，覆盖语言、数学、逻辑和专业知识。
- [MuSR](https://arxiv.org/abs/2310.16049)（[开源代码](https://github.com/Zayne-sprague/MuSR)）：评什么：多步软推理，含 murder mystery、object placement 和 team allocation 等任务；核心思想：要求模型在长题干中维护约束并逐步排除候选。
- [GPQA](https://arxiv.org/abs/2311.12022)（[开源代码](https://github.com/idavidrein/gpqa)）：评什么：研究生级、抗搜索的科学问答；核心思想：强调专家级推理和抗数据泄漏，常作为通用推理模型的硬题基线。
- [LiveBench](https://arxiv.org/abs/2406.19314)（[开源代码](https://github.com/LiveBench/LiveBench)）：评什么：持续更新、含推理/数学/编码/语言/数据分析等任务；核心思想：通过时间更新和自动评分降低污染，适合做近时效能力跟踪。
- [LogicVista](https://arxiv.org/abs/2407.04973)（[开源代码](https://github.com/Yijia-Xiao/LogicVista)）：评什么：视觉逻辑推理（更接近“看图做逻辑题/谜题”）；核心思想：用视觉谜题把逻辑约束落到可见结构上，减少纯文本推理的捷径。
- [ProcBench](https://arxiv.org/abs/2410.03117)（[开源代码](https://github.com/ifujisawa/proc-bench)；[数据集](https://huggingface.co/datasets/ifujisawa/procbench)）：评什么：多步推理与“按流程执行”的能力；核心思想：把程序性/步骤性正确性作为主要评价对象，减少只看最终答案的偶然性。
- [ARC-AGI-2（ARC Prize）](https://github.com/arcprize/ARC-AGI-2)：评什么：更强调泛化与抗“刷榜”策略的 ARC 系能力；核心思想：典型有效解法强绑定 `DSL / program synthesis + executor + scoring/search` 的 benchmark-specific runtime，而不是纯对话式提示工程。
- [JustLogic](https://arxiv.org/abs/2501.14851)：评什么：减少先验知识捷径后的演绎推理。核心思想：生成可控的逻辑论证，系统调节推理深度、语言形式和任务复杂度，以支持更细粒度的错误分析。
- [VPCT](https://huggingface.co/datasets/camelCase12/vpct-1)：评什么：视觉模式与规律补全类谜题；核心思想：以 pattern completion/推断为主，常用于检验模型是否能从视觉结构中抽取生成规则。
- [iVISPAR](https://arxiv.org/abs/2502.03214)：评什么：交互式视觉-空间推理与规划；核心思想：把滑块谜题改造成 VLM agent 可交互环境，分别用 2D、3D 与文本模态测量空间规划能力。
- [ZEROBench](https://arxiv.org/abs/2502.09696)（[开源代码](https://github.com/jonathan-roberts1/zerobench)）：评什么：对视觉谜题/规律类任务的泛化与鲁棒性；核心思想：强调“零样本迁移”式的压力测试，检验是否依赖训练分布的捷径。
- [NaturalReasoning](https://arxiv.org/abs/2502.13124)（数据集：[facebook/natural_reasoning](https://huggingface.co/datasets/facebook/natural_reasoning)）：评什么：真实来源中的自然推理问题。核心思想：用 280 万道跨 STEM、经济和社会科学等领域的高难问题覆盖更自然的推理分布，既可用于训练也可用于评估。
- [VisualQuest](https://arxiv.org/abs/2503.19936)：评什么：抽象视觉推理与符号/文化/语言知识整合；核心思想：用非照片化、风格化图像与定向问题检查模型能否把视觉识别和抽象语义推断结合起来。
- [QuestBench](https://arxiv.org/abs/2503.22674)（[开源代码](https://github.com/google-deepmind/questbench)，[数据集](https://huggingface.co/datasets/belindazli/QuestBench)）：评什么：在信息不足的推理任务中能否问出正确澄清问题。核心思想：把缺失信息获取形式化为约束推理问题，评分模型是否能在解题前提出最小必要问题。
- [VGRP-Bench](https://arxiv.org/abs/2503.23064)：评什么：视觉网格推理谜题；核心思想：用 20 类不同难度的 grid puzzle 系统控制线索数、网格大小与规则复杂度，诊断 LVLM 的感知、规则理解和逻辑推理瓶颈。
- [GraphOmni](https://arxiv.org/abs/2504.12764)（[开源代码](https://github.com/GAI-Community/GraphOmni)）：评什么：图论任务中的理解、推理与生成。核心思想：把图结构解析、算法性推理和图生成任务组织成可扩展 benchmark framework，补足通用推理中对结构化对象的覆盖。
- [VisuLogic](https://arxiv.org/abs/2504.15279)（[开源代码](https://github.com/VisuLogic-Benchmark/VisuLogic-Eval)）：评什么：视觉逻辑与规则推断；核心思想：把逻辑推理与视觉结构紧耦合，强调可诊断的逻辑错误类型划分。
- [SeePhys](https://arxiv.org/abs/2505.19099)：评什么：基于图像的物理推理；核心思想：让视觉元素成为解题必需信息，用跨教育阶段和物理子领域的问题暴露“只靠题干文字走捷径”的模型缺陷。
- [REASONING GYM / Reasoning Gym Eval](https://arxiv.org/abs/2505.24760)：评什么：带可验证奖励的程序化推理环境；核心思想：用可生成、可判分的任务族覆盖逻辑、算法、符号与组合推理，适合作为强化学习和 test-time search 的通用 harness。
- [ZebraLogic](https://proceedings.mlr.press/v267/lin25i.html)（[榜单](https://huggingface.co/spaces/WildEval/ZebraLogic)，[数据集](https://huggingface.co/datasets/allenai/ZebraLogicBench)）：评什么：可控复杂度的逻辑格谜题与 CSP 式演绎推理。核心思想：通过控制变量数、约束数和冲突结构观察模型推理随搜索空间增大时的崩塌点。
- [TurnBench-MS](https://arxiv.org/abs/2506.01341)：评什么：多轮、多步推理中的状态维护与约束更新；核心思想：把推理过程拆进连续交互回合，检验模型是否能在前后轮信息变化下保持一致决策。
- [Decrypto Benchmark](https://arxiv.org/abs/2506.20664)：评什么：合作与竞争通信游戏中的多 agent 推理和 theory of mind。核心思想：用交互式游戏平台测试模型如何推断其他 agent 的信念、线索和意图。
- [ENIGMATA-Eval](https://papers.neurips.cc/paper_files/paper/2025/hash/058460c719f190500568b341bd06875f-Abstract-Conference.html)（[项目页](https://seed-enigmata.github.io/)）：评什么：可生成、可验证的逻辑谜题推理。核心思想：用 36 类 puzzle family 同时服务 RLVR 训练和独立评测，强调问题可程序生成、答案可验证和难度可控。
- [LTD-Bench](https://arxiv.org/abs/2511.02347)（[开源代码](https://github.com/walktaster/LTD-Bench)，[数据集](https://huggingface.co/datasets/walktaster/LTD_Bench)）：评什么：让模型“画出来”的语言与空间概念推理。核心思想：要求模型用点阵或可执行代码绘图，把抽象语言理解、几何关系和视觉输出对齐放到同一个可判定任务里。
- [ARCHE](https://arxiv.org/abs/2511.12485)：评什么：从科学论证中抽取潜在推理链。核心思想：要求模型把演绎、归纳和溯因步骤组织成 reasoning logic tree，并同时评估实体覆盖与逐步逻辑有效性。
- [Omanic](https://arxiv.org/abs/2603.16654)：评什么：带子问题分解与中间答案标注的开放域多跳推理。核心思想：把逐步标注作为诊断单位，使推理失败能在最终答案评分前被定位。
- [ARC-AGI-3](https://arxiv.org/abs/2603.24621)（[官方页](https://arcprize.org/arc-agi/3/)；[开发者工具](https://github.com/arcprize/ARC-AGI-3-Agents)）：评什么：交互式程序归纳与小游戏式任务求解；核心思想：把 ARC 从静态 grid completion 推向可行动环境，要求 agent 通过观察、试探、状态记忆和策略搜索学习新规则。
- [DeonticBench](https://arxiv.org/abs/2604.04443)：评什么：在显式规则下围绕义务、许可和禁止进行推理。核心思想：在法律与政策式场景中测试长上下文规则推理，并可选择把规则翻译成可执行 Prolog 轨迹。

## 1.9.3 Agent Harness

- [ReAct](https://arxiv.org/abs/2210.03629)（[开源代码](https://github.com/ysymyth/ReAct)）把 reasoning trace 与工具/环境 action 交替编排，是通用推理 agent 的早期强基线。
- [Reflexion](https://arxiv.org/abs/2303.11366)（[开源代码](https://github.com/noahshinn/reflexion)）把失败轨迹转成语言反馈和 episodic memory，再用于下一轮尝试。
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（[开源代码](https://github.com/princeton-nlp/tree-of-thought-llm)）是“把推理过程树化”的代表性搜索式 test-time harness。
- [Adaptive Graph of Thoughts](https://arxiv.org/abs/2502.05078)：统一 chain、tree 和 graph 结构的测试时自适应推理 harness。核心思想：在推理过程中选择并改写推理拓扑，而不是固定使用某一种 CoT、ToT 或 GoT 模式。
- [Plan and Budget](https://arxiv.org/abs/2505.16122)：面向 LLM 推理的测试时扩展框架。核心思路是在求解前或求解过程中规划推理预算，把推理计算投入到更可能从额外思考中受益的问题上。
- ARC-AGI-solution（[开源代码](https://github.com/aviad12g/ARC-AGI-solution)；无独立论文）：LLM 引导 DSL 搜索的工程化 ARC 求解代理。
- [RAP](https://arxiv.org/abs/2305.14992)（[开源代码](https://github.com/Ber666/RAP)）更强调推理作为规划问题。
- [Graph of Thoughts](https://arxiv.org/abs/2308.09687)（[开源代码](https://github.com/spcl/graph-of-thoughts)）把 ToT 的树结构推广为图式中间状态，支持合并、聚合与更复杂的推理拓扑。
- [LATS](https://arxiv.org/abs/2310.04406)（[开源代码](https://github.com/lapisrocks/LanguageAgentTreeSearch)）把规划、评估与搜索更系统地接入 agent loop。
- [PlanGEN](https://arxiv.org/abs/2502.16111)：面向复杂规划与推理的多 agent inference-time harness；设计关键词：constraint agent、verification agent、selection agent、自适应选择 BoN/ToT/REBASE。
- [AB-MCTS for ARC-AGI-2](https://arxiv.org/abs/2503.04412)（[开源代码](https://github.com/SakanaAI/ab-mcts-arc2)）：把 ARC-AGI-2 显式建模为程序空间的树搜索问题；设计关键词：MCTS、程序空间搜索、多模型裁决。
- [VerifiAgent](https://arxiv.org/abs/2504.00406)（[开源代码](https://github.com/Jiuzhouh/VerifiAgent)）：统一验证 agent，把 meta-verification 与工具自适应验证接入推理；设计关键词：数学/逻辑/常识工具选择、反馈修订、inference scaling。
- [VSA for ARC-AGI](https://arxiv.org/abs/2511.08747)（[开源代码](https://github.com/ijoffe/ARC-VSA-2025)）：把 ARC-AGI 做成更显式的神经-符号程序归纳问题；设计关键词：神经-符号、可验证执行。
- [Reaching Agreement Among Reasoning LLM Agents](https://arxiv.org/abs/2512.20184)：面向推理 agent 的一致性感知编排协议；设计关键词包括增量 quorum 检测、提前终止、安全与活性保证，以及减少拖尾延迟。
- [Executable World Models for ARC-AGI-3](https://arxiv.org/abs/2605.05138)（[开源代码](https://github.com/alexisfox7/RGB-Agent)）：面向 ARC-AGI-3 榜单的 Read-Grep-Bash agent；设计关键词：可执行世界模型、文件化环境观察、shell 工具调用、以代码和日志维护任务状态。

## 1.9.4 Skill

- [skill-with-prompt-engineering](https://github.com/openclaw/skills/tree/main/skills/golofu/skill-with-prompt-engineering) 内含 `CoT / ReAct / self-consistency / multi-path reasoning` 等可直接复用的推理套路。
- [sympy](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/scientific/sympy) 适合把中间推理转成可执行程序或符号表达式。
- [long-context](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/ai-research/emerging-techniques-long-context) 适合维护搜索树摘要、失败分支与状态压缩。
