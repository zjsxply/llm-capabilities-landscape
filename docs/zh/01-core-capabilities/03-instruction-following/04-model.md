# 1.3.4 Model

- [FLAN](https://arxiv.org/abs/2109.01652)：奠基性的指令调优方法，在大量自然语言任务指令上微调语言模型，以提升零样本泛化。
- [InstructGPT](https://arxiv.org/abs/2203.02155)：定义指令遵循 RLHF 路线的代表性工作，结合监督示范、人类偏好奖励建模和策略优化。
- [Self-Instruct](https://arxiv.org/abs/2212.10560)：合成指令数据生成方法，由语言模型自举生成指令，经过过滤后微调以增强指令遵循。
- [DPO](https://arxiv.org/abs/2305.18290)：偏好优化算法，直接从偏好对对齐指令遵循模型，而不单独训练显式奖励模型。
- [Tulu 3](https://arxiv.org/abs/2411.15124)：开放后训练路线，结合高质量指令数据、偏好学习、类 RL 优化和评测驱动迭代。
- [Measuring Data Diversity for Instruction Tuning: A Systematic Analysis and A Reliable Metric](https://arxiv.org/abs/2502.17184)：定义指令微调数据多样性指标，并分析多样性如何改变指令遵循表现。
- [HelpSteer3](https://arxiv.org/abs/2503.04378)：提供人类反馈与编辑数据，用于提升开放式指令行为和推理时扩展效果。
- [D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning](https://arxiv.org/abs/2503.11441)：按多样性、难度和可靠性选择指令微调数据，以提升样本高效的指令遵循。
- [Adaptive Length-Bias Mitigation](https://aclanthology.org/2025.findings-naacl.169/)：缓解 RLHF 奖励模型中过长和过短回答偏好的长度偏置。
- [Generative RLHF-V](https://arxiv.org/abs/2505.18531)：从多模态人类偏好中学习对齐原则，而不只优化成对偏好分数。
- [RAIN-Merging](https://arxiv.org/abs/2602.22538)：面向大型推理模型指令合规性的 gradient-free model merging 方法，同时保留 reasoning format。
