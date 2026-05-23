# 2.5 计算机操作（GUI）

> 上级章节：2. 基础 Agent


## 2.5.1 Leaderboard

- [OSWorld / OSWorld-Verified Leaderboard](https://os-world.github.io/)：持续维护 desktop computer-use 的官方结果表和 verified 轨迹；适合追踪 UI-TARS、Agent S、Claude、Gemini、OpenAI 系列模型以及不同最大步数设置下的可比结果。
- [AndroidWorld 官方 Leaderboard](https://docs.google.com/spreadsheets/d/1cchzP9dlTZ3WXQTfYNhh3avxoLipqHN75v1Tb86uhHo/edit?gid=0#gid=0)：移动端 GUI agent 的公开提交表；从该榜单可追踪 Mobile-Agent、Minitap/mobile-use、DroidRun、FinalRun 等可复用移动 agent harness。
- [WindowsAgentArena Results](https://microsoft.github.io/WindowsAgentArena/)：公开 Windows OS agent 的项目结果、Navi baseline 与 BYOA 复现接口；当前更像官方结果页而非滚动提交榜，但仍是 Windows GUI agent 的主要公开对照入口。
- [OSWorld-Human Efficiency Leaderboard](https://github.com/WukLab/osworld-human)：在 OSWorld 分数之外加入人类参考轨迹和效率指标，避免只看最终成功率而忽略超长、低效或反复试错的完成路径。
- [MMBench-GUI Leaderboard](https://github.com/open-compass/MMBench-GUI)：仓库已公开评测数据与跨平台协议，README 中 leaderboard 仍标记为 coming soon；当前作为跟踪入口，不应当引用为已上线排名。
- [OSWorld-MCP Leaderboard](https://osworld-mcp.github.io/)：面向 GUI + MCP 工具调用的 computer-use 榜单，同时报告 accuracy、tool invocation rate 和 average completion steps；适合比较纯 GUI、工具增强和混合 agent 配置。
- [ClawBench Leaderboard](https://claw-bench.com/)：真实 live website 浏览器 agent 榜单，提供 V1/V2 任务、trace、HTTP interception 与 reward 指标；它同时暴露模型、harness 和真实网站不稳定性对 GUI web agent 的影响。

## 2.5.2 Bench

- [WebArena](https://arxiv.org/abs/2307.13854)（[开源代码](https://github.com/web-arena-x/webarena)）：评测自主网页 agent 在真实可复现网站中的任务完成；核心思想是把电商、论坛、GitLab、地图等完整 Web 应用封装成可重置环境，用最终状态而非只看文本回答评估网页操作。
- [VisualWebArena](https://arxiv.org/abs/2401.13649)（[开源代码](https://github.com/web-arena-x/visualwebarena)）：评测多模态网页 agent；核心思想是在 WebArena 式真实网站基础上加入图像、布局和视觉线索依赖任务，检验 agent 是否能把截图理解与 DOM/文本信息结合起来。
- [OSWorld / OSWorld-Verified](https://arxiv.org/abs/2404.07972)：评测 desktop computer-use 的通用基准；核心思想是把真实操作系统任务抽象成可复现的观察-行动-验证闭环；官方 leaderboard 同时维护原始任务与 verified 轨迹/子集。
- [AndroidWorld](https://arxiv.org/abs/2405.14573)（[开源代码](https://github.com/google-research/android_world)）：评测移动端 GUI agent 的任务完成与泛化；核心思想是用真实 Android 模拟器与可动态实例化任务，把手机操作标准化为可执行 benchmark。
- [WindowsAgentArena](https://arxiv.org/abs/2409.08264)（[开源代码](https://github.com/microsoft/WindowsAgentArena)）：评测 Windows 生态中的 GUI agent 与 skill 组合；核心思想是让真实桌面任务在统一环境里可复现、可回放、可自动比较。
- [A3](https://arxiv.org/abs/2501.01149)（[开源代码](https://github.com/YuxiangChai/A3)）：评测移动 GUI agent 在真实 Android 任务中的关键状态达成；核心思想是用 essential-state procedural evaluation 规避只看最后截图或静态 app 的脆弱性，更直接检查任务中必须发生的状态转移。
- [WorldGUI](https://arxiv.org/abs/2502.08047)（[开源代码](https://github.com/showlab/WorldGUI)）：评测桌面 GUI agent 从任意中间状态启动时的自动化能力；核心思想是把真实用户常见的“半完成/非默认界面”纳入任务初态，检验 planning 与恢复能力而不是只测标准起点。
- [MM-BrowseComp](https://arxiv.org/abs/2502.14595)：评测多模态浏览与信息获取（含 GUI/网页交互成分）；核心思想是把“看、点、读、写”纳入同一条可执行轨迹并可评分。
- [BEARCUBS](https://arxiv.org/abs/2503.07919)（[项目页](https://bear-cubs.github.io/)）：评测 computer-using web agent 在 live web 中完成信息查找、浏览与多模态交互的能力；核心思想是用会持续变化的真实网页内容、视频理解和 3D 导航等任务，避免纯文本检索绕过真实网页操作。
- [RealWebAssist](https://arxiv.org/abs/2504.10445)（[开源代码](https://github.com/SCAI-JHU/RealWebAssist)）：评测真实用户长程网页协助；核心思想是把模糊、会变化、需要分阶段确认的用户指令组织成长序列任务，补足一次性网页 benchmark 对真实协助场景的覆盖不足。
- [OSUniverse](https://arxiv.org/abs/2505.03570)（[开源代码](https://github.com/agentsea/osuniverse)）：评测复杂、多模态、桌面导向 GUI 导航任务；核心思想是用跨应用、跨模态的真实桌面任务补足 OSWorld 之后对视觉理解、工具选择和长链路导航的综合压力测试。
- [RedTeamCUA / RTC-Bench](https://arxiv.org/abs/2505.21936)（[项目页](https://osu-nlp-group.github.io/RedTeamCUA)）：评测混合 Web-OS 环境中 computer-use agent 的间接提示注入风险；核心思想是用真实 GUI/网页动作空间和红队样例暴露跨应用执行时的攻击面。
- [WebChoreArena](https://arxiv.org/abs/2506.01952)（[开源代码](https://github.com/WebChoreArena/WebChoreArena)）：评测网页 agent 处理繁琐复杂网页任务的能力；核心思想是把人类也会觉得重复、分支多、容易出错的 web chores 做成可执行 benchmark，放大鲁棒性和耐心执行问题。
- [VPI-Bench](https://arxiv.org/abs/2506.02456)（数据集：[VPI-Bench/vpi-bench](https://huggingface.co/datasets/VPI-Bench/vpi-bench)）：评测 computer-use / browser-use agent 面对视觉提示注入攻击的安全性；核心思想是把恶意指令嵌入网页视觉内容中，检查 agent 是否会把屏幕文字误当作用户指令执行。
- [GUI-Robust](https://arxiv.org/abs/2506.14477)（[开源代码](https://github.com/chessbean1/GUI-Robust)）：评测 GUI agent 面对真实异常场景时的鲁棒性；核心思想是在常规 GUI 轨迹中加入遮挡、误触、弹窗和环境异常等干扰，观察 agent 是否能从非理想界面状态中恢复。
- [OS-Harm](https://arxiv.org/abs/2506.14866)（[开源代码](https://github.com/tml-epfl/os-harm)）：评测 computer-use agent 在操作系统任务中的安全性；核心思想是基于 OSWorld 覆盖恶意用户请求、提示注入和模型误行为三类风险，检查 agent 是否会在邮件、浏览器、代码编辑器等应用中执行危险动作。
- [OSWorld-Human](https://arxiv.org/abs/2506.16042)（[OSWorld-Human Efficiency Leaderboard](https://github.com/WukLab/osworld-human)；[开源代码](https://github.com/WukLab/osworld-human)）：评测 computer-use agent 相对人类参考轨迹的效率；核心思想是在 OSWorld 上加入人工标注轨迹，用 weighted excess steps 等指标区分“能完成”和“以合理步骤完成”。
- [MMBench-GUI](https://arxiv.org/abs/2507.19478)（[开源代码](https://github.com/open-compass/MMBench-GUI)）：评测 Windows、macOS、Linux、iOS、Android 与 Web 的跨平台 GUI agent；核心思想是把 GUI 内容理解、元素定位、任务自动化和任务协作分层评估，并用效率-质量面积指标衡量执行冗余。
- [FineState-Bench](https://arxiv.org/abs/2508.09241)（[开源代码](https://github.com/AnonymousThewarehouse/FineState-Bench)，[数据集](https://huggingface.co/datasets/Willtime2006/Static-FineBench)）：评测 GUI agent 的细粒度状态控制；核心思想是把感知、定位、操作和状态达成拆成多阶段指标，专门暴露真实 GUI 操作中精细控制与视觉定位瓶颈。
- [SCUBA](https://arxiv.org/abs/2509.26506)（[开源代码](https://github.com/SalesforceAIResearch/SCUBA)）：评测 Salesforce 企业软件中的 computer-use 能力；核心思想是把 CRM 式表单、记录、权限和业务对象放进真实企业 GUI 任务，强调专业 SaaS 操作中的状态一致性与业务规则遵循。
- [BrowserArena](https://arxiv.org/abs/2510.02418)：评测真实开放网页上的 web agent 导航；核心思想是收集用户提交的 live web 任务并用 arena 式比较与逐步人工反馈定位 captcha、弹窗和直接 URL 导航等真实网页失败模式。
- [OSWorld-MCP](https://arxiv.org/abs/2510.24563)（[项目页](https://osworld-mcp.github.io/)）：评测 computer-use agent 在 GUI 操作之外调用 MCP 工具的能力；核心思想是在真实 OSWorld 式环境中引入 158 个跨常用应用的 MCP 工具，并同时报告任务准确率、工具调用率和平均完成步数。
- [MobileWorld](https://arxiv.org/abs/2512.19432)（[开源代码](https://github.com/Tongyi-MAI/MobileWorld)）：评测自主移动 agent 在 agent-user 交互与 MCP 增强环境中的任务完成；核心思想是把移动端 GUI 操作、用户澄清和外部工具调用放进统一 benchmark，补足 AndroidWorld 的静态任务边界。
- [OS-Marathon](https://arxiv.org/abs/2601.20650)（[项目页](https://os-marathon.github.io/)）：评测 computer-use agent 的长程重复 GUI 任务；核心思想是让 agent 在长时间、重复但状态会累积变化的桌面操作中保持节奏、记忆和错误恢复能力。
- [MemGUI-Bench](https://arxiv.org/abs/2602.06075)（[开源代码](https://github.com/lgy0404/MemGUI-Bench)）：评测移动 GUI agent 的记忆能力；核心思想是用跨会话、跨应用和动态环境任务专门测 memory retention 与 cross-session learning。
- [ClawBench](https://arxiv.org/abs/2604.08523)（[项目页](https://claw-bench.com/)；[开源代码](https://github.com/reacher-z/ClawBench)；[数据集](https://huggingface.co/datasets/TIGER-Lab/ClawBench)）：评测真实 live website 上的浏览器 agent；核心思想是用 HTTP 请求拦截、payload judge 和多层轨迹记录，让写操作型网页任务可以被评测而不真实提交破坏性操作。
- [OS-Blind](https://arxiv.org/abs/2604.10577)（[项目页](https://limenlp.github.io/OS_Blind/)）：评测用户指令无害但执行上下文可能有害时的 CUA 安全盲点；核心思想是让危害来自环境状态或执行后果，要求 agent 在 GUI 操作前主动识别风险。
- [Odysseys](https://arxiv.org/abs/2604.24964)（[项目页](https://odysseys-website.pages.dev/)）：评测网页 agent 的真实长程 GUI 任务；核心思想是用现实网站中的多阶段目标和状态依赖测试 agent 的导航、信息整合、错误恢复与持续执行能力。
- [WindowsWorld](https://arxiv.org/abs/2604.27776)：评测 Windows 上的跨应用 GUI 工作流；核心思想是把多应用、多检查点的职业流程显式化，专门放大跨应用协调与阶段性核验失败。
- [SaaS-Bench](https://arxiv.org/abs/2605.15777)（[开源代码](https://github.com/UniPat-AI/SaaS-Bench)）：评测真实 SaaS 系统上的专业工作流；核心思想是把可部署的多应用业务流程、检查点验证和长链路状态维护放进 self-hosted SaaS 环境。

## 2.5.3 Agent Harness

- [SeeAct](https://arxiv.org/abs/2401.01614)（[开源代码](https://github.com/OSU-NLP-Group/SeeAct)；视觉 grounding + 结构信息融合的网页 GUI agent 起点范式，后续被多类 CUA 吸收）
- [Agent S](https://arxiv.org/abs/2410.08164)（[开源代码](https://github.com/simular-ai/Agent-S)；ACI + 分层规划 + 外部知识检索 + 经验记忆的一体化 computer-use workflow）
- [AgentStore](https://arxiv.org/abs/2410.18603)（[开源代码](https://github.com/chengyou-jia/AgentStore)；类 App Store 的异构 agent 动态选择与组合平台）
- [OpenWebVoyager](https://arxiv.org/abs/2410.19609)（[开源代码](https://github.com/MinorJerry/OpenWebVoyager)；通过真实网页探索、反馈和优化构建多模态 web agent，连接 WebArena/VisualWebArena 与开放网页操作）
- [BrowserGym Ecosystem](https://arxiv.org/abs/2412.05467)（[开源代码](https://github.com/ServiceNow/BrowserGym)；统一 WebArena、VisualWebArena、WorkArena 等网页 GUI 环境，并提供可复现评测接口）
- Browser-Use（[开源代码](https://github.com/browser-use/browser-use)；HAL/AssistantBench/Online Mind2Web 等榜单常见的浏览器 agent scaffold，把 Playwright 浏览器状态、动作执行、持久浏览器和工具扩展封装成可直接复用的 web automation harness）
- [UI-TARS](https://arxiv.org/abs/2501.12326)（[开源代码](https://github.com/bytedance/UI-TARS)；端到端视觉-动作 GUI agent，把截图理解、坐标定位、操作历史与动作生成结合到原生 computer-use 轨迹中）
- [PC-Agent](https://arxiv.org/abs/2502.14282)（[开源代码](https://github.com/X-PLUG/MobileAgent/tree/main/PC-Agent)；用 `Manager / Progress / Decision / Reflection` 层级多代理协作处理 PC 上的跨应用复杂任务）
- [Agent S2](https://arxiv.org/abs/2504.00906)（[开源代码](https://github.com/simular-ai/Agent-S)；generalist-specialist 组合的多角色工作流）
- [GUI-R1](https://arxiv.org/abs/2504.10458)（[开源代码](https://github.com/ritzz-ai/GUI-R1)；R1-style vision-language-action 模型，把 reinforcement fine-tuning 引入通用 GUI action 生成）
- [ARPO](https://arxiv.org/abs/2505.16282)（[开源代码](https://github.com/dvlab-research/ARPO)；用 experience replay 改造 GRPO，在 OSWorld 这类长程 GUI 环境中做端到端 policy optimization）
- [LiteCUA](https://arxiv.org/abs/2505.18829)（开源代码：未公开；把“计算机”抽象成 MCP server 的环境语义层，降低动作空间复杂度）
- [UI-Evol](https://arxiv.org/abs/2505.21964)（[开源代码](https://github.com/microsoft/FIVE-UI-Evol)；可插拔知识演化模块，基于 Agent S2 在 OSWorld 上提升成功率并降低行为方差）
- [ZeroGUI](https://arxiv.org/abs/2505.23762)（[开源代码](https://github.com/OpenGVLab/ZeroGUI)；用自动任务生成、自动奖励估计和在线强化学习降低 GUI agent 数据收集成本）
- [CoAct-1](https://arxiv.org/abs/2508.03923)（[开源代码](https://github.com/SalesforceAIResearch/CoAct)；显式多代理协作，包含 `Orchestrator / GUI Operator / Programmer`）
- [Mobile-Agent-v3](https://arxiv.org/abs/2508.15144)（[开源代码](https://github.com/X-PLUG/MobileAgent)；GUI foundation model 与通用 GUI agent framework，在 OSWorld/AndroidWorld 等多基准上报告结果）
- [UI-TARS-2](https://arxiv.org/abs/2509.02544)（[开源代码](https://github.com/bytedance/UI-TARS-desktop)；把 GUI agent 拆成更清晰的感知、规划和执行栈，面向桌面/浏览器原生自动化提供可运行 harness）
- [Agentic Lybic](https://arxiv.org/abs/2509.11067)（[开源代码](https://github.com/xlang-ai/OSWorld/tree/main/mm_agents/maestro)；FSM 驱动的 `Controller / Manager / Worker / Evaluator` 分工与质量控制）
- [Surfer 2](https://arxiv.org/abs/2510.19949)（开源代码：未公开；跨 web/desktop/mobile 的统一架构：层级上下文、计划执行解耦、自验证与自恢复）
- [AgentProg](https://arxiv.org/abs/2512.10371)（[开源代码](https://github.com/MobileLLM/AgentProg)；把长程 GUI 交互历史重写成带变量和控制流的程序化上下文，并用全局 belief state 维持移动 GUI 任务中的部分可观测状态）
- [OS-Symphony](https://arxiv.org/abs/2601.07779)（[开源代码](https://github.com/OS-Copilot/OS-Symphony)；Orchestrator + Reflection-Memory + 教程检索的跨平台 computer-use 框架）
- [CUA-Skill Agent](https://arxiv.org/abs/2601.21123)（[开源代码](https://github.com/microsoft/cua_skill)；结构化 GUI skill 库 + 参数化组合图 + 动态 skill 检索/实例化 + memory-aware recovery）
- [BEAP-Agent](https://arxiv.org/abs/2601.21352)（开源代码：未公开；把 GUI 执行显式建模为 DFS，支持多级回溯与动态任务跟踪）
- [Minitap mobile-use](https://arxiv.org/abs/2602.07787)（[开源代码](https://github.com/minitap-ai/mobile-use)；围绕 AndroidWorld 的任务分解式多代理移动端 harness，通过 supervisor、视觉定位和动作执行分工把移动 GUI 任务拆成可复核子目标）
- [Natural-Language Agent Harnesses](https://arxiv.org/abs/2603.25723)（[开源代码](https://github.com/curated-skills/LinguaClaw)；把 harness 逻辑外显成可编辑自然语言文档，用共享 runtime 执行、写回状态与工件）

## 2.5.4 Skill

- [screenshot](https://skills.sh/openai/skills/screenshot)（截图能力；偏感知层，OSWorld 弱相关但常用）
- [playwright-interactive](https://skills.sh/openai/skills/playwright-interactive)（浏览器/Electron 交互；OSWorld 弱相关但可覆盖部分 GUI 界面）
- [pc-control](https://github.com/openclaw/skills/tree/main/skills/zeron-g/pc-control)（桌面截图、键鼠控制与闭环验证）
- [computer-use-agents](https://skills.sh/sickn33/antigravity-awesome-skills/computer-use-agents)（computer-use 设计模式库）
- [ubuntu-desktop-control](https://github.com/lommaj/ubuntu-desktop-control)（Ubuntu / X11 桌面控制：`xdotool`、`scrot` 等）
- [agent-desktop](https://skills.sh/lahfir/agent-desktop/agent-desktop)（桌面 GUI 自动化工具型 skill；实现偏 macOS，Linux/Windows 不完整）
- [desktop-controller-skill](https://github.com/24kchengYe/desktop-controller-skill)（Windows 本地 computer use；Win32 + Playwright 双引擎）
- [guicountrol](https://clawhub.ai/dreamtraveler13/guicountrol)（Linux GUI 控制：`xdotool`、`wmctrl`、`dogtail`，含可访问性树检查）
- [computer-use](https://clawhub.ai/Ram-Raghav-S/computer-use)（无头 Linux server：`Xvfb`、`XFCE`、`xdotool`，含 VNC 观察能力）
- [desktop-control](https://clawhub.ai/matagul/desktop-control)（通用桌面自动化：键鼠、截图、窗口管理与图像识别）
- [turix-cua](https://clawhub.ai/Tongyu-Yan/turix-cua)（桌面 GUI 自动化与工作流编排；调用其自有 CUA 模型）
