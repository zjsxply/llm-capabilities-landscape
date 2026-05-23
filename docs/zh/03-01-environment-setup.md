# 3.1 配环境

> 上级章节：3. 下游应用

## 3.1.1 Leaderboard

说明：截至 2026-05-22，环境搭建方向还没有看到像 BFCL、Terminal-Bench 2.0 或 SkillsBench 那样成熟、持续更新、集中接收提交的公开榜单。

## 3.1.2 Survey

- [If LLM Is the Wizard, Then Code Is the Wand: A Survey on How Code Empowers Large Language Models to Serve as Intelligent Agents](https://arxiv.org/abs/2401.00812)：关于可执行工作流中代码执行与程序化反馈的基础总览。
- [AI Agentic Programming: A Survey of Techniques, Challenges, and Opportunities](https://arxiv.org/abs/2508.11126)：通过执行、测试与调试闭环为仓库搭建和构建修复 agent 提供背景。
- [Agentic Software Engineering: Foundational Pillars and a Research Roadmap](https://arxiv.org/abs/2509.06216)：回顾任务分解、工具、验证、反馈闭环与工程工作流。
- [Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures](https://arxiv.org/abs/2604.03515)：解释 scaffold 中的 shell 执行、环境状态、修复循环与仓库级控制。

## 3.1.3 Bench

- [SUPER](https://arxiv.org/abs/2409.07440)：评什么：从真实 ML/NLP 研究仓库中完成 setup 与任务执行。核心思想：把研究复现拆成 Expert、Masked 与 AutoGen 三组任务，并同时记录成功率与过程进展，暴露 agent 在依赖安装、脚本入口定位和实验运行中的实际失败点。（[开源代码](https://github.com/allenai/super-benchmark)，[数据集](https://huggingface.co/datasets/allenai/super)）
- [Repo2Run](https://arxiv.org/abs/2502.13681)（公开 benchmark + agent）：评什么：给定代码仓库，自动构建可执行 Docker 环境并跑通 unit tests。核心思想：把环境构建建模成 `build image -> run tests -> 读反馈 -> 修 Dockerfile` 的闭环合成问题，并公开包含 420 个 Python 仓库的评测集（论文称）。
- [RepoST](https://arxiv.org/abs/2503.07358)：评什么：repo-level code generation 的可执行 sandbox testing 环境构造。核心思想：隔离目标函数及本地依赖生成独立测试脚本，降低整仓库依赖配置成本，并发布 RepoST-Train / RepoST-Eval 支撑带执行反馈的训练与评测。（[项目页](https://repost-code-gen.github.io/)，[开源代码](https://github.com/yiqingxyq/RepoST)）
- [EnvBench](https://arxiv.org/abs/2503.14443)（公开 benchmark；[开源代码](https://github.com/JetBrains-Research/EnvBench)，[数据与 trajectories](https://jb.gg/envbench)）：评什么：仓库级环境配置（Python 与 JVM：Java/Kotlin），强调真实配置难点而非“脚本一键可装”。核心思想：通过静态分析（Python missing imports）与编译检查（JVM）等自动指标，形成可扩展的 setup-eval 体系，并发布可复现实验轨迹（以论文/官方资源为准）。
- [PIPer-eval](https://huggingface.co/datasets/PIPer-iclr/PIPer-eval)：评什么：Python 环境安装规划与修复能力。核心思想：把依赖安装、冲突诊断和执行反馈组织成公开评测结果数据集，适合作为 EnvBench/Repo2Run 之外的 setup planning 参考。
- [CompileAgentBench](https://arxiv.org/abs/2505.04254)（公开 benchmark + agent；[开源代码](https://github.com/Ch3nYe/AutoCompiler)）：评什么：真实仓库/项目的编译错误定位与修复。核心思想：把依赖安装、构建命令、编译日志解析和补丁回写串成可执行闭环，直接衡量 agent 让项目从不可编译到可编译的能力。
- [SetupBench](https://arxiv.org/abs/2507.09063)（公开 benchmark）：评什么：从 bare Linux sandbox 引导开发环境（多语言生态、数据库、多服务编排）。核心思想：用“确定性的成功命令”作为验收，隔离出 environment-bootstrap 这一关键子能力，并分析 agent 在探索效率与持久化修改上的系统性失败模式。
- [BuildBench](https://arxiv.org/abs/2509.25248)：评什么：真实开源软件的编译与构建成功率。核心思想：把 agent 放到复杂构建系统、依赖链和系统包约束下，检验其能否读日志、修配置并最终完成可验证构建。（注：截至撰写时暂未见稳定的官方独立开源仓库/数据入口。）
- [EnConda-bench](https://arxiv.org/abs/2510.25694)：评什么：环境配置过程中的规划、错误诊断、反馈修复与最终执行能力。核心思想：通过注入 realistic README errors 构造 Docker 验证任务，既看端到端可执行性，也看轨迹级内部能力。（[开源代码](https://github.com/TencentYoutuResearch/EnConda-Bench)）
- [Multi-Docker-Eval](https://arxiv.org/abs/2512.06915)：评什么：Docker 环境构建/修复 agent 的可执行性与“从失败到成功”的修复能力。核心思想：用 Fail-to-Pass、Commit Rate 等指标衡量从构建失败到可运行环境的端到端修复质量。（注：截至撰写时暂未见稳定的官方独立开源仓库/数据入口。）
- [DevOps-Gym](https://arxiv.org/abs/2601.12961)：评什么：DevOps 场景中的构建配置、部署、测试和运维任务。核心思想：用可执行的 CI/CD 与仓库运维任务检验 agent 是否具备跨工具链、跨服务的工程操作能力。（[项目页](https://www.devops-gym.com/)，[开源代码](https://github.com/ucsb-mlsec/DevOps-Gym)）
- [MEnvBench](https://arxiv.org/abs/2601.22859)（公开 benchmark）：评什么：多语言（polyglot）仓库的环境构建与可验证执行。核心思想：将环境构建拆成 Planning-Execution-Verification 闭环，并用环境复用机制降低构建开销；论文报告覆盖 1000 题、10 种语言、200 个仓库（以论文为准）。
- [ResearchEnvBench](https://arxiv.org/abs/2603.06739)：评什么：研究代码执行的环境合成。核心思想：给定研究仓库、文档和目标执行设定，要求 agent 把环境真正搭起来并跑通运行时。

## 3.1.4 Agent Harness

- [Installamatic](https://arxiv.org/abs/2412.06294)（[开源代码](https://github.com/coinse/installamatic)）是最典型的安装步骤合成与失败恢复 agent。
- [ExecutionAgent](https://arxiv.org/abs/2412.10133)（[开源代码](https://github.com/sola-st/ExecutionAgent)）代表“基于执行反馈修复环境命令”。
- [Repo2Run](https://arxiv.org/abs/2502.13681)（[开源代码](https://github.com/bytedance/Repo2Run)）把环境构建明确成 Dockerfile 合成与测试闭环。
- [SetUpAgent](https://arxiv.org/abs/2503.07701)（开源代码：未公开）聚焦自反式 Dockerfile 合成与环境修补，是把“试错建环境”显式 agent 化的代表工作。
- [SWE-smith](https://arxiv.org/abs/2504.21798)（[开源代码](https://github.com/SWE-bench/SWE-smith)）将可执行环境构建、任务合成与验证流水线打通，更偏“配环境能力驱动的数据工厂”。
- [CompileAgent](https://arxiv.org/abs/2505.04254)（[开源代码](https://github.com/Ch3nYe/AutoCompiler)）面向编译失败修复，强调从编译日志中定位缺失依赖、API 不兼容和构建脚本问题。
- [SWE-Builder（SWE-Factory）](https://arxiv.org/abs/2506.10954)（[开源代码](https://github.com/DeepSoftwareAnalytics/swe-factory)）把环境构建模块化为可复用组件，用于大规模生成可执行 SWE 训练与评测实例。
- [OSS-BUILD-AGENT](https://arxiv.org/abs/2509.25248)（开源代码：未找到稳定公开仓库）聚焦真实开源软件构建失败恢复，核心是基于构建日志反复修改依赖、配置与脚本直到编译通过。
- [GradleFixer（Automating Android Build Repair）](https://arxiv.org/abs/2510.08640)（开源代码：未公开）属于边界相关：聚焦 Android/Gradle 构建失败修复，任务核心强依赖构建与依赖环境操作；其思路对“配环境 + 构建修复”类任务有参考，但不是通用 Repo2Run/EnvBench 风格 benchmark。
- [SWE-Bench++](https://arxiv.org/abs/2512.17419)（[开源代码](https://github.com/TuringEnterprises/SWE-Bench-plus-plus)）在自动生成 SWE benchmark 的流程中显式引入 environment synthesis，并与 setup agent 做对比。
- [MEnvAgent](https://arxiv.org/abs/2601.22859)（[开源代码](https://github.com/ernie-research/MEnvAgent)）把“多语言环境构建”做成多 agent 的 Planning-Execution-Verification 闭环，并引入环境复用机制。
- [DockSmith](https://arxiv.org/abs/2602.00592)（开源代码：未公开）将 Docker 环境构建作为核心 agentic 能力来训练/评测，并以 Multi-Docker-Eval 为主评测基准。
- [SWE-Universe](https://arxiv.org/abs/2602.02361)（开源代码：未公开）主张大规模自动构造可验证的 SWE 环境与任务数据，环境能力评测基于作者自建多语言任务集。
- [HerAgent](https://arxiv.org/abs/2602.07871)（[开源代码](https://github.com/EuniAI/HerAgent)）聚焦自动环境部署，并在多个 setup 相关子基准上做统一评测对比（见论文）。
- [AgentCgroup](https://arxiv.org/abs/2602.09345)：面向沙盒化 AI agent 的资源控制框架。核心思想：刻画 coding agent 在 OS 层面的 CPU、内存和工具调用资源峰值，并用 cgroup 式策略控制多租户执行。
- [ScaleSWE](https://arxiv.org/abs/2602.09892)（[开源代码](https://github.com/AweAI-Team/ScaleSWE)）通过 setup agent、test creation agent 与 problem synthesis agent 的多代理流水线构造大规模 verified SWE 实例。
- [SWE-rebench V2](https://arxiv.org/abs/2602.23866)（[开源代码](https://github.com/SWE-rebench/SWE-rebench-V2)）公开了 interactive setup synthesis 代理及其镜像构建流程，用于复杂仓库 setup 自动化。
- [SWE-Hub](https://arxiv.org/abs/2603.00575)（[开源代码](https://github.com/zhenglw02/SWE-Hub)）将 Env Agent 作为数据工厂执行底座介绍，强调环境搭建在大规模 SWE 流水线中的基础设施角色。
- [RepoLaunch](https://arxiv.org/abs/2603.05026)（[开源代码](https://github.com/microsoft/RepoLaunch)）把跨语言仓库的 build-test 打通抽象成通用流水线。
- [daVinci-Env（OpenSWE）](https://arxiv.org/abs/2603.13023)（[开源代码](https://github.com/GAIR-NLP/OpenSWE)）用多代理流水线大规模合成可执行 Docker 环境与评测脚本，更偏“可复现基础设施 + 环境合成”。
- [BootstrapAgent](https://arxiv.org/abs/2605.15815)（[开源代码](https://github.com/Vossera/BootstrapAgent)）把仓库启动经验蒸馏成可复用的 `.bootstrap` contract；核心流程包括证据抽取、结构化规划、Docker 验证、trace-driven repair 与 clean replay，目标是让后续 coding agent 少重复试错。

## 3.1.5 Skill

- [docker-configuration-validator](https://skills.sh/rknall/claude-skills/docker-configuration-validator) 适合先检查 Dockerfile / compose 配置。
- [docker-containerization](https://skills.sh/ailabs-393/ai-labs-claude-skills/docker-containerization) 适合快速容器化。
- [devcontainer-helper](https://skills.sh/gabeosx/agent-skills/devcontainer-helper) 适合本地开发环境标准化。
- [package-managing](https://skills.sh/ingpdw/pdw-python-dev-tool/package-managing) 适合依赖安装与版本治理。
- [error-recovery](https://skills.sh/zpankz/mcp-skillset/error-recovery) 适合在环境拉起失败后做 repair loop。
- [multi-stage-dockerfile](https://skills.sh/github/awesome-copilot/multi-stage-dockerfile) 适合生成可复现、可裁剪的 multi-stage Dockerfile，缓解“镜像过大/依赖不稳定/构建慢”。
- [devcontainer-setup](https://skills.sh/shipshitdev/library/devcontainer-setup) 适合把仓库环境固化为可复用 devcontainer 配置（偏 monorepo 挂载与端口映射）。
- [devcontainer-setup](https://skills.sh/trailofbits/skills/devcontainer-setup) 适合把多语言工具链与 Claude Code 一并打包到 devcontainer（偏安全/工程化）。
- [python-dependency-resolver](https://skills.sh/jorgealves/agent_skills/python-dependency-resolver) 适合定位 pip 版本冲突、循环依赖与约束不一致。
- [python-uv](https://skills.sh/mindrally/skills/python-uv) 适合 uv-first Python 项目搭建、lockfile 修复和依赖工作流标准化，补足通用 pip repair 与完整 Docker/devcontainer setup 之间的空档。
- [python-packaging](https://skills.sh/wshobson/agents/python-packaging) 适合修复 `pyproject`、build backend、wheel、包元数据和依赖布局问题。
- [docker-compose-orchestration](https://skills.sh/manutej/luxor-claude-marketplace/docker-compose-orchestration) 适合多服务 compose 环境，尤其是 setup benchmark 中数据库、worker 和应用服务必须一起启动的场景。
- [ARIS experiment-support skills](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/main/skills) 里的 `experiment-queue`、`run-experiment`、`vast-gpu`、`serverless-modal` 和 `system-profile` 等技能覆盖排队实验执行、远程 GPU/云端执行和系统画像，适合 research-code setup 循环。
- [flonat python-env](https://github.com/flonat/claude-research/tree/main/skills/python-env) 适合学术 Python 项目环境、虚拟环境检查、依赖 sanity check 和实验前运行卫生。
- [install-script-generator](https://skills.sh/luongnv89/skills/install-script-generator) 适合生成可一键执行的跨平台安装脚本。
- [repo-runner](https://clawhub.ai/zyl-hub/repo-runner) 适合按仓库文档拉起项目并带风险护栏（更偏 runbook/执行助手）。
