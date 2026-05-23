# 1.4.4 Agent Harness

- [RARR](https://arxiv.org/abs/2210.08726)（[开源代码](https://github.com/anthonywchen/RARR)）：retrieval-backed hallucination repair；典型闭环为 `声明切分 -> 检索证据 -> 证据过滤/对齐 -> 回填修订`。
- [SelfCheckGPT](https://arxiv.org/abs/2303.08896)（[开源代码](https://github.com/potsawee/selfcheckgpt)）：通过自一致性与变体采样检测可疑声明；核心思想是把“不一致”作为 hallucination 风险信号。
- [FacTool](https://arxiv.org/abs/2307.13528)（[开源代码](https://github.com/GAIR-NLP/factool)）：工具增强事实性检测框架；核心思想是把 QA、代码、数学和科学文献综述等任务中的生成内容拆解为可查证单元，再调用外部工具与证据判断 factual errors。
- [Chain-of-Verification](https://arxiv.org/abs/2309.11495)：把复杂回答拆成待核验子声明并逐条验证；核心思想是把核验控制流显式化，降低“整体看起来合理但细节胡说”。
- [SAFE](https://arxiv.org/abs/2403.18802)（[开源代码](https://github.com/google-deepmind/long-form-factuality)）：搜索增强事实性评测 harness；核心思想是把长回答拆成 atomic claims，再用检索证据逐条判断是否被支撑。
- [MiniCheck](https://arxiv.org/abs/2404.10774)（[开源代码](https://github.com/Liyan06/MiniCheck)）：轻量 grounded factuality verifier；核心思想是在 LLM-AggreFact 上训练/评测小型检测器，用较低成本判断回答与参考文档是否一致。
- [RefChecker](https://arxiv.org/abs/2405.14486)（[开源代码](https://github.com/amazon-science/RefChecker)）：reference-based 细粒度幻觉检查器；核心思想是把回答拆成可核验片段并与参考证据对齐，输出 span/claim 级 hallucination 判断。
- [RAGChecker](https://arxiv.org/abs/2408.08067)（[开源代码](https://github.com/amazon-science/RAGChecker)）：RAG 系统诊断式评测框架；核心思想是从 claim-level 支撑、遗漏和噪声定位检索端与生成端的事实性错误。
- [SelfCheckAgent](https://arxiv.org/abs/2502.01812)：多 agent 零资源幻觉检测框架；核心思想是组合 symbolic、specialized detection 与 contextual consistency agents，用多维一致性信号判断生成内容是否可靠。
- [REFIND](https://arxiv.org/abs/2502.13622)（[开源代码](https://github.com/oneonlee/REFIND)）：retrieval-augmented factuality hallucination detection；核心思想是用检索文档与 context sensitivity ratio 定位幻觉 span，并在多语言设置中验证鲁棒性。
- [FactSelfCheck](https://arxiv.org/abs/2503.17229)：基于 fact triple 的黑盒幻觉检测；核心思想是把回答拆成细粒度事实后做多轮一致性检查。
- [Premise Verification](https://arxiv.org/abs/2504.06438)：面向 false-premise query 的检索增强逻辑验证框架；核心思想是在生成前把用户问题转成逻辑前提并逐条查证，提前阻断“顺着错误前提胡编”的幻觉链路。
- [FaithJudge](https://arxiv.org/abs/2505.04847)（[开源代码](https://github.com/vectara/FaithJudge)）：面向 factual faithfulness 的自动 judge；核心思想是用可复用评测器判断生成内容是否忠实于给定证据，并服务于 Vectara 幻觉榜单的后续版本。
