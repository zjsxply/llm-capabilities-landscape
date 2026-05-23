# 1.10.4 Model

- [Position Interpolation](https://arxiv.org/abs/2306.15595): Extends RoPE-based LLM context windows by interpolating positional indices with limited additional training.
- [LongLoRA](https://arxiv.org/abs/2309.12307): A parameter-efficient long-context fine-tuning recipe using sparse local attention during training and dense attention at inference.
- [LongAlign](https://arxiv.org/abs/2401.18058): A long-context alignment recipe that combines long instruction data, efficient packing, and training strategies while preserving short-context ability.
- [LongRoPE](https://arxiv.org/abs/2402.13753): Extends RoPE-based LLMs through non-uniform positional interpolation, progressive extension, and short-context readjustment.
- [LongRecipe](https://arxiv.org/abs/2409.00509): An efficient long-context generalization recipe using simulated long-sequence inputs, position-index transformation, and training optimizations.
- [QwenLong-L1](https://arxiv.org/abs/2505.17667): Trains long-context large reasoning models with reinforcement learning for document-level reasoning beyond retrieval-style use.
- [EMLoC](https://arxiv.org/abs/2505.19812): Selects and compresses informative layers to support efficient multimodal long-context adaptation without retraining.
- [MesaNet](https://arxiv.org/abs/2506.05233): Introduces a recurrent sequence-modeling layer based on locally optimal test-time training, improving long-context language modeling with bounded memory trade-offs.
- [Lag-Relative Sparse Attention In Long Context Training](https://arxiv.org/abs/2506.11498): Trains long-context models with lag-relative sparse attention to extend context while keeping attention structured.
- [Modular Techniques for Synthetic Long-Context Data Generation in Language Model Training and Evaluation](https://arxiv.org/abs/2509.01185): Builds synthetic long-context data for training and evaluation, targeting long-range dependency coverage.
- [Breadcrumbs Reasoning: Memory-Efficient Reasoning with Compression Beacons](https://arxiv.org/abs/2510.13797): Uses compression beacons for memory-efficient reasoning over long contexts, keeping compressed traces tied to reasoning.
- [LoongRL](https://arxiv.org/abs/2510.19363): Uses KeyChain synthesis and RL to train plan-retrieve-reason-recheck behavior over long contexts.
- [End-to-End Test-Time Training for Long Context](https://arxiv.org/abs/2512.23675): Applies end-to-end test-time training to adapt models during long-context inference.
- [DySCO](https://arxiv.org/abs/2602.22175): A training-free dynamic attention-scaling decoding method that upweights task-relevant long-context tokens during generation.
