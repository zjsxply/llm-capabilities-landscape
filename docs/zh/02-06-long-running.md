# 2.6 长时运行

> 上级章节：2. 基础 Agent


## 2.6.1 Leaderboard

- [AssistantBench Leaderboard](https://huggingface.co/spaces/AssistantBench/leaderboard)：公开真实耗时网页助理任务的提交入口；它把 test set 答案隐藏并用 Hugging Face portal 收集预测，适合跟踪 web agent 在长程浏览与信息转移任务上的持续进展。
- [METR Time Horizon Reports](https://github.com/METR/eval-analysis-public)：持续发布 time-horizon 版本化报告和可复现分析代码；它不是单一分数榜，而是把 agent 能完成的任务人类时长作为长期自治能力曲线来比较。
- [OSWorld-Human Efficiency Leaderboard](https://github.com/WukLab/osworld-human)：把 OSWorld 成功率和人类参考轨迹效率放在一起比较，特别适合发现长程 GUI agent 通过大量冗余步骤“勉强完成”的问题。
- [HAL Long-Horizon Tracks](https://hal.cs.princeton.edu/)：Princeton HAL 聚合 AssistantBench、GAIA、Online Mind2Web 等任务，并报告成本、运行时间和 pass rate；可作为跨 benchmark 比较 long-horizon agent harness 的元榜单。
- [ClawMark Leaderboard](https://claw-mark.com/leaderboard)：面向 1 到 3 天 timeline 的 coworker-agent 任务榜单，覆盖多模态输入、日历等待、消息协同和跨天状态维护，是比单会话长任务更接近 long-running autonomy 的公开入口。

## 2.6.2 Bench

- [AssistantBench](https://arxiv.org/abs/2407.15711)（[项目页](https://assistantbench.github.io/)）：评什么：真实、耗时的开放网页助理任务。核心思想：让 agent 在房产监控、商户搜索等需要持续浏览和多步筛选的任务中工作，并用自动评价检查最终结果，早期暴露了网页 agent 在长时现实任务上的不稳定性。
- [Vending-Bench](https://arxiv.org/abs/2502.15840)：评什么：长时运行自治体在超长时间跨度上的一致性与稳定性（以“自动经营售货机”为简化业务场景，单次运行可达 >20M tokens）。核心思想：把每一步都很简单但长程耦合的决策链拉长，显式暴露“高方差、失控（meltdown loops）、错误状态难以恢复”等长程 failure mode。
- [METR Time Horizon](https://arxiv.org/abs/2503.14499)（[开源分析代码](https://github.com/METR/eval-analysis-public)）：评什么：AI agent 能稳定完成多长的人类工作时长任务。核心思想：按合格人类完成时间标定任务难度，并用成功率曲线估计 p50/p80 time horizon，形成可随模型和 agent 系统更新的长期自治能力尺度。
- [RealWebAssist](https://arxiv.org/abs/2504.10445)（[开源代码](https://github.com/SCAI-JHU/RealWebAssist)）：评什么：真实用户长程网页协助。核心思想：把用户会补充、修正和模糊表达的需求拆成顺序指令，考察 agent 是否能在长时间交互中维持目标、识别需要澄清的点并持续推进。
- [OSWorld-Human](https://arxiv.org/abs/2506.16042)（[OSWorld-Human Efficiency Leaderboard](https://github.com/WukLab/osworld-human)；[开源代码](https://github.com/WukLab/osworld-human)）：评什么：computer-use agent 相对人类参考轨迹的效率。核心思想：在 OSWorld 成功率之外加入 human trace 和 weighted excess steps 等指标，识别“能完成但执行极低效”的长程 GUI agent。
- [OdysseyBench](https://arxiv.org/abs/2508.09124)（[开源代码](https://github.com/microsoft/OdysseyBench)）：评什么：长程办公生产力 workflow 中的记忆与上下文复用。核心思想：围绕文档、邮件、日历和表格构造跨阶段状态依赖，专门检查 agent 在多步执行后是否还能正确引用早期结果。
- [Gaia2](https://arxiv.org/abs/2509.17158)（[开源代码](https://github.com/facebookresearch/meta-agents-research-environments)）：评什么：动态、异步、会随时间变化的 realistic agent 环境。核心思想：把任务从一次性问答推进到持续变化的环境状态、通知和外部系统交互，要求 agent 在长程上下文中维护目标、更新计划并适应新信息。
- [HAL / Holistic Agent Leaderboard](https://arxiv.org/abs/2510.11977)（[HAL Long-Horizon Tracks](https://hal.cs.princeton.edu/)；[开源代码](https://github.com/princeton-pli/hal-harness)）：评什么：跨 AssistantBench、GAIA、Online Mind2Web 等任务的长程 agent 统一比较。核心思想：把 accuracy、cost、runtime 和 traces 放到同一 leaderboard/harness 中，便于比较不同 long-horizon agent scaffold 的通用性。
- [DeepPlanning](https://arxiv.org/abs/2601.18137)（[项目页](https://qwenlm.github.io/Qwen-Agent/en/benchmarks/deepplanning/)）：评什么：长程 agentic planning 与多步骤执行。核心思想：用需要深度分解、约束跟踪和阶段性回填的任务专门测 agent 是否能把高层目标稳定落到长链路行动序列。
- [OS-Marathon](https://arxiv.org/abs/2601.20650)（[项目页](https://os-marathon.github.io/)）：评什么：computer-use agent 在长时、重复 GUI 任务中的稳定性。核心思想：把单步难度不高但持续时间长、状态会累积的桌面任务拉长，观察 agent 的节奏保持、记忆污染、早停和错误恢复失败。
- [AgentLongBench](https://arxiv.org/abs/2601.20730)：评什么：长上下文 agent 的动态环境回合；核心思想：把静态检索题改成环境 rollouts，专门测多轮反馈、非线性推理和信息整合在长链路中的衰减。
- [TRIP-Bench](https://arxiv.org/abs/2602.01675)：评什么：真实旅行规划场景中的长程多轮交互 agent。核心思想：用 18 个工具、40+ 旅行约束、最多 15 轮用户交互和 150+ 次工具调用，专门测试全局约束维护、需求变化适应与长上下文下的版本修订能力。
- [EcoGym](https://arxiv.org/abs/2602.09514)（[开源代码](https://github.com/OPPO-PersonalAI/EcoGym)）：评什么：交互式经济系统中的长时程 `plan-and-execute` 能力；核心思想：在统一接口下提供 `Vending / Freelance / Operation` 三类环境，以 1000+ steps 的长时域预算动作评估长期策略一致性、稳健性与收益表现。
- [LongCLI-Bench](https://arxiv.org/abs/2602.14337)（[开源代码](https://github.com/finyorko/longcli-bench)）：评什么：命令行环境中的长程 agentic programming。核心思想：用更长任务跨度、细粒度中间指标和较低污染风险的 CLI 工作流，评估编码 agent 能否持续计划、执行、调试和恢复。
- [MMR-Life](https://arxiv.org/abs/2603.06746)（[开源代码](https://github.com/BugMakerzzz/MMR-Life)）：评什么：日常生活长上下文 agent 的多模态多视角推理。核心思想：用真实世界长时间、多视角、多模态记录测试 agent 是否能跨时间保存、检索并组合生活场景证据。
- [RetailBench](https://arxiv.org/abs/2603.16453)：评什么：现实零售环境中的长程自治决策与策略稳定性。核心思想：在随机需求和外部条件演化下检验 agent 是否能把高层策略与低层执行分开维护，并在复杂度升高时保持长期运营一致性。
- [ClawMark](https://arxiv.org/abs/2604.23781)（[项目页](https://claw-mark.com/)；[开源代码](https://github.com/evolvent-ai/ClawMark)）：评什么：多日历时间跨度的多模态同事型 agent。核心思想：用 1 到 3 天的真实日程、消息、文件和外部事件约束任务，评估 agent 是否能等待、提醒、跨天续接和处理延迟反馈。
- [Odysseys](https://arxiv.org/abs/2604.24964)（[项目页](https://odysseys-website.pages.dev/)）：评什么：真实网页上的长程 agent 任务。核心思想：把现实网站、多阶段目标、状态依赖和错误恢复放进同一条执行轨迹，测试 web agent 是否能在更长时间跨度内保持任务一致性。
- [π-Bench](https://arxiv.org/abs/2605.14678)：评什么：主动式个人助理 agent 的长期偏好、隐含意图和跨会话行动。核心思想：让 agent 在会持续演化的个人事务场景中判断何时主动行动、何时等待确认，以及如何在多轮上下文里保持用户偏好与任务边界。
- [Vending-Bench 2](https://andonlabs.com/evals/vending-bench-2)：评什么：Andon Labs 自动售货机评测的新一版公开长程业务运营 agent 任务。核心思想：保留 Vending-Bench 的一年模拟经营设定，同时加入对抗性供应商、谈判、配送延迟、供应商失效、退款请求和更明确的账户余额评分，放大长期经营稳定性压力。

## 2.6.3 Agent Harness

- AutoGPT（[开源代码](https://github.com/Significant-Gravitas/AutoGPT)）：持续运行式自治代理框架，把任务队列、工具调用、长期执行与结果回写组织成可反复迭代的 agent loop，是公开生态里最早一批强调 long-running autonomy 的实现。
- [Voyager](https://arxiv.org/abs/2305.16291)（[开源代码](https://github.com/MineDojo/Voyager)）以 Minecraft 为平台做“终身学习”式长时程代理，核心 harness 是 `自动课程生成 + skill library + 可执行反馈` 的长期自增量闭环。
- [MemGPT](https://arxiv.org/abs/2310.08560)（[开源代码](https://github.com/cpacker/MemGPT)）把长时运行的核心矛盾显式化为“记忆管理/上下文调度”问题，通过外部 memory 与检索将对话/任务状态从上下文窗口中外置。
- LangGraph（[开源代码](https://github.com/langchain-ai/langgraph)）把 long-running agent 的控制流显式化为 state graph，并提供 checkpointer 等机制，适合把 `checkpoint/rollback/分支恢复/可重复执行` 写进运行时。
- [SeePlanAct (SPA)](https://arxiv.org/abs/2407.15711)（[开源代码](https://github.com/oriyor/assistantbench)；AssistantBench 配套 web agent，在 SeeAct 之上加入显式 planning 与 memory 组件，用于长程网页任务中的阶段计划、信息传递和最终答案聚合）
- [HomerAgent](https://arxiv.org/abs/2508.09124)（[开源代码](https://github.com/microsoft/OdysseyBench)）是 OdysseyBench 配套的长程办公 workflow agent，用显式记忆维护阶段结果，适合分析长期任务中的上下文遗忘、错误复用和阶段间依赖失败。
- [ARE](https://arxiv.org/abs/2509.17158)（[开源代码](https://github.com/facebookresearch/meta-agents-research-environments)）把 long-running harness 做成动态环境运行时，支持异步事件、状态演化、外部工具和评测日志，适合研究持续执行中的计划更新与上下文维护。
- [PRISM](https://arxiv.org/abs/2602.01532)：把主动介入建模为成本敏感选择性行动的 proactive-agent deliberation harness；设计关键词：接受概率校准门控、不确定性感知推理、用户负担控制。

## 2.6.4 Skill

- [implementation-planner](https://skills.sh/jumppad-labs/jumppad/implementation-planner) 适合把长链路任务拆成可 checkpoint 的阶段计划与验收点。
- [tapestry](https://skills.sh/nicepkg/ai-workflow/tapestry) 适合把跨系统工具调用串成可持续运行的业务工作流骨架。
- [error-recovery](https://skills.sh/zpankz/mcp-skillset/error-recovery) 适合作为长时运行中的失败恢复/回滚提示模板。
- [agent-context-loader](https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/agent-context-loader) 适合分批加载任务上下文与持续追加背景材料，缓解长时运行中的上下文组织问题。
