# 从这里开始

导出对象：测试工程师能力包
导出时间：2026-10-14

## 这个包能做什么

- 把 PRD、验收标准、开发变更整理成测试计划。
- 输出测试场景、测试用例、回归范围和发布验收建议。
- 支持验收标准检查、测试策略规划、测试范围分析、测试数据与环境准备、测试用例设计、接口与集成测试、兼容性测试、非功能风险测试、回归测试、探索式测试、自动化测试规划、缺陷复现、测试执行报告和发布验收。
- 检查测试输出是否具备执行条件。

## 什么时候使用这个包

当用户输入包含以下意图时，优先使用本能力包：

- 测试计划
- 测试策略
- 验收标准检查
- 测试数据准备
- 测试用例
- 接口测试
- 集成测试
- 兼容性测试
- 非功能测试
- 回归测试
- 探索式测试
- 自动化测试规划
- 缺陷复现
- 测试报告
- 发布验收
- 测试评审

## 与团队总调度的关系

如果外部项目中同时存在 `team-orchestration-kit`，产品、UI、开发、测试相关任务默认先由 `team-orchestration-kit` 接管。

本包直接接管的情况：

- 项目没有 `team-orchestration-kit`。
- 用户明确指定只使用 `tester-kit`。
- `team-orchestration-kit` 已判断这是纯测试任务，并转交给本包。

## 一句话启动

```text
请只参考 tester-kit/ 下的文件工作。请先阅读 tester-kit/README.md、tester-kit/usage-guide.md 和 tester-kit/workflows/tester/tester-workflow.md。我的测试任务是：{写下你的任务}。请先判断任务类型，再说明会使用哪个 workflow、template 和 scorecard，然后继续产出结果。
```

## 更短版本

```text
请使用 tester-kit 处理我的测试任务：{写下你的任务}
```

## 外部自动读取配置

如果希望用户不输入“请使用 tester-kit”，可以在新项目根目录放置默认读取文件，例如：

```text
AI-WORKFLOW-RULES.md
```

并写入：

```text
当用户输入测试计划、测试用例、回归测试、缺陷复现、发布验收或测试评审任务时，请自动调用 tester-kit。

调用前先阅读：
1. tester-kit/START-HERE.md
2. tester-kit/README.md
3. tester-kit/usage-guide.md
4. tester-kit/workflows/tester/tester-workflow.md

执行前请说明任务判断、使用工作流、使用模板、检查标准和保存位置。
如果无法判断是否属于测试任务，请先向用户确认。
```

## 执行顺序

1. 判断任务类型。
2. 检查输入是否足够。
3. 使用 `workflows/tester/tester-workflow.md` 编排测试链路。
4. 根据任务类型选择细分 workflow、template 和 scorecard。
5. 输出结果后进行质量检查。

## 细分能力

| 任务 | 工作流 | 模板 | 评分表 |
| --- | --- | --- | --- |
| 检查验收标准是否可测 | `acceptance-criteria-review-workflow.md` | `acceptance-criteria-review-template.md` | `acceptance-criteria-review-scorecard.md` |
| 制定整体测试策略 | `test-strategy-planning-workflow.md` | `test-strategy-planning-template.md` | `test-strategy-planning-scorecard.md` |
| 先明确测什么、不测什么 | `test-scope-analysis-workflow.md` | `test-scope-analysis-template.md` | `test-scope-analysis-scorecard.md` |
| 准备测试数据、环境、账号和依赖 | `test-data-environment-workflow.md` | `test-data-environment-template.md` | `test-data-environment-scorecard.md` |
| 生成测试用例 | `test-case-design-workflow.md` | `test-case-template.md` | `test-case-scorecard.md` |
| 做接口、联调和模块协作测试 | `api-integration-test-workflow.md` | `api-integration-test-template.md` | `api-integration-test-scorecard.md` |
| 做多端、多设备和特殊屏幕兼容测试 | `compatibility-test-workflow.md` | `compatibility-test-template.md` | `compatibility-test-scorecard.md` |
| 检查性能、稳定性、安全等非功能风险 | `non-functional-risk-test-workflow.md` | `non-functional-risk-test-template.md` | `non-functional-risk-test-scorecard.md` |
| 开发改动后判断回归范围 | `regression-test-workflow.md` | `regression-test-template.md` | `regression-test-scorecard.md` |
| 做探索式测试 | `exploratory-test-workflow.md` | `exploratory-test-template.md` | `exploratory-test-scorecard.md` |
| 规划自动化测试 | `automation-test-planning-workflow.md` | `automation-test-planning-template.md` | `automation-test-planning-scorecard.md` |
| 用户反馈 bug 或测试发现问题 | `defect-reproduction-workflow.md` | `defect-reproduction-template.md` | `defect-reproduction-scorecard.md` |
| 汇总测试执行结果 | `test-execution-report-workflow.md` | `test-execution-report-template.md` | `test-execution-report-scorecard.md` |
| 上线前判断是否可发布 | `release-acceptance-workflow.md` | `release-acceptance-template.md` | `release-acceptance-scorecard.md` |

## 角色全链路原则

```text
任务识别 -> 验收标准检查 -> 测试策略规划 -> 测试范围分析 -> 测试数据与环境准备 -> 测试用例设计 -> 接口与集成测试 -> 兼容性和非功能风险测试 -> 回归范围判断 -> 探索式测试 -> 缺陷复现或执行结果整理 -> 测试执行报告 -> 发布验收判断
```

## 执行状态格式

```text
当前阶段：{测试阶段}
任务判断：{任务类型}
调用能力包：tester-kit
使用工作流：{workflow}
使用模板：{template}
检查标准：{scorecard}
执行方式：{只分析 / 先确认后继续 / 直接产出}
是否需要用户确认：{是 / 否}
已完成：{已完成内容}
正在执行：{当前动作}
下一步：{下一阶段或等待确认}
保存位置：{对话直接输出 / 用户指定目录 / 已有文档目录 / docs/}
```

## 外部项目输出目录策略

用户指定目录时使用用户指定目录；否则优先使用项目已有 `docs/`、`documents/`、`测试文档/`、`docs/test/` 等目录。没有合适目录时再创建 `docs/`。

不要在外部项目中默认创建 `04-outputs/` 或 `12-projects/`。

## 长期迭代记忆管理

长期使用时优先维护项目已有记忆文件，例如 `AGENTS.md`、`AI-WORKFLOW-RULES.md`、`docs/project-memory.md` 或 `docs/ai-context.md`。

如果没有合适文件，建议使用：

```text
docs/ai-memory-summary.md
```

## 输出确认格式

```text
任务判断：{任务类型}
调用能力包：tester-kit
使用工作流：{workflow}
使用模板：{template}
检查标准：{scorecard}
保存位置：{保存位置}
```

## 任务结束标准

- 已说明测试范围和非范围。
- 已检查验收标准是否可测试。
- 已说明测试策略、测试层级和风险优先级。
- 已承接 PRD、验收标准或开发变更。
- 已说明测试环境、账号、权限、数据和外部依赖。
- 已覆盖核心路径、边界和异常场景。
- 已判断接口集成、兼容性、非功能风险、回归和自动化测试是否需要覆盖。
- 已说明是否可执行、暂缓或需要补充信息。

## 使用原则

- 不在需求和验收标准不清时强行给通过结论。
- 不替代产品经理决定需求优先级。
- 不替代开发修复代码。

## 首次接入

首次使用先看：

```text
INSTALL.md
usage-guide.md
examples/quick-start-example.md
```
