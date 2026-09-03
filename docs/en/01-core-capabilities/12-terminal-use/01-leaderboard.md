# 1.12.1 Leaderboard

- [Terminal-Bench 2.0 official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0) and [Terminal-Bench 2.1 official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.1): The most important continuous terminal-agent leaderboard family today; the 2.1 page is the newer official release while 2.0 remains useful for historical comparisons.
  The leaderboard supports submissions from both new models and custom agents, and requires that timeouts or resource limits not be modified, making it suitable for comparing real terminal execution, context compression, completion checks, retry, and verification strategies in agent harnesses.
- [Claw-Eval-Live](https://claw-eval-live.github.io/): A continuous workflow-agent leaderboard with tasks spanning terminal, services, files, and the tool ecosystem.
  Its value is in using fixed fixtures, audit logs, service state, and artifact verification to track long-term agent performance in real workflows, making it a dynamic terminal-adjacent leaderboard beyond Terminal-Bench.
- [DevOps-Gym](https://www.devops-gym.com/): A terminal-adjacent leaderboard/evaluation entry point more focused on DevOps and system operations.
  It is suitable for observing command-line capability in deployment, configuration, monitoring, and failure recovery, complementing Terminal-Bench's single-task Linux environment.
- [LinuxArena](https://www.linuxarena.ai/): An official arena/results page for agents in live, multi-service Linux production environments.
  It complements terminal task-completion leaderboards by pairing legitimate systems work with side tasks, so it is useful for tracking both command-line competence and control failures.
- [SREGym Leaderboard](https://sregym.com/leaderboard): An official leaderboard for AI SRE agents in high-fidelity production-incident scenarios.
  It is especially relevant for terminal use because agents must diagnose, inspect logs and metrics, edit configuration, and repair cloud-native services through command-line workflows.
