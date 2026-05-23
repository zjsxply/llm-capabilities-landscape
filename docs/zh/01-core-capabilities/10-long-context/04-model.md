# 1.10.4 Model

- [Position Interpolation](https://arxiv.org/abs/2306.15595)：通过插值位置索引扩展 RoPE 系 LLM 上下文窗口，并只需要有限额外训练。
- [LongLoRA](https://arxiv.org/abs/2309.12307)：参数高效长上下文微调路线，训练时使用稀疏局部注意力，推理时保留密集注意力。
- [LongAlign](https://arxiv.org/abs/2401.18058)：长上下文对齐路线，结合长指令数据、高效 packing 和训练策略，同时保持短上下文能力。
- [LongRoPE](https://arxiv.org/abs/2402.13753)：通过非均匀位置插值、渐进式扩展和短上下文再校准扩展 RoPE 系 LLM。
- [LongRecipe](https://arxiv.org/abs/2409.00509)：高效长上下文泛化训练 recipe，结合模拟长序列输入、位置索引变换和训练优化。
- [QwenLong-L1](https://arxiv.org/abs/2505.17667)：用强化学习训练长上下文大推理模型，目标是文档级推理而非普通检索式使用。
- [EMLoC](https://arxiv.org/abs/2505.19812)：选择并压缩关键信息层，在无需重新训练的情况下支持高效多模态长上下文适配。
- [MesaNet](https://arxiv.org/abs/2506.05233)：提出基于局部最优测试时训练的循环序列建模层，在有界内存权衡下提升长上下文语言建模。
- [Lag-Relative Sparse Attention In Long Context Training](https://arxiv.org/abs/2506.11498)：用滞后相对稀疏注意力训练长上下文模型，在扩展上下文的同时保持注意力结构。
- [Modular Techniques for Synthetic Long-Context Data Generation in Language Model Training and Evaluation](https://arxiv.org/abs/2509.01185)：构建用于训练和评估的合成长上下文数据，覆盖长程依赖能力。
- [Breadcrumbs Reasoning: Memory-Efficient Reasoning with Compression Beacons](https://arxiv.org/abs/2510.13797)：用压缩信标支持长上下文上的内存高效推理，使压缩轨迹仍与推理绑定。
- [LoongRL](https://arxiv.org/abs/2510.19363)：用 KeyChain 合成与 RL 训练长上下文中的 plan-retrieve-reason-recheck 行为。
- [End-to-End Test-Time Training for Long Context](https://arxiv.org/abs/2512.23675)：在长上下文推理期间进行端到端测试时训练，使模型按实例适配。
- [DySCO](https://arxiv.org/abs/2602.22175)：无需训练的动态注意力缩放解码方法，在生成时强化任务相关长上下文 token。
