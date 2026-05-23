## Environment

Use the uv-managed Python virtual environment in this workspace.
Install dependencies with `uv pip install ...`.
Run scripts with `source .venv/bin/activate && python ...`.

## Bilingual Documentation

All documentation must be bilingual and semantically aligned.
For root-level project documents such as `README` and `AGENTS`, use paired files:
- English in `*.md`
- Chinese in `*.zh.md`

For numbered landscape documents, use language-specific trees:
- English under `docs/en/<chapter>/<topic>/`
- Chinese under `docs/zh/<chapter>/<topic>/`

Use `README.md` as the topic overview file when a topic is split into section files. Section files use the third-level number and slug, for example `03-bench.md`, `04-model.md`, and `05-agent-harness.md`.
The introduction chapter is the exception: it uses second-level Markdown files directly under `docs/<lang>/00-introduction/`, for example `01-landscape-structure.md`.

The English and Chinese numbered files must share the same base filename.
Do not add a `.zh` suffix to files under `docs/zh/`.

When one version changes, update the paired version in the same edit.
For documentation changes, revise the English version first and then update the Chinese version.
Document expression should follow native language conventions in each version; avoid stiff literal translation.
When editing AGENTS, preserve meaning and constraints but phrase them naturally; verbatim copying of user wording is not required.

## Research and Writing Style

Prioritize English sources and professional academic references, especially conference literature.
Focus on recent progress from roughly the past year, including both survey papers and milestone papers.
Search in both Chinese and English across PDFs, PPTs, and web pages, while using English sources as primary evidence.
Think and operate in English during execution, then produce final artifacts in fluent natural Chinese.

If remote repositories are needed, first check whether a matching copy already exists at the canonical `/tmp` path; if it does, run `git pull` in that directory, otherwise clone there.
To make reused materials easy to find across different agent runs, use the following `/tmp` layout:
- GitHub repositories: `/tmp/github-repos/<owner>/<repo>`
- arXiv TeX sources: `/tmp/arxiv/<arxiv_id>` (for example `/tmp/arxiv/1706.03762`)
If you need a project-local temporary directory for drafts, intermediate files, or page checks, use the workspace-root `.tmp/` directory rather than creating another ad hoc temp folder.
For GitHub paths, strip any trailing `.git` suffix and reuse the normalized owner/repo path.
For arXiv paths, use the canonical paper ID as the directory name; keep a version suffix only when the task explicitly depends on that version.
If arXiv papers are involved, download and extract TeX sources into their canonical `/tmp` directory before deep reading.
If a Hugging Face dataset is needed, it is allowed to load directly via `datasets.load_dataset(...)`.
Local caching under `.cache` (for example `~/.cache`) is allowed in this workspace.

## Paper Citation Style

For related-work writing in this project:
- Keep wording concise; avoid inflated or repetitive phrasing.
- Prefer placing citations at clause boundaries as soon as the claim appears.
- Avoid stacking many citations only at the end of a long sentence.
- If a sentence claims an industry/product adoption fact, attach the citation right after that clause.
- If a paper has a short, well-recognized name or acronym (for example, SkillRL or SkillsBench), use that name directly. If the title is long or awkward in running text, use neutral phrasing such as "a study/work" instead of spelling out the full title.
- Manuscript prose must follow formal scientific writing conventions: avoid symbolic shorthand such as `/` and `+` in narrative sentences, and use explicit conjunction phrases instead.

## Skill Search Workflow

When the task is to search for skills, follow this workflow:
- Use both `npx skills find` and `npx clawhub search` to find skills that can do **【target capability/task】**.
- Also query SkillNet via its API endpoint, for example `curl -s 'http://api-skillnet.openkg.cn/v1/search?q=paper%20rebuttal'`, and treat its results as an additional first-class source when searching for **【target capability/task】**.
- In addition to skill marketplaces, also search GitHub directly for repositories or skill directories related to **【target capability/task】**. Try multiple keyword variants there as well, and treat GitHub hits as first-class candidates for later implementation inspection.
- `npx clawhub` is rate-limited fairly aggressively, so throttle requests, prefer serial execution, and avoid launching several searches in a short burst.
- The SkillNet API is keyword-based as well; always try multiple keyword variants, and normalize returned GitHub/blob/tree URLs to the most stable public entry you can verify.
- Read **【target paper】** first, then align screening criteria to that paper's task definition.
- These search interfaces are keyword-only rather than semantic retrieval. Always try multiple keyword variants.
- If multiple candidate skills are returned, spawn parallel sub-agents and verify each candidate independently.
- Clone candidate repositories into their canonical `/tmp/github-repos/<owner>/<repo>` path, but first check whether each candidate is already cloned locally. If it exists, continue from that directory and run `git pull`; if not, clone it there. Then inspect the real implementation (for example `SKILL.md`, scripts, templates, helper code) to decide whether it truly matches **【target capability/task】**.
- After confirming the final matched set, provide a concrete design summary for each skill.

## Agent Search Workflow

When the task is to search for agents, follow this workflow:
- Read the target benchmark or target paper first, then pin down the task boundary, input-output format, and evaluation protocol from that source.
- While screening candidates, open each relevant paper and inspect its baseline section so you can understand what it is compared against, where the gains come from, and whether the evaluation setup is actually comparable.
- It is also useful to inspect later papers that cite these works, in order to identify follow-up high-impact methods, variants, and extensions.
- Prioritize candidates whose main contribution is rich prompts, tool use, workflow orchestration, memory, or explicit multi-agent collaboration.
- If a paper's primary contribution is training algorithms, data scaling, pretraining, or post-training recipes, and the agent design itself is weak, do not treat it as a core agent candidate for this task.
- If multiple agent candidates remain, cross-check the paper, project page, and actual repository implementation rather than relying only on leaderboard positions or abstract-level claims.

## `sota-agents-and-skills` Formatting Rules

When updating this document, follow these rules:
- For every Agent entry, put the paper link on the Agent name, then add the open-source code URL in parentheses.
- You must actively search for and use the arXiv paper URL whenever a paper exists.
- If it is clear that no paper exists for an Agent, do not keep a hyperlink on the Agent name.
- For every Skill entry, put a hyperlink on the Skill name (from `skills.sh`, `clawhub`, or another official source).
- Verify every newly added URL in this file is accessible. If a newly added link is broken, fix or remove it before finishing the edit.
