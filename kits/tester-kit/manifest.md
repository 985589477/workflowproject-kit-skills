# tester-kit 来源清单

导出时间：2026-10-14

## 来源文件

| 类型 | 来源 | 导出位置 |
| --- | --- | --- |
| 角色定义 | `02-roles/tester/role-definition.md` | `roles/role-definition.md` |
| 总入口工作流 | `04-workflows/tester/tester-workflow.md` | `workflows/tester/tester-workflow.md` |
| 验收标准检查工作流 | `04-workflows/tester/acceptance-criteria-review-workflow.md` | `workflows/tester/acceptance-criteria-review-workflow.md` |
| 测试策略规划工作流 | `04-workflows/tester/test-strategy-planning-workflow.md` | `workflows/tester/test-strategy-planning-workflow.md` |
| 测试范围工作流 | `04-workflows/tester/test-scope-analysis-workflow.md` | `workflows/tester/test-scope-analysis-workflow.md` |
| 测试数据与环境准备工作流 | `04-workflows/tester/test-data-environment-workflow.md` | `workflows/tester/test-data-environment-workflow.md` |
| 测试用例工作流 | `04-workflows/tester/test-case-design-workflow.md` | `workflows/tester/test-case-design-workflow.md` |
| 接口与集成测试工作流 | `04-workflows/tester/api-integration-test-workflow.md` | `workflows/tester/api-integration-test-workflow.md` |
| 兼容性测试工作流 | `04-workflows/tester/compatibility-test-workflow.md` | `workflows/tester/compatibility-test-workflow.md` |
| 非功能风险测试工作流 | `04-workflows/tester/non-functional-risk-test-workflow.md` | `workflows/tester/non-functional-risk-test-workflow.md` |
| 回归测试工作流 | `04-workflows/tester/regression-test-workflow.md` | `workflows/tester/regression-test-workflow.md` |
| 探索式测试工作流 | `04-workflows/tester/exploratory-test-workflow.md` | `workflows/tester/exploratory-test-workflow.md` |
| 自动化测试规划工作流 | `04-workflows/tester/automation-test-planning-workflow.md` | `workflows/tester/automation-test-planning-workflow.md` |
| 缺陷复现工作流 | `04-workflows/tester/defect-reproduction-workflow.md` | `workflows/tester/defect-reproduction-workflow.md` |
| 测试执行报告工作流 | `04-workflows/tester/test-execution-report-workflow.md` | `workflows/tester/test-execution-report-workflow.md` |
| 发布验收工作流 | `04-workflows/tester/release-acceptance-workflow.md` | `workflows/tester/release-acceptance-workflow.md` |
| 模板 | `06-templates/tester/` | `templates/tester/` |
| 评分表 | `11-evaluations/output-scorecards/*test*` 等 | `scorecards/` |
| 质量检查清单 | `05-standards/quality-checklists/tester-checklist.md` | `standards/quality-checklists/tester-checklist.md` |
| 记忆工作流 | `04-workflows/common/iteration-memory-management-workflow.md` | `workflows/common/iteration-memory-management-workflow.md` |
| 记忆模板 | `06-templates/common/iteration-memory-summary-template.md` | `templates/common/iteration-memory-summary-template.md` |

## 维护说明

更新测试全局能力后，需要重新同步本包，并运行：

```bash
python3 tools/refresh_maps.py
```
