#!/usr/bin/env bash
# self_check.sh —— 本仓库对自己的检查（改完任何东西都该跑一遍）
#
# 为什么存在：下面第 2 项抓的这个 bug，我在同一个下午犯了 3 次 ——
# `$VAR` 后面紧跟全角括号时，bash 会把多字节字符**吞进变量名**，
# 于是在 `set -u` 下报 `unbound variable`，而且**只在那一行真的被执行时才炸**
# （字符串里的变量是执行时展开，所以正常路径测不出来）。
# 教训：这种"只在报错路径触发"的 bug，靠人工测试抓不住，必须机器扫。
#
# 用法：./scripts/self_check.sh
# 退出码：0 = 全过；1 = 有问题

set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
PY="${PYTHON:-python3}"
fail=0
ok()   { printf '  ✅ %s\n' "$1"; }
bad()  { printf '  ❌ %s\n' "$1"; fail=1; }

echo "① shell 语法（bash -n）"
for f in scripts/*.sh; do
  [ -e "$f" ] || continue
  if bash -n "$f" 2>/dev/null; then ok "$f"; else bad "$f"; bash -n "$f"; fi
done

echo
echo "② \$VAR 紧跟非 ASCII 字符（bash 会把它吞进变量名 → set -u 下 unbound variable）"
hits=$(grep -rnE '\$[A-Za-z_][A-Za-z0-9_]*[^ -~]' scripts/*.sh 2>/dev/null | grep -v '^\s*#' || true)
if [ -z "$hits" ]; then
  ok "0 处（正确写法：\${VAR}）"
else
  bad "以下位置要改成 \${VAR}："
  printf '%s\n' "$hits" | sed 's/^/      /'
fi

echo
echo "③ Cursor 插件清单"
if $PY scripts/check_plugin_manifests.py . >/dev/null 2>&1; then ok "符合规范"; else bad "不合格，跑 $PY scripts/check_plugin_manifests.py . 看详情"; fi

echo
echo "④ SKILL.md 引用完整性（提到的路径都得存在）"
$PY - <<'PYEOF'
import pathlib, re, sys
N = pathlib.Path(".")
s = (N/"SKILL.md").read_text(encoding="utf-8")
refs = set(re.findall(r'\]\(([^)]+\.md)\)', s))
refs |= set(re.findall(r'`(scripts/[^`]+\.py|templates/[^`]+\.md|gates/[^`]+\.md)`', s))
refs |= {f"gates/{m}" for m in re.findall(r'gates/(\d+-[\w-]+\.md)', s)}
missing = sorted(r for r in refs if not (N/r).exists())
if missing:
    print(f"  ❌ {len(missing)} 个引用指向不存在的文件：")
    for m in missing: print(f"      {m}")
    sys.exit(1)
print(f"  ✅ {len(refs)} 个引用全部存在")
PYEOF
[ $? -ne 0 ] && fail=1

echo
echo "⑤ 7 个 skill 的 frontmatter（name + description，且 name 合法）"
$PY - <<'PYEOF'
import pathlib, re, sys
N = pathlib.Path(".")
bad = []
dirs = [N] + sorted(d for d in (N/"kits").iterdir() if d.is_dir())
for d in dirs:
    sk = d/"SKILL.md"
    if not sk.is_file():
        bad.append(f"{d.name}: 缺 SKILL.md"); continue
    t = sk.read_text(encoding="utf-8")
    if not t.startswith("---"): bad.append(f"{d.name}: 无 frontmatter"); continue
    fm = t.split("---", 2)[1]
    nm = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    ds = re.search(r"^description:\s*\S", fm, re.M)
    if not nm: bad.append(f"{d.name}: 缺 name")
    elif not re.fullmatch(r"[a-z0-9][a-z0-9-]*", nm.group(1)): bad.append(f"{d.name}: name 非法 {nm.group(1)}")
    if not ds: bad.append(f"{d.name}: 缺 description")
if bad:
    print(f"  ❌ {len(bad)} 个问题：")
    for b in bad: print(f"      {b}")
    sys.exit(1)
print(f"  ✅ {len(dirs)} 个 skill 的 frontmatter 都合法")
PYEOF
[ $? -ne 0 ] && fail=1

echo
if [ "$fail" = "0" ]; then echo "✅ 自检全过"; else echo "❌ 自检未通过"; fi
exit "$fail"
