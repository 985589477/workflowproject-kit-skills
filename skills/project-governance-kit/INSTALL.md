# 接入说明

## 一条命令安装

在 WorkflowProject 根目录执行：

```bash
python3 tools/install_project_kits.py /你的代码项目路径
```

默认安装项目治理、团队总调度、产品、UI、开发和测试六个能力包，并生成：

```text
目标项目/.ai/kits/
目标项目/AGENTS.md
目标项目/AI-WORKFLOW-RULES.md
目标项目/.cursor/rules/project-governance.workflowproject.mdc
```

建议先预览：

```bash
python3 tools/install_project_kits.py /你的代码项目路径 --dry-run
```

只安装开发相关能力：

```bash
python3 tools/install_project_kits.py /你的代码项目路径 --kits governance,team,developer,tester
```

已有同名文件默认不会覆盖。如已确认需要覆盖，再使用 `--force`。

## 基本接入

将 `project-governance-kit/` 放入真实项目根目录或统一的 AI 能力目录。

## 自动读取

将 `START-HERE.md` 中的“外部自动读取配置”复制到项目根目录的 `AI-WORKFLOW-RULES.md`、Codex 可读取的项目规则文件，或 Cursor 的项目规则中。

自动读取配置只是入口规则，不代表 AI 已经掌握项目架构。AI 仍然必须读取当前项目的架构、模块和设计文档。

## 与其他能力包一起使用

如果同时接入 `team-orchestration-kit` 和角色能力包，默认顺序是：

```text
project-governance-kit
-> team-orchestration-kit
-> 具体角色包
```

如果只是一个纯开发任务，治理检查完成后可以直接转交 `developer-kit`。
