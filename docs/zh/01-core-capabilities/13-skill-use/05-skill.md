# 1.13.5 Skill

- [SkillFortify](https://arxiv.org/abs/2603.00195)：面向 agentic skill 供应链的形式化分析框架。核心思想是建模 skill 生命周期中的恶意 skill，结合静态分析、capability sandbox 和审计证据，使 skill 生态获得强于启发式扫描的安全保证。
- [SkillNet](http://skillnet.openkg.cn)（论文：[SkillNet](https://arxiv.org/abs/2603.04448)；[开源代码](https://github.com/zjunlp/SkillNet)）更像 skill registry / ontology / marketplace 基础设施，覆盖 skill 创建、评估、连接与检索。
- [SkillSieve](https://arxiv.org/abs/2604.06550)：用于检测恶意 AI agent skill 的分层筛查框架。核心思想是结合快速静态检查、聚焦的 LLM 子分析，并只对可疑 skill 包做更深审查，使 skill 市场能同时筛查代码与 `SKILL.md` 自然语言攻击面。

这条线当前更成熟的是 `benchmark + retrieval/orchestration/runtime + registry`，而不是“专门服务于 skill 调用”的单个 skill。如果要落到工程实践，更值得回看 [0.4.1 Skill Creator](../../00-introduction/04-other.md) 里的 creator / validator / reviewer 路线；它们决定了 skill 是否可发现、可安装、可组合。
