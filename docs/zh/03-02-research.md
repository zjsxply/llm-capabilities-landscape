# 3.2 科研

> 上级章节：3. 下游应用


## 3.2.1 Leaderboard

- [MLE-bench Leaderboard / Official Results](https://github.com/openai/mle-bench)：OpenAI MLE-bench 官方仓库维护公开结果与提交说明；适合追踪 AIDE、MLE-STAR、MLEvolve、Famou-Agent、MARS+ 等 ML 工程 agent 在 Kaggle-derived 任务上的可复现表现。
- [PaperBench Leaderboard / Official Results](https://github.com/openai/frontier-evals/blob/main/project/paperbench/README.md)：OpenAI Frontier Evals 中 PaperBench 的官方入口；适合比较论文复现、代码开发和 rubric grading 下的长程科研编码 agent。
- [MLRC-Bench Leaderboard](https://huggingface.co/spaces/launch/MLRC_Bench)：MLRC-Bench 官方 Hugging Face 榜单；适合观察更开放 ML research challenge 中的 agent 研究推进能力。
- [ResearchCodeBench Leaderboard](https://researchcodebench.github.io/leaderboard/index.html)：ResearchCodeBench 官方榜单；适合比较模型和 coding agent 是否能根据最新 ML 论文实现未见过的研究代码。
- [SciArena](https://sciarena.allen.ai/)：AI2 科学文献任务开放评测平台；适合追踪科学文献理解、跨论文综合、引用式回答和用户偏好评价。
- [AstaBench Leaderboard](https://huggingface.co/spaces/allenai/asta-bench-leaderboard)：AI2 AstaBench 榜单；适合把文献理解、工具使用和科学研究型任务统一到 science agent 评测视图中。
- [CORE-Bench / CORE-Bench Hard](https://hal.cs.princeton.edu/corebench_hard)：HAL 的 CORE-Bench Hard 榜单；适合追踪研究复现类 agent 在真实论文可复现性任务上的表现。

## 3.2.2 Bench

- [MLAgentBench](https://arxiv.org/abs/2310.03302)（[开源代码](https://github.com/snap-stanford/MLAgentBench)）：评什么：机器学习研究任务的端到端自动化；核心思想：把研究任务、执行环境与评分协议打包成可复现平台，测量 agent 是否真的能做出可运行实验与有效改进。
- [DiscoveryBench](https://arxiv.org/abs/2407.01725)（[开源代码](https://github.com/allenai/discoverybench)）：评什么：数据驱动的科学发现；核心思想：用真实科学数据与假设生成/验证流程，评测 agent 能否提出并检验有意义的科学结论。
- [SciCode](https://arxiv.org/abs/2407.13168)（[开源代码](https://github.com/scicode-bench/SciCode)）：评什么：真实科研问题的科学编码（scientist-curated research coding）。核心思想：题目由科学家参与构建，提供 gold solutions/tests，并把科研问题拆成多个需要知识召回、推理与代码合成的子问题。
- [CORE-Bench / CORE-Bench Hard](https://arxiv.org/abs/2409.11363)：评什么：已发表研究的计算可复现性。核心思想：把论文、代码、数据和执行环境转成可由 agent 操作的复现实验任务，作为 PaperBench 之前“科研复现”路线的重要基线；HAL 另维护 CORE-Bench Hard 榜单作为更难复现子集入口。
- [MLE-bench](https://arxiv.org/abs/2410.07095)（[开源代码](https://github.com/openai/mle-bench)）：评什么：机器学习工程与数据科学竞赛式建模能力，覆盖 75 个 Kaggle competition，并以生成 `submission.csv` 后的竞赛指标和 `Any Medal` 聚合分数评估。核心思想：把真实 ML 工程中的数据读取、EDA、特征工程、模型选择、调参、训练、验证、提交格式修复和长时间实验迭代放进同一个可执行 benchmark；官方还提供 22 题 Low/Lite split，降低完整评测的 3.3TB 数据与 24 小时运行成本。
- [SciArena](https://sciarena.allen.ai/SciArena_An_Open_Evaluation_Platform_for_Foundation_Models_in_Scientific_Literature_Tasks.pdf)（[平台](https://sciarena.allen.ai/)）：评什么：科学文献理解、综合与引用式回答。核心思想：用开放评测平台收集模型在 literature tasks 上的表现，把文献级理解和用户偏好评价接进科研 agent 评估。
- [RE-Bench](https://arxiv.org/abs/2411.15114)（[开源代码](https://github.com/METR/RE-Bench)）：评什么：AI R&D 自动化中的真实研究工程任务，覆盖算法设计、实验执行和结果分析等开放式研发工作。核心思想：与 MLE-bench 的 Kaggle 竞赛协议互补，RE-Bench 更强调研究工程师式的问题求解、代码实验与研究判断。
- [MLGym](https://arxiv.org/abs/2502.14499)（[开源代码](https://github.com/facebookresearch/MLGym)）：评什么：AI research agent 的可交互 ML 研究环境与 benchmark。核心思想：把开放式机器学习研究任务做成 Gym 式环境，使 agent 能反复实验、观察结果并改进研究方案。
- [BixBench](https://arxiv.org/abs/2503.00096)（[开源代码](https://github.com/Future-House/BixBench)，[数据集](https://huggingface.co/datasets/futurehouse/BixBench)）：评什么：生物信息学真实数据分析任务中的 agent 表现。核心思想：从 Code Ocean capsule 派生多步骤开放式问题，让 agent 探索数据、执行分析并解释结果，突出“科学数据分析”而不只是论文问答。
- [SciReplicate-Bench](https://arxiv.org/abs/2504.00255)（[开源代码](https://github.com/xyzCS/SciReplicate-Bench)）：评什么：从近期研究论文复现算法实现。核心思想：要求 agent 理解论文中的算法描述、检索依赖并写出可执行代码，用 reasoning graph accuracy 与执行准确率共同衡量科研复现能力。
- [PaperBench](https://arxiv.org/abs/2504.01848)：评什么：读论文并在 fresh sandbox 复现实验/实现，然后用 rubric grading 评估。核心思想：把“是否真的能复现/跑通”作为核心验收，强调 sandbox rerun 与 rubric judge，而不是仅看生成代码的表面相似度。
- [MLRC-Bench](https://arxiv.org/abs/2504.09702)（[Leaderboard](https://huggingface.co/spaces/launch/MLRC_Bench)）：评什么：机器学习研究挑战中的 agent 表现，任务来自更开放的 ML research challenge 场景。核心思想：把“能否完成竞赛建模”进一步推向“能否推进研究挑战”，适合作为 MLE-bench 与 MLR-Bench 之间的过渡评测。
- [MASSW](https://aclanthology.org/2025.findings-naacl.127/)（[数据集](https://osf.io/7ygrq/?view_only=3d8261a0ea09489fa67ece2c68235afa)）：评什么：AI-assisted scientific workflows。核心思想：把多步骤科学工作实践做成 benchmark 任务，覆盖 workflow 规划与执行，而不只是论文问答。
- [CSR-Bench](https://aclanthology.org/2025.naacl-long.633/)：评什么：LLM agent 部署计算机科学研究仓库的能力。核心思想：把论文/仓库理解与环境配置、执行、调试连接起来，使研究仓库部署成为具体可测任务。
- [BAISBench](https://arxiv.org/abs/2505.08341)（[开源代码](https://github.com/ErpaiLuo/BAISBench)，[数据集](https://huggingface.co/datasets/ErpaiLuo/BAISBench)）：评什么：组学数据驱动的生物 AI scientist。核心思想：用真实单细胞转录组数据构造细胞类型标注和科学发现问答，评估 agent 能否从实验数据中提出有意义的生物学结论。
- [MLR-Bench](https://arxiv.org/abs/2505.19955)（[开源代码](https://github.com/chchenhui/mlrbench)）：评什么：开放式机器学习研究（idea -> proposal -> experimentation -> paper writing），含端到端与分阶段评估。核心思想：提供 `MLR-Judge` 与 `MLR-Agent` scaffold，把“科研流程”变成可复现、可审阅的评测协议，并显式暴露“实验造假/无效实验结果”等可靠性失败模式。
- [EXP-Bench](https://arxiv.org/abs/2505.24785)（[开源代码](https://github.com/Just-Curieous/Curie/tree/main/benchmark/exp_bench)）：评什么：AI agent 能否完成完整 AI 研究实验。核心思想：给定研究问题和不完整 starter code，要求 agent 提出假设、设计实验、实现、执行并分析结果，直接评估端到端实验能力。
- [ResearchCodeBench](https://arxiv.org/abs/2506.02314)（[项目页](https://researchcodebench.github.io/)；[开源代码](https://github.com/PatrickHua/ResearchCodeBench)）：评什么：从最新机器学习论文实现未见过的研究代码。核心思想：用 2024-2025 顶会论文构造 212 个可执行 coding challenge，专门检测模型是否能把新研究贡献翻译成代码。
- [KRAMABENCH](https://arxiv.org/abs/2506.06541)（[项目页](https://kramabench.org/)；[开源代码](https://github.com/mitdbg/KramaBench)，[数据集](https://huggingface.co/datasets/eugenie-y/KramaBench)）：评什么：数据湖上的 data-to-insight pipeline。核心思想：要求 agent 完成数据发现、清洗、整合、统计推理和 Python pipeline 编排，补足 MLE-bench 之外对开放数据科学研究流程的覆盖。
- [LLM Speedrunner](https://arxiv.org/abs/2506.22419)（[开源代码](https://github.com/facebookresearch/llm-speedrunner)）：评什么：agent 复现 NanoGPT speedrun 改进的能力。核心思想：把一个活跃的 ML 系统竞赛转成可执行复现任务，要求 agent 理解上一纪录训练脚本、实现已发布加速思路，并在 benchmark harness 下验证收益。
- [RExBench](https://arxiv.org/abs/2506.22598)（[项目页](https://rexbench.com/)）：评什么：coding agent 能否实现 AI 研究扩展。核心思想：把已发表论文和原始代码库作为上下文，让 agent 实现专家写出的新实验/扩展，并通过自动执行与指标检查评估研究延展能力。
- [AbGen](https://aclanthology.org/2025.acl-long.611/)：评什么：科研中的 ablation study 设计与评价。核心思想：测试模型是否能判断该消融什么、什么证据重要以及实验结论是否成立，而不是只会总结论文。
- [Sci2Pol-Bench](https://arxiv.org/abs/2509.21493)（[开源代码](https://github.com/WeiminWu2000/Sci2Pol)，[数据集](https://huggingface.co/datasets/Northwestern-CSSI/Sci2Pol-Bench)）：评什么：从科学论文到政策简报的科研转译流程。核心思想：把补全、理解、总结、生成和验证拆成五阶段写作任务，衡量模型能否把科学证据转化为面向政策读者的可用材料。
- [EvidenceBench](https://openreview.net/forum?id=lEQnUI5lEA)：评什么：从生物医学论文中抽取证据。核心思想：要求模型定位并抽取支撑主张的科学文本证据，是文献 grounded 科研 agent 的关键子任务。
- [MoSciBench](https://openreview.net/forum?id=kZHSvETWdi)（[开源代码](https://github.com/usail-hkust/MoSciBench)）：评什么：多模态数据驱动科学发现。核心思想：用端到端科学任务要求 agent 对齐异构数据、建模、解释并完成假设验证，连接多模态理解和科学分析流程。
- [FML-bench](https://arxiv.org/abs/2510.10472)（[开源代码](https://github.com/qrzou/FML-bench)）：评什么：基础机器学习研究问题中的 agent 迭代改进能力。核心思想：给 agent baseline code、评价 harness 和研究任务描述，要求它像科研人员一样迭代提升方案，而不只优化应用指标。
- [PaperArena](https://arxiv.org/abs/2510.10909)（[项目页](https://paperarena-ai.github.io/)；[开源代码](https://github.com/Melmaphother/PaperArena)）：评什么：跨论文、多工具辅助的科学文献推理。核心思想：要求 agent 调用解析、检索和计算等工具，把多个论文里的多格式证据整合成有根据答案。
- [AstaBench](https://arxiv.org/abs/2510.21652)（[开源代码](https://github.com/allenai/asta-bench)；[Leaderboard](https://huggingface.co/spaces/allenai/asta-bench-leaderboard)）：评什么：综合科研 agent 能力。核心思想：把文献检索、代码执行、数据分析和科学发现等任务统一到 Asta 科研 agent suite，用标准化工具环境和公开榜单比较不同 agent。
- [ReplicationBench](https://arxiv.org/abs/2510.24591)：评什么：agent 能否复现实验天体物理论文的核心贡献。核心思想：把整篇论文拆成由原作者共同设计的关键任务，分别评 faithfulness 与 correctness，更贴近真实科研复现。
- [LMR-BENCH](https://aclanthology.org/2025.emnlp-main.314/)：评什么：LLM agent 复现语言模型研究的能力。核心思想：在 language modeling 子领域内同时测试论文理解、实验配置、代码执行和结果复现。
- [Paper2SysArch](https://arxiv.org/abs/2511.18036)：评什么：从科学论文生成系统架构图。核心思想：把论文与真实架构图配对，并从语义准确性、布局连贯性和视觉质量评分，使科研传播工件的评测不只停留在纯文本或幻灯片。
- [SGI-Bench](https://arxiv.org/abs/2512.16969)（论文：Probing Scientific General Intelligence of LLMs with Scientist-Aligned Workflows）：评什么：科研流程对齐的科学通用智能评测。核心思想：把 scientist-aligned workflows 作为统一协议，考察模型在检索、推理、实验规划和结果整理上的端到端表现。
- [AInsteinBench](https://arxiv.org/abs/2512.21373)（[开源代码](https://github.com/ByteDance-Seed/AInsteinBench)）：评什么：科学计算/科研软件生态中的仓库级开发能力（基于真实科研代码库与 maintainer PR 派生任务）。核心思想：把科学研究软件开发放回“可执行环境 + 测试验证 + 科学语义失败模式”的真实语境中，衡量 agent 是否具备科研级工程能力。
- [HeurekaBench](https://arxiv.org/abs/2601.01678)（[开源代码](https://github.com/mlbio-epfl/HeurekaBench)，[项目页](https://brbiclab.epfl.ch/projects/heurekabench/)）：评什么：AI co-scientist 在真实实验数据驱动科研问题上的表现。核心思想：以 sc-HeurekaBench 等开放式单细胞分析任务评估 co-scientist agent 是否能提出可检验假设、执行分析并用 critic module 改善科学结论。
- [APEX / APEX-Bench](https://arxiv.org/abs/2601.04794)：评什么：agent 的学术海报编辑能力。核心思想：开放多层级海报编辑 API 与 review-adjust 循环，使 agent 能按细粒度用户指令修订高密度科研图文产物。
- [BABE](https://arxiv.org/abs/2602.05857)：评什么：生物领域的“实验推理”能力（在文本与视觉证据交织的科学材料上做研究式推断）。核心思想：强调把实验结果与上下文知识整合，考察因果推理与跨尺度推断，而不是背诵式生物知识 QA。
- [AIRS-Bench](https://arxiv.org/abs/2602.06855)（[开源代码](https://github.com/facebookresearch/airs-bench)）：评什么：前沿 AI 研究代理的端到端科研流程。核心思想：把 idea generation、实验分析与迭代修订放进同一套任务，专门观察 agent 是否能推进真实 AI research workflow。
- [SciAgentGym / SciAgentBench](https://arxiv.org/abs/2602.12984)（[项目页](https://www.huayusha.org/publication/SciAgentGym/)）：评什么：科学 agent 的多步骤工具使用。核心思想：提供 1,780 个跨自然科学工具和分层评测集，专门压测从单步调用到长程 workflow 的工具编排能力。
- [DECKBench](https://arxiv.org/abs/2602.13318)：评什么：多智能体系统生成和迭代编辑学术幻灯片的能力。核心思想：结合论文到幻灯片样本和真实感编辑指令，从内容忠实度、整套幻灯片连贯性、版式质量和多轮遵循度评估科研演示文稿生产。
- [SciPredict](https://arxiv.org/abs/2604.10718)：评什么：自然科学实验结果预测。核心思想：把“实验还没做时能否判断结果”单独作为科学预测任务，测试 LLM/agent 是否能超越知识问答而形成可验证的实验预判。
- [ResearchClawBench](https://github.com/InternScience/ResearchClawBench)（[数据集镜像](https://huggingface.co/datasets/InternScience/ResearchClawBench)）：评什么：OpenClaw/InternScience 生态中从 re-discovery 到 new-discovery 的端到端自动科研任务。核心思想：把目标论文、相关工作、数据、图表和多模态 checklist judge 打包到同一评测流程里，让 agent 按“是否复现甚至超过原论文”评分，而不是只回答文献问题。
- [AutoResearchBench](https://arxiv.org/abs/2604.25256)（[项目页](https://cheryou.github.io/autoresearchbench.github.io/)；[开源代码](https://github.com/CherYou/AutoResearchBench)）：评什么：复杂科学文献发现。核心思想：把 Deep Research 与 Wide Research 两类任务落到 1,000 个专家策划问题上，要求 agent 精确定位目标论文或全面收集满足条件的论文集合。
- [BioMysteryBench](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)（[数据集](https://huggingface.co/datasets/Anthropic/BioMysteryBench-full)）：评什么：真实生物信息学数据上的开放式科研谜题。核心思想：由专家提出可从实验数据客观验证的问题，用最终答案而非固定分析路径评分，补齐生物数据分析的高难开放式评测。
- [BixBench-Verified-50](https://huggingface.co/datasets/phylobio/BixBench-Verified-50)（说明：[Phylo blog](https://phylo.bio/blog/evaluating-ai-agents-in-biology)）：评什么：经专家清洗的 BixBench 子集。核心思想：移除或修正歧义题与错误答案，让生物信息学 agent 的分数更少受 benchmark 噪声影响，近期 BIOS、K-Dense Web、BioResearcher 等都在该子集上报告结果。
- [GeneBench](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)：评什么：遗传学多阶段推理和数据分析 agent。核心思想：用真实数据文件、数据库查询和多步推断组织任务，考察 agent 能否在复杂生命科学证据中形成可核验结论。
- [Multimodal Conference Dataset / MCD](https://arxiv.org/abs/2605.05831)：评估论文、幻灯片、报告视频和讲解视频之间的细粒度对应关系。核心思路是测试模型能否在真实科研传播使用的多种媒介之间对齐科学概念和视觉证据。
- [BioMedArena](https://arxiv.org/abs/2605.06177)（[开源代码](https://github.com/AI-in-Health/BioMedArena)）：评什么：生物医学 deep research agent 的统一评测与训练平台。核心思想：把 benchmark loading、tool exposure、execution mode、context management 和 scoring 解耦，接入 147 个生物医学 benchmark 与 75 个工具，降低各论文 harness 不一致带来的不可比问题。
- [PDEAgent-Bench](https://arxiv.org/abs/2605.09636)：评什么：从 PDE 规格生成可执行数值求解器。核心思想：用 DOLFINx、Firedrake、deal.II 等专业 FEM 库，从可运行、数值精度和效率三层评估 scientific coding agent。
- [Ambig-DS](https://arxiv.org/abs/2605.09698)：评什么：数据科学 agent 在任务框定歧义下是否会主动澄清。核心思想：基于 DSBench 和 MLE-bench 构造目标变量/评价目标歧义任务，暴露“产物可运行但任务理解错”的隐性失败。
- [SciIntegrity-Bench](https://arxiv.org/abs/2605.10246)（[开源代码](https://github.com/liuxingtong/Sci-Integrity-Bench)）：评什么：AI scientist 的学术诚信。核心思想：构造只能诚实承认失败、不能通过造数据/造结果完成的 dilemmatic scenarios，评估 agent 在完成压力下是否会学术不端。
- [Collider-Bench](https://arxiv.org/abs/2605.13950)（开源代码和任务语料见论文）：评什么：粒子物理实验分析复现。核心思想：要求 agent 从 LHC 论文和公开软件复现 simulation-and-selection pipeline，并用连续 histogram 指标和轨迹审计评分，补足真实科学复现任务。

## 3.2.3 Agent Harness

- [MLAgentBench Research Agent](https://arxiv.org/abs/2310.03302)（[开源代码](https://github.com/snap-stanford/MLAgentBench)）是 MLAgentBench 中用于科研任务评测的基线研究代理。
- [BudgetMLAgent](https://arxiv.org/abs/2411.07464)（开源代码：未公开）在 MLAgentBench 上用多代理协作、检索复用与 LLM cascade 做低成本科研任务自动化（以论文为准）。
- [AIDE](https://arxiv.org/abs/2502.13138)（[开源代码](https://github.com/WecoAI/aideml)）代表“迭代式代码实验”科研/数据科学代理路线，也是 MLE-bench 官方初始评测里最核心的开源 ML 工程 agent 之一；设计重点是 `propose experiment -> edit/run code -> inspect metric/log -> refine` 的实验树迭代，而不是一次性生成建模脚本。
- [AI co-scientist](https://arxiv.org/abs/2502.18864)（开源代码：未公开）：Google Research 的 Gemini 2.0 多代理科学假设生成系统，核心是 `generate -> debate -> evolve` 的异步假设锦标赛；在药物再利用、靶点发现和细菌进化机制解释中给出实验验证线索。
- [AI Scientist v2](https://arxiv.org/abs/2504.08066)（[开源代码](https://github.com/SakanaAI/AI-Scientist-v2)）强调从研究想法到实验与论文草稿的端到端闭环。
- [Paper2Code](https://arxiv.org/abs/2504.17192)（[开源代码](https://github.com/going-doer/Paper2Code)）是面向“论文到代码实现”的专项科研代理工作。
- [Robin](https://arxiv.org/abs/2505.13400)（[开源代码](https://github.com/Future-House/robin)）是 FutureHouse 的 lab-in-the-loop 多代理科学发现系统；把文献搜索、假设生成、实验设计、数据分析和后续假设更新接成闭环，并在 dAMD 药物候选发现案例中完成实验验证。
- [R&D-Agent](https://arxiv.org/abs/2505.14738)（[开源代码](https://github.com/microsoft/RD-Agent)）聚焦研发场景的分工式多代理工作流编排。
- [R&D-Agent-Quant](https://arxiv.org/abs/2505.15155)（[开源代码](https://github.com/microsoft/RD-Agent)）把 R&D-Agent 扩展到量化金融；核心工作流把量化研究拆成假设驱动的因子挖掘、代码生成、回测反馈和自适应调度，用于因子与模型联合优化。
- [MLR-Agent](https://arxiv.org/abs/2505.19955)（[开源代码](https://github.com/chchenhui/mlrbench)）是 MLR-Bench 论文提供的模块化 scaffold，覆盖 idea/proposal/experiment/writing 四阶段。
- [MLE-STAR](https://arxiv.org/abs/2506.15692)（[开源代码](https://github.com/google/adk-samples/tree/main/python/agents/machine-learning-engineering)）是 Google ADK 的机器学习工程 agent；核心 workflow 是 `web/search 参考方案 -> 生成 baseline -> 针对瓶颈做 targeted refinement`，在 MLE-bench 上成为 AIDE 之后的重要开源强基线。
- [ML-Master](https://arxiv.org/abs/2506.16499)（[开源代码](https://github.com/sjtu-sai-agents/ML-Master)）面向 AI-for-AI 机器学习研究任务，把探索和推理集成到多角色协作流程中，是 MLE-bench/MLE 任务上的代表性研究代理。
- [STELLA](https://arxiv.org/abs/2507.02004)（开源代码：未找到稳定公开仓库）是面向生物医学研究的自进化多代理系统；核心是 evolving Template Library 与动态 Tool Ocean，让工具创建代理持续发现并整合新的生信工具。
- [AIRA-dojo](https://arxiv.org/abs/2507.02554)（[开源代码](https://github.com/facebookresearch/aira-dojo)）是“训练场式科研代理行为框架”，用于构建与评估科研类代理行为。
- [K-Dense Analyst](https://arxiv.org/abs/2508.07043)（开源代码：未找到稳定公开仓库）是面向生物信息学分析的层级多代理系统；核心思想：用 planning loop 与 validated execution loop 连接高层科学目标、代码执行和结果校验。
- [RePro](https://arxiv.org/abs/2508.16671)（开源代码：未找到稳定公开仓库）强调细粒度验证与反思修复，是 PaperBench Code-Dev 方向较有代表性的论文复现代理工作。
- DS-GURU（[开源代码](https://github.com/mitdbg/KramaBench)；无独立论文；KRAMABENCH 配套数据科学 agent，把数据湖洞察任务分解为子任务并生成可执行 Python 数据处理/分析 pipeline）
- [ToolUniverse](https://arxiv.org/abs/2509.23426)（[开源代码](https://github.com/mims-harvard/ToolUniverse)）是用于构建 AI scientist 的工具生态和 MCP/SDK 底座；把 1000+ 科学工具、模型、数据库和 API 标准化为可调用组件，并支持从自然语言生成/优化工具接口。
- MLEvolve（[开源代码](https://github.com/InternScience/MLEvolve)；无 arXiv 论文）是 MLE-bench 榜单上公开代码的进化式 ML agent，突出多候选实验、进化搜索与性能反馈驱动的方案迭代。
- [AutoMLGen](https://arxiv.org/abs/2510.08511)（[开源代码](https://github.com/Alpha-Innovator/InternAgent)）面向 coding agent 的细粒度 AutoML 优化导航；在 MLE-bench 上报告 medal rate 与 valid submission 等指标，是 InternAgent/MLE 工程路线的论文版扩展。
- [MOSAIC](https://arxiv.org/abs/2510.08804)（开源代码：论文称接收后发布）是面向 SciCode 的多代理科学编码系统，通过 task-intelligent orchestration 分解、执行和验证科学代码任务，并按 SciCode 官方协议报告 main problem/subproblem 表现。
- [Famou-Agent](https://arxiv.org/abs/2510.26144)（[开源代码](https://github.com/baidubce/FM-Agent)）是面向机器学习工程任务的闭环编码与实验代理；在 MLE-bench 语境下更接近“竞赛建模专家 harness”，强调历史经验、实验计划、执行反馈与多轮模型/特征迭代。
- [Kosmos](https://arxiv.org/abs/2511.02824)（开源代码：未找到稳定公开仓库）是面向数据驱动科学发现的长时程 AI scientist；通过结构化 world model 连接文献搜索代理和数据分析代理，可在 12 小时级运行中持续读论文、写代码、生成假设并输出可追踪报告。
- [ArchPilot](https://arxiv.org/abs/2511.03985)（开源代码：未找到稳定公开仓库）是面向 MLE-bench 的多代理机器学习工程框架，在 AIDE、ML-Master 等基线之上强调代理分工、模型方案搜索和实验反馈驱动的架构改进。
- [AgenticSciML](https://arxiv.org/abs/2511.07262)（开源代码：未找到稳定公开仓库）面向科学机器学习发现；由 10+ 专门代理通过结构化辩论、方法记忆和演化搜索共同设计 SciML 架构、损失函数与训练策略。
- InternAgent（[开源代码](https://github.com/InternScience/InternAgent)；无 arXiv 论文）是面向深度科研和 ML 工程任务的开源 agent 系统，在 MLE-bench 上有公开提交；可作为 AIDE / R&D-Agent 之外的实验执行型 harness 参考。
- [Prompt-Free Collaborative Agents for Paper2Code](https://arxiv.org/abs/2512.02812)（[开源代码](https://github.com/going-doer/Paper2Code)）提出了面向 Paper2Code 的无提示协同代理框架。
- [DeepCode](https://arxiv.org/abs/2512.07921)（开源代码：未找到稳定公开仓库）是开放式 agentic coding 系统，在 PaperBench 上与商业 agent 和人类基线对比，代表论文复现/长程代码生成方向的后续工作。
- [ML-Master 2.0 / Cognitive Accumulation](https://arxiv.org/abs/2601.10402)（[开源代码](https://github.com/sjtu-sai-agents/ML-Master)）把 ML-Master 扩展到超长程机器学习工程，强调跨阶段认知积累、经验复用和长时间实验推进。
- [Deep Research](https://arxiv.org/abs/2601.12542)（开源代码：未找到稳定公开仓库）来自 “Rethinking the AI Scientist”；核心是 planner、data analysis、literature search、novelty detection 等专门代理共享 persistent world state，让科学发现从离线批处理转向分钟级交互式循环。
- [Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525)（开源代码：未找到稳定公开仓库）把科研想法生成和真实执行反馈绑定起来；核心思想：让 agent 通过运行实验检验 idea，而不是只生成看起来合理的研究方案。
- [MARS / MARS+](https://arxiv.org/abs/2602.02660)（开源代码：未找到稳定公开仓库）是面向 MLE-bench 的模块化反思搜索 agent；论文把 ML 建模拆成候选方案生成、实验执行、结果反思、分支搜索与 ensemble/refinement 等阶段，属于典型的 test-time search / reflective ML engineering harness。
- [ArchAgent](https://arxiv.org/abs/2602.22425)（开源代码：未找到稳定公开仓库；围绕自动化设计空间搜索构建的计算机体系结构发现 agent 系统；设计关键词：缓存替换策略设计、代码生成、仿真反馈、竞赛式评测）
- [SciDER](https://arxiv.org/abs/2603.01421)（开源代码：未找到稳定公开仓库）是数据中心式端到端科学研究代理；核心思想是从原始实验数据出发，自动完成数据处理、分析、假设形成和报告生成，补足只面向论文或竞赛数据的科研代理。
- [OrchMAS](https://arxiv.org/abs/2603.03005)（开源代码：未找到稳定公开仓库；异构科学专家多 agent 编排框架；设计关键词：双层编排、动态角色与 workflow 适配、模型路由、对中间推理分歧的修订）
- [EvoScientist](https://arxiv.org/abs/2603.08127)（[开源代码](https://github.com/EvoScientist/EvoScientist)）是自进化多代理 AI scientist；用 Researcher Agent、Engineer Agent 与 Evolution Manager Agent，加上 ideation / experimentation 两类持久记忆，让研究策略和代码实验能力随交互历史持续改进。
- [AIRA_2](https://arxiv.org/abs/2603.26499)（开源代码：未找到稳定公开仓库）是 AIRA-dojo 的直接扩展，针对吞吐、评测噪声和固定 operator 三个瓶颈引入异步多 GPU、Hidden Consistent Evaluation 与 ReAct operators，并继续在 MLE-bench-30 上报告长时程结果。
- UniScientist（[官方文章](https://unipat.ai/blog/UniScientist)，[开源代码](https://github.com/UniPat-AI/UniScientist)，[模型](https://huggingface.co/UnipatAI/UniScientist-30B-A3B)；论文待发布）是 UniPat AI 的科学研究智能模型与 agentic inference 框架；核心是 Active Evidence Integration、Model Abduction、Evolving Polymathic Synthesis 和多 rollout 报告聚合。
- [LitPivot](https://arxiv.org/abs/2604.02600)：通过文献语境化与批判来发展研究想法的 research-ideation harness；核心思想是在 agent 修改研究方向时持续引入文献版图，使新颖性和定位成为工作流的一部分，而不是事后检查。
- [Deep Researcher Agent](https://arxiv.org/abs/2604.05854)（[开源代码](https://github.com/Xiangyue-Zhang/auto-deep-researcher-24x7)）是深度研究式 harness 的执行代理，强调多轮检索、证据压缩和结论生成。
- [Toward Autonomous Long-Horizon Engineering for ML Research](https://arxiv.org/abs/2604.13018)（开源代码：未找到稳定公开仓库）提出面向 ML 研究工程的长程 agent 机制，在 PaperBench 与 MLE-Bench Lite 上评测 File-as-Bus 等协作/状态管理设计。
- [AIBuildAI](https://arxiv.org/abs/2604.14455)（[开源代码](https://github.com/aibuildai/AI-Build-AI)）是自动构建 AI 模型的 agent，实现重点是自动读取数据、生成训练与推理代码、持续运行实验并修复提交；论文在 MLE-bench 上报告自动建模结果。
- [EvoMaster](https://arxiv.org/abs/2604.17406)（开源代码：未找到稳定公开仓库）把多代理协作和进化式搜索用于科学问题求解；核心思想：通过假设生成、候选演化与验证反馈，在 FrontierScience 等高难科学推理任务上提升表现。
- [ARA / Agent-Native Research Artifacts](https://arxiv.org/abs/2604.24658)（开源代码：未找到稳定公开仓库）把科研产物从线性论文扩展成可执行、可审计的 agent-native artifact，并在 PaperBench 与 RE-Bench 上报告 review/reproduction workflow 的改进。
- [SciResearcher](https://arxiv.org/abs/2605.01489)（开源代码：未找到稳定公开仓库）扩展 deep research agent 到前沿科学推理，强调多轮证据整合、任务分解与 frontier scientific reasoning benchmark 上的稳定提升。
- [PARNESS](https://arxiv.org/abs/2605.05258)（[开源代码](https://github.com/gtrhythm/PARNESS)）是面向端到端自动科研的 paper harness；通过动态 YAML workflow、全文索引、代码仓库索引和跨运行知识积累，补齐 AI Scientist/AutoSOTA/DeepResearch 类固定流程的刚性问题。
- [BioResearcher](https://arxiv.org/abs/2605.05985)（开源代码：未找到稳定公开仓库）是面向转化医学的 scenario-guided 多代理系统，在 BixBench-Verified-50 等 biomedical benchmark 上评估异质证据综合、多组学分析和可追溯报告生成。
- [DataMaster](https://arxiv.org/abs/2605.10906)（开源代码：未找到稳定公开仓库）是数据中心式自主 AI research agent，在 MLE-Bench Lite 与 PostTrainBench 上评测，把数据发现、清洗、建模和迭代优化作为统一自动研究流程。
- [GEAR](https://arxiv.org/abs/2605.13874)（开源代码：未找到稳定公开仓库）用 genetic AutoResearch 维护多个 research state，把代码、反思与性能轨迹作为 population-based search 的遗传单元，是 AIDE/AIRA/EvoScientist 路线的进化式后续。

## 3.2.4 Skill

- [systematic-literature-review](https://skills.sh/huangwb8/chineseresearchlatex/systematic-literature-review) 适合系统综述。
- [literature-review](https://skills.sh/jackspace/claudeskillz/literature-review) 适合文献筛选与结构化综述。
- [scholar-evaluation](https://skills.sh/jackspace/claudeskillz/scholar-evaluation) 适合学术工作评价与比较。
- [scientific-manuscript-review](https://skills.sh/lyndonkl/claude/scientific-manuscript-review) 适合科研稿件审阅。
- [meta-research](https://github.com/AmberLJC/meta-research) 适合研究问题定义、证据聚合与研究设计梳理。
- [openalex-database](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/scientific/openalex-database) 适合论文元数据检索与作者图谱分析。
- [citation-management](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/scientific/citation-management) 适合引文清洗、核验与 Bib 管理。
- [EvoSkills](https://github.com/EvoScientist/EvoSkills) 是 EvoScientist 的官方科研 skill 库；核心是把 ideation、idea tournament、paper planning 等研究子流程做成可安装知识包，并与长期记忆协同演化。
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)（Codex-native 分发：[academic-research-suite](https://github.com/Imbad0202/academic-research-skills-codex)；skills.sh：[deep-research](https://skills.sh/imbad0202/academic-research-skills/deep-research)、[academic-paper](https://skills.sh/imbad0202/academic-research-skills/academic-paper)、[academic-paper-reviewer](https://skills.sh/imbad0202/academic-research-skills/academic-paper-reviewer)、[academic-pipeline](https://skills.sh/imbad0202/academic-research-skills/academic-pipeline)）覆盖深度研究、系统综述、论文写作、稿件审阅、research-to-paper pipeline 与实验规划，是更完整的通用科研工作流 skill 套件。
- [agent-research-skills](https://github.com/lingzhi227/agent-research-skills) 是覆盖科研论文生命周期的 31-skill 集合，包含文献检索、综述生成、related work 写作、citation/LaTeX 管理、论文审阅、paper-to-code 和 slide generation。
- [paper-to-code](https://github.com/lingzhi227/agent-research-skills/tree/main/skills/paper-to-code) 是贴近 `PaperBench` 的“论文到实现”子技能。
- [implement-paper](https://github.com/marimo-team/skills/tree/main/skills/implement-paper) 面向“论文到交互式 marimo notebook”的实现与讲解，把 paper implementation 从完整复现实验转成可运行、可交互、可教学的最小示例。
- [implement-paper-from-scratch](https://github.com/ghostscientist/skills/tree/main/skills/implement-paper-from-scratch) 是贴近 `PaperBench` 的“从零复现论文”技能。
- [kaggle](https://skills.sh/shepsci/kaggle-skill/kaggle) 适合 Kaggle 竞赛/数据集下载、notebook 与 submission 工作流，是 MLE-bench 这类 Kaggle-derived benchmark 的直接工具层补充。
- [ml-engineer](https://skills.sh/404kidwiz/claude-supercode-skills/ml-engineer) 适合把通用机器学习建模流程显式化，包括 EDA、特征工程、模型训练、评估与调参，可作为 MLE-bench/AIDE 类 agent 的领域先验 skill。
- [automl-pipeline-setup](https://skills.sh/dengineproblem/agents-monorepo/automl-pipeline-setup) 适合快速搭建 AutoML/训练流水线，把数据读取、候选模型、验证指标和输出文件标准化。
- [machine-learning-expert](https://github.com/luokai0/ai-agent-skills-by-luo-kai) 适合 scikit-learn、XGBoost、交叉验证、特征工程与模型评估的专家化建模流程，适合作为 tabular 类 MLE-bench 题目的轻量 skill。
- [scikit-learn](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/scientific/scikit-learn) 适合把 preprocessing、pipeline、交叉验证和指标计算写成可复用代码模板，尤其适合 MLE-bench 中大量表格/文本 baseline。
- [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)（skill 集合仓库）包含 literature-review、citation-management、openalex-database 等科研子技能，可作为 MLR-Bench / PaperBench 类任务的通用工具箱。
- [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)（skill 集合仓库）覆盖文献综述、科学写作、假设生成、统计分析等模块，适合作为科研任务的 skill 库底座。
- [open-science-skills](https://github.com/justaddcoffee/open-science-skills)（skill 集合仓库）更偏学科先验与分析策略注入，覆盖 genomics、metabolomics、structural biology、data science 等领域。
- [scientific-research-skills](https://github.com/jxtse/scientific-research-skills)（skill 集合仓库）提供 literature-search、paper-reading、paper-fulltext-harvest、related-work-survey、Zotero 管理和社媒论文线索 triage，适合补足论文发现、全文获取和资料管理环节。
- [research-pipeline-runner](https://github.com/WILLOSCAR/research-units-pipeline-skills/tree/main/.codex/skills/research-pipeline-runner)（skill）以 `UNITS.csv` 与 checkpoint 驱动 survey / systematic review / tutorial / peer review 的端到端执行。
- [cailmdaley/skills](https://github.com/cailmdaley/skills)（skill 集合仓库）包含 bibliography management、scientific visualization、autonomous iteration 等科研工具链模块。
