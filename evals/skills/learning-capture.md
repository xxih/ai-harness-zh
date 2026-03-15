# Asset Eval: learning-capture

## Asset Under Test

- Type: skill
- Path: src/skills/learning-capture/SKILL.md
- Goal: provide a manual learning-capture entry that helps users accumulate task-level learnings and promotion candidates before introducing automation.

## Capability Evals

### capability-1

Goal: the skill is clearly manual-triggered and scoped to session/task accumulation.

Success Criteria:

- [ ] `SKILL.md` states that the current phase is manual trigger rather than hooks-driven automation
- [ ] `SKILL.md` targets a single session or task, not a full automatic learning system
- [ ] `SKILL.md` defines concrete trigger phrases such as “复盘一下” or “手动触发学习积累”

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill establishes durable structure before future automation.

Success Criteria:

- [ ] `SKILL.md` defines a project-root default such as `.learned/`
- [ ] `SKILL.md` separates `learnings.md`, `promote-candidates.md`, and `project-rules.md`
- [ ] `SKILL.md` defines `keep-local`, `promote-later`, `propose-agents-update`, and `drop`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill remains light-weight and does not overreach into later phases.

Success Criteria:

- [ ] the skill body is primarily in Chinese
- [ ] `SKILL.md` does not require hooks or observer runtime
- [ ] `SKILL.md` does not claim to auto-create formal `src/skills/`, `src/commands/`, or `evals/` assets
- [ ] `SKILL.md` links to `references/templates.md`
- [ ] `SKILL.md` can capture project-level rule corrections and queue AGENTS/README updates without directly editing them by default
- [ ] `SKILL.md` does not treat `nanospec` as the default learning sink

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
