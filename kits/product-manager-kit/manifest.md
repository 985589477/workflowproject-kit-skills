# 来源清单

导出时间：2026-10-15

## 时间管理规则

本能力包不使用版本号。

判断新旧只看导出时间。每次重新导出时，更新本文件和入口文件中的导出时间。

## 导出对象

产品经理能力包。

## 导出目标

```text
14-exports/product-manager-kit/
```

## 来源项目

```text
WorkflowProject
```

## 导出范围

### 角色定义

| 导出文件 | 来源 |
| --- | --- |
| `roles/role-definition.md` | `02-roles/product-manager/role-definition.md` |

### 工作流

| 导出目录 | 来源 |
| --- | --- |
| `workflows/product-manager/` | `04-workflows/product-manager/` |
| `workflows/common/idea-to-input-workflow.md` | `04-workflows/common/idea-to-input-workflow.md` |
| `workflows/common/input-analysis-workflow.md` | `04-workflows/common/input-analysis-workflow.md` |
| `workflows/common/output-review-workflow.md` | `04-workflows/common/output-review-workflow.md` |
| `workflows/common/iteration-memory-management-workflow.md` | `04-workflows/common/iteration-memory-management-workflow.md` |

### 模板

| 导出目录 | 来源 |
| --- | --- |
| `templates/product-manager/` | `06-templates/product-manager/` |
| `templates/meta/idea-to-input-generator.md` | `06-templates/meta/idea-to-input-generator.md` |
| `templates/meta/output-reviewer.md` | `06-templates/meta/output-reviewer.md` |
| `templates/common/iteration-memory-summary-template.md` | `06-templates/common/iteration-memory-summary-template.md` |

### 评分表

| 导出目录 | 来源 |
| --- | --- |
| `scorecards/` | `11-evaluations/output-scorecards/` 中产品经理相关评分表 |

### 知识

| 导出文件 | 来源 |
| --- | --- |
| `knowledge/product-manager-capability-system.md` | `10-knowledge-base/patterns/product-manager-capability-system.md` |

### 使用体验层

| 导出文件 | 作用 |
| --- | --- |
| `INSTALL.md` | 外部项目首次接入说明 |
| `examples/quick-start-example.md` | 快速启动示例 |
| `integrations/codex-usage.md` | Codex 使用说明 |
| `integrations/cursor-usage.md` | Cursor 使用说明 |
| `SKILL.md` | Codex skill 草稿 |

## 未导出内容

以下内容没有直接导出：

- `12-projects/` 中的项目过程材料。
- `15-dashboard/` React 可视化控制台。
- `13-visual-maps/` XMind 导图。
- `99-archive/` 历史归档。
- 其他角色能力。

## 原因

本能力包目标是独立使用产品经理能力，不复制整个 WorkflowProject。

项目过程材料只适合作为案例，不适合作为能力包主体。

## 后续维护方式

当 WorkflowProject 中以下内容变化时，应重新导出：

- `04-workflows/product-manager/`
- `06-templates/product-manager/`
- `11-evaluations/output-scorecards/` 中产品经理评分表
- `10-knowledge-base/patterns/product-manager-capability-system.md`
- `02-roles/product-manager/role-definition.md`
- `04-workflows/common/iteration-memory-management-workflow.md`
- `06-templates/common/iteration-memory-summary-template.md`

重新导出后更新本文件的导出时间和来源清单。
