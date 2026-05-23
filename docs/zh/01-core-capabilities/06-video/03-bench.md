# 1.6.3 Bench

（以下按发布时间排序，覆盖 video knowledge、video reasoning、motion/perception、long-video、multi-video、streaming 与 agentic/web-video 等子任务。）

- [ContPhy](https://arxiv.org/abs/2402.06119)：评测连续物理过程与动态理解；核心思想是连续变化条件下的物理一致性与状态预测。
- [TempCompass](https://arxiv.org/abs/2403.00476)：评测时间定位与事件顺序理解；核心思想是细粒度时序对齐与时间点检索。
- [Video-MME](https://arxiv.org/abs/2405.21075)（[项目页](https://mme-benchmark.github.io/)；[开源代码](https://github.com/MME-Benchmarks/Video-MME)）：评测视频分析的全谱系能力；核心思想：用更系统的任务覆盖与评测协议把“视频理解”拆成可对比维度，并提供一键评测脚本。
- [LVBench](https://arxiv.org/abs/2406.08035)：评测长视频理解；核心思想是以更长时间跨度与更强信息检索需求区分长视频能力。
- [LongVideoBench](https://arxiv.org/abs/2407.15754)：评测长视频理解；核心思想是把 `frames + subtitles + question` 交织输入，并显式参数化帧预算（如 `max_num_frames`）实现可复现比较。（[项目页](https://longvideobench.github.io/)；[数据集](https://huggingface.co/datasets/longvideobench/LongVideoBench)；[开源代码](https://github.com/longvideobench/LongVideoBench)）
- [TVBench](https://arxiv.org/abs/2410.07752)：评测时序理解与运动相关感知；核心思想是把变化/运动作为主要信号，而非静态单帧识别。
- [VideoWebArena](https://arxiv.org/abs/2410.19100)（[项目页](https://videowebarena.github.io/)；[开源代码](https://github.com/ljang0/videowebarena)）：评测长上下文多模态 agent 在网页任务中的视频理解；核心思想是把 tutorial/video evidence、网页状态和可执行动作放进同一环境，按任务成功率衡量“看视频后会不会操作”。
- [TOMATO](https://arxiv.org/abs/2410.23266)：评测时序推理与动作理解；核心思想是围绕事件边界与状态转移构造问题。
- [CG-Bench](https://arxiv.org/abs/2412.12075)：评测长链路视频理解与复杂推理/生成；核心思想是提高组合推理与输出约束强度，减少“短路”。
- [OVBench](https://arxiv.org/abs/2501.00584)（[开源代码](https://github.com/MCG-NJU/VideoChat-Online)）：评测在线/流式视频理解与交互；核心思想：把“边接收视频边更新状态并作答”作为输入协议的一部分，并提供可复现的在线视频运行与评测脚本。
- [MotionBench](https://arxiv.org/abs/2501.02955)：评测运动理解与细粒度动作感知；核心思想是覆盖多种运动模式并提供统一评测协议。
- [OVOBench](https://arxiv.org/abs/2501.05510)：评测在线视频/在线交互理解；核心思想是面向在线场景的实时性约束与状态持续更新。
- [MMVU](https://arxiv.org/abs/2501.12380)：评测通用视频理解与问答；核心思想是以更系统的任务分解/问题类型覆盖，诊断从事实回忆到理解推理的能力谱。
- [Video-MMMU（VideoMMMU）](https://arxiv.org/abs/2501.13826)：评测“看视频学知识”的问答能力；核心思想是除绝对准确率外引入 `delta accuracy` 等增量指标，并规范输入组织（例如把题图追加到视频最后一帧）以便统一评测。（[项目页](https://videommmu.github.io/)；[数据集](https://huggingface.co/datasets/lmms-lab/VideoMMMU)；[开源代码](https://github.com/EvolvingLMMs-Lab/VideoMMMU)）
- [VideoAutoArena](https://videoautoarena.github.io/)：评测开放式视频分析模型的自动竞技场式比较；核心思想是通过用户模拟、模型对战和自动裁判补足固定选择题 benchmark 的真实用户任务覆盖不足。
- [Video-OCR Benchmark](https://arxiv.org/abs/2502.06445)（[开源代码](https://github.com/video-db/ocr-benchmark)）：评测 VLM 与传统 OCR 在视频帧文字识别上的差异；核心思想是把视频文本识别从单图 OCR 中拆出来，显式比较抽帧、时间冗余和端到端视觉语言模型的收益。
- [MimeQA](https://arxiv.org/abs/2502.16671)（[开源代码](https://github.com/MIT-MI/MimeQA)，[数据集](https://huggingface.co/datasets/hzli1202/MimeQA)）：评什么：默剧视频中的非语言社交理解。核心思想：用无声的表达性表演作为视频问答来源，测试 foundation model 是否理解手势、姿态、情绪和社交意图，而不是只依赖语言主导的社会推理。
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
- [Q-Bench-Video](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Q-Bench-Video_Benchmark_the_Video_Quality_Understanding_of_LMMs_CVPR_2025_paper.html)：评什么：大多模态模型的视频质量理解。核心思想：把视频质量感知与质量推理做成显式 benchmark 目标，补充事件中心的视频问答。
- [VidHalluc](https://openaccess.thecvf.com/content/CVPR2025/html/Li_VidHalluc_Evaluating_Temporal_Hallucinations_in_Multimodal_Large_Language_Models_for_CVPR_2025_paper.html)（[项目页](https://people-robots.github.io/vidhalluc)）：评什么：视频 MLLM 的时序幻觉。核心思想：测试模型是否编造视频中并不存在的事件、动作或时间关系。
- [LongVALE](https://openaccess.thecvf.com/content/CVPR2025/html/Geng_LongVALE_Vision-Audio-Language-Event_Benchmark_Towards_Time-Aware_Omni-Modal_Perception_of_Long_Videos_CVPR_2025_paper.html)：评什么：长视频中时间感知的全模态理解。核心思想：对齐视觉、音频、语言和事件证据，使长视频理解覆盖跨模态时序 grounding。
- [VELOCITI](https://openaccess.thecvf.com/content/CVPR2025/html/Saravanan_VELOCITI_Benchmarking_Video-Language_Compositional_Reasoning_with_Strict_Entailment_CVPR_2025_paper.html)：评什么：带严格蕴含约束的视频-语言组合推理。核心思想：要求模型判断视频内容上的细粒度 entailment，而不是只在宽泛摘要之间选择。
- [OmniMMI](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_OmniMMI_A_Comprehensive_Multi-modal_Interaction_Benchmark_in_Streaming_Video_Contexts_CVPR_2025_paper.html)：评什么：流式视频上下文中的多模态交互。核心思想：把在线交互和多模态输入纳入 benchmark，测试模型在视频证据持续到达时更新状态的能力。
- [V-STaR](https://v-star-bench.github.io/#leaderboard)：评测视频空间-时间推理；核心思想是把对象运动、事件顺序和跨片段 grounding 作为独立压力点，补足 Video-MME/LongVideoBench 中时空推理维度的细分诊断。
- [VideoMathQA](https://arxiv.org/abs/2506.05349)（[项目页](https://mbzuai-oryx.github.io/VideoMathQA)；[开源代码](https://github.com/mbzuai-oryx/VideoMathQA)）：评测视频中的数学推理；核心思想是让模型跨视觉、音频、文本和长时序线索理解教学/解题过程，连接视频理解与数学推理能力。
- [Morse-500](https://arxiv.org/abs/2506.05523)：评测更细粒度的视频推理与线索追踪；核心思想是以更高密度的推理点与更严格的答案约束做诊断。
- [EASG-Bench](https://arxiv.org/abs/2506.05787)（[开源代码](https://github.com/fpv-iplab/EASG-bench)）：评测基于 egocentric action scene graph 的视频问答；核心思想是从带时空 grounding 的动态图生成 QA，重点检查 actor、action、object 关系与时序顺序理解。
- [Video-CoT](https://arxiv.org/abs/2506.08817)：评什么：带 chain-of-thought 标注的时空视频理解。核心思想：把细粒度视频问答与推理轨迹配对，使时间和空间证据整合能够被更显式地诊断。
- [CausalVQA](https://arxiv.org/abs/2506.09943)：评测真实视频中的物理因果推理；核心思想是用 counterfactual、hypothetical、anticipation、planning 等问题类型，要求模型基于视觉证据预测事件后果而非套用语言先验。
- [HiVU](https://arxiv.org/abs/2506.13589)（[开源代码](https://github.com/xzc-zju/AdaVideoRAG)）：评测长视频问答中的分层索引与证据检索；核心思想是把视频拆成多粒度索引层级，诊断模型是否能在超长视频里定位有效片段而非均匀抽帧。
- [AnyCap](https://arxiv.org/abs/2507.12841)：通过统一框架、数据集与 benchmark 评估可控 omni-modal captioning。核心思想：测试 captioning 系统能否依据视觉、音频与时间证据满足可控描述要求，而不只是生成通用 caption。
- [CausalStep](https://arxiv.org/abs/2507.16878)：评测显式逐步因果推理；核心思想是把视频切成因果关联单元并采用顺序作答协议，防止模型利用全局上下文捷径直接猜最终答案。
- [M3-Bench](https://arxiv.org/abs/2508.09736)：评测长视频智能体的跨模态长程记忆；核心思想是同时包含视觉、音频和文本记忆信号，要求模型在长期上下文中保持、检索和组合历史证据。
- [VRBench](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_VRBench_A_Benchmark_for_Multi-Step_Reasoning_in_Long_Narrative_Videos_ICCV_2025_paper.html)：评什么：长叙事视频中的多步推理。核心思想：把长视频故事和显式推理步骤、时间戳配对，使时序证据链能被检查，而不是只看最终答案。
Video reasoning（时序/因果/多跳推理）：
- [OmniVideoBench](https://arxiv.org/abs/2510.10689)（[项目页](https://omnivideobench.github.io/omnivideobench_home/)；[开源代码](https://github.com/NJU-LINK/OmniVideoBench)）：评测长视频全模态理解；核心思想是把视觉、音频、OCR 和 ASR 等证据放进同一评测协议，检查模型是否能在长视频中跨模态整合信息。
- [CrossVid](https://arxiv.org/abs/2511.12263)：评测跨多个视频的对比、检索与聚合推理；核心思想是多视频证据组织与一致性推理，而非单视频问答。
- [LongShOTBench](https://arxiv.org/abs/2512.16978)（[项目页](https://mbzuai-oryx.github.io/LongShOT/)；[数据集](https://huggingface.co/datasets/MBZUAI/longshot-bench)；[开源代码](https://github.com/mbzuai-oryx/longshot)）：评测长视频中的 omni-modal reasoning 与 agentic tool use；核心思想是把视觉、语音和环境音证据、开放式问答、多轮对话和可解释评分 rubric 放进同一评测协议。


- [GameplayQA](https://arxiv.org/abs/2603.24329)（[项目页](https://hats-ict.github.io/gameplayqa/)；[数据集](https://huggingface.co/datasets/wangyz1999/GameplayQA)；[标注软件](https://github.com/wangyz1999/sync-video-label)）：评测面向 3D 虚拟 agent 的决策密集、POV 同步多视频理解；核心思想是用多个第一视角游戏视频流和 Self/Other/World 标注检查时间 grounding、跨视频指代和 agent 角色归因。
- [VideoZeroBench](https://arxiv.org/abs/2604.01569)：评什么：带时空证据校验的长视频问答。核心思想：不只看答案是否正确，还检查支撑答案的时间区间与空间框位置，暴露“答案看似合理但没有真实 grounding”的视频推理缺口。
- [ZeroVideo](https://github.com/ByteDance-Seed/Seed2.0)：Seed2.0 model card 报告的高难真实视频评测；目前未确认有独立公开版本。核心思想：跟踪模型厂商用于压力测试超长、真实视频推理的内部或 model-card-only 视频集，即使当前只有聚合结果公开。
- [SYNCR](https://arxiv.org/abs/2605.08412)：评测带 synthetic grounding 的跨视频推理；核心思想是用可控合成线索检查模型是否能在多个视频之间建立对应关系、定位证据并完成组合推断。
- [EgoMemReason](https://arxiv.org/abs/2605.09874)（[项目页](https://egomemreason.github.io/)；[数据集](https://huggingface.co/datasets/Ted412/EgoMemReason)；[开源代码](https://github.com/Ziyang412/EgoMemReason)）：评测长时第一视角视频的记忆驱动推理；核心思想是从 LongVideoBench 引用链扩展到生活记录式 egocentric video，要求模型保留、检索并组合长期个人视觉证据。
- [TOC-Bench](https://arxiv.org/abs/2605.09904)：评测视频大模型的 temporal object consistency；核心思想是追踪同一对象跨时间片段的身份、属性和状态一致性，避免模型只凭局部帧做静态识别。
