# Cursor 使用说明

## 推荐用法

把以下目录放到项目根目录或统一 AI 能力目录：

```text
product-manager-kit/
ui-designer-kit/
developer-kit/
tester-kit/
team-orchestration-kit/
```

然后在 Cursor 对话中输入：

```text
请使用 team-orchestration-kit 判断这个任务需要哪些角色参与，并按阶段推进：{任务}
```

## 自动触发

可以把 `START-HERE.md` 中的“外部自动读取配置”复制到 Cursor 项目规则中，例如：

```text
.cursor/rules/team-orchestration.mdc
```

## 使用建议

- 需求不清时，让总调度先进入产品经理阶段。
- 页面、组件、适配不清时，让总调度切到 UI 设计师阶段。
- 实现前，让总调度检查产品和 UI 交接是否通过。
- 代码实现时，让开发角色接管。
- 交付前，让测试角色接管并输出发布建议。
