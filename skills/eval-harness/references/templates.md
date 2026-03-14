# Eval Templates

## Skill Eval Definition

```md
# Asset Eval: <asset-name>

## Asset Under Test

- Type: skill | command
- Path: skills/<name>/SKILL.md | commands/<name>.md
- Goal: one-sentence summary

## Capability Evals

### capability-1

Goal: describe the new capability.

Success Criteria:

- [ ] criterion 1
- [ ] criterion 2

Graders:

- Code: deterministic command or script
- Rule: optional regex or schema check
- Model: optional quality review prompt

## Regression Evals

### regression-1

Goal: describe what must not break.

Success Criteria:

- [ ] preserved behavior 1
- [ ] preserved behavior 2

Graders:

- Code: deterministic command or script

## Exit Criteria

- Capability evals: pass@3 >= target
- Regression evals: pass^3 = target
- Report: short conclusion with residual risks
```

## Verification Report

```md
# Eval Report: <asset-name>

## Summary

- Asset: <path>
- Result: READY | BLOCKED

## Capability Evals

- capability-1: PASS
- capability-2: FAIL

## Regression Evals

- regression-1: PASS

## Metrics

- pass@1: 0.50
- pass@3: 1.00

## Risks

- one concise risk per line
```

## Grader Preference

1. Code grader
2. Rule grader
3. Model grader
4. Human review
