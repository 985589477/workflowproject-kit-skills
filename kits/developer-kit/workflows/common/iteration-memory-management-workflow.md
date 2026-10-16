# 迭代记忆管理工作流

## 目的

当项目经过多轮产品、开发、设计、测试或复盘迭代后，帮助 AI 把大量历史记录整理成可继续使用的项目记忆，降低后续上下文读取成本。

本工作流不删除历史，而是把历史压缩成“当前继续项目真正需要知道的摘要”。

## 记忆文件位置

如果在 WorkflowProject 内部项目中使用，默认更新：

```text
00-progress/memory-summary.md
```

如果在外部项目或导出能力包中使用，优先使用项目已有记忆文件，例如：

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

## 适用场景

适用于：

- 项目持续迭代，`progress-log.md` 越来越长。
- 每次继续项目都需要读大量历史。
- 项目阶段完成，需要整理当前状态。
- 能力建设项目准备沉淀或导出。
- 真实项目需要长期维护。
- 用户觉得项目记录太多，不知道当前重点是什么。

## 输入要求

优先读取：

```text
README.md
00-progress/next-actions.md
00-progress/progress-log.md
00-progress/decision-log.md
```

按需读取：

```text
{目标文档目录}/
{目标文档目录}/
05-review/
06-lessons/
```

## 执行步骤

1. 读取当前入口文件，整理项目状态。
2. 提取当前目标、当前阶段、有效进展、已完成内容、有效决策、可用资产和下一步。
3. 识别已废弃方向、过期计划和不再需要每次阅读的历史。
4. 列出需要追溯时再读取的文件。
5. 创建或更新项目记忆摘要。WorkflowProject 内部使用 `00-progress/memory-summary.md`，外部项目优先使用已有记忆文件或 `docs/ai-memory-summary.md`。
6. 确保 `00-progress/next-actions.md` 与记忆摘要一致。
7. 在 `progress-log.md` 中记录本轮整理动作。

## 推荐输出结构

```md
# 迭代记忆整理结果

## 当前状态

## 已压缩的历史范围

## 当前有效决策

## 已废弃方向

## 后续优先读取文件

## 需要追溯时再读取的文件

## 下一步建议
```

## 质量要求

- 必须生成或更新项目记忆摘要。
- 必须区分当前有效信息和历史证据。
- 必须列出需要追溯时再读的文件。
- 不删除历史记录。
- 不把 AI 推断写成事实。
