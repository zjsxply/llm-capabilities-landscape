# 0.1 What Is a Harness

> Parent chapter: 0. Harness and Skill Creator


- A `Harness` is a task runtime outside the model.
  It usually handles `task decomposition`, `tool wiring`, `context organization`, `environment execution`, `search/backtracking`, and `verification and recovery`, so the same base model can often be reused across multiple benchmarks.
- A `Harness` is not a training algorithm.
  Training answers "what the model has learned"; a harness answers "how the system turns capability into a stable executable workflow."
- To avoid mixing "training" and "harness", start with a three-way split when reading papers:
  `model training algorithms` (gains mainly come from parameter updates or training data/objectives), `external harnesses` (gains mainly come from task decomposition, control flow, context/memory, tool and environment interfaces, search and verification loops), and `hybrid work` (both are present).
- When reading an agent paper, first identify where the gain comes from.
  If it mainly comes from `SFT / RL / data scaling / pretraining`, it is model work; if it mainly comes from `planner-executor`, `tool loop`, `memory`, `validator`, `DAG/FSM`, or `skill library`, it is closer to harness work.
