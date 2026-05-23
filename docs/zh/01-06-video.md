# 1.6 视频

> 上级章节：1. 基础能力


## 1.6.1 Leaderboard

- [Video-MME Leaderboard](https://video-mme.github.io/home_page.html#leaderboard)：持续榜单：短、中、长视频的多任务理解；适合作为视频 VLM 综合能力的基础参照。
- [LongVideoBench Leaderboard](https://longvideobench.github.io/index.html#leaderboard)：持续榜单：长上下文 interleaved video-language understanding；适合比较不同抽帧预算、字幕输入和长程检索策略。
- [VideoAutoArena](https://videoautoarena.github.io/)：持续榜单：通过用户模拟、模型对战和自动裁判比较开放式视频分析模型；适合补足选择题 benchmark 对真实用户视频任务覆盖不足的问题。
- [Video-MMMU Leaderboard](https://videommmu.github.io/#Leaderboard)：持续榜单：多学科专业视频中的知识获取与问答；适合跟踪视频模型是否能从教程/讲座式视频中获取新知识。
- [MMVU Leaderboard](https://mmvu-benchmark.github.io/#leaderboard)：持续榜单：通用视频理解与问答；适合与 Video-MME、Video-MMMU 交叉筛选强视频 agent runtime。
- [V-STaR Leaderboard](https://v-star-bench.github.io/#leaderboard)：持续榜单：视频空间-时间推理；适合专门观察 object motion、event ordering 和跨片段 grounding 能力。

## 1.6.2 Bench

（以下按发布时间排序，覆盖 video knowledge、video reasoning、motion/perception、long-video、multi-video、streaming 与 agentic/web-video 等子任务。）

- [ContPhy](https://arxiv.org/abs/2402.06119)：评测连续物理过程与动态理解；核心思想是连续变化条件下的物理一致性与状态预测。
- [TempCompass](https://arxiv.org/abs/2403.00476)：评测时间定位与事件顺序理解；核心思想是细粒度时序对齐与时间点检索。
- [Video-MME](https://arxiv.org/abs/2405.21075)（[项目页](https://mme-benchmark.github.io/)；[开源代码](https://github.com/MME-Benchmarks/Video-MME)）：评测视频分析的全谱系能力；核心思想：用更系统的任务覆盖与评测协议把“视频理解”拆成可对比维度，并提供一键评测脚本。
- [LVBench](https://arxiv.org/abs/2406.08035)：评测长视频理解；核心思想是以更长时间跨度与更强信息检索需求区分长视频能力。
- [LongVideoBench](https://arxiv.org/abs/2407.15754)：评测长视频理解；核心思想是把 `frames + subtitles + question` 交织输入，并显式参数化帧预算（如 `max_num_frames`）实现可复现比较。（[项目页](https://longvideobench.github.io/)；[数据集](https://huggingface.co/datasets/longvideobench/LongVideoBench)；[开源代码](https://github.com/longvideobench/LongVideoBench)）
- [VideoAutoArena](https://videoautoarena.github.io/)：评测开放式视频分析模型的自动竞技场式比较；核心思想是通过用户模拟、模型对战和自动裁判补足固定选择题 benchmark 的真实用户任务覆盖不足。
- [TVBench](https://arxiv.org/abs/2410.07752)：评测时序理解与运动相关感知；核心思想是把变化/运动作为主要信号，而非静态单帧识别。
Video reasoning（时序/因果/多跳推理）：
- [VideoWebArena](https://arxiv.org/abs/2410.19100)（[项目页](https://videowebarena.github.io/)；[开源代码](https://github.com/ljang0/videowebarena)）：评测长上下文多模态 agent 在网页任务中的视频理解；核心思想是把 tutorial/video evidence、网页状态和可执行动作放进同一环境，按任务成功率衡量“看视频后会不会操作”。
- [TOMATO](https://arxiv.org/abs/2410.23266)：评测时序推理与动作理解；核心思想是围绕事件边界与状态转移构造问题。
- [CG-Bench](https://arxiv.org/abs/2412.12075)：评测长链路视频理解与复杂推理/生成；核心思想是提高组合推理与输出约束强度，减少“短路”。
- [OVBench](https://arxiv.org/abs/2501.00584)（[开源代码](https://github.com/MCG-NJU/VideoChat-Online)）：评测在线/流式视频理解与交互；核心思想：把“边接收视频边更新状态并作答”作为输入协议的一部分，并提供可复现的在线视频运行与评测脚本。
- [MotionBench](https://arxiv.org/abs/2501.02955)：评测运动理解与细粒度动作感知；核心思想是覆盖多种运动模式并提供统一评测协议。
- [OVOBench](https://arxiv.org/abs/2501.05510)：评测在线视频/在线交互理解；核心思想是面向在线场景的实时性约束与状态持续更新。
- [MMVU](https://arxiv.org/abs/2501.12380)：评测通用视频理解与问答；核心思想是以更系统的任务分解/问题类型覆盖，诊断从事实回忆到理解推理的能力谱。
- [Video-MMMU（VideoMMMU）](https://arxiv.org/abs/2501.13826)：评测“看视频学知识”的问答能力；核心思想是除绝对准确率外引入 `delta accuracy` 等增量指标，并规范输入组织（例如把题图追加到视频最后一帧）以便统一评测。（[项目页](https://videommmu.github.io/)；[数据集](https://huggingface.co/datasets/lmms-lab/VideoMMMU)；[开源代码](https://github.com/EvolvingLMMs-Lab/VideoMMMU)）
- [Video-OCR Benchmark](https://arxiv.org/abs/2502.06445)（[开源代码](https://github.com/video-db/ocr-benchmark)）：评测 VLM 与传统 OCR 在视频帧文字识别上的差异；核心思想是把视频文本识别从单图 OCR 中拆出来，显式比较抽帧、时间冗余和端到端视觉语言模型的收益。
- [ViSpeak](https://arxiv.org/abs/2503.12769)：评测视频到语言的实时/半实时表达；核心思想是强调时间一致性、信息覆盖与输出流畅性。
- [EgoTempo](https://arxiv.org/abs/2503.13646)：评测第一视角视频的时序与动作理解；核心思想是利用 egocentric 视角的遮挡、快速运动与交互性提高难度。
- [FAVOR-Bench](https://arxiv.org/abs/2503.14935)（[项目页](https://favor-bench.github.io/)；[开源代码](https://github.com/FAVOR-Bench/FAVOR-Bench)；[数据集](https://huggingface.co/datasets/zl2048/FAVOR)）：评测细粒度视频运动理解；核心思想是覆盖第一视角与第三视角视频、闭集问答和开放描述，专门诊断模型是否真正看懂动作细节、运动轨迹和时间动态。
- [VideoSimpleQA](https://arxiv.org/abs/2503.18923)：评测基础视频事实问答；核心思想是用低歧义 QA 协议快速区分“看到了没有/记住了没有”。


- [IV-Bench](https://arxiv.org/abs/2504.15415)（[开源代码](https://github.com/multimodal-art-projection/IV-Bench)）：评测 image-grounded video perception and reasoning；核心思想是把参考图像、视频和文本问题一起输入，检查模型能否把外部视觉上下文融入视频理解而不是只依赖当前视频帧。
- [LiveSports3K](https://arxiv.org/abs/2504.16030)：评测直播体育场景下的理解与字幕/解说相关能力；核心思想是以直播分布与时间敏感信息为挑战。
- [Minerva](https://arxiv.org/abs/2505.00681)：评测复杂视频推理与知识整合；核心思想是更长链路推理与跨模态信息融合。
- [VideoEval-Pro](https://arxiv.org/abs/2505.14640)：评测更专业的长视频理解/评测协议鲁棒性；核心思想是更严格的评测设置与更贴近实际的长视频任务组织。
- [MME-VideoOCR](https://arxiv.org/abs/2505.21333)：评测视频中的动态文字感知、识别与推理；核心思想是把 text-in-video 当成视频理解的关键维度，覆盖多语言、多场景和 OCR-to-reasoning 问题。
- [Video-Holmes](https://arxiv.org/abs/2505.21374)：评测“侦探式”视频推理与证据链对齐；核心思想是用可解释线索链约束推理过程，降低拍脑袋结论。
- [VideoReasonBench](https://arxiv.org/abs/2505.23359)：评测时序、因果与多步推理；核心思想是显式要求跨片段线索整合而非单帧识别。
- [ScaleLong](https://arxiv.org/abs/2505.23922)（[开源代码](https://github.com/multimodal-art-projection/ScaleLong)）：评测多时间尺度长视频理解；核心思想是把秒级、分钟级、小时级上下文放到统一评测协议里，诊断模型随视频长度增长时的检索、记忆与跨片段推理退化。
- [V-STaR](https://v-star-bench.github.io/#leaderboard)：评测视频空间-时间推理；核心思想是把对象运动、事件顺序和跨片段 grounding 作为独立压力点，补足 Video-MME/LongVideoBench 中时空推理维度的细分诊断。
- [VideoMathQA](https://arxiv.org/abs/2506.05349)（[项目页](https://mbzuai-oryx.github.io/VideoMathQA)；[开源代码](https://github.com/mbzuai-oryx/VideoMathQA)）：评测视频中的数学推理；核心思想是让模型跨视觉、音频、文本和长时序线索理解教学/解题过程，连接视频理解与数学推理能力。
- [Morse-500](https://arxiv.org/abs/2506.05523)：评测更细粒度的视频推理与线索追踪；核心思想是以更高密度的推理点与更严格的答案约束做诊断。
- [EASG-Bench](https://arxiv.org/abs/2506.05787)（[开源代码](https://github.com/fpv-iplab/EASG-bench)）：评测基于 egocentric action scene graph 的视频问答；核心思想是从带时空 grounding 的动态图生成 QA，重点检查 actor、action、object 关系与时序顺序理解。
- [CausalVQA](https://arxiv.org/abs/2506.09943)：评测真实视频中的物理因果推理；核心思想是用 counterfactual、hypothetical、anticipation、planning 等问题类型，要求模型基于视觉证据预测事件后果而非套用语言先验。
- [HiVU](https://arxiv.org/abs/2506.13589)（[开源代码](https://github.com/xzc-zju/AdaVideoRAG)）：评测长视频问答中的分层索引与证据检索；核心思想是把视频拆成多粒度索引层级，诊断模型是否能在超长视频里定位有效片段而非均匀抽帧。
- [CausalStep](https://arxiv.org/abs/2507.16878)：评测显式逐步因果推理；核心思想是把视频切成因果关联单元并采用顺序作答协议，防止模型利用全局上下文捷径直接猜最终答案。
- [M3-Bench](https://arxiv.org/abs/2508.09736)：评测长视频智能体的跨模态长程记忆；核心思想是同时包含视觉、音频和文本记忆信号，要求模型在长期上下文中保持、检索和组合历史证据。
- [OmniVideoBench](https://arxiv.org/abs/2510.10689)（[项目页](https://omnivideobench.github.io/omnivideobench_home/)；[开源代码](https://github.com/NJU-LINK/OmniVideoBench)）：评测长视频全模态理解；核心思想是把视觉、音频、OCR 和 ASR 等证据放进同一评测协议，检查模型是否能在长视频中跨模态整合信息。
- [CrossVid](https://arxiv.org/abs/2511.12263)：评测跨多个视频的对比、检索与聚合推理；核心思想是多视频证据组织与一致性推理，而非单视频问答。
- [LongShOTBench](https://arxiv.org/abs/2512.16978)（[项目页](https://mbzuai-oryx.github.io/LongShOT/)；[数据集](https://huggingface.co/datasets/MBZUAI/longshot-bench)；[开源代码](https://github.com/mbzuai-oryx/longshot)）：评测长视频中的 omni-modal reasoning 与 agentic tool use；核心思想是把视觉、语音和环境音证据、开放式问答、多轮对话和可解释评分 rubric 放进同一评测协议。
- [SYNCR](https://arxiv.org/abs/2605.08412)：评测带 synthetic grounding 的跨视频推理；核心思想是用可控合成线索检查模型是否能在多个视频之间建立对应关系、定位证据并完成组合推断。
- [EgoMemReason](https://arxiv.org/abs/2605.09874)（[项目页](https://egomemreason.github.io/)；[数据集](https://huggingface.co/datasets/Ted412/EgoMemReason)；[开源代码](https://github.com/Ziyang412/EgoMemReason)）：评测长时第一视角视频的记忆驱动推理；核心思想是从 LongVideoBench 引用链扩展到生活记录式 egocentric video，要求模型保留、检索并组合长期个人视觉证据。
- [TOC-Bench](https://arxiv.org/abs/2605.09904)：评测视频大模型的 temporal object consistency；核心思想是追踪同一对象跨时间片段的身份、属性和状态一致性，避免模型只凭局部帧做静态识别。


## 1.6.3 Agent Harness

- [LMMs-Eval](https://arxiv.org/abs/2407.12772)（[开源代码](https://github.com/EvolvingLMMs-Lab/lmms-eval)）：多模态评测 harness，覆盖 Video-MME、LongVideoBench、Video-MMMU 等视频任务；适合作为复现实验和批量榜单提交的统一入口。
- [VideoChat-Online](https://arxiv.org/abs/2501.00584)（[开源代码](https://github.com/MCG-NJU/VideoChat-Online)）：在线/流式视频理解的参考实现，与 OVBench 的 benchmark-specific runtime 强绑定。
- [VideoRAG](https://arxiv.org/abs/2502.01549)（[开源代码](https://github.com/HKUDS/VideoRAG)）：针对超长视频的检索增强生成工作流，把“找片段证据”外包给视频检索与索引结构。
- [LVAgent](https://arxiv.org/abs/2503.10200)（[开源代码](https://github.com/64327069/LVAgent)）：面向长视频问答的动态 agent；通过 task planning、迭代式工具调用和实时进度管理，在不同问题上自适应选择检索与分析路径。
- [VideoMind](https://arxiv.org/abs/2503.13444)（[开源代码](https://github.com/yeliudev/VideoMind)）：把长视频理解拆成 planning、grounding、retrieval 与 reasoning 的 agentic pipeline，并用 Chain-of-LoRA 适配长视频任务。
- [LiveCC](https://arxiv.org/abs/2504.16030)（[开源代码](https://github.com/showlab/LiveCC)）：面向直播体育等时间敏感场景的理解与字幕/解说生成链路。
- [MR.Video](https://arxiv.org/abs/2504.16082)（[开源代码](https://github.com/ziqipang/MR-Video)）：把长视频理解组织成 MapReduce 风格的 evidence aggregation，先分段抽取局部证据，再全局汇总推理。
- [TimeChat-Online](https://arxiv.org/abs/2504.17343)（[开源代码](https://github.com/yaolinli/TimeChat-Online)）：面向时间敏感的在线视频交互理解，强调在线状态更新与时间对齐。
- [Deep Video Discovery](https://arxiv.org/abs/2505.18079)（[开源代码](https://github.com/microsoft/DeepVideoDiscovery)）：面向长视频理解的 agentic search harness；通过多粒度视频数据库和 search-centric tools，让 agent 按问题自适应规划、检索片段并汇总证据。
- [VideoDeepResearch](https://arxiv.org/abs/2506.10821)（[开源代码](https://github.com/yhy-2000/VideoDeepResearch)）：把“看片 -> 检索外部资料 -> 生成报告”组织成可复用长链路 pipeline。
- [AdaVideoRAG](https://arxiv.org/abs/2506.13589)（[开源代码](https://github.com/xzc-zju/AdaVideoRAG)）：长视频 RAG harness；按任务自适应选择层级化索引和检索深度，减少固定抽帧或固定 chunk 策略的浪费。
- [Flash-VStream](https://arxiv.org/abs/2506.23825)（[开源代码](https://github.com/IVGSZ/Flash-VStream)）：长视频流式理解的 memory budget harness；强调实时性约束下的记忆更新与信息保真。
- [M3-Agent](https://arxiv.org/abs/2508.09736)（开源代码：暂未见稳定公开官方仓库）：面向长视频的长时记忆 agent；将“看、听、记、推理”拆成可交互模块，并配套 M3-Bench 检验记忆保留和跨模态证据调用。
- [GCAgent](https://arxiv.org/abs/2511.08909)（开源代码：暂未见稳定公开官方仓库）：面向长视频的图压缩 agent；用图结构压缩长视频事件与实体关系，再围绕问题做局部扩展和推理。
- [LongVT](https://arxiv.org/abs/2511.20785)（[开源代码](https://github.com/EvolvingLMMs-Lab/LongVT)）：面向长视频的原生 tool-calling 与“thinking with long videos”工作流，常被用作长视频场景的 agentic runtime 参考。
- [SAGE](https://arxiv.org/abs/2512.13874)（[开源代码](https://github.com/allenai/SAGE)）：any-horizon 长视频推理 agent；把“何时单轮回答/何时多轮搜证据”做成可学习的策略。
- [LongShOTAgent](https://arxiv.org/abs/2512.16978)（[开源代码](https://github.com/mbzuai-oryx/longshot)）：围绕 LongShOTBench 的长视频 agentic system；用预处理、跨模态检索、工具调用和迭代 refinement 处理视觉、语音与环境音证据。
- [EGAgent](https://arxiv.org/abs/2601.18157)（开源代码：暂未见稳定公开官方仓库）：面向 very long egocentric video 的 agentic workflow；核心在于按 query 主动检索、压缩和重组第一视角生活记录中的证据。
- [VideoSEAL](https://arxiv.org/abs/2605.12571)（开源代码：暂未见稳定公开官方仓库）：面向 agentic long video understanding 的证据校准框架；核心思想是把答案生成权与证据对齐/校验解耦，缓解长视频 agent 在检索片段和最终回答之间的错配。
- [VideoSeeker](https://arxiv.org/abs/2605.16079)（开源代码：论文称将公开，暂未确认稳定公开仓库）：面向视频理解的原生 agentic tool invocation；强调 instance-level 工具选择，把 search、grounding 和 verification 纳入模型决策过程。

## 1.6.4 Skill

- [ffmpeg](https://skills.sh/digitalsamba/claude-code-video-toolkit/ffmpeg) 适合切片、抽帧、转码。
- [ffmpeg-video-editor](https://skills.sh/sundial-org/awesome-openclaw-skills/ffmpeg-video-editor) 适合视频局部编辑和片段导出。
- [whisper](https://skills.sh/davila7/claude-code-templates/whisper) 适合视频语音转写。
- [faster-whisper](https://skills.sh/theplasmak/faster-whisper/faster-whisper) 适合低延迟语音转写。
- [ffmpeg-analyse-video](https://skills.sh/fabriqaai/ffmpeg-analyse-video-skill/ffmpeg-analyse-video) 适合结构化分析视频内容。
- [video-understand](https://github.com/heygen-com/skills/tree/master/skills/video-understand) 是本地 `ffmpeg + whisper` 视频理解工作流 skill；更贴近可复用视频处理链路，而不是某个 benchmark 命名。
