# Asset Eval: coding-quality-loop

## Asset Under Test

- Type: skill
- Path: skills/coding-quality-loop/SKILL.md
- Goal: provide a single, lightweight coding-quality skill that defaults to a full quality loop and can route to `/tdd`, `/verify`, or `/review` when explicitly requested.

## Capability Evals

### capability-1

Goal: the skill provides one default quality loop without requiring stage-specific entry upfront.

Success Criteria:

- [ ] `SKILL.md` defines a default path that covers implementation quality end to end
- [ ] `SKILL.md` explicitly includes test-first, verification, and review as parts of one loop
- [ ] `SKILL.md` describes the loop through coding phases such as before implementation, after changes, and before delivery
- [ ] `SKILL.md` does not require the user to pick a sub-skill before getting guidance

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill supports command-like routing through explicit stage triggers.

Success Criteria:

- [ ] `SKILL.md` routes `/tdd` to a dedicated TDD stage
- [ ] `SKILL.md` routes `/verify` to a dedicated verification stage
- [ ] `SKILL.md` routes `/review` to a dedicated review stage

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-3

Goal: the skill keeps the entry lightweight and moves detailed procedures into references.

Success Criteria:

- [ ] `SKILL.md` links to `references/tdd.md`
- [ ] `SKILL.md` links to `references/verify.md`
- [ ] `SKILL.md` links to `references/review.md`
- [ ] `SKILL.md` defines a reusable report output such as `quality-check.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill remains clearly about coding quality rather than prompt-asset governance.

Success Criteria:

- [ ] the skill body is primarily in Chinese
- [ ] `SKILL.md` is clearly about coding tasks and code changes
- [ ] `SKILL.md` does not require prompt-asset-specific review paths like paired eval checks

Graders:

- Code: `python3 scripts/validate_assets.py`

### regression-2

Goal: the skill stays tool-neutral and does not depend on harness-specific runtime features.

Success Criteria:

- [ ] `SKILL.md` does not require `.claude/`
- [ ] `SKILL.md` does not require subagents, hooks, or plugin marketplaces
- [ ] detailed stage guidance lives in `references/`

Graders:

- Code: `python3 scripts/validate_assets.py`

### regression-3

Goal: the default entry stays user-facing and does not expose internal packaging rationale.

Success Criteria:

- [ ] `SKILL.md` does not use memory-cost phrasing such as “不想分别记忆”
- [ ] `SKILL.md` does not tell the user they need to assemble the workflow themselves
- [ ] `SKILL.md` explains when to use the loop via coding context and quality actions rather than skill-packaging reasons

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
