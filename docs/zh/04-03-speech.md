# 4.3 语音模型

> 上级章节：4. 多模态

说明：本页收纳语音、音频、voice agent、音乐、口语对话和音频安全评测，以及音频专用 agent harness。

## 4.3.1 Bench

- [OmniBench](https://arxiv.org/abs/2409.15272)（[开源代码](https://github.com/multimodal-art-projection/OmniBench)，[数据集](https://huggingface.co/datasets/m-a-p/OmniBench)）：评什么：omni-language models 的视觉、听觉和文本三模态理解。核心思想：检查模型能否同时识别、解释并推理多种模态，而不是把多模态评测局限为图文任务。
- [MusicEval](https://arxiv.org/abs/2501.10811)：用专家评分样本评测文生音乐生成。核心思想：以专业音乐判断支撑生成音乐质量与提示对齐的自动评测，补充 TTA-Bench 旁边的音频生成评测空白。
- [Jailbreak-AudioBench](https://arxiv.org/abs/2501.13772)：评测 large audio-language models 的 jailbreak 威胁。核心思想：测试有害请求是否能通过语音或音频通道变化绕过安全机制，把安全评测从纯文本 jailbreak prompts 扩展到音频模态。
- [Talking Turns](https://arxiv.org/abs/2503.01174)：评测音频基础模型的对话轮转动态。核心思想：用轮转事件判别器和用户研究协议，测试语音对话系统能否避免过度重叠或沉默，并处理会话发言权切换。
- [Full-Duplex-Bench](https://arxiv.org/abs/2503.04721)：评测全双工口语对话模型的轮次转换能力。核心思想：检查语音系统能否同时听与说、适当打断并管理话轮变化，而不是只按孤立回合回应。
- [S2S-Arena](https://arxiv.org/abs/2503.05085)：评测 speech-to-speech 模型的副语言指令遵循能力。核心思想：检查口语对话系统能否按语气、韵律、情绪等非词汇线索执行指令，而不只是保持转写文本内容。
- [QualiSpeech](https://arxiv.org/abs/2503.20290)（数据集：[tsinghua-ee/QualiSpeech](https://huggingface.co/datasets/tsinghua-ee/QualiSpeech)）：评什么：auditory LLM 的低层语音质量理解。核心思想：用覆盖 11 类噪声与失真维度的自然语言质量描述和推理，补充单一音频分数式评测。
- [Vox-Profile](https://arxiv.org/abs/2505.14648)：评测语音基础模型对多样说话人与语音特征的刻画能力。核心思想：诊断 audio-language model 是否能识别说话人属性、发声状态和语音特征，而不是把语音输入简化为文字。
- [AudioTrust](https://arxiv.org/abs/2505.16211)：评测音频大语言模型的多维可信性。核心思想：围绕安全性、鲁棒性、隐私和可靠性等维度评估音频语言系统，而不是只把音频能力等同于识别准确率或感知质量。
- [JALMBench](https://arxiv.org/abs/2505.17568)：评测大音频语言模型的 jailbreak 脆弱性。核心思想：用大规模文本和音频样本、多个攻击方法、主流 LALM 与防御机制组成统一评测框架，使音频 jailbreak 鲁棒性能系统比较。
- [EmergentTTS-Eval](https://arxiv.org/abs/2505.23009)：评测 TTS 模型在复杂韵律、表现力和语言挑战上的能力；核心思想是用 model-as-a-judge protocol 衡量普通可懂度或自然度分数之外的语音生成行为。
- [SOVA-Bench](https://arxiv.org/abs/2506.02457)：评测基于 LLM 的语音助手对话能力。核心思想：在同一语音助手协议中同时评估通用知识、语音识别与理解、语义回复质量和声学生成质量。
- [MMSU](https://arxiv.org/abs/2506.04779)：评测多任务口语理解与推理。核心思路是检查全模态或音频语言模型能否直接围绕语音输入推理，而不只是依赖转写文本。
- [InstructTTSEval](https://arxiv.org/abs/2506.16381)：评测 TTS 系统对复杂自然语言指令的遵循能力；核心思想是检查语音生成器是否能满足风格、韵律、说话人和内容指令，而不只是生成可懂音频。
- [WildSpeech-Bench](https://arxiv.org/abs/2506.21875)：评测自然语音会话中的 audio LLM。核心思想：用真实会话语音测试模型对自发说话方式、互动上下文和自然声学变化的鲁棒性，而不只评干净脚本音频。
- [MULTIVOX](https://arxiv.org/abs/2507.10859)：评测多模态交互中的语音助手。核心思想：测试 spoken assistant 能否在面向用户的交互任务中协调语音、视觉或上下文证据，而不是只回答孤立音频问题。
- [WearVox](https://arxiv.org/abs/2507.11824)（[开源代码](https://github.com/facebookresearch/wearvox)）：评什么：可穿戴语音助手的上下文感知能力。核心思想：把语音、视觉和用户情境结合起来评估移动生活场景中的助手能力，补足桌面/网页工作流之外的现实助理形态。
- [TELEVAL](https://arxiv.org/abs/2507.18061)：评测中文真实交互场景中的 spoken language models；核心思想是同时衡量可靠内容完成和合适的互动策略，避免只用任务答案正确率评价语音 agent。
- [SpeechIQ](https://arxiv.org/abs/2507.19361)：通过覆盖记忆、理解和应用三个层级的 speech-agentic intelligence quotient 评测语音理解模型；核心思想是超越词错误率，在解释能力、下游问答、标注错误发现和幻觉信号上比较级联系统与端到端语音智能体。
- [C3](https://arxiv.org/abs/2507.22968)：评什么：复杂对话中的双语 spoken dialogue model。核心思想：用多轮语音互动检查模型是否能维持上下文、处理对话挑战并跨语言给出合适回应。
- [SpeechRole](https://arxiv.org/abs/2508.02013)：评测语音角色扮演 agent。核心思想：把大规模语音到语音角色扮演语料与 SpeechRole-Eval 结合起来，使 agent 不只按文本人格一致性评价，也要看交互能力、语音表现力和角色忠实度。
- [SpeechR](https://arxiv.org/abs/2508.02018)：评什么：大音频语言模型的语音推理能力。核心思想：检查模型能否基于 spoken audio evidence 做推断、比较和推理，而不只是转写或分类表层语音内容。
- [Omni-SafetyBench](https://arxiv.org/abs/2508.07173)：评测音视频大语言模型在联合模态输入下的安全性。核心思想：使用平行模态变体和跨模态安全一致性指标，使全模态安全评测不被简化为纯文本或纯图像拒答行为。
- [MSU-Bench](https://arxiv.org/abs/2508.08155)：评测多说话人会话场景中的语音理解。核心思想：以说话人为中心，从静态和动态说话人属性扩展到多说话人背景与互动理解，暴露单说话人音频 benchmark 难以发现的失败。
- [MMAU-Pro](https://arxiv.org/abs/2508.13992)：评测覆盖语音、非语音声音和音乐的整体音频通用智能。核心思想：提高音频语言评测的难度与覆盖面，使模型不只在孤立语音或音乐子任务上比较，而要接受更广泛的听觉理解测试。
- [MTalk-Bench](https://arxiv.org/abs/2508.18240)：用竞技场式比较和 rubric 协议评测多轮 speech-to-speech 模型。核心思想：沿对话轨迹评估口语互动，使评测覆盖连贯性、话轮管理和回复质量，而不止单轮语音任务。
- [AHELM](https://arxiv.org/abs/2508.21376)：对 audio-language model 做整体评测；核心思想是把音频中心任务与指标组织成统一 benchmark，使语音、声音和音乐理解能在同一协议下比较。
- [AudioMOS Challenge 2025](https://arxiv.org/abs/2509.01336)：评估音频平均主观评分的自动预测能力。核心思路：通过共享挑战协议比较系统是否能贴近人类对生成或处理音频的质量判断。
- [TTA-Bench](https://arxiv.org/abs/2509.02398)：从功能表现、可靠性和社会责任维度评估文本到音频生成。核心思路是在统一协议中结合多样提示、客观指标和大规模人工标注。
- [VoxRole](https://arxiv.org/abs/2509.03940)：评测基于语音的角色扮演 agent；核心思想是把 role-playing 评测从纯文本扩展到角色一致性、韵律、情绪和语音互动质量。
- [VStyle](https://arxiv.org/abs/2509.09716)：评什么：基于 spoken instructions 的 voice style adaptation。核心思想：检查语音系统能否理解声音风格要求并调整生成语音，而不只满足转写层面的正确性。
- [MMedFD](https://arxiv.org/abs/2509.19817)：评什么：真实医疗场景中的多轮全双工自动语音识别。核心思想：用存在重叠语音、轮次切换和专业术语的流式医疗对话，测试比干净单说话人 ASR 更困难的识别能力。
- [CMDAR](https://arxiv.org/abs/2509.22461)：评测中文多场景动态音频推理；核心思想是用多样音频场景和推理问题测试模型是否理解中文音频环境中的事件、上下文与时间变化。
- [XGC-AVQuiz](https://arxiv.org/abs/2509.23251)：评测真实与 AI 生成视频中的音视频内容理解；核心思想是用多任务覆盖时序对齐和跨模态推理，测试模型能否联合利用声音与视觉证据回答问题。
- [SingMOS-Pro](https://arxiv.org/abs/2510.01812)：评估歌声质量评估能力。核心思路：为生成或处理后的歌声音频提供专门基准，使人声演唱质量不只依赖通用音频评分。
- [Full-Duplex-Bench-v2](https://arxiv.org/abs/2510.07838)：带自动考官的全双工对话系统多轮评测框架。核心思想：把全双工语音评测从话轮转换片段扩展到更长的交互轨迹，测试打断、重叠语音处理和考官驱动的对话控制。
- [LISTEN](https://arxiv.org/abs/2510.10444)：评测 audio language model 是依赖词汇线索还是声学情绪线索。核心思想是用线索一致与冲突的受控设置，检查模型是否真正利用副语言声学证据，而不只是转写语音内容。
- [VCB Bench](https://arxiv.org/abs/2510.11098)：评测基于音频证据的 LLM 对话智能体。核心思想：把 spoken-dialogue 评测从转写文本扩展到多轮对话中的声学证据 grounding。
- [SpeechLLM-as-Judges / SpeechEval](https://arxiv.org/abs/2510.14664)：用结构化、可解释的 SpeechLLM 评审评估合成语音质量。核心思路是结合多语言语音片段与质量维度标注，使语音生成比较不再只依赖单一偏好分数。
- [VocalBench-DF](https://arxiv.org/abs/2510.15406)：评测 Speech-LLM 面对不流利语音时的鲁棒性；核心思想是用多维 disfluency taxonomy（含语障相关场景）测试语音模型是否能脱离干净音频仍保持可靠交互。
- [EchoMind](https://arxiv.org/abs/2510.22758)：通过相互关联的多层任务评测具备同理心的语音语言模型；核心思想是把语音内容理解、非词汇声学线索、情绪推理和同理回应生成串起来，而不是孤立评分。
- [MULTI-Bench](https://arxiv.org/abs/2511.00850)：评什么：多轮 spoken dialogue model 的情绪智能。核心思想：用交互式对话检查语音 agent 是否理解情感线索、维持情绪上下文，并在多轮中做出合适回应。
- [SpeechJudge](https://arxiv.org/abs/2511.07931)：评测语音自然度判断能力，并配套大规模人工偏好语音对。核心思想是把 speech/audio LLM 裁判与人类对自然度和可懂度的偏好对齐比较，避免合成语音评估只看转写准确率或通用音频质量。
- [SACRED-Bench](https://arxiv.org/abs/2511.10222)：评测针对多模态 LLM 的语音-音频组合攻击。核心思想：组合有害与无害语音、非语音音频和多说话人对话，使音频安全测试覆盖隐藏在复杂听觉场景中的黑盒攻击。
- [MTR-DuplexBench](https://arxiv.org/abs/2511.10262)：评测全双工语音语言模型的多轮对话能力。核心思想：把连续、可重叠的对话切分为轮次级评估，并测试单轮语音问答之外的对话性、上下文一致性和交互质量。
- [HPSU](https://arxiv.org/abs/2511.23178)：评测真实 spoken speech understanding 中的人类水平感知能力。核心思想：检验语音模型能否捕捉自然语音中的感知线索，而不止理解转写文本语义。
- [ICASSP 2026 HumDial Challenge](https://arxiv.org/abs/2601.05564)：评测类人语音对话系统，覆盖情绪智能与全双工交互两个赛道。核心思想：用真实人类对话和共享挑战协议，测试语音智能体能否同时具备情感理解和实时轮转能力。
- [RSA-Bench](https://arxiv.org/abs/2601.10384)：在真实声学场景中评测 audio large model。核心思想：用环境声音和真实声学条件检验听觉理解，而不是只测试干净语音输入。
- [AQUA-Bench](https://arxiv.org/abs/2601.12248)：评测包含无答案情形的音频问答。核心思想：测试 audio-language model 能否识别音频证据不足并拒答，而不是强行生成幻觉答案。
- [VoxPrivacy](https://arxiv.org/abs/2601.19956)：评什么：语音语言模型的交互式隐私意识。核心思想：测试语音助手在隐私敏感对话场景中的处理是否合适，补足主要关注识别、推理或生成质量的音频 benchmark。
- [LALM-as-a-Judge](https://arxiv.org/abs/2602.04796)：评测 large audio-language model 在多轮 spoken dialogue 中的安全评估能力。核心思想：测试音频语言 judge 能否沿着口语交互轨迹发现不安全行为。
- [Aegis](https://arxiv.org/abs/2602.07379)：红队评测 AI voice agents 的治理、完整性与安全风险。核心思想：建模真实语音 agent 部署流水线，并在银行、IT 支持、物流等场景中测试隐私泄漏、权限提升、资源滥用等对抗情形。
- [AdvBench-Omni](https://arxiv.org/abs/2602.10161)：评测跨模态语义冲突下的全模态安全性。核心思想：把不同模态中的有害语义解耦，检验文本、图像、音频或视频证据相互冲突时拒答行为是否仍然稳定。
- [Interspeech 2026 Audio Reasoning Challenge](https://arxiv.org/abs/2602.14224)：评什么：音频推理模型和 agent 的 reasoning process quality。核心思想：用 shared challenge 协议不只评价最终音频推理答案，也评价中间推理行为质量。
- [Human or Machine?](https://arxiv.org/abs/2602.24080)：提出面向 speech-to-speech 互动的图灵测试式评测。核心思想：直接比较人类与机器口语互动，使自然度、响应性和会话人类感不只依赖转写准确率。
- [PolyBench](https://arxiv.org/abs/2603.05128)：评什么：复调音频中的组合推理。核心思想：测试音频语言模型能否分离并推理重叠声音事件，而不是只给出粗粒度场景标签。
- [PARSA-Bench](https://arxiv.org/abs/2603.14456)：评测波斯语 audio-language model。核心思想：覆盖语音理解、副语言分析、文化音频理解、诗歌、传统音乐与 code-switching，使波斯语音频能力不被简化为翻译文本评测。
- [DEAF](https://arxiv.org/abs/2603.18048)：评什么：音频语言模型的声学忠实性。核心思想：诊断模型输出是否真正基于音频信号，把类似幻觉检测的可靠性评测扩展到听觉证据。
- [SID-Bench](https://arxiv.org/abs/2603.24144)：评测口语对话系统中的语义感知打断检测；核心思想是使用真实人类对话和 Average Penalty Time 指标，在全双工交互中同时衡量误触发打断与响应过慢的代价。
- [Full-Duplex-Bench-v3](https://arxiv.org/abs/2604.04847)：评测全双工语音智能体在真实口语不流畅条件下的工具使用能力；核心思想是把真人音频与链式 API 调用场景配对，并同时评估准确率、时延和轮次管理，使语音工具智能体不只在干净转写文本上做函数调用。
- [AudioSafetyBench / AudioGuard](https://arxiv.org/abs/2604.08867)：评测音频系统在原生有害声音事件、高风险说话人属性、冒充、语音与内容组合风险以及非语音声音上的安全性。核心思路是把语音智能体安全做成基于政策分类的可测协议，而不是把它简化为“把不安全文本念出来”。
- [Jamendo-MT-QA](https://arxiv.org/abs/2604.09721)：面向多轨比较式音乐问答的基准，将音频与音乐评测从生成质量扩展到结构化聆听和比较。
- [HumDial-EIBench](https://arxiv.org/abs/2604.11594)：评什么：真人录制多轮音频对话中的情绪智能。核心思想：用真实语音交互而非纯转写文本，测试音频语言模型能否在多轮中识别并回应情感线索。
- [NVBench](https://arxiv.org/abs/2604.16211)：评测包含非语言发声的语音合成；核心思想是考察语音生成系统能否处理笑声、叹息、呼吸等非语言声音事件，而不只评价普通语音内容。
- [VIBE / Voice-Induced Bias Evaluation](https://arxiv.org/abs/2604.17248)：通过真实语音评测 large audio-language model 的开放式偏见。核心思想：检查声音线索和口语表达是否会改变模型判断或回复，把偏见评测从纯文本提示扩展到语音输入。
- [MINT-Bench](https://arxiv.org/abs/2604.17958)：评什么：文本转语音系统的多语言指令遵循。核心思想：测试语音生成能否跨语言遵循内容、风格、语种和控制指令，而不只是生成可懂音频。
- [SpeechParaling-Bench](https://arxiv.org/abs/2604.20842)：评测具备副语言信息感知的语音生成。核心思想：把韵律、情绪、说话人风格等非文本语音因素纳入可测协议，而不是只用通用质量分数评价合成语音。
- [SongBench](https://arxiv.org/abs/2604.25937)：面向歌曲质量评估的细粒度多维基准，为音乐生成评测补充更具体的质量维度。
- [VoxDialogue](https://www.semanticscholar.org/paper/8b20adb0a2bd79dc0ec89e8a07417c0e3ccd1297)：评测口语对话系统是否能理解文字转写之外的信息。核心思想：用包含声学和副语言线索的多轮口语对话理解任务，检查音频语言模型是否能利用说话人状态与互动证据，而不只依赖转写文本语义。
- [MedMosaic](https://arxiv.org/abs/2605.00969)：评测多样化医学音频理解。核心思想：用大规模 medical audio benchmark 检查 audio-language model 是否能处理临床相关声学证据，而不只是在通用语音或音乐上表现良好。
- [Massive Sound Embedding Benchmark (MSEB)](https://arxiv.org/abs/2605.04556)：评什么：LLM 与音频模型在声音嵌入任务上的能力。核心思想：检验音频表征能否迁移到不同声音理解场景，补充语音问答或音频生成之外的 embedding 质量视角。
- [Expressive Appropriateness of Speech](https://arxiv.org/abs/2605.09413)：评测生成语音在丰富上下文中的表达适切性。核心思想：按照语境期望判断韵律、情感和表达方式，而不是只用通用自然度或可懂度指标评价语音质量。
- [Fine-Grained Multi-Dimensional Speech Understanding](https://arxiv.org/abs/2605.12036)：从细粒度多维度评测语音理解。核心思想：把数据流水线、benchmark 任务与模型比较结合起来，使 audio-language model 的评测超越转写式理解。

## 4.3.2 Agent Harness

- [AudioToolAgent](https://arxiv.org/abs/2510.02995)：面向 audio-language model 的 agentic harness。核心思想：将音频理解与生成任务路由到外部工具，使听觉智能体能拆解工作流，而不是只依赖单次端到端模型调用。
- [MIST](https://arxiv.org/abs/2605.06897)：面向智能家居的多模态语音工具调用助手框架。核心思想：把语音交互、多模态上下文和可执行设备工具连接起来，使工具使用型 agent 不局限于纯文本 API 调用。
