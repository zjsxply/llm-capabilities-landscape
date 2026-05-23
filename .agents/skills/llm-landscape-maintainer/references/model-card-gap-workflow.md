# Model-Card Gap Workflow

Use this reference when the task is to align the landscape with frontier model cards or system cards from vendors such as OpenAI, Anthropic, Moonshot/Kimi, ByteDance Seed, Google, xAI, Meta, or DeepSeek.

## Goal

Find benchmarks, task families, safety evaluations, and internal/closed evaluation suites that appear in recent model cards but are missing from this repository. The output should be a categorized gap list and, when requested, bilingual landscape edits.

## Workflow

1. Identify the latest relevant model cards from official sources. Use web verification because model cards change over time; save source snippets or extracted text under `.tmp/model-card-gap/`.
2. Extract every benchmark or evaluation mention into a compact table with provider, model/card name, card date, benchmark name, capability category, public status, source URL, and evidence note.
3. Mark public status explicitly: public paper, public dataset, public leaderboard, project page only, model-card-only, closed/internal, or unclear.
4. Build the repository inventory from the recursive `docs/en/` tree first, then spot-check the paired `docs/zh/` tree for bilingual alignment. Normalize aliases before deciding a benchmark is missing.
5. Classify gaps by task axis, not by implementation substrate. Cybersecurity evaluations go under Cybersecurity even when they use terminals; embodied, game, robot, or vision-language-action evaluations go under Embodied/VLA rather than GUI-only computer use.
6. When a gap does not fit existing taxonomy, propose a new category only if it reflects a durable task boundary rather than a one-off benchmark.
7. Prioritize gaps that indicate current frontier-vendor focus: medical/health, biological and chemical risk, cybersecurity, agent safety, real-world work, long-horizon agents, deep research, computer use, embodied/VLA, and high-difficulty reasoning.
8. Include closed or internal evaluations in the relevant Bench list when they are repeatedly emphasized by model cards or fill a high-priority task gap. State that they are not publicly released and avoid implying reproducibility.
9. Sort inserted entries by release time. For papers, use arXiv or publication date; for datasets/leaderboards, use public launch date if known; for model-card-only or internal evaluations, use the card/report date.
10. Update English Markdown first, then the Chinese counterpart. Preserve semantic alignment rather than literal translation.
11. Run URL checks on edited files and report successful, soft-blocked/rate-limited, and broken links separately.

## Pitfalls

- Do not classify by execution substrate. A cyber benchmark that runs in a Linux terminal is still cybersecurity; a game or robot benchmark with screenshots is still embodied/VLA, not GUI computer use.
- Do not leave the same benchmark as a primary Bench entry in both the old and new category after a taxonomy split. Search exact names and common aliases in both languages.
- Do not treat a vendor's closed/internal evaluation as reproducible. Use wording such as "reported in the model card", "not publicly released", or "no standalone public release has been confirmed".
- Do not assume model-card-only evaluations have the same date as the benchmark family they reference. Place them by the model card/report date unless a public benchmark release date is known.
- Do not rely on a full URL check alone to judge your edit. Broad checks often reveal unrelated historical 404s; run a narrow check over newly added pages or newly added URLs to isolate regressions.
- Do not update only README or only one language side when adding a new category. Add the paired `docs/en/<chapter>/<topic>/README.md`, `docs/zh/<chapter>/<topic>/README.md`, root `README.md`, and root `README.zh.md` together.

## Reporting Shape

Group findings by repository category. For each missing item, include:

- benchmark or evaluation name;
- provider/model card source;
- public status;
- why it belongs in this category;
- whether it was added, deferred, or needs follow-up verification.
