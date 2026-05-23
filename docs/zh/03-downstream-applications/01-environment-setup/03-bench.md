# 3.1.3 Bench

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
