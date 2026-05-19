---
name: setup-pre-commit
description: 在当前仓库配 Husky pre-commit hook + lint-staged(Prettier)+ 类型检查 + 测试。当用户想加 pre-commit hook、配 Husky、配 lint-staged,或加提交时格式化/类型检查/测试时使用。
---

# Setup Pre-Commit Hooks

> 原文:[skills/misc/setup-pre-commit/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/misc/setup-pre-commit/SKILL.md)

## 这个 skill 配了什么

- **Husky** pre-commit hook
- **lint-staged** 对所有 staged 文件跑 Prettier
- **Prettier** 配置(如缺失)
- pre-commit hook 里跑 **typecheck** 和 **test** 脚本

## 步骤

### 1. 检测 package manager

查 `package-lock.json`(npm)、`pnpm-lock.yaml`(pnpm)、`yarn.lock`(yarn)、`bun.lockb`(bun)。哪个在用哪个。**不清楚就用 npm**。

### 2. 装依赖

作为 devDependencies 装:

```
husky lint-staged prettier
```

### 3. 初始化 Husky

```bash
npx husky init
```

会建 `.husky/` 目录并往 package.json 加 `prepare: "husky"`。

### 4. 建 `.husky/pre-commit`

写这份文件(Husky v9+ 不需要 shebang):

```
npx lint-staged
npm run typecheck
npm run test
```

**适配**:把 `npm` 替换成检测到的 package manager。如果 package.json 里没有 `typecheck` 或 `test` 脚本,**省掉对应行并告知用户**。

### 5. 建 `.lintstagedrc`

```json
{
  "*": "prettier --ignore-unknown --write"
}
```

### 6. 建 `.prettierrc`(如缺失)

**只在没有 Prettier 配置时建**。用默认:

```json
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 80,
  "singleQuote": false,
  "trailingComma": "es5",
  "semi": true,
  "arrowParens": "always"
}
```

### 7. 验证

- [ ] `.husky/pre-commit` 存在且可执行
- [ ] `.lintstagedrc` 存在
- [ ] package.json 里 `prepare` 脚本是 `"husky"`
- [ ] Prettier 配置存在
- [ ] 跑 `npx lint-staged` 验证能跑

### 8. Commit

把所有改动/新建文件 stage 并提交,信息:`Add pre-commit hooks (husky + lint-staged + prettier)`

这次提交会走新 pre-commit hook —— **是一个不错的冒烟测试**。

## 注

- Husky v9+ 的 hook 文件不需要 shebang
- `prettier --ignore-unknown` 跳过 Prettier 解析不了的文件(图片等)
- pre-commit 先跑 lint-staged(快、只对 staged),然后全量 typecheck + test
