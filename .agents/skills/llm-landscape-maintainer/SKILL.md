---
name: llm-landscape-maintainer
description: Maintain the llm-capabilities-landscape repository and its benchmark, agent harness, skill, citation, leaderboard, and URL entries. Use when updating or auditing this repository's Markdown landscape files, researching new LLM capability benchmarks or agents from seed papers/projects, aligning coverage with frontier model cards, checking Semantic Scholar citations and references, validating URLs, or migrating and reusing citation caches for this project.
---

# LLM Landscape Maintainer

## Capability Modes

- **Seed expansion**: start from user-provided seed papers, projects, benchmarks, or agents; expand through surveys, baselines, references, citations, repositories, leaderboards, and implementation checks before updating the landscape.
- **Model-card alignment**: compare the latest vendor model cards/system cards against the repository inventory, identify benchmark/task gaps, classify them into the taxonomy, and add important public or closed/internal evaluations with clear public-status notes. For this workflow, read `references/model-card-gap-workflow.md`.
- **Venue-track intake**: when the user asks for the latest papers from a conference, proceedings, workshop, or named track, enumerate the official accepted-paper source first, then screen and expand the accepted set through papers, repositories, and citation edges. Keyword search and citation closure are supplements, not completeness checks for a recent venue.

## High-Value Workflows

- **Taxonomy split or category cleanup**: define the task axis first, add paired English/Chinese category files when needed, update both README files, move entries out of neighboring categories, then run `rg` for every moved benchmark name across `docs/en` and `docs/zh` to catch leftover mentions in Bench and Agent Harness prose.
- **Latest-conference intake**: pin the venue, year, track, and acceptance status; enumerate its official index, proceedings, or OpenReview venue page/API; save a screening ledger in `.tmp/` with official title, alias, paper URL, repository/dataset URL, inclusion decision, and destination file; only then run taxonomy filtering and citation expansion. For NeurIPS Datasets and Benchmarks, explicitly query the Datasets and Benchmarks track rather than assuming a general NeurIPS or arXiv keyword search covers it.
- **Model-card gap ingestion**: extract vendor-reported evaluations into a table, normalize aliases against `docs/en/*.md`, classify by task axis, add closed/internal suites only with explicit "not publicly released" wording, and place them by card/report date.
- **Chronological maintenance**: when inserting entries, compare surrounding arXiv IDs, publication dates, dataset launch dates, and card dates before editing. Do not just append new model-card gaps at the end of a section unless the card date makes that correct.
- **Validation pass**: run a narrow URL check on newly added or heavily edited files, and a broader check when many existing files changed. Treat old broken links found by the broad check separately from newly introduced failures.

## Core Workflow

1. Read `AGENTS.md` and the target `*.md`/`*.zh.md` files before editing.
2. Preserve bilingual alignment outside `research/`: update English first, then Chinese.
3. Define inclusion and exclusion criteria before collecting candidates. State what belongs in Bench, Agent Harness, Skill, or Leaderboard, and what belongs in a neighboring category.
4. Sort entries by release time when dates are known. For model-card-only, closed, or internal evaluations, place them by the model card or report date and explicitly mark that the task set is not publicly released.
5. Select the discovery anchor from the request. For a latest-conference or named-track request, sweep the official accepted-paper source before doing topic search. For a seed/topic request, search recent surveys first to map task boundaries, benchmark families, terminology variants, and common baselines.
6. Normalize official paper titles, benchmark acronyms, alternate project names, arXiv identifiers, and OpenReview identifiers against existing documents before deciding that a work is missing.
7. Read milestone or newly accepted papers and inspect their baseline/comparison sections. Baselines are first-class candidates for this landscape.
8. For every already included or newly accepted paper that matters to the target section, use Semantic Scholar API to collect both citations and references as candidate related work. If the API returns `429`, slow down and retry from cache; if a complete run remains impractical, preserve the official-venue sweep and explicitly report the bounded closure rather than implying full citation coverage.
9. Cross-check accepted candidates against the paper, official venue entry, project page, official repository, leaderboard, and actual implementation when relevant. Keep a stable official paper URL when no arXiv version is available.
10. Verify newly added URLs before finishing.
11. Keep final Chinese prose concise, professional, and classification-oriented.

## Venue-Track Coverage

Use this checklist whenever completeness over a recent conference or track matters:

1. Record the exact venue, year, track, and accepted-paper source used for enumeration; do not silently broaden a workshop, main conference, or Datasets and Benchmarks track into another population.
2. Extract the complete official candidate list into a `.tmp/` ledger before screening. Preserve paper titles and official IDs even when arXiv, code, or dataset pages are absent.
3. Resolve title drift and benchmark aliases before deduplication. A paper title and its benchmark name may differ substantially, so match using the official title, acronym, arXiv ID, OpenReview ID, project page, and repository where available.
4. Assign each in-scope candidate a destination category and a brief reason, or log a deferral/exclusion reason. When a benchmark is genuinely cross-cutting or a stable family has not formed, place it in a documented `Other` category rather than forcing it into a misleading neighboring axis.
5. Run reference and citation expansion after venue enumeration to explore adjacent work and follow-ups. Treat this expansion as closure around the official seed set, not as proof that the official seed set was complete.
6. When reporting results, distinguish official-venue coverage, arXiv/project-link enrichment, citation/reference closure, URL verification, and any incomplete phase caused by rate limiting or inaccessible sources.

## Candidate Screening

Accept candidates that clearly fit one of these roles:

- **Leaderboard**: official or widely used public ranking with enough task specificity to help readers locate current systems.
- **Bench**: evaluates a capability with a defined task, dataset, protocol, leaderboard, or metric.
- **Agent Harness**: contributes prompting, workflow orchestration, tool use, memory, multi-agent collaboration, environment management, verification, or other model-external execution logic.
- **Skill**: provides reusable agent capability packages, skill runtime infrastructure, skill benchmarks, skill creation, skill selection, skill safety, or skill portability.

Reject or defer candidates when:

- the main contribution is pretraining, post-training, data scaling, or model architecture and the agent/harness layer is thin;
- the paper is only a narrow domain application that does not broaden the target capability taxonomy;
- it duplicates a stronger existing entry without adding a distinct axis;
- the project link is inaccessible and no stable paper or repository URL exists.

## Evidence And Writing

- Prefer English academic sources, especially conference papers, arXiv papers, official project pages, official repositories, and benchmark leaderboards.
- Use arXiv URLs when a paper exists. If no paper exists, do not force a paper link.
- Cite industry, product, and leaderboard facts adjacent to the claim.
- Treat Semantic Scholar candidates as candidates only; read the source before adding it.
- Keep a claim-evidence map for substantive edits. Each new paragraph or entry should have a reason to exist, a source that supports it, and a clear category.
- Separate official baselines, reproduced baselines, local modified runs, retry runs, and leaderboard systems; do not merge incompatible evaluation protocols.
- Put citations near the claim they support, not in a bundle at the end of a long sentence.
- For this standalone repository, keep English `*.md` and Chinese `*.zh.md` semantically aligned outside any future `research/` directory.
- Avoid symbolic shorthand such as `/` and `+` in narrative prose; use explicit conjunction phrases.

## Scripts

Run scripts from the repository root.

- Semantic citation and reference scan:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/semantic_scholar_citation_scan.py --out .tmp/s2_report.md TARGET_FILES...`
  The scanner adaptively changes its request delay: successful network requests linearly reduce the delay toward `--min-delay`, while `429` responses double the delay up to a hard 30-second cap.
- Citation coverage audit before or after Markdown edits:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/citation_coverage_audit.py --out .tmp/s2_citation_coverage.md TARGET_FILES...`
  Use this instead of ad hoc Python for finding Markdown papers that lack cached citation edges.
- Missing citation backfill:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/scan_missing_citations.py --out .tmp/missing_s2_citation_report.md TARGET_FILES...`
  This wraps the coverage audit and then runs the serial Semantic Scholar scanner with `--direct-edges`, `--citations-only`, `--min-delay 0.1`, adaptive backoff, and cache reuse.
- Candidate report from existing Semantic Scholar cache:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/citation_candidate_report.py --out .tmp/citation_candidates_existing_cache.md TARGET_FILES...`
  Use this to inspect cached citation/reference edges before doing new API calls.
- Large candidate triage:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/citation_candidate_triage.py .tmp/unchecked.json --chunk-dir .tmp/triage_chunks`
  Use this when citation closure creates thousands of candidates. It conservatively auto-rejects only low-citation, single-relation candidates with no title/abstract signal for this repository's taxonomy, and writes compact review chunks for subagents.
- Subagent decision sync:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/sync_candidate_decisions.py --apply --mark-state`
  Use this after parallel candidate screening. It normalizes both `decision` and `status` schemas, maps subagent include/accept recommendations to `deferred` until the parent actually edits official docs, updates the checked-paper registry under the shared lock, and records synced chunk files so repeated runs only process new outputs. Use `--resync chunk-006.json` when a previously synced chunk needs correction.
- Parent-review shortlist:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/parent_review_shortlist.py`
  Use this after all subagent chunks are synced. It scores include recommendations, removes entries already present in docs, writes a strict parent-review shortlist, and splits it by target document so final edits can stay focused. Treat this as a review aid, not an automatic inclusion decision.
- Checked-paper registry:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/checked_paper_registry.py candidates --out .tmp/s2_unchecked_candidates.md`
  The default registry is `.tmp/landscape-maintainer/checked-papers.json`; use it to mark papers already included, rejected, or deferred so future citation scans surface only newly unchecked candidates.
  For parallel screening, each subagent must reserve work with `claim --owner NAME --out .tmp/NAME.md --json-out .tmp/NAME.json`, then submit decisions with `mark-from-json`. Registry operations acquire a shared `.lock` file, silently wait up to `--lock-timeout` seconds by retrying every `--lock-wait` seconds, and save updates atomically; do not edit the JSON registry directly.
- URL accessibility check:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/check_urls.py --out .tmp/url_report.md TARGET_FILES...`
  URL results are cached by default in `.tmp/landscape-maintainer/url-check-cache.json`; entries checked within the last 30 days are reused instead of being requested again. Use `--refresh-cache` only for targeted rechecks, or `--cache-ttl-days N` when a shorter or longer freshness window is justified.
- URL check for changed Markdown only:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/check_changed_urls.py --out .tmp/url_check_changed.md`
  Use this instead of manually expanding `git diff` file lists. It shares the same 30-day URL cache, which avoids repeatedly hitting sites during broad checks.
- Session command mining:
  `python3 .agents/skills/llm-landscape-maintainer/scripts/session_command_miner.py --min-tokens 300 --out .tmp/session_long_commands.md`
  Use this when extracting reusable long commands from `~/.codex` sessions. Promote only commands that match this repository's maintenance workflow.

The Semantic Scholar cache lives under `.tmp/semantic_citation_cache/`. Reuse it across runs. The legacy cache from `/data/panly/skill-arena/.tmp` has been migrated here; do not recreate project-specific caches under the old repository.
If a one-off shell or Python command grows beyond roughly 300 tokens or recurs across sessions, prefer adding a focused script under this skill instead of leaving it as terminal history.

## Notes

- Keyword search misses many relevant works. Combine keyword search, survey reading, baseline inspection, references, citations, GitHub search, and leaderboard inspection.
- Fresh proceedings and benchmark tracks are especially easy to miss through keywords or citation graphs: titles may use project names rather than task terms, accepted papers may have sparse citation edges, and some works may temporarily have only an official venue page. Use official venue enumeration as the recall anchor.
- Semantic Scholar closure broadens a seed set but does not certify coverage of a newly accepted conference track. Preserve and report official-track coverage separately from citation-graph expansion.
- Semantic Scholar citation results are noisy. Rank by fit first, then recency and citation count; do not add every candidate just because it appears in the graph.
- Survey papers are useful twice: they identify taxonomy and expose baselines that should be checked as potential landscape entries.
- Benchmark names drift across papers, project pages, and leaderboards. Normalize names and verify whether variants are distinct tasks or aliases.
- Active leaderboards can contain systems without papers. Add them only when the system is relevant and the leaderboard or project URL is stable.
- Keep task boundaries clean when benchmarks use the same substrate. For example, cybersecurity benchmarks belong in the cybersecurity category even when they run in a terminal, and embodied or vision-language-action benchmarks belong in an embodied/VLA category rather than GUI-only computer use.
- When moving a benchmark to a new category, remove duplicate primary listings from old categories. Keep cross-references only when they explain a neighboring capability rather than re-listing the benchmark as part of that category.
- Cache per paper and per edge list so interrupted Semantic Scholar runs are recoverable.
- Treat empty citation-cache files as valid only if they contain a successful response with empty `data`; re-fetch malformed or truncated JSON.
- Do not let several subagents hit Semantic Scholar in parallel. Use one serial scanner, or a shared file lock and cache, while subagents do reading and screening from saved reports.
- Keep candidate provenance such as `candidate cites arXiv:<seed>` or `seed references arXiv:<candidate>` in `.tmp` reports so rejected and accepted items remain auditable.
- Use GET fallback when HEAD fails. Some sites block HEAD even when the page is accessible.
- Reuse the project-local URL cache for routine checks. A URL checked in the last month should not be fetched again unless a focused verification requires `--refresh-cache`.
- Report URL checks in three classes: successful, soft-blocked or rate-limited, and broken. A blocked dynamic page needs manual replacement only when a better stable URL exists.
- A broad URL check can surface pre-existing 404s unrelated to the current edit. Do not hide them, but do not conflate them with newly added links; run a narrow check for new pages or new URLs before final reporting.
- For GitHub code links, prefer checking the repository itself rather than only the HTML page status.
- Give each subagent a disjoint file scope or a read-only report path under `.tmp/`.
- Prefer single-writer final edits: subagents write memos, while the parent agent merges into official Markdown files after rereading current file contents and `git status`.
- In dirty worktrees, inspect both `git diff` and `git diff --cached` for relevant files. Some agent sessions leave files staged as additions, so `git diff --stat` alone may under-report the actual content being edited.
- Agent Harness entries should emphasize workflow, tool orchestration, memory, environment interaction, verification, or multi-agent design.
- Skill entries should point to real skill artifacts, skill runtimes, skill benchmarks, skill safety work, or skill portability infrastructure.

## Hard Rules

- Do not rely on keyword search alone for paper discovery; use citation and reference traversal.
- When the request concerns latest papers from a named conference or track, do not rely on arXiv, keyword search, or citation traversal as the primary inventory; enumerate the official accepted-paper source first and record that sweep.
- Do not claim citation or reference closure is complete when an API was rate-limited, unavailable, or only partially scanned; report the bounded evidence actually collected.
- Do not add leaderboard, product, or adoption claims without an adjacent citation or URL.
- Do not append new Bench, Agent Harness, Skill, or Leaderboard entries out of chronological order when release dates are available.
- Do not treat training-only model papers as core Agent Harness entries unless the harness/workflow design is the contribution.
- Do not leave broken newly added URLs in the repository.
- Do not let parallel subagents edit overlapping files without explicit file ownership.
