# 2.3.5 Skill

- [playwright-cli](https://github.com/microsoft/playwright-cli/tree/main/skills/playwright-cli)（可复用 browser-native action skill；与 WebArena 风格动作空间较贴近）
- [playwright](https://skills.sh/openai/skills/playwright)（通用 Playwright skill；偏浏览器执行层）
- [browser-automation](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/utilities/browser-automation)（系统化的 Playwright / Puppeteer 等待策略与网页自动化经验库）
- [bright-data-mcp](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/web-data/bright-data-mcp)（更适合“搜索 + 抓取 + 浏览器交互 + 抽取”的一体化工作流）
- [actionbook](https://skills.sh/actionbook/actionbook/actionbook)（把网页交互操作做成可复用 action script，含选择器与回退逻辑）
- [browserbase/agent-browse/browser](https://skills.sh/browserbase/agent-browse/browser)（浏览器自动化执行 skill；偏运行时）
- [serpapi](https://skills.sh/vm0-ai/vm0-skills/serpapi)（搜索 API skill；更贴近 WideSearch 的 search-heavy workflow）
- [ddgr](https://skills.sh/ysm-dev/ddgr-skill/ddgr)（终端搜索 skill；适合作为轻量检索层）
- [parallel-web-search](https://skills.sh/parallel-web/parallel-agent-skills/parallel-web-search) 适合并行 query fan-out 与来源收集，可服务 WideSearch/BrowseComp 类需要广召回再综合的任务。
- [web-search](https://skills.sh/brave/brave-search-skills/web-search) 是 Brave Search 支撑的 provider skill，适合需要稳定搜索 API、而不是浏览器抓取的 agent。
- [tavily](https://github.com/openclaw/openclaw/tree/main/extensions/tavily/skills/tavily) 是 Tavily 支撑的搜索与抽取 skill，更贴近“搜索 + 内容抽取”的工作流，而不只是 SERP 查询。
- [web-search-2](https://clawhub.ai/okaris/web-search-2)（研究、事实核查与内容抽取导向的检索型 skill）
