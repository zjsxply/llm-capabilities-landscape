# LLM Capabilities Research Landscape

A structured landscape of LLM capabilities, tasks, benchmarks, and agent-oriented methods.

This repository organizes recent LLM research by capability areas, benchmark families, and representative technical approaches, with a particular focus on agent harnesses, workflows, tool use, memory, skill use, and downstream agent applications.

## Contents

### 0. Introduction

- [0.1 Landscape Structure](docs/en/00-introduction/01-landscape-structure.md)
- [0.2 Overall Experience-Oriented Leaderboards](docs/en/00-introduction/02-overall-leaderboards.md)
- [0.3 Evaluation Methodology](docs/en/00-introduction/03-evaluation-methodology.md)
- [0.4 Other](docs/en/00-introduction/04-other.md)

### 1. Core Capabilities

- [1.1 Multilingual](docs/en/01-core-capabilities/01-multilingual/README.md)
- [1.2 Scientific Knowledge](docs/en/01-core-capabilities/02-scientific-knowledge/README.md)
- [1.3 Instruction Following](docs/en/01-core-capabilities/03-instruction-following/README.md)
- [1.4 Hallucination](docs/en/01-core-capabilities/04-hallucination/README.md)
- [1.5 Images, Including OCR](docs/en/01-core-capabilities/05-image-ocr/README.md)
- [1.6 Video](docs/en/01-core-capabilities/06-video/README.md)
- [1.7 Spatial Reasoning](docs/en/01-core-capabilities/07-spatial/README.md)
- [1.8 Mathematics, Including Multimodal Math](docs/en/01-core-capabilities/08-math/README.md)
- [1.9 General Reasoning, Including Visual Puzzles](docs/en/01-core-capabilities/09-general-reasoning/README.md)
- [1.10 Long Context](docs/en/01-core-capabilities/10-long-context/README.md)
- [1.11 Tool Use](docs/en/01-core-capabilities/11-tool-use/README.md)
- [1.12 Terminal Use](docs/en/01-core-capabilities/12-terminal-use/README.md)
- [1.13 Skill Use](docs/en/01-core-capabilities/13-skill-use/README.md)
- [1.14 Writing and Long-Form Generation](docs/en/01-core-capabilities/14-writing/README.md)
- [1.15 Memory](docs/en/01-core-capabilities/15-memory/README.md)
- [1.16 Agent Swarm](docs/en/01-core-capabilities/16-agent-swarm/README.md)
- [1.17 Creativity](docs/en/01-core-capabilities/17-creativity/README.md)
- [1.18 Other](docs/en/01-core-capabilities/18-other/README.md)

### 2. Agent Capabilities

- [2.1 Competitive Programming](docs/en/02-agent-capabilities/01-competitive-programming/README.md)
- [2.2 Software Development](docs/en/02-agent-capabilities/02-software-development/README.md)
- [2.3 Web Search](docs/en/02-agent-capabilities/03-web-search/README.md)
- [2.4 Deep Research](docs/en/02-agent-capabilities/04-deep-research/README.md)
- [2.5 Computer Use, GUI](docs/en/02-agent-capabilities/05-computer-use-gui/README.md)
- [2.6 Long-Running Agents](docs/en/02-agent-capabilities/06-long-running/README.md)
- [2.7 Real-World Work](docs/en/02-agent-capabilities/07-real-world-work/README.md)
- [2.8 Future Prediction](docs/en/02-agent-capabilities/08-future-prediction/README.md)
- [2.9 Agent Safety](docs/en/02-agent-capabilities/09-agent-safety/README.md)
- [2.10 Cybersecurity](docs/en/02-agent-capabilities/10-cybersecurity/README.md)
- [2.11 Embodied and VLA Agents](docs/en/02-agent-capabilities/11-embodied-vla/README.md)

### 3. Downstream Applications

- [3.1 Environment Setup](docs/en/03-downstream-applications/01-environment-setup/README.md)
- [3.2 Research](docs/en/03-downstream-applications/02-research/README.md)

### 4. Multimodal

- [4.1 Image Generation and Editing Models](docs/en/04-multimodal/01-image-generation-editing/README.md)
- [4.2 Video Generation Models](docs/en/04-multimodal/02-video-generation/README.md)
- [4.3 Speech and Audio Models](docs/en/04-multimodal/03-speech/README.md)
- [4.4 Autonomous Driving](docs/en/04-multimodal/04-autonomous-driving/README.md)

## Maintenance

This project is maintained semi-automatically. Recent topics and research results are extracted from citation networks, model-vendor model cards, and newly accepted papers from major conferences, then screened and merged by an agent-guided workflow. See the repository maintenance skill at [.agents/skills/llm-landscape-maintainer/SKILL.md](.agents/skills/llm-landscape-maintainer/SKILL.md).

Numbered landscape content is organized as `docs/<language>/<chapter>/<topic>/README.md` plus numbered section files such as `03-bench.md`, `04-model.md`, and `05-agent-harness.md`. The introduction chapter uses second-level Markdown files directly under `docs/<language>/00-introduction/`.

## Chinese Version

The original Chinese version is kept alongside the English translation. See [README.zh.md](README.zh.md).
