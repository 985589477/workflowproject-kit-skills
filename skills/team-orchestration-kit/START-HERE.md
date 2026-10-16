# 从这里开始

导出对象：跨角色团队总调度能力包
导出时间：2026-10-15

## 这个包能做什么

- 把产品经理、UI 设计师、开发工程师、测试工程师组织成一个完整 AI 协作团队。
- 判断用户需求应该由哪个角色先接管，以及后续是否需要其他角色参与。
- 按产品、UI、开发、测试的链路推进需求、设计、实现、验证和交付。
- 检查上游产物是否能被下游角色看懂。
- 检查开发交付是否能通过产品、UI 和测试三方验收。
- 当角色之间沟通不畅时，输出阻塞原因、补充问题和 badcase 回流建议。

## 什么时候使用这个包

当用户输入包含以下意图时，优先使用本能力包：

- 一个需求可能需要产品、UI、开发、测试多个角色协作。
- 用户只有模糊想法，不确定应该先做需求、设计、开发还是测试。
- 需要从需求一路推进到设计、开发、测试和验收。
- 需要检查 PRD、设计交接、开发交付或测试报告是否能被其他角色理解。
- 需要判断某个阶段是否可以进入下一阶段。
- 需要进行跨角色互审、交接检查或三方验收。
- 角色之间出现理解不一致，需要记录 badcase 并回到能力建设项目优化。

## 总调度优先规则

如果外部项目中存在 `team-orchestration-kit`，则产品、UI、开发、测试相关任务默认先由 `team-orchestration-kit` 接管。

总调度入口先做判断，再决定是否转交具体角色包。

默认路由：

```text
用户提出任务
-> team-orchestration-kit 先接管
-> 判断是否跨角色
-> 判断谁先接管
-> 必要时转交 product-manager-kit / ui-designer-kit / developer-kit / tester-kit
```

### Skill 与子 Agent 的分流

- 单角色、单产出、没有交接或并行：当前 Agent 直接调用对应 Skill，不创建子 Agent。
- 多角色、多阶段、需要交接、联合验收或并行：父 Agent 必须创建真实子 Agent。
- 当前运行环境没有真实子 Agent 工具：先报告限制，未经用户确认不得降级，也不得把单 Agent 执行描述为子 Agent 协作。

每次执行必须声明：

```text
执行模式：单 Agent + Skill / 父 Agent + 子 Agent / 单 Agent 降级模拟，不是真实子 Agent
```

只有在以下情况，具体角色包才直接接管：

- 当前项目没有 `team-orchestration-kit`。
- 用户明确说“只使用某个角色包”。
- 总调度判断这是纯单角色轻量任务，并说明不需要跨角色协作。

## 一句话启动

在新项目或新 AI 对话里，直接复制下面这句话：

```text
请只参考 team-orchestration-kit/ 下的文件工作。请先阅读 team-orchestration-kit/README.md、team-orchestration-kit/usage-guide.md 和 team-orchestration-kit/workflows/mixed/team-orchestration-workflow.md。我的任务是：{写下你的任务}。请先判断需要哪些角色参与、谁先接管、会使用哪些 workflow、template 和 scorecard，然后按阶段推进。
```

## 更短版本

如果只是快速启动，可以说：

```text
请使用 team-orchestration-kit 调度产品、UI、开发和测试处理我的任务：{写下你的任务}
```

## 外部自动读取配置

如果希望用户不输入“请使用 team-orchestration-kit”，可以在新项目根目录放置默认读取文件，例如：

```text
AI-WORKFLOW-RULES.md
```

并在文件里写入：

```text
你是当前项目的 AI 团队总调度器。

当用户输入任务时，请先判断是否属于跨角色协作任务。

如果用户输入包含以下意图之一，请自动调用 team-orchestration-kit：
- 需求需要产品、UI、开发、测试连续协作
- 用户不确定应该先找哪个角色
- 需要从想法推进到需求、设计、开发、测试或验收
- 需要检查产品、UI、开发、测试之间的交接是否清楚
- 需要判断某个阶段能否进入下一阶段
- 需要跨角色互审、三方验收或 badcase 反馈

触发 team-orchestration-kit 后，请先阅读：
1. team-orchestration-kit/START-HERE.md
2. team-orchestration-kit/README.md
3. team-orchestration-kit/usage-guide.md
4. team-orchestration-kit/workflows/mixed/team-orchestration-workflow.md

执行前请先说明：
- 你判断这是哪一类跨角色任务。
- 哪些角色需要参与。
- 当前由哪个角色先接管。
- 你将使用哪个 workflow。
- 你将参考哪个 template。
- 你将使用哪个 scorecard 检查结果。
- 是否需要用户确认。

如果任务只属于单一角色，也应先由 `team-orchestration-kit` 给出判断，再建议使用对应角色包：
- product-manager-kit
- ui-designer-kit
- developer-kit
- tester-kit

简单任务在当前 Agent 中直接调用对应角色 Skill，不创建子 Agent。只有组合任务才创建父 Agent 和子 Agent，并为每个子 Agent 提供任务简报和验收标准。

如果无法判断任务类型，请先向用户确认。
```

## 依赖的角色包

team-orchestration-kit 是总调度入口，建议和以下角色包放在同级目录：

```text
product-manager-kit/
ui-designer-kit/
developer-kit/
tester-kit/
team-orchestration-kit/
```

如果外部项目没有某个角色包，总调度仍然可以输出协作判断，但需要说明缺失的角色包和影响。

## 执行顺序

1. 先判断任务类型和是否跨角色。
2. 再判断需要哪些角色参与。
3. 决定当前优先接管角色。
4. 选择当前阶段的 workflow、template 和 scorecard。
5. 执行当前阶段产出。
6. 做交接检查，判断下游角色是否看得懂。
7. 判断是否进入下一角色或下一阶段。
8. 如果发生阻塞，输出 badcase 和回流建议。

## 团队全链路原则

team-orchestration-kit 不应把“命中某个角色”当成任务结束。

当用户提出完整功能或项目需求时，应默认按团队链路判断后续阶段：

```text
用户输入
-> 需求识别和角色判断
-> 产品经理接管：需求分析 / PRD / 验收标准
-> UI 设计师接管：设计规范 / 页面结构 / 组件 / 适配 / 设计交接
-> 开发工程师接管：项目理解 / 方案规划 / 任务拆解 / 实现 / 验证
-> 测试工程师接管：验收标准检查 / 测试策略 / 用例 / 回归 / 发布验收
-> 跨角色互审
-> 交付结论
-> badcase 反馈和能力优化建议
```

不是每个任务都必须经过所有角色。跳过任何角色都要说明理由。

## 执行状态格式

每次执行前或阶段切换时，先输出：

```text
当前阶段：{团队协作阶段}
总调度判断：{当前任务类型}
参与角色：{产品经理 / UI 设计师 / 开发工程师 / 测试工程师}
当前接管角色：{角色}
调用能力包：{product-manager-kit / ui-designer-kit / developer-kit / tester-kit / team-orchestration-kit}
使用工作流：{workflow}
使用模板：{template}
检查标准：{scorecard}
执行方式：{只分析 / 先确认后继续 / 直接产出 / 先方案后实现}
是否需要用户确认：{是 / 否}
已完成：{已完成内容}
正在执行：{当前动作}
下一步：{下一角色或下一阶段}
交接状态：{通过 / 不通过 / 待确认}
保存位置：{对话直接输出 / 用户指定目录 / 已有文档目录 / docs/}
```

## 外部项目输出目录策略

当本能力包在其他项目中使用，并且用户要求把结果保存为文件时，必须先判断当前项目是否已有统一文档目录。

优先级如下：

1. 如果用户明确指定输出目录，使用用户指定目录。
2. 如果项目已有统一文档目录，优先使用该目录，例如 `docs/`、`documents/`、`项目文档/`。
3. 如果项目已有明确的协作文档目录，优先使用该目录，例如 `docs/team/`、`docs/workflow/`、`docs/delivery/`。
4. 如果没有任何合适目录，再在项目根目录创建 `docs/`。

不要在外部项目中默认创建或使用 WorkflowProject 内部目录，例如：

```text
{目标文档目录}/
12-projects/
```

## 长期迭代记忆管理

如果 team-orchestration-kit 在同一个外部项目中持续使用，建议维护项目记忆摘要，避免每次让 AI 读取大量历史协作记录。

优先使用项目已有的记忆或规则文件，例如：

```text
AGENTS.md
AI-WORKFLOW-RULES.md
docs/project-memory.md
docs/ai-context.md
```

如果没有合适文件，并且用户希望保存长期上下文，则在已有文档目录中创建：

```text
docs/ai-memory-summary.md
```

每轮跨角色任务结束时，如果产生新的关键结论、角色分工、交接规则、阻塞、风险、验证结果或下一步，应更新该摘要。

如果需要整理长期历史，使用：

```text
workflows/common/iteration-memory-management-workflow.md
templates/common/iteration-memory-summary-template.md
```

## 输出确认格式

每次执行前，先输出：

```text
任务判断：{任务类型}
调用能力包：team-orchestration-kit
参与角色：{角色列表}
当前接管角色：{角色}
使用工作流：{workflow}
使用模板：{template}
检查标准：{scorecard}
保存位置：{对话直接输出 / 用户指定目录 / 已有文档目录 / docs/}
```

## 任务结束标准

任务结束前必须说明：

- 本次有哪些角色参与。
- 每个角色完成了什么。
- 哪些交接通过，哪些不通过。
- 是否可以进入下一阶段。
- 是否存在待确认问题。
- 是否存在 badcase 或能力优化建议。
- 输出是否经过对应 scorecard 或质量检查。
- 输出是否保存，保存位置是什么。
- 下一步应该由哪个角色接管。

## 使用原则

- 只要外部项目存在 `team-orchestration-kit`，产品、UI、开发、测试相关任务默认先走团队总入口。
- 已经明确只有单一角色任务时，也先由总调度判断并转交对应角色包，除非用户明确要求直接使用某个角色包。
- 不要把单个角色输出当作任务结束，必须判断后续角色是否需要接手。
- 上游产物下游看不懂时，不要硬推进，先反馈阻塞。
- 开发交付后要让产品、UI、测试分别验收。
- 信息不明确或角色判断冲突时，先询问用户。
- 不需要理解原 WorkflowProject。

## 首次接入

如果这是第一次在外部项目使用 team-orchestration-kit，请先阅读：

```text
INSTALL.md
examples/quick-start-example.md
integrations/codex-usage.md
integrations/cursor-usage.md
```
