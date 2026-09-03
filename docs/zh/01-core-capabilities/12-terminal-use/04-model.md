# 1.12.4 Model

- [BYOS: Knowledge-driven Large Language Models Bring Your Own Operating System More Excellent](https://arxiv.org/abs/2503.09663)：把 LLM 驱动的 Linux kernel tuning 约束在结构化 OS 知识中，通过知识构建、配置空间收缩和持续知识维护减少跨 workload 与 kernel 版本的幻觉配置。
- [TerminalTraj](https://arxiv.org/abs/2602.01244)：从 Dockerized repository 生成终端 agent 轨迹，包含可执行任务、验证器和已验证 action trace，用于训练终端能力。
- [TermiGen](https://arxiv.org/abs/2602.07274)：合成高保真终端环境和鲁棒恢复轨迹，缓解 execution-grounded 训练数据稀缺。
- [TACO](https://arxiv.org/abs/2604.19572)：自进化终端上下文压缩方法，从交互轨迹中学习可复用观察压缩规则。
- [SkillSynth](https://arxiv.org/abs/2604.25727)：使用 scenario-mediated skill graph 合成可执行终端任务和最小执行轨迹，用于训练与评测。
- [Terminal-World](https://arxiv.org/abs/2605.20876)：通过 agent skills 扩展 terminal-agent environments。核心思想：用 skills 自动合成终端 agent 任务、环境和 teacher trajectories，构造 5,723 个训练环境，并用这些生成轨迹训练 Terminal-World models。
- [LiteCoder-Terminal](https://arxiv.org/abs/2605.29559)（[代码和资源](https://github.com/icip-cas/LiteCoder)）：用 11,255 条合成终端轨迹做可规模化 SFT，在 602 个可验证环境中用 Decoupled Clip and Dynamic sAmpling Policy Optimization 做强化学习，并继续在标准 benchmark 任务上 RL，训练具备终端能力的语言智能体。
- [chatHPC: Empowering HPC users with large language models](https://doi.org/10.1007/s11227-024-06637-1)：描述面向 HPC 问答与脚本生成的端到端 LLM 对齐管线，包含预训练、微调、服务部署、自指令数据生成，以及 coherence、semantic accuracy、hallucination 和 privacy 评测。
