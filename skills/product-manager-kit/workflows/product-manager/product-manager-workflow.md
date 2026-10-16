# 产品经理总入口工作流

## 目的

这是产品经理角色的总入口。

当用户不确定该使用哪个产品经理工作流，或只给出一个模糊想法、原始材料、业务问题、产品问题时，先使用本工作流进行判断和调度。

本工作流不是“命中一个细分工作流就结束”的路由器，而是产品工作主流程。

本工作流不负责替代所有细分工作流，而是负责：

1. 把模糊想法转成可处理输入。
2. 判断当前任务类型。
3. 选择正确的产品经理细分工作流。
4. 说明为什么调度这个工作流。
5. 编排从想法到版本复盘的完整产品链路。
6. 在进入 PRD、版本规划或开发交接前确认范围、边界和待确认问题。
7. 在信息不足、方向不明确或影响范围较大时主动询问用户。
8. 明确产出位置、评审方式和后续流转。

## 什么时候使用

当你不知道该选哪个产品经理工作流时，使用它。

典型说法：

```text
请使用产品经理总入口处理我的想法：{你的想法}
```

也可以直接说：

```text
我的想法是 {你的想法}，请帮我判断应该用哪个产品经理工作流，并继续执行。
```

## 总体原则

### 先判断，再执行

不要一上来直接写 PRD、路线图或复盘。

先判断用户当前真正需要的是：

- 把想法整理清楚。
- 分析需求。
- 生成 PRD。
- 拆功能。
- 写验收标准。
- 判断优先级。
- 规划版本。
- 管理需求池。
- 处理变更。
- 做版本复盘。

### 先进入最小正确工作流

如果任务只需要需求分析，不要直接进入 PRD。

如果任务只是一个新想法，不要直接进入版本规划。

如果任务是版本执行中新增需求，不要直接改 PRD，应先进入需求变更评估。

### 不以单个文档作为终点

完成某个产品文档不代表任务结束。

每完成一个阶段后，都必须判断：

- 当前阶段是否已经完成。
- 是否需要用户确认。
- 是否可以进入下一阶段。
- 下一阶段应该使用哪个工作流。
- 是否需要回到上一阶段补充信息。

### 关键阶段前必须确认

进入以下阶段前，必须确认输入是否足够：

- 从想法进入需求分析。
- 从需求分析进入 PRD。
- 从 PRD 进入验收标准或功能规划。
- 从功能规划进入版本规划。
- 从版本规划进入开发交接。
- 从执行中变更进入当前版本。

如果目标用户、场景、范围、优先级、约束、验收标准或决策人不清楚，应先询问用户，不要把推断写成确定结论。

### 保留解释

每次调度时都要说明：

- 当前判断是什么。
- 调用了哪个工作流。
- 为什么不是其他工作流。
- 预期会输出什么。
- 后续可能进入哪里。

## 标准产品生命周期

产品经理总入口默认按照下面生命周期推进。

不是每个任务都必须完整走完所有阶段，但跳过阶段时必须说明理由。

| 阶段 | 目标 | 默认工作流 | 是否需要用户确认 |
| --- | --- | --- | --- |
| 0. 任务识别 | 判断用户输入属于哪类产品任务 | `product-manager-workflow.md` | 不一定 |
| 1. 想法标准化 | 把模糊想法整理成可处理输入 | `idea-to-input-workflow.md` | 信息不足时需要 |
| 2. 需求分析 | 明确目标用户、场景、问题、边界和待确认问题 | `requirement-analysis-workflow.md` | 中高风险需要 |
| 3. 是否进入 PRD | 判断需求是否足够清楚，是否可以写 PRD | `requirement-analysis-scorecard.md` | 需要 |
| 4. PRD 生成 | 形成产品目标、范围、功能、非范围和风险 | `prd-generation-workflow.md` | 需要 |
| 5. 验收标准 | 明确做到什么程度算完成 | `acceptance-criteria-workflow.md` | 需要 |
| 6. 功能规划 | 拆分功能模块、依赖、优先级和边界 | `feature-planning-workflow.md` | 中高风险需要 |
| 7. 用户故事 | 用用户视角说明为什么做、谁受益、价值是什么 | `user-story-workflow.md` | 不一定 |
| 8. 优先级判断 | 多个需求或功能之间做取舍 | `priority-decision-workflow.md` | 需要 |
| 9. 版本规划 | 判断当前版本、后续版本和不做范围 | `version-planning-workflow.md` | 需要 |
| 10. 路线图或需求池 | 管理长期方向或多个需求 | `product-roadmap-workflow.md` / `requirement-pool-workflow.md` | 不一定 |
| 11. 变更评估 | 执行中出现新增需求或范围变化时评估影响 | `requirement-change-evaluation-workflow.md` | 需要 |
| 12. 复盘沉淀 | 版本完成后复盘目标、结果、问题和经验 | `version-retrospective-workflow.md` | 不一定 |

## 阶段推进规则

### 从想法到 PRD

当用户给的是模糊想法、业务问题或产品方向时，默认推进链路是：

```text
想法标准化
-> 需求分析
-> 是否确认进入 PRD
-> PRD 生成
-> 验收标准
-> 功能规划
-> 优先级或版本规划
-> 后续开发交接或需求池沉淀
```

如果用户只要求分析，不要擅自生成 PRD。

如果需求分析中存在关键待确认问题，应先标记并询问用户，不要把推断写成确定需求。

### 从已有需求分析到 PRD

当用户已经有需求分析结果时，默认推进链路是：

```text
需求分析质量检查
-> PRD 生成
-> 验收标准
-> 功能规划
-> 版本规划或开发交接
```

如果需求分析质量不足，先回到需求分析，不要直接写 PRD。

### 从反馈或竞品到产品决策

当用户提供用户反馈、竞品材料或市场信息时，默认推进链路是：

```text
资料整理
-> 用户反馈分析 / 竞品分析
-> 产品策略判断
-> 优先级判断
-> 需求池或版本规划
```

如果资料不足，应明确资料缺口。

### 从执行中变更到版本决策

当版本已经进入设计、开发、测试或上线准备，用户提出新增需求或范围变化时，默认推进链路是：

```text
变更对象确认
-> 影响范围分析
-> 是否接入当前版本
-> 更新 PRD / 验收标准 / 版本规划
-> 通知开发或测试
```

不要直接修改 PRD，应先做需求变更评估。

## 产品交付前门禁

进入 PRD、版本规划或开发交接前，必须满足以下条件：

- 已明确目标用户。
- 已明确核心场景。
- 已明确要解决的问题。
- 已明确本次范围和非范围。
- 已保留事实、推断和待确认问题。
- 已说明关键依赖、风险和约束。
- 已说明后续应该进入哪个阶段。

如果不满足，先补对应阶段，不要强行进入下一步。

## 主动询问规则

当问题不明确时，先问用户。

提问要少而关键，优先问会影响方向的问题。

推荐格式：

```text
我现在不能直接进入 {下一阶段}，因为 {原因}。
需要你确认：
1. {关键问题 1}
2. {关键问题 2}

如果你希望我先按默认假设推进，我会按 {默认假设} 处理，并把它标记为 AI 推断。
```

可以主动给出默认假设，但必须明确标记为推断，不要把推断当事实。

## 执行状态格式

每次执行前或阶段切换时，输出：

```text
当前阶段：{任务识别 / 想法标准化 / 需求分析 / PRD 生成 / 验收标准 / 功能规划 / 优先级判断 / 版本规划 / 路线图 / 需求变更评估 / 版本复盘}
任务判断：{任务类型}
使用工作流：{workflow}
使用模板：{template}
检查标准：{scorecard}
执行方式：{只分析 / 先确认后继续 / 直接产出}
是否需要用户确认：{是 / 否}
已完成：{已完成内容}
正在执行：{当前动作}
下一步：{下一阶段或等待确认}
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

如果这些信息没有说明完整，不应直接宣称任务完成。

## 输入类型判断

### 类型 1：只有模糊想法

用户只说了一个方向，例如：

```text
我想做一个会员系统。
我想优化登录流程。
我想让 AI 帮我写一个 PRD。
```

先使用：

```text
06-templates/meta/idea-to-input-generator.md
04-workflows/common/idea-to-input-workflow.md
```

产出：

```text
01-inputs/original-requirement.md
```

然后再判断进入哪个产品经理细分工作流。

### 类型 2：已有需求或业务描述

使用：

```text
04-workflows/product-manager/requirement-analysis-workflow.md
```

适合输出：

```text
{目标文档目录}/requirement-analysis.md
```

### 类型 3：已有需求分析，想写产品文档

使用：

```text
04-workflows/product-manager/prd-generation-workflow.md
```

适合输出：

```text
{目标文档目录}/prd.md
```

### 类型 4：已有 PRD 或功能说明，想让团队知道做到什么程度

使用：

```text
04-workflows/product-manager/acceptance-criteria-workflow.md
```

适合输出：

```text
{目标文档目录}/acceptance-criteria.md
```

### 类型 5：需要拆功能范围

使用：

```text
04-workflows/product-manager/feature-planning-workflow.md
```

适合输出：

```text
{目标文档目录}/feature-planning.md
```

### 类型 6：需要用用户视角讲清楚为什么做

使用：

```text
04-workflows/product-manager/user-story-workflow.md
```

适合输出：

```text
{目标文档目录}/user-story.md
```

### 类型 7：有用户反馈、客服记录、评论或吐槽

使用：

```text
04-workflows/product-manager/user-feedback-workflow.md
```

适合输出：

```text
{目标文档目录}/user-feedback-analysis.md
```

### 类型 8：有竞品资料、截图或竞品功能描述

使用：

```text
04-workflows/product-manager/competitor-analysis-workflow.md
```

适合输出：

```text
{目标文档目录}/competitor-analysis.md
```

### 类型 9：多个需求、功能或机会需要排序

使用：

```text
04-workflows/product-manager/priority-decision-workflow.md
```

适合输出：

```text
{目标文档目录}/priority-decision.md
```

### 类型 10：需要安排 v1、v1.1、v2 做什么

使用：

```text
04-workflows/product-manager/version-planning-workflow.md
```

适合输出：

```text
{目标文档目录}/version-planning.md
```

### 类型 11：需要判断一个方向值不值得做

使用：

```text
04-workflows/product-manager/product-strategy-workflow.md
```

适合输出：

```text
{目标文档目录}/product-strategy.md
```

### 类型 12：需要管理很多需求、反馈和想法

使用：

```text
04-workflows/product-manager/requirement-pool-workflow.md
```

适合输出：

```text
{目标文档目录}/requirement-pool.md
```

### 类型 13：需要规划季度、半年或年度产品方向

使用：

```text
04-workflows/product-manager/product-roadmap-workflow.md
```

适合输出：

```text
{目标文档目录}/product-roadmap.md
```

### 类型 14：项目执行中出现新增需求或范围变化

使用：

```text
04-workflows/product-manager/requirement-change-evaluation-workflow.md
```

适合输出：

```text
{目标文档目录}/requirement-change-evaluation.md
```

### 类型 15：版本完成、上线或阶段结束后需要总结

使用：

```text
04-workflows/product-manager/version-retrospective-workflow.md
```

适合输出：

```text
{目标文档目录}/version-retrospective.md
```

## 调度表

| 用户想做的事 | 优先使用的工作流 | 典型输出 |
| --- | --- | --- |
| 把模糊想法整理成输入 | `idea-to-input-workflow.md` | `original-requirement.md` |
| 分析需求是否清楚 | `requirement-analysis-workflow.md` | 需求分析 |
| 写 PRD | `prd-generation-workflow.md` | PRD |
| 明确完成标准 | `acceptance-criteria-workflow.md` | 验收标准 |
| 拆功能范围 | `feature-planning-workflow.md` | 功能规划 |
| 用用户视角表达需求 | `user-story-workflow.md` | 用户故事 |
| 整理用户反馈 | `user-feedback-workflow.md` | 反馈分析 |
| 分析竞品 | `competitor-analysis-workflow.md` | 竞品分析 |
| 判断先做什么 | `priority-decision-workflow.md` | 优先级建议 |
| 规划版本阶段 | `version-planning-workflow.md` | 版本规划 |
| 判断方向是否值得做 | `product-strategy-workflow.md` | 策略判断 |
| 管理多个需求 | `requirement-pool-workflow.md` | 需求池 |
| 规划中长期方向 | `product-roadmap-workflow.md` | 产品路线图 |
| 评估需求变更 | `requirement-change-evaluation-workflow.md` | 变更评估 |
| 复盘版本结果 | `version-retrospective-workflow.md` | 版本复盘 |

## 标准执行流程

### 第 1 步：确认输入是否足够

如果用户只有一句话想法，先生成标准输入。

如果用户已经提供材料，先判断材料属于哪类任务。

### 第 2 步：说明调度判断

输出类似：

```text
我判断这次任务属于 {任务类型}。
建议使用 {工作流路径}。
原因是 {选择理由}。
本次预计输出 {输出文档}。
后续可能进入 {后续工作流}。
```

### 第 3 步：进入细分工作流

按照对应细分工作流的输入要求、执行步骤、输出结构和质量标准执行。

### 第 4 步：输出并评审

生成输出后，使用对应评分表或 `06-templates/meta/output-reviewer.md` 评审。

评分表优先使用：

```text
11-evaluations/output-scorecards/
```

### 第 5 步：判断后续流转

根据输出结果，判断下一步进入：

- 需求池。
- 需求分析。
- PRD。
- 验收标准。
- 优先级判断。
- 版本规划。
- 产品路线图。
- 需求变更评估。
- 版本复盘。
- 暂停并沉淀。

## 保存和项目记录策略

如果只是在外部项目临时问答，可以直接引用本工作流，不一定创建项目记录。

如果用户要求保存输出文档，使用目标项目的文档目录：

```text
{目标文档目录}/
```

目标文档目录的选择规则：

1. 用户明确指定输出目录时，使用用户指定目录。
2. 项目已有统一文档目录时，使用已有目录，例如 `docs/`、`documents/`、`产品文档/`、`需求文档/`。
3. 项目已有产品文档目录时，使用该目录，例如 `docs/product/`、`docs/prd/`、`product-docs/`。
4. 如果没有合适目录，再在项目根目录创建 `docs/`。

不要在外部项目中默认创建或使用 WorkflowProject 内部目录，例如：

```text
{目标文档目录}/
12-projects/
```

如果是在 WorkflowProject 内部保存真实执行过程，使用真实项目目录：

```text
12-projects/product-manager/real-cases/{项目名}/
```

如果是建设或优化某个能力，使用能力建设目录：

```text
12-projects/product-manager/capability-building/{能力名}/
```

## 使用示例

### 示例 1：从想法开始

```text
请使用产品经理总入口处理我的想法：
我想做一个 AI 提示词模板管理工具，可以帮我判断应该先产出什么。
```

预期调度：

```text
idea-to-input -> requirement-analysis -> prd-generation
```

### 示例 2：已有需求分析，生成 PRD

```text
请参考 04-workflows/product-manager/product-manager-workflow.md。
我已经有需求分析结果，请帮我生成 PRD。
```

预期调度：

```text
prd-generation-workflow.md
```

### 示例 3：中途来了新增需求

```text
当前版本已经进入开发，但业务方临时要求新增导出功能，请帮我判断要不要接。
```

预期调度：

```text
requirement-change-evaluation-workflow.md
```

### 示例 4：版本上线后总结

```text
这个版本已经上线，请帮我复盘目标达成、问题和下一步改进。
```

预期调度：

```text
version-retrospective-workflow.md
```

## 质量检查

使用本总入口时检查：

- 是否先判断任务类型。
- 是否说明调度理由。
- 是否选择了正确细分工作流。
- 是否没有跳过标准输入。
- 是否保留事实、推断和待确认问题。
- 是否明确输出文档。
- 是否说明后续流转。
- 是否使用对应评分表或评审模板。

## 注意事项

- 本文件是总入口，不是所有产品文档的万能模板。
- 明确任务类型后，应进入对应细分工作流。
- 如果任务跨多个阶段，可以串联多个工作流，但每一步都要说明当前阶段。
- 如果任务涉及 UI、开发或测试，应先完成产品目标、范围、PRD 或验收标准，再交给对应角色。
