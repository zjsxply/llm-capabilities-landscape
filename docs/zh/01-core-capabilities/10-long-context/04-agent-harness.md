# 1.10.4 Agent Harness

注：公开生态里“只为某个长上下文 benchmark 命名”的 solver agent 并不多；更常见的是可复用的长程代理习惯（分段加载、状态摘要、失败分支记录）和可插拔的压缩/检索组件。

- [LLMLingua](https://arxiv.org/abs/2310.05736)（[开源代码](https://github.com/microsoft/LLMLingua)）：可插拔上下文压缩组件，常用于长上下文代理中降低无关 token 干扰并提升有效信息密度。
- [LongLLMLingua](https://arxiv.org/abs/2310.06839)（[开源代码](https://github.com/microsoft/LLMLingua)）：面向更长输入的压缩与重排策略，强调在高压缩率下保留关键推理证据。
- [RAPTOR](https://arxiv.org/abs/2401.18059)（[开源代码](https://github.com/parthsarthi03/raptor)）：用递归摘要树组织文档记忆，让代理在不同粒度的上下文块之间检索和聚合证据。
- [LongAgent](https://arxiv.org/abs/2402.11550)（[评测代码/数据](https://github.com/zuucan/needleinahaystack-plus)）：多 agent 协作式长上下文 harness；核心思想是把超长文本分配给多个 member agent，再由 leader agent 聚合局部证据，适合替代单次全量塞入 prompt 的处理方式。
- [HippoRAG](https://arxiv.org/abs/2405.14831)（[开源代码](https://github.com/OSU-NLP-Group/HippoRAG)）：把知识图谱式关联和海马体启发的检索机制接入 RAG，适合长程事实联想与多跳证据组织。
- [Chain-of-Agents](https://arxiv.org/abs/2406.02818)（[非官方实现](https://github.com/rudrankriyam/Chain-of-Agents)）：把长输入拆成 worker agent 串行处理并逐段传递中间消息，最后由 manager agent 汇总答案，适合长文档问答和摘要类任务。
- [Graph of Agents](https://arxiv.org/abs/2509.06644)（[开源代码](https://github.com/tjoo512/graph-of-agents)）：面向长上下文的图式多 agent 协作 harness；核心思想是把文本块、局部 agent 输出与汇总节点组织成可扩展图结构，用局部处理和跨节点聚合替代单一长 prompt。
