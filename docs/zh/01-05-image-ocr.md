# 1.5 图像（含 OCR）

> 上级章节：1. 基础能力


## 1.5.1 Leaderboard

- [DocVQA Challenge](https://www.docvqa.org/challenges)：持续榜单：文档视觉问答的经典公开挑战；适合跟踪 OCR、版面理解与答案抽取在真实文档问答上的长期进展。
- [Vision Arena](https://huggingface.co/spaces/WildVision/vision-arena)：持续榜单：开放式图像对话模型的 pairwise battle；适合补充传统准确率榜单之外的人类偏好/开放问答比较。
- [OCRBench v2 Leaderboard](https://www.codesota.com/ocr/benchmark/ocrbench-v2)：持续榜单：围绕 OCRBench v2 聚合 text-rich image、文档、图表和 OCR-to-reasoning 结果；适合快速追踪新 VLM 在“读文字并推理”链路上的位置。
- [OmniDocBench Leaderboard](https://github.com/opendatalab/OmniDocBench#leaderboard)：持续榜单：文档解析 pipeline 的版面、表格、段落和结构化指标；适合比较 OCR-free/OCR-based parser 与端到端文档模型。
- [IDP Leaderboard](https://idp-leaderboard.org/)：持续榜单：企业文档 AI 模型的 OCR、表格抽取、KIE、VQA、分类与长文档处理；适合作为“文档智能”工程侧综合榜单。
- [OCR Arena](https://www.ocrarena.ai/)：持续榜单：OCR/文档模型的竞技场式比较；适合发现可复用的文档解析、表格抽取和视觉问答模型配置。

## 1.5.2 Bench

（以下按发布时间排序，覆盖 OCR、文档理解、图表理解、通用 VQA 与诊断、STEM/理科图推理、视觉 agent/tool-use 评测等子任务。）

- [DocVQA](https://arxiv.org/abs/2007.00398)（[挑战页](https://www.docvqa.org/challenges)）：评什么：文档图像上的视觉问答、表格理解与信息抽取。核心思想：把真实扫描/拍照文档中的 OCR、版面结构和答案定位放进统一挑战协议，是 DocVQA Challenge 榜单对应的核心 benchmark。
- [FSC-147](https://arxiv.org/abs/2105.08386)：评什么：few-shot counting（给少量标注示例后在新图像上计数）；核心思想：用小样本设定检验计数泛化能力，常作为“计数”子能力的经典参考。
- `CountBench`（见 [Teaching CLIP to Count to Ten](https://arxiv.org/abs/2302.12066)；[数据集](https://huggingface.co/datasets/vikhyatk/CountBenchQA)）：评什么：视觉计数与数量概念可靠性；核心思想：用“数得准不准”诊断视觉基础能力与偏置（常与 VQA/偏差诊断结合使用）。
- [HallusionBench](https://arxiv.org/abs/2310.14566)（[开源代码](https://github.com/tianyi-lab/HallusionBench)；[数据集](https://huggingface.co/datasets/lmms-lab/HallusionBench)）：评什么：视觉幻觉与视觉错觉驱动的错误；核心思想：用可控视觉错觉与图像-上下文推理题诊断“看图胡说”的具体类型。
- [MMMU](https://arxiv.org/abs/2311.16502)（[主页/榜单](https://mmmu-benchmark.github.io/#leaderboard)；[数据集](https://huggingface.co/datasets/MMMU/MMMU)；[评测代码](https://github.com/MMMU-Benchmark/MMMU)）：评什么：多学科多模态理解与推理；核心思想：用跨学科题型与统一评分协议，衡量“看图 + 读题 + 推理”一体化能力。
- [MMStar](https://arxiv.org/abs/2403.20330)（[项目页](https://mmstar-benchmark.github.io/)；[开源代码](https://github.com/MMStar-Benchmark/MMStar)；[数据集](https://huggingface.co/datasets/Lin-Chen/MMStar)）：评什么：vision-indispensable 的综合多模态评测；核心思想：用多维子能力轴与“多模态增益/泄漏”等分析指标，衡量模型是否真正利用视觉输入。
- [Vibe-Eval](https://arxiv.org/abs/2405.02287)（[开源代码](https://github.com/reka-ai/reka-vibe-eval)）：评什么：多模态模型在多维任务上的综合能力；核心思想：用更接近人类主观偏好的标注与评分协议，提供覆盖面更广的综合评测套件。
- [MTVQA](https://arxiv.org/abs/2405.11985)（[项目页](https://mtvqa.github.io/)；[开源代码](https://github.com/bytedance/MTVQA)）：评什么：多语言“文本中心”视觉问答（读图中文字并理解）；核心思想：覆盖多语言与低资源语言，强调文字感知与跨语言理解的一体化评测。
- [MuirBench](https://arxiv.org/abs/2406.09411)（[项目页](https://muirbench.github.io/)；[开源代码](https://github.com/muirbench/MuirBench)；[数据集](https://huggingface.co/datasets/muirbench/MuirBench)）：评什么：多图输入下的鲁棒 multi-image understanding；核心思想：把多图任务拆成一组稳健性/一致性子任务，专门检验跨图对齐与抗干扰能力。
- [Vision Arena](https://huggingface.co/spaces/WildVision/vision-arena)：评什么：开放式图像对话模型的人类偏好/竞技场式比较。核心思想：用 pairwise battle 补充固定 VQA/OCR 题集，适合观察真实开放图像问答中的模型偏好排序。
- [CharXiv](https://arxiv.org/abs/2406.18521)（[项目页](https://princeton-nlp.github.io/CharXiv/)；[数据集](https://huggingface.co/datasets/princeton-nlp/CharXiv)）：评什么：科研论文场景的图表/插图与图文对齐理解；核心思想：把“图-文证据对齐”做成可量化问答。
- [VLMs are Blind](https://arxiv.org/abs/2407.06581)（[项目页](https://vlmsareblind.github.io/)）：评什么：VLM 在极简单视觉原语任务上的可靠性；核心思想：用人类几乎无难度的几何/空间/计数小测试，诊断模型是否真的“看见”关键证据。
- [MMMU-Pro](https://arxiv.org/abs/2409.02813)（[主页/榜单](https://mmmu-benchmark.github.io/#leaderboard)；[数据集](https://huggingface.co/datasets/MMMU/MMMU_Pro)；[评测代码](https://github.com/MMMU-Benchmark/MMMU)）：评什么：更强“必须看图”的多模态 STEM；核心思想：把题面文本嵌入图像、过滤可纯文本作答题，并增强迷惑性选项，使评测更依赖视觉输入与推理链路。
- [OmniDocBench 1.5](https://arxiv.org/abs/2412.07626)（[开源代码](https://github.com/opendatalab/OmniDocBench)；[数据集](https://huggingface.co/datasets/opendatalab/OmniDocBench)）：评什么：文档解析的模块化能力（版面、段落、表格、结构等）；核心思想：用模块化指标与工程化 runtime（如 hybrid matching、CDM、Docker 化）把“文档解析能力”拆解可测。
- [OCRBench v2](https://arxiv.org/abs/2501.00321)（[评测实现汇总](https://github.com/Yuliang-Liu/MultimodalOCR)）：评什么：多模态 OCR（读图中文字并完成理解/推理）；核心思想：把 OCR 与下游推理耦合，区分“读不到”和“读到了但不会用”。
- [EMMA](https://arxiv.org/abs/2501.05444)（[主页/榜单](https://emma-benchmark.github.io/)；[数据集](https://huggingface.co/datasets/luckychao/EMMA-mini)；[开源代码](https://github.com/EMMA-Bench/EMMA)）：评什么：跨数学/物理/化学/编码的“有机多模态推理”；核心思想：构造必须跨模态串联证据的题型，并提供生成与评测脚本以复现比较。
- [RealWorldQA](https://huggingface.co/datasets/xai-org/RealworldQA)：评什么：真实世界场景图像上的问答正确性；核心思想：用真实环境图像与可直接核验的简短问答，减少合成数据分布与模板化题型带来的高估。
- [SimpleVQA](https://arxiv.org/abs/2502.13059)（[开源代码](https://github.com/SimpleVQA/SimpleVQA)）：评什么：多模态事实性（factuality）与“图像是否真正被使用”；核心思想：通过简单但严格的 VQA 协议，识别模型是否依赖语言先验而非视觉证据。
- [IDP Leaderboard](https://idp-leaderboard.org/)：评什么：企业智能文档处理中的 OCR、表格抽取、KIE、VQA、分类与长文档处理。核心思想：把 document AI 工程侧常见任务组织成公开榜单式评测入口，补齐学术 DocVQA/OCRBench 对真实业务文档覆盖不足的问题。
- [VisFactor](https://arxiv.org/abs/2502.16435)（[开源代码](https://github.com/CUHK-ARISE/VisFactor)）：评什么：多模态模型的基础视觉认知（偏“视觉原语”）；核心思想：把基础视觉子能力系统化拆分为可控子测，降低语言投机空间。
- [XLRS-Bench](https://arxiv.org/abs/2503.23771)（[项目页](https://xlrs-bench.github.io/home_page.html)；[开源代码](https://github.com/AI9Stars/XLRS-Bench)）：评什么：超大分辨率遥感图像的感知与推理；核心思想：用超高分辨率、遥感 domain 语义与跨尺度细粒度任务挑战通用 VLM。
- [ChartQAPro](https://arxiv.org/abs/2504.05506)（[开源代码](https://github.com/vis-nlp/ChartQAPro)；[数据集](https://huggingface.co/datasets/ahmed-masry/ChartQAPro)）：评什么：图表理解与图表问答；核心思想：覆盖多样图表类型并提高推理占比，配套可复现评测脚本。
- [Omni-Chart-600K](https://doi.org/10.18653/v1/2025.findings-naacl.226)：评估多类型图表理解能力。核心思想：扩大图表类型覆盖，使文档模型和视觉语言模型不只在常见柱状图、折线图和饼图上测试。
- [PointArena（PointBench）](https://arxiv.org/abs/2505.09990)（[开源代码](https://github.com/pointarena/pointarena)）：评什么：pointing/指向定位能力（在图上点选/定位目标或区域）；核心思想：把 grounding 从文本变成可度量的空间输出，定位误差可直接评估。
- [WildDoc](https://arxiv.org/abs/2505.11015)：评什么：真实野外文档理解的全面性与鲁棒性；核心思想：从 OCRBench v2 后续引用链补足更接近真实采集噪声、复杂版面和多任务文档理解的压力测试。
- [ViC-Bench](https://arxiv.org/abs/2505.14404)：评估 MLLM 的视觉交织式思维链能力。核心思路是允许模型生成自由形式的中间视觉状态，并检验这些状态是否支撑忠实的逐步多模态推理。
- [OCR Arena](https://www.ocrarena.ai/)：评什么：OCR/文档模型的竞技场式比较。核心思想：把 OCR、文档解析、表格抽取和视觉问答模型放进持续公开比较入口，作为 OCRBench、OmniDocBench 与 IDP Leaderboard 之外的实用补充。
- [PhyX](https://arxiv.org/abs/2505.15929)（[项目页](https://phyx-bench.github.io/)；[数据集](https://huggingface.co/datasets/Cloudriver/PhyX)；[开源代码](https://github.com/killthefullmoon/PhyX)）：评什么：视觉场景下的物理推理；核心思想：以真实高保真视觉情境承载大学水平物理题，并提供多版本输入（如 Text-DeRedundancy）与评测脚本减少“读题冗余”带来的偏置。
- [MMDocRAG](https://arxiv.org/abs/2505.16470)（[项目页](https://mmdocrag.github.io/MMDocRAG/)；[开源代码](https://github.com/MMDocRAG/MMDocRAG)）：评什么：多页、多证据链的文档问答与多模态 RAG；核心思想：同时评估检索、证据选择和“文本 + 图像证据”整合，避免只测文本化 DocQA。
- [OCR-Reasoning Benchmark](https://arxiv.org/abs/2505.17163)：评什么：复杂 text-rich image reasoning；核心思想：把 OCR 读取得分与读后推理明确拆开，测试模型能否在密集文字、表格和图像证据上完成组合推理。
- [InfoChartQA](https://arxiv.org/abs/2505.19028)：评什么：信息图风格图表的多模态问答；核心思想：从 ChartQAPro 引用链补足 infographic chart 场景，覆盖更强版式变化、文本说明和图表语义融合。
- [VLMs are Biased](https://arxiv.org/abs/2505.23941)（[项目页](https://vlmsarebiased.github.io/)；[开源代码](https://github.com/anvo25/vlms-are-biased)）：评什么：VLM 的视觉偏置与“记忆替代看图”的失败模式；核心思想：用客观计数/对照构造揭示模型被熟悉对象先验牵引而忽视真实像素证据。
- [Agent-X](https://arxiv.org/abs/2505.24876)（[开源代码](https://github.com/mbzuai-oryx/Agent-X)；[数据集](https://huggingface.co/datasets/Tajamul21/Agent-X)）：评什么：视觉中心的多步 agentic task；核心思想：把图像、多图、视频和网页等视觉上下文放进真实工具使用环境，并用 step-level 指标评估推理链与工具调用质量。
- [SFE](https://arxiv.org/abs/2506.10521)（[赛页](https://internscience.github.io/sfe-competition-2025/)；[数据集](https://huggingface.co/datasets/PrismaX/SFE)）：评什么：科学考试风格的理解、推理与表达；核心思想：以更贴近科研/科学考试表述的题目与评分协议测试科学推理能力。
- [Table Recognition with Vision LLMs](https://www.ijcai.org/proceedings/2025/279)：评什么：vision LLM 的表格识别与推理。核心思想：把 benchmark 和 neighbor-guided toolchain reasoner 结合起来，同时评估结构化表格解析和下游推理。
- [M4Bench](https://www.ijcai.org/proceedings/2025/762)：评什么：面向 MLLM 的多领域、多粒度、多图理解。核心思想：测试模型是否能跨多张图和多种粒度协调证据，而不是把每张图孤立处理。
- [DashboardQA](https://arxiv.org/abs/2508.17398)：评什么：交互式 dashboard 上的多模态 agent 问答；核心思想：把图表理解、控件状态和页面级信息检索放进同一任务，诊断 agent 是否能围绕可视化界面主动取证。
- [HiPhO](https://arxiv.org/abs/2509.07894)（[数据集](https://huggingface.co/datasets/SciYu/HiPhO)；[开源代码](https://github.com/SciYu/HiPhO)）：评什么：最新高物/奥赛题的物理推理（含多模态输入）；核心思想：用高难度奥赛题降低“常识式猜测”，更强调严谨推导与物理建模。
- [GroundingSuite](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_GroundingSuite_Measuring_Complex_Multi-Granular_Pixel_Grounding_ICCV_2025_paper.html)（[开源代码](https://github.com/hustvl/GroundingSuite)）：评什么：复杂多粒度 pixel grounding。核心思想：在多个定位粒度上测试 grounding，为视觉问答、GUI grounding 和具身感知流水线提供基础评测。
- [MC-Bench](https://openaccess.thecvf.com/content/ICCV2025/html/Xu_MC-Bench_A_Benchmark_for_Multi-Context_Visual_Grounding_in_the_Era_ICCV_2025_paper.html)（[项目页](https://xuyunqiu.github.io/MC-Bench)）：评什么：MLLM 时代的多上下文视觉 grounding。核心思想：要求模型在多个上下文之间定位并对齐证据，是文档、GUI 和具身视觉 agent 的基础能力。
- [MMReason](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_MMReason_An_Open-Ended_Multi-Modal_Multi-Step_Reasoning_Benchmark_for_MLLMs_Toward_ICCV_2025_paper.html)：评什么：开放式多模态多步推理。核心思想：要求围绕视觉证据进行更长的自由形式推理，补足选择题 VQA 的局限。
- [OCR Hinders RAG / OHR-Bench](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.html)（[开源代码](https://github.com/opendatalab/OHR-Bench)）：评什么：OCR 错误如何级联影响检索增强生成。核心思想：在不完美文档抽取下评估下游 RAG 可靠性，而不是把 OCR 质量当作孤立指标。
- [UNIDOC-BENCH](https://arxiv.org/abs/2510.03663)（[开源代码](https://github.com/SalesforceAIResearch/UniDoc-Bench)）：评什么：文档中心的多模态 RAG；核心思想：在真实 PDF 页面的文本、表格、图像证据上统一比较 text-only、image-only、融合式和联合检索式 MM-RAG。
- [M4DocBench](https://arxiv.org/abs/2510.21603)：评什么：多模态、多跳、多文档、多轮 deep research；核心思想：由 Doc-Researcher 引入完整证据链标注，专门测试跨文档视觉语义保留、动态检索粒度和迭代式证据累积。
- [DiagramEval](https://arxiv.org/abs/2510.25761)：通过图结构评测 LLM 生成的 diagram。核心思想是把 SVG 式图示解析为节点和关系，使图示质量能按结构忠实度判断，而不只依赖通用图像相似度。
- [ChartAB](https://arxiv.org/abs/2510.26781)：评什么：图表 grounding 与 dense alignment；核心思想：要求模型抽取表格数据、定位可视化元素、识别图表属性，并用结构化 JSON 与双图对齐任务评估细粒度图表感知。
- [TIR-Bench](https://arxiv.org/abs/2511.01833)：评什么：agentic thinking-with-images；核心思想：要求模型在推理链中创建或调用图像处理工具，覆盖旋转 OCR、仪表读取、迷宫、找不同、视觉搜索等 13 类动态视觉任务。
- [MME-CC](https://arxiv.org/abs/2511.03146)：评什么：多模态认知能力（cognitive capacity）诊断；核心思想：以更具挑战性的多维子项衡量综合能力边界（暂未见稳定官方代码仓库）。
- [DOCR-Inspector](https://arxiv.org/abs/2512.10619)（[开源代码](https://github.com/ZZZZZQT/DOCR-Inspector)）：评什么：真实文档解析结果的细粒度错误检测与质量评估；核心思想：用 VLM-as-a-Judge 对文档图像和解析输出逐项检查，按 28 类错误与 Chain-of-Checklist 诊断解析失败，并配套 DOCRcaseBench。
- [BabyVision](https://arxiv.org/abs/2601.06521)（[开源代码](https://github.com/UniPat-AI/BabyVision)）：评什么：超越语言提示的核心视觉推理能力；核心思想：以更“早期视觉/组合概念”的题型诊断模型视觉能力短板。
- [WorldVQA](https://arxiv.org/abs/2602.02537)：评测多模态大模型中的原子世界知识。核心思想：提出依赖真实世界实体、属性和关系识别的视觉问答，补充偏 OCR 和偏图表的图像评测。
- [AgentVista](https://arxiv.org/abs/2602.23166)（[开源代码](https://github.com/hkust-nlp/AgentVista)）：评什么：现实视觉场景中的超难多模态 agent 任务；核心思想：从 Agent-X 引用链扩展到更开放、更接近真实环境的视觉任务，强调场景理解、行动选择和多步反馈。
- [FinDocBench](https://arxiv.org/abs/2603.11044)：评什么：金融 PDF 的目录结构、跨页表格拼接和单元格级定位；核心思想：用专家验证的金融文档类别与 TocEDS、cross-page TEDS、C-IoU 等指标评估审计级文档解析。
- [MADQA](https://arxiv.org/abs/2603.12180)：评什么：多文档集合中的 agentic document QA；核心思想：把准确率和检索/阅读 effort 绑定，诊断 agent 是策略性导航还是暴力遍历。
- [VTC-Bench](https://arxiv.org/abs/2603.15030)：评什么：agentic multimodal model 的组合式视觉工具链调用；核心思想：把视觉任务拆成可组合工具调用序列，评估模型是否会选择、排序和校验多个视觉工具而不是一次性作答。
- [VAREX](https://arxiv.org/abs/2603.15118)（[项目页](https://udibarzi.github.io/varex-bench/)；[数据集](https://huggingface.co/datasets/ibm-research/VAREX)；[开源代码](https://github.com/udibarzi/varex-bench)）：评什么：政府表单上的多模态结构化抽取；核心思想：为每份文档提供唯一 schema 与四种输入模态，区分模型“会读字段”和“会按 schema 稳定输出”。
- [MDPBench](https://arxiv.org/abs/2603.28130)（[开源代码](https://github.com/Yuliang-Liu/MultimodalOCR/tree/main/MDPBench)）：评什么：真实场景中的多语言文档解析；核心思想：覆盖 17 种语言、数字文档与拍照文档，重点暴露非拉丁文字和低资源语言下的解析退化。
- [ParseBench](https://arxiv.org/abs/2604.08538)（[开源代码](https://github.com/run-llama/ParseBench)）：评什么：文档解析的语义正确性、表格/图表保真与视觉 grounding；核心思想：把企业文档里最影响自动决策的解析失败拆成可评测维度。
- [HLE-VL](https://github.com/ByteDance-Seed/Seed2.0)：Seed2.0 model card 报告的 HLE 风格视觉语言评测；目前未确认有独立公开版本。核心思想：即使具体评测子集只在 model card 中出现，也应跟踪模型厂商对高难视觉知识与推理任务的关注。
- [CC-OCR V2](https://arxiv.org/abs/2605.03903)（[开源代码](https://github.com/eioss/CC-OCR-V2)）：评什么：真实企业文档处理中的 OCR literacy；核心思想：覆盖文本识别、文档解析、文档 grounding、关键信息抽取和文档问答五条 OCR-centric track，强调 hard/corner cases。
## 1.5.3 Agent Harness

- [VisProg](https://arxiv.org/abs/2211.11559)（[开源代码](https://github.com/allenai/visprog)）：把视觉任务转成“生成可执行程序 + 执行回填”的可复用 harness，弱化单模型端到端幻觉风险。
- [Visual ChatGPT](https://arxiv.org/abs/2303.04671)（[开源代码](https://github.com/microsoft/visual-chatgpt)）：多视觉工具协作的通用视觉 agent harness；典型闭环是 `plan -> call tools -> verify -> refine`。
- [ViperGPT](https://arxiv.org/abs/2303.08128)（[开源代码](https://github.com/cvlab-columbia/viper)）：以 Python 执行作为中间层的视觉推理 harness，把模型输出约束为可执行 API 组合。
- [MM-REACT](https://arxiv.org/abs/2303.11381)（[开源代码](https://github.com/microsoft/MM-REACT)）：多模态 ReAct 工作流；把视觉感知、推理与动作（工具调用）组织成可复用的提示控制流。
- [HuggingGPT](https://arxiv.org/abs/2303.17580)（[开源代码](https://github.com/microsoft/JARVIS)）：把多模态任务路由到工具/模型并编排执行的通用 agent 框架（包含视觉任务路由与组合）。
- [MDocAgent](https://arxiv.org/abs/2503.13964)（[开源代码](https://github.com/aiming-lab/MDocAgent)）：面向文档问答的多模态多 agent RAG 框架；把 text agent、image agent、critical agent、summary agent 等角色组合起来做跨模态证据整合。
- [ChartAgent](https://arxiv.org/abs/2507.06157)（开源代码：暂未见稳定公开官方仓库）：面向图表问答的 agentic workflow，常见做法是 `读图/OCR -> 表格化/结构化 -> 计算/校验 -> 作答` 的分阶段编排。
- [PyVision](https://arxiv.org/abs/2507.07998)（[项目页](https://agent-x.space/pyvision/)；[开源代码](https://github.com/agents-x-project/PyVision)）：面向视觉推理的动态工具 harness；让模型按任务生成、执行和修正 Python 图像处理工具，而不是依赖固定 toolset。
- [VProChart](https://arxiv.org/abs/2507.17209)（开源代码：暂未见稳定公开官方仓库）：面向图表推理的流程化方法，更强调把图表理解与计算/验证模块化以降低图表 hallucination。
- [Doc-Researcher](https://arxiv.org/abs/2510.21603)（开源代码：暂未见稳定公开官方仓库）：面向多模态文档 deep research 的多 agent 系统；把解析、分层检索、问题分解、证据累积和跨文档综合连接成迭代式 workflow。
- [DocAgent](https://aclanthology.org/2025.emnlp-main.893/)（[开源代码](https://github.com/lisun-ai/DocAgent)）：面向多模态长上下文文档理解的 agentic framework；强调记忆与 reviewer 机制，把文本、版面、图表、表格和图像证据统一到长文档推理链中。
- [ARIAL](https://arxiv.org/abs/2511.18192)（开源代码：暂未见稳定公开官方仓库）：面向 Document VQA 与答案定位的 agentic framework；通过 planner 编排 OCR、语义检索、答案生成和文本到区域对齐，同时输出答案与 bounding box 证据。
- [DocDancer](https://arxiv.org/abs/2601.05163)（开源代码：论文称开源，暂未确认稳定公开仓库）：把 DocQA 建模成工具驱动的信息寻求过程，显式区分 document exploration 与 answer synthesis，并用合成轨迹训练开放式文档 agent。
- [OCR-Agent](https://arxiv.org/abs/2602.21053)（[开源代码](https://github.com/AIGeeksGroup/OCR-Agent)）：面向 OCR/文档理解的专门 agent；强调 `OCR -> 结构化解析 -> 校验 -> 回填` 的迭代式工作流。
- [Doc-V*](https://arxiv.org/abs/2604.13731)（开源代码：暂未见稳定公开官方仓库）：面向多页 Document VQA 的 coarse-to-fine 交互式视觉推理 harness；核心思想是用页面级检索、区域级放大、证据验证和答案生成闭环替代一次性全页阅读。

## 1.5.4 Skill

- [computer-vision-opencv](https://skills.sh/mindrally/skills/computer-vision-opencv) 适合图像预处理、检测、透视变换与标注。
- [paddleocr-text-recognition](https://skills.sh/aidenwu0209/paddleocr-skills/paddleocr-text-recognition) 适合文档 OCR。
- [pdf-ocr](https://skills.sh/yejinlei/pdf-ocr-skill/pdf-ocr) 适合扫描 PDF 前处理。
- [pymupdf-pdf](https://skills.sh/kesslerio/pymupdf-pdf-parser-clawdbot-skill/pymupdf-pdf) 适合 PDF 结构解析与页级抽取。
- [pdf](https://skills.sh/anthropics/skills/pdf) 适合把 PDF 解析和引用抽取接入通用工作流。
