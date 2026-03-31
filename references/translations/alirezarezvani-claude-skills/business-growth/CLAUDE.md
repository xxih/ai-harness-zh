# Business & Growth Skills - Claude Code Guidance

本指南覆盖 3 个可用于生产环境的 business & growth skills 及其 Python 自动化工具。

## Business & Growth Skills 概览

**可用 skills：**

1. **customer-success-manager/**：客户健康度评分、流失风险分析、扩张机会（3 个 Python 工具）
2. **sales-engineer/**：技术调研、RFP 分析、竞品定位、POC 规划（3 个 Python 工具）
3. **revenue-operations/**：pipeline 分析、预测准确率、GTM 效率指标（3 个 Python 工具）

**工具总数：** 9 个 Python 自动化工具、9 份知识库、19+ 模板

## Python 自动化工具

### Customer Success Manager

#### 1. Health Score Calculator

`customer-success-manager/scripts/health_score_calculator.py`

**用途：** 多维客户健康度评分，并支持趋势分析

**功能：**

- 基于 4 个维度的加权评分：usage、engagement、support、relationship
- 可配置阈值的红/黄/绿分类
- 当前周期与上一周期的趋势对比
- 针对 Enterprise / Mid-Market / SMB 的分层基准

**用法：**

```bash
python customer-success-manager/scripts/health_score_calculator.py customer_data.json
python customer-success-manager/scripts/health_score_calculator.py customer_data.json --format json
```

#### 2. Churn Risk Analyzer

`customer-success-manager/scripts/churn_risk_analyzer.py`

**用途：** 识别高风险账户，并给出干预建议

**功能：**

- 基于行为信号的风险评分
- 预警信号识别与分类
- 与客户层级匹配的干预 playbook
- 按紧急程度排序

**用法：**

```bash
python customer-success-manager/scripts/churn_risk_analyzer.py customer_data.json
python customer-success-manager/scripts/churn_risk_analyzer.py customer_data.json --format json
```

#### 3. Expansion Opportunity Scorer

`customer-success-manager/scripts/expansion_opportunity_scorer.py`

**用途：** 识别 upsell 与 cross-sell 机会

**功能：**

- 跨产品模块的采用深度分析
- 未使用特性的 whitespace mapping
- 收入机会估算
- 基于投入与影响的优先级排序

**用法：**

```bash
python customer-success-manager/scripts/expansion_opportunity_scorer.py customer_data.json
python customer-success-manager/scripts/expansion_opportunity_scorer.py customer_data.json --format json
```

### Sales Engineer

#### 4. RFP Response Analyzer

`sales-engineer/scripts/rfp_response_analyzer.py`

**用途：** 为 RFP/RFI 覆盖情况打分并识别缺口

**功能：**

- 需求覆盖评分（Full / Partial / Planned / Gap）
- 各需求项的投入估算
- 缺口识别与缓解策略
- 最终 bid / no-bid 建议

**用法：**

```bash
python sales-engineer/scripts/rfp_response_analyzer.py rfp_data.json
python sales-engineer/scripts/rfp_response_analyzer.py rfp_data.json --format json
```

#### 5. Competitive Matrix Builder

`sales-engineer/scripts/competitive_matrix_builder.py`

**用途：** 生成功能对比矩阵与竞争定位

**功能：**

- 逐功能对比矩阵
- 带权重的竞品评分
- 差异化优势识别
- 可直接用于 battlecard 的输出

**用法：**

```bash
python sales-engineer/scripts/competitive_matrix_builder.py competitive_data.json
python sales-engineer/scripts/competitive_matrix_builder.py competitive_data.json --format json
```

#### 6. POC Planner

`sales-engineer/scripts/poc_planner.py`

**用途：** 规划 proof-of-concept 项目

**功能：**

- 基于范围的时间线估算
- 资源分配规划
- 成功标准定义
- 评估 scorecard 生成

**用法：**

```bash
python sales-engineer/scripts/poc_planner.py poc_data.json
python sales-engineer/scripts/poc_planner.py poc_data.json --format json
```

### Revenue Operations

#### 7. Pipeline Analyzer

`revenue-operations/scripts/pipeline_analyzer.py`

**用途：** 分析销售 pipeline 的健康度与速度

**功能：**

- Coverage ratio（pipeline / quota）
- 各 stage 转化率分析
- 销售速度指标（4-lever model）
- Deal aging 分析

**用法：**

```bash
python revenue-operations/scripts/pipeline_analyzer.py pipeline_data.json
python revenue-operations/scripts/pipeline_analyzer.py pipeline_data.json --format json
```

#### 8. Forecast Accuracy Tracker

`revenue-operations/scripts/forecast_accuracy_tracker.py`

**用途：** 衡量并改进预测准确率

**功能：**

- MAPE 计算
- 预测偏差识别（高估 / 低估）
- 周期趋势分析
- 按类别拆解准确率

**用法：**

```bash
python revenue-operations/scripts/forecast_accuracy_tracker.py forecast_data.json
python revenue-operations/scripts/forecast_accuracy_tracker.py forecast_data.json --format json
```

#### 9. GTM Efficiency Calculator

`revenue-operations/scripts/gtm_efficiency_calculator.py`

**用途：** 计算 go-to-market 效率指标

**功能：**

- Magic number 计算
- LTV:CAC 比率分析
- CAC payback period
- Burn multiple 评估
- 行业 benchmark 对比

**用法：**

```bash
python revenue-operations/scripts/gtm_efficiency_calculator.py gtm_data.json
python revenue-operations/scripts/gtm_efficiency_calculator.py gtm_data.json --format json
```

## 质量标准

**所有 business & growth Python 工具都必须：**

- 只依赖标准库
- 通过 `--format` 同时支持 JSON 与人类可读输出
- 对非法输入给出清晰错误信息
- 返回正确退出码
- 只在本地处理文件，不做 API 调用
- 使用 `argparse`，并支持 `--help`

## 相关 Skills

- **Marketing：** 内容创作、需求生成 → `../marketing-skill/`
- **Product Team：** 用户研究、特性优先级 → `../product-team/`
- **C-Level：** 战略规划 → `../c-level-advisor/`
- **Engineering：** 技术实施 → `../engineering-team/`

---

**Last Updated:** February 2026  
**Skills Deployed:** 3/3 business & growth skills production-ready  
**Total Tools:** 9 Python automation tools
