# 2.9 Agent Safety

> Parent section: 2. Foundation Agents


## 2.9.1 Leaderboard

- [CAIS AI Dashboard](https://dashboard.safe.ai/): Includes Risk Index, capability index, and automation views, and is currently the most suitable public safety overview for observing the joint evolution of capabilities and risks across models.
- [SafePro](https://safeprobench.github.io/safepro/): A project page for professional-grade agent safety, providing benchmark descriptions and result signals such as unsafe rate; useful for tracking "can complete but unsafe" failure modes in real professional work.

Note: Agent safety does not yet have a mature, unified, continuously submitted public leaderboard comparable to SWE-bench or Terminal-Bench. Project pages, dashboards, and result tables inside papers are currently more common.

## 2.9.2 Bench

- [SafeArena](https://arxiv.org/abs/2503.04957) ([project page](https://safearena.github.io/)): Evaluates how autonomous web agents behave on safety-related and harmful web tasks. Core idea: pair safe and harmful tasks to observe whether agents comply with risky requests involving misinformation, illegal activity, harassment, cybercrime, bias, and related harms.
- [RedTeamCUA / RTC-Bench](https://arxiv.org/abs/2505.21936) ([project page](https://osu-nlp-group.github.io/RedTeamCUA)): Evaluates red-team testing for computer-use agents in hybrid Web-OS environments. Core idea: use 864 indirect prompt-injection examples and real GUI/web action spaces to expose the attack surface of CUA during cross-application execution.
- [VPI-Bench](https://arxiv.org/abs/2506.02456) (dataset: [VPI-Bench/vpi-bench](https://huggingface.co/datasets/VPI-Bench/vpi-bench)): Evaluates visual prompt-injection robustness for computer-use/browser-use agents. Core idea: embed malicious instructions into web screenshots and visual content to test whether agents execute attack text on the screen as user intent.
- [OS-Harm](https://arxiv.org/abs/2506.14866) ([open-source code](https://github.com/tml-epfl/os-harm)): Evaluates computer-use agent safety in operating-system tasks. Core idea: build three risk classes on top of OSWorld, namely malicious user requests, prompt injection, and model misbehavior, checking whether agents perform dangerous actions in email, browsers, code editors, and other applications.
- [OpenAgentSafety](https://arxiv.org/abs/2507.06134): Evaluates comprehensive safety for realistic multi-tool, multi-user agents. Core idea: connect browsers, code execution, file systems, shells, and messaging platforms, covering eight risk categories in multi-turn, multi-user tasks.
- [OASIS](https://arxiv.org/abs/2511.08487): Evaluates agent safety vulnerabilities under hidden intent and task complexity. Core idea: hide dangerous user intent inside complex task structures and check whether agents focus only on surface-level task plausibility while missing underlying risk.
- [SafePro](https://arxiv.org/abs/2601.06663) ([project page](https://safeprobench.github.io/safepro/)): Evaluates safety for professional-grade AI agents. Core idea: jointly assess task completion and unsafe actions in professional services and real work tasks, avoiding deployability judgments based only on output quality.
- [ATBench](https://arxiv.org/abs/2604.02022) (dataset: [AI45Research/ATBench](https://huggingface.co/datasets/AI45Research/ATBench)): Evaluates safety diagnostics for long-horizon agent trajectories. Core idea: organize trajectory-level samples by risk source, failure mode, and real-world harm, analyzing whether risk appears during planning, tool use, environment observation, or recovery.
- [OS-Blind](https://arxiv.org/abs/2604.10577) ([project page](https://limenlp.github.io/OS_Blind/)): Evaluates CUA risks where the user instruction itself is harmless but the execution context may be harmful. Core idea: shift safety judgment from "reading the user request" to "reading the environment state and execution consequences," specifically exposing blind spots in computer-use agents.
- [SkillSafetyBench](https://arxiv.org/abs/2605.12015): Evaluates agent safety under skill-facing attack surfaces. Core idea: treat third-party skills, local artifacts, and task materials as attack surfaces, checking whether agents exceed authority or execute dangerous workflows when invoking skills.

## 2.9.3 Agent Harness

- [ST-WebAgentBench](https://arxiv.org/abs/2410.06703) ([open-source code](https://github.com/segev-shlomov/ST-WebAgentBench)): A safety and trustworthiness evaluation harness for web agents; its value lies in organizing web environments, task states, and safety constraints into a reproducible browser-agent testing protocol.
- [RedTeamCUA](https://arxiv.org/abs/2505.21936) (project page: [RedTeamCUA](https://osu-nlp-group.github.io/RedTeamCUA)): A hybrid Web-OS red-team harness; its value lies in combining web prompt injection, desktop actions, and real OS state to test CUA.
- [OpenAgentSafety](https://arxiv.org/abs/2507.06134): A comprehensive agent-safety evaluation framework; its value lies in using real tools and multi-user settings to reproduce deployment-like risks rather than only static prompt classification.
- [ATBench](https://arxiv.org/abs/2604.02022): A trajectory-level safety diagnostic harness; its value lies in locating risk in specific stages of an execution trajectory, making it easier to analyze systematic defects in agent scaffolds.

## 2.9.4 Skill

- [fact-checker](https://skills.sh/daymade/claude-code-skills/fact-checker) is suitable for adding fact-checking and evidence-support checks before high-risk conclusions are output.
- [validation](https://skills.sh/profpowell/vanilla-breeze/validation) is suitable for passing outputs or action plans through a layer of rule auditing.
- [skill-validator](https://skills.sh/daffy0208/ai-dev-standards/skill-validator) is suitable for checking skill definitions, execution boundaries, and reusability risks.
- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) is suitable for providing isolated execution environments for high-risk tool calls.
