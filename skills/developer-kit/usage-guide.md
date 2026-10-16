# 使用指南

导出时间：2026-10-14

## 最快启动

在新项目或新 AI 对话里复制：

```text
请只参考 developer-kit/ 下的文件工作。请先阅读 developer-kit/README.md、developer-kit/usage-guide.md 和 developer-kit/workflows/developer/developer-kit-workflow.md。我的开发任务是：{写下你的任务}。请先判断任务类型，再说明会使用哪个 workflow、template 和 scorecard，然后继续执行。
```

## 第零步：第一次接入

如果这是第一次在某个项目中使用 developer-kit，先阅读：

```text
INSTALL.md
```

然后用快速示例验证：

```text
examples/quick-start-example.md
```

## 第一步：判断你现在要做什么

如果你不确定，先使用：

```text
workflows/developer/developer-kit-workflow.md
```

它会帮 AI 判断当前任务属于哪个阶段，并决定是进入单个细分工作流，还是按完整开发生命周期继续推进。

## 第二步：选择对应工作流

| 你想做什么 | 使用文件 |
| --- | --- |
| 启动一个新开发项目 | `workflows/developer/project-bootstrap-workflow.md` |
| 接手和理解已有项目 | `workflows/developer/project-understanding-workflow.md` |
| 把需求转换成技术影响 | `workflows/developer/requirement-to-architecture-workflow.md` |
| 判断模块职责和边界 | `workflows/developer/module-boundary-analysis-workflow.md` |
| 判断改动风险 | `workflows/developer/change-risk-assessment-workflow.md` |
| 分析影响范围 | `workflows/developer/impact-analysis-workflow.md` |
| 判断是否需要写代码、避免过度设计 | `workflows/developer/minimal-change-governance-workflow.md` |
| 定位报错、白屏、测试失败或性能异常 | `workflows/developer/issue-diagnosis-workflow.md` |
| 定义数据/API/状态契约 | `workflows/developer/data-api-contract-workflow.md` |
| 检查安全、权限和敏感数据风险 | `workflows/developer/security-permission-workflow.md` |
| 编排多个开发工作流 | `workflows/developer/workflow-orchestration-guide.md` |
| 整理长期迭代记忆 | `workflows/common/iteration-memory-management-workflow.md` |
| 执行代码实现 | `workflows/developer/implementation-workflow.md` |
| 做测试和验收 | `workflows/developer/testing-verification-workflow.md` |
| 同步文档 | `workflows/developer/documentation-sync-workflow.md` |
| 做代码评审 | `workflows/developer/code-review-workflow.md` |
| 记录架构决策 | `workflows/developer/architecture-decision-record-workflow.md` |
| 管理依赖和技术债 | `workflows/developer/dependency-and-tech-debt-workflow.md` |
| 管理环境配置 | `workflows/developer/environment-config-governance-workflow.md` |
| 准备发布和回滚 | `workflows/developer/release-and-rollback-workflow.md` |
| 复盘 AI 协作 | `workflows/developer/ai-collaboration-retrospective-workflow.md` |

## 第三步：使用模板生成结果

每个开发工作流通常对应一个模板：

```text
templates/developer/
```

例如：

```text
implementation-workflow.md
-> implementation-template.md
-> implementation-scorecard.md
```

最小必要变更判断对应：

```text
minimal-change-governance-workflow.md
-> minimal-change-governance-template.md
-> minimal-change-governance-scorecard.md
```

## 第四步：用评分表检查结果

生成结果后，到：

```text
scorecards/
```

选择对应评分表检查输出是否合格。

## 第五步：决定执行方式

根据任务风险选择执行方式：

| 风险 | 执行方式 |
| --- | --- |
| 低风险 | 可以直接实现，并说明验证结果 |
| 中风险 | 先说明影响范围和计划，再实现 |
| 高风险 | 先输出方案、风险、回滚策略和待确认问题 |

## 第六步：按开发生命周期推进

developer-kit 不应该在某一个工作流结束后自动停止。

当任务从需求进入开发时，默认链路是：

```text
需求理解
-> 是否确认进入开发
-> 项目理解
-> 功能整体规划
-> 数据/API/状态契约检查
-> 安全与权限检查
-> 风险和影响范围确认
-> 最小必要变更判断
-> 代码实现
-> 测试验证
-> 文档同步
-> 代码评审
-> 发布或复盘判断
```

如果只执行其中一部分，必须说明：

- 为什么本次只做到这里。
- 下一步应该进入哪里。
- 是否需要用户确认。

进入代码实现前，必须先输出整体功能规划。

如果任务是报错、白屏、测试失败或性能异常，进入实现前应先使用 `issue-diagnosis-workflow.md` 定位根因。

如果任务涉及接口字段、数据结构、状态归属、缓存、错误处理或前后端协作，进入实现前应先使用 `data-api-contract-workflow.md` 明确契约。

如果任务涉及登录、鉴权、角色权限、敏感数据、密钥、上传下载、支付、删除或批量操作，进入实现前应先使用 `security-permission-workflow.md` 做安全与权限检查。

如果执行过程中发现需要插入、回退、跳过或暂停确认，应参考 `workflow-orchestration-guide.md`。

进入代码实现前，应使用 `minimal-change-governance-workflow.md` 做最小必要变更判断，避免过度设计、过早抽象和不必要依赖。

最小必要变更判断必须回答：

- 这个需求是否真的需要新增代码。
- 是否可复用项目已有能力。
- 是否可使用平台能力、语言标准库或框架原生能力。
- 是否可使用已安装依赖，而不是新增依赖。
- 如果必须新增代码，最小完整方案是什么。
- 本次明确不做什么。
- 哪些安全、校验、错误处理、可访问性和测试不能省略。

进入代码实现前，还必须检查项目已有规范，包括：

- 设计规范、组件规范、交互规范、视觉规范。
- 代码风格、架构约束、目录约定、命名规范。
- 测试规范、文档规范。
- AI 协作规则，例如 `AGENTS.md`、`AI-WORKFLOW-RULES.md`、`.cursor/rules/`。

如果存在这些规范，必须先阅读并遵守；如果不存在，需要说明缺失项，并根据风险决定是从现有代码归纳临时约定、先补充规范，还是向用户确认。

中高风险实现前，必须先输出开发任务列表，并按任务逐条实现、逐条验证。

如果需求、范围、方案、验收或风险不明确，先问用户，不要替用户做关键决定。

## 第七步：持续输出执行状态

每次阶段切换时，使用以下格式：

```text
当前阶段：
任务判断：
使用工作流：
执行方式：
风险等级：
是否需要用户确认：
已完成：
正在执行：
下一步：
```

这样用户可以知道 AI 现在做到哪一步，而不是只看到最终结果。

## 第八步：判断任务是否结束

任务结束前必须回答：

- 当前阶段是否完成。
- 下一阶段是什么。
- 是否需要用户确认。
- 如果停止，为什么停止。
- 如果实现了代码，验证结果是什么。
- 是否需要文档同步、代码评审、发布判断或复盘。

## 第九步：决定是否保存文档

如果只是让 AI 在对话里输出结果，不需要创建文件。

如果你希望把分析、方案或报告保存到当前项目，请按下面顺序选择输出位置：

1. 用户明确指定输出目录时，使用用户指定目录。
2. 当前项目已有统一文档目录时，使用已有目录，例如 `docs/`、`documents/`、`工程文档/`、`技术文档/`。
3. 当前项目已有开发文档目录时，使用该目录，例如 `docs/dev/`、`docs/engineering/`、`technical-docs/`。
4. 如果没有合适目录，再在项目根目录创建 `docs/`。

不要把 WorkflowProject 内部目录习惯带到外部项目，不要默认创建：

```text
{目标文档目录}/
12-projects/
```

## 第十步：长期迭代记忆管理

如果同一个项目会持续开发，建议维护：

```text
docs/ai-memory-summary.md
```

如果项目已有 `AGENTS.md`、`AI-WORKFLOW-RULES.md`、`docs/project-memory.md` 或 `docs/ai-context.md`，优先沿用已有文件。

每轮开发任务结束时，如果产生新的关键结论、架构决策、模块边界变化、风险、验证结果、待处理任务或下一步，应更新记忆摘要。

整理长期历史时使用：

```text
workflows/common/iteration-memory-management-workflow.md
templates/common/iteration-memory-summary-template.md
```

## 推荐执行方式

对 AI 说：

```text
请先阅读以下文件：
1. workflows/developer/README.md
2. workflows/developer/developer-kit-workflow.md
3. knowledge/developer-governance-capability-system.md

我的开发任务是：{你的任务}

请先判断任务类型、风险等级、会使用哪个 workflow、template 和 scorecard。
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

- 不要让 AI 跳过项目理解直接大范围改代码。
- 不要在没有检查项目规范的情况下直接实现代码，尤其是 UI、组件、交互、视觉和架构类改动。
- 不要把所有任务都走完整流程，小任务应该轻量执行。
- 不要把文档当成限制 AI 能力的边界，文档应该约束目标、风险和验收。
- 不要让模块边界分析停留在目录描述，必须说明职责、依赖和禁止跨越的边界。
- 不要只实现不验证，也不要只验证不说明剩余风险。
