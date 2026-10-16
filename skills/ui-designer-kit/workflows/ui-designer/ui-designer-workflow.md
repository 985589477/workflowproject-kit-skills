# UI 设计总入口工作流

## 目的

这是 UI 设计角色的总入口。

当用户提供产品需求、PRD、页面想法、竞品截图、品牌资料或交互问题时，先使用本工作流判断应该进入设计规范确认、设计令牌与平台适配、设计系统检查、设计输入分析、响应式与多端适配、页面类型模式、信息架构、组件库规划、交互状态、可访问性与可用性检查、设计评审、设计交接，还是设计到开发实现约束。

本工作流不是简单分流器，而是 UI 设计链路编排器。它不仅负责产出页面方案，也负责控制设计规范、组件复用、适配策略、可用性和开发交接边界。

## 什么时候使用

```text
请使用 UI 设计总入口处理我的设计任务：{写下你的任务}
```

## UI 设计生命周期

```text
任务识别
-> 输入理解
-> 设计系统检查
-> 设计规范确认
-> 设计令牌策略
-> 平台适配判断
-> 用户场景和页面目标确认
-> 响应式与多端适配判断
-> 页面类型模式选择
-> 信息架构
-> 页面结构
-> 组件库规划
-> 组件和状态设计
-> 视觉方向
-> 交互体验优化
-> 可访问性与可用性检查
-> 可用性和一致性检查
-> 设计交接
-> 设计到开发实现约束
-> 复盘沉淀
```

不是每个任务都必须完整执行所有阶段，但跳过阶段时必须说明原因。

## 细分工作流调度表

| 任务类型 | 使用工作流 | 使用模板 | 检查标准 |
| --- | --- | --- | --- |
| 设计规范、风格、端和适配不清楚 | `design-specification-workflow.md` | `design-specification-template.md` | `design-specification-scorecard.md` |
| 需要建立颜色、字体、间距和组件令牌 | `design-token-workflow.md` | `design-tokens-template.json` | `design-token-scorecard.md` |
| 需要把令牌转换到具体平台 | `design-token-workflow.md` | `platform-adaptation-template.md` | `design-token-scorecard.md` |
| 已有项目规范不清、风格不一致、组件库不明 | `design-system-audit-workflow.md` | `design-system-audit-template.md` | `design-system-audit-scorecard.md` |
| 输入不清、PRD 转设计输入 | `design-input-analysis-workflow.md` | `design-input-analysis-template.md` | `design-input-analysis-scorecard.md` |
| Web、移动端、iPad 或多端适配 | `responsive-adaptation-workflow.md` | `responsive-adaptation-template.md` | `responsive-adaptation-scorecard.md` |
| 需要判断首页、列表、详情、表单、看板等页面模式 | `page-type-pattern-workflow.md` | `page-type-pattern-template.md` | `page-type-pattern-scorecard.md` |
| 需要拆页面内容和层级 | `information-architecture-workflow.md` | `information-architecture-template.md` | `information-architecture-scorecard.md` |
| 需要规划组件库、组件复用、组件变体 | `component-library-planning-workflow.md` | `component-library-planning-template.md` | `component-library-planning-scorecard.md` |
| 需要补组件状态、反馈、异常 | `interaction-state-workflow.md` | `interaction-state-template.md` | `interaction-state-scorecard.md` |
| 操作不方便、点击区域小、流程绕、反馈不清或视觉层级混乱 | `interaction-optimization-workflow.md` | `interaction-optimization-template.md` | `interaction-optimization-scorecard.md` |
| 需要检查可访问性、可用性和误操作风险 | `accessibility-usability-review-workflow.md` | `accessibility-usability-review-template.md` | `accessibility-usability-review-scorecard.md` |
| 已有 UI 方案，需要评审 | `design-review-workflow.md` | `design-review-template.md` | `design-review-scorecard.md` |
| 准备交给开发或测试 | `design-handoff-workflow.md` | `design-handoff-template.md` | `design-handoff-scorecard.md` |
| 准备进入开发，需要实现约束和验收规则 | `design-to-development-handoff-workflow.md` | `design-to-development-handoff-template.md` | `design-to-development-handoff-scorecard.md` |
| 不确定任务类型 | `ui-designer-workflow.md` | `ui-brief-template.md` | `ui-design-scorecard.md` |

## 阶段推进规则

### 从 PRD 到设计交接

```text
设计规范确认
-> 设计令牌与平台适配
-> 设计系统检查
-> 响应式与多端适配判断
设计输入分析
-> 页面类型模式选择
-> 信息架构
-> 页面结构
-> 组件库规划
-> 交互状态
-> 可访问性与可用性检查
-> 设计评审
-> 设计交接
-> 设计到开发实现约束
```

如果设计端、设计规范、用户想要的风格或适配范围不清楚，先进入设计规范确认，不要直接输出页面结构。

如果需要输出颜色、字体、字号、间距或组件视觉规则，先确认令牌源文件和目标平台。未确认平台时，输出平台中立 `design-tokens.json`，不要默认输出 CSS。

如果已有项目但规范来源不清楚，先进入设计系统检查，不要直接新建一套视觉或组件规则。

如果涉及 Web、移动端、iPad、小程序、多端或响应式，先进入响应式与多端适配判断，不要只输出单一页面结构。

如果输入材料不足，进入设计输入分析，不要直接输出页面结构。

如果页面类型没有判断清楚，先进入页面类型设计模式，不要直接堆模块。

如果页面信息很多，先进入信息架构，不要直接给组件方案。

如果页面中存在复用组件或多个页面共享能力，进入组件库规划，不要只写页面级 UI。

如果页面结构已有但状态不完整，进入交互状态设计。

如果用户反馈操作不方便、点击区域过小、流程步骤过多、反馈不清、页面难看或视觉层级混乱，进入 `interaction-optimization-workflow.md`，不能只重新描述页面结构或凭 AI 审美重做。

如果涉及关键流程、复杂表单、数据表、上传、编辑器、支付或高频操作，进入可访问性与可用性检查。

如果已有具体可用性问题或用户反馈，优先进入 `interaction-optimization-workflow.md`，再根据风险补充可访问性检查。

如果已有设计稿或 UI 方案，进入设计评审。

如果准备开发，进入设计交接。

如果开发需要开始实现，进入设计到开发实现约束，明确布局、组件、状态、数据、适配和验收规则。

## 阶段门禁

进入页面结构或组件设计前，必须确认：

- 设计对象属于 Web、移动端、iPad、小程序、桌面端还是多端。
- 是否需要适配 iPad、横屏、不同手机尺寸或桌面宽屏。
- 是否已有品牌规范、视觉规范、组件库或设计系统。
- 用户想要什么样的设计风格，以及不希望出现什么风格。
- 页面目标是否清楚。
- 目标用户和核心场景是否清楚。
- 必须展示的信息是否清楚。
- 操作路径和关键状态是否清楚。
- 是否已有品牌、组件、设计系统或平台规范。
- 是否已有平台中立设计令牌，以及令牌源文件的位置。
- 是否需要输出平台适配文件；如果需要，目标平台、框架和主题接入方式是什么。
- 是否需要建设或扩展组件库。
- 页面属于哪一种页面类型模式。
- 是否存在可访问性、可用性或误操作风险。
- 核心操作区域是否达到目标平台要求，视觉图标和实际热区是否分离。
- 用户完成核心任务是否需要无价值的重复步骤。
- 操作后是否有明确反馈，失败后是否能恢复。
- 视觉问题是否被拆成层级、对比、间距、密度和一致性问题。
- 是否准备交给开发实现。

如果缺少设计规范，应先进入 `design-specification-workflow.md`。

如果不清楚项目设计系统状态，应先进入 `design-system-audit-workflow.md`。

如果涉及多端或响应式，应先进入 `responsive-adaptation-workflow.md`。

如果涉及多页面复用或组件沉淀，应先进入 `component-library-planning-workflow.md`。

如果准备进入开发，应先进入 `design-to-development-handoff-workflow.md`。

如果平台已确认但令牌尚未转换，应先完成 `design-token-workflow.md`。

如果用户没有明确风格方向或适配目标，不要直接按 AI 审美输出方案，应先询问用户，或给出明确标记为 AI 推断的默认假设。

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

## 推荐输出

默认输出 UI brief；如果任务类型明确，应输出对应细分文档。

UI brief 包含：

- 设计目标
- 设计规范和视觉方向
- 平台中立设计令牌或令牌源文件
- 平台适配说明和实现映射
- 目标端和适配策略
- 用户和场景
- 页面信息架构
- 页面结构
- 关键组件
- 组件库规划和复用边界
- 交互状态
- 可访问性与可用性风险
- 视觉方向
- 待确认问题
- 设计交接说明
- 开发实现约束

## 主动询问规则

如果页面目标、目标用户、品牌风格、平台端、适配范围、核心流程、交互约束或令牌接入方式不清楚，应先问用户。

可以给出默认假设，但必须标记为 AI 推断。

## 结束标准

每次任务结束前必须说明：

- 当前阶段是否完成。
- 是否需要进入下一设计阶段。
- 使用了哪个细分工作流、模板和评分表。
- 是否已确认设计规范、目标端和适配策略。
- 输出是否可交给产品、开发或测试。
- 仍有哪些待确认问题。
