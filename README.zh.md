# LLM 能力研究图谱

一个围绕 LLM 能力、任务、benchmark 与面向 agent 的方法整理的结构化研究图谱。

本仓库按能力方向、benchmark 家族与代表性技术路线组织近期 LLM 研究，重点关注 agent harness、工作流、工具调用、记忆、skill 调用以及下游 agent 应用。

## 目录

### 0. 引言

- [0.1 内容结构](docs/zh/00-introduction/01-landscape-structure.md)
- [0.2 偏总体验的总榜](docs/zh/00-introduction/02-overall-leaderboards.md)
- [0.3 评测方法](docs/zh/00-introduction/03-evaluation-methodology.md)
- [0.4 其它](docs/zh/00-introduction/04-other.md)

### 1. 基础能力

- [1.1 多语言](docs/zh/01-core-capabilities/01-multilingual/README.md)
- [1.2 科学知识](docs/zh/01-core-capabilities/02-scientific-knowledge/README.md)
- [1.3 指令遵循](docs/zh/01-core-capabilities/03-instruction-following/README.md)
- [1.4 幻觉](docs/zh/01-core-capabilities/04-hallucination/README.md)
- [1.5 图像（含 OCR）](docs/zh/01-core-capabilities/05-image-ocr/README.md)
- [1.6 视频](docs/zh/01-core-capabilities/06-video/README.md)
- [1.7 空间](docs/zh/01-core-capabilities/07-spatial/README.md)
- [1.8 数学（含多模态数学）](docs/zh/01-core-capabilities/08-math/README.md)
- [1.9 通用推理（含视觉谜题）](docs/zh/01-core-capabilities/09-general-reasoning/README.md)
- [1.10 长上下文](docs/zh/01-core-capabilities/10-long-context/README.md)
- [1.11 工具调用](docs/zh/01-core-capabilities/11-tool-use/README.md)
- [1.12 终端调用](docs/zh/01-core-capabilities/12-terminal-use/README.md)
- [1.13 Skill 调用](docs/zh/01-core-capabilities/13-skill-use/README.md)
- [1.14 写作与长文生成](docs/zh/01-core-capabilities/14-writing/README.md)
- [1.15 记忆](docs/zh/01-core-capabilities/15-memory/README.md)
- [1.16 其它](docs/zh/01-core-capabilities/16-other/README.md)

### 2. 基础 Agent

- [2.1 竞赛编程](docs/zh/02-agent-capabilities/01-competitive-programming/README.md)
- [2.2 软件开发](docs/zh/02-agent-capabilities/02-software-development/README.md)
- [2.3 互联网搜索](docs/zh/02-agent-capabilities/03-web-search/README.md)
- [2.4 深度研究](docs/zh/02-agent-capabilities/04-deep-research/README.md)
- [2.5 计算机操作（GUI）](docs/zh/02-agent-capabilities/05-computer-use-gui/README.md)
- [2.6 长时运行](docs/zh/02-agent-capabilities/06-long-running/README.md)
- [2.7 现实工作](docs/zh/02-agent-capabilities/07-real-world-work/README.md)
- [2.8 未来预测](docs/zh/02-agent-capabilities/08-future-prediction/README.md)
- [2.9 Agent 安全](docs/zh/02-agent-capabilities/09-agent-safety/README.md)
- [2.10 网络安全](docs/zh/02-agent-capabilities/10-cybersecurity/README.md)
- [2.11 具身与 VLA Agent](docs/zh/02-agent-capabilities/11-embodied-vla/README.md)

### 3. 下游应用

- [3.1 配环境](docs/zh/03-downstream-applications/01-environment-setup/README.md)
- [3.2 科研](docs/zh/03-downstream-applications/02-research/README.md)

### 4. 多模态

- [4.1 图片生成与编辑模型](docs/zh/04-multimodal/01-image-generation-editing/README.md)
- [4.2 视频生成模型](docs/zh/04-multimodal/02-video-generation/README.md)
- [4.3 语音模型](docs/zh/04-multimodal/03-speech/README.md)
- [4.4 自动驾驶](docs/zh/04-multimodal/04-autonomous-driving/README.md)

## 维护方式

本项目采用半自动化方式维护。最新关注热点与研究成果会从引文网络、模型厂商 model card，以及顶会最新接收论文中提取，再经 agent 辅助筛选后合并进图谱。具体流程见本仓库维护 skill：[.agents/skills/llm-landscape-maintainer/SKILL.md](.agents/skills/llm-landscape-maintainer/SKILL.md)。

编号研究图谱内容按 `docs/<language>/<chapter>/<topic>/README.md` 加 `03-bench.md`、`04-model.md`、`05-agent-harness.md` 等小节文件组织；引言章直接使用 `docs/<language>/00-introduction/` 下的二级 Markdown 文件。

## English Version

英文版与中文原文并列维护，见 [README.md](README.md)。
