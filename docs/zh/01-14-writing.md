# 1.14 写作与长文生成

> 上级章节：1. 基础能力

说明：写作与 DeepResearch 有重叠，但评测目标不同。写作类任务主要看在给定主题、材料、风格、结构、长度和受众约束下，能否产出高质量文本；核心失败模式是跑题、结构失控、风格不一致、冗余、叙事/论证不连贯和不满足格式/长度约束。DeepResearch 则主要看开放信息获取、来源筛选、证据支撑、引用一致性和多源综合，写作只是它的最后表达阶段。因此这里保留为独立基础能力；凡是“先搜证据再写报告”的工作，优先放在 [2.4 深度研究](02-04-deep-research.zh.md)，本节只交叉记录对写作质量、长文结构或成稿流程有直接贡献的代表性工作。

## 1.14.1 Leaderboard

- [EQ-Bench Creative Writing](https://eqbench.com/creative_writing.html)：社区维护的创意写作榜单，偏主观文本质量、风格和叙事表现；适合补充 WritingBench 这类 rubric 驱动评测对文学/创作类文本的覆盖。
- [LLM Stats Best AI for Writing](https://llm-stats.com/leaderboards/best-ai-for-writing)：第三方持续汇总写作相关模型表现、速度和价格，适合快速观察通用模型在写作场景中的产品化排序；引用时应把它视为聚合榜单而非单一论文 benchmark。
- [WritingBench](https://github.com/X-PLUG/WritingBench)：官方仓库维护模型评测脚本、榜单线索和任务定义，适合追踪真实写作需求下的模型表现。
- [Arena-Write](https://huggingface.co/datasets/THU-KEG/Arena-Write)：LongWriter-Zero 配套的 pairwise/Elo 写作评测集，适合观察超长输出模型在真实写作 prompt 上的偏好排序。

## 1.14.2 Bench

- [P2P](https://arxiv.org/abs/2505.17104)：评测自动论文到海报生成。核心思想：把研究论文转化为结构化 poster，并细粒度评价内容选择、版式组织和图文摘要的忠实性。
- [CreativityPrism](https://arxiv.org/abs/2510.20091)：评测 LLM 在发散思维、创意写作和逻辑推理中的创造力。核心思想：把质量、新颖性和多样性拆开衡量，避免把创意写作能力和其他创造性生成能力混在一起。
- [EQ-Bench Creative Writing](https://eqbench.com/creative_writing.html)：评什么：创意写作与长篇风格化文本的主观质量。核心思想：用开放写作 prompt 和社区榜单持续比较模型在文学性、表达、叙事节奏和风格控制上的差异，适合作为学术 benchmark 之外的产品化参考。
- [Suri](https://arxiv.org/abs/2406.19371)（[开源代码](https://github.com/chtmp223/suri)）：评什么：长文生成中的多约束指令遵循。核心思想：把长文任务里的主题、格式、长度、风格和内容约束拆成可检查维度，专门测试模型能否在长输出中持续满足多个细粒度要求。
- [LongWriter / LongBench-Write](https://arxiv.org/abs/2408.07055)（[开源代码](https://github.com/THUDM/LongWriter)）：评什么：1 万词级长文本生成与长度扩展能力。核心思想：通过 LongWrite-Ruler 与 LongBench-Write 暴露模型“能读长上下文”并不等于“能稳定写长输出”，尤其关注长度控制、结构延展和中后段退化。
- [LongGenBench](https://arxiv.org/abs/2409.02076)：评什么：长上下文 LLM 的长文生成。核心思想：用更长输入、更长输出和多维质量评价，把摘要式短输出与真正的长文成稿区分开。
- [HelloBench](https://arxiv.org/abs/2409.16191)：评什么：LLM 长文本生成能力。核心思想：围绕长输出场景构造多类型 prompt 与评价协议，观察模型在长篇连贯性、重复、结构稳定性和指令满足上的系统退化。
- [LongProc](https://arxiv.org/abs/2501.05414)（[开源代码](https://github.com/princeton-pli/LongProc)）：评什么：长过程性文本生成。核心思想：要求模型生成食谱、教程、工作流、说明书等过程性长文，评估步骤顺序、依赖一致性、完整性和可执行性，而不是只看单段语言流畅度。
- [WritingBench](https://arxiv.org/abs/2503.05244)（[开源代码](https://github.com/X-PLUG/WritingBench)）：评什么：生成式写作能力，覆盖 6 个核心写作领域和 100 个子领域。核心思想：把写作任务拆成与查询相关的评价标准，用更贴近真实需求的 prompt、rubric 和评审协议衡量模型是否能写出符合目的、风格、结构和内容约束的长文。
- [WebNovelBench](https://arxiv.org/abs/2505.14818)：评什么：网络小说式长篇叙事写作。核心思想：把 LLM 生成小说放到真实 web novel 分布中比较，关注人物、情节、叙事节奏、章节延续和读者偏好，而不是只评短故事片段。
- [UNCLE](https://arxiv.org/abs/2505.16922)：评什么：长文生成中的不确定性表达。核心思想：专门检查模型是否能在长文里用合适、校准的语言表达不确定性，避免在开放写作中把模糊信息写成过度确定的断言。
- [ExpertLongBench](https://arxiv.org/abs/2506.01241)：评什么：专家级长文生成任务。核心思想：用结构化 checklist 评审专业长文，强调任务特定要求、可核验子标准和长文整体质量，减少只靠单一总分 judge 的不稳定性。
- [Arena-Write](https://arxiv.org/abs/2506.18841)（[数据集](https://huggingface.co/datasets/THU-KEG/Arena-Write)）：评什么：真实写作 prompt 下的 pairwise 偏好与 Elo 排名。核心思想：把长文写作结果放进 arena-style 比较，补足单一 rubric critic 难以捕捉整体偏好的问题。
- [LitBench](https://arxiv.org/abs/2507.00769)：评什么：基于人工标注故事对比的创意写作自动评测可靠性。核心思想：提供标准化偏好 benchmark 和配对数据集，用来测试 LLM judge 与 reward model 对文学生成质量的判断。
- [LongWeave](https://arxiv.org/abs/2510.24345)：评什么：真实相关且可验证的长文生成。核心思想：让长文任务既贴近真实写作需求，又能通过引用、事实和结构化约束进行核验，连接写作质量与可验证性。
- [PaperWritingBench](https://arxiv.org/abs/2604.05018)：评什么：AI research paper 写作。核心思想：把摘要、引言、相关工作、方法、实验叙述等论文写作环节组织成可评测任务，检查学术写作的结构、论证、引用上下文和段落质量。
- [HoWToBench](https://arxiv.org/abs/2604.19071)：评什么：人类水平写作能力。核心思想：提出 Tree of Writing，将写作拆成意图理解、素材组织、结构规划、局部段落生成、全局修订等节点，做更细粒度的写作过程评测。

## 1.14.3 Agent Harness

- [Self-Refine](https://arxiv.org/abs/2303.17651)（[开源代码](https://github.com/madaan/self-refine)）：`生成 -> 反馈 -> 修订` 的通用写作修订 loop；适合把一次性写作改造成可审稿、可迭代的长文生成流程。
- [Weaver](https://arxiv.org/abs/2401.17268)（开源代码：未找到稳定公开仓库）：创意写作 foundation model 与写作流程参考；虽然更偏模型工作，但它系统化处理设定、情节和叙事风格，是后续创意写作 agent 评测的重要基线。
- [STORM](https://arxiv.org/abs/2402.14207)（[开源代码](https://github.com/stanford-oval/storm)）：面向长篇百科式写作的 `检索 -> 多视角提问 -> 大纲 -> 成稿` harness；更接近报告/综述型长文生成而不是单轮作文。
- [LongWriter](https://arxiv.org/abs/2408.07055)（[开源代码](https://github.com/THUDM/LongWriter)）：长文本生成与扩展写作框架；核心思想是把超长输出拆成可控扩展和分段生成过程，适合作为长文输出稳定性的工程参考。
- [Heterogeneous Recursive Planning](https://arxiv.org/abs/2503.08275)（开源代码：未找到稳定公开仓库）：自适应长文写作规划 harness；核心思想：不只生成一次性大纲，而是递归拆分不同粒度的写作单元，并在生成过程中按内容需要调整规划深度。
- [Writing-Zero](https://arxiv.org/abs/2506.00103)（[开源代码](https://github.com/damoonsh/writing-zero)）：把非可验证写作任务转成可优化的 reward 流程；核心思想是用过程化反馈和可检查约束缩小主观写作质量与可训练信号之间的距离。
- [StoryWriter](https://arxiv.org/abs/2506.16445)（开源代码：未找到稳定公开仓库）：长篇故事生成多代理框架；核心思想：把角色设定、情节规划、章节写作和一致性检查拆给不同 agent，减少长故事中的人物漂移和情节断裂。
- [LongWriter-Zero](https://arxiv.org/abs/2506.18841)（开源代码：未找到稳定公开仓库；[数据集](https://huggingface.co/datasets/THU-KEG/Arena-Write)）：面向超长写作的 RL 框架；核心思想是用 `think before writing`、长度/质量 reward 和 Arena-Write 评测，让模型在 1 万词级输出中保持结构和连贯性。
- [ACE-RL](https://arxiv.org/abs/2509.04903)（开源代码：未找到稳定公开仓库）：WritingBench 引文网络中的代表性后续工作；核心思想：自动把写作指令分解为细粒度约束，并用约束满足度作为长文生成 RL reward，属于训练型写作系统而非纯交互式 agent。
- [HiFlow](https://arxiv.org/abs/2603.04996)（开源代码：未找到稳定公开仓库）：约束长文生成的层级反馈优化框架；核心思想：按全局结构、段落质量和局部约束分层反馈，迭代修复长文中的约束遗漏和结构失衡。
- [PaperOrchestra](https://arxiv.org/abs/2604.05018)（开源代码：未找到稳定公开仓库）：自动 AI 研究论文写作的多代理框架；核心思想：把论文写作拆成 topic/context 分析、section drafting、交叉审阅和整体修订，对应 PaperWritingBench 的学术写作任务。

## 1.14.4 Skill

- [academic-paper](https://skills.sh/imbad0202/academic-research-skills/academic-paper) 适合论文写作、结构化段落组织与学术表达。
- [scientific-manuscript-review](https://skills.sh/lyndonkl/claude/scientific-manuscript-review) 适合在成稿后做审稿式质量检查。
- [literature-review](https://skills.sh/davila7/claude-code-templates/literature-review) 适合把长文写作前的资料筛选、证据表和引用管理固化成流程。
- [writing-plans](https://skills.sh/obra/superpowers/writing-plans) 适合把长文写作拆成选题、结构、段落目标和修订计划。
- [writing-skills](https://skills.sh/obra/superpowers/writing-skills) 适合通用写作流程、段落打磨和成稿修订。
- [story-architecture](https://skills.sh/haowjy/creative-writing-skills/story-architecture) 适合故事结构、角色关系和章节化叙事规划。
- [cw-prose-writing](https://skills.sh/haowjy/creative-writing-skills/cw-prose-writing) 适合创意写作中的句段风格、语气和描写质量控制。
