# Data Migration Specialist Review Checklist

适用范围：当 `SCOPE_MIGRATIONS=true`
输出格式：每行一个 JSON finding。Schema：
`{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"data-migration","summary":"...","fix":"...","fingerprint":"path:line:data-migration","specialist":"data-migration"}`

如果没有发现：只输出 `NO FINDINGS`，不要输出别的内容。

---

## 审查类别

### 可回滚性
- 这个 migration 能否在不丢数据的前提下回滚？
- 是否存在对应的 down / rollback migration？
- rollback 是否真的撤销了变更，而不是空操作？
- 回滚后会不会把当前应用代码直接搞坏？

### 数据丢失风险
- 删除仍有数据的列，应该先做 deprecation period
- 改字段类型可能截断数据（如 `varchar(255) -> varchar(50)`）
- 删表前没有确认代码里已经完全无引用
- 改列名却没同步所有引用（ORM、raw SQL、views）
- 给已有 NULL 数据的列加 `NOT NULL`，却没先 backfill

### 锁持有时长
- 大表上做 `ALTER TABLE`，却没用 `CONCURRENTLY`（PostgreSQL）
- 大于 100K 行的表加索引，但没 `CONCURRENTLY`
- 多条 `ALTER TABLE` 本可合并成一次锁获取
- 高峰流量时执行会拿独占锁的 schema change

### Backfill 策略
- 新 `NOT NULL` 列没有 `DEFAULT` 值，需要先 backfill 再加约束
- 新列默认值依赖计算，需要批量回填
- 缺少面向存量记录的 backfill script 或 rake task
- backfill 一次性 update 全表，而不是批处理，容易锁表

### 索引创建
- 生产表上 `CREATE INDEX` 却没 `CONCURRENTLY`
- 重复索引，新索引覆盖了已有索引的同一列组合
- 新 foreign key 列缺索引
- partial index 与 full index 的选择不合理

### 多阶段发布安全
- migration 只能按特定顺序配合应用代码发布
- schema change 会直接打断当前线上代码，应该先发代码、再迁移
- migration 默认存在 deploy boundary，但旧代码 + 新 schema 会 crash
- rolling deploy 期间需要 feature flag，却没有提供
