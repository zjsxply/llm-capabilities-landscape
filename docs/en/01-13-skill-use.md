# 1.13 Skill Use

> Parent section: 1. Foundational Capabilities


Note: This thread is not about "whether an API call can be made correctly", but about whether an agent can retrieve, select, combine, and reuse packaged skills or workflow templates.
Compared with `1.11 Tool Use`, skill use adds another layer of runtime responsibility: `skill discovery -> adaptation -> orchestration -> persistent reuse`.

## 1.13.1 Leaderboard

- [SkillsBench Leaderboard](https://www.skillsbench.ai/leaderboard): The most direct continuously updated leaderboard for skill use.
  It compares agents under conditions such as `no skill / curated skill / self-generated skill`, making it useful for judging whether skills truly improve task success rather than only comparing base model capability.
- [PinchBench](https://pinchbench.com/about): A real-task leaderboard and evaluation entry point in the OpenClaw ecosystem.
  It is not a pure skill benchmark, but its tasks include ClawHub skill installation, skill search, and skill-use scenarios, so it is a useful practical supplement for productized skill ecosystems.
- [Claw-Eval-Live](https://claw-eval-live.github.io/): A continuously updated workflow-agent leaderboard that explicitly uses ClawHub skill signals to construct tasks.
  It is better suited for observing whether agents can discover, install, call, and verify skills in dynamic workflows, rather than only comparing pass rates under ideal given-skill settings.

## 1.13.2 Bench

- [LifelongAgentBench](https://arxiv.org/abs/2505.11942): What it evaluates: whether LLM agents can learn, remember, and reuse skills across long task sequences.
  Core idea: chain tasks as episodes so that agents use past experience, tool-operation patterns, and transferable skills on new tasks instead of only planning within a single task.
- [SkillsBench](https://arxiv.org/abs/2602.12670) ([code](https://github.com/benchflow-ai/skillsbench); [website](https://www.skillsbench.ai/)): What it evaluates: whether agents achieve stable task-success gains when using human-written or self-generated skills.
  Core idea: make skill value measurable through a three-way comparison of `no skill / curated skill / self-generated skill`; the paper version covers 86 tasks across 11 domains, while the current website shows 84 tasks.
- [SkillInject](https://arxiv.org/abs/2602.20156): What it evaluates: whether agents are vulnerable to prompt injection embedded in skill files. Core idea: treat reusable skills as an explicit attack surface and measure whether malicious instructions redirect agent behavior during execution.
- [SkillCraft](https://arxiv.org/abs/2603.00718) ([code](https://github.com/shiqichen17/SkillCraft); [project page](https://skillcraft-website.github.io/page/)): What it evaluates: whether agents can abstract atomic tools into reusable skills and cache and reuse them across long-horizon tasks.
  Core idea: stress-test skill abstraction through `quantitative scaling` and `structural scaling`; it considers not only instance-level success but also efficiency gains from skill reuse.
- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) ([code](https://github.com/GeniusHTX/SWE-Skills-Bench); [dataset](https://huggingface.co/datasets/GeniusHTX/SWE-Skills-Bench)): What it evaluates: whether agent skills truly help on real software engineering tasks.
  Core idea: shift the evaluation target from "can a coding agent fix code" to "does a given skill improve the success rate, efficiency, and behavior quality of software engineering agents".
- [MM Claw skill-compliance suite](https://www.minimax.io/news/minimax-m27-en) (model-card-only; no standalone public release confirmed): What it evaluates: whether an agent can keep following and reusing more than 40 complex skills during extended OpenClaw-style work. Core idea: treat skill adherence itself as an evaluation signal, complementing public skill-search and skill-injection benchmarks.
- [Agentic Skills in the Wild](https://arxiv.org/abs/2604.04323): What it evaluates: whether skills still help when agents search for, select, and use skills that do not perfectly match the task in a real skill ecosystem.
  Core idea: relax the "ideal skill is directly provided" setting into retrieval, noise, and adaptation pressure, then measure how skill utility degrades under realistic settings.
- [SkillLearnBench](https://arxiv.org/abs/2604.20087) ([code](https://github.com/cxcscmu/SkillLearnBench)): What it evaluates: continual skill learning and generation; core idea: evaluate skill quality, execution trajectories, and task outcomes together to see whether reusable skills are learned reliably.
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139) ([project page](https://claw-eval-live.github.io/); [code](https://github.com/Claw-Eval-Live/Claw-Eval-Live)): What it evaluates: continuously updated real workflow-agent tasks that explicitly use ClawHub skill signals. Core idea: place skill discovery, installation, invocation, and verification inside a periodically refreshed task distribution, complementing the static comparisons in SkillsBench.
- [SkillRet](https://arxiv.org/abs/2605.05726): What it evaluates: large-scale retrieval over agent skill libraries; core idea: treat skill selection as a retrieval problem and evaluate long queries, noisy libraries, and NDCG / recall.
- [FORTIS](https://arxiv.org/abs/2605.09163): What it evaluates: whether agent skills cross least-privilege boundaries.
  Core idea: split evaluation into "whether the minimally sufficient skill is selected" and "whether execution expands to tools or actions outside that skill", elevating the skill layer from an organizational abstraction to a measurable permission boundary.
- [SkillSafetyBench](https://arxiv.org/abs/2605.12015): What it evaluates: whether agents facing a skill-facing attack surface can be induced by third-party skills, local materials, or local artifacts into unsafe actions.
  Core idea: combine ordinary tasks, risk domains, malicious or benign skill materials, and rule validators in a runnable environment, showing that skill safety cannot rely only on model-level alignment evaluations.
- [AgentTrap](https://arxiv.org/abs/2605.13940) ([code](https://github.com/zhmzm/AgentTrap); [dataset](https://huggingface.co/datasets/zhmzm/AgentTrap)): What it evaluates: whether agents blindly execute malicious runtime behavior embedded in third-party skills.
  Core idea: combine ordinary user tasks, malicious or benign skill packages, and sandboxed execution environments, then judge attack success, blocking, non-triggering, and no-evidence outcomes from full trajectories.
- [SkillGenBench](https://arxiv.org/abs/2605.18693): What it evaluates: the skill generation pipeline of LLM agents; core idea: go beyond final task success by evaluating skill distillation, executability, generalization, and later reuse.
- [PinchBench](https://pinchbench.com/about) ([code](https://github.com/pinchbench/skill)): Better treated as a practical supplementary benchmark for skill use rather than a purely academic "skills benchmark".
  It primarily evaluates the overall execution of OpenClaw agents on real tasks, but its task set explicitly includes `ClawHub skill installation` and `skill search/installation` scenarios, filling in skill integration and invocation capability in product ecosystems.

## 1.13.3 Agent Harness

- [SkillFlow](https://arxiv.org/abs/2504.06188): A multi-stage agent skill retrieval pipeline; core idea: model skill acquisition as information retrieval by chaining dense retrieval, cross-encoder reranking, and LLM selection over about 36K community `SKILL.md` definitions.
- [CUA-Skill](https://arxiv.org/abs/2601.21123) ([project page](https://microsoft.github.io/cua_skill/)): A structured skill base and CUA-Skill Agent for computer-use agents; core idea: package GUI operation knowledge as skills with parameterized execution and composition graphs, then call them through retrieval, parameter instantiation, and memorized failure recovery.
- [Skill-Pro](https://arxiv.org/abs/2602.01869): A procedural-skill learning harness. Core idea: learn executable skills from episodic experience with explicit activation, execution, and termination conditions.
- [SkillRL](https://arxiv.org/abs/2602.08234) ([code](https://github.com/aiming-lab/SkillRL)): Recursive skill-augmented reinforcement learning; core idea: summarize experience into reusable skills and continue reading, extending, and validating the skill bank in later RL iterations.
- [AgentSkillOS](https://arxiv.org/abs/2603.02176) ([code](https://github.com/ynulihao/AgentSkillOS)): An OS-style route for skill retrieval and orchestration; it decomposes skill use into `capability tree retrieval -> DAG orchestration -> artifact-rich output evaluation`.
  Core idea: compare "flat direct invocation" with "structured retrieval + DAG composition" at ecosystem scales from 200 to 200K skills; the paper also provides 30 artifact-rich tasks across five categories, showing that skill use is not only about finding a skill, but about organizing multiple skills into an executable pipeline.
- [XSkill](https://arxiv.org/abs/2603.12056): A continual multimodal-agent skill harness. Core idea: jointly retain visual experiences and structured reusable skills so later tasks can draw on both episodic evidence and procedural abstractions.
- [Memento-Skills](https://arxiv.org/abs/2603.18743) ([code](https://github.com/Memento-Teams/Memento-Skills)): A generalist agent system that treats reusable skills as persistent, evolvable memory.
  Core idea: use read-write reflective learning to select, update, and extend Markdown skill files, allowing agents to continually reshape task-specific agents without updating model parameters.
- [Trace2Skill](https://arxiv.org/abs/2603.25158): A trajectory-to-skill distillation harness. Core idea: analyze execution trajectories in parallel and hierarchically consolidate local lessons into transferable agent skills.
- [SkVM](https://arxiv.org/abs/2604.03088) ([code](https://github.com/SJTU-IPADS/SkVM)): Skill compilation and runtime; core idea: treat skills as compilable artifacts for capability binding, concurrent extraction, and JIT hardening, improving portability across harnesses.
- [SkillFoundry](https://arxiv.org/abs/2604.03964) ([code](https://github.com/ma-compbio-lab/SkillFoundry)): Builds self-evolving skill libraries from heterogeneous scientific and engineering resources.
  Core idea: extract procedural knowledge from documents, repositories, scripts, notebooks, databases, and papers into skill packages with inputs, outputs, execution steps, environment assumptions, provenance, and tests, then close the loop through expansion, repair, merge, and pruning.
- [SkillX](https://arxiv.org/abs/2604.04804) ([code](https://github.com/zjunlp/SkillX)): Automatically builds plug-and-play skill knowledge bases.
  Core idea: distill trajectories into a three-level structure of strategic plans, functional skills, and atomic skills, then iteratively correct and actively expand skill coverage through execution feedback.
- [Graph of Skills](https://arxiv.org/abs/2604.05333) ([code](https://github.com/davidliuk/graph-of-skills)): Dependency-aware structured retrieval for skills; core idea: replace flat skill lists with structured context containing prerequisite relations, reducing blind selection.
- [From Skills to Talent](https://arxiv.org/abs/2604.22446): Organizes heterogeneous agents as portable Talents. Core idea: package skills, tools, and runtime configuration into recruitable agent identities, then use an Explore-Execute-Review tree search and a Talent Market to assemble, execute, and improve multi-agent organizations dynamically.
- [SkCC](https://arxiv.org/abs/2605.03353): Cross-framework skill compilation and security hardening; core idea: use the strongly typed intermediate representation SkIR to decouple the semantics of Markdown skills from the prompt formats of different agent frameworks, while incorporating permissions, safety checks, and portability into the compilation process.
- [SPARK](https://arxiv.org/abs/2605.09192) ([code](https://github.com/EtaYang10th/spark-skills)): Structured pipelines for autonomous runnable tasks; core idea: compress post-task experience into runnable skill flows, emphasizing posterior skill formation and later reuse.
- [SkillRAE](https://arxiv.org/abs/2605.10114): Skill-based context compilation for retrieval-augmented execution; core idea: compile retrieved skills into compact, grounded, executable context instead of directly stuffing a set of raw Markdown skills into the agent.
- [SkillEvolver](https://arxiv.org/abs/2605.10500): An online skill-learning meta-skill; core idea: package the process of "write, deploy, and revise domain skills after failure" as a meta-skill, using fresh-agent audit to avoid overfitting only to the current agent.
- [CTA / Counterfactual Trace Auditing](https://arxiv.org/abs/2605.11946): A trajectory-level auditing framework for skill influence; core idea: align same-task trajectories with and without skills segment by segment and annotate skill influence patterns, addressing behavioral changes that pass-rate-only evaluation may miss.

## 1.13.4 Skill

- [SkillNet](http://skillnet.openkg.cn) (paper: [SkillNet](https://arxiv.org/abs/2603.04448); [code](https://github.com/zjunlp/SkillNet)) is closer to skill registry / ontology / marketplace infrastructure, covering skill creation, evaluation, connection, and retrieval.

This thread is currently more mature around `benchmark + retrieval/orchestration/runtime + registry` than around a single skill dedicated to skill use.
For engineering practice, it is more useful to revisit the creator / validator / reviewer paths in `0.3 Skill Creator`; they determine whether skills are discoverable, installable, and composable.
