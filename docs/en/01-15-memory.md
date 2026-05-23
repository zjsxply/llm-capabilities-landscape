# 1.15 Memory

> Parent section: 1. Foundational Capabilities

Note: The boundary between this section and [1.10 Long Context](01-10-long-context.md) is whether state persists across interactions.
Long context mainly evaluates whether a model can read, locate, compress, and synthesize long inputs within a single prompt or task window.
Memory evaluates whether an agent can write facts, preferences, experiences, procedural knowledge, and failure trajectories into external or internal memory, then correctly retrieve, update, merge, and forget them across later turns, sessions, tasks, or environment changes.

## 1.15.1 Leaderboard

- [LOCOMO](https://github.com/snap-research/locomo): An entry point for long-term dialogue memory evaluation, suitable for tracking recall of facts, preferences, and events across multiple sessions.
- [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench): Public code and evaluation entry point for incremental interactive agent memory, useful for comparing external memory modules, summary memory, and full-context strategies.
- [MemGUI-Bench](https://github.com/lgy0404/MemGUI-Bench): An entry point for mobile GUI agent memory evaluation, useful for observing retention and cross-session learning in GUI tasks across sessions.
- [EvoMemBench](https://github.com/DSAIL-Memory/EvoMemBench): An entry point for self-evolving memory evaluation, useful for comparing in-episode/cross-episode and knowledge/execution memory.

## 1.15.2 Bench

- [LOCOMO](https://arxiv.org/abs/2402.17753) ([code](https://github.com/snap-research/locomo)): What it evaluates: very long-term dialogue memory. Core idea: treat facts, preferences, and events in multi-session dialogue as retrieval targets, evaluating whether agents can use historical information consistently over long periods.
- [LongMemEval](https://arxiv.org/abs/2410.10813): What it evaluates: memory question answering in long dialogue and personal assistant scenarios. Core idea: split long histories into local facts, global preferences, and cross-time reasoning questions to test whether models or memory systems can locate and combine relevant memories from lengthy interactions.
- [MemBench](https://arxiv.org/abs/2506.21605) ([code](https://github.com/import-myself/Membench)): What it evaluates: episodic, semantic, and procedural memory in LLM-based agents. Core idea: separately model "participatory memory" and "observational memory", and introduce large-scale noisy conversations to test long-term memory retrieval.
- [MemoryAgentBench](https://arxiv.org/abs/2507.05257) ([code](https://github.com/HUST-AI-HYZ/MemoryAgentBench)): What it evaluates: memory writing, updating, and recall in multi-turn incremental interaction. Core idea: do not put all history into the prompt at once; instead, provide information gradually as an interaction stream and test whether the memory module can evolve with state.
- [MemGUI-Bench](https://arxiv.org/abs/2602.06075) ([code](https://github.com/lgy0404/MemGUI-Bench)): What it evaluates: memory capability of mobile GUI agents. Core idea: use cross-session, cross-app, and dynamic-environment tasks to specifically test memory retention and cross-session learning, connecting memory capability with GUI action reliability.
- [MemoryArena](https://arxiv.org/abs/2602.16313): What it evaluates: agent memory in multi-session, interdependent tasks. Core idea: bind cross-session dependencies and mutually interfering facts to later actions, evaluating whether agents can maintain usable memory reliably over long-term interaction.
- [YC-Bench](https://arxiv.org/abs/2604.01212): What it evaluates: state memory in long-term planning and consistent execution. Core idea: make agents repeatedly use historical goals, resource states, and intermediate decisions in ongoing business-management-style tasks, observing the real benefits of context truncation, scratchpads, and memory strategies.
- [LongMemEval-V2](https://arxiv.org/abs/2605.12493): What it evaluates: long-term agent memory for the "experienced coworker" scenario. Core idea: move long-term interaction memory beyond QA recall toward experience reuse, preference persistence, and context transfer in work settings.
- [EvoMemBench](https://arxiv.org/abs/2605.18421) ([code](https://github.com/DSAIL-Memory/EvoMemBench)): What it evaluates: self-evolution capability of agent memory. Core idea: divide memory tasks by `in-episode / cross-episode` x `knowledge / execution` to evaluate memory strategies more systematically.
- [MINTEval](https://arxiv.org/abs/2605.18565): What it evaluates: memory for long-horizon, frequently updated, mutually interfering information. Core idea: use multi-objective interference to upgrade static recall pressure into dynamic memory and aggregation reasoning.
- [MemGym](https://arxiv.org/abs/2605.20833): What it evaluates: long-horizon agent memory environments. Core idea: use Memory-Isolated Tasks to isolate memory writing, retention, and later use from ordinary task capability, and connect scenarios such as MEMGYM-DR and MEMGYM-SWE to deep research and software tasks.

## 1.15.3 Agent Harness

- [Reflexion](https://arxiv.org/abs/2303.11366) ([code](https://github.com/noahshinn/reflexion)): Converts failure trajectories into language feedback and episodic memory for use in the next attempt; an early representative of using experience memory to improve repeated agent attempts.
- [Generative Agents](https://arxiv.org/abs/2304.03442) ([code](https://github.com/joonspk-research/generative_agents)): Combines memory streams, reflection, and planning loops into long-term behavioral agents, and is a common starting point for later agent-memory papers.
- [MemoryBank](https://arxiv.org/abs/2305.10250) ([code](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)): Builds long-term memory writing, retrieval, and personality/preference updates as dialogue-agent components, useful for tracking cross-turn consistency.
- [Voyager](https://arxiv.org/abs/2305.16291) ([code](https://github.com/MineDojo/Voyager)): Distills exploration experience into a callable skill library and long-term memory; although the task is Minecraft, it established the classic harness form of `experience writing -> retrieval reuse -> capability accumulation`.
- [MemGPT](https://arxiv.org/abs/2310.08560) ([code](https://github.com/cpacker/MemGPT)): Reframes the long-context problem as explicit memory tiers and scheduling policies, forming a reusable long-horizon agent runtime.
- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) (code: no stable public repository found): A memory mechanism for multi-step agent workflows; core idea: have agents explicitly record key states, tool results, and decision rationales during task execution, then retrieve them as needed in later steps instead of feeding back the full history.
- [Zep](https://arxiv.org/abs/2501.13956) ([code](https://github.com/getzep/graphiti)): A temporal knowledge-graph architecture for agent memory; core idea: organize events, entities, relations, and temporal evolution into a queryable graph for long-term personalization and cross-session recall.
- [A-MEM](https://arxiv.org/abs/2502.12110) ([code](https://github.com/WujiangXu/A-mem)): A dynamic memory organization framework for agents. Core idea: write memory fragments as linkable and evolvable knowledge structures that support later retrieval, recombination, and reflection.
- [Mem0](https://arxiv.org/abs/2504.19413) ([code](https://github.com/mem0ai/mem0)): A scalable long-term memory layer for production agents. Core idea: use an automatic extraction, update, and retrieval memory pipeline to reduce reliance on full historical context.
- [MemoryOS](https://arxiv.org/abs/2506.06326) ([code](https://github.com/BAI-LAB/MemoryOS)): Decomposes agent memory into OS-like operations such as storage, update, retrieval, and consolidation; useful as a general memory runtime for long-term interaction tasks.
- [MemOS](https://arxiv.org/abs/2507.03724) ([code](https://github.com/MemTensor/MemOS)): Builds long-term memory, hybrid retrieval, cross-task experience reuse, and token savings into a self-evolving memory OS, suitable for memory-first runtimes in production agents.
- [MIRIX](https://arxiv.org/abs/2507.07957) ([code](https://github.com/Mirix-AI/MIRIX)): A multi-agent memory system. Core idea: use specialized memory-management agents to maintain short-term, episodic, semantic, and procedural memory for cross-session calls in long-horizon tasks.
- [Hindsight](https://arxiv.org/abs/2512.12818) ([code](https://github.com/vectorize-io/hindsight)): A memory harness for production agents. Core idea: distill execution trajectories after tasks into retrievable experience and reuse it in later tasks through recall and reflection.
- [UMA](https://arxiv.org/abs/2602.18493): Unifies memory operations and question answering under a single policy. Core idea: use an explicit Memory Bank for CRUD memory writing, targeting ultra-long streaming state tracking.
- [True Memory](https://arxiv.org/abs/2605.04897): A systematic response to the idea that "storage is not memory". Core idea: define the key capabilities of a memory system as extraction, organization, update, retrieval, forgetting, and action binding, rather than merely placing historical text in a vector database.

## 1.15.4 Skill

- [deep-agents-memory](https://skills.sh/langchain-ai/langchain-skills/deep-agents-memory) is suitable for adding a retrievable long-term memory layer to deep agents.
- [remembering-conversations](https://skills.sh/obra/episodic-memory/remembering-conversations) is suitable for saving and recalling user facts and preferences from multi-turn conversations.
- [memory-management](https://skills.sh/anthropics/knowledge-work-plugins/memory-management) is suitable for explicitly maintaining long-term preferences, project state, and work habits in knowledge work.
- [agent-memory-systems](https://skills.sh/sickn33/antigravity-awesome-skills/agent-memory-systems) is suitable for designing memory stores, retrievers, summarizers, and update strategies.
- [mem0-mcp](https://skills.sh/mem0ai/mem0/mem0-mcp) is suitable for connecting mem0 memory to runtimes such as Claude Code, Codex, and Cursor through MCP tools.
- [mem0-codex](https://skills.sh/mem0ai/mem0/mem0-codex) is suitable for automatic memory retrieval, key learning writes, and session-state saving in Codex-style tasks.
