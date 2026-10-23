---
name: trading-signal-standard
description: "把交易判据（洗盘区/一字板/放量倍数/破位/二高点等）落成可验证代码的规范：判据必须函数化、口径三件套（定义/量纲/边界）必须登记、禁止未来函数（lookahead）、边界用例必盖。用于新增或修改任何交易/选股信号、给策略加参数、评审交易功能实现、或排查「回测赚钱实盘亏钱」这类口径不一致问题。Use when implementing or reviewing trading signals, strategy parameters, or backtest entry/exit logic, or when a definition, units, or boundary (suspension, limit-up, adjustment, new listing) is unclear. Do not use for chart pattern reading (use stock-trading-system) or generic engineering governance (use developer-kit)."
---

# 交易信号落地标准

> **适用**：把「交易判据」（人话）变成「可回测、可解释、可复现的代码」。
> **不适用**：判断行情（那是 `stock-trading-system`）；通用工程治理（那是 `developer-kit`）。

## 0. 一句话

> 判据先落成**一个纯函数**，口径写清**定义/量纲/边界**，才算能进策略；写不清口径的判据 = 还没想清楚。

## 1. 四条硬规则

1. **判据函数化**：判据先落成信号函数（纯函数、显式参数、边界在函数内处理），策略文件只做组合调用。
   **禁止在策略/组件里内联判据** —— 否则同一口径会在不同入口各写一遍，早晚不一致。
2. **口径三件套**：每个信号函数必须写清 ①**定义式**（算什么、以谁为基准）②**量纲/单位**（%、倍、元、天）③**边界**（含不含当天、不足样本、停牌、一字板、复权、新股、ST、数据缺口）。
   并在项目的口径登记表里登记一行（见 [`chapters/01-criteria-to-code.md`](chapters/01-criteria-to-code.md)）。
3. **推算值必须登记**：`estimate_*` / `next_*` / 「用最新价推算明日」这类函数**可以存在**（只读当天及之前的数据不算未来函数），但**必须登记用途并写清假设**（假设了什么价格、用在哪一段判断）。
   **一律禁止**：把推算值当成「已知的未来数据」参与选股/回测信号。盘中信号必须显式带 `as_of`。
   详见 [`chapters/02-lookahead-and-edges.md`](chapters/02-lookahead-and-edges.md)。
4. **边界用例必盖**：新判据至少配 1 个 golden 用例 + 边界用例（停牌 / 一字板无法成交 / 除权 / 不足 N 根 / ST / 缺口）。金标准必须**注入违规就变红**，否则不算守卫。

## 2. 落地三步（按目标项目探测，不假设目录）

| 步 | 做什么 | 产物 |
|---|---|---|
| ① 探测 | 判据函数在哪一层？参数怎么声明？有没有 tests/、docs/？ | 一句话写清落点 |
| ② 登记 | 建/更新 `docs/TRADING_METRICS.md`，**先登记在用的**，不要求一次全登记 | 每个判据一行 |
| ③ 守卫 | 用 [`templates/signal_guard_test.py`](templates/signal_guard_test.py) 落成测试；存量用白名单承接，新判据必须合规 | 一条能变红的测试 |

## 3. 何时该读哪一章

| 场景 | 读 |
|---|---|
| 新增一个判据 / 给策略加参数 / 评审别人的信号实现 | [`chapters/01-criteria-to-code.md`](chapters/01-criteria-to-code.md) |
| 怀疑回测偷看了未来 / 边界要不要处理 / 写守卫测试 | [`chapters/02-lookahead-and-edges.md`](chapters/02-lookahead-and-edges.md) |

## 4. 与知识体系的分工

- **判据从哪来**：`stock-trading-system`（主线/买点/洗盘/风控那套人话）。
- **判据怎么落地**：本技能。
- **本技能不复制判据内容**，只按名字引用 —— 判据改了口径时只改一处，避免两边漂移。

## 5. 交付前自检（5 问）

1. 这个判据是**函数**还是散在策略里？
2. 定义式/量纲/边界，**写在哪**？能指到行吗？
3. 有没有用到「当前 K 线之后」的数据？
4. 样本不足 / 停牌 / 一字板时返回什么？是 `None` 还是 `0`/`False`（两者含义完全不同）？
5. 守卫测试**注入违规会不会红**？
