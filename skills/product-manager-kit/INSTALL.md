# 接入说明

导出时间：2026-10-13

## 这个文件解决什么问题

这个文件用于告诉使用者：把 `product-manager-kit` 复制到一个新项目后，第一步该怎么接入、怎么启动、怎么验证是否生效。

## 推荐放置位置

把整个目录复制到目标项目根目录：

```text
your-project/
├── product-manager-kit/
├── docs/
└── README.md
```

如果目标项目已经有统一的 AI 能力目录，也可以放到那里，例如：

```text
your-project/
└── ai-kits/
    └── product-manager-kit/
```

放到非根目录时，启动话术里的路径也要对应调整。

## 最快验证方式

复制完成后，在新 AI 对话里输入：

```text
请只参考 product-manager-kit/ 下的文件工作。请先阅读 product-manager-kit/START-HERE.md、product-manager-kit/usage-guide.md 和 product-manager-kit/workflows/product-manager/product-manager-workflow.md。

我想验证 product-manager-kit 是否生效：我有一个模糊产品想法，想做一个 AI 提示词模板管理工具。请先判断当前阶段，并告诉我下一步应该产出什么。
```

如果 AI 正确输出以下内容，说明接入基本生效：

- 当前阶段。
- 任务判断。
- 使用的 workflow。
- 是否需要用户确认。
- 下一阶段。
- 不直接跳到 PRD。

## 默认自动读取配置

如果希望用户不必每次输入“请使用 product-manager-kit”，可以在目标项目根目录创建：

```text
AI-WORKFLOW-RULES.md
```

写入：

```text
你是当前项目的 AI 产品经理协作调度器。

当用户提出产品想法、需求、PRD、验收标准、版本规划、用户反馈、竞品分析或产品复盘相关任务时，请先检查是否存在 product-manager-kit/。

如果存在，请先阅读：
1. product-manager-kit/START-HERE.md
2. product-manager-kit/usage-guide.md
3. product-manager-kit/workflows/product-manager/product-manager-workflow.md

执行时必须输出：
- 当前阶段
- 任务判断
- 使用工作流
- 使用模板
- 检查标准
- 是否需要用户确认
- 下一步

不要把单个文档输出当作任务结束。每个阶段结束后，都要判断是否进入下一阶段。
进入 PRD、版本规划或开发交接前，必须确认范围、边界、风险和待确认问题。
当目标用户、场景、范围、优先级、验收标准或决策人不明确时，必须先询问用户。
```

## 第一次使用建议

不要一上来直接让 AI 写 PRD。

建议按下面顺序验证：

1. 给一个模糊想法，让 AI 先做想法标准化。
2. 让 AI 进入需求分析。
3. 让 AI 判断是否可以进入 PRD。
4. 确认后再让 AI 生成 PRD。
5. 检查 AI 是否继续判断验收标准、功能规划和版本规划。

## 常见错误

| 错误 | 后果 | 正确做法 |
| --- | --- | --- |
| 直接说“帮我写 PRD” | AI 可能跳过需求分析 | 先要求使用产品经理总入口判断阶段 |
| 复制了 product-manager-kit 但没告诉 AI | AI 不会自动知道要用 | 增加 `AI-WORKFLOW-RULES.md` 或启动话术 |
| 把需求分析当成终点 | 后续 PRD 和验收缺失 | 阶段结束后判断下一步 |
| 没有结束标准 | AI 输出一个文档就停 | 要求输出当前阶段、下一步和是否需要确认 |
