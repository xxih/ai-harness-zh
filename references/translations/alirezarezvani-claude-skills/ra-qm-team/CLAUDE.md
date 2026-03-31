# Regulatory Affairs & Quality Management Skills - Claude Code Guidance

本指南覆盖 12 个面向 HealthTech / MedTech 公司的生产级 RA/QM 合规 skill。

## RA/QM Skills 概览

**Strategic Leadership（2 个 skills）：**

- `regulatory-affairs-head`：法规战略、监管情报、主管机构关系
- `quality-manager-qmr`：QMS 监督、管理评审、质量文化

**Quality Systems（3 个 skills）：**

- `quality-manager-qms-iso13485`：ISO 13485 合规、流程管理
- `capa-officer`：CAPA 体系管理、根因分析
- `quality-documentation-manager`：DHF、DMR、DHR 管理

**Risk & Security（2 个 skills）：**

- `risk-management-specialist`：ISO 14971 合规、风险分析
- `information-security-manager-iso27001`：ISO 27001、数据保护、ISMS

**Regulatory Specialists（2 个 skills）：**

- `mdr-745-specialist`：EU MDR 2017/745 合规、技术文档
- `fda-consultant-specialist`：FDA 510(k)、PMA、QSR 合规

**Audit & Compliance（3 个 skills）：**

- `qms-audit-expert`：内审、ISO 13485 认证
- `isms-audit-expert`：ISO 27001 审计、安全评估
- `gdpr-dsgvo-expert`：GDPR / DSGVO 合规、数据隐私

**总计：** 面向医疗器械行业的 12 个专业合规 skill

## Compliance Frameworks

### ISO 13485（医疗器械质量管理）

**负责 skill：** `quality-manager-qms-iso13485`、`qms-audit-expert`

**关键领域：**

- 管理职责
- 资源管理
- 产品实现
- 测量、分析与改进

**工具：**

- QMS process mapping
- 文档控制系统
- 变更管理工作流

### ISO 14971（医疗器械风险管理）

**负责 skill：** `risk-management-specialist`

**关键领域：**

- 风险分析与评估
- 风险控制措施
- 剩余风险评估
- 风险管理评审

**工具：**

- 风险评估模板
- FMEA / FMECA 分析
- 风险收益分析

### MDR 2017/745（欧盟医疗器械法规）

**负责 skill：** `mdr-745-specialist`

**关键领域：**

- 技术文档（Annex II、III）
- 临床评价（Annex XIV）
- 上市后监督
- UDI（Unique Device Identification）

### FDA Regulations（美国医疗器械合规）

**负责 skill：** `fda-consultant-specialist`

**关键领域：**

- 510(k) premarket notification
- PMA（Premarket Approval）
- QSR（Quality System Regulation）
- 上市后报告

### ISO 27001（信息安全管理）

**负责 skill：** `information-security-manager-iso27001`、`isms-audit-expert`

**关键领域：**

- ISMS 建立与维护
- 风险评估与处置
- 安全控制（Annex A）
- 持续改进

### GDPR / DSGVO（数据保护）

**负责 skill：** `gdpr-dsgvo-expert`

**关键领域：**

- 数据保护影响评估（DPIA）
- Privacy by design
- 数据主体权利
- 泄露通报

## Regulatory Workflows

### Workflow 1: 新医疗器械开发

```text
1. 风险管理（ISO 14971） → risk-management-specialist
2. QMS 流程搭建（ISO 13485） → quality-manager-qms-iso13485
3. 技术文档（MDR） → mdr-745-specialist
4. FDA 提交 → fda-consultant-specialist
5. 临床评价 → regulatory-affairs-head
```

### Workflow 2: QMS Audit Preparation

```text
1. Internal Audit → qms-audit-expert
2. CAPA Implementation → capa-officer
3. Document Review → quality-documentation-manager
4. Management Review → quality-manager-qmr
5. Certification Audit → qms-audit-expert
```

### Workflow 3: Data Protection Compliance

```text
1. GDPR Assessment → gdpr-dsgvo-expert
2. ISMS Implementation → information-security-manager-iso27001
3. Security Audit → isms-audit-expert
4. Continuous Monitoring → information-security-manager-iso27001
```

## 集成模式

**RA/QM ↔ Engineering：** 法规要求会反向塑造技术设计决策  
**RA/QM ↔ Product：** 合规要求会影响产品特性与 roadmap  
**RA/QM ↔ Security：** ISO 27001 与安全工程实践对齐

## Additional Resources

- **RA/QM Overview:** `README.md`
- **Complete Skills Collection:** `final-complete-skills-collection.md`
- **Start Here:** `START_HERE.md`（若存在）
- **Main Documentation:** `../CLAUDE.md`

---

**Last Updated:** November 5, 2025  
**Skills Deployed:** 12/12 RA/QM skills production-ready  
**Focus:** Medical device compliance（ISO 13485、MDR、FDA、ISO 27001、GDPR）
