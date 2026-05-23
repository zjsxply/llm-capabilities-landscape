# 1.12 终端调用

> 上级章节：1. 基础能力


说明：这条线关注 agent 是否能在真实命令行环境中完成长程、状态化、可验证的操作。
它和 `1.11 工具调用` 的差异在于，终端调用不是结构化 API 填参，而是要在文件系统、进程、依赖、日志、测试脚本与可能被破坏的中间状态之间持续决策。
因此这里更看重 `命令选择 -> 输出读取 -> 错误恢复 -> 环境感知 -> 产物验证` 的闭环。

## 1.12.1 Leaderboard

- [Terminal-Bench 2.0 官方榜单](https://www.tbench.ai/leaderboard/terminal-bench/2.0)：当前最重要的持续终端 agent 榜单，官方页面截至 2026-05-22 显示 143 个提交条目。
  榜单同时支持新模型和自定义 agent 提交，并要求不能修改 timeout 或资源限制，因此适合比较 agent harness 的真实终端执行、上下文压缩、完成检查、重试和验证策略。
- [Claw-Eval-Live](https://claw-eval-live.github.io/)：持续 workflow agent 榜单，任务跨终端、服务、文件和工具生态。
  它的价值在于用固定 fixture、审计日志、服务状态和产物验证跟踪 agent 在真实 workflow 里的长期表现，可作为 Terminal-Bench 之外的动态终端近邻榜单。
- [DevOps-Gym](https://www.devops-gym.com/)：更偏 DevOps/系统操作的终端近邻榜单/评测入口。
  它适合观察 agent 在部署、配置、监控和故障恢复中的命令行能力，与 Terminal-Bench 的单任务 Linux 环境形成互补。

## 1.12.2 Survey

- [OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use](https://arxiv.org/abs/2508.04482)：综述操作系统级交互、观察行动闭环、评测与安全；终端使用是其中的重要子场景。
- [AI Agentic Programming: A Survey of Techniques, Challenges, and Opportunities](https://arxiv.org/abs/2508.11126)：回顾 agentic programming 工作流中的命令执行、调试、测试与验证。
- [Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures](https://arxiv.org/abs/2604.03515)：归纳暴露 shell 执行、修复循环与环境控制的 coding-agent scaffold。

## 1.12.3 Bench

- [Terminal-Bench 2.0](https://www.tbench.ai/registry/terminal-bench/2.0)（[官方榜单](https://www.tbench.ai/leaderboard/terminal-bench/2.0)；运行入口：[Harbor / Terminal-Bench 运行入口](https://harborframework.com/docs/running-tbench)；论文：[Terminal-Bench](https://arxiv.org/abs/2601.11868)；[开源代码](https://github.com/laude-institute/terminal-bench)）：评什么：真实 Linux 终端环境中的端到端任务完成，官方注册页当前展示 89 个任务。
  核心思想：每个任务由 instruction、Docker 环境与测试脚本定义，agent 必须通过读写文件、运行命令、安装/调用工具、调试失败并产出可验证结果来通过自动评测。
- [DevOps-Gym](https://arxiv.org/abs/2601.20882)（[项目页](https://www.devops-gym.com/)）：评什么：软件 DevOps cycle 中的长程终端任务，例如部署、配置、监控、故障定位与回归验证。
  核心思想：把任务拆进真实仓库、服务环境和命令行流程，强调 agent 在日志、配置、依赖、测试和运行时状态之间的闭环恢复。
- [CLI-Gym](https://arxiv.org/abs/2602.10999)：评什么：可规模化生成的 CLI 环境密集型任务。
  核心思想：把 Dockerfile 的健康环境历史反向还原为带故障的早期状态，通过可执行反馈生成依赖、系统配置和运行时修复类终端任务。
- [LongCLI-Bench](https://arxiv.org/abs/2602.14337)（[开源代码](https://github.com/finyorko/longcli-bench)）：评什么：命令行界面中的长程 agentic programming。
  核心思想：从课程作业和真实工作流中整理长链路任务，并用 fail-to-pass、pass-to-pass 和 step-level scoring 定位 agent 在规划、执行和回归保护中的失败点。
- [Terminal Wrench](https://arxiv.org/abs/2604.17596)（[开源代码](https://github.com/few-sh/terminal-wrench)）：评什么：终端 benchmark 中可被 reward hacking 绕过的环境和轨迹。
  核心思想：保留 331 个 reward-hackable 终端环境与 3,632 条 exploit trajectories，专门揭示 verifier 被绕过、输出伪造和环境劫持等评测可靠性风险。
- [SkillSynth](https://arxiv.org/abs/2604.25727)：评什么：终端任务与执行轨迹的可规模化合成。
  核心思想：用 scenario-mediated skill graph 采样命令行 workflow，再经多代理 harness 实例化为可执行任务，为 Terminal-Bench 类环境补充任务生成和训练数据来源。
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)（[项目页](https://claw-eval-live.github.io/)；[开源代码](https://github.com/Claw-Eval-Live/Claw-Eval-Live)）：评什么：持续更新的真实 workflow agent 任务。
  核心思想：从公开 workflow-demand signals 和 ClawHub skill 信号生成带固定 fixture、服务、workspace 和 grader 的发布快照，用轨迹、审计日志、服务状态和产物验证执行。
- [SREGym](https://arxiv.org/abs/2605.07161)：评什么：AI SRE agent 在高保真生产故障场景中的诊断与缓解。
  核心思想：在真实云原生系统栈上注入多层故障、噪声和复杂 failure mode，让 agent 面对接近生产系统的日志、指标、配置和修复闭环。
- [MMTB / MultiMedia-TerminalBench](https://arxiv.org/abs/2605.10966)（[项目页](https://mm-tbench.github.io/multimedia-terminal-bench/)；[开源代码](https://github.com/mm-tbench/multimedia-terminal-bench)；[数据集](https://huggingface.co/datasets/mm-tbench/mmtb-media)）：评什么：终端 agent 处理音频、视频等多媒体文件任务的能力。
  核心思想：把 Terminal-Bench 的文本/代码/结构化文件工作流扩展到多媒体证据读取、文件转换和跨文件动作选择，并配套 Terminus-MM harness。
- [TAB / Task Alignment Benchmark](https://arxiv.org/abs/2605.12233)：评什么：终端 agent 是否能选择性使用环境里的相关指令、忽略无关或误导性指令。
  核心思想：从 Terminal-Bench 2.1 派生任务，在自然文件、README、注释和日志中同时放入必要线索与干扰线索，补足“盲目跟随环境文本也能过关”的评测盲点。
- [ClawForge](https://arxiv.org/abs/2605.14133)：评什么：可执行 command-line agent benchmark 的生成。
  核心思想：从场景模板、初始化状态、参考轨迹和 validators 编译可复现任务，重点考察 agent 是否会检查已有状态、处理冲突产物并达到正确最终状态。

## 1.12.4 Agent Harness

论文与方法类工作：

- Harbor（[开源代码](https://github.com/harbor-framework/harbor)；[官网](https://www.harborframework.com/)）：Terminal-Bench 2.0 生态中的通用 agent evaluation / RL environment 框架。
  它把任务定义、Docker 环境、agent 运行、轨迹和结果管理统一起来，适合作为 terminal benchmark-side harness。
- Terminus 2（[官方说明](https://www.tbench.ai/news/terminus)）：Terminal-Bench 团队维护的研究型终端 agent baseline。
  它刻意保持最小 loop：模型向 tmux 发送命令、读取 buffer、继续决策；适合作为评测底座，但强榜单结果通常还要靠更细的上下文、超时、输出截断与完成检查设计。
- Terminus-KIRA（[开源代码](https://github.com/krafton-ai/kira)；[技术博客](https://www.krafton.ai/blog/posts/2026-02-20-terminus_kira/terminus-en.html)）：KRAFTON 在 Terminus/Terminus 2 之上做的轻量终端 harness 改造。
  关键改动包括更强的自完成检查、replanning prompt、避免重型依赖安装的通用提示，以及从 tmux `push and wait` 改为更高效的 `pull` 式读取。
- [CAMEL-AI](https://arxiv.org/abs/2303.17760)（[开源代码](https://github.com/camel-ai/camel)）：多智能体协作框架；在终端任务里可作为角色化协作、工具调用与任务拆解的开放基线。
- [OpenHands](https://arxiv.org/abs/2407.16741)（[开源代码](https://github.com/OpenHands/OpenHands)）：通用软件开发 agent 平台；在终端评测中适合作为成熟开源工程 agent 的强基线。
- container-use（[开源代码](https://github.com/dagger/container-use)；[官网](https://container-use.com/)）：MCP server 和 CLI，为 coding agents 提供隔离容器、按分支隔离的工作区、命令历史和可检查日志，适合作为可审计执行与人工接管的终端 harness。
- [TerminalTraj](https://arxiv.org/abs/2602.01244)（[开源代码](https://github.com/multimodal-art-projection/TerminalTraj)）：面向 Dockerized environments 的终端 agent 轨迹生成框架。
  它关注可规模化构造环境、采集执行轨迹和生成训练数据，代表 terminal agent 从静态评测走向轨迹生产基础设施。
- [TermiGen](https://arxiv.org/abs/2602.07274)：高保真终端环境与鲁棒轨迹合成 pipeline。
  它用可验证环境、失败恢复轨迹和执行反馈补足 open-weight terminal agent 的训练/评测数据缺口，适合作为 Terminal-Bench 类任务的数据生成侧基础设施。
- [OpenSage / SageAgent](https://arxiv.org/abs/2602.16891)（[开源代码](https://github.com/opensage-agent/opensage-adk)）：AI-centric ADK 路线，让 agent 在执行中自生成拓扑、工具与层级记忆。
  SageAgent 在 Terminal-Bench 2.0、SWE-Bench Pro 与 DevOps-Gym 上报告了强结果；设计重点是动态子代理、工具/skill 合成与图式记忆，而不是只靠固定 prompt。
- [OPENDEV](https://arxiv.org/abs/2603.05344)（[开源代码](https://github.com/opendev-to/opendev)）：Rust 实现的 terminal-native coding agent。
  设计重点是双代理规划/执行架构、惰性工具发现、模型路由、上下文压缩和跨 session memory，适合作为 terminal-first agent scaffold 的工程蓝图。
- [Meta-Harness](https://arxiv.org/abs/2603.28052)（[开源代码](https://github.com/stanford-iris-lab/meta-harness)；[TerminalBench-2 artifact](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact)）：自动搜索并改写 LLM harness 代码的外层优化系统。
  在 TerminalBench-2 上，它从 Terminus 2 / Terminus-KIRA 等强基线出发，让 proposer agent 读取候选 harness 源码、得分与完整执行轨迹，在代码空间里发现更好的环境 bootstrap 与完成检查逻辑。
- [TACO](https://arxiv.org/abs/2604.19572)（[开源代码](https://github.com/multimodal-art-projection/TACO)）：面向终端 agent 的自演化 observation compression 层。
  它从交互轨迹中发现、精炼并复用结构化压缩规则，在保留任务关键信号的同时降低长程终端历史的 token 噪声。
Terminal-Bench 2.0 榜单中的主要 agent（截至 2026-05-22，官方榜单显示 143 个提交条目；下面按公开信息和每个 agent 的高分记录）：
- Codex CLI（[开源代码](https://github.com/openai/codex)；[README](https://github.com/openai/codex/blob/main/README.md)）：OpenAI 的终端 coding agent，在榜单中以 GPT-5.5 组合达到最高档；设计重点是本地/云端终端执行、文件编辑、命令运行、审批与多 agent 工作流。
- ForgeCode（[官方主页](https://forgecode.dev/)；[Agent 文档](https://forgecode.dev/docs/operating-agents/)）：Zsh-native 终端 coding harness；榜单高分显示其多代理、bounded context、快速工具纠错与模型切换策略对 Terminal-Bench 2.0 很关键。
- TongAgents（[官方主页](https://tongagents.mybigai.ac.cn/zh.html)；[BIGAI 新闻](https://www.bigai.ai/blog/news/%E4%BA%A7%E5%93%81%E8%83%BD%E5%8A%9B%E9%A2%86%E8%B7%91%E5%85%A8%E7%90%83%EF%BC%81%E9%80%9A%E7%A0%94%E9%99%A2-tongagents-%E7%99%BB%E4%B8%8A%E5%A4%9A%E9%A1%B9%E5%9B%BD%E9%99%85%E6%99%BA%E8%83%BD/)）：BIGAI 的行业智能体平台；公开介绍强调结构化推理、多层容错、命令超时后台挂起、流式分段返回与异步完成通知。
- Droid（[官方主页](https://factory.ai/)；[技术文章](https://factory.ai/news/terminal-bench)）：Factory 的自主工程 agent；早期 Terminal-Bench 结果突出“同一底模下 agent scaffold 决定差距”，设计关键词是端到端开发流程、自动测试、上下文组织与企业工程系统集成。
- Capy（[官方主页](https://capy.ai/)；[文档](https://docs.capy.ai/automations)）：并行 coding agents 开发环境；核心是 Captain 规划、Build agents 在隔离 VM 中执行、GitHub PR 回写与多任务并行。
- Simple Codex（[官方产品页](https://openai.com/codex)）：OpenAI 在 Terminal-Bench 2.0 上的简化 Codex 基线；适合作为“强模型 + 轻量官方 scaffold”的对照点。
- Mux（[开源代码](https://github.com/coder/mux)；[Agent 文档](https://mux.coder.com/agents)）：Coder 的多 agent 工作台；支持 project/global agent definitions、subagent workspace、远程/本地运行时与可控工具白名单。
- MAYA-V2（[官方主页](https://adya.ai/maya)）：ADYA 的终端/工程任务 agent；公开信息主要来自 Terminal-Bench 2.0 榜单与公司公告，适合作为高分闭源/产品型 harness 候选。
- Junie CLI（[官方主页](https://junie.jetbrains.com)）：JetBrains 的 CLI/IDE 侧 coding agent；适合作为 IDE 厂商进入终端 agent 评测的代表。
- CodeBrain-1（[开源代码](https://github.com/feelingai-team/CodeBrain)）：Feeling AI 的 coding agent “大脑”组件；公开介绍强调 LSP/代码索引驱动的有用上下文检索、执行逻辑优化与验证反馈。
- Ante（[官方主页](https://antigma.ai)）：Antigma Labs 的 in-terminal agent runtime；设计关键词是 Rust 单二进制、local-first、轻量 agent core、本地模型支持与大规模 self-organizing agents。
- IndusAGI Coding Agent（[官方主页](https://www.indusagi.com)）：榜单中的独立 coding agent；公开资料有限，主要按 Terminal-Bench 2.0 提交记录纳入。
- Crux：榜单中的 Roam/Crux agent；官方榜单给出的代码 URL 当前不可访问，因此这里先只按榜单名记录，避免保留失效链接。
- Deep Agents（[开源代码](https://github.com/langchain-ai/deepagents)）：LangChain 的深度代理框架；适合把规划、工具、上下文和长程任务状态组合成可复用 terminal workflow。
- II-Agent（[开源代码](https://github.com/Intelligent-Internet/ii-agent)；[官方博客](https://ii.inc/web/blog/post/ii-agent-chat)）：Intelligent Internet 的开源通用 agent；覆盖研究、编码、内容生成、文件搜索、code interpreter 与多模型切换。
- Warp（[官方主页](https://www.warp.dev/)）：AI-native terminal 产品；作为终端环境本身与 agent workflow 结合的代表，重点在 shell UI、命令解释、团队上下文与工作流自动化。
- Letta Code（[官方主页](https://www.letta.com/)）：Letta 的 coding agent 方向；适合关注 memory-first agent runtime 在终端任务中的效果。
- Abacus AI Desktop（[官方文档](https://abacus.ai/help/abacusai-desktop/introduction)）：Abacus.AI 的桌面/开发 agent；榜单表现可作为闭源 desktop agent 进入 terminal benchmark 的参考。
- Claude Code（[官方产品页](https://www.claude.com/product/claude-code)）：Anthropic 的终端 coding agent；设计关键词是 repo-aware 工作流、命令执行、文件编辑、memory、hooks、MCP 与 subagents。
- grok-cli（[开源代码](https://github.com/superagent-ai/grok-cli)）：面向 xAI/Grok 模型的开源 terminal-native agent；支持 headless 模式、子代理、Telegram 远程控制、hooks、sandbox 与项目级指令文件。
- Goose（[开源代码](https://github.com/block/goose)；[官方文档](https://block.github.io/goose/)）：Block 开源的本地/桌面/CLI agent；强调任意模型接入、MCP 扩展、recipes、session persistence 与本地可审计执行。
- [AgentFlow](https://arxiv.org/abs/2604.20801)：多代理 harness 合成；核心思想：把角色、提示、工具、通信拓扑和协调协议一起搜索，直接优化 TerminalBench-2 这类任务的 harness 设计。
- OpenCode（[开源代码](https://github.com/sst/opencode)；[官方主页](https://opencode.ai/)）：开源 terminal-native coding agent；特点是模型无关、LSP 集成、多 session 并行、隐私优先与桌面/IDE/终端多入口。
- Gemini CLI（[开源代码](https://github.com/google-gemini/gemini-cli)）：Google 的 Gemini 终端 agent；适合观察模型厂商官方 CLI 在 Terminal-Bench 2.0 上的基础 scaffold 表现。
- [Agentic Harness Engineering](https://arxiv.org/abs/2604.25850)（[开源代码](https://github.com/china-qijizhifeng/agentic-harness-engineering)）：observability-driven 的 coding-agent harness 自动演化。
  它把 harness 视为可迭代优化的代码工件，结合执行轨迹、失败观测和多轮改写改进 Terminal-Bench 2.0 类任务的 scaffold。


- cchuter（[开源代码](https://github.com/cchuter/blobfish)）：teamblobfish 的榜单 agent；公开信息有限，主要价值在于提供一个可检查的社区提交实现。
- Mini-SWE-Agent（[开源代码](https://github.com/SWE-agent/mini-swe-agent)）：Princeton/SWE-agent 系的极简软件工程 agent；适合用作低复杂度、易改造的 terminal/SWE baseline。
- spoox-m（[开源代码](https://github.com/plaume8/spoox)）：TUM/社区提交的终端 agent；公开信息有限，但代码可用于查看其 Terminal-Bench 适配方式。
- Dakou Agent（[官方主页](https://dakou.iflow.cn/)）：iflow 的 coding agent；榜单中作为中文产品型 terminal coding agent 参考。

## 1.12.5 Skill

- [mcp-code-execution](https://skills.sh/athola/claude-night-market/mcp-code-execution) 适合把终端任务组织成 `写代码 -> 执行 -> 读错误 -> 修复` 的可复用循环。
- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) 适合为终端调用提供隔离执行环境，降低本机副作用风险。
- [tmux](https://github.com/openclaw/openclaw/tree/main/skills/tmux) 适合通过 session 发现、pane 捕获、按键发送和提示监控来控制持久交互式 CLI 会话。
- [pytest](https://skills.sh/bobmatnyc/claude-mpm-skills/pytest) 适合把终端中的验证动作固化为测试运行与回归检查。
- [pytest-advanced](https://skills.sh/laurigates/claude-plugins/pytest-advanced) 适合更复杂的测试发现、参数化运行与失败定位。
- [docker-local-dev](https://skills.sh/thienanblog/awesome-ai-agent-skills/docker-local-dev) 适合把终端任务封装到可复现容器环境中，贴近 Terminal-Bench 的执行方式。
