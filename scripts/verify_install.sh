#!/usr/bin/env bash
# verify_install.sh —— 确认本 kit 是否已在各工具里生效
#
# 为什么需要它：skill 装错了**不会报错**，只会"列表里看不到"或"还是旧内容"。
# 这条命令把所有技能根扫一遍，告诉你每个 skill 是从哪加载的、是不是新版本、
# 有没有同名冲突（同名 skill 出现在多个根里时，谁生效是不确定的）。
#
# 用法：./scripts/verify_install.sh
# 退出码：0 = 7 个 skill 都能在某个根里解析到；1 = 有缺失或冲突

set -uo pipefail

KIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SUBSKILLS=(project-governance-kit team-orchestration-kit product-manager-kit ui-designer-kit developer-kit tester-kit)

if [ -n "${DSH_HOME:-}" ]; then DSH_ROOT="$DSH_HOME/skills"
elif [ -d "$HOME/Library/Application Support/dsh-desktop/harness" ]; then
  DSH_ROOT="$HOME/Library/Application Support/dsh-desktop/harness/skills"
else DSH_ROOT="$HOME/.dsh/harness/skills"; fi

ROOTS=("$DSH_ROOT" "$HOME/.codex/skills" "$HOME/.cursor/skills" "$HOME/.agents/skills")

# 本 kit 自带的主 skill 名（从 frontmatter 读，不写死）
MAIN_SKILL="$KIT_ROOT/skills/workflowproject-kit"
MAIN_NAME="$(awk '/^name:/{print $2; exit}' "$MAIN_SKILL/SKILL.md" 2>/dev/null)"
[ -n "$MAIN_NAME" ] || { echo "❌ 读不到 $MAIN_SKILL/SKILL.md 的 name" >&2; exit 2; }
ALL=("$MAIN_NAME" "${SUBSKILLS[@]}")

echo "kit:   ${KIT_ROOT}（SKILL.md $(wc -l < "$MAIN_SKILL/SKILL.md" | tr -d ' ') 行）"
echo "扫描的技能根："
for r in "${ROOTS[@]}"; do [ -d "$r" ] && echo "  ✓ $r" || echo "  · ${r}（不存在）"; done
echo

missing=0; conflicts=0; found=0
for name in "${ALL[@]}"; do
  hits=()
  # 注意：断掉的符号链接对 -e 是 false（因为目标不存在），所以要单独用 -L 认出来，
  # 否则仓库搬家后会被误报成"没装"，而不是"链接断了"。
  for r in "${ROOTS[@]}"; do [ -e "$r/$name" ] || [ -L "$r/$name" ] && hits+=("$r/$name"); done

  if [ ${#hits[@]} -eq 0 ]; then
    printf '  ❌ %-26s 任何根里都没有 → 不会被触发\n' "$name"
    missing=$((missing+1)); continue
  fi

  found=$((found+1))
  printf '  %s %-26s\n' "$([ ${#hits[@]} -gt 1 ] && echo '⚠️ ' || echo '✅')" "$name"
  [ ${#hits[@]} -gt 1 ] && conflicts=$((conflicts+1))

  for h in "${hits[@]}"; do
    kind="实体目录"
    if [ -L "$h" ]; then
      kind="链接 → $(readlink "$h")"
      [ -d "$h" ] || kind="$kind  ❌ 断链（目标不存在）—— 仓库搬过家？重跑 install.sh 即可重新指向"
    fi
    sk="$h/SKILL.md"
    if [ -r "$sk" ]; then
      lines="$(wc -l < "$sk" | tr -d ' ')"
      fm="$(awk '/^name:/{print $2; exit}' "$sk")"
      printf '       %s\n' "$(dirname "$h")  [$kind]  ${lines} 行  name=$fm"
    else
      printf '       %s  [%s]  ❌ 读不到 SKILL.md\n' "$(dirname "$h")" "$kind"
    fi
  done
done

echo
if [ "$conflicts" -gt 0 ]; then
  echo "⚠️  $conflicts 个 skill 出现在多个根里 —— 谁生效不确定，建议只留一处。"
  echo "      推荐：只留 ~/.codex/skills 那一处 —— DSH、Codex、Cursor 三家都读它，"
  echo "            它一处就够；--all 反而会让 DSH/Cursor 各看到同一 skill 两次。"
  echo "      清理：./scripts/install.sh            # 装到 ~/.codex/skills（默认）"
  echo "            然后把其它根里的同名条目改名备份（加 .backup-日期 后缀）"
fi
if [ "$missing" -gt 0 ]; then
  echo "❌ $missing 个 skill 找不到 → 装一下： ./scripts/install.sh"
  exit 1
fi
echo "✅ 7 个 skill 都能解析到（若上面有 ⚠️ 先消掉冲突）。重启 DSH / Cursor 后生效。"
echo
echo "触发测试：新会话里让 AI 做一件「大范围重构」或「接手已有项目」的事，"
echo "看它是否先输出开跑门禁状态行、并去读 gates/01-baseline-freeze.md。"
exit 0
