# Asset Eval: quality-router

## Asset Under Test

- Type: skill
- Path: src/skills/quality-router/SKILL.md
- Goal: provide a manual, command-like routing entry for the quality skill family so users can explicitly trigger quality actions without relying on `src/commands/`.

## Capability Evals

### capability-1

Goal: the skill routes explicit quality triggers to the right prefixed skill.

Success Criteria:

- [ ] `SKILL.md` routes `/tdd` to `quality-tdd`
- [ ] `SKILL.md` routes `/verify` to `quality-verify`
- [ ] `SKILL.md` routes `/review` to `quality-review`
- [ ] `SKILL.md` routes `/review-feedback` to `quality-review-feedback`

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill works as a `src/commands/` replacement rather than a second full methodology.

Success Criteria:

- [ ] `SKILL.md` states that it is a manual routing entry for quality actions
- [ ] `SKILL.md` keeps detailed procedures in the routed skills instead of duplicating them
- [ ] `SKILL.md` defines a shared durable output strategy without requiring `nanospec`
- [ ] `SKILL.md` uses a project-local default output path such as `output/quality/quality-check.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the router stays inside the `quality-*` naming family.

Success Criteria:

- [ ] the skill body is primarily in Chinese
- [ ] `SKILL.md` references all routed skills with the `quality-` prefix
- [ ] `SKILL.md` does not route to `coding-quality-loop`
- [ ] `SKILL.md` does not require `nanospec/<task>/...` as its output path

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
