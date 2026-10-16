# 来源清单

导出时间：2026-10-14

## 时间管理规则

本能力包不使用版本号。

判断新旧只看导出时间。每次重新导出时，更新本文件和入口文件中的导出时间。

## 导出对象

开发治理能力包。

## 导出目标

```text
14-exports/developer-kit/
```

## 来源项目

```text
WorkflowProject
```

## 导出范围

### 工作流

| 导出目录 | 来源 |
| --- | --- |
| `workflows/developer/` | `04-workflows/developer/` |
| `workflows/common/iteration-memory-management-workflow.md` | `04-workflows/common/iteration-memory-management-workflow.md` |

其中 `workflows/developer/developer-kit-workflow.md` 是开发治理总入口工作流，负责判断任务类型并调度细分工作流。

它不只是单点分流器，还负责按开发生命周期判断后续阶段：

```text
需求理解 -> 开发确认 -> 项目理解 -> 功能规划 -> 契约/安全检查 -> 实现 -> 验证 -> 文档 -> 评审 -> 发布或复盘
```

本次导出包含新增的真实开发协同能力：

```text
issue-diagnosis-workflow.md
data-api-contract-workflow.md
security-permission-workflow.md
workflow-orchestration-guide.md
minimal-change-governance-workflow.md
```

其中 `minimal-change-governance-workflow.md` 融合 Ponytail 的最小必要变更思想，用于实现前和评审时避免过度设计、过早抽象和不必要依赖。

### 角色

| 导出目录 | 来源 |
| --- | --- |
| `roles/role-definition.md` | `02-roles/developer/role-definition.md` |
| `roles/minimal-change-guardian.md` | `02-roles/developer/minimal-change-guardian.md` |

### 模板

| 导出目录 | 来源 |
| --- | --- |
| `templates/developer/` | `06-templates/developer/` |
| `templates/common/iteration-memory-summary-template.md` | `06-templates/common/iteration-memory-summary-template.md` |

### 评分表

| 导出目录 | 来源 |
| --- | --- |
| `scorecards/` | `11-evaluations/output-scorecards/` 中开发治理相关评分表 |

### 知识

| 导出文件 | 来源 |
| --- | --- |
| `knowledge/developer-governance-capability-system.md` | `10-knowledge-base/patterns/developer-governance-capability-system.md` |
| `knowledge/ponytail-minimal-change-principles.md` | `10-knowledge-base/patterns/ponytail-minimal-change-principles.md` |

### 使用体验层

| 导出文件 | 作用 |
| --- | --- |
| `INSTALL.md` | 外部项目首次接入说明 |
| `examples/quick-start-example.md` | 快速启动示例 |
| `integrations/codex-usage.md` | Codex 使用说明 |
| `integrations/cursor-usage.md` | Cursor 使用说明 |

## 未导出内容

以下内容没有直接导出：

- `12-projects/` 中的项目过程材料。
- `15-dashboard/` React 可视化控制台。
- `13-visual-maps/` XMind 导图。
- `99-archive/` 历史归档。
- 其他角色能力。

## 原因

本能力包目标是独立使用开发治理能力，不复制整个 WorkflowProject。

项目过程材料只适合作为案例和复盘，不适合作为能力包主体。

## 后续维护方式

当 WorkflowProject 中以下内容变化时，应重新导出：

- `04-workflows/developer/`
- `06-templates/developer/`
- `11-evaluations/output-scorecards/` 中开发治理评分表
- `10-knowledge-base/patterns/developer-governance-capability-system.md`
- `04-workflows/common/iteration-memory-management-workflow.md`
- `06-templates/common/iteration-memory-summary-template.md`

重新导出后更新本文件的导出时间和来源清单。
