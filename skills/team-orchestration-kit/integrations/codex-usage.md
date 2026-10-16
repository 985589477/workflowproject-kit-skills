# Codex 使用说明

## 推荐用法

在 Codex 中，把 `team-orchestration-kit/` 和四个角色包放在同一个项目中，然后说：

```text
请使用 team-orchestration-kit 调度产品、UI、开发和测试处理我的任务：{任务}
```

Codex 应先读取：

```text
team-orchestration-kit/START-HERE.md
team-orchestration-kit/README.md
team-orchestration-kit/usage-guide.md
team-orchestration-kit/workflows/mixed/team-orchestration-workflow.md
```

## 适合 Codex 的任务

- 判断一个需求应该由哪些角色参与。
- 规划从产品到 UI、开发、测试的推进顺序。
- 检查交接文档是否足够下游使用。
- 在开发前判断产品和 UI 是否已经准备好。
- 在交付后做产品、UI、测试三方验收。

## 注意

如果任务进入真实代码实现，应由 `developer-kit` 接管，并遵守目标项目的代码规范、测试规范和 AI 协作规则。
