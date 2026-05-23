# 1.13.1 Leaderboard

- [SkillsBench Leaderboard](https://www.skillsbench.ai/leaderboard): The most direct continuously updated leaderboard for skill use.
  It compares agents under conditions such as `no skill / curated skill / self-generated skill`, making it useful for judging whether skills truly improve task success rather than only comparing base model capability.
- [PinchBench](https://pinchbench.com/about): A real-task leaderboard and evaluation entry point in the OpenClaw ecosystem.
  It is not a pure skill benchmark, but its tasks include ClawHub skill installation, skill search, and skill-use scenarios, so it is a useful practical supplement for productized skill ecosystems.
- [Claw-Eval-Live](https://claw-eval-live.github.io/): A continuously updated workflow-agent leaderboard that explicitly uses ClawHub skill signals to construct tasks.
  It is better suited for observing whether agents can discover, install, call, and verify skills in dynamic workflows, rather than only comparing pass rates under ideal given-skill settings.
