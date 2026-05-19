# 为 gstack 增加一个新的 Host

gstack 使用声明式 host config 系统。每个受支持的 AI coding agent
（Claude、Codex、Factory、Kiro、OpenCode、Slate、Cursor、OpenClaw）
都定义为一个带类型的 TypeScript config object。新增一个 host 只需要创建
一个文件并重新导出它。generator、setup 或 tooling 都不需要额外改代码。

## 工作方式

```
hosts/
├── claude.ts        # Primary host
├── codex.ts         # OpenAI Codex CLI
├── factory.ts       # Factory Droid
├── kiro.ts          # Amazon Kiro
├── opencode.ts      # OpenCode
├── slate.ts         # Slate (Random Labs)
├── cursor.ts        # Cursor
├── openclaw.ts      # OpenClaw (hybrid: config + adapter)
└── index.ts         # Registry: imports all, derives Host type
```

每个 config 文件都会导出一个 `HostConfig` object，告诉 generator：

- 生成后的 skills 应该放到哪里
- frontmatter 应该如何变换（allowlist/denylist fields）
- 哪些 Claude-specific 引用需要改写（路径、tool names）
- 自动安装时要检测哪个 binary
- 哪些 resolver sections 需要 suppress
- 安装时哪些资产要 symlink

generator、setup script、platform-detect、uninstall、health checks、worktree
copy 和 tests 都会读取这些 config。它们内部都没有 per-host code。

## 分步操作：添加一个新 host

### 1. 创建 config 文件

先复制一个现有 config 当起点。`hosts/opencode.ts` 是一个比较精简的示例。
`hosts/factory.ts` 展示了 tool rewrites 和 conditional fields。
`hosts/openclaw.ts` 展示了 host 的 tool model 不同时该如何使用 adapter pattern。

创建 `hosts/myhost.ts`：

```typescript
import type { HostConfig } from '../scripts/host-config';

const myhost: HostConfig = {
  name: 'myhost',
  displayName: 'MyHost',
  cliCommand: 'myhost',        // `command -v` 检测时使用的 binary name
  cliAliases: [],              // 可选的备用 binary names

  globalRoot: '.myhost/skills/gstack',
  localSkillRoot: '.myhost/skills/gstack',
  hostSubdir: '.myhost',
  usesEnvVars: true,           // 只有 Claude 为 false（它使用字面量 ~ 路径）

  frontmatter: {
    mode: 'allowlist',         // 'allowlist' 只保留列出的 fields
    keepFields: ['name', 'description'],
    descriptionLimit: null,    // 有长度限制的 host 可设为 1024
  },

  generation: {
    generateMetadata: false,   // 只有 Codex 为 true（openai.yaml）
    skipSkills: ['codex'],     // codex skill 是 Claude-only
  },

  pathRewrites: [
    { from: '~/.claude/skills/gstack', to: '~/.myhost/skills/gstack' },
    { from: '.claude/skills/gstack', to: '.myhost/skills/gstack' },
    { from: '.claude/skills', to: '.myhost/skills' },
  ],

  runtimeRoot: {
    globalSymlinks: ['bin', 'browse/dist', 'browse/bin', 'gstack-upgrade', 'ETHOS.md'],
    globalFiles: { 'review': ['checklist.md', 'TODOS-format.md'] },
  },

  install: {
    prefixable: false,
    linkingStrategy: 'symlink-generated',
  },

  learningsMode: 'basic',
};

export default myhost;
```

### 2. 在 index 中注册

编辑 `hosts/index.ts`：

```typescript
import myhost from './myhost';

// Add to ALL_HOST_CONFIGS array:
export const ALL_HOST_CONFIGS: HostConfig[] = [
  claude, codex, factory, kiro, opencode, slate, cursor, openclaw, myhost
];

// Add to re-exports:
export { claude, codex, factory, kiro, opencode, slate, cursor, openclaw, myhost };
```

### 3. 更新 .gitignore

把 `.myhost/` 加进 `.gitignore`（生成出来的 skill docs 默认不提交）。

### 4. 生成并验证

```bash
# 为新 host 生成 skill docs
bun run gen:skill-docs --host myhost

# 验证输出存在，且没有 .claude/skills 泄漏
ls .myhost/skills/gstack-*/SKILL.md
grep -r ".claude/skills" .myhost/skills/ | head -5
# （应为空）

# 为所有 hosts 生成（包含新 host）
bun run gen:skill-docs --host all

# Health dashboard 会显示新 host
bun run skill:check
```

### 5. 跑测试

```bash
bun test test/gen-skill-docs.test.ts
bun test test/host-config.test.ts
```

这些参数化 smoke tests 会自动拾取新 host。测试代码本身不需要改。它们会验证：
输出存在、没有 path leakage、frontmatter 合法、freshness check 通过、`codex`
skill 被正确排除。

### 6. 更新 README.md

在合适的章节里补上新 host 的安装说明。

## Config field 参考

完整的 `HostConfig` interface 以及每个 field 的 JSDoc 说明，见
`scripts/host-config.ts`。

关键字段：

| Field | Purpose |
|-------|---------|
| `frontmatter.mode` | `allowlist`（只保留列出的）或 `denylist`（移除列出的） |
| `frontmatter.descriptionLimit` | 最大字符数，`null` 表示不限 |
| `frontmatter.descriptionLimitBehavior` | `error`（构建失败）、`truncate`、`warn` |
| `frontmatter.conditionalFields` | 根据模板值追加 fields（例如 `sensitive` → `disable-model-invocation`） |
| `frontmatter.renameFields` | 重命名模板字段（例如 `voice-triggers` → `triggers`） |
| `pathRewrites` | 对内容做字面量 `replaceAll`。顺序有影响。 |
| `toolRewrites` | 改写 Claude tool names（例如 `"use the Bash tool"` → `"run this command"`） |
| `suppressedResolvers` | 对当前 host 返回空结果的 resolver functions |
| `coAuthorTrailer` | Git co-author string |
| `boundaryInstruction` | 跨模型调用时的 anti-prompt-injection warning |
| `adapter` | 用于复杂变换的 adapter module 路径 |

## Adapter pattern（适用于 tool model 明显不同的 host）

如果简单的字符串替换不足以处理 tool rewrites（也就是 host 的 tool semantics
本质上就不同），请使用 adapter pattern。参考 `hosts/openclaw.ts` 与
`scripts/host-adapters/openclaw-adapter.ts`。

adapter 会在所有通用 rewrites 之后作为 post-processing step 运行。它导出：

`transform(content: string, config: HostConfig): string`

## Validation

`scripts/host-config.ts` 中的 `validateHostConfig()` 会检查：

- Name：只允许小写字母、数字和连字符
- CLI command：只允许字母数字、连字符和下划线
- Paths：只允许安全字符（字母数字、`.`、`/`、`$`、`{}`、`~`、`-`、`_`）
- 所有 configs 之间不允许重复的 names、hostSubdirs 或 globalRoots

运行下面的命令可校验全部 configs：

```bash
bun run scripts/host-config-export.ts validate
```
