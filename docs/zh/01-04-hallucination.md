# 1.4 幻觉

> 上级章节：1. 基础能力


## 1.4.1 Leaderboard

- [Hallucinations Leaderboard](https://huggingface.co/spaces/hallucinations-leaderboard/leaderboard)：早期开放幻觉榜单尝试；价值在于把 TruthfulQA、HaluEval、FEVER 等信号聚合到统一比较入口。
- [LLM-AggreFact Leaderboard](https://llm-aggrefact.github.io/)：grounded factuality verifier 榜单；价值在于把多源 factual consistency 数据统一成可比较评测集，并连接 MiniCheck 等可运行检测器。
- [Vectara Hallucination Evaluation Leaderboard](https://huggingface.co/spaces/vectara/Hallucination-evaluation-leaderboard)：面向摘要/RAG 场景的公开幻觉榜单；价值在于持续比较回答是否由输入事实支撑，并提供 HHEM/FaithJudge 等自动评测器线索。
- [Google DeepMind Eval Suite 中的 FACTS 入口](https://deepmind.google/research/evals/)：FACTS 事实性评测的公开入口；价值在于把 grounded、search、parametric 和 multimodal factuality 等设置组织为可比较、可提交、可复核的评测轨道。

## 1.4.2 Bench

- [FEVER](https://arxiv.org/abs/1803.05355)：评测基于证据的事实核查与声明验证；核心思想是把 claim、Wikipedia 证据句和 supports/refutes/not-enough-info 标签组织成可检索、可判定的事实性任务，也是早期 Hallucinations Leaderboard 聚合信号之一。
- [TruthfulQA](https://arxiv.org/abs/2109.07958)（数据集：[truthfulqa/truthful_qa](https://huggingface.co/datasets/truthfulqa/truthful_qa)）：评测模型在常见迷思问题上的“真实而非迎合”回答；核心思想是把问题设计成“最常见的错误答案更诱人”，以暴露幻觉与胡编倾向。
- [HaluEval](https://arxiv.org/abs/2305.11747)：评测 LLM 识别和生成幻觉的能力；核心思想是通过采样后过滤构造大规模 hallucinated samples，并结合人工标注检查模型能否发现与来源或事实知识冲突的内容。
- [FActScore](https://arxiv.org/abs/2305.14251)（[开源代码](https://github.com/shmsw25/FActScore)）：评测长篇回答的原子事实正确性；核心思想是 `原子事实切分 -> 逐条判定 -> 聚合打分`，并将“可核验性”从主观评价中分离出来。
- [FELM](https://arxiv.org/abs/2310.00741)：评测 factuality evaluator 本身；核心思想是对 LLM 输出做细粒度片段级事实标注，并覆盖世界知识、数学、推理等多类错误，而不只看百科事实。
- [RAGTruth](https://arxiv.org/abs/2401.00396)（[开源代码](https://github.com/ParticleMedia/RAGTruth)）：评测 RAG 场景中的词级幻觉；核心思想是收集近 18,000 条 RAG 生成回答并做人工标注，区分 unsupported 与 contradictory claims，专门服务于 RAG 幻觉检测与缓解。
- [LongFact](https://arxiv.org/abs/2403.18802)（[开源代码](https://github.com/google-deepmind/long-form-factuality)）：评测长篇生成的事实性与可证据支撑程度；核心思想是把回答拆成可核验的 atomic claims，并用搜索增强的判定协议统计整体 factuality（论文中也包含 LongFact-Objects/Concepts 等设置）。
- [LLM-AggreFact](https://arxiv.org/abs/2404.10774)（[开源代码](https://github.com/Liyan06/MiniCheck)）：评测 grounded factuality verifier；核心思想是聚合多源事实一致性数据，统一比较检测器在有参考文档场景下判断回答是否被证据支撑的能力。
- [FACTS Grounding](https://arxiv.org/abs/2501.03200)：评测长文本回答是否被给定证据充分支撑；核心思想是用公开榜单和人工偏好校准的协议比较模型的 grounded factuality，后续扩展到更广义 FACTS factuality leaderboard。
- [HLE-Verified](https://arxiv.org/abs/2501.14249)（数据集：[lmms-lab/HLE-Verified](https://huggingface.co/datasets/lmms-lab/HLE-Verified)）：高难知识问答的人工审核可验证子集；核心思想是通过筛题与核验提升“可判定性”，更适合做可靠性/事实性压力测试。
- [HalluVerse25](https://arxiv.org/abs/2503.07833)：评测细粒度多语言幻觉检测；核心思想是在英语、阿拉伯语和土耳其语中标注实体、关系和句子级幻觉，避免只看英语事实问答。
- [HalluLens](https://arxiv.org/abs/2504.17550)（[开源代码](https://github.com/facebookresearch/HalluLens)）：统一评测 intrinsic/extrinsic hallucination；核心思想是先澄清幻觉与 factuality 的边界，再用可动态生成的 extrinsic 测试减少数据泄漏与饱和。
- [HalluMix](https://arxiv.org/abs/2505.00506)（数据集：[quotientai/HalluMix](https://huggingface.co/datasets/quotientai/HalluMix)）：评测真实多域、长短上下文下的 hallucination detection；核心思想是覆盖 RAG 场景中的多文档与整句输出，检查检测器在任务和上下文长度变化下是否稳健。
- [MultiHal](https://arxiv.org/abs/2505.14101)：评测知识图谱支撑的多语言多跳幻觉；核心思想是从开放知识图谱中构造高质量 KG 路径，让生成式评测同时检查事实关系、跨语言表达和图结构证据对齐。
- [PhD](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_PhD_A_ChatGPT-Prompted_Visual_Hallucination_Evaluation_Dataset_CVPR_2025_paper.html)：评测 MLLM 的视觉幻觉。核心思想：用 ChatGPT 提示生成的图像问题样例，检查多模态模型是否回答出无视觉支撑的物体、属性或关系。
- [ODE](https://openaccess.thecvf.com/content/CVPR2025/html/Tu_ODE_Open-Set_Evaluation_of_Hallucinations_in_Multimodal_Large_Language_Models_CVPR_2025_paper.html)：评测 MLLM 的开放集幻觉。核心思想：把物体与属性存在性测试做得更动态，避免视觉幻觉诊断过度绑定固定闭集标签空间。
- [AbstentionBench](https://arxiv.org/abs/2506.09038)：评测模型面对不可回答问题时是否会拒绝而非胡编；核心思想是覆盖未知答案、信息不足、错误前提、主观解释和过时信息等 20 类数据来源，把“知道何时不答”作为幻觉风险的一部分。
- [FACTORY](https://arxiv.org/abs/2508.00109)：评测长篇事实性生成；核心思想是用人工核验的、可回答且无歧义的事实寻求提示，暴露模型在长尾事实和长回答原子声明上的不可靠性。
- [SimpleQA Verified](https://arxiv.org/abs/2509.07968)：评测短事实问答的正确性与幻觉率；核心思想是用低歧义问题集与严格核验协议降低判读噪声。
- [AuthenHallu](https://arxiv.org/abs/2510.10539)：评测真实 LLM-human 交互中的幻觉检测；核心思想是从真实对话中标注幻觉，而不是合成诱导样本。
- [CAP](https://arxiv.org/abs/2510.22395)：评测科学文本生成中的多语言幻觉检测；核心思想是基于 ACL 论文构造 900 个科学问题和 7,000 多个模型回答，并给出科学事实错误与语言流畅性标注。
- [MMM-Fact](https://arxiv.org/abs/2510.25120)：评估不同检索难度下的多模态、多领域事实核查。核心思想：测试模型能否把事实性声明 grounding 到检索到的多模态证据中，而不是依赖无支撑生成。
- [Vectara Hallucination Evaluation](https://huggingface.co/spaces/vectara/Hallucination-evaluation-leaderboard)：评测摘要/RAG 场景中生成内容是否忠实于输入事实；核心思想是把真实文档摘要和自动 factuality judge 接成公开榜单协议，适合跟踪 HHEM、FaithJudge 等检测器。

## 1.4.3 Agent Harness

- [RARR](https://arxiv.org/abs/2210.08726)（[开源代码](https://github.com/anthonywchen/RARR)）：retrieval-backed hallucination repair；典型闭环为 `声明切分 -> 检索证据 -> 证据过滤/对齐 -> 回填修订`。
- [SelfCheckGPT](https://arxiv.org/abs/2303.08896)（[开源代码](https://github.com/potsawee/selfcheckgpt)）：通过自一致性与变体采样检测可疑声明；核心思想是把“不一致”作为 hallucination 风险信号。
- [FacTool](https://arxiv.org/abs/2307.13528)（[开源代码](https://github.com/GAIR-NLP/factool)）：工具增强事实性检测框架；核心思想是把 QA、代码、数学和科学文献综述等任务中的生成内容拆解为可查证单元，再调用外部工具与证据判断 factual errors。
- [Chain-of-Verification](https://arxiv.org/abs/2309.11495)：把复杂回答拆成待核验子声明并逐条验证；核心思想是把核验控制流显式化，降低“整体看起来合理但细节胡说”。
- [SAFE](https://arxiv.org/abs/2403.18802)（[开源代码](https://github.com/google-deepmind/long-form-factuality)）：搜索增强事实性评测 harness；核心思想是把长回答拆成 atomic claims，再用检索证据逐条判断是否被支撑。
- [MiniCheck](https://arxiv.org/abs/2404.10774)（[开源代码](https://github.com/Liyan06/MiniCheck)）：轻量 grounded factuality verifier；核心思想是在 LLM-AggreFact 上训练/评测小型检测器，用较低成本判断回答与参考文档是否一致。
- [RefChecker](https://arxiv.org/abs/2405.14486)（[开源代码](https://github.com/amazon-science/RefChecker)）：reference-based 细粒度幻觉检查器；核心思想是把回答拆成可核验片段并与参考证据对齐，输出 span/claim 级 hallucination 判断。
- [RAGChecker](https://arxiv.org/abs/2408.08067)（[开源代码](https://github.com/amazon-science/RAGChecker)）：RAG 系统诊断式评测框架；核心思想是从 claim-level 支撑、遗漏和噪声定位检索端与生成端的事实性错误。
- [SelfCheckAgent](https://arxiv.org/abs/2502.01812)：多 agent 零资源幻觉检测框架；核心思想是组合 symbolic、specialized detection 与 contextual consistency agents，用多维一致性信号判断生成内容是否可靠。
- [REFIND](https://arxiv.org/abs/2502.13622)（[开源代码](https://github.com/oneonlee/REFIND)）：retrieval-augmented factuality hallucination detection；核心思想是用检索文档与 context sensitivity ratio 定位幻觉 span，并在多语言设置中验证鲁棒性。
- [FactSelfCheck](https://arxiv.org/abs/2503.17229)：基于 fact triple 的黑盒幻觉检测；核心思想是把回答拆成细粒度事实后做多轮一致性检查。
- [Premise Verification](https://arxiv.org/abs/2504.06438)：面向 false-premise query 的检索增强逻辑验证框架；核心思想是在生成前把用户问题转成逻辑前提并逐条查证，提前阻断“顺着错误前提胡编”的幻觉链路。
- [FaithJudge](https://arxiv.org/abs/2505.04847)（[开源代码](https://github.com/vectara/FaithJudge)）：面向 factual faithfulness 的自动 judge；核心思想是用可复用评测器判断生成内容是否忠实于给定证据，并服务于 Vectara 幻觉榜单的后续版本。

## 1.4.4 Skill

- [fact-checker](https://skills.sh/shubhamsaboo/awesome-llm-apps/fact-checker) 适合事实核查与证据追踪。
- [fact-checker](https://skills.sh/daymade/claude-code-skills/fact-checker) 更偏“报告式核查结果”。
- [fact-check](https://github.com/openclaw/skills/tree/main/skills/webguhui/fact-check) 可把任意声明转成交叉比对流程。
- [clarity-gate](https://github.com/openclaw/skills/tree/main/skills/frmoretto/clarity-gate) 会显式标注“缺不确定性标记”“可核验声明未核验”等风险。
- [citation-validator](https://skills.sh/liangdabiao/claude-code-stock-deep-research-agent/citation-validator) 适合在带引文输出中拦截“来源看似存在但不支持结论”的情况。
