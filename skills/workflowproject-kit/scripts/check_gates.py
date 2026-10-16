#!/usr/bin/env python3
"""check_gates.py —— 校验一个项目是否真的具备 workflowproject-kit 要求的治理门禁。

这是把「规范从提示词变成红灯」的那一环。规则写在文档里没人执行；
跑这条命令会**非 0 退出**，才能进 pre-commit / CI 真正拦住。

用法：
    python3 check_gates.py [项目目录]        # 默认当前目录
    python3 check_gates.py --audit [目录]    # 只列出哪些门禁有证据、哪些没有（找"死规则"）
    python3 check_gates.py --strict [目录]   # 把警告也算失败

退出码：0 = 硬门禁全过；1 = 有硬门禁未过；2 = 用法错误。

设计原则（对应 kit 门禁表）：
  门禁 01 基线固化          → AGENTS.md 有「基线」段，且含数字测试基线 + 回退命令
  门禁 02 可运行守卫        → 仓库里存在守卫测试文件
  门禁 03 以代码为准        → AGENTS.md 记录了文档一致性核查结论
  门禁 04 人工判断检查点    → AGENTS.md 或计划文档里有该段
  门禁 05 子 Agent 契约     → AGENTS.md 引用了子 Agent 返回契约模板
  门禁 06 环境能力探测      → AGENTS.md 有实测验证命令
  门禁 08 数据资产保护      → 仓库含 db/大二进制时，AGENTS.md 必须有备份段
  门禁 07 工作量单位        → 计划文档用会话数而非天数（软检查）

只依赖标准库。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- 检测工具

AGENTS_CANDIDATES = ("AGENTS.md", "agents.md", ".ai/AGENTS.md", "docs/AGENTS.md")

# 守卫文件的命名模式 —— 命中任一即认为存在守卫
GUARD_PATTERNS = (
    r"test_.*guard.*\.py$",
    r".*guards?.*\.py$",
    r"test_.*architecture.*\.py$",
    r"test_.*contract.*\.py$",
    r"test_.*snapshot.*\.py$",
    r".*\.snapshot\.(txt|json)$",
    r".*golden\.(json|txt|csv)$",
    r".*\.golden\.",
)

# 验证命令里可识别的测试运行器 —— 用来判断"验证命令是否实测可用"
RUNNER_HINTS = (
    "pytest", "unittest", "npm test", "npm run test", "pnpm test", "yarn test",
    "go test", "cargo test", "vitest", "jest", "tox", "nox",
)

DATA_SUFFIXES = (".db", ".sqlite", ".sqlite3", ".duckdb", ".parquet", ".mdb")
BIG_FILE_BYTES = 20 * 1024 * 1024  # 20MB

PLAN_CANDIDATES = ("PLAN.md", "docs/PLAN.md", "docs/REFACTORING_PLAN.md", "ROADMAP.md", "docs/ROADMAP.md")


class Result:
    def __init__(self, gate: str, title: str, hard: bool = True):
        self.gate, self.title, self.hard = gate, title, hard
        self.ok = False
        self.detail = ""
        self.hint = ""

    def passed(self, detail: str) -> "Result":
        self.ok, self.detail = True, detail
        return self

    def failed(self, detail: str, hint: str = "") -> "Result":
        self.ok, self.detail, self.hint = False, detail, hint
        return self


def find_agents(root: Path) -> Path | None:
    for rel in AGENTS_CANDIDATES:
        p = root / rel
        if p.is_file():
            return p
    return None


def find_plan(root: Path) -> Path | None:
    for rel in PLAN_CANDIDATES:
        p = root / rel
        if p.is_file():
            return p
    return None


def scan_guards(root: Path) -> list[str]:
    hits: list[str] = []
    for pattern in GUARD_PATTERNS:
        rx = re.compile(pattern)
        for p in root.rglob("*"):
            if p.is_file() and not any(part in {".git", "node_modules", "__pycache__", "dist"} for part in p.parts):
                if rx.search(p.as_posix()):
                    rel = p.relative_to(root).as_posix()
                    if rel not in hits:
                        hits.append(rel)
    return sorted(hits)[:8]


def scan_data_assets(root: Path) -> list[tuple[str, int]]:
    out: list[tuple[str, int]] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in {".git", "node_modules", "__pycache__"} for part in p.parts):
            continue
        try:
            size = p.stat().st_size
        except OSError:
            continue
        if p.suffix.lower() in DATA_SUFFIXES or size >= BIG_FILE_BYTES:
            out.append((p.relative_to(root).as_posix(), size))
    return sorted(out, key=lambda t: -t[1])[:6]


def has_section(text: str, *keywords: str) -> bool:
    """判断文本里是否有包含这些关键词的小节/表格行。"""
    lowered = text.lower()
    return all(k.lower() in lowered for k in keywords)


def has_measured_command(text: str) -> bool:
    """找被反引号或代码块包起来的、含测试运行器的命令。"""
    lowered = text.lower()
    for runner in RUNNER_HINTS:
        for line in lowered.splitlines():
            if runner in line and ("`" in line or line.strip().startswith(("$", "python", "npm", "pnpm", "yarn", "go ", "cargo"))):
                return True
    return False


def has_numeric_baseline(text: str) -> bool:
    return bool(re.search(r"\b\d+\s*(passed|个测试)", text, re.I))


# ---------------------------------------------------------------- 各门禁检查


def gate_01_baseline(root: Path, agents: str | None) -> Result:
    r = Result("01", "基线固化")
    if agents is None:
        return r.failed("找不到 AGENTS.md，无法确认基线", "用 templates/project-agents.md 建一个")
    if not has_section(agents, "基线"):
        return r.failed("AGENTS.md 里没有「基线」段", "见 gates/01-baseline-freeze.md")
    missing = []
    if not has_numeric_baseline(agents):
        missing.append("测试基线数字（形如 `188 passed`）")
    if not re.search(r"回退|reset --hard|恢复备份", agents):
        missing.append("回退命令")
    if missing:
        return r.failed("「基线」段缺：" + "、".join(missing), "见 gates/01-baseline-freeze.md")
    return r.passed("有基线段，含数字基线与回退命令")


def gate_02_guards(root: Path, agents: str | None) -> Result:
    r = Result("02", "可运行守卫")
    hits = scan_guards(root)
    if not hits:
        return r.failed(
            "没找到守卫文件（守卫测试 / 契约快照 / golden 文件）",
            "见 gates/02-runnable-guards.md；写完后注入一个故意违规确认它变红",
        )
    return r.passed(f"找到 {len(hits)} 个：{', '.join(hits[:3])}{' …' if len(hits) > 3 else ''}")


def gate_03_code_over_docs(root: Path, agents: str | None) -> Result:
    r = Result("03", "以代码为准", hard=False)
    if agents is None:
        return r.failed("找不到 AGENTS.md")
    if has_section(agents, "文档") and re.search(r"一致|矛盾|以代码为准|过期", agents):
        return r.passed("AGENTS.md 记录了文档一致性结论")
    return r.failed("没有文档一致性核查的记录", "见 gates/03-code-over-docs.md")


def gate_04_human_checkpoints(root: Path, agents: str | None, plan: Path | None) -> Result:
    r = Result("04", "人工判断检查点")
    blob = (agents or "")
    if plan is not None:
        blob += "\n" + plan.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"人工判断|必须用户|需用户|用户亲自", blob):
        return r.passed("计划/AGENTS.md 里有该段")
    return r.failed("没有列出「必须用户亲自判断」的检查点", "见 gates/04-human-judgment-checkpoints.md")


def gate_05_subagent(root: Path, agents: str | None) -> Result:
    r = Result("05", "子 Agent 契约", hard=False)
    if agents is None:
        return r.failed("找不到 AGENTS.md")
    if re.search(r"子\s*Agent|subagent", agents, re.I) and re.search(r"复核|未验证|证据", agents):
        return r.passed("AGENTS.md 含子 Agent 契约与复核要求")
    return r.failed("未记录子 Agent 返回契约 / 复核义务", "见 gates/05-subagent-contract.md")


def gate_06_env(root: Path, agents: str | None) -> Result:
    r = Result("06", "环境能力探测")
    if agents is None:
        return r.failed("找不到 AGENTS.md", "用 templates/project-agents.md 建一个")
    if not re.search(r"环境|验证命令", agents):
        return r.failed("AGENTS.md 没有「环境与验证命令」段", "见 gates/06-environment-probe.md")
    if not has_measured_command(agents):
        return r.failed("没有找到实测过的验证命令（带反引号的测试运行器）", "见 gates/06-environment-probe.md")
    return r.passed("有验证命令段且含可识别的测试运行器")


def gate_08_data(root: Path, agents: str | None) -> Result:
    r = Result("08", "数据资产保护")
    assets = scan_data_assets(root)
    if not assets:
        return r.passed("未发现数据库/大文件（本门禁不适用）")
    if agents is None:
        return r.failed(
            f"发现 {len(assets)} 个数据资产但无 AGENTS.md 记录备份",
            "见 gates/08-data-asset-protection.md",
        )
    if not re.search(r"备份", agents):
        return r.failed(
            f"发现数据资产（{assets[0][0]} 等 {len(assets)} 个）但 AGENTS.md 未记录备份路径",
            "见 gates/08-data-asset-protection.md",
        )
    return r.passed(f"{len(assets)} 个数据资产已在 AGENTS.md 记录")


def gate_07_effort(root: Path, plan: Path | None) -> Result:
    r = Result("07", "工作量单位", hard=False)
    if plan is None:
        return r.failed("没找到计划文档")
    text = plan.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"会话数", text):
        return r.passed("计划用会话数作为工作量单位")
    if re.search(r"\d+\s*(天|周|个月)", text):
        return r.failed("计划用日历时间（天/周/月）估算", "见 gates/07-effort-unit.md；改用会话数 + 检查点数")
    return r.failed("计划里没有工作量单位", "见 gates/07-effort-unit.md")


# ---------------------------------------------------------------- 主流程


def run(root: Path, audit: bool, strict: bool) -> int:
    agents_path = find_agents(root)
    plan_path = find_plan(root)
    agents = agents_path.read_text(encoding="utf-8", errors="ignore") if agents_path else None

    results = [
        gate_01_baseline(root, agents),
        gate_02_guards(root, agents),
        gate_06_env(root, agents),
        gate_08_data(root, agents),
        gate_04_human_checkpoints(root, agents, plan_path),
        gate_05_subagent(root, agents),
        gate_03_code_over_docs(root, agents),
        gate_07_effort(root, plan_path),
    ]

    print(f"project: {root}")
    print(f"AGENTS.md: {agents_path.relative_to(root).as_posix() if agents_path else '❌ 未找到'}")
    print(f"计划文档: {plan_path.relative_to(root).as_posix() if plan_path else '—'}")
    print()

    if audit:
        print("门禁覆盖审计（没证据的就是死规则 → 删掉或改触发条件）：")
        for r in results:
            mark = "✅" if r.ok else ("⚠️ " if not r.hard else "❌")
            print(f"  {mark} {r.gate} {r.title:16} {'' if r.ok else '— ' + r.detail}")
        print(f"\n有证据 {sum(1 for r in results if r.ok)}/{len(results)}")
        return 0

    print("门禁检查：")
    failed_hard = 0
    failed_soft = 0
    for r in results:
        if r.ok:
            print(f"  ✅ {r.gate} {r.title:16} {r.detail}")
        elif r.hard:
            failed_hard += 1
            print(f"  ❌ {r.gate} {r.title:16} {r.detail}")
            if r.hint:
                print(f"       → {r.hint}")
        else:
            failed_soft += 1
            print(f"  ⚠️  {r.gate} {r.title:16} {r.detail}")
            if r.hint:
                print(f"       → {r.hint}")

    print()
    if failed_hard:
        print(f"结果：{failed_hard} 个硬门禁未过，{failed_soft} 个软门禁未过 → 不许开始改造")
        return 1
    if failed_soft and strict:
        print(f"结果：硬门禁全过，但 --strict 下 {failed_soft} 个软门禁未过 → 失败")
        return 1
    print(f"结果：硬门禁全过（{failed_soft} 个软门禁待补）")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="校验项目是否具备 workflowproject-kit 要求的治理门禁")
    parser.add_argument("path", nargs="?", default=".", help="项目目录（默认当前目录）")
    parser.add_argument("--audit", action="store_true", help="只列出各门禁是否有证据")
    parser.add_argument("--strict", action="store_true", help="软门禁未过也算失败")
    args = parser.parse_args(argv)

    root = Path(args.path).expanduser().resolve()
    if not root.is_dir():
        print(f"错误：{root} 不是目录", file=sys.stderr)
        return 2
    return run(root, args.audit, args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
