# Asset Eval: spec-driven

## Asset Under Test

- Type: skill
- Path: src/domains/workflow/skills/spec-driven/SKILL.md
- Goal: provide a pure task-container convention with alignment-first correction rules, without bundling built-in phase routing.

## Capability Evals

### capability-1

Goal: the skill defines a stable task container for cross-skill collaboration.

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

Goal: the skill stays pure and leaves stage execution to other skills.

Success Criteria:

- [ ] `SKILL.md` says it only provides directory structure and align
- [ ] `SKILL.md` explicitly does not provide built-in `init` / `clarify` / `spec` / `plan` / `execute` / `accept` / `summary` / `onboard` / `run`
- [ ] `SKILL.md` says phase-specific work is handled by other skills

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill stays repository-local and does not require an external CLI.

Success Criteria:

- [ ] `SKILL.md` does not require `nanospec` CLI as a prerequisite
- [ ] `SKILL.md` allows direct file creation as the fallback path

Graders:

- Code: `python3 scripts/validate_assets.py`

### regression-2

Goal: the skill does not re-grow into a full workflow router.

Success Criteria:

- [ ] `SKILL.md` does not document slash-command routing such as `/init` or `/run`
- [ ] `SKILL.md` stays focused on structure, shared work surfaces, and align

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
