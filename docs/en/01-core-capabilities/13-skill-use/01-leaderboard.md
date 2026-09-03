# 1.13.1 Leaderboard

- [SkillsBench Leaderboard](https://www.skillsbench.ai/leaderboard): The most direct continuously updated leaderboard for skill use.
  It compares agents under conditions such as `no skill / curated skill / self-generated skill`, making it useful for judging whether skills truly improve task success rather than only comparing base model capability.
- [PinchBench](https://pinchbench.com/about): A real-task leaderboard and evaluation entry point in the OpenClaw ecosystem.
  It is not a pure skill benchmark, but its tasks include ClawHub skill installation, skill search, and skill-use scenarios, so it is a useful practical supplement for productized skill ecosystems.
- [Letta Context-Bench Skills Suite](https://leaderboard.letta.com/): A public leaderboard that includes skill-suite evaluations for agentic context management.
  It is broader than skill use alone, but the skills slice is useful for comparing whether agents can select and apply context packages in task settings rather than only consume a pre-attached skill file.
- [SkillTester](https://skilltester.ai/): An official skill utility and security ranking surface.
  It is useful as a supplemental leaderboard because it evaluates whether skills improve execution while also exposing security risks from reusable skill artifacts.
- [SkillSafetyBench](https://jinchang1223.github.io/skill-safety-bench-website/): An official project and leaderboard/results page for skill-facing attack-surface evaluation.
  It complements utility-focused skill benchmarks by measuring whether third-party skills, local materials, or local artifacts can induce unsafe agent behavior.
- [Claw-Eval-Live](https://claw-eval-live.github.io/): A continuously updated workflow-agent leaderboard that explicitly uses ClawHub skill signals to construct tasks.
  It is better suited for observing whether agents can discover, install, call, and verify skills in dynamic workflows, rather than only comparing pass rates under ideal given-skill settings.
