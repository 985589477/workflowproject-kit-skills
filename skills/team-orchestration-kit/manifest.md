# 来源清单

导出时间：2026-10-15

## 时间管理规则

本能力包不使用版本号。

判断新旧只看导出时间。每次重新导出时，更新本文件和入口文件中的导出时间。

## 导出对象

跨角色团队总调度能力包。

## 导出目标

```text
14-exports/team-orchestration-kit/
```

## 来源项目

```text
WorkflowProject
```

## 导出范围

### 工作流

| 导出目录 | 来源 |
| --- | --- |
| `workflows/mixed/` | `04-workflows/mixed/` |
| `workflows/common/iteration-memory-management-workflow.md` | `04-workflows/common/iteration-memory-management-workflow.md` |
| `workflows/common/agent-orchestration-workflow.md` | `04-workflows/common/agent-orchestration-workflow.md` |

### 模板

| 导出目录 | 来源 |
| --- | --- |
| `templates/mixed/` | `06-templates/mixed/` |
| `templates/common/iteration-memory-summary-template.md` | `06-templates/common/iteration-memory-summary-template.md` |
| `templates/common/agent-task-brief-template.md` | `06-templates/common/agent-task-brief-template.md` |
| `templates/common/agent-result-report-template.md` | `06-templates/common/agent-result-report-template.md` |

### 评分表

| 导出目录 | 来源 |
| --- | --- |
| `scorecards/team-orchestration-scorecard.md` | `11-evaluations/output-scorecards/team-orchestration-scorecard.md` |

### 知识和标准

| 导出文件 | 来源 |
| --- | --- |
| `knowledge/role-kit-lifecycle-standard.md` | `05-standards/role-kit-lifecycle-standard.md` |
| `knowledge/agent-orchestration-standard.md` | `05-standards/agent-orchestration-standard.md` |

### 使用体验层

| 导出文件 | 作用 |
| --- | --- |
| `START-HERE.md` | 外部 AI 和用户的统一入口 |
| `README.md` | 能力包说明 |
| `usage-guide.md` | 使用步骤和工作流选择 |
| `INSTALL.md` | 外部项目首次接入说明 |
| `examples/quick-start-example.md` | 快速启动示例 |
| `integrations/codex-usage.md` | Codex 使用说明 |
| `integrations/cursor-usage.md` | Cursor 使用说明 |
| `SKILL.md` | Codex skill 草稿 |

## 依赖关系

本能力包建议与以下能力包同级使用：

```text
product-manager-kit/
ui-designer-kit/
developer-kit/
tester-kit/
```

这些能力包负责具体角色产出，`team-orchestration-kit` 负责总调度、交接检查和跨角色验收。

## 未导出内容

- `12-projects/` 中的一次性项目过程材料。
- `15-dashboard/` React 可视化控制台。
- `13-visual-maps/` XMind 导图。
- 其他非相关角色资产。

## 后续维护方式

当 WorkflowProject 中以下内容变化时，应重新导出：

- `04-workflows/mixed/`
- `06-templates/mixed/`
- `11-evaluations/output-scorecards/team-orchestration-scorecard.md`
- `05-standards/role-kit-lifecycle-standard.md`
- `04-workflows/common/iteration-memory-management-workflow.md`
- `06-templates/common/iteration-memory-summary-template.md`

重新导出后更新本文件的导出时间和来源清单。
