# 1.12.3 Bench

- [CSR-Bench: Benchmarking LLM Agents in Deployment of Computer Science Research Repositories](https://arxiv.org/abs/2502.06111)：CSR-Bench 评测 agents 部署计算机科学研究仓库，覆盖依赖、环境和执行验证。
- [LLM-Supported Natural Language to Bash Translation](https://arxiv.org/abs/2502.06858)：提供经验证的自然语言到 Bash 数据集和执行感知等价评测。
- [SandboxEval: Towards Securing Test Environment for Untrusted Code](https://arxiv.org/abs/2504.00018)：SandboxEval 关注不可信代码的测试环境安全，适合 terminal/code execution 场景的 benchmark。
- [Code Execution Reasoning Coherency and Consistency](https://arxiv.org/abs/2510.15079)：评估 LLM 的代码执行推理是否连贯一致，为终端邻近的 execution reasoning 补充 benchmark 轴。
- [Terminal-Bench 2.0](https://www.tbench.ai/registry/terminal-bench/2.0)（[2.0 官方榜单](https://www.tbench.ai/leaderboard/terminal-bench/2.0)；[2.1 官方榜单](https://www.tbench.ai/leaderboard/terminal-bench/2.1)；运行入口：[Harbor / Terminal-Bench 运行入口](https://harborframework.com/docs/running-tbench)；论文：[Terminal-Bench](https://arxiv.org/abs/2601.11868)；[开源代码](https://github.com/laude-institute/terminal-bench)）：评什么：真实 Linux 终端环境中的端到端任务完成，官方注册页当前展示 89 个任务。
  核心思想：每个任务由 instruction、Docker 环境与测试脚本定义，agent 必须通过读写文件、运行命令、安装/调用工具、调试失败并产出可验证结果来通过自动评测。
- [Endless Terminals](https://arxiv.org/abs/2601.16443)：扩展面向终端 agent 的强化学习环境。核心思想是把终端任务和轨迹生成为训练与评测流水线，而不是只依赖固定终端 benchmark 数据集。
- [DevOps-Gym](https://arxiv.org/abs/2601.20882)（[项目页](https://www.devops-gym.com/)）：评什么：软件 DevOps cycle 中的长程终端任务，例如部署、配置、监控、故障定位与回归验证。
  核心思想：把任务拆进真实仓库、服务环境和命令行流程，强调 agent 在日志、配置、依赖、测试和运行时状态之间的闭环恢复。
- [CLI-Gym](https://arxiv.org/abs/2602.10999)：评什么：可规模化生成的 CLI 环境密集型任务。
  核心思想：把 Dockerfile 的健康环境历史反向还原为带故障的早期状态，通过可执行反馈生成依赖、系统配置和运行时修复类终端任务。
- [LongCLI-Bench](https://arxiv.org/abs/2602.14337)（[开源代码](https://github.com/finyorko/longcli-bench)）：评什么：命令行界面中的长程 agentic programming。
  核心思想：从课程作业和真实工作流中整理长链路任务，并用 fail-to-pass、pass-to-pass 和 step-level scoring 定位 agent 在规划、执行和回归保护中的失败点。
- [LinuxArena](https://arxiv.org/abs/2604.15384)（[官方 arena/results 页面](https://www.linuxarena.ai/)）：评测 agent 在真实多服务 Linux 生产环境中的表现。核心思想是把合法软件工程任务与数据外泄、后门等 side task 配对，使终端能力与控制失败可以同时衡量。
- [Terminal Wrench](https://arxiv.org/abs/2604.17596)（[开源代码](https://github.com/few-sh/terminal-wrench)）：评什么：终端 benchmark 中可被 reward hacking 绕过的环境和轨迹。
  核心思想：保留 331 个 reward-hackable 终端环境与 3,632 条 exploit trajectories，专门揭示 verifier 被绕过、输出伪造和环境劫持等评测可靠性风险。
- [SkillSynth](https://arxiv.org/abs/2604.25727)：评什么：终端任务与执行轨迹的可规模化合成。
  核心思想：用 scenario-mediated skill graph 采样命令行 workflow，再经多代理 harness 实例化为可执行任务，为 Terminal-Bench 类环境补充任务生成和训练数据来源。
- [What Makes a Good Terminal-Agent Benchmark Task: A Guideline for Adversarial, Difficult, and Legible Evaluation Design](https://arxiv.org/abs/2604.28093)：给出 terminal-agent benchmark 的任务设计准则；核心思想是让任务具备对抗性、难度、可读性和稳健验证，而不是快速拼装的 shell 谜题。
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)（[项目页](https://claw-eval-live.github.io/)；[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：评什么：持续更新的真实 workflow agent 任务。
  核心思想：从公开 workflow-demand signals 和 ClawHub skill 信号生成带固定 fixture、服务、workspace 和 grader 的发布快照，用轨迹、审计日志、服务状态和产物验证执行。
- [SREGym](https://arxiv.org/abs/2605.07161)（[官方榜单](https://sregym.com/leaderboard)；[开源代码](https://github.com/SREGym/SREGym)）：评什么：AI SRE agent 在高保真生产故障场景中的诊断与缓解。
  核心思想：在真实云原生系统栈上注入多层故障、噪声和复杂 failure mode，让 agent 面对接近生产系统的日志、指标、配置和修复闭环。
- [MMTB / MultiMedia-TerminalBench](https://arxiv.org/abs/2605.10966)（[项目页](https://mm-tbench.github.io/multimedia-terminal-bench/)；[开源代码](https://github.com/mm-tbench/multimedia-terminal-bench)；[数据集](https://huggingface.co/datasets/mm-tbench/mmtb-media)）：评什么：终端 agent 处理音频、视频等多媒体文件任务的能力。
  核心思想：把 Terminal-Bench 的文本/代码/结构化文件工作流扩展到多媒体证据读取、文件转换和跨文件动作选择，并配套 Terminus-MM harness。
- [TAB / Task Alignment Benchmark](https://arxiv.org/abs/2605.12233)：评什么：终端 agent 是否能选择性使用环境里的相关指令、忽略无关或误导性指令。
  核心思想：从 Terminal-Bench 2.1 派生任务，在自然文件、README、注释和日志中同时放入必要线索与干扰线索，补足“盲目跟随环境文本也能过关”的评测盲点。
- [ClawForge](https://arxiv.org/abs/2605.14133)：评什么：可执行 command-line agent benchmark 的生成。
  核心思想：从场景模板、初始化状态、参考轨迹和 validators 编译可复现任务，重点考察 agent 是否会检查已有状态、处理冲突产物并达到正确最终状态。
- [TerminalWorld](https://arxiv.org/abs/2605.22535)：基于真实终端任务评测 agent。核心思想：从 80,870 条真实 terminal recordings 生成 1,530 个 validated tasks，并提供 200 个任务的 Verified 子集，使终端评测来自真实命令行工作流，而不只依赖人工编写的 shell 谜题。
