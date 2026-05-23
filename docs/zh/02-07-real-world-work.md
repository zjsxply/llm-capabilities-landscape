# 2.7 现实工作

> 上级章节：2. 基础 Agent


## 2.7.1 Leaderboard

- [GAIA Leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard)：通用现实助理任务的长期公开榜单，覆盖推理、网页浏览、多模态和工具使用；它仍是比较“能否完成真实问题”而非单工具能力的重要入口。
- [TheAgentCompany Leaderboard](https://the-agent-company.com/#/leaderboard)：面向模拟软件公司数字员工任务的公开榜单；适合观察现实工作中网页、代码、文件和同事通信混合任务的端到端完成率。
- [HAL / Holistic Agent Leaderboard](https://hal.cs.princeton.edu/)（[开源 harness](https://github.com/princeton-pli/hal-harness)）：跨 GAIA、AssistantBench、tau-bench、Online Mind2Web、SWE-bench Verified 等任务报告 accuracy、cost、runtime 和 traces；价值在于把模型、agent scaffold 和评测成本一起公开比较。
- [GDPval Leaderboard](https://evals.openai.com/gdpval/leaderboard)：面向经济价值任务交付物的公开榜单；重点看 rubric 驱动的专业输出质量，并把模型能力、上下文和 scaffolding 的现实工作收益放到同一入口。
- [Remote Labor Index Leaderboard](https://labs.scale.com/leaderboard/rli)：围绕真实远程劳动项目的自动化率和交付质量持续比较 agent；与 GDPval 互补，强调可外包项目、经济信号和端到端交付。
- [APEX-Agents Leaderboard](https://www.mercor.com/apex/apex-agents-leaderboard/)：覆盖投行、咨询、公司法律等专业服务任务的公开榜单；它把文件、工具、rubric 和 gold outputs 作为现实白领工作交付物评估对象。
- [ClawBench Leaderboard](https://claw-bench.com/)：真实 live website 写操作任务榜单，记录 model、harness、trace、HTTP interception 和 reward；现实网页工作流中 agent 行为是否可审计是它的主要价值。
- [ClawMark Leaderboard](https://claw-mark.com/leaderboard)：多日历时间 coworker-agent 工作流榜单，适合跟踪能跨天等待、回忆和协同的真实工作 agent，而不是只完成单次会话任务。

## 2.7.2 Bench

- [GAIA](https://arxiv.org/abs/2311.12983)（[数据集](https://huggingface.co/datasets/gaia-benchmark/GAIA)）：评什么：通用 AI assistant 在真实问题上的推理、多模态、网页浏览和工具使用。核心思想：用人类容易但模型困难的现实问题，把“会查、会算、会用工具、会整合证据”组合成早期通用 agent 评测锚点。
- [WorkArena](https://arxiv.org/abs/2403.07718)（[开源代码](https://github.com/ServiceNow/WorkArena)）：评什么：ServiceNow 企业软件中的常见知识工作网页任务。核心思想：用真实企业软件风格的平台与 BrowserGym 环境评测 agent 的网页操作、表单处理、检索与流程执行能力。
- [WorkBench](https://arxiv.org/abs/2405.00823)（[开源代码](https://github.com/olly-styles/WorkBench)）：评什么：真实办公室/业务活动中的工具调用与状态变更任务。核心思想：提供含 5 个数据库、26 个工具和 690 个任务的 sandbox，以 outcome-centric evaluation 检查最终数据库状态是否唯一正确，强调邮件、会议、记录更新等常见工作流的可执行性与误操作风险。
- [tau-bench](https://arxiv.org/abs/2406.12045)（[开源代码](https://github.com/sierra-research/tau-bench)）：评什么：真实领域中的工具-代理-用户多轮交互（如零售与航空）。核心思想：用模拟用户、领域 API 与 policy guideline 共同约束 agent，并以最终数据库状态评估是否真正完成用户目标。
- [WorkArena++](https://arxiv.org/abs/2407.05291)（[开源代码](https://github.com/ServiceNow/WorkArena)）：评什么：更组合化的企业知识工作流。核心思想：把 WorkArena 扩展到 682 个需要组合规划、逻辑/算术推理、检索与上下文理解的任务，专门放大“多步骤企业流程”中的规划失败。
- [AssistantBench](https://arxiv.org/abs/2407.15711)（[项目页](https://assistantbench.github.io/)）：评什么：真实且耗时的网页助理任务。核心思想：把监控、筛选、定位和信息整合类网页工作做成可自动评价任务，连接 GAIA 的通用助理能力与 WebArena 式可执行网页环境。
- [OfficeBench](https://arxiv.org/abs/2407.19056)（[开源代码](https://github.com/zlwang-cs/OfficeBench)）：评什么：跨 Word/Excel/PDF/日历/邮件等多应用的办公室自动化。核心思想：用 300 个多应用任务测长程规划、应用切换与大动作空间 grounding，突出日常办公工作流中的冗余操作、幻觉和跨应用失败。
- [CRMArena](https://arxiv.org/abs/2411.02305)：评什么：CRM 系统中的专业客户服务、分析与管理任务。核心思想：引入工业对象、隐变量和业务规则，检验 agent 在真实 CRM 工作环境中的函数调用、规则遵循与业务流程可靠性。
- [TheAgentCompany](https://arxiv.org/abs/2412.14161)（[开源代码](https://github.com/TheAgentCompany/TheAgentCompany)）：评什么：模拟软件公司中的真实数字员工任务。核心思想：构建自包含的公司环境、内部网站与同事通信，让 agent 通过浏览网页、写代码、运行程序和沟通协作完成工作，而不是只在单一工具里操作。
- [ML-Dev-Bench](https://arxiv.org/abs/2502.00964)：评什么：应用机器学习开发 workflow 中的 agentic 能力。核心思想：从数据处理、训练、改进现有代码到实验报告生成，评估 agent 是否能完成完整 ML 开发链路，而不是只解孤立代码题或 Kaggle 式单点任务。
- [RealWebAssist](https://arxiv.org/abs/2504.10445)（[开源代码](https://github.com/SCAI-JHU/RealWebAssist)）：评什么：真实用户的长程网页协助。核心思想：用顺序、多变、含澄清需求的人类指令评估 agent 的持续协助能力，贴近现实用户把网页任务委托给 AI 的工作流。
- [CRMArena-Pro](https://arxiv.org/abs/2505.18878)：评什么：销售、服务、报价配置等多业务场景下的 CRM agent。核心思想：在 CRMArena 基础上加入 B2B/B2C、多人设多轮交互与保密意识评估，更贴近企业部署中“会话 + 数据 + 规则 + 权限”的复合需求。
- [FieldWorkArena](https://arxiv.org/abs/2505.19662)：评什么：制造、仓储、零售等现场工作的多模态任务。核心思想：用真实场地采集的图片/视频与一线员工访谈构造任务，测安全隐患、流程违规与关键事件识别，补齐“数字办公室之外”的现实工作评测。
- [ITBench](https://github.com/itbench-hub/ITBench)：评什么：SRE、FinOps、CISO 等企业 IT 自动化任务。核心思想：提供开源的 IT automation benchmark framework，把告警排障、成本治理和安全运营这类真实后台工作纳入可执行环境与状态检查，而不只评文本建议。
- [WebChoreArena](https://arxiv.org/abs/2506.01952)（[开源代码](https://github.com/WebChoreArena/WebChoreArena)）：评什么：现实网页中的繁琐复杂 chores。核心思想：把大量筛选、重复确认、跨页面状态维护等“人类不愿做但工作中常见”的网页任务做成 benchmark，检验 agent 的稳定执行和错误恢复。
- [SpreadsheetBench Verified](https://arxiv.org/abs/2506.03768)：评什么：可验证的表格/电子表格任务（公式、计算、操作与结果一致性）。核心思想：以“可自动验证”的协议把 spreadsheet 这种常见生产工具纳入编程代理能力谱系。
- [AssetOpsBench](https://arxiv.org/abs/2506.03828)（[开源代码](https://github.com/IBM/AssetOpsBench)）：评什么：工业资产运维中的多步骤决策与操作。核心思想：把 Industry 4.0 场景中的设备状态、维护策略和操作约束组织成可执行任务，补充办公室软件之外的企业运营工作流。
- [xbench](https://arxiv.org/abs/2506.13651)：评什么：与职业生产力直接对齐的动态真实工作评测，初始覆盖招聘与营销。核心思想：由行业专家定义商业重要任务，并用可随时间更新的 evalset 追踪 agent 的 Technology-Market Fit，而不是只看静态学术题。
- [OpenAgentSafety](https://arxiv.org/abs/2507.06134)：评什么：真实工具环境中的 agent 安全。核心思想：接入浏览器、代码执行、文件系统、shell 和消息平台，覆盖多轮多用户任务中的 8 类风险，用现实工作流暴露安全对齐缺口。
- [WearVox](https://arxiv.org/abs/2507.11824)（[开源代码](https://github.com/facebookresearch/wearvox)）：评什么：可穿戴语音助手的上下文感知能力。核心思想：把语音、视觉和用户情境结合起来评估移动生活场景中的助手能力，补足桌面/网页工作流之外的现实助理形态。
- [OdysseyBench](https://arxiv.org/abs/2508.09124)（[开源代码](https://github.com/microsoft/OdysseyBench)）：评什么：长程办公生产力工作流中的 agent memory。核心思想：围绕文档、邮件、日历、表格等办公室任务构造跨阶段状态依赖，检验 agent 是否能在长链路中保留关键上下文并正确复用历史操作结果。
- [MCP-Bench](https://arxiv.org/abs/2508.20453)（[开源代码](https://github.com/Accenture/mcp-bench)）：评什么：通过 MCP servers 执行复杂真实任务的工具使用能力。核心思想：每个 MCP server 提供互补工具，任务要求跨工具规划、schema 理解、轨迹级决策与最终任务完成，贴近企业 MCP 化工具生态。
- [AgentArch](https://arxiv.org/abs/2509.10769)（[开源代码](https://github.com/ServiceNow/AgentArch)）：评什么：企业场景中不同 agent 架构的端到端效果。核心思想：把 ReAct、planner-executor、多代理、记忆和工具路由等架构选择放到统一企业任务集里比较，帮助区分模型能力与 harness 设计贡献。
- [Gaia2](https://arxiv.org/abs/2509.17158)（[开源代码](https://github.com/facebookresearch/meta-agents-research-environments)）：评什么：动态现实环境中的异步任务、通知和外部系统交互。核心思想：用会变化的环境状态和持续事件流逼近真实工作中的“等待、更新、再计划”，适合作为静态一次性 workplace benchmark 的动态补充。
- [SCUBA](https://arxiv.org/abs/2509.26506)（[开源代码](https://github.com/SalesforceAIResearch/SCUBA)）：评什么：Salesforce GUI 中的企业 computer-use 任务。核心思想：以 CRM 业务对象和真实 SaaS 界面为载体，测 agent 在记录查改、表单导航、规则遵循和状态一致性上的可靠性。
- [DRBench](https://arxiv.org/abs/2510.00172)（[开源代码](https://github.com/ServiceNow/drbench)，[数据集](https://huggingface.co/datasets/ServiceNow/drbench)）：评什么：企业 deep research 工作。核心思想：要求 agent 跨公开网页、私有文件、邮件、聊天和生产力工具检索证据并生成带引用报告，补齐现实企业场景中“信息分散且有权限边界”的研究型工作流。
- [GDPval](https://arxiv.org/abs/2510.04374)（公开 benchmark；[Leaderboard](https://evals.openai.com/gdpval/leaderboard)）：评什么：真实经济价值任务（覆盖多职业/多行业的“可交付物”型工作任务）。核心思想：用明确的交付物与 rubric 驱动的评分把“现实工作”落到可比对的评价协议上，并讨论 `reasoning effort / 上下文 / scaffolding` 对表现的影响。
- [HAL / Holistic Agent Leaderboard](https://arxiv.org/abs/2510.11977)（[开源代码](https://github.com/princeton-pli/hal-harness)）：评什么：跨 GAIA、AssistantBench、tau-bench、Online Mind2Web、SWE-bench Verified 等任务的统一 agent 评测。核心思想：把 accuracy、cost、runtime 和 traces 一起公开，作为现实工作 agent 的跨 benchmark 对照框架。
- [LaborMarketplaceBenchmark](https://openreview.net/forum?id=be76fus1ou)（NeurIPS 2025 LLM Evaluation Workshop）：评什么：来自真实自由职业市场的知识工作任务。核心思想：从固定价格、单里程碑、已被客户接受的 marketplace 任务构造可刷新评测集，并保留 payout、任务类别与人类反馈迭代等经济信号，作为 RLI 的近邻方向。
- [ProfBench](https://arxiv.org/abs/2510.18941)（数据集：[nvidia/ProfBench](https://huggingface.co/datasets/nvidia/ProfBench)，[开源代码](https://github.com/NVlabs/ProfBench)）：评什么：需要专业知识的文档处理、信息综合与报告生成/评判。核心思想：由物理、化学、金融与咨询专家提供人类 rubric，用专家级判据评估开放式专业产出，适合作为 GDPVal/RLI 的“专业 rubric”补充。
- [Tool Decathlon（Toolathlon）](https://arxiv.org/abs/2510.25726)：评什么：多应用、多工具、长程任务执行。核心思想：提供更真实的环境设置与 execution-based evaluation，考察 agent 在跨域工具链中完成长任务的稳定性，可作为 OfficeBench/MCP-Bench 的通用工具执行近邻。
- [Remote Labor Index（RLI）](https://arxiv.org/abs/2510.26787)（[开源评估平台](https://github.com/centerforaisafety/rli_evaluation_platform)；公开数据入口见仓库 README）：评什么：远程自由职业/外包式真实项目的端到端自动化。核心思想：把“能否替代远程劳动”落到有经济价值的项目交付物上，强调多行业、长工时、模糊需求与最终交付质量，而不是只测孤立技能。
- [EnterpriseBench](https://arxiv.org/abs/2510.27287)：评什么：企业环境中的软件工程、HR、财务与行政工作任务。核心思想：用数据源碎片化、访问控制层级和跨职能 workflow 构造 500 个企业任务，检验 agent 是否能在接近真实组织约束的 sandbox 中完成工作。
- [NL2Repo-Bench](https://arxiv.org/abs/2512.12730)（公开 benchmark）：评什么：从自然语言需求文档端到端构建完整软件仓库（空工作区起步，需架构设计、依赖管理、多文件实现、可安装包与测试）。核心思想：用“长时程 repo construction + tests”把 vibe coding 的跨文件一致性与长链路执行失败模式显式 benchmark 化。
- [Finch（FinWorkBench）](https://arxiv.org/abs/2512.13168)（[开源代码](https://github.com/FinWorkBench/Finch)，[数据集](https://huggingface.co/datasets/FinWorkBench/Finch)）：评什么：企业级金融和会计中的 spreadsheet-centric workflow。核心思想：从真实企业工作区、邮件线程和表格版本历史中构造长程复合任务，覆盖数据录入、建模、验证、检索、可视化和报告交付。
- [SafePro](https://arxiv.org/abs/2601.06663)（[项目页](https://safeprobench.github.io/safepro/)）：评什么：专业级 AI agent 的安全性。核心思想：在复杂专业任务中同时看任务完成与不安全动作，补足 GDPval、RLI、APEX-Agents 等现实工作评测对安全失败的覆盖不足。
- [TraineeBench](https://arxiv.org/abs/2601.08173)（[开源代码](https://github.com/KnowledgeXLab/EvoEnv)）：评什么：新员工式工作场景中的动态学习、探索与任务调度。核心思想：让 agent 在陌生 workplace 环境中持续接收流式任务、主动探索信息、总结规则并滚动调度，评估生产环境更常见的“第一天上岗”能力，而不是静态一次性任务完成。
- [AgencyBench](https://arxiv.org/abs/2601.11044)（[开源代码](https://github.com/GAIR-NLP/AgencyBench)）：评什么：来自日常 AI 使用的长程真实任务。核心思想：覆盖 32 个现实场景、138 个任务，强调 1M token、约 90 次工具调用和数小时执行时间下的交付物与 rubric 自动评估。
- [APEX-Agents](https://arxiv.org/abs/2601.14242)（[评估基础设施 Archipelago](https://github.com/Mercor-Intelligence/archipelago)）：评什么：投行、管理咨询、公司法律等专业服务中的长程跨应用任务。核心思想：在带文件与工具的现实工作环境里测 Pass@1，并把题目、rubric、gold outputs、文件与元数据开放，强调“白领专业服务”的可交付成果质量。
- [EntWorld](https://arxiv.org/abs/2601.17722)：评什么：企业 GUI agent 在 CRM、ITIL、ERP 等高密度业务系统中的长程工作流。核心思想：从数据库 schema 反推业务逻辑并合成 1,756 个任务，用 SQL 状态转移做确定性验证，强调企业系统里规则约束、信息一致性和多步骤界面操作的组合难度。
- [World of Workflows](https://arxiv.org/abs/2601.22130)：评什么：企业系统中的端到端 workflow 执行。核心思想：围绕多步骤业务流程、跨系统状态和规则约束构造任务，把“能否完成一个完整工作流”而不是单个 API/页面动作作为核心评测对象。
- [AIRS-Bench](https://arxiv.org/abs/2602.06855)（[开源代码](https://github.com/facebookresearch/airs-bench)）：评什么：AI research science 的端到端研究任务。核心思想：从前沿 ML 论文中抽取 idea generation、实验分析、代码实现、文献理解等完整研究生命周期任务，评估 agent 是否能产出可验证的研究工作结果。
- [WorldTravel](https://arxiv.org/abs/2602.08367)（公开 benchmark）：评什么：真实旅行规划（强耦合约束、多目标、多步骤计划），含 text-only 与多模态网页环境（WorldTravel-Webscape）。核心思想：用“强耦合约束 + 真实网页参数读取（视觉布局）”把规划与感知-行动闭环的脆弱性显式放大，指标以“计划可行性/约束满足”为核心。
- [EcoGym](https://arxiv.org/abs/2602.09514)：评什么：长时程经济环境中的连续计划与执行，覆盖 Vending、Freelance 和 Operation 三类场景。核心思想：用 1000+ 步、部分可观测、随机扰动和业务指标（净值、收入、DAU 等）测试 agent 是否能在经济系统中维持长期策略一致性，而不是只优化短期动作。
- [LongCLI-Bench](https://arxiv.org/abs/2602.14337)（[开源代码](https://github.com/finyorko/longcli-bench)）：评什么：命令行中的长程 agentic programming 工作流。核心思想：用 CLI 任务把真实软件工程中的规划、执行、调试和阶段性检查拉长，并通过细粒度指标记录中间失败模式。
- [LiveAgentBench](https://arxiv.org/abs/2603.02586)：评什么：来自真实用户需求的综合 agent 任务，覆盖社交媒体和真实产品问题。核心思想：用 Social Perception-Driven Data Generation 构造 104 个现实场景、374 个任务，并持续从真实交互更新，以减少静态 benchmark 与真实需求之间的偏差。
- [OneMillion-Bench](https://arxiv.org/abs/2603.07980)：评什么：高经济后果场景下的专家级职业任务，覆盖法律、金融、工业、医疗健康与自然科学。核心思想：要求检索权威来源、处理冲突证据、应用领域规则并做约束决策，用 rubric 同时评估事实正确性、逻辑一致性、实践可行性与专业合规。
- [EnterpriseOps-Gym](https://arxiv.org/abs/2603.13594)（[项目页](https://enterpriseops-gym.github.io/)；[开源代码](https://github.com/ServiceNow/EnterpriseOps-Gym)；[数据集](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym)）：评什么：企业环境中的有状态规划、工具使用与策略合规。核心思想：提供含 164 张数据库表、512 个功能工具和 1150 个专家任务的容器化企业 sandbox，覆盖客服、HR、IT、邮件、日历、Teams、Drive 与混合场景，并用 SQL 检查最终状态而非只看轨迹文本。
- [Data Agent Benchmark（DAB）](https://arxiv.org/abs/2603.20576)（[开源代码](https://github.com/ucbepic/DataAgentBench)）：评什么：企业数据代理回答自然语言数据问题的能力。核心思想：用 12 个数据集、9 个领域、4 类数据库管理系统和 54 个查询，测试跨数据库集成、脏键 join、非结构化文本转换和领域知识，而不是只测单库 Text-to-SQL。
- [EnterpriseArena（CFO）](https://arxiv.org/abs/2603.23638)：评什么：动态企业环境中的 CFO 式长时程资源分配。核心思想：把决策展开为 132 个月的企业模拟，agent 需要在预算化工具调用、部分可观测财务状态、宏观信号和资金约束下维持现金不为负并最大化终局价值，专门暴露“只分析不行动”和长期风险控制失败。
- [Claw-Eval](https://arxiv.org/abs/2604.06132)（[开源代码](https://github.com/claw-eval/claw-eval)）：评什么：真实软件环境中的多步骤 agent 工作流。核心思想：用 300 个真人验证任务、9 类场景和 2,159 个细粒度 rubric，把 Completion、Safety、Robustness 和跨三次运行的一致通过率纳入统一评测，并通过执行轨迹、审计日志和环境快照做 trajectory-aware grading。
- [ClawBench](https://arxiv.org/abs/2604.08523)（[项目页](https://claw-bench.com/)；[开源代码](https://github.com/reacher-z/ClawBench)；[数据集](https://huggingface.co/datasets/TIGER-Lab/ClawBench)）：评什么：真实 live website 上的日常在线任务与状态变更操作。核心思想：从 153 个跨 144 个真实平台的写操作型网页任务起步，并在新版 leaderboard 中维护 130 个更新任务；通过最终 HTTP 请求拦截、payload judge 和多层轨迹记录，降低真实网站评测的破坏性与不可复现性。
- [OccuBench](https://arxiv.org/abs/2604.10866)（[开源代码](https://github.com/GregxmHu/OccuBench)，[数据集](https://huggingface.co/datasets/gregH/OccuBench)）：评什么：跨行业、跨职业的真实专业任务场景。核心思想：用 Language World Models / Language Environment Simulators 模拟领域工具响应，覆盖 100 个专业任务场景、10 个行业类别、65 个专业领域和 382 个可解实例；同时通过显式错误、隐式数据退化与混合故障注入评估“任务完成 + 环境鲁棒性”的职业画像。
- [AlphaEval](https://arxiv.org/abs/2604.12162)（[开源代码](https://github.com/GAIR-NLP/AlphaEval)）：评什么：生产环境中的完整 agent 产品表现。核心思想：从 7 家真实部署 agent 的公司抽取 94 个生产任务，覆盖 6 个 O*NET 职业领域，用 LLM-as-a-Judge、reference-driven metrics、formal verification、rubric、UI 测试等多范式组合评价 Claude Code、Codex 等完整 agent system，而不只评模型 API。
- [CI-Work](https://arxiv.org/abs/2604.21308)：评什么：企业 LLM agent 的 contextual integrity 与隐私泄漏风险。核心思想：在 dense retrieval 企业工作流中区分 essential content 与 sensitive context，覆盖 5 类信息流方向，评估 agent 能否完成任务同时抑制敏感上下文外泄，补足现实工作里“有用但不能泄密”的安全维度。
- [ClawMark](https://arxiv.org/abs/2604.23781)（[项目页](https://claw-mark.com/)；[开源代码](https://github.com/evolvent-ai/ClawMark)）：评什么：多日历时间跨度的多模态同事型现实工作任务。核心思想：用真实文件、日历、消息和延迟事件构造 1 到 3 天的 coworker-agent 工作流，检验 agent 是否能跨天维持任务状态、等待外部反馈并按时交付。
- [Odysseys](https://arxiv.org/abs/2604.24964)（[项目页](https://odysseys-website.pages.dev/)）：评什么：真实网页上的长程现实任务。核心思想：用真实网站、多阶段目标和状态依赖构造 realistic long-horizon web tasks，介于网页 GUI、现实在线工作和长时运行评测之间。
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)（[项目页](https://claw-eval-live.github.io/)；[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：评什么：会随真实需求变化的企业工作流 agent。核心思想：从 ClawHub marketplace 信号中刷新任务分布，当前版本含 105 个任务和 17 个任务族，并计划按季度重采样；评分同时读取执行 trace、审计日志、服务状态和 workspace 产物，使 benchmark 不只是静态题库。
- [Workspace-Bench](https://arxiv.org/abs/2605.03596)：评什么：带大规模文件依赖的 workspace learning 任务。核心思想：构造包含 5 类 worker profile、74 种文件类型和 20,476 个文件的现实工作区，用文件依赖图和多维 rubric 检查 agent 是否能跨文件检索、推理、更新和交付。
- [WildClawBench](https://arxiv.org/abs/2605.10912)（[开源代码](https://github.com/internlm/WildClawBench)）：评什么：真实 CLI agent harness 中的长程、多模态、双语工作任务。核心思想：在可复现 Docker 容器里运行 OpenClaw、Claude Code、Codex 或 Hermes Agent 等真实 harness，提供 60 个平均 8 分钟、20+ 工具调用的人工任务，并用规则检查、环境状态审计与 LLM/VLM judge 混合评分，显式暴露 harness 选择对结果的影响。

## 2.7.3 Agent Harness

- [BrowserGym Ecosystem](https://arxiv.org/abs/2412.05467)（[开源代码](https://github.com/ServiceNow/BrowserGym)）：统一 WebArena、VisualWebArena、WorkArena 等网页/企业工作环境，并配套 AgentLab 实验框架，适合做现实网页和 workplace agent 的可复现比较。
- [Alita](https://arxiv.org/abs/2505.20286)（[开源代码](https://github.com/CharlesQ9/Alita)）：偏生产环境的通用 solver agent，强调跨工具编排与复杂工作流执行，可迁移到现实业务任务的多步骤执行场景。
- [WorkForceAgent-R1](https://arxiv.org/abs/2505.22942)（开源代码：未找到稳定公开仓库）：面向 WorkArena 的 workplace web agent，使用规则化 R1-style 强化学习提升单步推理、格式遵循和动作正确性；更像“企业网页导航”场景中的专项执行器，而非通用聊天代理。
- [HomerAgent](https://arxiv.org/abs/2508.09124)（[开源代码](https://github.com/microsoft/OdysseyBench)）：OdysseyBench 配套的办公生产力 agent/harness，用显式记忆组织长程工作流中的阶段结果，适合分析 office workflow 中的上下文遗忘和错误复用。
- [AgentArch Reference Harness](https://arxiv.org/abs/2509.10769)（[开源代码](https://github.com/ServiceNow/AgentArch)）：用统一企业任务环境比较多种 agent 架构，适合把 planner-executor、多代理、memory、工具路由等 harness 设计变量拆开做消融。
- [ARE](https://arxiv.org/abs/2509.17158)（[开源代码](https://github.com/facebookresearch/meta-agents-research-environments)）：把真实任务环境做成会异步变化的运行时，支持通知、外部系统、状态演化和执行日志，适合评测 agent 在动态工作流中的持续计划更新。
- [BrowserAgent](https://arxiv.org/abs/2510.10666)（[开源代码](https://github.com/TIGER-AI-Lab/BrowserAgent)）：在真实浏览器动作空间中执行多步任务的 solver agent，适合 WorldTravel 这类现实约束驱动的网页任务。
- [HAL Harness](https://openreview.net/pdf?id=vUaY1t64ZZ)（[开源代码](https://github.com/princeton-pli/hal-harness)）：标准化、成本可见的 agent evaluation harness，提供统一 CLI、并行运行、日志/成本追踪与 leaderboard 提交流程，适合把现实工作 agent 的可复现实验从“单论文脚本”推进到持续评测。
- [Enterprise Deep Research](https://arxiv.org/abs/2510.17797)（[开源代码](https://github.com/SalesforceAIResearch/enterprise-deep-research)）：企业研究场景的多代理深研系统实现；核心思想：把企业私有知识、公开网页、消息和文件检索接到 planner/retriever/writer/checker 流程中，适合现实组织内的调研和汇报工作流。
- [EvoEnv](https://arxiv.org/abs/2601.08173)（[开源代码](https://github.com/KnowledgeXLab/EvoEnv)）：TraineeBench 背后的统一 environment / harness 框架，提供 workspace manager、virtual clock、tool gateway、trajectory/evaluation pipeline 和可视化 trace viewer，适合研究动态任务调度与持续学习型 workplace agent。
- [DAB DataAgent](https://arxiv.org/abs/2603.20576)（[开源代码](https://github.com/ucbepic/DataAgentBench)）：Data Agent Benchmark 自带的数据代理执行框架，围绕多数据库连接、Python 执行、查询日志、工具调用轨迹和 Pass@1 聚合评估组织，适合企业数据问答/分析类任务的 harness 参考。
- [EnterpriseLab](https://arxiv.org/abs/2603.21630)（开源代码：未找到稳定公开仓库）：面向企业 agent 的全栈开发与部署平台；把 MCP 化企业应用环境、自动轨迹合成、训练流水线和持续评估接在一起，并以含 15 个应用、140+ 工具的 EnterpriseArena 实例验证，属于“企业私有化 agent harness + 数据生成 + 训练评测闭环”路线。
- [Claw-Eval Harness](https://arxiv.org/abs/2604.06132)（[开源代码](https://github.com/claw-eval/claw-eval)）：围绕 OpenClaw 风格 agent 运行多类真实任务，强调三路证据记录、细粒度 rubric、Pass^k 稳定性和安全/鲁棒性检查，适合做可部署 agent 的回归评测框架。
- [ClawBench Browser Harness](https://arxiv.org/abs/2604.08523)（[开源代码](https://github.com/reacher-z/ClawBench)）：围绕真实浏览器会话构建任务录制、HTTP 拦截、轨迹回放和 payload 判定流水线，适合评测会改写远端状态的浏览器 agent，同时尽量避免真的提交破坏性操作。
- [OccuBench LWM Harness](https://arxiv.org/abs/2604.10866)（[开源代码](https://github.com/GregxmHu/OccuBench)）：把职业场景中的工具响应外包给 Language World Model，并提供 reference agent loop、fault injection、3-vote rubric verifier 与 OpenAI-compatible API 接口；其价值在于让缺少真实后端系统的职业任务也能被 agent 交互式评测。
- [Agentic Harness Engineering](https://arxiv.org/abs/2604.25850)：把 harness 变成可观测、可迭代的对象；核心思想：用组件可见性、经验可见性和决策可见性，把 coding-agent harness 的自动演化变成可验证闭环。
- [Claw-Eval-Live Harness](https://arxiv.org/abs/2604.28139)（[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：把 marketplace signal 到任务快照、mock service、workspace fixture、grader 与 leaderboard 聚合打通，适合构建会周期性刷新且能保留可复现快照的 workflow benchmark。
- [WildClawBench Native Runtime Harness](https://arxiv.org/abs/2605.10912)（[开源代码](https://github.com/internlm/WildClawBench)）：用 Docker 和真实 CLI agent harness 承载长程任务，强调 agent 系统、工具运行时与模型三者共同评测，是对只测裸模型或轻量 wrapper 的现实化补充。

## 2.7.4 Skill

- [travel-planner](https://skills.sh/ailabs-393/ai-labs-claude-skills/travel-planner) 最贴近 `WorldTravel`。
- [implementation-planner](https://skills.sh/jumppad-labs/jumppad/implementation-planner) 适合把现实工作拆成可执行多阶段计划。
- [ocr-document-processor](https://skills.sh/dkyazzentwatwa/chatgpt-skills/ocr-document-processor) 适合 `信息抽取 / 文档处理`。
- [train-fasttext](https://skills.sh/letta-ai/skills/train-fasttext) 适合 `Text Classification` 这类轻量结构化任务。
- [tapestry](https://skills.sh/nicepkg/ai-workflow/tapestry) 适合把跨系统工作流拼成现实业务流程。
- [minimax-xlsx](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) 适合表格类现实工作：读取/清洗/分析与生成 `.xlsx` 工件。
- [minimax-docx](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) 适合办公文档类现实工作：生成/编辑 `.docx` 报告、合同草案与结构化材料。
- [pptx-generator](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) 适合把现实工作输出固化为可交付的 `.pptx` 演示文稿。
- [minimax-pdf](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) 适合把 PDF 材料纳入现实工作流：解析、抽取与结构化引用。
