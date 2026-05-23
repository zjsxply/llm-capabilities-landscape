# 4.4 Autonomous Driving

> Parent chapter: 4. Multimodal

Note: This page collects autonomous-driving, traffic-scenario, vehicle-cockpit, in-vehicle assistant, and driving-video world-model evaluations. General robot manipulation and navigation remain in [2.11 Embodied and VLA Agents](02-11-embodied-vla.md).

## 4.4.1 Bench

- [Capability-Driven Scenario Understanding Evaluation](https://arxiv.org/abs/2503.11400): Evaluates multimodal large language models on autonomous-driving scenario understanding. Core idea: organize driving-scene comprehension by capabilities so failures in perception, context reasoning, and decision-relevant understanding can be separated.
- [Drive4C](https://doi.org/10.1109/CVPRW67362.2025.00371): A closed-loop benchmark for language-guided autonomous driving, aimed at testing which foundation-model capabilities matter when instructions must translate into driving behavior.
- [STSBench](https://arxiv.org/abs/2506.06218): Evaluates spatio-temporal scenario understanding for multimodal large language models in autonomous driving. Core idea: test whether models reason over dynamic driving scenes and temporal relations rather than only classify static road images.
- [AD^2-Bench](https://arxiv.org/abs/2506.09557): Evaluates multimodal large language models for autonomous driving under adverse conditions. Core idea: use hierarchical chain-of-thought style tasks to test whether models can reason about degraded driving scenes rather than only handle clean visual inputs.
- [Bench2ADVLM](https://arxiv.org/abs/2508.02028): A closed-loop benchmark for vision-language models in autonomous driving. Core idea: evaluate driving-relevant perception, reasoning, and decision behavior in a loop rather than only scoring static scene understanding.
- [ODVBench](https://arxiv.org/abs/2509.24871): Evaluates online video understanding in autonomous-driving scenarios as part of the StreamForest work. Core idea: test generalization under driving videos where temporal state, scene changes, and persistent event memory matter.
- [Evaluating Video Models as Simulators of Multi-Person Pedestrian Trajectories](https://arxiv.org/abs/2510.20182): Evaluates whether video models can simulate multi-person pedestrian trajectories. Core idea: test social-motion and trajectory consistency so video generation is judged as a usable simulator rather than only by visual plausibility.
- [VehicleWorld](https://aclanthology.org/2025.findings-emnlp.23/): What it evaluates: API agents for intelligent vehicle-cockpit interaction. Core idea: provide executable vehicle modules, APIs, properties, and real-time state so agents must build environment awareness and recover from tool-call errors across tightly coupled subsystems.
- [AIGV-Bench](https://arxiv.org/abs/2512.06376): Evaluates whether AI-generated driving videos are usable for autonomous-driving training and evaluation. Core idea: diagnose artifacts, implausible motion, and traffic-semantic violations, then measure their downstream impact on perception tasks.
- [DrivingGen](https://arxiv.org/abs/2601.01528): Evaluates generative video world models for autonomous driving. Core idea: use driving-specific scene dynamics and controllability requirements to test whether generated futures are useful for embodied planning rather than only visually plausible.
- [AutoDriDM](https://arxiv.org/abs/2601.14702): An explainable benchmark for VLM decision-making in autonomous driving. Core idea: evaluate whether vision-language models produce grounded, interpretable driving decisions rather than only perception labels.
- [AgentDrive](https://arxiv.org/abs/2601.16964): Evaluates agentic reasoning in autonomous systems with LLM-generated driving scenarios. Core idea: use open scenario data to test whether agents can reason about autonomous-system situations rather than only classify static driving scenes.
- [ScenePilot-4K](https://arxiv.org/abs/2601.19582): evaluates vision-language models in first-person autonomous-driving scenes. Core idea: use large-scale egocentric driving data and benchmark tasks to test whether models understand driving-relevant scene evidence from the vehicle viewpoint.
- [VehicleMemBench](https://arxiv.org/abs/2603.23840): What it evaluates: long-term multi-user memory in in-vehicle agents. Core idea: make memory affect executable tool-state outcomes in a simulated vehicle assistant, exposing preference conflict and user-specific recall failures.

## 4.4.2 Agent Harness

- [Drive Like A Human](https://arxiv.org/abs/2307.07162) ([open-source code](https://github.com/PJLab-ADG/DriveLikeAHuman)): An early closed-loop LLM driving harness in HighwayEnv, useful as a precursor for later memory/reflection-based autonomous-driving agents.
- [DiLu](https://arxiv.org/abs/2309.16292) ([open-source code](https://github.com/PJLab-ADG/DiLu)): A closed-loop self-evolving driving framework with environment, reasoning, reflection, and memory modules, making driving decisions through an explicit agent loop rather than a single perception model.
- [Agent-Driver](https://arxiv.org/abs/2311.10813) ([open-source code](https://github.com/physical-superintelligence-lab/Agent-Driver); [project page](https://usc-gvl.github.io/Agent-Driver/)): An LLM cognitive agent for autonomous driving with function-call tools, cognitive memory, reasoning, task planning, motion planning, and self-reflection.
- [AGENTS-LLM](https://arxiv.org/abs/2507.13729): An agentic LLM framework for generating challenging traffic scenarios. Core idea: use LLM-driven scenario augmentation to stress autonomous-driving agents with harder, more diverse traffic situations than fixed scenario libraries provide.

## 4.4.3 Skill

- [RoboSafe-Lab AD Safety Research Skills](https://github.com/RoboSafe-Lab/ad-safety-research-skills) provides Claude Code skills for autonomous-driving safety research, including AD foundation models, scenario analysis, experiment design, and generative-model workflows; these are agent-readable research skills rather than learned driving policy primitives.
