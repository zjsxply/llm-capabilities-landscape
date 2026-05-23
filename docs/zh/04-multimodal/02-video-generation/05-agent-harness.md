# 4.2.5 Agent Harness

- [FilmAgent](https://arxiv.org/abs/2501.12909)：面向虚拟 3D 空间的多智能体电影自动化框架。核心思路：把电影创作拆成多个协作角色和可执行的场景生产步骤，而不是把视频生成简化为单次提示词调用。
- [MM-StoryAgent](https://arxiv.org/abs/2503.05242)（[开源代码](https://github.com/X-PLUG/MM_StoryAgent)）：面向有声故事书视频生成的多智能体 harness。核心思路是协调写作、视觉生成、旁白、音效和音乐模块，使故事能够跨文本、图像与音频工具完成规划和渲染，而不是依赖单一模型一次性生成。
- [MovieAgent](https://arxiv.org/abs/2503.07314)：一个用于自动化长视频生成的多智能体规划框架。核心思路是让导演、编剧、分镜师和场景管理等 LLM 智能体分工协作，将脚本拆解为场景、镜头、机位、字幕、音频和角色一致的生成步骤。
- [V-Stylist](https://arxiv.org/abs/2503.12077)：一个多智能体视频风格化框架。核心思路是协调视频解析、风格模型搜索和反思修正，使 MLLM 智能体能够分解多镜头视频并迭代改进风格化结果。
- [AniMaker](https://arxiv.org/abs/2506.10540)：一个面向动画叙事的多智能体 harness。核心思想：结合角色化故事规划与 MCTS 驱动的片段生成，使长动画能在多个 agent 间拆解、搜索和修订。
- [AniME](https://arxiv.org/abs/2508.18781)：一个面向长动画生成的多智能体规划 harness。核心思想：自适应协调规划角色，使长动画在生成片段之间保持情节、角色和场景一致性。
- [EditDuet](https://arxiv.org/abs/2509.10761)：面向非线性视频编辑的多智能体 harness。核心思想是把编辑拆给使用视频编辑工具的 Editor agent 和给出反馈或确认渲染的 Critic agent，使指令驱动视频编辑成为迭代式工具工作流。
- [MagicWand](https://arxiv.org/abs/2511.18352)：面向图像和视频 AIGC 的用户偏好对齐生成与评估智能体。核心思路是在提示增强、生成、评估和迭代修正中持续引入偏好描述，并用 UniPreferBench 评估偏好对齐。
- [AutoMV](https://arxiv.org/abs/2512.12196)：围绕歌曲结构、节拍、歌词和音乐属性协调多个 Agent，规划并生成时间一致的完整 MV。
- [The Script is All You Need](https://arxiv.org/abs/2601.17737)：面向长程对话到电影化视频生成的智能体框架，将脚本作为多阶段视频创作的规划载体。
- [SAGE: Scalable Agentic 3D Scene Generation](https://arxiv.org/abs/2602.10116)：为具身 agent 评测提供可扩展 3D 场景生成。核心思想：合成带行动约束的场景，使机器人或模拟 agent 能在多样可行动环境中测试，而不是依赖少量固定地图。
- [SPIRAL](https://arxiv.org/abs/2603.08403)：面向长程动作条件视频生成的反思式规划 harness。核心思想：由 PlanAgent 分解目标，结合记忆上下文逐段生成视频，再由 CriticAgent 反思并修复跨时间的动作执行。
- [Mind-of-Director](https://arxiv.org/abs/2603.14790)：多模态智能体驱动的影片预演框架，通过协作决策组织生成前的电影化规划。
- [CutClaw](https://arxiv.org/abs/2603.29664)（[开源代码](https://github.com/GVCLab/CutClaw)）：通过音乐同步进行小时级视频剪辑的 agentic harness。核心思想：围绕音频结构协调长程剪辑决策，使视频剪辑智能体能处理更长时间线。
- [DIRECT](https://arxiv.org/abs/2604.04875)：采用层级式多智能体规划与意图引导编辑的视频混剪生成框架，适合作为视频组合创作中的智能体编排案例。
- [Camera Artist](https://arxiv.org/abs/2604.09195)：面向电影化语言叙事视频生成的多智能体框架，关注叙事、镜头与拍摄决策的协同。
