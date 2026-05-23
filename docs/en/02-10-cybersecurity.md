# 2.10 Cybersecurity

> Parent section: 2. Foundation Agents

Note: Cybersecurity is separated from Terminal Use because the task axis is vulnerability discovery, exploit construction, cyber operations, defense, or security policy. Many benchmarks still use a terminal as the execution substrate, but they should not be mixed into the general terminal-task list.

## 2.10.1 Leaderboard

- [ExploitBench](https://exploitbench.ai/): A project and leaderboard entry point for hierarchical cybersecurity-agent tasks; useful for tracking capability levels from reconnaissance to exploit-chain completion.

## 2.10.2 Bench

- [Cybench](https://arxiv.org/abs/2408.08926): Evaluates cybersecurity capabilities and risks through CTF-style challenges. Core idea: place models in executable security tasks where they must reason, use tools, and complete exploit-oriented objectives rather than only answer cyber knowledge questions.
- [ITBench](https://arxiv.org/abs/2502.05352) ([code](https://github.com/itbench-hub/ITBench)): Evaluates enterprise IT automation workflows such as SRE, CISO, and FinOps. Core idea: put security operations, incident response, and cost/governance work into executable scenarios with interpretable metrics.
- [CVE-Bench](https://arxiv.org/abs/2503.17332) ([code](https://github.com/uiuc-kang-lab/cve-bench)): Evaluates AI agents' ability to exploit real web-application vulnerabilities. Core idea: connect code understanding, vulnerability localization, terminal operations, and exploit construction into one protocol using high-severity CVEs, isolated environments, and executable validation.
- [BountyBench](https://arxiv.org/abs/2505.15216) ([project page](https://bountybench.github.io/)): Evaluates attacker and defender agents in real cybersecurity systems. Core idea: use bug-bounty scenarios and dollar-impact signals to measure Detect, Exploit, and Patch tasks, supplementing security evaluation that only checks CTF success rates.
- [CyberGym](https://arxiv.org/abs/2506.02548) ([project page](https://www.cybergym.io/)): Evaluates vulnerability understanding and exploitation loops for agents in real cybersecurity tasks. Core idea: integrate CVE scenarios, executable environments, tool calls, and final verification so agents must make continuous penetration-testing or repair decisions.
- [SEC-bench](https://arxiv.org/abs/2506.11791) ([project page](https://sec-bench.github.io/); [code](https://github.com/SEC-bench/SEC-bench)): Evaluates PoC generation and vulnerability repair in real software-security tasks. Core idea: automatically construct vulnerable repositories with harnesses and isolated reproduction environments, forcing agents to read code, run verification, and generate attacks or patches.
- [AIRTBench](https://arxiv.org/abs/2506.14682) ([code](https://github.com/dreadnode/AIRTBench-Code)): Evaluates attack discovery, code execution, and exploitation-chain loops in autonomous AI red-teaming scenarios. Core idea: place black-box CTF-style AI/ML security challenges into runnable tasks and check whether agents can write scripts, call tools, and verify compromise.
- [Patch-to-PoC](https://arxiv.org/abs/2602.07287): Evaluates agents' ability to reproduce N-day PoCs from Linux kernel patches. Core idea: combine patch analysis, kernel builds, debugging, and exploit verification to check whether agents can convert fixed vulnerabilities back into executable attack evidence.
- [ExploitGym](https://arxiv.org/abs/2605.11086): Evaluates whether AI agents can turn security vulnerabilities into real attacks. Core idea: measure end-to-end capability in reconnaissance, exploit construction, failure debugging, and achieving attack objectives using real vulnerabilities, executable environments, and exploit-result verification.
- [ExploitBench](https://arxiv.org/abs/2605.14153) ([project page](https://exploitbench.ai/); [code](https://github.com/exploitbench/exploitbench)): Evaluates a hierarchical capability ladder for cybersecurity agents. Core idea: use tasks ranging from basic reconnaissance to complex exploit-chain organization to distinguish "can use tools" from "can complete a real exploit chain."
- [AuthBench](https://arxiv.org/abs/2605.14859): Evaluates whether terminal/code agents can infer minimally sufficient file-level permission boundaries for tasks. Core idea: combine task-usability verification and attack-result verification to test how coding agents trade off read/write/execute permissions, sensitive-file exposure, and least-privilege authorization.
- [MOSAIC-Bench](https://arxiv.org/abs/2605.03952): Evaluates compositional vulnerability induction in coding agents. Core idea: give multi-stage, benign-looking tickets on deployed software substrates and use deterministic exploit oracles to check whether agents introduce exploitable vulnerabilities.
- [CyBiasBench](https://arxiv.org/abs/2605.07830): Evaluates behavioral bias in cyber-attack agents. Core idea: measure whether agents systematically over-select or under-select attack families across offensive scenarios, complementing exploit-success benchmarks with behavior diagnostics.
- OpenAI cyber risk evaluations (reported in the [GPT-5.5 system card](https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf)): closed or model-card-only evaluations including Capture the Flag (Professional), Cyber Range, VulnLMP, Irregular's atomic challenge suite, and CyScenarioBench. Core idea: track vendor emphasis on end-to-end cyber operations, vulnerability research, exploit construction, and long-horizon offensive cybersecurity tasks even when exact challenge sets are not public.

## 2.10.3 Agent Harness

- CyberGym's execution stack, SEC-bench's vulnerable-repository harnesses, and ExploitBench's staged task environments are the most relevant benchmark-side harness references here. The reusable harness pattern is `reconnaissance -> hypothesis -> exploit or patch attempt -> verifier-owned evidence -> retry`, with strict sandboxing and audit logs.
- [Co-RedTeam](https://arxiv.org/abs/2602.02164): A coordinated security discovery and exploitation harness. Core idea: combine discovery, exploitation, execution feedback, validation, and memory reuse across cooperating red-team agents.

## 2.10.4 Skill

- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) is suitable for isolating high-risk cyber or exploit-like tool calls.
- [docker-local-dev](https://skills.sh/thienanblog/awesome-ai-agent-skills/docker-local-dev) is suitable for packaging vulnerable services, reproduction environments, and resettable validators.
