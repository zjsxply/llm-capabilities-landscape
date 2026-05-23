# 1.16 其它

> 上级章节：1. 基础能力

说明：本页收纳主轴较交叉、偏 meta-evaluation，或暂时还不足以单独形成一个稳定类别的 benchmark。后续如果同类工作积累到足够密度，应再移入更具体的页面。

## 1.16.1 Bench

- [OmniBench](https://arxiv.org/abs/2409.15272)（[开源代码](https://github.com/multimodal-art-projection/OmniBench)，[数据集](https://huggingface.co/datasets/m-a-p/OmniBench)）：评什么：omni-language models 的视觉、听觉和文本三模态理解。核心思想：检查模型能否同时识别、解释并推理多种模态，而不是把多模态评测局限为图文任务。
- [STEER-ME](https://arxiv.org/abs/2502.13119)（数据集：[narunraman/steer_me](https://huggingface.co/datasets/narunraman/steer_me)）：评什么：LLM 的微观经济推理。核心思想：用非战略性经济决策设定诊断模型是否能推理激励、偏好和权衡，而不是只回答经济领域事实。
- [ThinkBench](https://arxiv.org/abs/2502.16268)（[开源代码](https://github.com/huangshulin123/ThinkBench)，[数据集](https://huggingface.co/datasets/jiuyinjiu/ThinkBench)）：评什么：动态分布外生成条件下的稳健 LLM 推理。核心思想：生成并评测新鲜 OOD 推理样本，降低答案泄漏和 benchmark 过拟合风险，并用同一协议比较 reasoning 与 non-reasoning 模型。
- [AbsenceBench](https://arxiv.org/abs/2506.11440)（[开源代码](https://github.com/harvey-fin/absence-bench)，[数据集](https://huggingface.co/datasets/harveyfin/AbsenceBench)）：评什么：在长输入中发现被刻意删掉的信息。核心思想：用序列、诗歌和 GitHub pull request 中的“缺失项识别”补充 needle retrieval，暴露模型能找出现有事实但看不见遗漏的失败。
- [CorrectBench](https://arxiv.org/abs/2510.16062)（[项目页](https://correctbench.github.io/)，[数据集](https://huggingface.co/datasets/zeli2024/CorrectBench)）：评什么：LLM 推理的自我修正策略。核心思想：在多类推理任务上比较内在、外部和微调式修正设置，区分真正错误修复与重复错误或过度自信的错答。
- [Infinity-Chat](https://arxiv.org/abs/2510.22954)（[开源代码](https://github.com/liweijiang/artificial-hiveminds)，[数据集](https://huggingface.co/datasets/liweijiang/infinite-chats-taxonomy)）：评什么：开放式语言模型输出的多样性与同质化。核心思想：用包含大量合理答案空间的真实用户问题，衡量模型多次生成是否坍缩成相似的“蜂巢式”回答，而不是保持类似人类的表达差异。
