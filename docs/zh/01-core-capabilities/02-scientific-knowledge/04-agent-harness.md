# 1.2.4 Agent Harness

- [ReAct](https://arxiv.org/abs/2210.03629)（[开源代码](https://github.com/ysymyth/ReAct)）：通用“思考-检索/行动-观察”框架；对长尾科学知识任务更像可复用的 `检索 -> 证据整合 -> 再回答` 工作流骨架。
- [RARR](https://arxiv.org/abs/2210.08726)（[开源代码](https://github.com/anthonywchen/RARR)）：`retrieve -> revise -> cite` 框架，适合把知识回答改写为“带引用的可核验结论”。
- [Chain-of-Verification](https://arxiv.org/abs/2309.11495)：提出“先答，再拆验证问题，再回填修订”的通用 factuality workflow；当前未见稳定公开官方代码仓库。
- [DSPy](https://arxiv.org/abs/2310.03714)（[开源代码](https://github.com/stanfordnlp/dspy)）：把检索、提示与评分器组织为可编译/可评测的 program；常用于把 “RAG/证据组织/答案格式” 变成可调参的 harness，而不是一次性 prompt。
- [Agent Laboratory](https://arxiv.org/abs/2501.04227)（[开源代码](https://github.com/SamuelSchmidgall/AgentLaboratory)）：面向科研助手的多阶段工作流；覆盖文献检索、实验执行与报告写作。
- [AgentRxiv](https://arxiv.org/abs/2503.18102)（[开源代码](https://github.com/SamuelSchmidgall/AgentLaboratory)）：共享式研究记忆与协作预印本服务器；让研究 agent 能上传、检索并复用前序结果。
- [The AI Scientist-v2](https://arxiv.org/abs/2504.08066)（[开源代码](https://github.com/SakanaAI/AI-Scientist-v2)）：端到端自动科研系统；核心思想是用 agentic tree search 和实验管理 agent 迭代生成假设、运行实验、分析结果、绘图并撰写论文。
- [SafeScientist](https://arxiv.org/abs/2505.23559)（[开源代码](https://github.com/ulab-uiuc/SafeScientist)）：面向科研 agent 的风险感知 harness；核心思想是在任务输入、协作讨论、工具调用和伦理审稿环节加入安全监控，用 SciSafetyBench 检验拒答与风险规避能力。
- [AlphaEvolve](https://arxiv.org/abs/2506.13131)（开源代码：暂未见稳定公开官方仓库）：面向科学与算法发现的演化式 coding agent；核心思想是让 LLM 直接修改程序，并通过一个或多个自动 evaluator 的反馈进行群体式搜索与迭代优化。
