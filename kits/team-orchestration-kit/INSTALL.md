# 安装说明

导出时间：2026-10-14

## 推荐安装方式

把以下能力包复制到目标项目根目录或统一 AI 能力目录：

```text
product-manager-kit/
ui-designer-kit/
developer-kit/
tester-kit/
team-orchestration-kit/
```

推荐同级放置，因为 team-orchestration-kit 会调度其他四个角色包。

## 最小安装方式

如果只复制：

```text
team-orchestration-kit/
```

也可以使用总调度能力，但只能做角色判断、交接检查和流程建议，不能直接读取其他角色包的细分工作流。

## 首次验证

复制后，对 AI 说：

```text
请使用 team-orchestration-kit 判断这个需求应该由哪些角色参与：我想做一个登录注册功能，需要从需求到开发和测试完整推进。
```

AI 应该先判断参与角色，再说明当前接管角色和后续链路。

## 自动触发

如果希望 AI 自动判断是否使用本包，把 `START-HERE.md` 中“外部自动读取配置”复制到目标项目的：

```text
AI-WORKFLOW-RULES.md
```

或你的 AI 工具默认规则文件中。
