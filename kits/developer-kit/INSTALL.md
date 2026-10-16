# 接入说明

导出时间：2026-10-14

## 这个文件解决什么问题

这个文件用于告诉使用者：把 `developer-kit` 复制到一个新项目后，第一步该怎么接入、怎么启动、怎么验证是否生效。

## 推荐放置位置

把整个目录复制到目标项目根目录：

```text
your-project/
├── developer-kit/
├── src/
├── docs/
└── README.md
```

如果目标项目已经有统一的 AI 能力目录，也可以放到那里，例如：

```text
your-project/
└── ai-kits/
    └── developer-kit/
```

放到非根目录时，启动话术里的路径也要对应调整。

## 最快验证方式

复制完成后，在新 AI 对话里输入：

```text
请只参考 developer-kit/ 下的文件工作。请先阅读 developer-kit/START-HERE.md、developer-kit/usage-guide.md 和 developer-kit/workflows/developer/developer-kit-workflow.md。

我想验证 developer-kit 是否生效：请理解当前项目结构，并告诉我如果后续要新增一个功能，应该先走哪些阶段。
```

如果 AI 正确输出以下内容，说明接入基本生效：

- 任务判断。
- 当前阶段。
- 使用的 workflow。
- 风险等级。
- 是否需要用户确认。
- 下一阶段。
- 不直接跳到代码实现。

## 默认自动读取配置

如果希望用户不必每次输入“请使用 developer-kit”，可以在目标项目根目录创建：

```text
AI-WORKFLOW-RULES.md
```

写入：

```text
你是当前项目的 AI 开发协作调度器。

当用户提出开发、代码、架构、测试、文档、发布或项目治理相关需求时，请先检查是否存在 developer-kit/。

如果存在，请先阅读：
1. developer-kit/START-HERE.md
2. developer-kit/usage-guide.md
3. developer-kit/workflows/developer/developer-kit-workflow.md

执行时必须输出：
- 当前阶段
- 任务判断
- 使用工作流
- 执行方式
- 风险等级
- 是否需要用户确认
- 下一步

不要把单个工作流当作结束点。每个阶段结束后，都要判断是否进入下一阶段。
进入代码实现前，必须先形成整体功能规划。
当需求、范围、方案、验收或风险不明确时，必须先询问用户。
```

## Codex 使用

Codex 更适合项目级执行。

推荐说法：

```text
请使用 developer-kit 协助我处理这个开发任务：{任务}。
请先阅读 developer-kit/START-HERE.md 和 developer-kit/workflows/developer/developer-kit-workflow.md。
先判断阶段和风险，不要直接写代码。
```

更详细说明见：

```text
integrations/codex-usage.md
```

## Cursor 使用

Cursor 更适合 IDE 内持续协作。

推荐把 `AI-WORKFLOW-RULES.md` 或 `START-HERE.md` 中的关键规则放到 Cursor 的项目规则里。

更详细说明见：

```text
integrations/cursor-usage.md
```

## 第一次使用建议

不要一上来做高风险改动。

建议按下面顺序验证：

1. 让 AI 理解项目结构。
2. 给一个小功能，让 AI 做影响范围分析。
3. 让 AI 输出整体功能规划。
4. 确认后再让 AI 实现。
5. 检查 AI 是否进行了测试、文档同步和后续阶段判断。

## 常见错误

| 错误 | 后果 | 正确做法 |
| --- | --- | --- |
| 只说“帮我改代码” | AI 可能跳过规划 | 先要求使用 developer-kit 判断阶段 |
| 复制了 developer-kit 但没告诉 AI | AI 不会自动知道要用 | 增加 `AI-WORKFLOW-RULES.md` 或启动话术 |
| 让 AI 直接实现复杂需求 | 容易破坏模块边界 | 先做需求理解、项目理解和功能规划 |
| 没有结束标准 | AI 做到一半就停 | 要求输出当前阶段、下一步和是否需要确认 |
