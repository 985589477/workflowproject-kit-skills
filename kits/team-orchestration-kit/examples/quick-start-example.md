# 快速启动示例

## 用户输入

```text
请使用 team-orchestration-kit 调度产品、UI、开发和测试处理我的任务：

我想做一个账号登录注册功能，需要支持手机号验证码登录、密码登录、忘记密码和登录后的个人中心入口。
```

## AI 应先输出

```text
任务判断：跨角色完整功能需求
调用能力包：team-orchestration-kit
参与角色：产品经理、UI 设计师、开发工程师、测试工程师
当前接管角色：产品经理
使用工作流：workflows/mixed/team-orchestration-workflow.md
使用模板：templates/mixed/team-orchestration-template.md
检查标准：scorecards/team-orchestration-scorecard.md
保存位置：对话直接输出
```

## 推荐推进

```text
产品经理：先做需求分析、PRD 和验收标准
UI 设计师：在产品范围确认后做页面结构、状态、组件和适配交接
开发工程师：在产品和 UI 交接通过后做项目理解、方案、任务拆解和实现
测试工程师：根据 PRD、设计交接和开发变更做测试策略、用例、回归和发布验收
```

## 如果交接不通过

```text
协作阻塞：开发无法判断验证码登录的接口状态和错误处理
发现角色：开发工程师
来源角色：产品经理
问题类型：验收标准不清 / 数据状态不清
影响：无法稳定实现登录失败、验证码过期、重复发送等状态
建议补充：验证码有效期、发送间隔、错误次数限制、账号不存在处理
建议回到：product-manager-kit + acceptance-criteria-workflow
```
