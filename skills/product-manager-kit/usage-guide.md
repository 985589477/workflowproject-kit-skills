# 使用指南

导出时间：2026-10-13

## 最快启动

在新项目或新 AI 对话里复制：

```text
请只参考 product-manager-kit/ 下的文件工作。请先阅读 product-manager-kit/README.md、product-manager-kit/usage-guide.md 和 product-manager-kit/workflows/product-manager/product-manager-workflow.md。我的产品想法是：{写下你的想法}。请先判断任务类型，再说明会使用哪个 workflow、template 和 scorecard，然后继续产出结果。
```

## 第一步：判断你现在要做什么

如果你不确定，使用：

```text
workflows/product-manager/product-manager-workflow.md
```

它会帮你判断当前任务属于哪个产品阶段，并决定是进入单个细分工作流，还是按完整产品生命周期继续推进。

## 第零步：第一次接入

如果这是第一次在某个项目中使用 product-manager-kit，先阅读：

```text
INSTALL.md
```

然后用快速示例验证：

```text
examples/quick-start-example.md
```

## 第二步：选择对应工作流

| 你想做什么 | 使用文件 |
| --- | --- |
| 把想法整理成标准输入 | `workflows/common/idea-to-input-workflow.md` |
| 分析需求 | `workflows/product-manager/requirement-analysis-workflow.md` |
| 写 PRD | `workflows/product-manager/prd-generation-workflow.md` |
| 写验收标准 | `workflows/product-manager/acceptance-criteria-workflow.md` |
| 拆功能范围 | `workflows/product-manager/feature-planning-workflow.md` |
| 写用户故事 | `workflows/product-manager/user-story-workflow.md` |
| 整理用户反馈 | `workflows/product-manager/user-feedback-workflow.md` |
| 分析竞品 | `workflows/product-manager/competitor-analysis-workflow.md` |
| 判断优先级 | `workflows/product-manager/priority-decision-workflow.md` |
| 规划版本 | `workflows/product-manager/version-planning-workflow.md` |
| 判断方向是否值得做 | `workflows/product-manager/product-strategy-workflow.md` |
| 管理需求池 | `workflows/product-manager/requirement-pool-workflow.md` |
| 做产品路线图 | `workflows/product-manager/product-roadmap-workflow.md` |
| 评估需求变更 | `workflows/product-manager/requirement-change-evaluation-workflow.md` |
| 做版本复盘 | `workflows/product-manager/version-retrospective-workflow.md` |
| 整理长期迭代记忆 | `workflows/common/iteration-memory-management-workflow.md` |

## 第三步：使用模板生成结果

每个产品经理工作流通常对应一个模板：

```text
templates/product-manager/
```

例如：

```text
prd-generation-workflow.md
-> prd-template.md
-> prd-scorecard.md
```

## 第四步：用评分表检查结果

生成结果后，到：

```text
scorecards/
```

选择对应评分表检查输出是否合格。

## 第五步：按产品生命周期推进

product-manager-kit 不应该在某一个文档输出后自动停止。

当任务从想法进入产品文档时，默认链路是：

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

如果只执行其中一部分，必须说明：

- 为什么本次只做到这里。
- 下一步应该进入哪里。
- 是否需要用户确认。

进入 PRD、版本规划或开发交接前，必须先确认范围、边界、风险和待确认问题。

如果目标用户、场景、范围、优先级、验收或决策人不明确，先问用户，不要替用户做关键决定。

## 第六步：持续输出执行状态

每次阶段切换时，使用以下格式：

```text
当前阶段：
任务判断：
使用工作流：
使用模板：
检查标准：
是否需要用户确认：
已完成：
正在执行：
下一步：
```

## 第七步：判断任务是否结束

任务结束前必须回答：

- 当前阶段是否完成。
- 下一阶段是什么。
- 是否需要用户确认。
- 如果停止，为什么停止。
- 是否存在待确认问题。
- 是否需要继续生成 PRD、验收标准、功能规划或版本规划。
- 是否需要进入需求池、路线图、变更评估或复盘。

## 第八步：决定是否保存文件

如果只是让 AI 在对话里输出结果，不需要创建文件。

如果你希望把结果保存到当前项目，请按下面顺序选择输出位置：

1. 用户明确指定输出目录时，使用用户指定目录。
2. 当前项目已有统一文档目录时，使用已有目录，例如 `docs/`、`documents/`、`产品文档/`、`需求文档/`。
3. 当前项目已有产品文档目录时，使用该目录，例如 `docs/product/`、`docs/prd/`、`product-docs/`。
4. 如果没有合适目录，再在项目根目录创建 `docs/`。

不要把 WorkflowProject 内部目录习惯带到外部项目，不要默认创建：

```text
{目标文档目录}/
12-projects/
```

## 第九步：长期迭代记忆管理

如果同一个项目会持续进行产品迭代，建议维护：

```text
docs/ai-memory-summary.md
```

如果项目已有 `AGENTS.md`、`AI-WORKFLOW-RULES.md`、`docs/project-memory.md` 或 `docs/ai-context.md`，优先沿用已有文件。

每轮任务结束时，如果产生新的关键结论、产品决策、范围变化、版本计划、需求池变化、风险或下一步，应更新记忆摘要。

整理长期历史时使用：

```text
workflows/common/iteration-memory-management-workflow.md
templates/common/iteration-memory-summary-template.md
```

## 推荐执行方式

对 AI 说：

```text
请先阅读以下文件：
1. workflows/product-manager/product-manager-workflow.md
2. knowledge/product-manager-capability-system.md

我的任务是：{你的任务}

请先判断当前阶段、任务类型、会使用哪个 workflow、template 和 scorecard，并说明下一步是否需要用户确认。
```

## 导出时间管理

本能力包不使用版本号。

判断是否是最新包时，只看：

```text
导出时间
```

导出时间记录在：

```text
START-HERE.md
README.md
manifest.md
```

## 不建议的用法

- 不要一上来让 AI 直接写 PRD，除非你已经有清晰需求分析。
- 不要把用户反馈直接变成版本规划，应先整理反馈和判断优先级。
- 不要在需求变更时直接修改 PRD，应先做变更评估。
- 不要把复盘写成泛泛总结，应对比原计划和实际结果。
