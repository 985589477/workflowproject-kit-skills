# ui-designer-kit 来源清单

导出时间：2026-10-15

## 来源文件

| 类型 | 来源 | 导出位置 |
| --- | --- | --- |
| 角色定义 | `02-roles/ui-designer/role-definition.md` | `roles/role-definition.md` |
| 总入口工作流 | `04-workflows/ui-designer/ui-designer-workflow.md` | `workflows/ui-designer/ui-designer-workflow.md` |
| 设计规范确认工作流 | `04-workflows/ui-designer/design-specification-workflow.md` | `workflows/ui-designer/design-specification-workflow.md` |
| 设计令牌与平台适配工作流 | `04-workflows/ui-designer/design-token-workflow.md` | `workflows/ui-designer/design-token-workflow.md` |
| 设计系统检查工作流 | `04-workflows/ui-designer/design-system-audit-workflow.md` | `workflows/ui-designer/design-system-audit-workflow.md` |
| 响应式与多端适配工作流 | `04-workflows/ui-designer/responsive-adaptation-workflow.md` | `workflows/ui-designer/responsive-adaptation-workflow.md` |
| 页面类型设计模式工作流 | `04-workflows/ui-designer/page-type-pattern-workflow.md` | `workflows/ui-designer/page-type-pattern-workflow.md` |
| 设计输入分析工作流 | `04-workflows/ui-designer/design-input-analysis-workflow.md` | `workflows/ui-designer/design-input-analysis-workflow.md` |
| 信息架构工作流 | `04-workflows/ui-designer/information-architecture-workflow.md` | `workflows/ui-designer/information-architecture-workflow.md` |
| 组件库规划工作流 | `04-workflows/ui-designer/component-library-planning-workflow.md` | `workflows/ui-designer/component-library-planning-workflow.md` |
| 交互状态工作流 | `04-workflows/ui-designer/interaction-state-workflow.md` | `workflows/ui-designer/interaction-state-workflow.md` |
| 交互体验优化工作流 | `04-workflows/ui-designer/interaction-optimization-workflow.md` | `workflows/ui-designer/interaction-optimization-workflow.md` |
| 可访问性与可用性检查工作流 | `04-workflows/ui-designer/accessibility-usability-review-workflow.md` | `workflows/ui-designer/accessibility-usability-review-workflow.md` |
| 设计评审工作流 | `04-workflows/ui-designer/design-review-workflow.md` | `workflows/ui-designer/design-review-workflow.md` |
| 设计交接工作流 | `04-workflows/ui-designer/design-handoff-workflow.md` | `workflows/ui-designer/design-handoff-workflow.md` |
| 设计到开发实现约束工作流 | `04-workflows/ui-designer/design-to-development-handoff-workflow.md` | `workflows/ui-designer/design-to-development-handoff-workflow.md` |
| 模板 | `06-templates/ui-designer/` | `templates/ui-designer/` |
| 设计令牌标准 | `05-standards/design-token-standard.md` | `standards/design-token-standard.md` |
| 交互质量标准 | `05-standards/interaction-quality-standard.md` | `standards/interaction-quality-standard.md` |
| 评分表 | `11-evaluations/output-scorecards/*design*` 等 | `scorecards/` |
| 质量检查清单 | `05-standards/quality-checklists/ui-designer-checklist.md` | `standards/quality-checklists/ui-designer-checklist.md` |
| 记忆工作流 | `04-workflows/common/iteration-memory-management-workflow.md` | `workflows/common/iteration-memory-management-workflow.md` |
| 记忆模板 | `06-templates/common/iteration-memory-summary-template.md` | `templates/common/iteration-memory-summary-template.md` |

## 维护说明

更新 UI 设计全局能力后，需要重新同步本包，并运行：

```bash
python3 tools/refresh_maps.py
```
