# Cursor 使用说明

将自动读取配置复制到项目规则文件，例如：

```text
.cursor/rules/project-governance.mdc
```

然后输入：

```text
先检查当前项目治理基础，再处理这个需求：{需求}
```

Cursor 规则负责触发治理流程，项目 `docs/` 负责保存当前项目事实，角色能力包只在需要时调用。
