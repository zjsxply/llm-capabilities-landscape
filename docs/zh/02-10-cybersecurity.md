# 2.10 网络安全

> 上级章节：2. 基础 Agent

说明：网络安全从 Terminal Use 中独立出来，因为这里的任务轴是漏洞发现、exploit 构造、网络行动、防御或安全策略。许多 benchmark 仍以终端作为执行载体，但不应混入通用终端任务列表。

## 2.10.1 Leaderboard

- [ExploitBench](https://exploitbench.ai/)：网络安全 agent 分层任务的项目与榜单入口；适合追踪从侦察到 exploit chain 完成的能力层级。

## 2.10.2 Bench


- [Cybench](https://arxiv.org/abs/2408.08926)：通过 CTF 风格挑战评测网络安全能力与风险。核心思想：把模型放进可执行安全任务中，要求其推理、使用工具并完成 exploit-oriented 目标，而不只是回答网络安全知识题。
- [ITBench](https://arxiv.org/abs/2502.05352)（[开源代码](https://github.com/itbench-hub/ITBench)）：评测 SRE、CISO、FinOps 等企业 IT 自动化工作流。核心思想：把安全运营、事件响应和成本/治理工作放进可执行场景，并配套可解释指标。
- [CASTLE](https://arxiv.org/abs/2503.09433)：评测静态分析器、形式化工具和 LLM 的 CWE 检测能力。核心思想：用人工构造的 CWE 程序和专门评分方式，比较不止原始真阳性数量的漏洞检测质量。
- [CVE-Bench](https://arxiv.org/abs/2503.17332)（[开源代码](https://github.com/uiuc-kang-lab/cve-bench)）：评测 AI agent 利用真实 Web 应用漏洞的能力。核心思想：用高危 CVE、隔离环境和可执行验证，把代码理解、漏洞定位、终端操作和 exploit 构造接到同一协议中。
- [Digital Forensic Timeline Analysis Evaluation](https://arxiv.org/abs/2505.03100)：评测基于 LLM 的数字取证时间线分析；核心思想是明确数据集、时间线生成与 ground truth 构造，使取证推理不再只依赖案例展示，而能进行量化比较。
- [DecompileBench](https://arxiv.org/abs/2505.11340)：评测逆向工程工作流中的反编译器。核心思想：结合真实函数抽取、运行时感知验证和面向分析员的评判，衡量语义忠实度与可用性。
- [BountyBench](https://arxiv.org/abs/2505.15216)（[项目页](https://bountybench.github.io/)）：评测真实网络安全系统中的攻击者与防御者 agent。核心思想：用 bug bounty 场景和美元影响信号衡量 Detect、Exploit、Patch 三类任务，补足只看 CTF 成功率的安全评测。
- [SecVulEval](https://arxiv.org/abs/2505.19828)：评测 LLM 在真实 C/C++ 漏洞检测中的能力。核心思想：使用更贴近真实软件的漏洞代码，而不只依赖合成片段，检验模型能否在底层软件语境中定位安全缺陷。
- [DFIR-Metric](https://arxiv.org/abs/2505.19973)：评估大语言模型在数字取证与事件响应任务中的能力。核心思想：把 DFIR 知识和调查步骤转成 benchmark 数据集，使网络安全推理不只停留在通用安全问答。
- [CyberGym](https://arxiv.org/abs/2506.02548)（[项目页](https://www.cybergym.io/)）：评测真实网络安全任务中的漏洞理解与利用闭环。核心思想：把 CVE 场景、可执行环境、工具调用和最终验证整合起来，要求 agent 做类似真实渗透或修复流程的连续决策。
- [SafeGenBench](https://arxiv.org/abs/2506.05692)：评测 LLM 生成代码中的安全漏洞检测。核心思想：关注模型和工具能否识别生成程序中的不安全点，作为 exploit 与 patch 类 benchmark 之外的生成代码安全检测补充。
- [SEC-bench](https://arxiv.org/abs/2506.11791)（[项目页](https://sec-bench.github.io/)；[开源代码](https://github.com/SEC-bench/SEC-bench)）：评测真实软件安全任务中的 PoC 生成和漏洞修复。核心思想：自动构造带 harness 的漏洞仓库和隔离复现环境，让 agent 必须读代码、运行验证、生成攻击或补丁。
- [AIRTBench](https://arxiv.org/abs/2506.14682)（[开源代码](https://github.com/dreadnode/AIRTBench-Code)）：评测自主 AI red teaming 场景中的攻击发现、代码执行和利用链闭环。核心思想：把黑盒 CTF 风格 AI/ML 安全挑战放进可运行任务，检查 agent 能否写脚本、调用工具并验证 compromise。
- [Can You Really Trust Code Copilot?](https://doi.org/10.18653/v1/2025.acl-long.849)：从代码安全角度评估 LLM 编程助手。核心思路是检查生成或辅助编写的代码是否引入安全弱点，而不只衡量功能正确性。
- [CTFTiny and CTFJudge](https://arxiv.org/abs/2508.05674)：用轻量 CTF benchmark 和基于 judge 的轨迹分析评测 offensive-security agent。核心思想：衡量阶段性进展和步骤质量，而不只看最终 flag 是否提交成功。
- [VulnRepairEval](https://arxiv.org/abs/2509.03331)：用基于漏洞利用的验证评估 LLM 漏洞修复。核心思路是让修复后的代码在可复现容器流水线中抵御功能性 PoC，而不是只依赖表层测试。
- [CyberSOCEval](https://arxiv.org/abs/2509.20166)：在 CyberSecEval 4 中评测恶意软件分析和威胁情报推理。核心思想：把防御型 SOC 评测聚焦到运营证据，而不是通用安全知识。
- [CTIArena](https://arxiv.org/abs/2510.11974)：评测 LLM 在异构网络威胁情报中的知识与推理；核心思想是检查模型能否整合指标、报告、战术和证据，而不只是回答通用安全常识。
- [CAIBench](https://arxiv.org/abs/2510.24317)：评什么：网络安全 AI agent 的元基准。核心思想：把多类网络安全 agent 评测组织到可比较的基准层中，使能力判断不局限于单一 cyber suite。
- [PATCHEVAL](https://arxiv.org/abs/2511.11019)：评测 LLM 与 agent 修补 Go、JavaScript 和 Python 真实漏洞的能力。核心思想：把大规模 CVE 语料与沙箱化安全测试和功能测试结合起来验证补丁。
- [AutoDFBench 1.0](https://arxiv.org/abs/2512.16965)：在字符串搜索、删除文件恢复、文件雕刻、Windows 注册表恢复和 SQLite 数据恢复等任务上评测数字取证工具与 AI 生成的取证代码。核心思想：基于 CFTT 测试用例、REST 执行和 precision/recall/F1 指标，使取证工具和 agent 代码评测可复现。
- [Cyb-LLM](https://doi.org/10.1109/ICVADV67766.2026.11470531)：在安全约束下评测 LLM 的网络攻防能力。核心思想：把攻击请求、防御分诊、安全编码、恶意软件等网络安全工作流统一到一个 benchmark 中。
- [ThreatSage](https://doi.org/10.1109/icassp55912.2026.11463278)：评测由 LLM 编排的蓝队防御操作。核心思想：用模块化防御任务衡量检测、分析、协同与响应工作流。
- [ALPHA](https://arxiv.org/abs/2601.01320)：评测 LLM 与 SAST 工具在 Python 函数上的层级化 CWE 预测。核心思想：区分过度泛化、过度细化和横向错误并施加不同惩罚，使漏洞反馈比二分类检测更可操作。
- [SastBench](https://arxiv.org/abs/2601.02941)：评测软件安全工作流中的 agentic SAST triage 能力。核心思想：检查 agent 能否理解静态分析结果、排序漏洞风险并给出 triage 决策，而不只是产生原始告警。
- [Sola-Visibility-ISPM](https://arxiv.org/abs/2601.07880)：评测 agentic AI 的身份安全态势可见性能力。核心思想：检查 agent 能否审阅并推理身份安全态势管理中的证据与缺口。
- [HardSecBench](https://arxiv.org/abs/2601.13864)：评测 LLM 生成硬件代码时的安全意识；核心思想是检查生成的 HDL 或硬件相关代码是否避免安全缺陷，而不只看能否编译或实现功能。
- [RealSec-bench](https://arxiv.org/abs/2601.22706)：评估真实仓库中的安全代码生成。核心思想：测试生成代码能否在满足功能需求的同时避免现实仓库语境中的安全缺陷。
- [CIPHER](https://arxiv.org/abs/2602.01438)：评估 LLM 生成 Python 加密代码中的漏洞发生率。核心思路是在不安全、中性和安全提示之间做受控对比，并用加密专属漏洞分类与行级自动评分揭示隐蔽安全缺陷。
- [Capture the Flags](https://arxiv.org/abs/2602.05523)：用语义保持变换评测 agentic LLM 在 CTF 家族任务上的表现。核心思想：检查网络安全 agent 能否跨变换后的挑战变体泛化，而不是记住单个题面的表述。
- [Vulnerability Reasoning Evaluation](https://arxiv.org/abs/2602.06687)：用因果标注和语义扰动评测漏洞推理质量。核心思想：不只看检测结论是否正确，还检查模型解释是否匹配真实根因。
- [Patch-to-PoC](https://arxiv.org/abs/2602.07287)：评测 agent 从 Linux kernel 补丁复现 N-day PoC 的能力。核心思想：把补丁分析、内核构建、调试和漏洞利用验证合在一起，检查 agent 是否能把已修复漏洞重新转化为可执行攻击证据。
- [CyberExplorer](https://arxiv.org/abs/2602.08023)：在真实攻击仿真环境中评测 LLM 的进攻安全能力。核心思想：在交互式仿真中评估攻击规划与执行，而不是只做静态网络安全问答。
- [Penetration-Testing Planning Quality](https://doi.org/10.66279/enzxq198)：以无执行方式评测 LLM 渗透测试规划质量。核心思想：在工具执行前诊断 agent 能否形成合理、有序的攻击计划。
- [Before You Hand Over the Wheel](https://arxiv.org/abs/2603.06422)：评测 LLM 的安全事件分析能力。核心思想：检查模型能否分析事件证据，并支持需要谨慎移交的人机协同 SOC 决策。
- [TOSSS](https://arxiv.org/abs/2603.10969)：基于 CVE 的大语言模型软件安全 benchmark。核心思想：用真实漏洞案例评测安全推理能力，而不局限于通用安全编码问答。
- [CTI-REALM](https://arxiv.org/abs/2603.13517)：评测 agent 生成安全检测规则的能力。核心思想：把防御型网络安全评测从通用威胁情报推理推进到可用于 SOC 工作流的 detection rule 产出。
- [OrgForge-IT](https://arxiv.org/abs/2603.22499)：用可验证的合成组织证据评测 LLM 的内部威胁检测能力。核心思想：检验 agent 能否在类企业活动轨迹中推理并识别有 ground truth 可查的内部风险信号。
- [SIR-Bench](https://arxiv.org/abs/2604.12040)：通过 794 个回放测试用例评估自主安全事件响应智能体。核心思路是用分诊准确率、新证据发现和工具使用适当性区分真正的取证调查与复述告警。
- [Cyber Defense Benchmark](https://arxiv.org/abs/2604.19533)：评测 LLM 在 SecOps 工作流中的智能体化威胁狩猎能力；核心思路是检验智能体能否调查安全证据并完成防御性威胁狩猎任务，而不只是回答网络安全知识题。
- OpenAI 网络安全风险评测（见 [GPT-5.5 system card](https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf)）：封闭或 model-card-only 评测，包含 Capture the Flag (Professional)、Cyber Range、VulnLMP、Irregular 的 atomic challenge suite 与 CyScenarioBench。核心思想：即使具体 challenge set 未公开，也要跟踪模型厂商对端到端网络行动、漏洞研究、exploit 构造和长程攻防任务的关注。
- [MOSAIC-Bench](https://arxiv.org/abs/2605.03952)：评测 coding agent 的组合式漏洞诱导。核心思想：在已部署软件基底上给出多阶段、看似良性的 ticket，并用确定性 exploit oracle 检查 agent 是否引入可利用漏洞。
- [CyBiasBench](https://arxiv.org/abs/2605.07830)：评测 cyber-attack agent 的行为偏差。核心思想：衡量 agent 在进攻场景中是否系统性过度或不足选择某些 attack family，用行为诊断补充 exploit-success benchmark。
- [CrackMeBench](https://arxiv.org/abs/2605.10597)：评测 agent 的二进制逆向工程能力。核心思想：用 CrackMe 风格任务检查 agent 在可执行逆向工作流中的代码理解、工具使用、假设检验和解题验证能力。
- [ExploitGym](https://arxiv.org/abs/2605.11086)：评测 AI agent 能否把安全漏洞转化为真实攻击。核心思想：用真实漏洞、可执行环境和利用结果验证，衡量 agent 在侦察、构造 exploit、调试失败和达成攻击目标上的端到端能力。
- [ExploitBench](https://arxiv.org/abs/2605.14153)（[项目页](https://exploitbench.ai/)；[开源代码](https://github.com/exploitbench/exploitbench)）：评测网络安全 agent 的分层能力 ladder。核心思想：从基础侦察到复杂利用链组织逐级任务，帮助区分“会用工具”和“能完成真实 exploit chain”的能力差异。
- [AuthBench](https://arxiv.org/abs/2605.14859)：评测终端/代码 agent 能否为任务推断最小充分的文件级权限边界。核心思想：把任务可用性验证和攻击结果验证合并，专测 coding agent 在读写执行权限、敏感文件暴露和最小权限授权之间的折中。

## 2.10.3 Agent Harness


- [VulnBot](https://arxiv.org/abs/2501.13411)：自主多 agent 渗透测试框架。核心思想：用渗透任务图和专门的侦察、扫描、利用 agent 协调端到端测试。
- [CRAKEN](https://arxiv.org/abs/2505.17107)：知识增强的网络安全 LLM agent harness。核心思想：把任务关键信息分解、迭代检索和知识提示注入结合起来，用于 CTF 与 MITRE 风格攻击执行。
- [Task-Driven SOC Analysis](https://doi.org/10.1049/cit2.70138)：面向 LLM 安全运营分析的任务驱动框架。核心思想：把模糊 SOC 查询转化为可验证分析步骤和证据支撑结论。
- [PentestMCP](https://arxiv.org/abs/2510.03610)：面向 agentic penetration testing 的 MCP server 工具包。核心思想：把扫描、枚举、漏洞利用和后渗透功能暴露为可组合工具，供安全 agent 工作流调用。
- [Cybersecurity AI](https://arxiv.org/abs/2512.02654)：面向安全 CTF 的智能体系统。核心思路：围绕规划、工具使用和迭代验证组织网络安全挑战求解，可作为可执行 CTF 评测中的 harness 参考。
- [Automated Penetration Testing with LLM Agents and Classical Planning](https://arxiv.org/abs/2512.11143)：结合 LLM agent 与符号规划的渗透测试 harness。核心思想：用 classical planning 组织侦察与利用步骤，再由 LLM agent 负责解释和工具交互。
- [AuditGPT](https://doi.org/10.1109/icassp55912.2026.11463116)：用于增强静态分析的多 agent 框架。核心思想：围绕代码审计证据、疑似问题和验证过程协调多个 agent，降低静态分析 triage 成本。
- [KryptoPilot](https://arxiv.org/abs/2601.09129)：面向密码学 CTF 利用的开放世界知识增强智能体。核心思路是结合深度研究、持久工作区记忆、行为治理和成本感知模型路由，使智能体能够获取细粒度密码分析知识，并将其用于长链路利用流程。
- [VulnResolver](https://arxiv.org/abs/2601.13933)：自动化漏洞 issue 解决的混合式 agent 框架。核心思想：把漏洞分析、修复规划和验证反馈合入一个基于 LLM 的 issue 解决闭环。
- [PatchIsland](https://arxiv.org/abs/2601.17471)：编排 LLM agent 进行持续漏洞修复。核心思想：把检测、修补、验证和迭代组织成面向安全缺陷的修复闭环。
- [Co-RedTeam](https://arxiv.org/abs/2602.02164)：协同式安全发现与利用 harness。核心思想：让多个 red-team agent 协作完成 discovery、exploitation、执行反馈、验证与经验复用。
- [Dual-Loop Vulnerability Reproduction](https://arxiv.org/abs/2602.05721)：用于自动化漏洞复现的双循环 agent 框架。核心思想：协调 exploit 假设生成与验证反馈，使 agent 能复现 CVE 证据，而不只是报告疑似漏洞。
- [ClearAgent](https://doi.org/10.1145/3759425.3763397)：面向漏洞检测的 agentic 二进制分析 harness。核心思想：把二进制检查、证据抽取、推理和漏洞判断组织成使用工具的分析流程。
- [VulnAgent-X](https://arxiv.org/abs/2603.13384)：面向仓库级漏洞检测的分层 agentic 框架。核心思想：结合仓库上下文、分阶段分析和验证过程，支持更真实的漏洞检测。
- [Automated Membership Inference Attacks](https://arxiv.org/abs/2603.19375)：使用 LLM agent 发现 membership inference attack 的信号计算方式。核心思想：把模型隐私测试中的探索式攻击设计循环自动化。
- [STRIATUM-CTF](https://arxiv.org/abs/2603.22577)：面向通用 CTF 解题的协议驱动 agentic 框架。核心思想：把挑战分析、工具执行、反馈和答案提交组织为可复用的 CTF 解题工作流。
- [Red-MIRROR](https://arxiv.org/abs/2603.27127)：带反思验证和知识增强交互的自主渗透测试 harness。核心思想：闭环组织攻击尝试、证据检查和由记忆支撑的策略细化。
- [ALUSKORT](https://doi.org/10.12732/ijam.v38i5s.328)：面向自主安全运营的分层多 agent 认知架构。核心思想：把确定性 guardrail 与分阶段 LLM 推理 agent 结合起来，自动化 SOC 事件调查并产出面向证据的调查材料。
- [RAVEN](https://arxiv.org/abs/2604.17948)：面向源代码与二进制程序内存破坏分析的检索增强漏洞探索网络。核心思路是把检索、程序证据和面向漏洞利用的分析循环结合起来，服务于安全智能体工作流。
- [SLYP](https://arxiv.org/abs/2605.05000)：面向 Windows COM 漏洞推理的 agentic 二进制分析 harness。核心思想：把二进制探索、COM 元数据和调试器反馈封装为工具，使 agent 能从竞态漏洞发现推进到经调试验证的 PoC 生成。
- CyberGym 的执行栈、SEC-bench 的漏洞仓库 harness、ExploitBench 的分阶段任务环境，是这里最相关的 benchmark-side harness 参考。可复用模式是 `侦察 -> 假设 -> exploit 或 patch 尝试 -> verifier-owned evidence -> 重试`，同时要求严格 sandbox 与审计日志。

## 2.10.4 Skill

- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) 适合隔离高风险网络安全或 exploit-like 工具调用。
- [docker-local-dev](https://skills.sh/thienanblog/awesome-ai-agent-skills/docker-local-dev) 适合封装漏洞服务、复现环境和可重置 validator。
