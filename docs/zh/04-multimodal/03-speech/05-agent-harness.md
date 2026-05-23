# 4.3.5 Agent Harness

- [AudioGPT](https://arxiv.org/abs/2304.12995)（[开源代码](https://github.com/AIGC-Audio/AudioGPT)）：早期音频 agent harness，使用 ChatGPT/LangChain 风格规划调用 speech、singing、audio 和 talking-head foundation models 作为工具。
- [WavJourney](https://arxiv.org/abs/2307.14335)（[开源代码](https://github.com/Audio-AGI/WavJourney)；[demo](https://audio-agi.github.io/WavJourney_demopage/)）：组合式音频创作 harness，把文本意图分解为故事、语音、音乐和音效生成 workflow。
- [ReelWave](https://arxiv.org/abs/2503.07217)：面向电影声音生成的多 agent harness。核心思想：由 Sound Director agent 通过多模态对话协调屏内与屏外声音 agent，在多场景视频叙事中对齐语音、音效、环境声与音乐。
- [Dopamine Audiobook](https://arxiv.org/abs/2504.11002)：用于情感化有声书生成的免训练多 Agent harness。核心思路是围绕多模态输入拆分语音设计和音频设计角色，在语义与时间上对齐语音、音效和音乐，并加入与人类偏好对齐的自动评测。
- [AudioGenie](https://arxiv.org/abs/2505.22053)：面向 multimodality-to-multiaudio generation 的 training-free multi-agent harness。核心思想是协调细粒度多模态理解、音频类型规划和生成等专门 agent，使 speech、music、song 与 sound effects 能从混合输入中合成。
- [AudioToolAgent](https://arxiv.org/abs/2510.02995)（[开源代码](https://github.com/GLJS/AudioToolAgent)）：面向 audio-language model 的 agentic harness。核心思想：将音频理解与生成任务路由到外部工具，使听觉智能体能拆解工作流，而不是只依赖单次端到端模型调用。
- [LVAS-Agent / LVAS-Bench](https://aclanthology.org/2025.emnlp-main.1133/)：面向长视频音频合成的多 agent harness。核心思想：把长视频配音分解为场景切分、脚本生成、音频设计与音频合成，并用 LVAS-Bench 的专业长视频集合进行系统评测。
- [Open Full-duplex Voice Agent](https://doi.org/10.1109/ASRU65441.2025.11434669)：一个开源全双工语音到语音智能体框架。核心思想：把标准文本 LLM 转化为能在全双工交互中听说并处理打断的语音智能体，而不是只进行回合式文本交换。
- Pipecat（[开源代码](https://github.com/pipecat-ai/pipecat)；[文档](https://docs.pipecat.ai/)）：开源 Python 框架，用于实时语音和多模态对话 agent，覆盖 STT、LLM、TTS、WebRTC/WebSocket transports、pipeline composition 和 subagents。
- LiveKit Agents（[开源代码](https://github.com/livekit/agents)；[文档](https://docs.livekit.io/agents/)）：面向 conversational multimodal voice agents 的实时 programmable-participant 框架，包含 tool calls、telephony、MCP integrations、job scheduling 和测试支持。
- TEN Framework（[开源代码](https://github.com/TEN-framework/ten-framework)）：实时多模态 conversational-AI 框架，包含 voice assistant examples、VAD、turn detection、memory、RTC/WebSocket integrations 和 agent orchestration 组件。
- [AudioFab](https://arxiv.org/abs/2512.24645)：用于工具学习的开源音频智能体框架。核心思想：把分散的音频处理工具封装到自然语言接口后，简化依赖管理，并提升复杂音频任务中的工具选择与协作效率。
- [MIST](https://arxiv.org/abs/2605.06897)：面向智能家居的多模态语音工具调用助手框架。核心思想：把语音交互、多模态上下文和可执行设备工具连接起来，使工具使用型 agent 不局限于纯文本 API 调用。
