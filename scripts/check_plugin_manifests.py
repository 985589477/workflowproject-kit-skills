#!/usr/bin/env python3
"""校验 .cursor-plugin/ 清单是否符合 Cursor 的插件规范。

为什么要它：清单坏了 Cursor 只会**静默不显示**，不会给你有用的报错。
规则来自 https://cursor.com/docs/reference/plugins.md（2026-01）。

检查项：
  1. marketplace.json 必填：name / owner.name / plugins
  2. 每个插件条目：name 是 kebab-case；source 是相对路径、不含 `..`
  3. source 目录存在且含 SKILL.md
  4. **Root Skill 冲突**：source 里同时有 `skills/` 目录和根 `SKILL.md` 时，
     根 `SKILL.md` 会被忽略（文档明确写的 fallback 规则）—— 这正是本仓库会踩的坑
  5. 每个 skill 的 frontmatter `name:` 必须等于其目录名
  6. 清单文件 ≤ 10 MB

用法：python3 scripts/check_plugin_manifests.py [kit 根目录]
退出码：0 通过；1 有问题；2 用法/文件缺失
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

KEBAB = re.compile(r"^[a-z0-9]([a-z0-9.-]*[a-z0-9])?$")
MAX_MANIFEST_BYTES = 10 * 1024 * 1024


def frontmatter_name(skill_dir: pathlib.Path) -> str | None:
    sk = skill_dir / "SKILL.md"
    if not sk.is_file():
        return None
    m = re.search(r"^name:\s*(\S+)\s*$", sk.read_text(encoding="utf-8", errors="ignore"), re.M)
    return m.group(1) if m else None


def main(argv: list[str]) -> int:
    root = pathlib.Path(argv[1] if len(argv) > 1 else ".").expanduser().resolve()
    cp = root / ".cursor-plugin"
    if not cp.is_dir():
        print(f"❌ 找不到 {cp}", file=sys.stderr)
        return 2

    errors: list[str] = []
    checked: list[str] = []

    for name in ("marketplace.json", "plugin.json"):
        f = cp / name
        if not f.is_file():
            errors.append(f"缺 {name}")
            continue
        if f.stat().st_size > MAX_MANIFEST_BYTES:
            errors.append(f"{name} 超过 10 MB")
        try:
            json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{name} 不是合法 JSON：{exc}")

    mp_file = cp / "marketplace.json"
    if mp_file.is_file():
        mp = json.loads(mp_file.read_text(encoding="utf-8"))
        for field in ("name", "owner", "plugins"):
            if field not in mp:
                errors.append(f"marketplace.json 缺必填字段 {field}")
        if not isinstance(mp.get("owner"), dict) or "name" not in mp.get("owner", {}):
            errors.append("marketplace.json 的 owner 缺 name")
        if not KEBAB.match(mp.get("name", "")):
            errors.append(f"marketplace name 不是 kebab-case：{mp.get('name')}")

        for entry in mp.get("plugins", []):
            pname = entry.get("name", "")
            src = entry.get("source")
            if not pname:
                errors.append(f"插件条目缺 name：{entry}")
                continue
            if not KEBAB.match(pname):
                errors.append(f"插件 name 不是 kebab-case：{pname}")
            if src is None:
                continue
            if src.startswith("/") or ".." in pathlib.PurePosixPath(src).parts:
                errors.append(f"{pname}: source 必须是相对路径且不含 ..：{src}")
                continue
            d = (root / src).resolve()
            if not d.is_dir():
                errors.append(f"{pname}: source 目录不存在：{src}")
                continue
            if not (d / "SKILL.md").is_file():
                errors.append(f"{pname}: {src} 里没有 SKILL.md")
            if (d / "skills").is_dir():
                errors.append(
                    f"{pname}: {src} 同时有 skills/ 目录和根 SKILL.md —— "
                    f"按 Cursor 文档，此时根 SKILL.md 会被忽略"
                )
            nm = frontmatter_name(d)
            if nm and nm != d.name:
                errors.append(f"{pname}: frontmatter name: {nm} ≠ 目录名 {d.name}")
            checked.append(f"{pname} → {src}")

    # plugin.json 指向的根 skill 也要自查
    nm = frontmatter_name(root)
    if nm and nm != root.name:
        print(f"  · 提示：根目录名 {root.name} ≠ name: {nm}（不影响插件，安装时按 name 走）")

    print(f"kit 根：{root}")
    print(f"检查了 {len(checked)} 个插件条目：")
    for c in checked:
        print(f"  ✓ {c}")
    if errors:
        print(f"\n❌ {len(errors)} 个问题：")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("\n✅ 清单全部符合规范")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
