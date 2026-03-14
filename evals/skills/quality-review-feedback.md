# Asset Eval: quality-review-feedback

## Asset Under Test

- Type: skill
- Path: skills/quality-review-feedback/SKILL.md
- Goal: translate and absorb the superpowers review-reception discipline into a Chinese, reusable quality skill.

## Capability Evals

### capability-1

Goal: the skill requires technical verification before acting on review feedback.

Success Criteria:

- [ ] `SKILL.md` describes read-understand-verify-evaluate-respond-implement or an equivalent flow
- [ ] `SKILL.md` forbids performative agreement before verification
- [ ] `SKILL.md` requires clarifying unclear feedback before implementation

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill preserves skeptical handling of external review suggestions.

Success Criteria:

- [ ] `SKILL.md` states that external feedback is to be evaluated, not blindly followed
- [ ] `SKILL.md` includes pushback conditions such as breaking existing behavior or violating YAGNI
- [ ] `SKILL.md` defines a durable output strategy without requiring `nanospec`
- [ ] `SKILL.md` uses a project-local default output path such as `output/quality/quality-check.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill stays professional and reusable in Chinese.

Success Criteria:

- [ ] the skill body is primarily in Chinese
- [ ] `SKILL.md` is about code review feedback rather than general communication etiquette
- [ ] `SKILL.md` does not depend on GitHub-specific automation to be useful
- [ ] `SKILL.md` does not require `nanospec/<task>/...` as its output path

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
