# 这个目录是什么（以及为什么它没有生成器）

> 这是 workflowproject-kit 的**无生成器形态**：一个普通目录，直接就是可安装的 skill。
> 它同时也是**新仓库的根** —— 用 git 跟踪它，就等于"把 skill 做了记录"。

## 为什么去掉生成器

旧架构是：`14-exports/<6 kit>` →（`tools/export_unified_kit.py` 生成）→ `14-exports/workflowproject-kit/`。

那个生成器**本身**制造了一整类维护问题（都有实测证据）：

| 生成器带来的问题 | 证据 | 新形态为何不存在 |
|---|---|---|
| 导出物被整体删除重建，手写内容会被**静默覆盖** | `export_unified_kit.py:640` `shutil.rmtree(OUTPUT)` | 没有导出步骤 |
| 入口 `SKILL.md` 是脚本里的 **111 行内联常量** | `UNIFIED_SKILL = """..."""` | 入口就是一个普通 `.md` |
| 两个文件**逐字节相同**（构造性重复） | L674/675 用同一个 `AGENTS_CONTENT` 写两次 | 各自是普通文件，已被拆开 |
| 安装器是 **134 行内联字符串**，改它要在字符串里改 | `INSTALLER = r'''...'''` | `scripts/install_project.py` 是普通文件 |
| 仓库与已安装副本**必然漂移** | `cp -R` 安装 | 用**符号链接**安装，零漂移 |
| `product-manager-kit` 有两份不同内容 | `14-exports/` 里一份 + `~/.codex/skills/` 一份 | 一份源，符号链接指向它 |

**结论**：真正的问题不是"内容太多"，是"有生成器"。删掉它，这类问题全部消失。

## 目录结构

```text
workflowproject-kit/          ← 新仓库根 = 可直接安装的 skill
├── SKILL.md                  ← 入口（门禁表，唯一必读，110 行）
├── AI-WORKFLOW-RULES.md      ← 指针文件（规则本体在 SKILL.md / 项目 AGENTS.md）
├── gates/01..08-*.md         ← 8 个门禁（按需单独读，不要通读）
├── templates/                ← 3 个模板（门禁的产出载体）
├── scripts/
│   ├── check_gates.py        ← 可运行门禁校验（会报红，可进 pre-commit）
│   └── install_project.py    ← 往目标项目安装 AGENTS.md 等（默认不拷能力包）
└── kits/                     ← 6 个能力包，**原样保留，一个字节未改**
    ├── project-governance-kit/   （772 行）
    ├── team-orchestration-kit/   （2,035）
    ├── product-manager-kit/      （7,913）
    ├── ui-designer-kit/          （3,255）
    ├── developer-kit/            （10,923）
    └── tester-kit/               （2,133）
```

**注意**：`kits/` 里的 27,031 行是**原样搬运**的，我**没有改**任何内容（我只读了其中 1.1%，
没有资格改）。新加的东西全在 `kits/` **之外**：入口、8 个门禁、3 个模板、2 个脚本。

## 安装（符号链接，不是拷贝）

```bash
# 1) 把这个目录放到你选定的位置（它将成为 git 仓库的根）
mv workflowproject-kit ~/Desktop/workflowproject-kit      # 或任何位置

# 2) 用符号链接安装到 skill 根（零漂移：改仓库 = 改已安装的 skill）
H="$HOME/Library/Application Support/dsh-desktop/harness/skills"
rm -rf "$H/workflowproject-kit"
ln -s ~/Desktop/workflowproject-kit "$H/workflowproject-kit"

# 3) 6 个能力包各自注册成 skill（harness 只扫一层 skills/*/SKILL.md）
S="$HOME/.codex/skills"
for k in project-governance-kit team-orchestration-kit product-manager-kit ui-designer-kit developer-kit tester-kit; do
  [ -e "$S/$k" ] || ln -s ~/Desktop/workflowproject-kit/kits/$k "$S/$k"
done
```

> ⚠️ `product-manager-kit` 在 `~/.codex/skills/` **已有一份独立拷贝（内容不同）**。
> 上面第 3 步会跳过它。**你需要决定留哪份** —— 两份并存必然漂移。
> 建议：留 `kits/product-manager-kit`（跟仓库走，可版本控制），
> 删掉 `~/.codex/skills/product-manager-kit` 的实体、改成指向仓库的符号链接。

## 验证

```bash
# 入口行数（应为 ~110）
wc -l SKILL.md

# Cursor 插件清单是否合规（坏了 Cursor 只会静默不显示）
python3 scripts/check_plugin_manifests.py .

# 对任意项目跑门禁校验
python3 scripts/check_gates.py /path/to/project
python3 scripts/check_gates.py --audit /path/to/project   # 找出没证据的门禁（死规则）

# 引用完整性：SKILL.md 提到的路径都存在
grep -o '](\([^)]*\.md\))' SKILL.md
```

## 在 Cursor 里安装（三种方式，从简到繁）

依据：[Agent Skills](https://cursor.com/docs/skills) · [Plugins 参考](https://cursor.com/docs/reference/plugins)

**① 最简：`~/.codex/skills/`（Cursor 也读它）**
Cursor 为兼容会加载 `~/.codex/skills/`，而 `install.sh` 默认就装在那里。
`./scripts/install.sh` 一条命令即可，无需插件。

**② 项目级：`install.sh --project <路径>`**
生成 `.agents/skills/workflowproject-kit/` + `AGENTS.md` + `.cursor/rules/*.mdc`。
规则文件必须是 `.mdc`（`.md` 会被 Cursor **忽略**）。

**③ 从 GitHub 仓库安装（给别人用）**
仓库已含 `.cursor-plugin/marketplace.json` + `.cursor-plugin/plugin.json`，
符合 Cursor 的 multi-plugin 规范：

```bash
# 先在本地按官方方式试装（可选）
mkdir -p ~/.cursor/plugins/local
ln -s "$PWD" ~/.cursor/plugins/local/workflowproject-kit   # 或直接拷贝
# 然后 Cursor → Customize → 确认出现 7 个插件条目
```

远程方式：Cursor → **Customize → From GitHub Repository**，填
`https://github.com/985589477/workflowproject-kit-skills`。
（团队用户走 Dashboard → Plugins & MCPs → Team Marketplaces → Add Marketplace。
公开市场需提交审核：cursor.com/marketplace/publish）

**为什么仓库布局天然合规**：Cursor 有一条 `Root Skill` 规则 ——
`SKILL.md` 在插件根、且没有 `skills/` 目录时，整个包被当作**单 skill 插件**。
本仓库正好如此（入口在根，6 个能力包在 `kits/` 而非 `skills/`），
所以只需 2 个清单文件，**不用改任何目录结构**。

> ⚠️ 诚实说明：这 2 个清单是**按官方文档 schema 写的**，并用
> `scripts/check_plugin_manifests.py` 校验过（路径存在、kebab-case、Root Skill 不冲突）。
> 但**我无法在这里用真实 Cursor 验证它的解析行为** —— 本机没有 Cursor。
> 如果 Customize 里没出现条目，先跑上面那个校验脚本，再对照
> [Plugins 参考](https://cursor.com/docs/reference/plugins.md)。

## 已做的验证（实测，不是"应该能跑"）

| 项 | 结果 |
|---|---|
| 引用完整性 | ✅ SKILL.md 的 **10 个引用全部存在** |
| 6 个能力包 frontmatter 可注册性 | ✅ 全部含 `name` + `description` |
| `check_gates.py` | ✅ 三个用例（空项目报红 / 合格项目通过 / StockTools 8-8 通过） |
| `install_project.py` | ✅ `--help` 正常，`--with-kits` 生效 |
| `SKILL.md` 行数 | ✅ **110 行**（目标 ≤120） |
| 6 个能力包内容 | ✅ **一个字节未改**（27,031 行原样） |
| Cursor 插件清单 | ✅ 7 个插件条目，路径存在 / kebab-case / Root Skill 不冲突 |
| `check_plugin_manifests.py` | ✅ 两个用例：正常通过；注入 3 个破坏（坏 name / 路径不存在 / 缺 SKILL.md）→ **全部抓到，退出码 1** |

## 处理那份重复的 `product-manager-kit`

`~/.codex/skills/product-manager-kit`（59 文件 / 6,975 行）与本仓库的
`kits/product-manager-kit`（64 文件 / 7,913 行）**是两份不同的打包**：

| | 旧（`~/.codex/skills/`） | 新（本仓库） |
|---|---|---|
| 形态 | **wrapper 式**：真内容在 `references/product-manager-kit/` 下 | **直接导出**：`scorecards/` `templates/` `workflows/` 平铺 |
| SKILL.md | 英文，写明 "based on the exported package in `references/...`" | 中文框架 |
| 独有文件 | 只有 `agents/openai.yaml`（3 行**显示元数据**，无任何引用） | 其余**全覆盖** |

**本仓库那份是超集**，且可版本控制。建议替换（`install.sh` 会**跳过**已存在的实体目录，
所以必须手动处理一次）：

```bash
# ① 备份旧的（不要直接删）
mv ~/.codex/skills/product-manager-kit ~/.codex/skills/_backup-product-manager-kit-$(date +%Y%m%d)

# ② 换成指向仓库的符号链接
ln -s "$PWD/kits/product-manager-kit" ~/.codex/skills/product-manager-kit

# ③ 确认
ls -la ~/.codex/skills/
```

> 上面 `$PWD` 指本仓库根目录。确认没问题后再删 `_backup-*`。
