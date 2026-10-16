# 从这里开始

导出对象：UI 设计能力包
导出时间：2026-10-15

## 这个包能做什么

- 把产品需求、PRD、页面想法整理成 UI brief。
- 输出页面信息架构、页面结构、组件说明和交互状态。
- 支持设计输入分析、设计系统检查、页面类型模式、信息架构、组件库规划、交互状态、可访问性与可用性检查、设计评审和设计交接。
- 在页面设计前确认设计规范、目标端、响应式策略、iPad 适配和不同机型布局策略。
- 在开发前输出设计到开发实现约束，明确布局、组件、状态、数据、适配和验收规则。
- 输出平台中立设计令牌，并在确认平台后生成 CSS、TypeScript、Swift、Kotlin、Dart 或 WXSS 等适配映射。
- 检查 UI 输出是否具备设计交接条件。

## 什么时候使用这个包

当用户输入包含以下意图时，优先使用本能力包：

- 页面设计
- 设计规范
- 设计令牌
- 平台主题或样式适配
- 响应式适配
- iPad 适配
- 多端设计
- 设计系统检查
- 页面类型设计
- UI brief
- 信息架构
- 组件库规划
- 组件说明
- 交互状态
- 交互体验优化
- 可访问性
- 可用性检查
- 设计交接
- 设计评审

## 与团队总调度的关系

如果外部项目中同时存在 `team-orchestration-kit`，产品、UI、开发、测试相关任务默认先由 `team-orchestration-kit` 接管。

本包直接接管的情况：

- 项目没有 `team-orchestration-kit`。
- 用户明确指定只使用 `ui-designer-kit`。
- `team-orchestration-kit` 已判断这是纯 UI 设计任务，并转交给本包。

## 一句话启动

```text
请只参考 ui-designer-kit/ 下的文件工作。请先阅读 ui-designer-kit/README.md、ui-designer-kit/usage-guide.md 和 ui-designer-kit/workflows/ui-designer/ui-designer-workflow.md。我的设计任务是：{写下你的任务}。请先判断任务类型，再说明会使用哪个 workflow、template 和 scorecard，然后继续产出结果。
```

## 更短版本

```text
请使用 ui-designer-kit 处理我的设计任务：{写下你的任务}
```

## 外部自动读取配置

如果希望用户不输入“请使用 ui-designer-kit”，可以在新项目根目录放置默认读取文件，例如：

```text
AI-WORKFLOW-RULES.md
```

并写入：

```text
当用户输入页面设计、UI brief、组件说明、交互状态、设计评审或设计交接任务时，请自动调用 ui-designer-kit。

调用前先阅读：
1. ui-designer-kit/START-HERE.md
2. ui-designer-kit/README.md
3. ui-designer-kit/usage-guide.md
4. ui-designer-kit/workflows/ui-designer/ui-designer-workflow.md

执行前请说明任务判断、使用工作流、使用模板、检查标准和保存位置。
如果无法判断是否属于 UI 设计任务，请先向用户确认。
```

## 执行顺序

1. 判断任务类型。
2. 检查设计规范、目标端和适配范围是否足够。
3. 使用 `workflows/ui-designer/ui-designer-workflow.md` 编排设计链路。
4. 根据任务类型选择细分 workflow、template 和 scorecard。
5. 输出结果后进行质量检查。

## 细分能力

| 任务 | 工作流 | 模板 | 评分表 |
| --- | --- | --- | --- |
| 确认设计规范、风格、目标端 | `design-specification-workflow.md` | `design-specification-template.md` | `design-specification-scorecard.md` |
| 设计令牌和平台适配 | `design-token-workflow.md` | `design-tokens-template.json`、`platform-adaptation-template.md` | `design-token-scorecard.md` |
| 检查已有设计系统、规范和组件库 | `design-system-audit-workflow.md` | `design-system-audit-template.md` | `design-system-audit-scorecard.md` |
| PRD 或需求转设计输入 | `design-input-analysis-workflow.md` | `design-input-analysis-template.md` | `design-input-analysis-scorecard.md` |
| Web、移动端、iPad 或多端适配 | `responsive-adaptation-workflow.md` | `responsive-adaptation-template.md` | `responsive-adaptation-scorecard.md` |
| 判断页面类型和页面模式 | `page-type-pattern-workflow.md` | `page-type-pattern-template.md` | `page-type-pattern-scorecard.md` |
| 拆页面信息和优先级 | `information-architecture-workflow.md` | `information-architecture-template.md` | `information-architecture-scorecard.md` |
| 规划组件库、复用边界和组件变体 | `component-library-planning-workflow.md` | `component-library-planning-template.md` | `component-library-planning-scorecard.md` |
| 补组件状态和异常场景 | `interaction-state-workflow.md` | `interaction-state-template.md` | `interaction-state-scorecard.md` |
| 优化操作区域、任务路径、反馈恢复和视觉层级 | `interaction-optimization-workflow.md` | `interaction-optimization-template.md` | `interaction-optimization-scorecard.md` |
| 检查可访问性、可用性和误操作风险 | `accessibility-usability-review-workflow.md` | `accessibility-usability-review-template.md` | `accessibility-usability-review-scorecard.md` |
| 检查已有 UI 方案 | `design-review-workflow.md` | `design-review-template.md` | `design-review-scorecard.md` |
| 准备交给开发或测试 | `design-handoff-workflow.md` | `design-handoff-template.md` | `design-handoff-scorecard.md` |
| 准备进入开发实现 | `design-to-development-handoff-workflow.md` | `design-to-development-handoff-template.md` | `design-to-development-handoff-scorecard.md` |

## 角色全链路原则

```text
任务识别 -> 设计系统检查 -> 设计规范确认 -> 设计令牌与平台适配 -> 响应式与多端适配判断 -> 设计输入分析 -> 页面类型模式 -> 信息架构 -> 组件库规划 -> 交互状态 -> 交互体验优化 -> 可访问性与可用性检查 -> 设计评审 -> 设计交接 -> 设计到开发实现约束
```

进入页面结构前，必须先明确：

- 这是 Web、移动端、iPad、小程序还是多端设计。
- 是否需要适配 iPad、横屏、不同手机尺寸或桌面宽屏。
- 是否需要适配折叠屏、分屏、双屏或类似 iPhoneDuo 的特殊设备形态。
- 是否已有品牌、视觉、组件、布局、交互和适配规范。
- 当前项目的设计系统是否明确，是否存在规范缺失或冲突。
- 用户想要什么样子的设计规范，以及不希望出现什么设计方向。
- 是否已有平台中立设计令牌，以及令牌源文件的位置。
- 是否需要输出平台适配文件；如果需要，目标平台、框架和主题接入方式是什么。
- 通用适配规则，包括断点、容器、栅格、导航、操作区、信息降级、表格和表单适配。
- 核心组件规划，包括组件清单、变体、状态、复用边界和不同端的形态变化。
- 页面类型模式，包括首页、列表、详情、表单、看板、编辑器等页面骨架。
- 可访问性和可用性，包括任务路径、点击区域、焦点、读屏、颜色对比和误操作风险。
- 如果用户反馈操作不方便、点击区域过小、流程步骤过多、反馈不清或视觉层级混乱，必须进入交互体验优化，不得只凭 AI 审美重做页面。
- 开发交接必须说明折叠屏、分屏、双屏下的布局方案、中缝/铰链避让、安全区域、最小可用宽度和组件变化。

## 执行状态格式

```text
当前阶段：{UI 设计阶段}
任务判断：{任务类型}
调用能力包：ui-designer-kit
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

用户指定目录时使用用户指定目录；否则优先使用项目已有 `docs/`、`documents/`、`设计文档/`、`docs/design/` 等目录。没有合适目录时再创建 `docs/`。

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
调用能力包：ui-designer-kit
使用工作流：{workflow}
使用模板：{template}
检查标准：{scorecard}
保存位置：{保存位置}
```

## 任务结束标准

- 已说明页面目标、用户场景和信息架构。
- 已说明目标端、设计规范和适配策略。
- 已说明令牌源文件和平台适配策略。
- 已覆盖关键组件和状态。
- 已说明组件复用边界和必要的组件规划。
- 已检查基础可访问性、可用性和多端可用性风险。
- 已标记设计待确认问题。
- 已说明是否可进入设计交接或开发交接。

## 使用原则

- 不在需求不清时强行画方案。
- 不把 AI 推断写成确定设计要求。
- 不脱离现有品牌、组件和平台规范。

## 首次接入

首次使用先看：

```text
INSTALL.md
usage-guide.md
examples/quick-start-example.md
```
