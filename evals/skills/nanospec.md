# Asset Eval: nanospec

## Asset Under Test

- Type: skill
- Path: src/domains/workflow/skills/nanospec/SKILL.md
- Goal: provide a reusable task-container convention with alignment-first correction rules for spec-driven work.

## Capability Evals

### capability-1

Goal: the skill defines a stable task container instead of only a conversational workflow.

Success Criteria:

- [ ] `SKILL.md` defines a concrete `nanospec/<task>/` directory layout
- [ ] `SKILL.md` explains the roles of `assets/` and `outputs/`
- [ ] `SKILL.md` treats `.nanospec/.current` as optional rather than mandatory

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill makes align the default correction mechanism for drift and change.

Success Criteria:

- [ ] `SKILL.md` explicitly requires updating `alignment.md` when drift or change appears
- [ ] `SKILL.md` requires propagating changes to affected outputs
- [ ] `SKILL.md` requires writing follow-up actions back to `outputs/3-tasks.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-3

Goal: the skill supports both lightweight routing and full workflow continuation.

Success Criteria:

- [ ] `SKILL.md` supports direct stage routing such as `/plan`, `/align`, or `/run`
- [ ] `SKILL.md` allows cooperating with other plan, research, or execute skills
- [ ] `SKILL.md` keeps the full spec-driven workflow optional rather than mandatory

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill stays repository-local and does not require an external CLI.

Success Criteria:

- [ ] `SKILL.md` does not require `nanospec` CLI as a prerequisite
- [ ] `SKILL.md` provides a repository-local fallback such as direct file creation or bundled scripts

Graders:

- Code: `python3 scripts/validate_assets.py`

### regression-2

Goal: the skill keeps detailed phase instructions in references instead of bloating the main file.

Success Criteria:

- [ ] `SKILL.md` points to per-stage files under `references/`
- [ ] the main file stays focused on structure, routing, and alignment rules

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
