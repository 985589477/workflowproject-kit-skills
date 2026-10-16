# ui-designer-kit 使用指南

## 适合输入

- 产品需求
- PRD
- 页面想法
- 竞品页面描述
- 设计评审问题
- 交互状态问题

## 默认流程

```text
设计规范确认
-> 设计系统检查
-> 响应式与多端适配判断
设计输入分析
-> 页面类型模式
-> 信息架构
-> 组件库规划
-> 页面结构
-> 交互状态
-> 交互体验优化
-> 可访问性与可用性检查
-> 设计评审
-> 设计交接
-> 设计到开发实现约束
```

## 工作流选择

| 任务 | 使用文件 |
| --- | --- |
| 确认设计规范、风格、目标端 | `workflows/ui-designer/design-specification-workflow.md` |
| 检查已有设计系统、规范和组件库 | `workflows/ui-designer/design-system-audit-workflow.md` |
| PRD 或需求转设计输入 | `workflows/ui-designer/design-input-analysis-workflow.md` |
| Web、移动端、iPad 或多端适配 | `workflows/ui-designer/responsive-adaptation-workflow.md` |
| 判断页面类型和页面模式 | `workflows/ui-designer/page-type-pattern-workflow.md` |
| 拆页面信息和优先级 | `workflows/ui-designer/information-architecture-workflow.md` |
| 规划组件库、组件复用和变体 | `workflows/ui-designer/component-library-planning-workflow.md` |
| 补组件状态和异常场景 | `workflows/ui-designer/interaction-state-workflow.md` |
| 优化操作区域、任务路径、反馈恢复和视觉层级 | `workflows/ui-designer/interaction-optimization-workflow.md` |
| 检查可访问性和可用性 | `workflows/ui-designer/accessibility-usability-review-workflow.md` |
| 检查已有 UI 方案 | `workflows/ui-designer/design-review-workflow.md` |
| 准备交给开发或测试 | `workflows/ui-designer/design-handoff-workflow.md` |
| 准备进入开发实现 | `workflows/ui-designer/design-to-development-handoff-workflow.md` |

## 模板选择

| 输出 | 使用模板 |
| --- | --- |
| 设计规范确认 | `templates/ui-designer/design-specification-template.md` |
| 设计系统检查 | `templates/ui-designer/design-system-audit-template.md` |
| 设计输入分析 | `templates/ui-designer/design-input-analysis-template.md` |
| 响应式与多端适配 | `templates/ui-designer/responsive-adaptation-template.md` |
| 页面类型设计模式 | `templates/ui-designer/page-type-pattern-template.md` |
| 信息架构 | `templates/ui-designer/information-architecture-template.md` |
| 组件库规划 | `templates/ui-designer/component-library-planning-template.md` |
| 交互状态 | `templates/ui-designer/interaction-state-template.md` |
| 交互体验优化 | `templates/ui-designer/interaction-optimization-template.md` |
| 可访问性与可用性检查 | `templates/ui-designer/accessibility-usability-review-template.md` |
| 设计评审 | `templates/ui-designer/design-review-template.md` |
| 设计交接 | `templates/ui-designer/design-handoff-template.md` |
| 设计到开发实现约束 | `templates/ui-designer/design-to-development-handoff-template.md` |

## 设计规范输出要求

输出设计规范时，不要只描述风格。必须包含：

- 通用适配规则：断点、容器、栅格、导航、操作区、信息降级、表格适配、表单适配和安全区域。
- 组件规划：组件清单、组件来源、是否新增、组件变体、组件状态、复用范围和端差异。
- 组件适配矩阵：每个核心组件在小屏、平板、桌面端分别如何变化。
- 特殊设备形态：折叠屏、分屏、双屏、横屏、iPad 分屏下的布局方案和开发交接规则。

## 特殊设备交接要求

如果涉及折叠屏、分屏、双屏或类似 iPhoneDuo 的设备，交接给开发时必须说明：

- 展开态、折叠态、分屏态分别使用哪种布局。
- 是否存在中缝、铰链、分隔区或安全区域。
- 哪些组件需要避让中缝或安全区域。
- 列表、详情、筛选、弹窗、主操作在特殊形态下的位置。
- 哪些场景可以按普通响应式处理，哪些必须单独适配。

## 开发实现约束要求

准备进入开发时，必须补齐：

- 页面结构实现规则。
- 组件来源、数据字段和状态字段。
- 响应式、平板、横屏、折叠屏、分屏和双屏适配规则。
- 开发可调整范围、需要设计确认的范围和不可自行变更的范围。
- 开发验收清单。

## 输出文件建议

如果需要保存文件，优先使用目标项目已有设计文档目录，例如：

```text
docs/design/
docs/
设计文档/
```

不要默认使用 WorkflowProject 内部目录。
