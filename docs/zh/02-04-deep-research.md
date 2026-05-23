# 2.4 深度研究

> 上级章节：2. 基础 Agent

## 2.4.1 Leaderboard

- [Deep Research Bench Leaderboard](https://drb.futuresearch.ai/)：FutureSearch 官方持续榜单，同时覆盖 DRB 与 BTF-2；适合跟踪网页研究 agent 在可复现冻结语料和长轨迹审计下的端到端研究能力。
- [DeepResearch Bench Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)：DeepResearch Bench 官方 Hugging Face 榜单；适合按 `RACE` 报告质量与 `FACT` 引用可信度比较 deep research agent。
- [LiveResearchBench Leaderboard](https://livedeepresearch.github.io/)：LiveResearchBench 项目页含实时 deep research 榜单；适合观察动态网页、用户中心任务和引用关联评测下的 agent 差异。
- [Deep Research Arena](https://www.deepresearcharena.com/)：公开 deep research 对战与榜单站点；适合补充追踪产品化 deep research 系统、开源 harness 和商业 agent 的持续表现。
- [Deep Research SOTA on BrowseComp-ZH](https://www.wizwand.com/sota/deep-research-on-browsecomp-zh-score)：第三方 SOTA 聚合页；适合沿 BrowseComp-ZH 追踪 WebThinker、BrowseMaster、InfoSeeker、ReSum 等 deep-search / deep-research agent 的公开结果。

## 2.4.2 Survey

- [A Comprehensive Survey of Deep Research: Systems, Methodologies, and Applications](https://arxiv.org/abs/2506.12594)：围绕任务分解、搜索、证据管理、综合与评测组织 deep research。
- [Deep Research Agents: A Systematic Examination And Roadmap](https://arxiv.org/abs/2506.18096)：界定能力边界、系统、基准与可复现性问题。
- [A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges](https://arxiv.org/abs/2508.05668)：覆盖研究 agent 中检索密集的搜索与证据阶段。
- [Deep Research: A Survey of Autonomous Research Agents](https://arxiv.org/abs/2508.12752)：比较自动搜索、阅读、综合、引用并撰写报告的自主系统。
- [Reinforcement Learning Foundations for Deep Research Systems: A Survey](https://arxiv.org/abs/2509.06733)：连接长程搜索、报告质量、监督与奖励设计。

## 2.4.3 Bench

- [ResearchArena](https://arxiv.org/abs/2406.10291)：评测学术调研与综述生成；核心思想是把“检索文献 -> 对比方法 -> 写出结构化 survey”做成可评分的研究型 benchmark。
- [ResearchRubrics](https://arxiv.org/abs/2412.02077)（[开源代码](https://github.com/scaleapi/researchrubrics)）：评测研究型长文产出质量；核心思想是用 rubric 将“覆盖、证据、引用、可复核性、结构与写作质量”等维度显式化并可比。
- [BrowseComp-ZH](https://arxiv.org/abs/2504.19314)（[开源代码](https://github.com/PALIN2018/BrowseComp-ZH)；[Leaderboard](https://huggingface.co/spaces/PALIN2018/BrowseComp-ZH)；[Deep Research SOTA on BrowseComp-ZH](https://www.wizwand.com/sota/deep-research-on-browsecomp-zh-score)）：评测中文互联网环境中的高难网页浏览与多跳检索推理；核心思想是把中文网页生态中的平台碎片化、跨页检索与信息整合难点显式 benchmark 化，常被 deep-search/deep-research agent 用作 SOTA 对照。
- [Deep Research Bench](https://arxiv.org/abs/2506.06287)（[Leaderboard](https://drb.futuresearch.ai/)）：评测可复现网页研究 agent；核心思想是用 89 个多步骤网页研究任务和 frozen `RetroSearch` 网页语料，避免 live web 漂移，同时审计长轨迹中的工具使用、遗忘与幻觉。
- [DeepResearch Bench](https://arxiv.org/abs/2506.11763)（[主页](https://deepresearch-bench.github.io/)；[开源代码](https://github.com/Ayanami0730/deep_research_bench)）：评测 deep research agent 在 22 个领域上的长链路检索、证据组织与报告生成能力；核心思想是联合 `RACE` 与 `FACT` 两套协议，分别衡量报告质量与引用可信度。
- [Characterizing Deep Research](https://arxiv.org/abs/2508.04183)：评测 deep research 的宽域概念探索能力；核心思想是在形式化定义里把 deep research 和普通长文问答区分开，强调高 fan-out、跨概念检索与推理密集的信息探索。
- [BrowseComp-VL](https://arxiv.org/abs/2508.05748)：多模态 deep research 的补充评测子基准；核心思想是把视觉网页证据纳入 deep research 轨迹合成与评测。
- [BrowseComp-Plus](https://arxiv.org/abs/2508.06600)（[开源代码](https://github.com/texttron/BrowseComp-Plus)）：评测固定语料库上的 deep research agent；核心思想是从 BrowseComp 派生出可控文档集合、人工核验支持文档和 hard negatives，让研究者能分离检索质量、引用准确性与 agent 上下文工程。
- [ReportBench](https://arxiv.org/abs/2508.15804)（[开源代码](https://github.com/ByteDance-BandAI/ReportBench)）：评测 deep research agent 生成学术综述报告的质量；核心思想是从专家综述反推任务，并分别检查引用文献相关性、引用支撑关系和非引用事实正确性。
- [DeepScholar-Bench](https://arxiv.org/abs/2508.20033)（[开源代码](https://github.com/guestrin-lab/deepscholar)）：评测生成式学术研究综合；核心思想是从近期高质量 arXiv 论文抽取任务，让系统检索、综合并引用相关工作，自动衡量知识综合、检索质量与可验证性。
- [DeepTRACE](https://arxiv.org/abs/2509.04499)：评测 deep research 与生成式搜索系统的证据追踪可靠性；核心思想是把答案、来源和引用拆成 statement-level 支撑矩阵，审计结论是否真的被引用证据支持。
- [DRBench](https://arxiv.org/abs/2510.00172)（[开源代码](https://github.com/ServiceNow/drbench)，[数据集](https://huggingface.co/datasets/ServiceNow/drbench)）：评测企业 deep research。核心思想：要求 agent 跨公开网页、私有文件、邮件、聊天和生产力工具检索证据并生成带引用报告，明确区别于已有的 Dr. Bench。
- [Dr. Bench](https://arxiv.org/abs/2510.02190)：评测 deep research agent 从短答案到完整报告的多维表现；核心思想是同时覆盖任务分解、跨源检索、多阶段推理、信息整合和结构化输出，避免只按最终答案评分。
- [LiveResearchBench](https://arxiv.org/abs/2510.14240)（[主页](https://livedeepresearch.github.io/)；[开源代码](https://github.com/SalesforceAIResearch/LiveResearchBench)）：评测面向真实动态网页环境的用户中心 deep research；核心思想是以 live、user-centric、multi-faceted 任务和 `DeepEval` 多协议评测，显式考察实时检索、综合分析与引用关联质量。
- [Deep Research Arena](https://www.deepresearcharena.com/)：评什么：公开 deep research 对战与榜单式比较。核心思想：把产品化 deep research 系统、开源 harness 和商业 agent 放在持续 arena 入口中比较，补充论文 benchmark 对真实部署系统覆盖不足的问题。
- [DeepWideSearch](https://arxiv.org/abs/2510.20168)：评测 agentic information seeking 中“深度多跳推理”和“宽域信息收集”的同时满足能力；核心思想是要求 agent 在大量候选信息里完成多跳检索路径推理，暴露反思不足、检索不足和上下文溢出等失败模式。
- [DEER](https://arxiv.org/abs/2512.17776)：评测 deep research agent 的专家级报告生成；核心思想是用专家报告任务同时考察报告质量、领域专业性和 report-wide claim verification，减少只看文风或局部引用的偏差。
- [DeepSynth-Eval](https://arxiv.org/abs/2601.03540)：评测 deep survey writing 中的检索后信息整合。核心思想：提供 oracle context 和 checklist 式客观评分，把 synthesis 质量与 retrieval 质量拆开看。
- [Over-Searching](https://arxiv.org/abs/2601.05503)：评测 search-augmented agent 的另一类失败：过度搜索。核心思想：用搜索效率指标衡量不必要检索、噪声证据吸收，以及成本与质量之间的折中。
- [IDRBench](https://arxiv.org/abs/2601.06676)：评测交互式 deep research 代理；核心思想是把研究过程展开为多轮检索、计划更新与证据整合，强调过程质量而不是只看最终成稿。
- [Video Deep Research Benchmark](https://arxiv.org/abs/2601.06943)：评什么：开放网页上的视频深度研究。核心思想：让 agent 同时观看、检索和推理视频证据，评估长视频理解、网页搜索和跨模态证据整合的闭环能力。
- [DeepResearch Bench II](https://arxiv.org/abs/2601.08536)（[开源代码](https://github.com/imlrz/DeepResearch-Bench-II)）：评什么：深研报告的 rubric 诊断。核心思想：把专家报告拆成可核验条目，直接看信息找回、分析和呈现。
- [DeepResearchEval](https://arxiv.org/abs/2601.09688)：评测 deep research 的自动任务构造与 agentic evaluation。核心思想：生成 persona-driven 任务，并在报告缺少可靠引用时主动 fact-check。
- [DR-Arena](https://arxiv.org/abs/2601.10504)：用动态 trend-grounded 任务评测 deep research agent。核心思想：从近期主题构建信息树并自适应提高任务难度，需要与已有 Deep Research Arena 对战网站区分开。
- [MMDeepResearch-Bench](https://arxiv.org/abs/2601.12346)：评测多模态 deep research agent。核心思想：把图文证据收集、长报告综合、引用对齐和视觉证据完整性检查放进同一 benchmark。
- [TaxoBench](https://arxiv.org/abs/2601.12369)：评测 deep research agent 能否检索并组织一个领域。核心思想：把检索到的论文和 taxonomy tree 与专家 taxonomy 对比，而不只评报告文风。
- [Mr Dre](https://arxiv.org/abs/2601.13217)：评测 deep research agent 的多轮报告修订。核心思想：看 agent 能否吸收用户反馈，同时保留引用支撑并避免已正确部分退化。
- [DeepSearchQA](https://arxiv.org/abs/2601.20975)：评测 deep research agent 的高难多步信息搜索。核心思想：用跨领域、要求穷尽答案的任务检查 agent 是否搜得足够广、能否管理长证据链，以及是否会在只找到部分答案后过早停止。
- [ScholarGym](https://arxiv.org/abs/2601.21654)：评什么：deep research 信息收集阶段。核心思想：把“先找资料、再研究”的前半段单独 benchmark 化，直接测 agent 能否定位、筛选和组织高价值来源。
- [Deep Research Hallucination Evaluation](https://arxiv.org/abs/2601.22984)：评什么：完整深研轨迹中的幻觉。核心思想：不只查最终报告事实错误，还沿搜索、阅读、笔记和引用链审计幻觉如何在过程中产生并传播。
- [Wiki Live Challenge](https://arxiv.org/abs/2602.01590)：评什么：专家级 Wikipedia 条目写作式 deep research。核心思想：用动态百科条目需求逼迫 agent 做广泛检索、证据归纳和可引用写作，减少静态问答泄漏。
- [Vision-DeepResearch Benchmark](https://arxiv.org/abs/2602.02185)（[开源代码](https://github.com/Osilly/Vision-DeepResearch)）：评什么：视觉与文本混合搜索的深研能力。核心思想：把视觉网页证据、图片检索和文本证据放进同一 deep research 任务，诊断多模态搜索是否真正提升报告质量。
- [When Is Enough Not Enough?](https://arxiv.org/abs/2602.07549)：评什么：搜索 agent 的过早停止与虚假完成感。核心思想：构造“看似已经找到答案但仍缺关键证据”的任务，评估 agent 何时继续检索、何时停止。
- [DRACO](https://arxiv.org/abs/2602.11685)：评测跨领域真实用户式研究问题上的 deep research 准确性、完整性与客观性。核心思想：用专家撰写 rubric 分别评分事实性、广度与深度、引用支撑和呈现质量。
- [DREAM](https://arxiv.org/abs/2602.18940)：用 agentic metrics 评测 deep research。核心思想：让 evaluator 本身使用工具并自适应选择指标，从而检查 temporal validity、事实正确性与任务相关证据，而不是只靠静态 rubric。
- [DEEPSYNTH](https://arxiv.org/abs/2602.21143)（[开源代码](https://github.com/agentdeepsynthesis/deepsynth-bench)）：评测跨来源深度信息综合；核心思想是用 120 个跨 7 个领域的真实耗时任务，要求 agent 收集官方数据源、形成假设、做结构化推理并给出可核验洞见。
- [TRACE](https://arxiv.org/abs/2602.21230)：评什么：deep research agent 的轨迹级综合评测。核心思想：用 trajectory-aware 指标同时看正确性、证据质量、效率和推理健壮性，避免只用最终分数造成 high-score illusion。
- [DeepConsult](https://arxiv.org/abs/2602.21658)：评测面向“咨询式问题”的长链路调研与报告生成；核心思想是把 open-ended research 约束为可评分的长文产出与过程规范。
- [Super Research](https://arxiv.org/abs/2603.00582)：评什么：超宽、超深的复杂问题研究。核心思想：把需要大规模证据收集、长期规划和异质来源综合的问题单独提出，覆盖 Deep Research 与 Wide Search 的交叉区域。
- [DeepFact](https://arxiv.org/abs/2603.05912)：评测 deep research 报告事实性。核心思想：让 benchmark 条目和审计 agent 共同演化，使 claim-level 标签保持可修订、可证据支撑，而不是一次性固定。
- [MyScholarQA](https://arxiv.org/abs/2603.16120)：用真实用户评测 personalized deep research。核心思想：检查 agent 是否能理解个体研究偏好与信息需求，而不是只优化通用任务报告质量。
- [TRQA（Total Recall QA）](https://arxiv.org/abs/2603.18516)：评测深调研系统在长证据链下的事实找回与整合能力；核心思想是通过高召回要求把“搜得全不全、引得准不准”显式化。
- [MiroEval](https://arxiv.org/abs/2603.28407)：评什么：深研系统的过程和结果。核心思想：把最终报告、事实核验和过程审计一起评。
- [Reference Hallucination Detection](https://arxiv.org/abs/2604.03173)：评测商业 LLM 与 deep research agent 中的伪造、无效和过期引用。核心思想：区分 broken link 与 invented citation，并提供大规模 URL validity 审计工具。
- [Towards Knowledgeable Deep Research](https://arxiv.org/abs/2604.07720)：评什么：知识增强 deep research 的框架与评测。核心思想：把外部知识组织、检索和报告生成放进同一协议，区分“会搜索”与“会形成知识结构”的差别。
- [PaperScope](https://arxiv.org/abs/2604.11307)：评什么：跨海量科学论文的 agentic deep research。核心思想：基于 2,000 多篇 AI 论文的知识图谱，并联合正文、表格和图像证据，评测跨多篇相关论文的检索、推理、总结与问题求解。
- [DR3-Eval](https://arxiv.org/abs/2604.14683)（[开源代码](https://github.com/NJU-LINK/DR3-Eval)）：评什么：真实、多模态、可复现的深研评测。核心思想：用用户文件、静态 sandbox 和细粒度 rubric。
- [Cited but Not Verified](https://arxiv.org/abs/2605.06635)：评测 deep research 报告中的 source attribution。核心思想：可复现解析 Markdown 引用，再在报告尺度评估链接有效性、相关性与事实支撑。
- [ViDR](https://arxiv.org/abs/2605.13034)：评什么：多模态深研报告与视觉证据对齐。核心思想：要求报告结论能回指到具体视觉来源，减少“引用了页面但视觉证据不支撑结论”的多模态幻觉。

## 2.4.4 Agent Harness

- [STORM](https://arxiv.org/abs/2402.14207)（[开源代码](https://github.com/stanford-oval/storm)；[项目页](http://storm.genie.stanford.edu)）：检索增强的长文写作 harness，通过多视角提问、构建大纲和撰写带引用报告，成为现代 deep research agent 的重要前身。
- [Co-STORM](https://arxiv.org/abs/2408.15232)（[开源代码](https://github.com/stanford-oval/storm)；[项目页](http://storm.genie.stanford.edu)）：协作式探索研究 harness，包含 agent 对话、用户 steer、动态 mind map 与带引用报告输出。
- [Agent Laboratory](https://arxiv.org/abs/2501.04227)（[开源代码](https://github.com/SamuelSchmidgall/AgentLaboratory)）：端到端科研助理工作流，从人类给定研究想法出发，覆盖文献综述、实验和报告写作。
- [DeepResearcher](https://arxiv.org/abs/2504.03160)（[开源代码](https://github.com/GAIR-NLP/DeepResearcher)；在真实网页搜索环境中用端到端强化学习训练 deep research agent，并显式包含多代理浏览、交叉验证和自反思行为）
- [WebThinker](https://arxiv.org/abs/2504.21776)（[开源代码](https://github.com/RUC-NLPIR/WebThinker)；把“推理-检索-写作”交错成同一条长链路的 `think-search-draft` 工作流）
- [WebDancer](https://arxiv.org/abs/2505.22648)（[开源代码](https://github.com/Alibaba-NLP/DeepResearch/tree/main/WebAgent/WebDancer)；训练主导但系统形态清晰的信息检索型 web agent）
- [OWL](https://arxiv.org/abs/2505.23885)（[开源代码](https://github.com/camel-ai/owl)；把 deep research 显式拆成 `检索 -> 验证 -> 写作` 的角色化流水线）
- [Deep Cognition](https://arxiv.org/abs/2507.15759)（开源代码：未找到稳定公开仓库；透明、可中断的多 agent deep research 系统；核心思想是在研究过程中暴露细粒度人类 steering 与协作点，而不是把 deep research 做成封闭输入输出流程）
- [WebWatcher](https://arxiv.org/abs/2508.05748)（[开源代码](https://github.com/Alibaba-NLP/DeepResearch/tree/main/WebAgent/WebWatcher)；面向多模态 deep research 的视觉语言代理，并提出 BrowseComp-VL）
- [WebWeaver](https://arxiv.org/abs/2509.13312)（[开源代码](https://github.com/Alibaba-NLP/DeepResearch/tree/main/WebAgent/WebWeaver)；`planner + writer` 双代理，配合动态大纲与 evidence memory bank 管理长报告上下文）
- [Flash-Searcher](https://arxiv.org/abs/2509.25301)（[开源代码](https://github.com/OPPO-PersonalAI/Flash-Searcher)；把串行 pipeline 改成 DAG 并行执行，并按依赖关系动态调度）
- [FlowSearch](https://arxiv.org/abs/2510.08521)（[开源代码](https://github.com/InternScience/InternAgent)；流程编排驱动的搜写一体）
- [BrowserAgent](https://arxiv.org/abs/2510.10666)（[开源代码](https://github.com/TIGER-AI-Lab/BrowserAgent)；把真实浏览器动作空间接入 agent，并配显式 memory 支撑网页级长期任务）
- DRBA / DRBench Baseline Agent（[开源代码](https://github.com/ServiceNow/drbench)；无独立论文；DRBench 配套企业深研 baseline agent，围绕企业私有资料、公开网页、消息和生产力工具做检索、证据组织与带引用报告生成）
- [Enterprise Deep Research](https://arxiv.org/abs/2510.17797)（[开源代码](https://github.com/SalesforceAIResearch/enterprise-deep-research)；企业研究场景的多代理深研系统实现）
- [Tongyi Deep Research](https://arxiv.org/abs/2510.24701)（[开源代码](https://github.com/Alibaba-NLP/DeepResearch)；端到端深调研代理的一体化开源实现）
- [Dingtalk DeepResearch](https://arxiv.org/abs/2510.24760)（开源代码：未公开；企业办公场景的深调研代理，强调工作流嵌入与协同办公集成）
- [IterResearch](https://arxiv.org/abs/2511.07327)（[开源代码](https://github.com/Chen-GX/IterResearch)；长程 deep research 代理；核心思想是用多轮 interaction scaling 与状态重建避免单一上下文不断膨胀导致的噪声污染和上下文窒息）
- [RhinoInsight](https://arxiv.org/abs/2511.18743)（开源代码：未公开；企业情报洞察导向研究代理）
- [Step-DeepResearch Technical Report](https://arxiv.org/abs/2512.20491)（[开源代码](https://github.com/stepfun-ai/StepDeepResearch)；open-ended deep research 的端到端训练路线与评测补齐，含 checklist 式 judge）
- [Self-Manager](https://arxiv.org/abs/2601.17879)（开源代码：未公开；把多代理 thread scheduling 自身也交给 agent 管理）
- [Yunque DeepResearch](https://arxiv.org/abs/2601.19578)（[开源代码](https://github.com/Tencent-BAC/YunqueAgent)；腾讯系端到端深调研代理）
- FutureSearch ReAct Agent（[开源代码](https://github.com/futuresearch/futuresearch-python)；无独立 arXiv 论文；FutureSearch 在 BTF-2 论文中引用的开源网页研究 agent 实现，包含工具包、时间管理和 ReAct-style 系统提示，适合复现实验型 deep research / forecasting harness）
- [FS-Researcher](https://arxiv.org/abs/2602.01566)（[开源代码](https://github.com/Ignoramus0817/FS-Researcher)；分阶段检索与成稿研究代理）
- [IntentRL](https://arxiv.org/abs/2602.03468)（开源代码：未找到稳定公开仓库；在开放式 deep research 前训练主动意图澄清行为，为昂贵的长程搜索增加用户交互 gate）
- [AgentCPM-Report](https://arxiv.org/abs/2602.06540)（[开源代码](https://github.com/OpenBMB/AgentCPM/tree/main/AgentCPM-Report)；中文长报告生成特化代理）
- [Table-as-Search](https://arxiv.org/abs/2602.06724)（开源代码：未找到稳定公开仓库；把长程信息搜索表格化；核心思想是让 agent 维护待填字段、证据单元和缺口，统一处理 deep search、wide search 与 deep-wide search）
- [W&D](https://arxiv.org/abs/2602.07359)（开源代码：未找到稳定公开仓库；Wide-and-Deep parallel tool-calling harness；核心思想是在单个 agent step 内横向并行调用搜索/阅读工具，提升 BrowseComp 式任务的来源覆盖和验证冗余）
- [DualGraph](https://arxiv.org/abs/2602.13830)（开源代码：未找到稳定公开仓库；用两个共同演化的图分离知识探索与大纲规划，减少把来源发现和报告结构决策混在一起的倾向）
- [Search More, Think Less（SMTL）](https://arxiv.org/abs/2602.22675)（[开源代码](https://github.com/OPPO-PersonalAI/SMTL)；长程 deep research/search agent；核心思想是优先扩展检索宽度和证据覆盖，再用较轻推理综合，降低超长链路成本）
- [MiroFlow](https://arxiv.org/abs/2602.22808)（[开源代码](https://github.com/MiroMindAI/MiroFlow)；流程图式多阶段研究编排）
- [Hyper-Search（MM-DeepResearch）](https://arxiv.org/abs/2603.01050)（[开源代码](https://github.com/HJYao00/MM-DeepResearch)；多模态证据整合型深研代理，链接曾不稳定）
- [SynPlanResearch-R1](https://arxiv.org/abs/2603.07853)（[开源代码](https://github.com/HansiZeng/syn-plan-research)；用合成计划训练 tool exploration；核心思想是先生成可执行研究计划，再用计划约束检索、阅读与写作轨迹）
- [MiroThinker-1.7 & H1](https://arxiv.org/abs/2603.15726)（[开源代码](https://github.com/MiroMindAI/MiroThinker)；开源深研代理；核心思想：交互 scaling + 验证式推理）
- [OpenResearcher](https://arxiv.org/abs/2603.20278)（[开源代码](https://github.com/TIGER-AI-Lab/OpenResearcher)；用 15M 文档离线语料、`search/open/find` 原语和合成长轨迹训练开放 deep research agent，强调可复现的离线搜写闭环）
- [Marco DeepResearch](https://arxiv.org/abs/2603.28376)（开源代码：未确认公开；verification-centric deep research agent；核心思想是在 QA 合成、轨迹构造和测试时扩展中加入显式验证，避免长链路搜索错误一路传播到最终报告）
- [Trustworthy Report Generation](https://arxiv.org/abs/2604.05952)（开源代码：未找到稳定公开仓库；带 progressive confidence estimation and calibration 的 deep research agent；核心思想是在报告生成过程中持续维护证据置信度，降低引用不稳与结论过度自信）
- [DataSTORM](https://arxiv.org/abs/2604.06474)（开源代码：未确认公开；面向结构化数据的 deep research agent；核心思想是结合探索性数据分析、网页证据、主题生成与 data storytelling，让 agent 不只研究非结构化网页，也能研究大规模数据库）
- [Deep-Reporter](https://arxiv.org/abs/2604.10741)（开源代码：未找到稳定公开仓库；grounded multimodal long-form generation harness；核心思想：结合多模态搜索与过滤、checklist 引导的增量综合和 recurrent context management）
- [ARIS / Auto-Research-In-Sleep](https://arxiv.org/abs/2605.03042)（[开源代码](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)；[介绍](https://wanshuiyin.github.io/Auto-claude-code-research-in-sleep/ARIS_INTRO.html)）：skill-based autonomous research harness，包含跨模型对抗审阅、持久 research wiki、文献与实验工作流、引用/主张审计，以及 Codex/OpenClaw/Claude Code 可迁移性。
- [LongSeeker](https://arxiv.org/abs/2605.05191)（开源代码：未公开；长程搜索/深研 agent；核心思想是用 Context-ReAct 动态压缩、回滚、摘录和删除工作记忆，在 BrowseComp 与 BrowseComp-ZH 上验证长链路检索收益）
- [AgentDisCo](https://arxiv.org/abs/2605.11732)（开源代码：未找到稳定公开仓库；disentangled collaborative deep-research 架构；核心思想是把 critic 驱动的大纲/查询修正与 generator 驱动的检索/大纲更新拆开，再用 meta-optimization 发现可复用的 research-agent 设计策略）
- [Argus](https://arxiv.org/abs/2605.16217)：证据拼装式深研代理；核心思想：Searcher 收集证据，Navigator 维护证据图并调度并行搜索。
- Onyx（[开源代码](https://github.com/onyx-dot-app/onyx)；无 arXiv 论文；开源企业 AI 平台，内置 Deep Research、多步搜索、RAG、MCP 与 Code Interpreter）
- LangChain Open Deep Research（[开源代码](https://github.com/langchain-ai/open_deep_research)；无 arXiv 论文；LangChain 官方开源深研系统实现）
- AI-Q NVIDIA Research Assistant（[开源代码](https://github.com/NVIDIA-AI-Blueprints/aiq)；无 arXiv 论文；固定化“计划 -> 并行检索 -> 写作 -> 反思补检 -> 人类介入”的研究 loop）
- DeerFlow（[开源代码](https://github.com/bytedance/deer-flow)；无 arXiv 论文；把 deep research 抽象为可复用 super agent harness，并强调任务分支解耦）
- Spring AI Alibaba DeepResearch（[开源代码](https://github.com/spring-ai-alibaba/deepresearch)；无 arXiv 论文；Spring 生态集成版深调研）
- CellCog（[公开 SDK](https://github.com/CellCog/cellcog_python)；无 arXiv 论文；托管式多 agent 平台与 Python SDK，支持 agent team 与 research-cog）

## 2.4.5 Skill

- [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)（端到端检索到成稿框架）
- [meta-research](https://github.com/AmberLJC/meta-research)（“文献综述 -> 假设树 -> judgment gate -> 实验 -> 反思”的科研 workflow skill）
- [deep-research](https://skills.sh/bytedance/deer-flow/deep-research)（DeerFlow 官方 deep research skill）
- [github-deep-research](https://skills.sh/bytedance/deer-flow/github-deep-research)（DeerFlow 官方仓库深调研 skill；GitHub API + 网页检索 + 结构化报告生成）
- [deep-research](https://github.com/daymade/claude-code-skills/tree/main/deep-research)（强调证据表、格式契约与多稿合并）
- [deep-research-openclaw-agent](https://clawhub.ai/milleniumgenai/deep-research-openclaw-agent)（结构化 deep-research sub-agent 的安装/接线型 skill）
- [deep-research](https://skills.sh/shubhamsaboo/awesome-llm-apps/deep-research)（流程型 deep research 模板，强调多源综合与引用追踪）
- [academic-researcher](https://skills.sh/shubhamsaboo/awesome-llm-apps/academic-researcher)（学术写作与文献评述模板，偏结构化产出）
- [tooluniverse-literature-deep-research](https://skills.sh/mims-harvard/tooluniverse/tooluniverse-literature-deep-research)（文献导向，偏生物医药）
- [literature-review](https://skills.sh/davila7/claude-code-templates/literature-review)（系统综述流程模板，覆盖去重、筛选、引用校验与产出脚本）
- [web-research](https://skills.sh/langchain-ai/deepagents/web-research)（LangChain 官方网页调研子技能）
- [websearch-deep](https://skills.sh/thomasholknielsen/claude-code-config/websearch-deep)（网页检索后直接成稿模板）
- [deep-research](https://skills.sh/199-biotechnologies/claude-deep-research-skill/deep-research)（检查点密集的分步研究模板）
- [deep-research-agent](https://skills.sh/qodex-ai/ai-agent-skills/deep-research-agent)（以流程提示与样例代码为主，实验执行与评测能力不足）
- [academic-deep-research](https://skills.sh/kesslerio/academic-deep-research-clawhub-skill/academic-deep-research)（学术文献导向的成稿模板）
- [deep-research](https://github.com/feiskyer/claude-code-settings/tree/main/skills/deep-research)（多 agent 编排型深研 skill；偏多进程调研与聚合）
- [Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills)（多技能 deep research 套件；outline/字段扩展/并行 research/最终 report）
- [deep-research](https://github.com/wshuyi/deep-research/tree/main/skills/deep-research)（中文流程型 deep research skill；强调事实分层与中间产物留存）
- [ARIS research skills](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/main/skills)（论文：[ARIS](https://arxiv.org/abs/2605.03042)；skills.sh 示例：[research-pipeline](https://skills.sh/wanshuiyin/auto-claude-code-research-in-sleep/research-pipeline)、[research-lit](https://skills.sh/wanshuiyin/auto-claude-code-research-in-sleep/research-lit)、[citation-audit](https://skills.sh/wanshuiyin/auto-claude-code-research-in-sleep/citation-audit)）覆盖文献检索、多源检索、research-wiki 记忆、新颖性检查、跨模型审阅和引用/主张审计，更接近可执行科研 harness，而不是单个报告提示词。
- [parallel-deep-research](https://skills.sh/parallel-web/parallel-agent-skills/parallel-deep-research) 适合在最终综合前并行做来源发现和材料阅读的 deep research 工作流。
- [firecrawl-deep-research](https://skills.sh/firecrawl/firecrawl-workflows/firecrawl-deep-research) 适合基于 provider crawling 与内容抽取的检索到报告工作流。
- [doublecheck](https://github.com/github/awesome-copilot/tree/main/skills/doublecheck) 适合抽取主张、搜索来源，并检查证据支持或矛盾关系，可补充 Reference Hallucination Detection 和 Cited but Not Verified 等引用可靠性评测。
- [search-layer](https://github.com/blessonism/openclaw-search-skills/tree/main/search-layer)（更偏 deep research 底层检索层：多源并行搜索、去重、排序与引用链追踪）
- [last30days-skill](https://github.com/mvanhorn/last30days-skill) 和 [last30days-skill-cn](https://github.com/Jesseovo/last30days-skill-cn) 是面向最近一个月信息发现的 skills，覆盖社交平台、新闻、社区和网页来源；当 deep research 更需要新鲜度和跨平台趋势覆盖，再进入长文综合时很有用。
- [deep-research-pro](https://clawhub.ai/parags/deep-research-pro)（商业风格长报告模板）
- [deepresearchwork](https://clawhub.ai/jiacode/deepresearchwork)（任务拆步明确的调研模板）
- [in-depth-research](https://clawhub.ai/ivangdavila/in-depth-research)（纵深追问型长报告模板）
