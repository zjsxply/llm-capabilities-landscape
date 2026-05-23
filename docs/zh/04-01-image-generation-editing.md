# 4.1 图片生成与编辑模型

> 上级章节：4. 多模态

说明：本页收纳主目标为图片创作、文本到图像生成、图像编辑、视觉生成评测或生成图像安全性的 benchmark 与 harness。图像/OCR 理解类 benchmark 仍保留在 [1.5 图像](01-05-image-ocr.md)。

## 4.1.1 Leaderboard

- [Artificial Analysis Text to Image Leaderboard](https://artificialanalysis.ai/text-to-image)：基于盲测人类偏好的公开文本到图像竞技场式对比榜单。
- [Arena Image Edit Leaderboard](https://arena.ai/en/leaderboard/image-edit)：面向指令式图像编辑系统的公开竞技场榜单。

## 4.1.2 Survey

- [Text-to-image Diffusion Models in Generative AI: A Survey](https://arxiv.org/abs/2303.07909)：文本到图像扩散系统及其评测的基础综述。
- [Diffusion Model-Based Image Editing: A Survey](https://arxiv.org/abs/2402.17525)：综述指令式与文本驱动图像编辑方法及评测。
- [A Survey of Multimodal-Guided Image Editing with Text-to-Image Diffusion Models](https://arxiv.org/abs/2406.14555)：回顾由文本、mask、layout、参考图等条件引导的编辑。
- [Trustworthy Text-to-Image Diffusion Models: A Timely and Focused Survey](https://arxiv.org/abs/2409.18214)：覆盖安全、公平、隐私、鲁棒性与可信问题。
- [Personalized Image Generation with Deep Generative Models: A Decade Survey](https://arxiv.org/abs/2502.13081)：回顾主体保持、参考条件与个性化生成。

## 4.1.3 Bench

- [HarmonyIQA](https://arxiv.org/abs/2501.01116)：评测图像 harmonization 质量判断。核心思想：收集多个 harmonization 算法生成的合成图并配套人类偏好分数，测试图像质量模型能否发现通用 IQA 容易忽略的前景与背景光照、颜色不一致。
- [MEt3R](https://arxiv.org/abs/2501.06336)：评测生成图像的多视角一致性。核心思想：衡量不同生成视角是否保持共同的三维结构，从而暴露单图质量指标看不到的空间一致性问题。
- [IE-Bench](https://arxiv.org/abs/2501.09927)：用 source-aware 的人工意见分评测文本驱动图像编辑。核心思想是同时对照编辑提示和源图像判断结果，使编辑质量更贴近人类感知，而不只看图文对齐。
- [T2ISafety](https://arxiv.org/abs/2501.12612)：评测文生图模型中的公平性、毒性和隐私风险。核心思想：组织安全提示与判定协议，使图像生成器不仅按视觉质量和提示对齐比较，也要检查有害、偏见或隐私相关输出。
- [Q-Eval-100K](https://arxiv.org/abs/2503.02357)：评测 text-to-vision 内容的视觉质量和提示对齐。核心思想：通过大规模人工标注生成视觉输出，使图像和视频式生成的质量与提示遵循不再只依赖小规模偏好样本。
- [WISE](https://arxiv.org/abs/2503.07265)：评测文生图中的世界知识语义一致性；核心思想是检查生成图像是否保持常识性物体关系、空间布局和现实约束，而不只是匹配提示词。
- [ICE-Bench](https://arxiv.org/abs/2503.14482)：在统一基准中评测图像创建和编辑。核心思路是用共享任务和指标比较生成与编辑系统，从而同时诊断图像创建和图像修改能力。
- [LeX-Bench](https://arxiv.org/abs/2503.21749)：评测文生图系统中的视觉文字生成。核心思想：围绕文字渲染构造高质量提示和图像样本，测试生成器能否产出清晰、符合指令的文字，而不只是生成看似合理的周边画面。
- [GPT-ImgEval](https://arxiv.org/abs/2504.02782)：诊断 GPT-4o 类多模态生成器的图像生成质量。核心思路是组织生成提示和评测维度，暴露图像生成器在指令遵循、视觉保真和语义一致性上的失败。
- [Envisioning Beyond the Pixels](https://arxiv.org/abs/2504.02826)：评测推理驱动的视觉编辑能力。核心思想：检验编辑系统能否遵循语义与逻辑约束，而不只是匹配低层视觉指令。
- [LMM4LMM](https://arxiv.org/abs/2504.08358)：用大多模态模型评测大多模态图像生成。核心思路是以多模态裁判衡量生成图像质量和对齐程度，使图像生成比较比零散偏好判断更结构化。
- [ScienceT2I](https://arxiv.org/abs/2504.13129)：评估文生图中的科学合理性。核心思路是使用专家标注的科学提示、对抗图像对和独立测试集，暴露视觉上逼真但违反科学概念或物理真实性的生成结果。
- [Complex-Edit](https://arxiv.org/abs/2504.13143)：评测复杂度可控的图像编辑。核心思路是生成类似思维链的编辑指令并控制难度，使编辑模型接受组合式、多步骤意图测试，而不只处理简单局部修改。
- [Scalable Human-aligned Benchmark for Text-guided Image Editing](https://arxiv.org/abs/2505.00502)：用人类偏好对齐的判断评估文本引导图像编辑。核心思路：围绕编辑是否满足用户指令和人类质量偏好来扩展评测，而不只依赖低层视觉指标。
- [WorldGenBench](https://arxiv.org/abs/2505.01490)：评测融合世界知识的推理驱动文本到图像生成能力。核心思路是检验图像生成模型是否遵守常识和事实性世界约束，而不只是匹配局部提示词。
- [UniEval](https://arxiv.org/abs/2505.10483)：面向多模态理解与生成模型提供统一的整体评估。核心思路是减少分散任务评测带来的割裂，在同一框架下同时比较统一模型的理解能力与生成行为。
- [GIE-Bench](https://arxiv.org/abs/2505.11493)：评估有 grounding 约束的文本引导图像编辑。核心思路：检验编辑是否既遵循文本指令，又保持与源图像的对应关系，而不只是生成看似合理的变化。
- [CompBench](https://arxiv.org/abs/2505.12200)：评测复杂指令引导的图像编辑。核心思路是强化组合式编辑指令，衡量编辑模型是否同时完成目标修改并保持周边视觉一致性。
- [KRIS-Bench](https://arxiv.org/abs/2505.16707)：评测智能图像编辑模型；核心思想是在更复杂的编辑指令下检查模型是否保持语义意图、空间一致性和编辑保真度。
- [OmniGenBench](https://arxiv.org/abs/2505.18775)：评测 50 多类任务上的全能多模态生成能力。核心思路是将异构生成任务放入统一基准协议，使文本、图像、音频、视频及跨模态生成系统能够在单一任务指标之外进行比较。
- [MMIG-Bench](https://arxiv.org/abs/2505.19415)：评测结合文本提示和多视角参考图的多模态图像生成。核心思想：把文生图、图像条件生成、编辑和概念一致性检查放入统一协议，并用带标注主体和可解释维度诊断组合语义与常识一致性。
- [TIIF-Bench](https://arxiv.org/abs/2506.02161)：评测文生图模型的指令遵循能力。核心思路是将提示词遵循转化为专项基准，用于比较生成图像是否满足指定约束。
- [ByteMorph](https://arxiv.org/abs/2506.03107)：评测带有非刚性运动的指令引导图像编辑。核心思路是测试编辑系统能否处理形变、姿态变化和类运动变换，同时保持对象身份和场景连贯性。
- [RefEdit-Bench](https://arxiv.org/abs/2506.03448)：评测复杂场景中基于指代表达的指令式图像编辑。核心思想是把编辑目标绑定到 RefCOCO 风格的真实对象引用，使模型必须找准目标实体并保持源图像其他区域。
- [ComplexBench-Edit](https://arxiv.org/abs/2506.12830)（[代码](https://github.com/llllly26/ComplexBench-Edit)）：评估复杂指令驱动的图像编辑。核心思路是强调多指令和链式依赖编辑，并衡量未修改区域保持程度，避免模型只完成某个操作却破坏图像其他部分仍被高估。
- [AIGODI Quality Assessment](https://arxiv.org/abs/2506.21925)：评测 AI 生成全景图像的质量与显著性。核心思想：面向 VR/AR 风格的 360 度生成图，结合畸变感知质量评估和显著性预测，把全景伪影与普通单视角图像生成失败区分开。
- [MVGBench](https://arxiv.org/abs/2507.00006)：评估多视角生成模型。核心思路：检查生成器能否在多个视角之间保持对象、场景和视角一致性，而不是只评价单张图像质量。
- [LMM4Edit / EBench-18K](https://arxiv.org/abs/2507.16193)（[代码](https://github.com/IntMeGroup/LMM4Edit)）：用人工偏好标注和 LMM 评分评估文本引导图像编辑。核心思路是覆盖感知质量、编辑对齐、属性保持和任务相关 QA，使图像编辑评测更贴近人类判断。
- [7Bench](https://arxiv.org/abs/2508.12919)：评测布局引导的文生图生成；核心思想是同时考察图像生成模型对显式空间布局和文本提示的遵循能力，为更宽泛的多模态生成评测补充 layout control 维度。
- [EdiVal-Agent](https://arxiv.org/abs/2509.13399)：面向多轮图像编辑的对象中心评测框架。核心思路是用可扩展、细粒度检查让编辑轨迹可审计，而不只判断最终图像效果。
- [Text-to-Image Models Leave Identifiable Signatures](https://arxiv.org/abs/2510.06525)：研究生成图像模型 leaderboard 的安全性。核心思想：显示生成图像可高精度反推出匿名模型身份，使排名操纵和提示选择攻击成为匿名 arena 的具体可靠性风险。
- [DREAM](https://arxiv.org/abs/2510.10053)：评什么：深度伪造照片真实感评估。核心思想：测试模型或评审器能否区分并评价合成人脸图像的真实感，补充通用图像生成质量和安全评测。
- [GIR-Bench](https://arxiv.org/abs/2510.11026)：评估统一多模态模型的推理式图像生成能力。核心思路是测试理解与生成一致性、受推理约束的视觉合成，以及复杂视觉任务上的泛化能力。
- [ViVerBench](https://arxiv.org/abs/2510.13804)（[项目页](https://omniverifier.github.io/)；[数据集](https://huggingface.co/datasets/comin/ViVerBench)）：评什么：视觉结果的验证（verification）能力；核心思想：把视觉理解/生成的关键判断转成可核验子任务，强调“能否证明自己对/错”。
- [UniGenBench++](https://arxiv.org/abs/2510.18701)：评测文本到图像生成中的语义对齐。核心思路是用统一语义评测协议测试生成图像是否满足提示含义，而不只看视觉质量高低。
- [UniREditBench](https://arxiv.org/abs/2511.01295)：评估多模态生成模型的推理式图像编辑能力。核心思路是测试模型能否处理多对象交互、规则约束场景和隐式推理需求，而不只是简单属性修改。
- [Q-REAL](https://arxiv.org/abs/2511.16908)：评什么：AI 生成内容的真实感和合理性。核心思想：评估生成结果是否不仅观感精致，而且符合现实世界约束下的 plausibility。
- [Beyond Words and Pixels](https://arxiv.org/abs/2511.18271)：评测生成模型中的隐式世界知识推理。核心思路是检查生成结果是否遵守未明说的现实世界约束，而不只是匹配提示词表面信息。
- [SPQR](https://arxiv.org/abs/2511.19558)：面向 text-to-image diffusion model 安全对齐方法的标准化 benchmark。核心思想：用统一 T2I 协议比较现代安全机制，而不是依赖零散红队样例。
- [UnicEdit-10M](https://arxiv.org/abs/2512.02790)：评估带推理约束的大规模图像编辑。核心思路：把大规模编辑数据与统一验证结合起来，同时检查指令遵循、推理约束和编辑质量。
- [I2I-Bench](https://arxiv.org/abs/2512.04660)：评测图像到图像编辑模型。核心思路是将图像编辑任务组织成基准套件，用于比较不同系统的指令遵循、内容保持和编辑质量。
- [LongT2IBench](https://arxiv.org/abs/2512.09271)：用图结构标注评测长文本到图像生成。核心思想：测试图像生成器能否保留长提示中的实体、属性、关系和约束，而不是只匹配短 caption。
- [TextEditBench](https://arxiv.org/abs/2512.16270)：评测超越简单渲染的推理感知文本编辑。核心思路是测试图像编辑器能否在上下文中修改文字，同时保持语义意图、版面和视觉一致性。
- [GenEval 2](https://arxiv.org/abs/2512.16853)：研究文生图评测中的基准漂移问题。核心思路：更新并诊断图像生成评测，使模型比较在系统逐渐适应旧基准分布后仍然有意义。
- [VIBE](https://arxiv.org/abs/2602.01851)：评估图像编辑中的视觉指令遵循能力。核心思想：用系统化的视觉编辑任务测试模型是否在编辑后保持语义和逻辑约束，而不只是做表层视觉修改。
- [GenArena](https://arxiv.org/abs/2602.06013)：用更贴近人类偏好的比较协议评估视觉生成任务。核心思路：通过 arena 式或偏好对齐评估，使图像和视觉生成输出的评价更接近人类判断。
- [WorldEdit](https://arxiv.org/abs/2602.07095)：用知识驱动的提示和检查评估开放世界图像编辑。核心思路：测试编辑模型是否理解世界知识与指令语义，而不只是执行局部视觉变换。
- [MICON-Bench](https://arxiv.org/abs/2602.19497)：评估统一多模态模型中的多图上下文图像生成能力。核心思想：测试生成器能否连贯利用多张参考图，而不是把每个视觉上下文孤立处理。
- [InEdit-Bench](https://arxiv.org/abs/2603.03657)：评估智能图像编辑中的中间逻辑路径。核心思路是要求模型在状态变化、动态过程、时间序列和科学模拟等场景中生成连贯的多步视觉变化，从而暴露仅看最终图像时难以发现的推理缺陷。
- [DSH-Bench](https://arxiv.org/abs/2603.08090)：用难度与场景感知的层级主题分类评测 subject-driven text-to-image generation。核心思想：按场景和难度区分主体保持失败，而不是只报告通用提示-图像对齐分数。
- [WeEdit](https://arxiv.org/abs/2603.11593)：评估以图中文字为核心的图像编辑能力，覆盖双语和多语种编辑操作。核心思路是用 HTML 自动生成的大规模编辑数据配合标准化基准，分别考察指令遵循、文字清晰度和非目标区域保持能力。
- [Omni IIE Bench](https://arxiv.org/abs/2603.16944)：评测实用场景中的指令式图像编辑能力。核心思想：用 single-turn consistency 与 multi-turn editing behavior 两条诊断轨道，考察模型在不同语义尺度编辑中的稳定性，而不只看混合任务平均分。
- [TIEdit](https://arxiv.org/abs/2603.19775)：评测代表性文本引导图像编辑任务。核心思想：将源图、编辑提示和多个系统生成的编辑结果配对，评估感知质量、指令对齐和内容保持，并分析自动 LLM 评审为何与人类感知不一致。
- [MultiBind](https://arxiv.org/abs/2603.21937)：评测多主体图像生成中的属性错绑问题。核心思想：使用多个主体参考图、背景参考和按实体编号的提示词，检查生成图像是否把属性保持或编辑在正确主体上，而不是在不同人物之间串换。
- [BizGenEval](https://arxiv.org/abs/2603.25732)：评测商业视觉内容生成。核心思路是用面向业务的视觉创作任务比较生成器是否满足版式、品牌、指令和内容质量要求。
- [CREval](https://arxiv.org/abs/2603.26174)：评估复杂指令下的创意图像编辑能力。核心思路：把复杂用户意图拆成可自动检查的维度，使图像编辑评估比粗粒度视觉偏好更具可解释性。
- [ImagenWorld](https://arxiv.org/abs/2603.27862)：用可解释人工评估在开放真实任务上压力测试图像生成模型。核心思想：评估生成图像是否满足现实任务约束，并使人工判断可追溯。
- [KITTEN](https://www.semanticscholar.org/paper/6ccd8fbaa9578bb6a3f7835329515353477d6ad3)：通过知识融合检查评估面向视觉实体的图像生成。核心思路：测试生成器能否保留实体特定的视觉事实与知识，而不只是生成看似合理的通用图像。
- [SCALE / ZoneMaestro](https://arxiv.org/abs/2605.02537)：评估不规则室内场景生成中的复杂空间编排。核心思路是用密集空间关系、功能区域和非凸布局施压，使空间推理评测超越简单物体摆放。
- [DynT2I-Eval](https://arxiv.org/abs/2605.06170)：用动态生成提示评测文生图模型。核心思想：构建结构化视觉语义空间，并在主体、逻辑约束、环境和构图等维度持续采样新提示，以降低 benchmark contamination，并诊断对齐、感知质量和美学表现。

## 4.1.4 Agent Harness

- [ComfyBench / ComfyAgent](https://arxiv.org/abs/2409.01392)（[开源代码](https://github.com/xxyQwQ/ComfyBench)；[项目页](https://xxyqwq.github.io/ComfyBench)）：ComfyUI workflow 生成与评测 harness，LLM agent 学习文档、生成可执行 workflow、运行并用 pass/resolve 式指标评分。
- [ComfyGPT](https://arxiv.org/abs/2503.17671)（[开源代码](https://github.com/comfygpt/comfygpt)；[项目页](https://comfygpt.github.io/)）：面向 ComfyUI workflow 生成的自优化多 agent 系统，包含 flow generation、refinement 和 execution agents。
- [CIGEval](https://arxiv.org/abs/2504.07046)：面向条件图像生成的 agentic evaluation harness。核心思想是让 LMM 选择工具并围绕多类条件生成任务做细粒度判断，使图像生成评测成为工具介入的工作流，而不是单一标量指标。
- [ComfyMind](https://arxiv.org/abs/2505.17908)（[开源代码](https://github.com/EnVision-Research/ComfyMind)）：基于 ComfyUI 的通用生成规划与反馈框架。核心思路是使用树形工作流规划和执行反馈，把复杂多模态生成任务分解、执行并修复，而不是只依赖一次性提示。
- [ComfyUI-Copilot](https://arxiv.org/abs/2506.05010)（[开源代码](https://github.com/AIDC-AI/ComfyUI-Copilot)）：ComfyUI workflow 生命周期助手，覆盖生成、调试、重写、参数调优和 ComfyUI 生态内的 agentic workflow 操作；其公开仓库目前说明官方 API 服务已暂停，因此实际部署需要用户自备 LLM API key 与 base URL。
- [Maestro](https://arxiv.org/abs/2509.10704)：面向自我改进文生图的智能体编排框架。核心思路：协调生成、批评和修订智能体，让图像输出通过显式流程改进，而不是依赖单次模型调用。
- [PromptSculptor](https://arxiv.org/abs/2509.12446)：面向文生图提示词优化的多 agent harness。核心思想：把提示词分析、改写和质量反馈拆给协作 agent，在基础生成模型之外迭代提升图像生成提示。
- [OmniVerifier](https://arxiv.org/abs/2510.13804)（[开源代码](https://github.com/Cominclip/OmniVerifier)）：面向视觉结果验证的生成式 verifier；可把“视觉判断”改造成显式验证与自我修正闭环，并在 ViVerBench 等上对比评测。
- [ComfySearch](https://arxiv.org/abs/2601.04060)：用于 ComfyUI 工作流的自主探索 harness。核心思路是在严格工作流约束下搜索组件图，并用验证引导构建过程，使 Agent 能生成可执行且质量更高的 ComfyUI pipeline。
- [coDrawAgents](https://arxiv.org/abs/2603.12829)：面向组合式图像生成的多智能体对话 harness。核心思想：拆分 interpreter、planner、checker 与 painter 等角色，在生成前迭代地约束复杂对象布局和属性。
- [EditRefiner](https://arxiv.org/abs/2605.07457)：面向图像编辑优化的人类对齐智能体框架。核心思路是将图像编辑封装为迭代优化流程，由基础生成器之外的反馈、对齐检查和修订环节推动改进。

## 4.1.5 Skill

- [comfyui-workflow](https://github.com/marduk191/qwen3_mcp/tree/6921bf522e0eb30c84e133777c0580984ea51ffe/skills/comfyui-workflow) 是通用 ComfyUI workflow skill，覆盖 text-to-image、image-to-image、inpainting、ControlNet、LoRA、IPAdapter、Flux、SDXL 和 SD3.5 工作流模式。
- [comfyui-character-gen](https://skills.sh/mckruz/comfyui-expert/comfyui-character-gen) 适合身份保持的角色生成、基于参考图的一致性、face preservation 和受控角色变体。
