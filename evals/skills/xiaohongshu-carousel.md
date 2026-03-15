# Asset Eval: xiaohongshu-carousel

## Asset Under Test

- Type: skill
- Path: src/skills/xiaohongshu-carousel/SKILL.md
- Goal: provide a repeatable workflow for turning existing Chinese content into publishable Xiaohongshu carousel images and renderable source files.

## Capability Evals

### capability-1

Goal: the skill stays focused on repackaging existing content rather than pre-production.

Success Criteria:

- [ ] `SKILL.md` explicitly targets existing content
- [ ] `SKILL.md` explicitly excludes 选题、定位、竞品、前期策划

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-2

Goal: the skill defines concrete output artifacts for publishable delivery.

Success Criteria:

- [ ] `SKILL.md` requires a markdown source file such as `slides.md`
- [ ] `SKILL.md` treats `source.json` as generated structure instead of the primary authoring format
- [ ] `SKILL.md` requires PNG outputs
- [ ] `SKILL.md` requires HTML or SVG source files as fallback or source of truth
- [ ] `SKILL.md` requires a `manifest.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-3

Goal: the skill captures Xiaohongshu-friendly readability and page structure.

Success Criteria:

- [ ] `SKILL.md` specifies `1242x1660`
- [ ] `SKILL.md` specifies `3:4`
- [ ] `SKILL.md` requires cover,正文结构,结尾页等关键页面角色

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-4

Goal: the skill protects factual accuracy during repackaging.

Success Criteria:

- [ ] `SKILL.md` forbids inventing facts not supported by the source
- [ ] `SKILL.md` requires preserving process order and technical accuracy

Graders:

- Code: `python3 scripts/validate_assets.py`

### capability-5

Goal: the skill supports reusable generation instead of one-off hand-crafted pages.

Success Criteria:

- [ ] `SKILL.md` references a reusable build script
- [ ] `SKILL.md` requires markdown-to-HTML generation
- [ ] `SKILL.md` treats `layout: markdown` as the default body-page authoring mode
- [ ] `SKILL.md` requires theme switching instead of duplicating ad-hoc page files

Graders:

- Code: `python3 scripts/validate_assets.py`

## Regression Evals

### regression-1

Goal: the skill remains Chinese-first and repository-aligned.

Success Criteria:

- [ ] the skill body is primarily in Chinese
- [ ] detailed page templates live in `references/` instead of bloating `SKILL.md`

Graders:

- Code: `python3 scripts/validate_assets.py`

### regression-2

Goal: the skill keeps a reusable output layout for downstream automation.

Success Criteria:

- [ ] outputs are organized under `output/xiaohongshu/<topic>/`
- [ ] generated files use numbered page naming such as `slide-01`
- [ ] the skill requires multiple visual styles or themes
- [ ] detailed theme guidance lives in `references/`
- [ ] markdown authoring guidance lives in `references/`

Graders:

- Code: `python3 scripts/validate_assets.py`

## Exit Criteria

- Capability evals: all pass in the current repository state
- Regression evals: all pass in the current repository state
- Report: validation command exits with status `0`
