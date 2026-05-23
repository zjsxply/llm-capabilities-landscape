# 2.10 网络安全

> 上级章节：2. 基础 Agent

说明：网络安全从 Terminal Use 中独立出来，因为这里的任务轴是漏洞发现、exploit 构造、网络行动、防御或安全策略。许多 benchmark 仍以终端作为执行载体，但不应混入通用终端任务列表。

## 2.10.1 Leaderboard

- [ExploitBench](https://exploitbench.ai/)：网络安全 agent 分层任务的项目与榜单入口；适合追踪从侦察到 exploit chain 完成的能力层级。

## 2.10.2 Bench

- [Cybench](https://arxiv.org/abs/2408.08926)：通过 CTF 风格挑战评测网络安全能力与风险。核心思想：把模型放进可执行安全任务中，要求其推理、使用工具并完成 exploit-oriented 目标，而不只是回答网络安全知识题。
- [ITBench](https://arxiv.org/abs/2502.05352)（[开源代码](https://github.com/itbench-hub/ITBench)）：评测 SRE、CISO、FinOps 等企业 IT 自动化工作流。核心思想：把安全运营、事件响应和成本/治理工作放进可执行场景，并配套可解释指标。
- [CVE-Bench](https://arxiv.org/abs/2503.17332)（[开源代码](https://github.com/uiuc-kang-lab/cve-bench)）：评测 AI agent 利用真实 Web 应用漏洞的能力。核心思想：用高危 CVE、隔离环境和可执行验证，把代码理解、漏洞定位、终端操作和 exploit 构造接到同一协议中。
- [BountyBench](https://arxiv.org/abs/2505.15216)（[项目页](https://bountybench.github.io/)）：评测真实网络安全系统中的攻击者与防御者 agent。核心思想：用 bug bounty 场景和美元影响信号衡量 Detect、Exploit、Patch 三类任务，补足只看 CTF 成功率的安全评测。
- [CyberGym](https://arxiv.org/abs/2506.02548)（[项目页](https://www.cybergym.io/)）：评测真实网络安全任务中的漏洞理解与利用闭环。核心思想：把 CVE 场景、可执行环境、工具调用和最终验证整合起来，要求 agent 做类似真实渗透或修复流程的连续决策。
- [SEC-bench](https://arxiv.org/abs/2506.11791)（[项目页](https://sec-bench.github.io/)；[开源代码](https://github.com/SEC-bench/SEC-bench)）：评测真实软件安全任务中的 PoC 生成和漏洞修复。核心思想：自动构造带 harness 的漏洞仓库和隔离复现环境，让 agent 必须读代码、运行验证、生成攻击或补丁。
- [AIRTBench](https://arxiv.org/abs/2506.14682)（[开源代码](https://github.com/dreadnode/AIRTBench-Code)）：评测自主 AI red teaming 场景中的攻击发现、代码执行和利用链闭环。核心思想：把黑盒 CTF 风格 AI/ML 安全挑战放进可运行任务，检查 agent 能否写脚本、调用工具并验证 compromise。
- [Patch-to-PoC](https://arxiv.org/abs/2602.07287)：评测 agent 从 Linux kernel 补丁复现 N-day PoC 的能力。核心思想：把补丁分析、内核构建、调试和漏洞利用验证合在一起，检查 agent 是否能把已修复漏洞重新转化为可执行攻击证据。
- [ExploitGym](https://arxiv.org/abs/2605.11086)：评测 AI agent 能否把安全漏洞转化为真实攻击。核心思想：用真实漏洞、可执行环境和利用结果验证，衡量 agent 在侦察、构造 exploit、调试失败和达成攻击目标上的端到端能力。
- [ExploitBench](https://arxiv.org/abs/2605.14153)（[项目页](https://exploitbench.ai/)；[开源代码](https://github.com/exploitbench/exploitbench)）：评测网络安全 agent 的分层能力 ladder。核心思想：从基础侦察到复杂利用链组织逐级任务，帮助区分“会用工具”和“能完成真实 exploit chain”的能力差异。
- [AuthBench](https://arxiv.org/abs/2605.14859)：评测终端/代码 agent 能否为任务推断最小充分的文件级权限边界。核心思想：把任务可用性验证和攻击结果验证合并，专测 coding agent 在读写执行权限、敏感文件暴露和最小权限授权之间的折中。
- [MOSAIC-Bench](https://arxiv.org/abs/2605.03952)：评测 coding agent 的组合式漏洞诱导。核心思想：在已部署软件基底上给出多阶段、看似良性的 ticket，并用确定性 exploit oracle 检查 agent 是否引入可利用漏洞。
- [CyBiasBench](https://arxiv.org/abs/2605.07830)：评测 cyber-attack agent 的行为偏差。核心思想：衡量 agent 在进攻场景中是否系统性过度或不足选择某些 attack family，用行为诊断补充 exploit-success benchmark。
- OpenAI 网络安全风险评测（见 [GPT-5.5 system card](https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf)）：封闭或 model-card-only 评测，包含 Capture the Flag (Professional)、Cyber Range、VulnLMP、Irregular 的 atomic challenge suite 与 CyScenarioBench。核心思想：即使具体 challenge set 未公开，也要跟踪模型厂商对端到端网络行动、漏洞研究、exploit 构造和长程攻防任务的关注。

## 2.10.3 Agent Harness

- CyberGym 的执行栈、SEC-bench 的漏洞仓库 harness、ExploitBench 的分阶段任务环境，是这里最相关的 benchmark-side harness 参考。可复用模式是 `侦察 -> 假设 -> exploit 或 patch 尝试 -> verifier-owned evidence -> 重试`，同时要求严格 sandbox 与审计日志。
- [Co-RedTeam](https://arxiv.org/abs/2602.02164)：协同式安全发现与利用 harness。核心思想：让多个 red-team agent 协作完成 discovery、exploitation、执行反馈、验证与经验复用。

## 2.10.4 Skill

- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) 适合隔离高风险网络安全或 exploit-like 工具调用。
- [docker-local-dev](https://skills.sh/thienanblog/awesome-ai-agent-skills/docker-local-dev) 适合封装漏洞服务、复现环境和可重置 validator。
