# 1.8.5 Agent Harness

- [Draft, Sketch, and Prove](https://arxiv.org/abs/2210.12283)（[开源代码](https://github.com/albertqjiang/draft_sketch_prove)）：两阶段 formal proving harness，先生成 proof sketch，再调用 prover/hammer 补全正式证明。
- [PAL](https://arxiv.org/abs/2211.10435)（[开源代码](https://github.com/reasoning-machines/pal)）：把数学推理改写为可执行程序再回填答案，是程序化数学 agent 的经典起点。
- [Program of Thoughts](https://arxiv.org/abs/2211.12588)（[开源代码](https://github.com/TIGER-AI-Lab/Program-of-Thoughts)）：显式把中间推理转成程序执行轨迹，降低纯文本推理的算术错误率。
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（[开源代码](https://github.com/princeton-nlp/tree-of-thought-llm)）：将推理轨迹树化并支持分支扩展、回溯与自评，是数学 test-time 搜索的代表性 harness。
- [LeanDojo](https://arxiv.org/abs/2306.15626)（[开源代码](https://github.com/lean-dojo/LeanDojo)）：把前提检索、proof state 交互与 verifier 反馈整合进 proof assistant in the loop 的可复现 runtime。
- [ToRA](https://arxiv.org/abs/2309.17452)（[开源代码](https://github.com/microsoft/ToRA)）：将自然语言推理、代码执行与符号工具调用编排成统一 math agent loop。
- [COPRA](https://arxiv.org/abs/2310.04353)（[开源代码](https://github.com/trishullab/copra)）：面向 Lean 的协作式证明代理，强调规划、检索与证明状态驱动的执行闭环。
- [Newclid](https://arxiv.org/abs/2411.11938)（[开源代码](https://github.com/Newclid/Newclid)）：面向几何证明的神经-符号代理框架，强调可验证搜索过程。
- [StepMathAgent](https://arxiv.org/abs/2503.10105)：面向数学解答的过程评测 agent；核心思想是通过 Tree-of-Error 表示对步骤进行切分、打分、聚合和错误组织，而不是只评最终答案。
- [Prover Agent](https://arxiv.org/abs/2506.19923)（[开源代码](https://github.com/kAIto47802/Prover-Agent)）：以代理式搜索与工具交互提升 Lean 证明求解能力。
- [Code2Math](https://arxiv.org/abs/2603.03202)：用代码智能体演化数学问题的多智能体框架。核心思想：通过代码执行和可解性验证循环，把已有问题转化为更难但可解的新变体，将问题生成变成探索式智能体工作流。
- [QED](https://arxiv.org/abs/2604.24021)：面向开放数学问题的多 agent 证明生成系统；核心思想是把证明搜索、批判、验证焦点与修订分配给专门 agent，以应对研究级证明中的系统性失败模式。
- [STAR-PólyaMath](https://arxiv.org/abs/2605.19338)（[开源代码](https://github.com/Julius-Woo/STAR-PolyaMath)）：面向 MathArena Apex、AIME、Putnam、IMO、HMMT 与 USAMO 等榜单的多 agent 数学推理 harness；核心思想是用 Meta-Strategist、Reasoner-Verifier 和 challenge-step-replan 状态机长期维护策略、回溯失败分支并限制幻觉累积。
