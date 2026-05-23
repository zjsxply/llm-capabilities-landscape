# 1.10 长上下文

> 上级章节：1. 基础能力

## 1.10.1 Leaderboard

- [LongBench Leaderboard](https://longbench2.github.io/)（[开源代码](https://github.com/THUDM/LongBench)）：从 LongBench 到 LongBench v2 的公开榜，覆盖多文档问答、长程推理、摘要与 RAG/no-context/CoT 等可控设置，是文本长上下文最常用的持续对照入口之一。
- [HELMET Leaderboard](https://princeton-nlp.github.io/HELMET/)（[开源代码](https://github.com/princeton-nlp/HELMET)）：按检索、RAG、重排序、推理、学习等维度组织长上下文榜单，适合避免只用 needle 类任务代表长上下文能力。
- [MileBench Leaderboard](https://milebench.github.io/)（[开源代码](https://github.com/milebench/MileBench)）：多模态长上下文榜，适合追踪视频、图像序列和跨模态长输入下的模型差异。
- [AcademicEval](https://github.com/ulab-uiuc/AcademicEval)：面向 live long-context generation 的榜单与评测脚本，使用新 arXiv 论文构造任务，适合评估模型在长论文语境下生成标题、摘要和相关工作的能力。

## 1.10.2 Survey

- [Beyond the Limits: A Survey of Techniques to Extend the Context Length in Large Language Models](https://arxiv.org/abs/2402.02244)：为 RoPE、插值、递归与检索路线提供基础综述。
- [A Survey on Large Language Model Acceleration based on KV Cache Management](https://arxiv.org/abs/2412.19442)：回顾高效长上下文推理的内存与服务化权衡。
- [A Survey on Transformer Context Extension: Approaches and Evaluation](https://arxiv.org/abs/2503.13299)：区分架构层面的上下文扩展与下游任务成功。
- [A Comprehensive Survey on Long Context Language Modeling](https://arxiv.org/abs/2503.17407)：综述长上下文方法、基准、评测陷阱与系统约束。
- [A Survey of Context Engineering for Large Language Models](https://arxiv.org/abs/2507.13334)：综述上下文构造、检索、记忆、工具轨迹与提示状态管理。

## 1.10.3 Bench

说明：这类 benchmark 往往不需要“专门命名的 solver agent”，更常见的形态是 `benchmark 自带 harness（切片、RAG 开关、无上下文对照）+ 可插拔上下文压缩/检索组件`。跨会话、跨任务的长期记忆已单列到 [1.15 记忆](01-15-memory.zh.md)，本节只保留与单次长输入或上下文增长过程直接相关的项目。

- [DUDE](https://arxiv.org/abs/2305.08455)：评测图文长上下文对文档理解的影响；核心思想是把图文混合长输入作为主要负载并强调 evidence 对齐。
- [L-Eval](https://arxiv.org/abs/2307.11088)（[开源代码](https://github.com/OpenLMLab/LEval)）：评什么：长上下文问答、摘要和闭卷/开卷任务；核心思想：建立标准化长上下文评测协议，早期区分上下文长度、任务类型和输入依赖。
- [LongBench](https://arxiv.org/abs/2308.14508)：评测长上下文下的任务完成质量（多任务集合）；核心思想是用统一数据与脚本对比 `长输入 vs 截断/无上下文`，暴露长程依赖失败模式。（[开源代码](https://github.com/THUDM/LongBench)）
- [BAMBOO](https://arxiv.org/abs/2309.13345)（[开源代码](https://github.com/RUCAIBox/BAMBOO)）：评什么：长文本建模能力，包括跨段推理、摘要和信息定位；核心思想：用多任务集合诊断 LLM 在长文本结构理解上的短板。
- [Needle In A Haystack](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)：评什么：长上下文单 needle 检索；核心思想：把目标片段埋入不同深度和长度的位置，快速暴露“声明窗口”和“可用窗口”的差距。
- [LV-Eval](https://arxiv.org/abs/2402.05136)（[开源代码](https://github.com/infinigence/LVEval)）：评什么：不同长度区间（最高到 256K）下的长上下文表现；核心思想：用长度分层（length levels）做更平衡的对照，避免只在单一长度点比较。
- [InfinityBench（∞Bench）](https://arxiv.org/abs/2402.13718)（[开源代码](https://github.com/OpenBMB/InfiniteBench)）：评什么：超过 100K tokens 的超长上下文任务能力；核心思想：把评测长度上限推到更大区间，显式暴露长输入下的退化曲线与截断策略影响。
- [Counting-Stars](https://arxiv.org/abs/2403.11802)（[开源代码](https://github.com/nick7nlp/Counting-Stars)）：评什么：长上下文中的多证据检索与推理。核心思想：同时改变证据位置和数量，要求模型汇集分散线索，而不是只完成单 needle 查找。
- [NovelQA](https://arxiv.org/abs/2403.12766)（[项目页](https://novelqa.github.io/)，[数据集](https://huggingface.co/datasets/NovelQA/NovelQA)）：评什么：超过 200K token 的长篇小说问答。核心思想：要求模型理解跨整本作品分散出现的人物、事件和细节证据，而不是只做孤立 needle 检索。
- [RULER](https://arxiv.org/abs/2404.06654)（[开源代码](https://github.com/hsiehjackson/RULER)）：评什么：长上下文模型的“真实可用上下文长度”；核心思想：用多种 needle/依赖形式系统诊断“宣称窗口大小”和“可用窗口大小”的差距。
- [MileBench](https://arxiv.org/abs/2404.18532)（[开源代码](https://github.com/milebench/MileBench)）：评什么：多模态长上下文模型在长视频、长图文序列和跨模态检索/推理上的表现；核心思想：把长上下文压力从纯文本扩展到多模态输入，并提供公开 leaderboard 方便对齐。
- [MRCR](https://huggingface.co/datasets/openai/mrcr)：评什么：长上下文中的多 needle 共指检索与定位；核心思想：在长对话中埋入 `2 / 4 / 8 needles` 的同分布请求，要求模型返回指定次序的目标片段，以测试真正的长程区分与索引能力。
- [GraphWalks](https://huggingface.co/datasets/openai/graphwalks)：评什么：长上下文中的图遍历式多跳推理；核心思想：把 BFS 与 parents 等图操作写成长 prompt 中的结构化任务，检验模型能否在长输入里维持结构状态并正确执行多步推理。
- [MMLongBench-Doc](https://arxiv.org/abs/2407.01523)：评测长文档多模态理解；核心思想是用文档型多模态输入检验跨页/跨段对齐与摘要压缩能力。
- [FRAMES](https://arxiv.org/abs/2409.12941)（数据集：[google/frames-benchmark](https://huggingface.co/datasets/google/frames-benchmark)）：评什么：检索增强与长文档环境中的事实性、检索与多跳推理；核心思想：用需要跨多篇文档整合证据的问题，联合测量 `factuality + retrieval + reasoning`。
- [HELMET](https://arxiv.org/abs/2410.02694)（[开源代码](https://github.com/princeton-nlp/HELMET)）：评什么：多维长上下文评测集合；核心思想：用检索、RAG、重排序、推理与学习等维度组合，避免只用 needle 类任务代表长上下文能力。
- [LongBench v2](https://arxiv.org/abs/2412.15204)：评测更新后的长上下文任务族与更强对照协议；核心思想是把 `--rag N / --no_context / --cot` 等开关显式化，强化 benchmark-side harness 的可控变量。（[开源代码](https://github.com/THUDM/LongBench)）
- [LongDocURL](https://arxiv.org/abs/2412.18424)：评测长文档 + URL/引用链的信息定位与引用一致性；核心思想是把外部引用（URL）与长文档证据对齐作为评分核心。
- [NoLiMa](https://arxiv.org/abs/2502.05167)：评什么：超越字面匹配的长上下文理解；核心思想：通过改写、间接指代和非字面线索降低 needle-style 检索捷径，更强调真正的语义定位与推理。
- [ETHIC](https://aclanthology.org/2025.naacl-long.283/)（[开源代码](https://github.com/dmis-lab/ETHIC)）：评什么：高信息覆盖率的长上下文任务。核心思想：迫使模型使用长输入中的许多相关证据，减少“只检索一个片段即可答题”的评测偏差。
- [MMLongBench](https://arxiv.org/abs/2505.10610)：评测多模态长上下文任务族；核心思想是把 `长视觉/长文本` 混合输入的鲁棒性做成可复现实验。
- [ToolHaystack](https://arxiv.org/abs/2505.23662)：评什么：工具增强模型在长期交互中的信息保持与调用决策；核心思想：把 haystack 压力测试扩展到真实多轮工具使用场景，观察历史证据、工具结果和当前目标之间的对齐。
- [LongBioBench](https://arxiv.org/abs/2506.02921)（[开源代码](https://github.com/Thomasyyj/LongBio-Benchmark)，[数据集](https://huggingface.co/datasets/thomasyyj/LongBioBench_Sample)）：评什么：人物传记叙事上的可控长上下文理解。核心思想：构造目标事实与上下文有语义关联的长上下文考试，让难度和证据位置比纯合成 needle 任务更可控。
- [PRELUDE](https://arxiv.org/abs/2508.09848)：评什么：需要全局理解和跨段推理的长上下文任务；核心思想：让问题依赖文档整体结构与远距离证据组合，减少局部片段检索即可答题的评测偏差。
- [LongLeader](https://arxiv.org/abs/2509.23161)：评什么：长上下文综合 leaderboard 与评测框架。核心思想：统一不同任务、长度区间和指标的排名口径，避免单一 LongBench/needle 任务过度代表长上下文能力。
- [LiteraryQA](https://arxiv.org/abs/2510.13494)：评测清洗后文学作品上的长文档叙事问答；核心思想是修正 NarrativeQA 式样本噪声并重新审视自动指标，使长上下文叙事理解建立在更可靠的证据上。
- [AcademicEval](https://arxiv.org/abs/2510.17725)（[开源代码](https://github.com/ulab-uiuc/AcademicEval)；[数据集](https://huggingface.co/datasets/ulab-ai/AcademicEval)）：评什么：基于 arXiv 新论文的长上下文生成任务；核心思想：把题源持续连接到新论文，自动构造 Title、Abstract、Introduction 和 Related Work 等任务，降低标签泄漏并覆盖层级抽象能力。
- [LooGLE v2](https://arxiv.org/abs/2510.22548)（[开源代码](https://github.com/MuLabPKU/LooGLE-v2)，[数据集](https://huggingface.co/datasets/MuLabPKU/LooGLE-v2)）：评什么：16K 到 2M token 的真实长文本理解。核心思想：用法律、金融、游戏和代码等长文档任务测试远距离依赖和全局理解，避免只用 needle 检索代表长上下文能力。
- [SYNC](https://doi.org/10.18653/v1/2025.emnlp-main.1707)：用合成、可控任务评测长上下文理解能力。核心思想：隔离上下文长度和推理变量，减少真实文档内容和任务构造差异对模型比较的干扰。
- [CL-Bench](https://arxiv.org/abs/2602.03587)：评测长上下文学习/记忆组织能力；核心思想是用更系统的 context learning 任务族把“记住什么、何时用、如何引用”变成可比较维度。
- [LOCA-bench](https://arxiv.org/abs/2602.07962)（[开源代码](https://github.com/hkust-nlp/LOCA-bench)）：评什么：在“上下文持续增长”条件下语言代理的稳健性；核心思想：把长上下文从“单次喂入”改成“可控增长过程”，专门检验记忆/压缩/检索策略的失效边界。
- [YC-Bench](https://arxiv.org/abs/2604.01212)：评什么：长期规划与一致执行；核心思想：让 agent 在持续经营类任务中反复使用历史目标、资源状态和中间决策，观察 context truncation、scratchpad 与 memory 策略的真实收益。

## 1.10.4 Agent Harness

注：公开生态里“只为某个长上下文 benchmark 命名”的 solver agent 并不多；更常见的是可复用的长程代理习惯（分段加载、状态摘要、失败分支记录）和可插拔的压缩/检索组件。

- [LLMLingua](https://arxiv.org/abs/2310.05736)（[开源代码](https://github.com/microsoft/LLMLingua)）：可插拔上下文压缩组件，常用于长上下文代理中降低无关 token 干扰并提升有效信息密度。
- [LongLLMLingua](https://arxiv.org/abs/2310.06839)（[开源代码](https://github.com/microsoft/LLMLingua)）：面向更长输入的压缩与重排策略，强调在高压缩率下保留关键推理证据。
- [RAPTOR](https://arxiv.org/abs/2401.18059)（[开源代码](https://github.com/parthsarthi03/raptor)）：用递归摘要树组织文档记忆，让代理在不同粒度的上下文块之间检索和聚合证据。
- [LongAgent](https://arxiv.org/abs/2402.11550)（[评测代码/数据](https://github.com/zuucan/needleinahaystack-plus)）：多 agent 协作式长上下文 harness；核心思想是把超长文本分配给多个 member agent，再由 leader agent 聚合局部证据，适合替代单次全量塞入 prompt 的处理方式。
- [HippoRAG](https://arxiv.org/abs/2405.14831)（[开源代码](https://github.com/OSU-NLP-Group/HippoRAG)）：把知识图谱式关联和海马体启发的检索机制接入 RAG，适合长程事实联想与多跳证据组织。
- [Chain-of-Agents](https://arxiv.org/abs/2406.02818)（[非官方实现](https://github.com/rudrankriyam/Chain-of-Agents)）：把长输入拆成 worker agent 串行处理并逐段传递中间消息，最后由 manager agent 汇总答案，适合长文档问答和摘要类任务。
- [Graph of Agents](https://arxiv.org/abs/2509.06644)（[开源代码](https://github.com/tjoo512/graph-of-agents)）：面向长上下文的图式多 agent 协作 harness；核心思想是把文本块、局部 agent 输出与汇总节点组织成可扩展图结构，用局部处理和跨节点聚合替代单一长 prompt。

## 1.10.5 Skill

- [long-context](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/ai-research/emerging-techniques-long-context) 直接面向长上下文压缩、摘要与检索组织。
- [long-context](https://skills.sh/davila7/claude-code-templates/long-context) 适合长上下文下的摘要、压缩与检索组织。
- [context-compression](https://skills.sh/sickn33/antigravity-awesome-skills/context-compression) 适合高 token 压力场景下的上下文裁剪。
- [token-saver-context-compression](https://skills.sh/oimiragieo/agent-studio/token-saver-context-compression) 适合以预算约束为目标的上下文压缩。
- [ai-rag-pipeline](https://skills.sh/inferen-sh/skills/ai-rag-pipeline) 适合把长文档任务改造成检索增强流程。
- [langchain-rag](https://skills.sh/langchain-ai/langchain-skills/langchain-rag) 适合把长文档任务改造成可维护的检索增强链路。
- [agent-context-loader](https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/agent-context-loader) 适合分批加载仓库或文档上下文。
- [gemini](https://skills.sh/zpankz/mcp-skillset/gemini) 属于“长窗口委派/外接执行”类 skill：把长上下文任务委派给大窗口模型，偏 harness 层的执行外接策略。
