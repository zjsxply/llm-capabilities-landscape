# 4.1.4 Agent Harness

- [ComfyBench / ComfyAgent](https://arxiv.org/abs/2409.01392)（[开源代码](https://github.com/xxyQwQ/ComfyBench)；[项目页](https://xxyqwq.github.io/ComfyBench)）：ComfyUI workflow 生成与评测 harness，LLM agent 学习文档、生成可执行 workflow、运行并用 pass/resolve 式指标评分。
- [ComfyGPT](https://arxiv.org/abs/2503.17671)（[开源代码](https://github.com/comfygpt/comfygpt)；[项目页](https://comfygpt.github.io/)）：面向 ComfyUI workflow 生成的自优化多 agent 系统，包含 flow generation、refinement 和 execution agents。
- [CIGEval](https://arxiv.org/abs/2504.07046)：面向条件图像生成的 agentic evaluation harness。核心思想是让 LMM 选择工具并围绕多类条件生成任务做细粒度判断，使图像生成评测成为工具介入的工作流，而不是单一标量指标。
- [ComfyMind](https://arxiv.org/abs/2505.17908)（[开源代码](https://github.com/EnVision-Research/ComfyMind)）：基于 ComfyUI 的通用生成规划与反馈框架。核心思路是使用树形工作流规划和执行反馈，把复杂多模态生成任务分解、执行并修复，而不是只依赖一次性提示。
- [ComfyUI-Copilot](https://arxiv.org/abs/2506.05010)（[开源代码](https://github.com/AIDC-AI/ComfyUI-Copilot)）：ComfyUI workflow 生命周期助手，覆盖生成、调试、重写、参数调优和 ComfyUI 生态内的 agentic workflow 操作；其公开仓库目前说明官方 API 服务已暂停，因此实际部署需要用户自备 LLM API key 与 base URL。
- [Maestro](https://arxiv.org/abs/2509.10704)：面向自我改进文生图的智能体编排框架。核心思路：协调生成、批评和修订智能体，让图像输出通过显式流程改进，而不是依赖单次模型调用。
- [PromptSculptor](https://arxiv.org/abs/2509.12446)：面向文生图提示词优化的多 agent harness。核心思想：把提示词分析、改写和质量反馈拆给协作 agent，在基础生成模型之外迭代提升图像生成提示。
- [OmniVerifier](https://arxiv.org/abs/2510.13804)（[开源代码](https://github.com/Cominclip/OmniVerifier)）：面向视觉结果验证的生成式 verifier；可把“视觉判断”改造成显式验证与自我修正闭环，并在 ViVerBench 等上对比评测。
- [ComfySearch](https://arxiv.org/abs/2601.04060)：用于 ComfyUI 工作流的自主探索 harness。核心思路是在严格工作流约束下搜索组件图，并用验证引导构建过程，使 Agent 能生成可执行且质量更高的 ComfyUI pipeline。
- [coDrawAgents](https://arxiv.org/abs/2603.12829)：面向组合式图像生成的多智能体对话 harness。核心思想：拆分 interpreter、planner、checker 与 painter 等角色，在生成前迭代地约束复杂对象布局和属性。
- [EditRefiner](https://arxiv.org/abs/2605.07457)：面向图像编辑优化的人类对齐智能体框架。核心思路是将图像编辑封装为迭代优化流程，由基础生成器之外的反馈、对齐检查和修订环节推动改进。
