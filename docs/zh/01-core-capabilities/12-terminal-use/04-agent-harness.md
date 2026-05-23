# 1.12.4 Agent Harness

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
