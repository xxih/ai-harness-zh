# Asset Eval: eval-harness

## Asset Under Test

- Type: skill
- Path: skills/eval-harness/SKILL.md
- Goal: provide a tool-neutral evaluation workflow for reusable AI prompt assets in this repository.

## Capability Evals

### capability-1

Goal: the skill defines an eval-first workflow instead of an implementation-first workflow.

Success Criteria:

- [ ] `SKILL.md` explicitly requires defining evals before changing the asset
- [ ] the workflow includes implementation, verification, and reporting steps

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill supports both `skills/` and `commands/` as first-class assets.

Success Criteria:

- [ ] `SKILL.md` mentions both asset types
- [ ] output paths cover both `evals/skills/` and `evals/commands/`

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-3

Goal: the skill stays tool-neutral instead of binding the workflow to Claude-specific conventions.

Success Criteria:

- [ ] `SKILL.md` does not mention `Claude Code`
- [ ] `SKILL.md` does not require `.claude/` as the storage root

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill still promotes deterministic validation as the default path.

Success Criteria:

- [ ] grader preference is ordered as code, rule, model, human
- [ ] the skill recommends code-based graders whenever possible

Graders:

- Code: `python3 scripts/validate_assets.py`

### regression-2

Goal: the skill remains concise and keeps examples out of the main workflow file.

Success Criteria:

- [ ] examples live in `references/templates.md`
- [ ] `SKILL.md` links to the reference file instead of duplicating long examples

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
