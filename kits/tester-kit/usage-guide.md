# tester-kit 使用指南

## 适合输入

- PRD
- 验收标准
- 用户故事
- 开发变更说明
- 缺陷反馈
- 上线前检查需求

## 默认流程

```text
测试范围分析
-> 验收标准检查
-> 测试策略规划
-> 测试数据与环境准备
-> 测试用例设计
-> 接口与集成测试
-> 兼容性和非功能风险测试
-> 回归范围判断
-> 探索式测试
-> 缺陷复现或执行结果整理
-> 测试执行报告
-> 发布验收建议
```

## 工作流选择

| 任务 | 使用文件 |
| --- | --- |
| 检查验收标准是否可测 | `workflows/tester/acceptance-criteria-review-workflow.md` |
| 制定整体测试策略 | `workflows/tester/test-strategy-planning-workflow.md` |
| 先明确测什么、不测什么 | `workflows/tester/test-scope-analysis-workflow.md` |
| 准备测试数据、环境、账号和依赖 | `workflows/tester/test-data-environment-workflow.md` |
| 生成测试用例 | `workflows/tester/test-case-design-workflow.md` |
| 做接口、联调和模块协作测试 | `workflows/tester/api-integration-test-workflow.md` |
| 做多端、多设备和特殊屏幕兼容测试 | `workflows/tester/compatibility-test-workflow.md` |
| 检查性能、稳定性、安全等非功能风险 | `workflows/tester/non-functional-risk-test-workflow.md` |
| 开发改动后判断回归范围 | `workflows/tester/regression-test-workflow.md` |
| 做探索式测试 | `workflows/tester/exploratory-test-workflow.md` |
| 规划自动化测试 | `workflows/tester/automation-test-planning-workflow.md` |
| 用户反馈 bug 或测试发现问题 | `workflows/tester/defect-reproduction-workflow.md` |
| 汇总测试执行结果 | `workflows/tester/test-execution-report-workflow.md` |
| 上线前判断是否可发布 | `workflows/tester/release-acceptance-workflow.md` |

## 模板选择

| 输出 | 使用模板 |
| --- | --- |
| 验收标准检查 | `templates/tester/acceptance-criteria-review-template.md` |
| 测试策略 | `templates/tester/test-strategy-planning-template.md` |
| 测试范围分析 | `templates/tester/test-scope-analysis-template.md` |
| 测试数据与环境准备 | `templates/tester/test-data-environment-template.md` |
| 测试用例 | `templates/tester/test-case-template.md` |
| 接口与集成测试 | `templates/tester/api-integration-test-template.md` |
| 兼容性测试 | `templates/tester/compatibility-test-template.md` |
| 非功能风险测试 | `templates/tester/non-functional-risk-test-template.md` |
| 回归范围 | `templates/tester/regression-test-template.md` |
| 探索式测试 | `templates/tester/exploratory-test-template.md` |
| 自动化测试规划 | `templates/tester/automation-test-planning-template.md` |
| 缺陷复现 | `templates/tester/defect-reproduction-template.md` |
| 测试执行报告 | `templates/tester/test-execution-report-template.md` |
| 发布验收 | `templates/tester/release-acceptance-template.md` |

## 测试治理要求

生成测试用例前，优先确认：

- 验收标准是否可测试。
- 测试策略、测试层级和风险优先级是否明确。
- 测试环境、账号、权限、数据和外部依赖是否可用。
- 是否涉及接口集成、兼容性、非功能风险、回归或自动化测试。

## 输出文件建议

如果需要保存文件，优先使用目标项目已有测试文档目录，例如：

```text
docs/test/
docs/qa/
docs/
测试文档/
```

不要默认使用 WorkflowProject 内部目录。
