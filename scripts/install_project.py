#!/usr/bin/env python3
"""把 workflowproject-kit 安装到目标代码项目。"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
KITS_ROOT = PACKAGE_ROOT / "kits"


def write_text(path: Path, content: str, force: bool, dry_run: bool, changed: list[str], skipped: list[str]) -> None:
    if path.exists() and not force:
        skipped.append(f"已存在，未覆盖：{path}")
        return
    if dry_run:
        changed.append(f"将写入：{path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    changed.append(str(path))


def install(args: argparse.Namespace) -> int:
    project = Path(args.project).expanduser().resolve()
    selected = [p.name for p in sorted(KITS_ROOT.iterdir()) if p.is_dir() and not p.name.startswith(".")]
    missing = [name for name in selected if not (KITS_ROOT / name / "SKILL.md").is_file()]
    if missing:
        print("能力包缺少 SKILL.md：" + ", ".join(missing))
        return 2

    changed: list[str] = []
    skipped: list[str] = []
    destination_root = project / ".ai" / "kits"
    print(f"目标项目：{project}")
    if args.with_kits:
        print("安装能力：" + ", ".join(selected))
    else:
        print("能力包：跳过复制（已作为 skill 全局注册）；要随项目携带请加 --with-kits")
    if args.dry_run:
        print("模式：预览，不写入文件")
    elif args.create_project:
        project.mkdir(parents=True, exist_ok=True)

    for name in (selected if args.with_kits else []):
        source = KITS_ROOT / name
        destination = destination_root / name
        if destination.exists() and not args.force:
            skipped.append(f"已存在，未覆盖：{destination}")
            continue
        if args.dry_run:
            changed.append(f"将复制：{source} -> {destination}")
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination, dirs_exist_ok=True)
        changed.append(str(destination))

    agents = """# WorkflowProject AI 开发治理规则

本项目已接入 WorkflowProject 统一能力包。

**开跑门禁**：动手前必须先输出下面这段状态行，缺项或留空不得进入实现。

```text
项目归属：新项目 / 已有项目（{路径}）
模块归属：{扩展模块 / 新模块 / 待确认}
设计规范状态：已有 / 需建立最小规范 / 不适用
目标端与适配范围：{网页 / 移动端 / iPad / 桌面端 / 多端；横屏 / 分屏 / 折叠}
项目记忆：{已读文件 / 未找到}
执行模式：单 Agent + Skill / 父 Agent + 子 Agent / 单 Agent 降级模拟，不是真实子 Agent
当前阶段：{阶段}
```

涉及页面、组件、界面或用户可见交互的任务，「设计规范状态」不得填「不适用」。用户中途换需求、换模块或换技术方案时，重新输出该状态行。

开始任何开发任务前：

1. 先读取项目已有的 `AGENTS.md`、`README.md`、架构、模块、设计规范、任务列表、测试规则和项目记忆。
2. 区分已确认事实、AI 推断和需要用户确认的问题。
3. 如果任务涉及页面、组件或新功能，先询问项目归属、模块划分、项目规范、UI 设计规范、目标端、适配范围、组件状态和验收测试。
4. 新项目先问询确认技术方案；新模块先确认是否沿用当前项目技术栈。
5. 缺少关键材料时，先列出缺口并询问用户。
6. 先形成整体规划和按优先级排列的任务列表，再开始写代码。
7. 一次只执行一条任务，完成后立即验证。
8. 根据任务需要调用产品、UI、开发或测试能力，不强制所有角色参与。
9. 代码、测试、架构、模块、设计规范或任务状态发生变化时同步项目文档。
10. 对话中持续报告当前进度、当前调度角色、使用的工作流、验证结果和下一步。

11. 简单任务直接使用 Skill，不创建子 Agent；组合任务才创建真实子 Agent。运行环境不支持时，先停下说明并询问是否降级。

统一能力包位置：`.ai/kits/`
"""
    cursor_rule = """---
description: WorkflowProject 项目级 AI 开发治理规则
alwaysApply: true
---

开始任务前，先读取项目本地规则和已有文档，并执行：

任务类型识别 -> 技术方案问询 -> 功能/组件问询（如适用） -> 项目治理检查 -> 架构与模块检查 -> 设计规范检查 -> 整体规划 -> 任务列表 -> 逐条实现 -> 逐条验证 -> 文档与记忆同步

缺少关键项目事实、技术方案或功能/组件设计信息未确认时，先向用户确认，不要直接大范围改动代码。根据实际需要使用 `.ai/kits/` 中的具体能力包。

执行分流：简单单角色任务直接调用 Skill，不创建子 Agent；组合任务由父 Agent 创建真实子 Agent。运行环境没有真实子 Agent 工具时，必须明确说明，未经用户确认不得伪装成子 Agent 协作。
"""
    if not args.no_agents:
        write_text(project / "AGENTS.md", agents, args.force, args.dry_run, changed, skipped)
    if not args.no_rules:
        write_text(project / "AI-WORKFLOW-RULES.md", agents, args.force, args.dry_run, changed, skipped)
        write_text(project / ".cursor" / "rules" / "workflowproject-governance.mdc", cursor_rule, args.force, args.dry_run, changed, skipped)

    print("\n已创建或准备创建：")
    for item in changed:
        print(f"- {item}")
    if skipped:
        print("\n已跳过：")
        for item in skipped:
            print(f"- {item}")
    print("\n安装后的启动语句：")
    print("请先执行 WorkflowProject 项目治理检查，再处理我的任务：{写下任务}")
    return 0


parser = argparse.ArgumentParser(description="安装 WorkflowProject 统一能力包")
parser.add_argument("project", help="目标代码项目路径")
parser.add_argument("--dry-run", action="store_true", help="只预览，不写入")
parser.add_argument("--force", action="store_true", help="覆盖同名能力包和规则文件")
parser.add_argument("--no-agents", action="store_true", help="不生成 AGENTS.md")
parser.add_argument("--no-rules", action="store_true", help="不生成 AI-WORKFLOW-RULES.md 和 Cursor 规则")
parser.add_argument("--create-project", action="store_true", help="目标目录不存在时创建它")
parser.add_argument("--with-kits", action="store_true",
                    help="把能力包复制进项目 .ai/kits/（默认不复制：能力包已作为 skill 全局注册，"
                         "项目内不需要副本；仅当要把项目分享给未安装这些 skill 的人才需要）")
raise SystemExit(install(parser.parse_args()))
