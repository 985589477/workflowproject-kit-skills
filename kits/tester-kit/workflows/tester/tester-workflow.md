# 测试工程师总入口工作流

## 目的

这是测试角色的总入口。

当用户提供 PRD、验收标准、开发变更、接口文档、缺陷反馈或上线前检查需求时，先使用本工作流判断应该进入验收标准检查、测试策略规划、测试范围分析、测试数据与环境准备、测试用例设计、接口与集成测试、兼容性测试、非功能风险测试、回归测试、探索式测试、自动化测试规划、缺陷复现、测试执行报告，还是发布验收。

本工作流不是简单分流器，而是测试生命周期编排器。

## 什么时候使用

```text
请使用测试工程师总入口处理我的测试任务：{写下你的任务}
```

## 测试生命周期

```text
任务识别
-> 输入理解
-> 需求和验收标准检查
-> 测试策略规划
-> 测试范围确认
-> 测试数据与环境准备
-> 风险和优先级判断
-> 测试用例设计
-> 接口与集成测试判断
-> 兼容性和非功能风险判断
-> 回归范围判断
-> 探索式测试
-> 执行结果整理
-> 测试执行报告
-> 发布验收判断
-> 缺陷复盘沉淀
```

不是每个任务都必须完整执行所有阶段，但跳过阶段时必须说明原因。

## 细分工作流调度表

| 任务类型 | 使用工作流 | 使用模板 | 检查标准 |
| --- | --- | --- | --- |
| 验收标准模糊、不可测试或需要评审 | `acceptance-criteria-review-workflow.md` | `acceptance-criteria-review-template.md` | `acceptance-criteria-review-scorecard.md` |
| 需要制定整体测试策略 | `test-strategy-planning-workflow.md` | `test-strategy-planning-template.md` | `test-strategy-planning-scorecard.md` |
| 输入不清、需要先定范围 | `test-scope-analysis-workflow.md` | `test-scope-analysis-template.md` | `test-scope-analysis-scorecard.md` |
| 需要准备账号、权限、数据、环境和依赖 | `test-data-environment-workflow.md` | `test-data-environment-template.md` | `test-data-environment-scorecard.md` |
| 需要生成测试用例 | `test-case-design-workflow.md` | `test-case-template.md` | `test-case-scorecard.md` |
| 涉及接口、联调、模块协作或第三方依赖 | `api-integration-test-workflow.md` | `api-integration-test-template.md` | `api-integration-test-scorecard.md` |
| 涉及多端、多浏览器、多设备或特殊屏幕 | `compatibility-test-workflow.md` | `compatibility-test-template.md` | `compatibility-test-scorecard.md` |
| 涉及性能、稳定性、安全、数据一致性等风险 | `non-functional-risk-test-workflow.md` | `non-functional-risk-test-template.md` | `non-functional-risk-test-scorecard.md` |
| 开发改动后需要回归 | `regression-test-workflow.md` | `regression-test-template.md` | `regression-test-scorecard.md` |
| 常规用例之外需要探索风险 | `exploratory-test-workflow.md` | `exploratory-test-template.md` | `exploratory-test-scorecard.md` |
| 需要判断哪些测试适合自动化 | `automation-test-planning-workflow.md` | `automation-test-planning-template.md` | `automation-test-planning-scorecard.md` |
| 用户反馈 bug 或测试发现缺陷 | `defect-reproduction-workflow.md` | `defect-reproduction-template.md` | `defect-reproduction-scorecard.md` |
| 需要整理阶段测试结果 | `test-execution-report-workflow.md` | `test-execution-report-template.md` | `test-execution-report-scorecard.md` |
| 上线前判断是否可发布 | `release-acceptance-workflow.md` | `release-acceptance-template.md` | `release-acceptance-scorecard.md` |
| 不确定任务类型 | `tester-workflow.md` | `test-plan-template.md` | `tester-scorecard.md` |

## 阶段推进规则

### 从 PRD 到发布验收

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
-> 执行结果整理
-> 测试执行报告
-> 发布验收
```

如果输入材料不足，先进入测试范围分析，不要直接生成完整测试用例。

如果验收标准不可测试，先进入验收标准检查，不要直接进入用例设计。

如果需求复杂、影响面大或时间有限，先进入测试策略规划。

如果账号、权限、数据、环境或外部依赖不清楚，先进入测试数据与环境准备。

如果涉及接口、数据流、模块协作或第三方服务，进入接口与集成测试。

如果涉及多端、多设备、浏览器、iPad、横屏、折叠屏、分屏或双屏，进入兼容性测试。

如果涉及性能、稳定性、安全、数据一致性、监控日志或关键业务链路，进入非功能风险测试。

如果用户反馈的是 bug，直接进入缺陷复现，不要混成测试计划。

如果开发已经完成改动，优先判断回归范围。

如果常规用例覆盖后仍担心遗漏，进入探索式测试。

如果需要长期回归或降低重复成本，进入自动化测试规划。

如果测试执行已经完成，进入测试执行报告。

如果准备上线，进入发布验收。

## 阶段门禁

进入测试用例设计前，必须确认：

- 测试对象是否清楚。
- 需求范围和非范围是否清楚。
- 验收标准是否清楚。
- 验收标准是否可测试、可判断、可追踪。
- 关键用户路径是否清楚。
- 影响模块和回归范围是否清楚。
- 测试环境、账号、权限、数据和依赖是否清楚。
- 是否涉及接口、集成、兼容、性能、安全或数据一致性风险。

如果需求或验收标准不清楚，不能直接生成“完整测试用例”，应先列出待确认问题。

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

## 推荐输出

默认输出测试计划和测试用例初稿；如果任务类型明确，应输出对应细分文档。

测试计划和测试用例初稿包含：

- 测试目标
- 验收标准检查
- 测试策略
- 测试范围和非范围
- 风险等级
- 测试数据和环境
- 测试场景
- 测试用例
- 接口与集成测试
- 兼容性和非功能风险
- 回归范围
- 自动化测试建议
- 待确认问题
- 发布验收建议

## 主动询问规则

如果需求范围、验收标准、目标端、数据状态、权限规则或影响模块不清楚，应先问用户。

可以给出默认假设，但必须标记为 AI 推断。

## 结束标准

每次任务结束前必须说明：

- 当前阶段是否完成。
- 是否需要进入下一测试阶段。
- 使用了哪个细分工作流、模板和评分表。
- 输出是否可执行、可回归、可交给开发或可用于发布判断。
- 仍有哪些待确认问题。
