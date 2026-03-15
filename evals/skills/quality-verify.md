# Asset Eval: quality-verify

## Asset Under Test

- Type: skill
- Path: src/skills/quality-verify/SKILL.md
- Goal: translate and absorb the superpowers completion-verification gate into a Chinese, reusable quality skill.

## Capability Evals

### capability-1

Goal: the skill enforces evidence before completion claims.

Success Criteria:

- [ ] `SKILL.md` states that `ready` requires fresh verification evidence
- [ ] `SKILL.md` states that missing fresh evidence means `not-ready`
- [ ] `SKILL.md` describes identify-run-read-verify-claim or an equivalent gate sequence

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill guards against common false-completion patterns.

Success Criteria:

- [ ] `SKILL.md` rejects partial verification as sufficient evidence
- [ ] `SKILL.md` explicitly warns against wording such as “应该可以” or “看起来没问题”
- [ ] `SKILL.md` includes build/tests/diff or equivalent verification scope

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill stays reusable rather than being tied to one harness runtime.

Success Criteria:

- [ ] the skill body is primarily in Chinese
- [ ] `SKILL.md` does not require a specific agent runtime
- [ ] `SKILL.md` defines a durable output strategy without requiring `nanospec`
- [ ] `SKILL.md` uses a project-local default output path such as `output/quality/quality-check.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
