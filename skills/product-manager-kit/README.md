# 产品经理能力包

这是从 WorkflowProject 导出的产品经理独立能力包。

它适合在不理解完整 WorkflowProject 的情况下，直接让 AI 执行产品经理相关任务。

导出时间：2026-10-13

product-manager-kit 的总入口不是简单分流器。它会把产品任务放进完整生命周期里判断：

```text
想法标准化 -> 需求分析 -> PRD -> 验收标准 -> 功能规划 -> 优先级 -> 版本规划 -> 路线图或需求池 -> 变更评估或复盘
```

小任务可以只执行部分阶段，但必须说明跳过哪些阶段以及为什么。

## 最快使用

在新项目或新 AI 对话里，直接复制：

```text
请只参考 product-manager-kit/ 下的文件工作。请先阅读 product-manager-kit/README.md、product-manager-kit/usage-guide.md 和 product-manager-kit/workflows/product-manager/product-manager-workflow.md。我的产品想法是：{写下你的想法}。请先判断任务类型，再说明会使用哪个 workflow、template 和 scorecard，然后继续产出结果。
```

如果想更短，可以说：

```text
请使用 product-manager-kit 处理我的产品想法：{写下你的想法}
```

## 首次接入

如果是第一次把 product-manager-kit 放入一个新项目，先看：

```text
INSTALL.md
```

如果想看一轮真实启动示例，先看：

```text
examples/quick-start-example.md
```

## 适用对象

- 产品经理。
- 创业者。
- 需要和 AI 协作产出产品文档的人。
- 想把模糊想法转成需求、PRD、路线图或复盘的人。

## 能做什么

本能力包覆盖产品经理主链路：

```text
想法整理
-> 需求分析
-> PRD
-> 验收标准
-> 功能规划
-> 用户故事
-> 用户反馈整理
-> 竞品分析
-> 优先级判断
-> 版本规划
-> 产品策略判断
-> 需求池管理
-> 产品路线图
-> 需求变更评估
-> 版本复盘
```

## 如何开始

如果你不知道该用哪个文件，先使用总入口：

```text
workflows/product-manager/product-manager-workflow.md
```

可以这样对 AI 说：

```text
请参考 workflows/product-manager/product-manager-workflow.md。
我的想法是：{你的想法}
请先判断应该使用哪个产品经理工作流，再继续执行。
```

## 输出保存规则

如果只是在对话中生成结果，不需要创建文件。

如果需要把结果保存到新项目里，请先检查新项目是否已有统一文档目录：

1. 用户指定了输出目录时，使用用户指定目录。
2. 项目已有统一文档目录时，使用已有目录，例如 `docs/`、`documents/`、`产品文档/`、`需求文档/`。
3. 项目已有产品文档目录时，使用该目录，例如 `docs/product/`、`docs/prd/`、`product-docs/`。
4. 如果没有合适目录，再在项目根目录创建 `docs/`。

不要在外部项目中默认创建或使用 WorkflowProject 内部目录，例如 `04-outputs/` 或 `12-projects/`。

## 长期迭代记忆管理

如果 product-manager-kit 在同一个外部项目中持续使用，建议维护项目记忆摘要，避免每次让 AI 读取大量历史产品文档。

优先使用项目已有的记忆或规则文件，例如 `AGENTS.md`、`AI-WORKFLOW-RULES.md`、`docs/project-memory.md` 或 `docs/ai-context.md`。

如果没有合适文件，并且用户希望保存长期上下文，则在已有文档目录中创建：

```text
docs/ai-memory-summary.md
```

整理长期历史时使用：

```text
workflows/common/iteration-memory-management-workflow.md
templates/common/iteration-memory-summary-template.md
```

## 目录说明

```text
workflows/      产品经理工作流和必要通用工作流
templates/      产品经理模板、必要 meta 模板和通用记忆模板
scorecards/     输出评分表
knowledge/      产品经理能力体系说明
roles/          产品经理角色定义
examples/       示例说明
integrations/   Codex 和 Cursor 使用说明
INSTALL.md      首次接入说明
SKILL.md        Codex skill 草稿
manifest.md     来源清单和维护说明
usage-guide.md  使用指南
```

## 推荐阅读顺序

1. `START-HERE.md`
2. `usage-guide.md`
3. `workflows/product-manager/product-manager-workflow.md`
4. `knowledge/product-manager-capability-system.md`
5. 具体任务对应的 workflow、template 和 scorecard。

## 工具集成

Codex 使用说明：

```text
integrations/codex-usage.md
```

Cursor 使用说明：

```text
integrations/cursor-usage.md
```

## 常用启动话术

### 从模糊想法开始

```text
请参考 workflows/product-manager/product-manager-workflow.md。
我的想法是：我想做一个 AI 提示词模板管理工具。
请先判断任务类型，再输出下一步应该生成什么文档。
```

### 生成 PRD

```text
请参考 workflows/product-manager/prd-generation-workflow.md 和 templates/product-manager/prd-template.md。
以下是我的需求分析结果：{粘贴内容}
请生成 PRD，并保留待确认问题。
```

### 评估需求变更

```text
请参考 workflows/product-manager/requirement-change-evaluation-workflow.md。
当前版本已经进入开发，但现在新增了这个需求：{变更内容}
请评估是否应该接入当前版本。
```

## 维护说明

本能力包来源于 WorkflowProject。

本包不使用版本号。后续维护以“导出时间”为准。

如果 WorkflowProject 中产品经理能力发生变化，应重新执行能力导出工作流，并更新：

```text
START-HERE.md
README.md
manifest.md
```
