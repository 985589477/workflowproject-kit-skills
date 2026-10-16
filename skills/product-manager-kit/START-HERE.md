# 从这里开始

导出对象：产品经理能力包
导出时间：2026-10-13

## 这个包能做什么

- 把模糊产品想法整理成可执行需求。
- 生成需求分析、PRD、用户故事和验收标准。
- 拆分功能范围、判断优先级、规划版本和路线图。
- 整理用户反馈、分析竞品、评估需求变更。
- 辅助产品策略判断、需求池管理和版本复盘。

## 什么时候使用这个包

当用户输入包含以下意图时，优先使用本能力包：

- 产品想法梳理。
- 需求分析。
- PRD 生成。
- 功能范围拆分。
- 用户故事。
- 验收标准。
- 用户反馈整理。
- 竞品分析。
- 优先级判断。
- 版本规划。
- 产品策略判断。
- 需求池管理。
- 产品路线图。
- 需求变更评估。
- 版本复盘。

## 与团队总调度的关系

如果外部项目中同时存在 `team-orchestration-kit`，产品、UI、开发、测试相关任务默认先由 `team-orchestration-kit` 接管。

本包直接接管的情况：

- 项目没有 `team-orchestration-kit`。
- 用户明确指定只使用 `product-manager-kit`。
- `team-orchestration-kit` 已判断这是纯产品经理任务，并转交给本包。

## 一句话启动

在新项目或新 AI 对话里，直接复制下面这句话：

```text
请只参考 product-manager-kit/ 下的文件工作。请先阅读 product-manager-kit/README.md、product-manager-kit/usage-guide.md 和 product-manager-kit/workflows/product-manager/product-manager-workflow.md。我的任务是：{写下你的任务}。请先判断任务类型，再说明会使用哪个 workflow、template 和 scorecard，然后继续产出结果。
```

## 更短版本

如果只是快速启动，可以说：

```text
请使用 product-manager-kit 处理我的任务：{写下你的任务}
```

## 外部自动读取配置

如果希望用户不输入“请使用 product-manager-kit”，可以在新项目根目录放置默认读取文件，例如：

```text
AI-WORKFLOW-RULES.md
```

并在文件里写入：

```text
你是当前项目的 AI 工作流调度器。

当用户输入任务时，请先判断是否属于产品经理能力范围。

如果用户输入包含以下意图之一，请自动调用 product-manager-kit：
- 产品想法梳理
- 需求分析
- PRD 生成
- 用户任务流程与交互要求
- 功能范围拆分
- 用户故事
- 验收标准
- 用户反馈整理
- 竞品分析
- 优先级判断
- 版本规划
- 产品策略判断
- 需求池管理
- 产品路线图
- 需求变更评估
- 版本复盘

触发 product-manager-kit 后，请先阅读：
1. product-manager-kit/START-HERE.md
2. product-manager-kit/README.md
3. product-manager-kit/usage-guide.md
4. product-manager-kit/workflows/product-manager/product-manager-workflow.md

执行前请先说明：
- 你判断这是哪一类产品任务。
- 你将使用哪个 workflow。
- 你将参考哪个 template。
- 你将使用哪个 scorecard 检查结果。

如果用户输入不属于产品经理任务，请不要强行调用 product-manager-kit，应继续判断是否需要其他能力包。
如果无法判断任务类型，请先向用户确认。
```

配置完成后，用户可以直接输入：

```text
我想做一个 AI 提示词模板管理工具，帮我梳理一下需求。
```

AI 应自动判断这是产品需求类任务，并进入 `product-manager-kit`。

## 执行顺序

1. 先判断任务类型。
2. 再选择对应 workflow。
3. 再选择对应 template。
4. 产出结果后使用对应 scorecard 检查。
5. 如果信息不足，先列出待确认问题。

## 产品全链路原则

product-manager-kit 不应把“输出某个产品文档”当成任务结束。

当用户提出一个产品想法或产品任务时，应默认按完整产品链路判断后续阶段：

```text
想法标准化
-> 需求分析
-> 是否确认进入 PRD
-> PRD 生成
-> 验收标准
-> 功能规划
-> 优先级判断
-> 版本规划
-> 需求池或路线图
-> 变更评估或版本复盘
```

不是每个任务都必须完整执行所有阶段，但跳过任何阶段都要说明理由。

进入 PRD、版本规划或开发交接前，必须确认目标用户、核心场景、问题、范围、非范围、风险、约束和待确认问题。

遇到目标用户不清、场景不清、范围不清、优先级不清、验收标准不清或决策人不清时，先主动询问用户，不要把推断写成确定需求。

## 执行状态格式

每次执行前或阶段切换时，先输出：

```text
当前阶段：{任务识别 / 想法标准化 / 需求分析 / PRD 生成 / 验收标准 / 功能规划 / 优先级判断 / 版本规划 / 路线图 / 需求变更评估 / 版本复盘}
任务判断：{任务类型}
调用能力包：product-manager-kit
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

当本能力包在其他项目中使用，并且用户要求把结果保存为文件时，必须先判断当前项目是否已有统一文档目录。

优先级如下：

1. 如果用户明确指定输出目录，使用用户指定目录。
2. 如果项目已有统一文档目录，优先使用该目录，例如 `docs/`、`documents/`、`产品文档/`、`需求文档/`。
3. 如果项目已有明确的产品文档目录，优先使用该目录，例如 `docs/product/`、`docs/prd/`、`product-docs/`。
4. 如果没有任何合适目录，再在项目根目录创建 `docs/`。

不要在外部项目中默认创建或使用 WorkflowProject 内部目录，例如：

```text
{目标文档目录}/
12-projects/
```

如果只是对话中直接输出结果，不需要创建文件。

## 长期迭代记忆管理

如果 product-manager-kit 在同一个外部项目中持续使用，建议维护项目记忆摘要，避免每次让 AI 读取大量历史产品文档。

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

每次产品任务结束时，如果产生新的关键结论、产品决策、范围变化、版本计划、需求池变化、风险或下一步，应更新该摘要。

如果需要整理长期历史，使用：

```text
workflows/common/iteration-memory-management-workflow.md
templates/common/iteration-memory-summary-template.md
```

## 输出确认格式

每次执行前，先输出：

```text
任务判断：{任务类型}
调用能力包：product-manager-kit
使用工作流：{workflow}
使用模板：{template}
检查标准：{scorecard}
保存位置：{对话直接输出 / 用户指定目录 / 已有文档目录 / docs/}
```

## 任务结束标准

任务结束前必须说明：

- 当前阶段是否完成。
- 是否已经进入或不进入下一阶段。
- 如果停止，停止原因是什么。
- 是否存在待确认问题。
- 是否需要继续生成 PRD、验收标准、功能规划或版本规划。
- 是否需要进入需求池、路线图、变更评估或复盘。
- 如果输出保存为文件，保存位置是什么。
- 是否需要更新项目记忆摘要。

如果这些信息没有说明完整，不应直接宣称任务完成。

## 使用原则

- 不确定做什么时，先走总入口。
- 已经明确任务时，直接指定对应工作流。
- 不要把单个产品文档当作结束点，必须判断后续阶段。
- 进入 PRD、版本规划或开发交接前必须确认范围、边界、风险和待确认问题。
- 信息不明确时主动询问用户。
- 生成结果后，用对应评分表检查。
- 不需要理解原 WorkflowProject。

## 首次接入

如果这是第一次在外部项目使用 product-manager-kit，请先阅读：

```text
INSTALL.md
examples/quick-start-example.md
integrations/codex-usage.md
integrations/cursor-usage.md
```
