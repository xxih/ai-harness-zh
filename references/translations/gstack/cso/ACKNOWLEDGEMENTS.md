# 致谢

`/cso v2` 参考了安全审计领域中的大量研究成果。致谢如下：

- **[Sentry Security Review](https://github.com/getsentry/skills)**：基于置信度的报告系统（只有 `HIGH` 置信度的 findings 才会上报），以及“先研究、再报告”的方法论（追踪 data flow、检查上游 validation），直接验证了我们“每日 8/10 置信度 gate”的可行性。TimOnWeb 评价它是 5 个测试对象里唯一值得安装的 security skill。
- **[Trail of Bits Skills](https://github.com/trailofbits/skills)**：先建立 audit context、再开始找 bug 的方法，直接启发了我们的 Phase 0。他们的 variant analysis 思路（找到一个 vuln 后，继续在整个 codebase 里搜同类模式）启发了 Phase 12 的 variant analysis 步骤。
- **[Shannon by Keygraph](https://github.com/KeygraphHQ/shannon)**：一个 autonomous AI pentester，在 XBOW benchmark 上做到 96.15%（100/104 exploits）。它证明 AI 可以做真正的安全测试，而不只是跑 checklist。我们的 Phase 12 active verification，本质上就是 Shannon 在线实测思路的静态分析版本。
- **[afiqiqmal/claude-security-audit](https://github.com/afiqiqmal/claude-security-audit)**：其中针对 AI / LLM 的专项安全检查（prompt injection、RAG poisoning、tool calling permissions）启发了 Phase 7。它对 framework 级自动识别的做法（识别 `Next.js`，而不是只识别 `Node/TypeScript`）也启发了 Phase 0 的框架检测步骤。
- **[Snyk ToxicSkills Research](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)**：其研究指出 36% 的 AI agent skills 存在安全缺陷，13.4% 带有恶意行为，这直接启发了 Phase 8（Skill Supply Chain scanning）。
- **[Daniel Miessler's Personal AI Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure)**：其中的 incident response playbooks 与 protection file 概念，为 remediation 与 LLM security phases 提供了参考。
- **[McGo/claude-code-security-audit](https://github.com/McGo/claude-code-security-audit)**：其“生成可共享报告与可执行 epic”的思路，推动了我们报告格式的演进。
- **[Claude Code Security Pack](https://dev.to/myougatheaxo/automate-owasp-security-audits-with-claude-code-security-pack-4mah)**：模块化拆分（独立的 `/security-audit`、`/secret-scanner`、`/deps-check` skills）证明这些确实是不同问题域。我们的统一方案则是用模块化换取跨阶段推理能力。
- **[Anthropic Claude Code Security](https://www.anthropic.com/news/claude-code-security)**：多阶段验证与置信度评分，验证了我们并行 findings verification 的方向。它在开源项目里找到了 500+ 个 zero-days。
- **[@gus_argon](https://x.com/gus_aragon/status/2035841289602904360)**：指出了 v1 的关键盲点：没有 stack detection（所有语言规则一起跑）、使用 bash `grep` 而不是 Claude Code 的 `Grep` 工具、`| head -20` 会静默截断结果，以及 preamble 过度膨胀。这些反馈直接塑造了 v2 的 stack-first 方案与 Grep tool mandate。
