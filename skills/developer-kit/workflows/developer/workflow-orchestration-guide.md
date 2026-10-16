# 开发工作流协同编排指南

## 目的

本指南用于增强 developer-kit 内部工作流之间的协同能力。

它解决的问题是：AI 不应该机械地“命中一个工作流就结束”，而应该根据任务状态在多个工作流之间前进、后退、插入检查或暂停确认。

## 使用原则

### 1. 总入口负责调度，细分工作流负责产出

`developer-kit-workflow.md` 负责判断当前阶段和下一阶段。

细分工作流负责完成具体产出。

### 2. 工作流可以前进，也可以回退

如果实现过程中发现边界不清，应回到模块边界分析。

如果测试失败且根因不清，应回到问题定位。

如果发现接口字段不清，应插入数据/API/状态契约。

如果发现权限或敏感数据，应插入安全与权限治理。

### 3. 不确定时先停

以下情况必须暂停并询问用户：

- 需求目标或验收标准不清。
- 会影响架构、数据、权限、安全、支付、生产配置。
- 有多个合理方案且没有明显最优解。
- 需要删除、迁移、批量修改或执行不可逆操作。
- 工作流输出之间互相冲突。

## 常见编排链路

### 新需求进入开发

```text
developer-kit-workflow
-> requirement-to-architecture-workflow
-> project-understanding-workflow
-> module-boundary-analysis-workflow
-> data-api-contract-workflow（如涉及数据/API/状态）
-> security-permission-workflow（如涉及权限/安全）
-> change-risk-assessment-workflow
-> impact-analysis-workflow
-> implementation-workflow
-> testing-verification-workflow
-> documentation-sync-workflow
-> code-review-workflow
-> release-and-rollback-workflow（如涉及发布）
```

### 已有问题修复

```text
developer-kit-workflow
-> project-understanding-workflow（如上下文不足）
-> issue-diagnosis-workflow
-> data-api-contract-workflow（如根因涉及数据/API/状态）
-> security-permission-workflow（如根因涉及权限/安全）
-> change-risk-assessment-workflow
-> implementation-workflow
-> testing-verification-workflow
-> code-review-workflow
```

### 低风险小改动

```text
developer-kit-workflow
-> 快速影响判断
-> implementation-workflow
-> 最小验证
```

可以跳过完整链路，但必须说明为什么可以跳过。

### 高风险变更

```text
developer-kit-workflow
-> requirement-to-architecture-workflow
-> module-boundary-analysis-workflow
-> data-api-contract-workflow
-> security-permission-workflow
-> change-risk-assessment-workflow
-> impact-analysis-workflow
-> 等待用户确认
-> implementation-workflow
-> testing-verification-workflow
-> release-and-rollback-workflow
-> ai-collaboration-retrospective-workflow
```

## 插入规则

| 触发信号 | 必须插入 |
| --- | --- |
| 报错、白屏、测试失败、性能异常 | `issue-diagnosis-workflow.md` |
| 接口字段、数据模型、状态归属不清 | `data-api-contract-workflow.md` |
| 登录、权限、用户数据、密钥、支付 | `security-permission-workflow.md` |
| 模块职责不清或新增模块争议 | `module-boundary-analysis-workflow.md` |
| 影响范围不清 | `impact-analysis-workflow.md` |
| 高风险或不可逆操作 | `change-risk-assessment-workflow.md` |
| 发布、上线、回滚 | `release-and-rollback-workflow.md` |
| 协作过程失控或规则缺失 | `ai-collaboration-retrospective-workflow.md` |

## 回退规则

| 当前阶段 | 发现问题 | 回退到 |
| --- | --- | --- |
| 实现中 | 根因不清 | `issue-diagnosis-workflow.md` |
| 实现中 | 模块放置不清 | `module-boundary-analysis-workflow.md` |
| 实现中 | 接口或状态不清 | `data-api-contract-workflow.md` |
| 实现中 | 权限或敏感数据不清 | `security-permission-workflow.md` |
| 测试中 | 失败原因不清 | `issue-diagnosis-workflow.md` |
| 发布前 | 缺少回滚策略 | `release-and-rollback-workflow.md` |

## 协同状态格式

```text
当前阶段：
刚完成的工作流：
发现的新问题：
是否需要插入工作流：
插入原因：
是否需要回退：
回退原因：
下一步工作流：
是否需要用户确认：
```

## 质量要求

- 必须说明为什么选择当前工作流。
- 必须说明为什么跳过某些工作流。
- 必须在阶段结束后判断下一步。
- 必须允许回退和插入检查。
- 高风险动作必须等待确认。
