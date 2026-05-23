# 2.3.4 Agent Harness

- [MindSearch](https://arxiv.org/abs/2407.20183)（[开源代码](https://github.com/InternLM/MindSearch)）：多智能体网页搜索 harness，把用户问题拆成子问题，检索并整合证据，最后生成带引用的答案；这是一个容易被 BrowseComp 泛关键词漏掉的知名搜索系统。
- [Co-STORM](https://arxiv.org/abs/2408.15232)（[开源代码](https://github.com/stanford-oval/storm)；[项目页](http://storm.genie.stanford.edu)）：协作式信息搜集 harness，多个 LM agent 探索来源、维护动态 mind map，并允许用户 steer，再输出带引用报告，连接开放网页搜索与 deep research。
- [FinSearch](https://arxiv.org/abs/2502.15684)：面向金融实时信息检索的时间感知 search-agent 框架。核心思想：把金融问题拆成图结构子查询，自适应改写搜索，按时间上下文加权证据，并在 FinSearchBench-24 上评测。
- [WebThinker](https://arxiv.org/abs/2504.21776)（[开源代码](https://github.com/RUC-NLPIR/WebThinker)；把 `think-search-draft` 交错在同一条长链路里，代表“搜写一体”的可迁移互联网搜索代理范式）
- [Alita](https://arxiv.org/abs/2505.20286)（[开源代码](https://github.com/CharlesQ9/Alita)；更偏通用工具编排的 agent，可对接多类搜索/浏览 runtime，不是单一 benchmark 专用）
- [BrowseMaster](https://arxiv.org/abs/2508.09129)（开源代码：未找到稳定公开仓库；程序化工具增强的双代理网页浏览框架，在 BrowseComp-en 与 BrowseComp-ZH 上报告强结果，适合作为“搜索策略 agent + 验证 agent”分工参考）
- [BrowserAgent](https://arxiv.org/abs/2510.10666)（[开源代码](https://github.com/TIGER-AI-Lab/BrowserAgent)；把真实浏览器动作空间与显式 memory 接入 agent loop，适合作为 browser-native 搜索/浏览任务的通用基线）
- [M-ASK](https://arxiv.org/abs/2601.04703)：多智能体搜索框架，把 search behavior agent 与 knowledge optimization agent 分开。核心思想：把规划、搜索执行和知识优化拆成可观察的角色，降低单体式 search agent 的轨迹膨胀和信用分配问题。
- [SmartSearch](https://arxiv.org/abs/2601.04888)（开源代码：未找到稳定公开仓库；面向 search agent 的过程奖励查询改写框架；核心思想是用查询级 reward 引导 agent 学会何时扩展、收缩和重写搜索目标）
- [Search More, Think Less（SMTL）](https://arxiv.org/abs/2602.22675)（[开源代码](https://github.com/OPPO-PersonalAI/SMTL)；长程 agentic search 框架；核心思想是把更多预算放到并行检索和证据覆盖上，减少昂贵深推理对跨场景泛化的负担）
- [InfoSeeker](https://arxiv.org/abs/2604.02971)（[开源代码](https://github.com/Memento-Teams/InfoSeeker)；层级并行网页信息寻址框架，在 WideSearch-en 与 BrowseComp-ZH 上报告效率和准确率收益，适合复用其 `planner -> parallel search -> evidence merge` harness）
- [MolmoWeb](https://arxiv.org/abs/2604.08516)（[开源代码](https://github.com/allenai/molmoweb)；视觉驱动的开放网页 agent；核心思想：只看截图做操作，不依赖 HTML / accessibility tree）
- [Web2BigTable](https://arxiv.org/abs/2604.27221)（[开源代码](https://github.com/web2bigtable/Web2BigTable)；互联网级信息搜索与抽取系统；核心思想是用 bi-level multi-agent 先找来源、再抽结构化表格，和 WideSearch 的表格产出协议直接相邻）
- [LongSeeker](https://arxiv.org/abs/2605.05191)（开源代码：未公开；长程搜索 agent；核心思想是用 `Skip / Compress / Rollback / Snippet / Delete` 等 Context-ReAct 操作弹性管理工作上下文，减少长链路搜索中的成本、遗忘与幻觉）
- [Context Gathering Decision Process](https://arxiv.org/abs/2605.07042)（开源代码：未公开；把 agentic search 形式化为 POMDP；核心思想是显式建模“是否继续搜、搜哪里、何时停止”，为长上下文代码库、企业数据和网页检索提供统一决策框架）
- [DIVAgent](https://doi.org/10.1145/3746252.3761059)：受人类搜索过程启发的多样化搜索 agent harness。核心思想：把查询意图理解、结果探索和多样化组织成 agent 工作流，减少冗余结果并覆盖更多用户意图。
