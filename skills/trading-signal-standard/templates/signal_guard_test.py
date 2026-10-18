"""交易信号落地守卫（模板）—— 复制到目标项目的 tests/ 后改顶部 3 个常量、填两个白名单即可。

四条检查（对应 skills/trading-signal-standard 的规则）：

  1. 口径表每一行都完整（判据/函数/定义式/量纲/边界/参数来源 六列都不空）
  2. 双向一致：登记的 `StrategyTools.xxx` 真实存在；代码里的 is_/has_ 判据要么登记、要么进白名单
  3. 推算类函数（estimate_/next_/forecast_/predict_）出现在信号路径里必须在口径表登记用途
  4. 已登记的判据必须在 tests/ 里被引用过（说明有 golden 或边界用例守着）

设计取舍（重要）：
  · **存量用白名单承接**，新判据必须合规 —— 一上来就红的门禁等于没有门禁。
  · 白名单只减不增：删掉一条说明那条存量已经补齐了口径。
  · 只做能机械判定的部分；口径写得对不对仍然要人评审。
  · 口径表里可以有多张表：本守卫只读以 `| 判据 |` 开头的那一张。
"""

from __future__ import annotations

import pathlib
import re

import pytest

# ── ① 按目标项目改这三个 ────────────────────────────────────────────────
PROJECT = pathlib.Path(__file__).resolve().parents[1]
SIGNALS_FILE = PROJECT / "src" / "strategies" / "tools.py"      # 判据函数所在的文件
LEDGER = PROJECT / "docs" / "TRADING_METRICS.md"               # 口径登记表
SIGNAL_DIRS = [PROJECT / "src" / "strategies", PROJECT / "src" / "backtest"]  # 信号路径
# ─────────────────────────────────────────────────────────────────────

DANGEROUS = re.compile(r"\b(estimate_|next_|forecast_|predict_)[a-z0-9_]*\s*\(")
LEDGER_HEADER = ("判据", "函数", "定义式", "量纲", "边界", "参数来源")

# ── ② 存量白名单（先空着跑一次，把报出来的名字填进来）──────────────────
KNOWN_UNTRACED: set[str] = set()        # 待补口径的判据函数
KNOWN_DANGEROUS: set[str] = set()       # 待登记用途的推算函数


def _all_functions() -> set[str]:
    """判据文件里定义的全部函数名（用于「登记的函数是否真实存在」）。"""
    if not SIGNALS_FILE.is_file():
        pytest.skip(f"找不到判据文件：{SIGNALS_FILE}（改了顶部常量？）")
    src = SIGNALS_FILE.read_text(encoding="utf-8", errors="replace")
    return set(re.findall(r"^\s{4}def ([a-z_][a-z0-9_]*)\(", src, re.M))


def _signal_functions() -> set[str]:
    """对外判据函数 = is_/has_ 开头（用于「代码里的判据必须登记」）。"""
    return {f for f in _all_functions() if f.startswith(("is_", "has_"))}


def _ledger_text() -> str:
    return LEDGER.read_text(encoding="utf-8") if LEDGER.is_file() else ""


def _ledger_rows() -> list[list[str]]:
    """只返回「判据表」的行：从 `| 判据 |` 表头开始，到表格结束为止。"""
    if not LEDGER.is_file():
        pytest.skip(f"还没有口径登记表：{LEDGER}（见 templates/metric-row.md）")
    rows: list[list[str]] = []
    in_table = False
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table:            # 判据表结束
                break
            continue
        if set(stripped) <= set("|- :"):     # 分隔行
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if cells[0] == LEDGER_HEADER[0]:     # 表头
            in_table = True
            continue
        if in_table:
            rows.append(cells)
    return rows


def _registered_names() -> set[str]:
    """判据表「函数」列里登记的函数名（不把文档别处的同名提及当登记）。"""
    names: set[str] = set()
    for cells in _ledger_rows():
        if len(cells) >= 2:
            for token in re.findall(r"[A-Za-z_][\w.]*", cells[1]):
                names.add(token.split(".")[-1])
    return names


def test_ledger_rows_are_complete() -> None:
    """规则 2：六列都不许空 —— 空一列就等于口径没有定义。"""
    bad = []
    for cells in _ledger_rows():
        if len(cells) != len(LEDGER_HEADER):
            bad.append(f"列数不是 {len(LEDGER_HEADER)}：{cells}")
            continue
        for name, value in zip(LEDGER_HEADER, cells):
            if not value:
                bad.append(f"{cells[0]} 的「{name}」为空")
    assert not bad, "口径表有未填完的行：\n  " + "\n  ".join(bad)


def test_ledger_and_code_agree() -> None:
    """规则 1：登记的函数必须真实存在；代码里的判据必须登记或进白名单。"""
    every = _all_functions()
    text = _ledger_text()

    # 只核对 `StrategyTools.xxx` 这种写法，避免把文件名当函数名。
    missing_in_code = sorted(
        fn.split(".")[-1]
        for fn in re.findall(r"`(StrategyTools\.[a-z_]\w*)`", text)
        if fn.split(".")[-1] not in every
    )
    untraced = sorted(_signal_functions() - _registered_names() - KNOWN_UNTRACED)

    assert not missing_in_code, f"口径表登记了代码里不存在的函数：{missing_in_code}"
    assert not untraced, (
        "这些判据函数还没登记口径（登记，或临时加进 KNOWN_UNTRACED）：\n  " + "\n  ".join(untraced)
    )


def test_forecast_helpers_are_registered() -> None:
    """规则 3：推算类函数出现在信号路径里必须登记用途（不一定违法，但必须说明假设）。"""
    text = _ledger_text()
    hits = []
    for base in SIGNAL_DIRS:
        if not base.is_dir():
            continue
        for path in base.rglob("*.py"):
            for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if line.lstrip().startswith(("#", "def ")):     # 注释与定义不算调用
                    continue
                for m in DANGEROUS.finditer(line):
                    name = m.group(0).rstrip("( \t")
                    if name in KNOWN_DANGEROUS or name in text:
                        continue
                    hits.append(f"{path.relative_to(PROJECT)}:{lineno}: {line.strip()}")
    assert not hits, (
        "信号路径里出现未登记的推算类调用：\n  " + "\n  ".join(hits)
        + "\n在口径表里登记它的假设（为什么不是未来函数）。"
    )


def test_registered_signals_have_tests() -> None:
    """规则 4：**登记过**的判据必须在 tests/ 里被引用过（存量未登记的不追溯）。"""
    tests_dir = PROJECT / "tests"
    if not tests_dir.is_dir():
        pytest.skip("没有 tests/ 目录")
    blob = "\n".join(
        p.read_text(encoding="utf-8", errors="replace")
        for p in tests_dir.rglob("*.py")
        if p.name != pathlib.Path(__file__).name
    )
    registered = sorted(_signal_functions() & _registered_names())
    missing = [fn for fn in registered if fn not in blob]
    assert not missing, f"这些已登记的判据没有任何测试引用：{missing}"
