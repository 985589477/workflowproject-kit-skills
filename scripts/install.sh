#!/usr/bin/env bash
# install.sh —— 把本 kit 安装到 DSH / Cursor / Codex / 任意项目
#
# 核心事实（来自各家官方文档，2026-01）：
#   · Agent Skills 是**跨工具开放标准**（agentskills.io），各家都读 `SKILL.md` + frontmatter。
#   · Cursor 自动加载：.agents/skills/、.cursor/skills/、~/.agents/skills/、~/.cursor/skills/，
#     **并且为兼容也读 .claude/skills/、.codex/skills/、~/.claude/skills/、~/.codex/skills/**
#   · Cursor **递归**扫描 skills 根 —— 「任意深度的 SKILL.md 都会被找到」。
#   · DSH 只扫**一层** `<根>/*/SKILL.md`（实测：6 个能力包曾嵌在 `kits/` 下，
#     frontmatter 全合法却 0 个被注册）——所以本仓库把它们摊平成 `skills/<kit>/`。
#   · frontmatter 的 `name` **必须等于父目录名**。
#
# 结论：`~/.codex/skills/` 是 DSH、Cursor、Codex 三家**共同读取**的位置。
#       所以默认只装这一处，就能三家通用；只因为 DSH 不递归，才需要给 6 个能力包各建一个链接。
#
# 用法：
#   ./install.sh                 # 装到 ~/.codex/skills/（三家通用）
#   ./install.sh --cursor        # 只装 ~/.cursor/skills/（**替代**默认根，不是叠加）
#   ./install.sh --dsh           # 只装 DSH harness 的 skills 根（同上）
#   ./install.sh --all           # 三个根都装（同一个 skill 出现 3 次，谁生效不确定）
#   ./install.sh --project PATH  # 装进某个项目（.agents/skills/ + AGENTS.md + .cursor 规则）
#   ./install.sh --copy          # 用拷贝代替符号链接（默认符号链接，零漂移）
#   ./install.sh --replace       # 已有同名实体目录时：先改名备份再换成链接（默认跳过）
#   ./install.sh --uninstall     # 卸载：删链接；实体目录**只在与仓库逐字节相同时**才删
#   ./install.sh --dry-run       # 只打印将要做什么
#
# 为什么 --cursor/--dsh 是"替代"而不是"叠加"：三家**都读** ~/.codex/skills，
# 装两处 = 同一个 skill 出现两次 = 谁生效不确定。要装两个根就分两次跑
# （例：`--copy`，再 `--dsh --copy`）。

set -euo pipefail

KIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIT_NAME="$(basename "$KIT_ROOT")"
# skills/ 下除入口以外的技能：安装/卸载/前置校验都按这个清单走。
# 新增技能时在这里加一行（目前 8 个 = 入口 workflowproject-kit + 下面 7 个）。
SUBSKILLS=(project-governance-kit team-orchestration-kit product-manager-kit ui-designer-kit developer-kit tester-kit stock-trading-system)
MAIN_DIR="workflowproject-kit"    # 入口 skill 的目录名（= frontmatter name）
SKILLS_ROOT="$KIT_ROOT/skills"    # 8 个 skill 都是这一层的直属子目录

CODEX_ROOT="${CODEX_HOME:-$HOME/.codex}/skills"
CURSOR_ROOT="$HOME/.cursor/skills"
if [ -n "${DSH_HOME:-}" ]; then
  # 注意：DSH_HOME 已经指到 .../dsh-desktop/harness，所以 skills 根是 $DSH_HOME/skills。
  # 别再拼一次 /harness —— 那会得到 harness/harness/skills（实测踩过）。
  DSH_ROOT="$DSH_HOME/skills"
elif [ -d "$HOME/Library/Application Support/dsh-desktop/harness" ]; then
  DSH_ROOT="$HOME/Library/Application Support/dsh-desktop/harness/skills"
else
  DSH_ROOT="$HOME/.dsh/harness/skills"
fi

DO_CODEX=0; DO_CURSOR=0; DO_DSH=0; MODE="link"; DRY=0; UNINSTALL=0; PROJECT=""; REPLACE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --cursor)    DO_CURSOR=1 ;;
    --dsh)       DO_DSH=1 ;;
    --all)       DO_CODEX=1; DO_CURSOR=1; DO_DSH=1 ;;
    --project)   PROJECT="${2:-}"; shift ;;
    --copy)      MODE="copy" ;;
    --uninstall) UNINSTALL=1 ;;
    --replace)   REPLACE=1 ;;
    --dry-run)   DRY=1 ;;
    -h|--help)   sed -n '2,/^set -euo pipefail/p' "$0" | sed '$d' | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "未知参数：$1（用 --help 看用法）" >&2; exit 2 ;;
  esac
  shift
done

# 默认：装到三家通用的 ~/.codex/skills。显式给了某个目标（--cursor/--dsh/--all）时**只装那一处**
# —— 因为三家都读 ~/.codex/skills，装两处会让同一个 skill 出现两次、谁生效不确定。
if [ "$DO_CODEX$DO_CURSOR$DO_DSH" = "000" ] && [ -z "$PROJECT" ]; then DO_CODEX=1; fi
[ "$UNINSTALL" = "1" ] && DRY=0

log()  { printf '%s\n' "$*"; }
# note() 写 stderr：命令替换 $(f) 只捕获 stdout，所以函数内部的提示/报错必须走 stderr，
# 否则提示文字会被当成函数返回值（实测踩过）。
note() { printf '%s\n' "$*" >&2; }

# 安装一个 skill 到某个 skills 根。$1=父目录 $2=源目录（含 SKILL.md）$3=目标名
install_one() {
  local root="$1" src="$2" name="$3"
  # 必须另起一行：同一行 local 的所有 RHS 会先展开，那时 $name 还没赋值（set -u 会直接报错）
  local dest="$root/$name"
  if [ "$MODE" = "copy" ]; then
    if [ "$DRY" = "1" ]; then log "  [dry-run] 拷贝 $dest"; return 0; fi
    # 不用 rsync：Windows 的 Git Bash 里没有它；而 DSH 侧**只能**拷贝（它拒绝含符号链接的
    # skill 来源），所以拷贝模式必须真的能用。只覆盖同名文件、不做 --delete ——
    # 与 install_one 的"绝不 rm 用户的东西"一致。
    mkdir -p "$dest"; cp -R "$src/." "$dest/"
    log "  ✓ 拷贝 $dest"
  else
    if [ -e "$dest" ] && [ ! -L "$dest" ]; then
      if [ "$REPLACE" != "1" ]; then
        log "  ⚠️  跳过（已存在实体目录，不是链接）：$dest"
        log "      要改用它：加 --replace（会先改名备份，绝不删除），或手动移开。"
        return 0
      fi
      # --replace：改名备份（同级、带时间戳），再建链接。绝不 rm 用户的东西。
      local bak="$dest.backup-$(date +%Y%m%d-%H%M%S)"
      if [ "$DRY" = "1" ]; then
        log "  [dry-run] 备份 $dest → $(basename "$bak")，然后链接到 $src"
        return 0
      fi
      mv "$dest" "$bak" || { log "  ❌ 备份失败，未改动：$dest"; return 1; }
      log "  · 已备份：$bak"
    fi
    if [ -L "$dest" ] && [ "$(readlink "$dest")" = "$src" ]; then
      log "  · 已是最新：$dest"; return 0
    fi
    if [ "$DRY" = "1" ]; then log "  [dry-run] 链接 $dest → $src"; return 0; fi
    # 先建目录再链接；任一步失败就报错，绝不打印成功（act 曾在做之前就打印 ✓，撒谎过）
    mkdir -p "$root" || { log "  ❌ 建不了目录：$root"; return 1; }
    ln -sfn "$src" "$dest" || { log "  ❌ 链接失败：$dest"; return 1; }
    log "  ✓ 链接 $dest → $src"
  fi
}

# 卸载一个 skill。$1=父目录 $2=目标名 $3=对应的仓库源目录（用于逐字节比对）
# 安全线：链接直接删；**实体目录只有与仓库源逐字节相同才删** —— 拷贝模式下那份就是本脚本
# 建的，删它安全；用户改过、有多余文件、或没有源可比对，一律保留并给出手动删除命令。
uninstall_one() {
  local root="$1" name="$2" src="${3:-}"
  local dest="$root/$name"   # 同上：不能和上一行合并
  if [ -L "$dest" ]; then rm -f "$dest"; log "  ✓ 已删链接 $dest"
  elif [ -d "$dest" ]; then
    if [ -n "$src" ] && [ -d "$src" ] && diff -r -q "$src" "$dest" >/dev/null 2>&1; then
      rm -rf "$dest"; log "  ✓ 已删拷贝（与仓库逐字节相同）$dest"
    else
      log "  ⚠️  保留实体目录（与仓库不一致，或没有可比对的源）：$dest"
      log "      确认不要了就手动删：rm -rf \"$dest\""
    fi
  elif [ -e "$dest" ]; then log "  ⚠️  保留（不是目录）：$dest"
  else log "  · 不存在：$dest"; fi
}

check_frontmatter() {
  local sk="$1/SKILL.md" dir
  dir="$(basename "$1")"
  [ -f "$sk" ] || { note "  ❌ $1 缺 SKILL.md"; return 1; }
  local nm
  nm="$(awk '/^name:/{print $2; exit}' "$sk")"
  grep -q '^description:' "$sk" || { note "  ❌ $dir 缺 description"; return 1; }
  [ -n "$nm" ] || { note "  ❌ $dir 缺 name"; return 1; }
  # 目录名不必等于 name：安装目标以 frontmatter 的 name 为准（clone 成什么目录名都行）。
  [ "$nm" = "$dir" ] || note "  · 目录名 $dir ≠ name: $nm —— 按 name 安装，不影响结果"
  printf '%s' "$nm"
}

log "kit: $KIT_ROOT"
log "模式: $MODE$([ "$DRY" = "1" ] && echo '（dry-run）')$([ "$UNINSTALL" = "1" ] && echo '（卸载）')"
log ""

# 前置校验：name / description 必须存在。
# 安装目标名 = frontmatter 的 name，所以 clone 出来的目录叫什么名字都无所谓
# （比如仓库叫 workflowproject-kit-skills，skill 名仍是 workflowproject-kit）。
log "前置校验："
FAIL=0
MAIN_NAME="$(check_frontmatter "$SKILLS_ROOT/$MAIN_DIR")" || FAIL=1
KIT_NAME="${MAIN_NAME:-$KIT_NAME}"
for k in "${SUBSKILLS[@]}"; do check_frontmatter "$SKILLS_ROOT/$k" >/dev/null 2>&1 || FAIL=1; done
if [ "$FAIL" = "0" ]; then
  log "  ✓ $(( ${#SUBSKILLS[@]} + 1 )) 个 skill 的 frontmatter 都合法；安装名以 name: 为准（= ${KIT_NAME}）"
else
  log ""
  log "frontmatter 有问题，先修再装。"
  exit 1
fi
log ""

targets=()
[ "$DO_CODEX" = "1" ] && targets+=("$CODEX_ROOT")
[ "$DO_CURSOR" = "1" ] && targets+=("$CURSOR_ROOT")
[ "$DO_DSH" = "1" ] && targets+=("$DSH_ROOT")

for root in "${targets[@]:-}"; do
  [ -n "$root" ] || continue
  log "目标：$root"
  if [ "$UNINSTALL" = "1" ]; then
    uninstall_one "$root" "$KIT_NAME" "$SKILLS_ROOT/$MAIN_DIR"
    for k in "${SUBSKILLS[@]}"; do uninstall_one "$root" "$k" "$SKILLS_ROOT/$k"; done
  else
    install_one "$root" "$SKILLS_ROOT/$MAIN_DIR" "$KIT_NAME"
    for k in "${SUBSKILLS[@]}"; do install_one "$root" "$SKILLS_ROOT/$k" "$k"; done
  fi
  log ""
done

if [ -n "$PROJECT" ]; then
  [ -d "$PROJECT" ] || { log "项目目录不存在：$PROJECT" >&2; exit 2; }
  log "项目：$PROJECT"
  if [ "$UNINSTALL" = "1" ]; then
    uninstall_one "$PROJECT/.agents/skills" "$KIT_NAME" "$SKILLS_ROOT/$MAIN_DIR"
    for k in "${SUBSKILLS[@]}"; do uninstall_one "$PROJECT/.agents/skills" "$k" "$SKILLS_ROOT/$k"; done
  else
    # 项目级：只装主 skill（6 个能力包通过它按需引用，不必各建一份）
    install_one "$PROJECT/.agents/skills" "$SKILLS_ROOT/$MAIN_DIR" "$KIT_NAME"
    log "  · 生成项目规则（AGENTS.md + .cursor/rules/*.mdc + AI-WORKFLOW-RULES.md）"
    if [ "$DRY" = "1" ]; then
      log "  [dry-run] python3 $KIT_ROOT/scripts/install_project.py $PROJECT"
    else
      python3 "$KIT_ROOT/scripts/install_project.py" "$PROJECT" >/dev/null && log "  ✓ 已生成"
    fi
  fi
  log ""
fi

# 装完后主动提示：其它技能根里若有**同名实体目录**，会造成同名冲突
if [ "$UNINSTALL" != "1" ]; then
  STALE=""
  for other in "$CODEX_ROOT" "$CURSOR_ROOT" "$DSH_ROOT" "$HOME/.agents/skills"; do
    [ -n "$other" ] || continue
    case " ${targets[*]:-} " in *" $other "*) continue ;; esac
    [ -e "$other/$KIT_NAME" ] && [ ! -L "$other/$KIT_NAME" ] && STALE="$STALE\n    $other/$KIT_NAME"
  done
  if [ -n "$STALE" ]; then
    log "⚠️  发现其它技能根里有同名实体目录（会造成同名冲突，谁生效不确定）："
    printf '%b\n' "$STALE"
    log "    建议改名备份（不删）：mv <上面路径> <上面路径>.backup-\$(date +%Y%m%d)"
    log ""
  fi
fi

if [ "$UNINSTALL" != "1" ]; then
  log "完成。验证："
  log "  # 看链接是否建好"
  for root in "${targets[@]:-}"; do [ -n "$root" ] && log "  ls -la \"$root\""; done
  log "  # 重启 DSH / Cursor 后，skill 应出现在各自的技能列表里"
  log ""
  log "注意："
  log "  · DSH 只扫一层 skills/*/SKILL.md，所以 6 个能力包必须各有一个条目（本脚本已建）。"
  log "  · Cursor 递归扫描，即使只装主 skill 也能发现嵌套的 6 个；但显式条目更清晰。"
  log "  · 符号链接模式下，改仓库 = 改已安装的 skill，不会漂移。"
  log "  · 默认只装 ~/.codex/skills 一处就够（DSH / Codex / Cursor 三家都读它）。"
  log "    不要用 --all：那会让 DSH 和 Cursor 各自看到同一个 skill 两次。"
fi
