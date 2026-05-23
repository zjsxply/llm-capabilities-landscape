# 0.3 Skill Creator

> Parent chapter: 0. Harness and Skill Creator


- `Skill Creator` is not about "solving one problem", but about "packaging stable workflows into reusable skills."
  It usually covers `frontmatter`, directory skeletons, progressive disclosure for `references/` and `scripts/`, validation scripts, and evaluation loops when needed.
- [Anthropic's official skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) is one of the most complete creator tracks today.
  It closes the loop around `create -> eval -> aggregate -> review` and emphasizes that "skills should also be benchmarked and iterated."
- [OpenAI's official system skill-creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) puts more emphasis on the Codex ecosystem.
  In addition to `SKILL.md`, it requires maintaining `agents/openai.yaml` and provides initialization and quick validation scripts.
- [GitHub's official microsoft-skill-creator](https://skills.sh/github/awesome-copilot/microsoft-skill-creator) is better suited for quickly starting a skill for the Microsoft Learn / Copilot ecosystem.
- [make-skill-template](https://skills.sh/github/awesome-copilot/make-skill-template) is also better suited for quickly starting a skill for the Microsoft Learn / Copilot ecosystem.
- [daymade/skill-creator](https://github.com/daymade/claude-code-skills/tree/main/skill-creator) discusses `inline / fork`, composability, and automatic rewriting in a more practical way.
- [daymade/skill-reviewer](https://github.com/daymade/claude-code-skills/tree/main/skill-reviewer) gives a practical treatment of skill review and quality-improvement workflows.
- [CreateSkill](https://github.com/danielmiessler/Personal_AI_Infrastructure/tree/main/Releases/v4.0.0/.claude/skills/Utilities/CreateSkill) is a heavyweight creator in the PAI system.
  Beyond initialization, it covers workflows such as canonicalize, validate, and update, and imposes strong constraints on naming, directory hierarchy, and dynamic loading.
- [composiohq/skill-creator](https://skills.sh/composiohq/awesome-claude-skills/skill-creator) is more like a lightweight community variant of Anthropic's creator.
  It keeps initialization, validation, and packaging scripts, but removes heavyweight evaluation-analysis components, making it better for fast production.
- [dot-agent/create-skill](https://skills.sh/siviter-xyz/dot-agent/create-skill) emphasizes short `SKILL.md` files, strict progressive disclosure, and the maintenance view that "skills themselves should also be tested across models."
- [skill-creator-operator](https://clawhub.ai/Kevjade/skill-creator-operator) represents the premium skill-creator track with a "first-run setup wizard."
  It writes personalized configuration to the workspace instead of continually piling it into the prompt.
- [uxc-skill-creator](https://clawhub.ai/jolestar/uxc-skill-creator) leans more toward API / MCP wrapping.
  It emphasizes endpoint discovery, authentication-method identification, fixed link naming, and `validate.sh` constraints.
- [nima-skill-creator](https://clawhub.ai/NimaChu/nima-skill-creator) is a Chinese-friendly creator.
  It combines Chinese requirement interviews with English technical specifications in one workflow, making it suitable for Chinese users who need requirement clarification.
