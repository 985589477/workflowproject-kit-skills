# developer-kit

导出时间：2026-10-14

`developer-kit` 是从 WorkflowProject 中拆分出来的开发治理能力包。

它不是替代 Codex 或 Cursor 写代码的工具，而是给 AI 开发协作增加一套稳定的项目治理方式：先理解项目，再判断风险，再选择工作流，最后完成实现、验证、文档和复盘闭环。

developer-kit 的总入口不是简单分流器。它会把开发任务放进完整生命周期里判断：

```text
需求理解 -> 开发确认 -> 项目理解 -> 功能规划 -> 契约/安全检查 -> 实现 -> 验证 -> 文档 -> 评审 -> 发布或复盘
```

小任务可以轻量执行，但必须说明跳过哪些阶段以及为什么。

## 适合解决的问题

- 新项目启动时，不知道需要补哪些工程规范。
- 已有项目接手时，不知道 AI 应该先读什么、怎么理解结构。
- 产品需求进入开发时，不知道会影响哪些模块。
- 模块边界不清晰，AI 容易把职责改乱。
- 报错、白屏、测试失败或性能异常时，需要先定位根因再修复。
- 接口字段、数据结构、状态归属或错误处理不清晰。
- 登录、权限、敏感数据、密钥、上传下载、支付等高风险能力需要先治理。
- 多个开发工作流之间需要插入、回退或暂停确认。
- 开发过程中缺少风险判断、测试验证、文档同步和评审闭环。
- 多轮 AI 协作后，项目规则和经验没有沉淀。
- AI 容易过度设计、过早抽象、重复造轮子或为小需求新增依赖。

## 包含内容

```text
developer-kit/
├── START-HERE.md
├── README.md
├── usage-guide.md
├── manifest.md
├── SKILL.md
├── INSTALL.md
├── workflows/
│   ├── developer/
│   └── common/
├── roles/
├── templates/
│   ├── developer/
│   └── common/
├── scorecards/
├── knowledge/
├── integrations/
└── examples/
```

## 最快使用

```text
请使用 developer-kit 协助我处理这个开发任务：{写下你的任务}
```

## 首次接入

如果是第一次把 developer-kit 放入一个新项目，先看：

```text
INSTALL.md
```

如果想看一轮真实启动示例，先看：

```text
examples/quick-start-example.md
```

如果你希望 AI 自动判断是否调用本能力包，请参考：

```text
START-HERE.md
```

## 推荐入口

优先阅读：

```text
START-HERE.md
usage-guide.md
workflows/developer/developer-kit-workflow.md
knowledge/developer-governance-capability-system.md
```

## 核心原则

- 先理解项目，再改动项目。
- 先判断风险，再决定执行深度。
- 实现前先做整体功能规划。
- 实现前先做最小必要变更判断：能不写就不写，能复用就复用，能用平台或标准库就不新增依赖。
- 不明确时主动询问用户。
- 小任务轻量执行，大任务完整治理。
- 代码实现必须配套验证。
- 结构、边界、决策和经验要能沉淀。
- 长期迭代项目要维护项目记忆摘要，避免每次读取完整历史。
- “少写代码”不能成为省略安全、校验、错误处理、可访问性和测试的理由。

## Ponytail 融合说明

本包吸收了 Ponytail 项目的核心思想：让 AI 在写代码前先判断是否真的需要写代码，并优先复用已有能力。

本包没有把 Ponytail 作为外部依赖引入，而是将其原则转化为：

```text
roles/minimal-change-guardian.md
workflows/developer/minimal-change-governance-workflow.md
templates/developer/minimal-change-governance-template.md
scorecards/minimal-change-governance-scorecard.md
knowledge/ponytail-minimal-change-principles.md
```

## 工具集成

Codex 使用说明：

```text
integrations/codex-usage.md
```

Cursor 使用说明：

```text
integrations/cursor-usage.md
```
