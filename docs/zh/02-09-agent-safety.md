# 2.9 Agent 安全

> 上级章节：2. 基础 Agent


## 2.9.1 Leaderboard

- [CAIS AI Dashboard](https://dashboard.safe.ai/)：包含 Risk Index、capability index 与 automation 视图，是当前最适合跨模型观察能力-风险共同演化的公开安全总览。
- [SafePro](https://safeprobench.github.io/safepro/)：专业级 agent 安全项目页，提供 benchmark 说明和 unsafe-rate 等结果线索；适合追踪现实专业工作中“能完成但不安全”的失败模式。

说明：Agent 安全方向还没有像 SWE-bench 或 Terminal-Bench 那样成熟统一的持续提交榜，当前更常见的是项目页、dashboard 和论文内结果表。

## 2.9.2 Bench

- [BBQ](https://arxiv.org/abs/2110.08193)：评测问答中的偏见，覆盖 ambiguous 与 disambiguated 两类上下文。核心思想：诊断模型是否依赖社会刻板印象，或能在上下文不足时拒绝/在上下文充分时正确使用证据；即使本页主要关注 agent，它仍是 model card 常用的基础安全信号。
- [Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691)：评测 LLM 控制机器人的越狱风险。核心思想：用 RoboPAIR 和 harmful-action 数据集测试攻击能否在自动驾驶、地面机器人和四足机器人场景中诱发不安全物理动作。
- [MASK Benchmark](https://arxiv.org/abs/2503.03750)：评测模型在压力下是否会违背自己声明过的知识或信念。核心思想：把 honesty 与 accuracy 分开，检查用户或系统压力诱导冲突答案时，模型是否仍保持已声明知识。
- [SafeArena](https://arxiv.org/abs/2503.04957)（[项目页](https://safearena.github.io/)）：评什么：自主 web agent 面对安全/有害网页任务时的行为。核心思想：用安全与有害任务配对，观察 agent 是否会顺从虚假信息、违法活动、骚扰、网络犯罪和偏见等风险请求。
- [SafePlan-Bench](https://arxiv.org/abs/2504.14650)：评测 LLM-based embodied agent 的任务规划安全。核心思想：在多类日常具身任务和危险类别中测试 agent 是否能生成安全计划，特别覆盖没有显式恶意指令的场景。
- [OrgAccess](https://arxiv.org/abs/2505.19165)：评测组织规模 LLM assistant 的基于角色访问控制能力。核心思想：测试模型在层级权限和冲突访问规则下，是否能遵守信息流与行动边界。
- [SAFEL / EMBODYGUARD](https://arxiv.org/abs/2505.19933)：评测 LLM-based embodied decision making 的物理安全性。核心思想：把命令拒绝与计划安全测试结合 PDDL-grounded 场景，诊断目标理解、状态转移建模和动作排序中的安全失败。
- [RedTeamCUA / RTC-Bench](https://arxiv.org/abs/2505.21936)（[项目页](https://osu-nlp-group.github.io/RedTeamCUA)）：评什么：混合 Web-OS 环境中的 computer-use agent 红队测试。核心思想：用 864 个间接提示注入样例和真实 GUI/网页动作空间，暴露 CUA 在跨应用执行时的攻击面。
- Agent Red Teaming（ART）tool-use benchmark（见 [Claude Opus 4.7 system card](https://cdn.sanity.io/files/4zrzovbb/website/037f06850df7fbe871e206dad004c3db5fd50340.pdf)）：Anthropic 使用的外部间接提示注入评测；目前未确认有独立公开版本。核心思想：测试工具型 agent 是否会执行出现在工具输出或环境内容中的攻击者注入指令。
- Shade 间接提示注入评测（见 [Claude Opus 4.7 system card](https://cdn.sanity.io/files/4zrzovbb/website/037f06850df7fbe871e206dad004c3db5fd50340.pdf)）：Gray Swan 面向 coding 与 computer-use 场景的外部自适应红队评测；具体 challenge set 未公开。核心思想：用自适应 prompt-injection attacker 评估鲁棒性，而不是只看固定静态 jailbreak 提示。
- [VPI-Bench](https://arxiv.org/abs/2506.02456)（数据集：[VPI-Bench/vpi-bench](https://huggingface.co/datasets/VPI-Bench/vpi-bench)）：评什么：computer-use / browser-use agent 的视觉提示注入鲁棒性。核心思想：把恶意指令嵌入网页截图和视觉内容中，测试 agent 是否会把屏幕上的攻击文本当作用户意图执行。
- [AGENTSAFE](https://arxiv.org/abs/2506.14697)：评测 embodied VLM agent 在危险指令下的安全性。核心思想：用 SAFE-THOR、SAFE-VERSE 和 SAFE-DIAGNOSE 分析对人、环境和 agent 自身有风险的感知、规划与执行失败。
- [OS-Harm](https://arxiv.org/abs/2506.14866)（[开源代码](https://github.com/tml-epfl/os-harm)）：评什么：computer-use agent 在操作系统任务中的安全性。核心思想：基于 OSWorld 构造恶意用户请求、提示注入和模型误行为三类风险，检查 agent 是否会在邮件、浏览器、代码编辑器等应用中执行危险动作。
- [BehaviorBench](https://arxiv.org/abs/2506.20606)：评测 LLM agent 的伦理行为与 harmful steering 风险。核心思想：用多层级道德心理学场景衡量 agent 在任务完成与伦理行动分离时，是趋向助益还是被引向伤害。
- [OpenAgentSafety](https://arxiv.org/abs/2507.06134)：评什么：真实多工具、多用户 agent 的综合安全。核心思想：接入浏览器、代码执行、文件系统、shell 和消息平台，覆盖多轮多用户任务中的 8 类风险。
- [SafeMind](https://arxiv.org/abs/2509.25885)：评测并缓解具身 LLM 智能体的安全风险。核心思路是诊断具身决策中的不安全行为，并配套缓解机制，使物理环境中的规划安全问题更可测量。
- [Physical-World Privacy Awareness Benchmark](https://arxiv.org/abs/2510.02356)：评测语言模型在物理世界情境中的隐私风险意识。核心思想：显式呈现涉及隐私的观察与动作，使具身或助理 agent 的安全评测超出纯文本政策问答。
- [DeceptionBench](https://arxiv.org/abs/2510.15501)（[开源代码](https://github.com/Aries-iai/DeceptionBench)，[数据集](https://huggingface.co/datasets/skyai798/DeceptionBench)）：评什么：真实场景中的 AI 欺骗行为。核心思想：按社会领域和干预设置组织欺骗倾向，把欺骗行为从零散 alignment 担忧变成可测量的安全失败模式。
- [VestaBench](https://doi.org/10.18653/v1/2025.emnlp-industry.149)：评估多约束与对抗设置下的安全长程具身规划。核心思路是检查智能体在完成长任务时能否同时维持安全性，并处理相互冲突或被攻击的约束。
- [OASIS](https://arxiv.org/abs/2511.08487)：评什么：意图隐藏与任务复杂度下的 agent safety 脆弱性。核心思想：把用户危险意图藏在复杂任务结构中，检查 agent 是否只看表层任务合理性而忽略潜在风险。
- [EvilGenie](https://arxiv.org/abs/2511.21654)：评测 agent 的 reward hacking 行为。核心思想：构造可通过利用目标函数或环境漏洞获得表面成功的任务，把规格作弊变成可测量的安全失败。
- [ResponsibleRobotBench](https://arxiv.org/abs/2512.04308)：评测多模态大语言模型驱动的负责任机器人操作。核心思想：在操作任务中同时衡量任务完成、安全性、规范遵守和负责任动作选择。
- [SafePro](https://arxiv.org/abs/2601.06663)（[项目页](https://safeprobench.github.io/safepro/)）：评什么：专业级 AI agent 的安全性。核心思想：在专业服务和现实工作任务中同时看任务完成与不安全动作，避免只以产出质量判断 agent 可部署性。
- [LPS-Bench](https://arxiv.org/abs/2602.03255)：评测 computer-use agent 的规划期安全意识。核心思想：在 benign 与 adversarial 长程场景中测试 MCP-based CUA 是否能在执行 GUI 或工具动作前预判风险。
- [MT-AgentRisk](https://arxiv.org/abs/2602.13379)：评测工具型 agent 的多轮安全风险。核心思想：把单轮有害请求转成真实多轮工具轨迹，观察 agent 是否会随着上下文累积而变得更不安全。
- [SPOC](https://arxiv.org/abs/2602.21595)：评测部分可观测和物理约束下的具身安全规划。核心思想：用状态和约束指标评估逐步家庭任务计划，覆盖火、液体、伤害、物体损坏和污染等危险。
- [CoT-Control](https://arxiv.org/abs/2603.05706)：评测推理模型在不同提示压力下能否控制或塑造自己的 chain-of-thought 行为。核心思想：诊断推理轨迹的可控性与可监控性风险，这是前沿 model card 已开始与答案准确率分开报告的安全维度。
- [HomeSafe-Bench](https://arxiv.org/abs/2603.11975)：评测 VLM 对家庭具身 agent 不安全动作的检测能力。核心思想：用仿真和生成的家庭场景及细粒度安全标注，检查模型能否在动作执行前识别动态风险。
- [Indirect Prompt Injection Competition](https://arxiv.org/abs/2603.15714)：通过大规模公开比赛评测 agent 对间接提示注入的脆弱性。核心思想：让处理不可信外部内容的 agent 面对真实发现的攻击模式，而不是只测固定 jailbreak 模板。
- [BeSafe-Bench](https://arxiv.org/abs/2603.25747)：评测 situated agent 在功能性环境中的行为安全风险。核心思想：覆盖 Web、Mobile、Embodied VLM 和 Embodied VLA 任务，观察不安全行为如何在环境交互中产生。
- [ATBench](https://arxiv.org/abs/2604.02022)（数据集：[AI45Research/ATBench](https://huggingface.co/datasets/AI45Research/ATBench)）：评什么：长程 agent 轨迹的安全诊断。核心思想：按风险来源、失败模式和现实危害组织轨迹级样本，分析风险是在计划、工具调用、环境观察还是恢复阶段出现。
- [ClawsBench](https://arxiv.org/abs/2604.05172)：评测模拟工作空间中 productivity agent 的能力与安全。核心思想：用高保真 Gmail、Slack、Calendar、Docs 和 Drive 复刻服务衡量任务成功与 unsafe action rate，避免直接操作真实服务。
- [OS-Blind](https://arxiv.org/abs/2604.10577)（[项目页](https://limenlp.github.io/OS_Blind/)）：评什么：用户指令本身无害但执行上下文可能有害的 CUA 风险。核心思想：把安全判断从“读用户请求”推进到“读环境状态和执行后果”，专门暴露 computer-use agent 的盲点。
- [DESPITE](https://arxiv.org/abs/2604.18463)（[数据集](https://huggingface.co/datasets/Lennittus/DESPITE)）：评测 LLM 具身规划中的安全风险；核心思想是用 12,279 个物理危险和规范性危险任务及确定性验证，说明规划成功率可能与行动计划安全性明显脱钩。
- [SafetyALFRED](https://arxiv.org/abs/2604.19638)：评估多模态大模型的安全意识规划能力。核心思路是把 ALFRED 式具身家居任务改造成带安全约束的规划评测，检查模型生成计划时是否考虑危险动作和限制。
- [OS-SPEAR](https://arxiv.org/abs/2604.24348)：评测 OS agent 的安全、性能、效率与鲁棒性。核心思想：把 OS-agent 失败分析为轨迹级可信问题，而不是只看最终任务成功。
- [Reward Hacking Benchmark](https://arxiv.org/abs/2605.02964)：衡量工具使用型 LLM agent 的 reward hacking 利用行为。核心思想：检查 agent 是否利用评测器、工具或任务漏洞，而不是完成真实目标。
- [SkillSafetyBench](https://arxiv.org/abs/2605.12015)：评什么：skill-facing attack surface 下的 agent 安全。核心思想：把第三方 skill、本地 artifact 和任务材料作为攻击面，检查 agent 是否会在调用技能时越权或执行危险流程。
- Minimal-LinuxBench（见 [Claude Opus 4.7 system card](https://cdn.sanity.io/files/4zrzovbb/website/037f06850df7fbe871e206dad004c3db5fd50340.pdf)）：Anthropic 基于 Redwood Research 私下共享 LinuxBench AI-control arena 做的开发中改编版本；未公开发布。核心思想：在高风险软件环境和监控条件下测试 agent 是否能隐蔽完成 side task。
- OpenAI 内部生产与部署安全评测（见 [GPT-5.5 system card](https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf)）：封闭评测，覆盖 production benchmark suites、standard evals、image-input safety、destructive-action avoidance、connectors 中的 prompt-injection attacks，以及动态 mental-health adversarial simulations。它们未公开，但应记录，因为这些类别反映了模型厂商当前关注的部署风险。
## 2.9.3 Agent Harness


- [ST-WebAgentBench](https://arxiv.org/abs/2410.06703)（[开源代码](https://github.com/segev-shlomov/ST-WebAgentBench)）：安全可信 web agent 评测 harness；价值在于把网页环境、任务状态和安全约束组织成可复现的 browser-agent 测试协议。
- [Safety Guardrails for LLM-Enabled Robots](https://arxiv.org/abs/2503.07885)：提出面向 LLM-enabled robots 的外部安全护栏 RoboGuard。核心思想：把安全规则 grounding 到机器人环境中，并用 temporal-logic control synthesis 处理不安全计划，同时尽量保持安全任务执行。
- [RedTeamCUA](https://arxiv.org/abs/2505.21936)（项目页：[RedTeamCUA](https://osu-nlp-group.github.io/RedTeamCUA)）：混合 Web-OS 红队 harness；价值在于把网页提示注入、桌面动作和真实 OS 状态结合起来测试 CUA。
- [OpenAgentSafety](https://arxiv.org/abs/2507.06134)：综合 agent 安全评测框架；价值在于用真实工具和多用户设置复现 deployment-like 风险，而不只做静态 prompt 分类。
- [Reflection-Driven Control](https://arxiv.org/abs/2512.21354)：面向可信代码 agent 的控制 harness。核心思想：围绕代码 agent 的行动引入由反思驱动的监督，使执行、补丁生成和验证过程更偏向安全行为。
- [PROTEA](https://arxiv.org/abs/2601.07186)：面向机器人任务规划与执行的安全框架。核心思路是在机器人智能体规划外加入安全检查，使不安全计划能在物理执行前被发现或修正。
- [MirrorGuard](https://arxiv.org/abs/2601.12822)：即插即用的 computer-use agent 防御框架；价值在于用 simulation-to-real reasoning correction 修正可疑 GUI 动作，而不是简单阻断任务。
- [INFA-Guard](https://arxiv.org/abs/2601.14667)：为 LLM 多 agent 系统提供 infection-aware 防御。核心思想：在通信拓扑中定位攻击者和被感染 agent，并通过替换或修复受损节点来抑制恶意传播。
- [MaMa](https://arxiv.org/abs/2602.04431)：博弈论式安全 agent 系统设计 harness；价值在于把 compromised subagents 建模成 meta-agent 与 meta-adversary 之间的 Stackelberg security game。
- [MUZZLE](https://arxiv.org/abs/2602.09222)：面向间接提示注入的 web agent 自适应红队 harness；价值在于搜索固定模板之外的攻击面和 payload。
- [ToolShield](https://arxiv.org/abs/2602.13379)：与 MT-AgentRisk 配套的 training-free 防御框架；价值在于调停多轮 agent 场景中的高风险工具轨迹。
- [SafeAudit](https://arxiv.org/abs/2603.18245)：tool-call safety benchmark 的 meta-audit 框架；价值在于系统枚举 workflow pattern，并找出通过 benchmark 后仍残留的不安全交互。
- [ATBench](https://arxiv.org/abs/2604.02022)：轨迹级安全诊断 harness；价值在于把风险定位到执行轨迹中的具体阶段，便于分析 agent scaffold 的系统性缺陷。
- [Pre-Execution Safety Gate and Task Safety Contracts](https://arxiv.org/abs/2604.05427)：面向 LLM 控制机器人系统的安全 harness。核心思想：在执行前检查任务级安全契约，使不安全计划在物理动作发生前被阻断或修改。
- [SnapGuard](https://arxiv.org/abs/2604.25562)：面向 screenshot-based web agents 的轻量提示注入检测器；价值在于防御恶意指令只出现在渲染页面视觉内容中的 web-agent pipeline。

## 2.9.4 Skill

- [fact-checker](https://skills.sh/daymade/claude-code-skills/fact-checker) 适合在高风险结论输出前追加事实核查和证据支撑检查。
- [validation](https://skills.sh/profpowell/vanilla-breeze/validation) 适合把输出或行动计划过一层规则审计。
- [skill-validator](https://skills.sh/daffy0208/ai-dev-standards/skill-validator) 适合检查技能定义、执行边界和可复用性风险。
- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) 适合为高风险工具调用提供隔离执行环境。
