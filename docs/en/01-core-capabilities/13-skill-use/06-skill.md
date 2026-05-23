# 1.13.6 Skill

- [SkillFortify](https://arxiv.org/abs/2603.00195): A formal-analysis framework for agentic skill supply chains. Core idea: model malicious skills across the skill lifecycle, combine static analysis with capability sandboxing and audit evidence, and give skill ecosystems stronger guarantees than heuristic scanning alone.
- [SkillNet](http://skillnet.openkg.cn) (paper: [SkillNet](https://arxiv.org/abs/2603.04448); [code](https://github.com/zjunlp/SkillNet)) is closer to skill registry / ontology / marketplace infrastructure, covering skill creation, evaluation, connection, and retrieval.
- [SkillSieve](https://arxiv.org/abs/2604.06550): A hierarchical triage framework for detecting malicious AI-agent skills. Core idea: combine fast static checks, focused LLM sub-analyses, and deeper review only for suspicious skill packages so skill marketplaces can screen both code and natural-language `SKILL.md` attack surfaces.

This thread is currently more mature around `benchmark + retrieval/orchestration/runtime + registry` than around a single skill dedicated to skill use.
For engineering practice, it is more useful to revisit the creator / validator / reviewer paths in `0.3 Skill Creator`; they determine whether skills are discoverable, installable, and composable.
