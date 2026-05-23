# 3.1.6 Skill

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
