# Finance Skills - Claude Code Guidance

本指南覆盖 finance skills 及其 Python 自动化工具。

## Finance Skills 概览

**可用 skills：**

1. **financial-analyst/**：财报分析、比率分析、DCF 估值、预算与预测（4 个 Python 工具）
2. **saas-metrics-coach/**：SaaS 财务健康分析，包括 ARR、MRR、churn、CAC、LTV、NRR、Quick Ratio、12 个月预测（3 个 Python 工具）

**工具总数：** 7 个 Python 自动化工具、5 份知识库、6 个模板

**Commands：** 2 个（`/financial-health`、`/saas-health`）

## Python 自动化工具

### 1. Ratio Calculator

`financial-analyst/scripts/ratio_calculator.py`

**用途：** 根据报表数据计算并解释财务比率

**功能：**

- 盈利能力指标（ROE、ROA、Gross / Operating / Net Margin）
- 流动性指标（Current、Quick、Cash）
- 杠杆指标（Debt-to-Equity、Interest Coverage、DSCR）
- 效率指标（Asset / Inventory / Receivables Turnover、DSO）
- 估值指标（P/E、P/B、P/S、EV/EBITDA、PEG）
- 内置解释与 benchmark

**用法：**

```bash
python financial-analyst/scripts/ratio_calculator.py financial_data.json
python financial-analyst/scripts/ratio_calculator.py financial_data.json --format json
```

### 2. DCF Valuation

`financial-analyst/scripts/dcf_valuation.py`

**用途：** 基于 Discounted Cash Flow 计算企业价值与股权价值

**功能：**

- 收入与现金流预测
- WACC 计算（基于 CAPM）
- 终值计算（永续增长法与退出倍数法）
- 企业价值与股权价值推导
- 双变量敏感性分析
- 无外部依赖，仅使用 `math` / `statistics`

**用法：**

```bash
python financial-analyst/scripts/dcf_valuation.py valuation_data.json
python financial-analyst/scripts/dcf_valuation.py valuation_data.json --format json
```

### 3. Budget Variance Analyzer

`financial-analyst/scripts/budget_variance_analyzer.py`

**用途：** 分析 actual、budget 与 prior year 之间的偏差

**功能：**

- 偏差计算（actual vs budget、actual vs prior year）
- 重大性阈值过滤
- 有利 / 不利分类
- 按部门与类别拆解

**用法：**

```bash
python financial-analyst/scripts/budget_variance_analyzer.py budget_data.json
python financial-analyst/scripts/budget_variance_analyzer.py budget_data.json --format json
```

### 4. Forecast Builder

`financial-analyst/scripts/forecast_builder.py`

**用途：** 基于 driver 的收入预测与现金流投影

**功能：**

- 基于 driver 的收入预测模型
- 13 周现金流预测
- 情景建模（base / bull / bear）
- 基于历史数据的趋势分析

**用法：**

```bash
python financial-analyst/scripts/forecast_builder.py forecast_data.json
python financial-analyst/scripts/forecast_builder.py forecast_data.json --format json
```

## 质量标准

**所有 finance Python 工具都必须：**

- 只依赖标准库（`math`、`statistics`、`json`、`argparse`）
- 通过 `--format` 同时支持 JSON 与人类可读输出
- 对非法输入给出清晰错误信息
- 返回正确退出码
- 只做本地文件处理，不发起 API 调用
- 使用 `argparse` 并支持 `--help`

## 相关 Skills

- **C-Level：** 战略财务决策 → `../c-level-advisor/`
- **Business & Growth：** revenue operations、销售指标 → `../business-growth/`
- **Product Team：** 预算分配、RICE scoring → `../product-team/`

---

**Last Updated:** March 2026  
**Skills Deployed:** 2/2 finance skills production-ready  
**Total Tools:** 7 Python automation tools  
**Commands:** /financial-health, /saas-health
