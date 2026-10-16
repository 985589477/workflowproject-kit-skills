# 使用指南

导出时间：2026-10-15

## 最快启动

在新项目或新 AI 对话里复制：

```text
请只参考 team-orchestration-kit/ 下的文件工作。请先阅读 team-orchestration-kit/README.md、team-orchestration-kit/usage-guide.md 和 team-orchestration-kit/workflows/mixed/team-orchestration-workflow.md。我的任务是：{写下你的任务}。请先判断需要哪些角色参与、谁先接管、会使用哪些 workflow、template 和 scorecard，然后按阶段推进。
```

## 第零步：第一次接入

如果这是第一次在某个项目中使用 team-orchestration-kit，先阅读：

```text
INSTALL.md
```

然后用快速示例验证：

```text
examples/quick-start-example.md
```

## 第一步：判断是否跨角色

如果外部项目中存在 `team-orchestration-kit`，产品、UI、开发、测试相关任务默认先由总调度入口接管。

总调度先判断任务是否跨角色，再决定是否转交具体角色包。

这里还必须判断是否需要创建子 Agent：

- 单角色、单产出、无交接、无并行：当前 Agent 直接调用 Skill，不创建子 Agent。
- 多角色、多阶段、需要交接、联合验收或并行：父 Agent 创建真实子 Agent。
- 当前运行环境没有真实子 Agent 工具：先向用户报告，未经确认不得伪装成子 Agent 或直接降级执行。

只有在以下情况，才让具体角色包直接接管：

- 当前项目没有 `team-orchestration-kit`。
- 用户明确指定只使用某个角色包。
- 总调度已经判断这是纯单角色轻量任务，并说明不需要跨角色协作。

如果任务涉及多个阶段、多个角色、交接检查或最终验收，使用：

```text
workflows/mixed/team-orchestration-workflow.md
```

每次输出都要声明执行模式：

```text
执行模式：单 Agent + Skill / 父 Agent + 子 Agent / 单 Agent 降级模拟，不是真实子 Agent
```

## 第二步：判断参与角色

| 输入特征 | 优先接管角色 | 后续协作角色 |
| --- | --- | --- |
| 只有想法、业务目标、用户问题 | 产品经理 | UI、开发、测试 |
| 已有 PRD，需要页面方案 | UI 设计师 | 产品、开发、测试 |
| 已有明确需求和设计，需要实现 | 开发工程师 | 产品、UI、测试 |
| 已有开发变更，需要验证 | 测试工程师 | 产品、开发、UI |
| 用户反馈 bug | 测试工程师 | 开发、产品、UI |
| 上线前检查 | 测试工程师 | 产品、开发、UI |
| 需求跨越多个角色且不明确 | 总调度先接管 | 按阶段逐步调度 |

## 第三步：选择对应能力包

| 角色 | 使用能力包 |
| --- | --- |
| 产品经理 | `product-manager-kit/` |
| UI 设计师 | `ui-designer-kit/` |
| 开发工程师 | `developer-kit/` |
| 测试工程师 | `tester-kit/` |
| 跨角色调度 | `team-orchestration-kit/` |

## 第四步：使用模板

跨角色调度模板：

```text
templates/mixed/team-orchestration-template.md
```

创建子 Agent 时补充阅读：

```text
templates/common/agent-task-brief-template.md
templates/common/agent-result-report-template.md
```

长期迭代记忆模板：

```text
templates/common/iteration-memory-summary-template.md
```

## 第五步：用评分表检查

跨角色总调度评分表：

```text
scorecards/team-orchestration-scorecard.md
```

检查重点：

- 是否正确判断参与角色。
- 是否说明当前接管角色。
- 是否检查上下游交接。
- 是否说明跳过角色的理由。
- 是否输出阻塞和 badcase。
- 是否判断下一阶段。

## 第六步：按团队生命周期推进

默认链路：

```text
用户输入
-> 需求识别和角色判断
-> 产品经理接管
-> UI 设计师接管
-> 开发工程师接管
-> 测试工程师接管
-> 跨角色互审
-> 交付结论
-> badcase 反馈和能力优化建议
```

不是每个任务都必须经过所有角色。跳过任何角色时必须说明理由。

## 第七步：交接不通过时怎么做

如果任何角色看不懂上游产物，必须停止推进并输出：

```text
协作阻塞：{阻塞点}
发现角色：{角色}
来源角色：{角色}
问题类型：{需求不清 / 设计不清 / 技术边界不清 / 验收标准不清 / 测试不可执行 / 其他}
影响：{会影响什么}
建议补充：{问题列表}
建议回到：{角色能力包 + 工作流}
badcase 记录建议：{建议保存到哪里}
```

## 第八步：外部项目保存位置

如果只是对话中直接输出结果，不需要创建文件。

如果用户要求保存文件，按优先级选择：

1. 用户指定目录。
2. 项目已有统一文档目录，例如 `docs/`、`documents/`。
3. 项目已有协作文档目录，例如 `docs/team/`、`docs/workflow/`、`docs/delivery/`。
4. 没有合适目录时，在项目根目录创建 `docs/`。

不要默认创建：

```text
{目标文档目录}/
12-projects/
```

## 第九步：长期迭代记忆管理

如果同一个项目会长期使用本包，建议维护：

```text
docs/ai-memory-summary.md
```

如果项目已有 `AGENTS.md`、`AI-WORKFLOW-RULES.md`、`docs/project-memory.md` 或 `docs/ai-context.md`，优先沿用已有文件。

整理长期历史时使用：

```text
workflows/common/iteration-memory-management-workflow.md
templates/common/iteration-memory-summary-template.md
```

## 推荐执行方式

对 AI 说：

```text
请先阅读以下文件：
1. team-orchestration-kit/START-HERE.md
2. team-orchestration-kit/workflows/mixed/team-orchestration-workflow.md
3. team-orchestration-kit/templates/mixed/team-orchestration-template.md

我的任务是：{你的任务}

请先判断任务类型、参与角色、当前接管角色、会使用哪个 workflow、template 和 scorecard。
```
