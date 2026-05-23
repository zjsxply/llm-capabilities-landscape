# 0.3 Skill Creator

> 上级章节：0. Harness 与 Skill Creator


- `Skill Creator` 关注的不是“解某一道题”，而是“怎样把稳定工作流打包成可复用 skill”。
  它通常覆盖 `frontmatter`、目录骨架、`references/` 与 `scripts/` 的渐进披露、验证脚本，以及必要时的评测闭环。
- [Anthropic 官方 skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) 是目前最完整的 creator 路线之一。
  它把 `create -> eval -> aggregate -> review` 做成闭环，强调“skill 也应被 benchmark 化迭代”。
- [OpenAI 官方 system skill-creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) 更强调 Codex 生态。
  它除了 `SKILL.md`，还要求维护 `agents/openai.yaml`，并提供初始化与快速校验脚本。
- [GitHub 官方 microsoft-skill-creator](https://skills.sh/github/awesome-copilot/microsoft-skill-creator) 更适合快速起一个面向 Microsoft Learn / Copilot 生态的 skill。
- [make-skill-template](https://skills.sh/github/awesome-copilot/make-skill-template) 更适合快速起一个面向 Microsoft Learn / Copilot 生态的 skill。
- [daymade/skill-creator](https://github.com/daymade/claude-code-skills/tree/main/skill-creator) 更实用地讨论了 `inline / fork`、组合性与自动改写。
- [daymade/skill-reviewer](https://github.com/daymade/claude-code-skills/tree/main/skill-reviewer) 更实用地讨论了 skill 审稿与质量改进流程。
- [CreateSkill](https://github.com/danielmiessler/Personal_AI_Infrastructure/tree/main/Releases/v4.0.0/.claude/skills/Utilities/CreateSkill) 是 PAI 体系里的重型 creator。
  它除了初始化，还覆盖 canonicalize、validate、update 等工作流，并对命名、目录层级与动态加载给出强约束。
- [composiohq/skill-creator](https://skills.sh/composiohq/awesome-claude-skills/skill-creator) 更像 Anthropic creator 的轻量社区变体。
  它保留初始化、校验与打包脚本，但去掉重型评测分析组件，更适合快速产出。
- [dot-agent/create-skill](https://skills.sh/siviter-xyz/dot-agent/create-skill) 强调短 `SKILL.md`、严格 progressive disclosure，以及“技能本身也要跨模型测试”的维护观。
- [skill-creator-operator](https://clawhub.ai/Kevjade/skill-creator-operator) 代表带“首次配置向导”的 premium skill creator 路线。
  它把个性化配置落盘到 workspace，而不是持续堆在 prompt 里。
- [uxc-skill-creator](https://clawhub.ai/jolestar/uxc-skill-creator) 更偏 API / MCP 封装。
  它强调 endpoint 探测、认证方式识别、固定 link 命名与 `validate.sh` 约束。
- [nima-skill-creator](https://clawhub.ai/NimaChu/nima-skill-creator) 则是中文友好型 creator。
  它把中文需求访谈与英文技术规范拼接在同一 workflow 中，适合中文用户做需求澄清。
