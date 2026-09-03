# 1.10.1 Leaderboard

- [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://doi.org/10.18653/v1/2025.naacl-long.439)：为long-context, memory compression, or context extension提供公开比较入口。
- [L-Eval Leaderboard](https://l-eval.github.io/)（[开源代码](https://github.com/OpenLMLab/LEval)）：L-Eval 官方榜覆盖 Exact Match、GPT-4、GPT-3.5、F1 和 ROUGE 等评测器，面向 3K 到 200K token 的长上下文任务。
- [LV-Eval Leaderboard](https://github.com/infinigence/LVEval#leaderboard)（[数据集](https://huggingface.co/datasets/Infinigence/LVEval)）：LV-Eval 官方仓库榜按 16K 到 256K words 五个长度层级比较模型，覆盖中英双语 single-hop 与 multi-hop QA。
- [LongBench Leaderboard](https://longbench2.github.io/)（[开源代码](https://github.com/THUDM/LongBench)）：从 LongBench 到 LongBench v2 的公开榜，覆盖多文档问答、长程推理、摘要与 RAG/no-context/CoT 等可控设置，是文本长上下文最常用的持续对照入口之一。
- [RULER Results](https://github.com/NVIDIA/RULER)（[论文](https://arxiv.org/abs/2404.06654)）：RULER 官方仓库按声明上下文长度、有效上下文长度，以及 4K 到 128K 序列长度得分发布模型结果，是常用的实际可用上下文窗口诊断入口。
- [HELMET Leaderboard](https://princeton-nlp.github.io/HELMET/)（[开源代码](https://github.com/princeton-nlp/HELMET)）：按检索、RAG、重排序、推理、学习等维度组织长上下文榜单，适合避免只用 needle 类任务代表长上下文能力。
- [MileBench Leaderboard](https://milebench.github.io/)（[开源代码](https://github.com/milebench/MileBench)）：多模态长上下文榜，适合追踪视频、图像序列和跨模态长输入下的模型差异。
- [AcademicEval](https://github.com/ulab-uiuc/AcademicEval)：面向 live long-context generation 的榜单与评测脚本，使用新 arXiv 论文构造任务，适合评估模型在长论文语境下生成标题、摘要和相关工作的能力。
