# project-governance-kit

`project-governance-kit` 是面向真实代码项目的 AI 开发前置治理能力包。

它的职责是确保 AI 在开始写代码前，先确认：

```text
项目架构
模块边界
设计规范
任务列表
模块文档
验证规则
```

它不把产品、UI、开发、测试固化成每次都必须经过的角色链，而是根据当前缺口按需调用专业能力。

## 推荐关系

```text
project-governance-kit
-> 检查和补齐项目治理
-> team-orchestration-kit（需要跨角色时）
-> product-manager-kit / ui-designer-kit / developer-kit / tester-kit（按需）
```

## 适用原则

- 真实项目文档优先于通用能力包建议。
- 关键事实缺失时先询问，不要静默猜测。
- 中大型功能必须先形成整体规划和任务列表。
- 一次只执行一条任务，完成后立即验证。
- 代码变化影响文档时必须检查同步。
