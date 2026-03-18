# superpowers 中文翻译

## 当前范围

- 源仓库：`references/repos/superpowers`
- 当前先覆盖：`skills/*/SKILL.md`
- 暂不覆盖：
  - `skills/*/references/*`
  - `skills/*/*-prompt.md`
  - `agents/`、`commands/`、`hooks/` 等其他目录

## 同步规则

维护 `superpowers` 中文翻译前，先运行：

```bash
python3 scripts/reference_translation_sync.py check superpowers --pull
```

如果提示 `STALE`：

1. 查看 upstream commit 是否变化
2. 查看哪些 `skills/*/SKILL.md` 发生了内容漂移
3. 同步修改本目录下对应中文文件
4. 运行 `python3 scripts/reference_translation_sync.py snapshot superpowers`

## 说明

- 中文翻译尽量保持 prompt 约束、流程顺序和强弱语气一致
- skill 名称、路径、命令、代码块和协议关键字保持原文
- 如果某段更适合保留英文原文（例如命令示例、路径、占位符），优先保留原文
