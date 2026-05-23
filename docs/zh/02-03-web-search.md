# 2.3 互联网搜索

> 上级章节：2. 基础 Agent

## 2.3.1 Leaderboard

- [BrowseComp Benchmark Leaderboard](https://llm-stats.com/benchmarks/browsecomp)：第三方持续汇总 BrowseComp 分数，适合追踪 live web search 能力的公开报告结果；不是 OpenAI 官方提交榜，引用时应把它视作聚合榜单。
- [BrowseComp-ZH Leaderboard](https://huggingface.co/spaces/PALIN2018/BrowseComp-ZH)：BrowseComp-ZH 官方 Hugging Face Space；适合比较中文网页搜索、多跳检索和信息整合 agent。
- [BrowseComp-Plus Leaderboard](https://huggingface.co/spaces/Tevatron/BrowseComp-Plus)：BrowseComp-Plus 官方 Hugging Face Space；适合在固定文档语料上比较检索器、浏览 agent 和上下文工程，而不受 live web 漂移影响。
- [Search Arena](https://github.com/lmarena/search-arena)：搜索增强 LLM 偏好数据与分析入口；适合观察 search augmentation、引用、来源可信度和用户偏好之间的关系。
- [Wizwand BrowseComp-ZH SOTA](https://www.wizwand.com/sota/deep-research-on-browsecomp-zh-score)：第三方 BrowseComp-ZH SOTA 聚合页；适合补充查找 BrowseMaster、InfoSeeker、ReSum 等网页搜索 agent 的公开成绩线索。

## 2.3.2 Survey

- [From Matching to Generation: A Survey on Generative Information Retrieval](https://arxiv.org/abs/2404.14851)：解释检索从文档排序转向生成结果与答案的演进。
- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG](https://arxiv.org/abs/2501.09136)：回顾规划检索、选择工具并迭代使用证据的 agent。
- [A Survey of Large Language Model Empowered Agents for Recommendation and Search: Towards Next-Generation Information Retrieval](https://arxiv.org/abs/2503.05659)：连接用户意图、交互式搜索、检索规划与反馈适应。
- [A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models](https://arxiv.org/abs/2503.23350)：覆盖网页环境、感知、规划、动作执行、评测与安全。
- [A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges](https://arxiv.org/abs/2508.05668)：把复杂搜索组织为迭代查询规划、证据获取、评测与综合。

## 2.3.3 Bench

- [WebArena](https://arxiv.org/abs/2307.13854)：评测 browser-native 动作空间下的端到端网页任务完成；核心思想是“自托管多站点网页环境 + 浏览器原生动作 + 自动评测脚本”。（[开源代码](https://github.com/web-arena-x/webarena)）
- [VisualWebArena](https://arxiv.org/abs/2401.13649)：评测带视觉网页理解的 WebArena 扩展；核心思想是在同一 browser-native runtime 中把视觉感知与交互纳入闭环。（[开源代码](https://github.com/web-arena-x/visualwebarena)）
- [ST-WebAgentBench](https://arxiv.org/abs/2410.06703)：评测安全与可信 web agent 的行为与约束遵循；核心思想是用 BrowserGym/WebArena 范式提供可复现的安全评测模板。（[开源代码](https://github.com/segev-shlomov/ST-WebAgentBench)）
- [Unsafe LLM-Based Search](https://arxiv.org/abs/2502.04951)：评测 AI-powered search engine 的安全风险。核心思想是定义 threat model 和风险类型，在恶意或不安全查询条件下测试生产搜索系统是否会引用有害内容或恶意网站。
- [BrowseComp](https://arxiv.org/abs/2504.12516)：评测在真实互联网环境中“检索、阅读、整合”的信息获取能力；核心思想是把信息获取约束为可执行的浏览与证据链路，而不是离线知识问答。
- [BrowseComp-ZH](https://arxiv.org/abs/2504.19314)（[开源代码](https://github.com/PALIN2018/BrowseComp-ZH)；[Leaderboard](https://huggingface.co/spaces/PALIN2018/BrowseComp-ZH)；[Wizwand BrowseComp-ZH SOTA](https://www.wizwand.com/sota/deep-research-on-browsecomp-zh-score)）：评测中文互联网环境中的高难网页浏览与多跳检索推理；核心思想是把中文网页生态中的平台碎片化、跨页检索与信息整合难点显式 benchmark 化。
- [Seal-0 / SealQA](https://arxiv.org/abs/2506.01062)：评测搜索增强推理在更高答案完整性要求下的表现。核心思想：通过检查 agent 是否先收集足够证据再给最终答案，提高“检索 + 推理”任务门槛。
- [WebChoreArena](https://arxiv.org/abs/2506.01952)：评测更繁琐、更贴近“网页劳动”的长流程网页操作；核心思想是把网页上的重复劳动与多步操作任务系统化。（[开源代码](https://github.com/WebChoreArena/WebChoreArena)）
- [Search Arena](https://arxiv.org/abs/2506.05334)（[开源代码](https://github.com/lmarena/search-arena)）：评测 search-augmented LLM 在真实用户偏好中的表现。核心思想：收集多轮搜索增强回答和人类偏好票，分析引用质量、来源可信度、搜索调用和最终回答偏好之间的关系。
- [Mind2Web 2](https://arxiv.org/abs/2506.21506)（[开源代码](https://github.com/OSU-NLP-Group/Mind2Web-2)）：评测 agentic search with agent-as-a-judge。核心思想：用长程实时网页搜索与信息综合任务检查 agent 在动态网页、证据引用和复杂答案构造中的表现，并用代理裁判辅助评估。
- [WebWalker](https://aclanthology.org/2025.acl-long.508/)：评测 LLM 的网站遍历能力。核心思想：要求模型或 agent 穿行网站子页面并系统抽取有用信息，补足浅层搜索结果阅读和深层站内导航之间的空白。
- [MMInA](https://aclanthology.org/2025.findings-acl.703/)：评测多跳多模态互联网 agent。核心思想：使用持续变化的真实多模态网站，让 agent 跨页面组合导航和取证，而不是解决静态多模态问答。
- [WebDS](https://arxiv.org/abs/2508.01222)（数据集：[yamhm/WebDS](https://huggingface.co/datasets/yamhm/WebDS)）：评测网页数据科学任务。核心思想：让 agent 在容器化网站中导航、获取数据、处理结构化/非结构化信息并产出分析报告，连接网页搜索、数据抽取和数据科学工作流。
- [BrowseComp-Plus](https://arxiv.org/abs/2508.06600)（[开源代码](https://github.com/texttron/BrowseComp-Plus)）：评测固定语料库中的深度网页检索与浏览推理；核心思想是把 BrowseComp 从黑盒 live search 改成约 10 万篇人工核验文档的可复现实验环境，从而解耦检索器、LLM agent 与上下文工程的影响。
- [WideSearch](https://arxiv.org/abs/2508.07999)：评测“宽域检索 -> 结构化表格产出”的 search-heavy 任务；核心思想是把输出约束为结构化条目，并用 `SR / Row-F1 / Item-F1` 等协议做可比评测。（[开源代码](https://github.com/ByteDance-Seed/WideSearch)）
- [MM-BrowseComp](https://arxiv.org/abs/2508.13186)（[开源代码](https://github.com/MMBrowseComp/MM-BrowseComp)）：评测多模态网页浏览 agent 的检索与推理能力；核心思想是把问题线索和网页证据中的图像、视频内容纳入 BrowseComp 风格的多跳浏览任务，并提供 checklist 做细粒度诊断。
- [FinSearchComp](https://arxiv.org/abs/2509.13160)：评测专家级金融搜索与推理。核心思想：要求 agent 检索、比对并综合金融信息，而不是只靠参数知识回答，适合作为 search-heavy 专业工作的垂直压力测试。
- [BrowserArena](https://arxiv.org/abs/2510.02418)：评测真实开放网页上的 LLM agent 导航任务；核心思想是用 live open-web arena 收集用户提交任务、进行 agent 对战，并用 step-level human feedback 诊断 captcha、弹窗和直接导航等失败模式。
- [Needle in the Web](https://arxiv.org/abs/2512.16553)（[开源代码](https://github.com/Tango-Whiskyman/Needle_in_the_Web)）：评测真实网页中的目标页面检索；核心思想是把模糊探索式查询转成需要找到唯一目标网页的任务，考察 agent 在语义歧义、多域网页和来源核验下的检索能力。
- [UIS-Digger](https://arxiv.org/abs/2603.08117)：评什么：真实世界未索引信息寻址。核心思想：把搜索引擎难以直接召回的网页、文件和深层入口组织成任务，评估 agent 是否会发现入口、调整查询并跟踪证据来源。
- [LiveWeb-IE](https://arxiv.org/abs/2603.13773)：评什么：在线网页信息抽取。核心思想：把网页变化、实时来源和结构化抽取目标放进 live benchmark，补足 BrowseComp 式问答对表格化抽取与数据更新的覆盖不足。
- [VisBrowse-Bench](https://arxiv.org/abs/2603.16289)：评什么：视觉原生多模态网页搜索。核心思想：要求 agent 在真实网页中同时处理截图、图像线索和文本页面，补足 MM-BrowseComp 之后对 visual-native search 轨迹的专门评测。
- [WebForge](https://arxiv.org/abs/2604.10988)：评什么：真实、可复现、可扩展的 browser agent benchmark。核心思想：自动生成带真实网页噪声的可控任务环境，缓解 live website 漂移、人工构造成本和静态 sandbox 失真之间的三难问题。
- [MERRIN](https://arxiv.org/abs/2604.13418)：评什么：噪声 web 环境里的多模态证据检索与多跳推理。核心思想：把文本、图像、视频、音频一起纳入搜索任务。
- [StressWeb](https://arxiv.org/abs/2604.16385)：评什么：真实交互扰动下的 web agent 鲁棒性。核心思想：在 WebArena/VisualWebArena 风格任务里系统注入动态 DOM、加载延迟、提示变体和 UI 噪声，诊断搜索/浏览 agent 的脆弱点。

## 2.3.4 Agent Harness

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

## 2.3.5 Skill

- [playwright-cli](https://github.com/microsoft/playwright-cli/tree/main/skills/playwright-cli)（可复用 browser-native action skill；与 WebArena 风格动作空间较贴近）
- [playwright](https://skills.sh/openai/skills/playwright)（通用 Playwright skill；偏浏览器执行层）
- [browser-automation](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/utilities/browser-automation)（系统化的 Playwright / Puppeteer 等待策略与网页自动化经验库）
- [bright-data-mcp](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/web-data/bright-data-mcp)（更适合“搜索 + 抓取 + 浏览器交互 + 抽取”的一体化工作流）
- [actionbook](https://skills.sh/actionbook/actionbook/actionbook)（把网页交互操作做成可复用 action script，含选择器与回退逻辑）
- [browserbase/agent-browse/browser](https://skills.sh/browserbase/agent-browse/browser)（浏览器自动化执行 skill；偏运行时）
- [serpapi](https://skills.sh/vm0-ai/vm0-skills/serpapi)（搜索 API skill；更贴近 WideSearch 的 search-heavy workflow）
- [ddgr](https://skills.sh/ysm-dev/ddgr-skill/ddgr)（终端搜索 skill；适合作为轻量检索层）
- [parallel-web-search](https://skills.sh/parallel-web/parallel-agent-skills/parallel-web-search) 适合并行 query fan-out 与来源收集，可服务 WideSearch/BrowseComp 类需要广召回再综合的任务。
- [web-search](https://skills.sh/brave/brave-search-skills/web-search) 是 Brave Search 支撑的 provider skill，适合需要稳定搜索 API、而不是浏览器抓取的 agent。
- [tavily](https://github.com/openclaw/openclaw/tree/main/extensions/tavily/skills/tavily) 是 Tavily 支撑的搜索与抽取 skill，更贴近“搜索 + 内容抽取”的工作流，而不只是 SERP 查询。
- [web-search-2](https://clawhub.ai/okaris/web-search-2)（研究、事实核查与内容抽取导向的检索型 skill）
