# team-orchestration-kit

导出时间：2026-10-15

`team-orchestration-kit` 是从 WorkflowProject 中拆分出来的跨角色团队总调度能力包。

它不替代产品经理、UI 设计师、开发工程师或测试工程师的单独能力包，而是负责把这些角色组织成一个协作团队：判断谁先接管、谁需要参与、什么时候交接、交接是否通过、开发交付是否能被产品/UI/测试验收。

## 适合解决的问题

- 用户提出一个完整需求，但不知道应该先做产品、设计、开发还是测试。
- 一个需求需要从想法推进到 PRD、设计、开发、测试和验收。
- 需要检查产品输出是否能被 UI、开发和测试看懂。
- 需要检查 UI 输出是否能被开发和测试看懂。
- 需要检查开发交付是否能通过产品、UI 和测试验收。
- 角色之间出现沟通不畅，需要记录 badcase 并回到对应能力项目优化。

## 推荐目录结构

建议把本包和四个角色包放在同级：

```text
product-manager-kit/
ui-designer-kit/
developer-kit/
tester-kit/
team-orchestration-kit/
```

如果只复制 `team-orchestration-kit/`，它仍然可以做调度判断，但无法直接读取各角色包中的细分工作流和模板。

## 包含内容

```text
team-orchestration-kit/
├── START-HERE.md
├── README.md
├── usage-guide.md
├── INSTALL.md
├── SKILL.md
├── manifest.md
├── workflows/
│   ├── mixed/
│   └── common/
├── templates/
│   ├── mixed/
│   └── common/
├── scorecards/
├── knowledge/
├── examples/
└── integrations/
```

## 最快使用

```text
请使用 team-orchestration-kit 调度产品、UI、开发和测试处理我的任务：{写下你的任务}
```

## 推荐入口

优先阅读：

```text
START-HERE.md
usage-guide.md
workflows/mixed/team-orchestration-workflow.md
templates/mixed/team-orchestration-template.md
scorecards/team-orchestration-scorecard.md
```

## 核心原则

- 总入口负责团队调度，不负责替代所有角色细节。
- 总入口先判断任务复杂度；简单任务直接调用一个 Skill，组合任务才创建父 Agent 和子 Agent。
- 简单任务禁止为了形式创建子 Agent；组合任务不得把单 Agent 顺序执行描述为真实子 Agent 协作。
- 组合任务运行环境没有真实子 Agent 能力时，必须先报告限制并获得用户确认后才能降级执行。
- 只要项目中存在 `team-orchestration-kit`，产品、UI、开发、测试相关任务默认先由总调度入口接管。
- 总调度先判断角色和阶段，再决定是否转交单一角色包。
- 上游产物必须能被下游角色理解。
- 交接不通过时，先反馈问题，不要硬推进。
- 开发交付后需要产品、UI、测试三方验收。
- 出现反复沟通问题时，应记录 badcase 并回流到对应角色能力项目优化。
- 外部项目保存文档时，优先使用已有文档目录，不默认创建 WorkflowProject 内部目录。

## 执行模式

每次执行必须报告：

```text
执行模式：单 Agent + Skill / 父 Agent + 子 Agent / 单 Agent 降级模拟，不是真实子 Agent
```

任务简报和结果回报模板位于：

```text
templates/common/agent-task-brief-template.md
templates/common/agent-result-report-template.md
```
