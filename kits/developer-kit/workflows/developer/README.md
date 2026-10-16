# 开发工程师工作流

这里放开发角色相关工作流，例如需求到技术方案、bug 到调试计划、代码到审查报告。

## 当前能力总纲

开发角色后续建设应优先参考：

```text
10-knowledge-base/patterns/developer-governance-capability-system.md
```

developer-kit 的定位不是教 AI 写代码，而是让 Codex、Cursor 等 AI 开发工具在项目中稳定协作、理解结构、控制风险、维护模块边界并完成交付闭环。

## 总入口使用方式

如果是在 WorkflowProject 内部建设或维护开发能力，直接使用本目录下的工作流。

如果不确定当前开发任务应该进入哪个细分工作流，先使用：

```text
04-workflows/developer/developer-kit-workflow.md
```

如果要把开发治理能力复制到其他项目中使用，优先使用导出包：

```text
14-exports/developer-kit/
```

在外部项目里可以直接对 AI 说：

```text
请使用 developer-kit 协助我处理这个开发任务：{写下你的任务}
```

developer-kit 会先判断任务类型，再选择对应工作流、模板和评分表。

## 推荐建设顺序

第一阶段：先管住项目不失控。

1. `project-bootstrap-workflow.md`：新项目启动检查与规范补齐。已完成第一版。
2. `project-understanding-workflow.md`：已有项目接手与上下文理解。已完成第一版。
3. `requirement-to-architecture-workflow.md`：产品需求到架构影响分析。已完成第一版。
4. `module-boundary-analysis-workflow.md`：模块边界与职责判断。已完成第一版。
5. `change-risk-assessment-workflow.md`：变更风险分级与确认策略。已完成第一版。
6. `impact-analysis-workflow.md`：影响范围分析。已完成第一版。
7. `minimal-change-governance-workflow.md`：最小必要变更治理。已完成第一版。

第二阶段：管住开发过程。

1. `implementation-workflow.md`：代码实现执行流程。已完成第一版。
2. `testing-verification-workflow.md`：测试与验收。已完成第一版。
3. `documentation-sync-workflow.md`：文档同步。已完成第一版。
4. `code-review-workflow.md`：代码评审。已完成第一版。

第三阶段：管住长期维护。

1. `architecture-decision-record-workflow.md`：架构决策记录。已完成第一版。
2. `dependency-and-tech-debt-workflow.md`：依赖与技术债治理。已完成第一版。
3. `environment-config-governance-workflow.md`：环境与配置治理。已完成第一版。
4. `release-and-rollback-workflow.md`：发布与回滚治理。已完成第一版。
5. `ai-collaboration-retrospective-workflow.md`：AI 协作复盘。已完成第一版。

第四阶段：增强真实开发协同。

1. `issue-diagnosis-workflow.md`：问题定位与根因分析。已完成第一版。
2. `data-api-contract-workflow.md`：数据/API/状态契约治理。已完成第一版。
3. `security-permission-workflow.md`：安全与权限治理。已完成第一版。
4. `workflow-orchestration-guide.md`：开发工作流协同编排指南。已完成第一版。
