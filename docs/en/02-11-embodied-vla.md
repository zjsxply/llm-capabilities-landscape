# 2.11 Embodied and VLA Agents

> Parent section: 2. Foundation Agents

Note: This category covers embodied agents and vision-language-action settings where the model must connect perception, language, planning, and actions in an interactive physical, simulated, game, or robot environment. GUI-only computer use stays in [2.5 Computer Use](02-05-computer-use-gui.md), while passive spatial or video understanding stays in the corresponding core-capability pages.

## 2.11.1 Leaderboard

- [VideoGameBench Leaderboard](https://vgbench.com/#leaderboard): A continuous leaderboard for embodied agent perception, navigation, manipulation, and planning in video-game environments; useful for tracking models and scaffolds that operate in executable visual worlds rather than static screenshots.

## 2.11.2 Bench

- [CALVIN](https://arxiv.org/abs/2112.03227): Evaluates language-conditioned long-horizon robot manipulation. Core idea: use a simulated tabletop environment and language instructions to test whether agents can compose manipulation skills over extended horizons.
- [MineDojo](https://arxiv.org/abs/2206.08853): Evaluates open-ended embodied agents in Minecraft with internet-scale knowledge resources. Core idea: use a rich, long-horizon sandbox environment to test exploration, tool use, crafting, navigation, and task completion under language goals.
- [VIMA-Bench](https://arxiv.org/abs/2210.03094): Evaluates general robot manipulation with multimodal prompts. Core idea: specify manipulation tasks through combinations of text, images, and object references, making the benchmark closer to vision-language-action grounding than pure language-conditioned control.
- [LIBERO](https://arxiv.org/abs/2306.03310): Evaluates knowledge transfer for lifelong robot learning. Core idea: organize robot-manipulation tasks into suites that test whether agents reuse skills and adapt across objects, layouts, and task families.
- [VideoGameBench](https://vgbench.com/#leaderboard): Evaluates embodied perception, navigation, manipulation, and planning in video-game environments. Core idea: place spatial understanding in actionable game worlds and use task completion plus trajectory quality to evaluate whether agents can translate visual-spatial relations into actions.
- [Spatial-Gym](https://arxiv.org/abs/2604.09338): Evaluates whether agents can turn spatial reasoning into sequential action. Core idea: use a Gymnasium-style interactive benchmark with pathfinding, backtracking, and action-level scoring rather than passive spatial QA.
- [Minedojo-Verified](https://github.com/ByteDance-Seed/Seed2.0): A verified embodied-agent visual task subset reported in the Seed2.0 model card; no standalone public release of this verified subset has been confirmed. Core idea: track whether frontier multimodal agents can ground perception, planning, and action in an interactive environment beyond static screenshots.

## 2.11.3 Agent Harness

- MineDojo, CALVIN, VIMA, and LIBERO are benchmark-side harnesses as much as datasets: they define environments, observations, action spaces, task resets, and success checks. The reusable design pattern is `observe multimodal state -> parse language goal -> plan/subgoal -> act -> verify environment state -> recover`.

## 2.11.4 Skill

- [computer-vision-opencv](https://skills.sh/mindrally/skills/computer-vision-opencv) is useful for perception-side preprocessing and visual diagnostics in simulated embodied environments.
- [setup-sandbox](https://skills.sh/recoupable/setup-sandbox) is useful when embodied or game environments require isolated runtime setup.
