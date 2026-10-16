# 这个目录是什么（以及为什么它没有生成器）

> 这是 workflowproject-kit 的**无生成器形态**：7 个 skill 就是 `skills/` 下的 7 个普通目录，
> 可直接安装。它同时也是**新仓库的根** —— 用 git 跟踪它，就等于"把 skill 做了记录"。
>
> **为什么是 `skills/<kit>/` 而不是 `kits/<kit>/`**：DSH 只扫技能根的**直属子目录**
> （`<根>/<名字>/SKILL.md`，见 `scripts/install.sh` 头注释里的实测记录）。`kits/` 这一层
> 没有 `SKILL.md`，会让 6 个能力包**一个都注册不上**；摊平到 `skills/` 之后，把 `skills/`
> 直接当技能根指过去就能全部识别。

## 为什么去掉生成器

旧架构是：`14-exports/<6 kit>` →（`tools/export_unified_kit.py` 生成）→ `14-exports/workflowproject-kit/`。

那个生成器**本身**制造了一整类维护问题（都有实测证据）：

| 生成器带来的问题 | 证据 | 新形态为何不存在 |
|---|---|---|
| 导出物被整体删除重建，手写内容会被**静默覆盖** | `export_unified_kit.py:640` `shutil.rmtree(OUTPUT)` | 没有导出步骤 |
| 入口 `SKILL.md` 是脚本里的 **111 行内联常量** | `UNIFIED_SKILL = """..."""` | 入口就是一个普通 `.md` |
| 两个文件**逐字节相同**（构造性重复） | L674/675 用同一个 `AGENTS_CONTENT` 写两次 | 各自是普通文件，已被拆开 |
| 安装器是 **134 行内联字符串**，改它要在字符串里改 | `INSTALLER = r'''...'''` | `scripts/install_project.py` 是普通文件 |
| 仓库与已安装副本**必然漂移** | `cp -R` 安装 | 按工具选安装方式：链接（零漂移，Codex/Cursor）或 `--copy`（DSH 不收符号链接） |
| `product-manager-kit` 有两份不同内容 | `14-exports/` 里一份 + `~/.codex/skills/` 一份 | 一份源，装进去的那份由 `install.sh` 同步 |

**结论**：真正的问题不是"内容太多"，是"有生成器"。删掉它，这类问题全部消失。

## 目录结构

```text
workflowproject-kit-skills/        ← 仓库根（放工具和文档，**不是**技能根）
├── skills/                       ← 技能根：7 个 skill 都是它的直属子目录
│   ├── workflowproject-kit/      ← 入口 skill
│   │   ├── SKILL.md              ← 门禁表（唯一必读，110 行）
│   │   ├── AI-WORKFLOW-RULES.md  ← 指针文件（规则本体在 SKILL.md / 项目 AGENTS.md）
│   │   ├── gates/01..08-*.md     ← 8 个门禁（按需单独读，不要通读）
│   │   ├── templates/            ← 3 个模板（门禁的产出载体）
│   │   └── scripts/check_gates.py ← 可运行门禁校验（会报红，可进 pre-commit）
│   ├── project-governance-kit/   （772 行）
│   ├── team-orchestration-kit/   （2,035）
│   ├── product-manager-kit/      （7,913）
│   ├── ui-designer-kit/          （3,255）
│   ├── developer-kit/            （10,923）
│   └── tester-kit/               （2,133）
├── scripts/                      ← 仓库工具（**不进技能包**）
│   ├── install.sh                ← 安装到各家技能根
│   ├── verify_install.sh         ← 校验 7 个 skill 是否都能解析到
│   ├── self_check.sh             ← 仓库自检（语法 / 引用完整性 / frontmatter）
│   ├── check_plugin_manifests.py ← Cursor 清单校验
│   └── install_project.py        ← 往目标项目装 AGENTS.md 等（默认不拷能力包）
├── docs/                         ← 仓库文档（含本文件）
└── .cursor-plugin/               ← Cursor 清单（7 个条目，source = skills/<kit>）
```

**注意**：`skills/<kit>/` 里的 27,031 行是**原样搬运**的，我**没有改**任何内容（我只读了其中 1.1%，
没有资格改）。新加的东西全在 6 个能力包**之外**：入口、8 个门禁、3 个模板、2 个脚本。

## 安装：**一条命令，只装一处**

```bash
# 把这个目录放到你选定的位置（它同时就是 git 仓库的根）
mv workflowproject-kit ~/Desktop/workflowproject-kit
cd ~/Desktop/workflowproject-kit

./scripts/install.sh --dry-run     # 先看要做什么
./scripts/install.sh               # 真装（默认 → ~/.codex/skills）
./scripts/verify_install.sh        # 确认 7 个 skill 都解析得到、没有同名冲突
```

> ⚠️ **装 DSH 必须加 `--copy`**：DSH 的技能来源**不接受符号链接**
> （`dsh-skills-manager` 里的符号链接检查会直接报 `error.source.symlink`）。
> 默认的链接模式对 Codex / Cursor 有效，对 DSH 无效：
> `./scripts/install.sh --copy`（拷贝模式已去掉 `rsync` 依赖，Git Bash 下也能跑）。

### 为什么默认只装 `~/.codex/skills` 一处就够

三家工具的技能根（官方文档 + 实测）：

| 工具 | 原生根 | 兼容读取 |
|---|---|---|
| **Codex** | `~/.codex/skills/` | — |
| **Cursor** | `~/.cursor/skills/`、`~/.agents/skills/`、项目内 `.cursor/skills/`/`.agents/skills/` | **`~/.codex/skills/`**、`~/.claude/skills/` 等 |
| **DSH** | `$DSH_HOME/skills/` | **`~/.codex/skills/`**（实测：目录里那份就是从这里读到的） |

→ **`~/.codex/skills/` 是三家共同读取的位置，一处即通吃。**

> ⚠️ **不要用 `--all`**：那会把同一个 skill 装进 3 个根，而 DSH 与 Cursor **各自**都会读
> 其中两个根 → 同一个 skill 出现两次、谁生效不确定。`--all` 只在"我确定只要某个根"时才用。

### 必须处理一次：harness 里的同名旧实体目录

DSH 自己的技能根里现在躺着一个**旧的 `workflowproject-kit` 实体目录**（108 行版）。
它是 `name: workflowproject-kit`，与 `~/.codex/skills` 里新装的那个**同名**。

`install.sh` 会主动警告这件事（不会覆盖你的目录）。处理方式：

```bash
H="$HOME/Library/Application Support/dsh-desktop/harness/skills"
mv "$H/workflowproject-kit" "$H/_backup-workflowproject-kit-$(date +%Y%m%d)"   # 改名备份，不删
./scripts/verify_install.sh                                                    # 应变成全 ✅ 无 ⚠️
```

> `product-manager-kit` 同理：`~/.codex/skills/` 里那份是**另一套打包**（wrapper 式、英文、
> 59 文件/6,975 行），本仓库那份是**超集**（平铺、中文、64 文件/7,913 行）。
> 旧版唯一独有的是 `agents/openai.yaml`（3 行显示元数据，无引用）。
> 处理：`mv ~/.codex/skills/product-manager-kit{,.backup-$(date +%Y%m%d)}` 后重跑 `install.sh`。

### 参数速查

```bash
./scripts/install.sh                 # 默认：~/.codex/skills（推荐，三家通用）
./scripts/install.sh --replace       # 遇到同名实体目录时：先改名备份再换链接（默认跳过）
./scripts/install.sh --cursor        # 额外装 ~/.cursor/skills（一般不需要）
./scripts/install.sh --dsh           # 额外装 DSH 原生根（一般不需要）
./scripts/install.sh --project PATH  # 装进某个项目 + 生成 AGENTS.md/.cursor 规则
./scripts/install.sh --copy          # 用拷贝代替符号链接（**装 DSH 时必加**）
./scripts/install.sh --uninstall     # 只删本脚本建的链接，绝不删实体目录
```

## 验证

```bash
# 入口行数（应为 ~110）
wc -l skills/workflowproject-kit/SKILL.md

# 仓库自检（shell 语法 / SKILL.md 引用完整性 / 7 个 frontmatter / Cursor 清单）
./scripts/self_check.sh

# Cursor 插件清单是否合规（坏了 Cursor 只会静默不显示）
python3 scripts/check_plugin_manifests.py .

# 对任意项目跑门禁校验
python3 skills/workflowproject-kit/scripts/check_gates.py /path/to/project
python3 skills/workflowproject-kit/scripts/check_gates.py --audit /path/to/project   # 找出没证据的门禁（死规则）

# 引用完整性：SKILL.md 提到的路径都存在
grep -o '](\([^)]*\.md\))' skills/workflowproject-kit/SKILL.md
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

**为什么新布局天然合规**：入口 `SKILL.md` 在 `skills/workflowproject-kit/` 里，
仓库根**没有**根 `SKILL.md`，`skills/` 就是标准技能目录 —— Codex 的 `<名字>/SKILL.md`、
DSH 的"只认直属子目录"、Cursor 的 `skills/` 自动发现，三者的规则同时命中。
清单里 7 个条目的 `source` 各自指向 `skills/<kit>`（不再有 `source: "."` 那种"整包当一个 skill"的形态）。

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
| Cursor 插件清单 | ✅ 7 个插件条目，`source = skills/<kit>`，路径存在 / kebab-case |
| `check_plugin_manifests.py` | ✅ 两个用例：正常通过；注入 3 个破坏（坏 name / 路径不存在 / 缺 SKILL.md）→ **全部抓到，退出码 1** |

## 处理那份重复的 `product-manager-kit`

`~/.codex/skills/product-manager-kit`（59 文件 / 6,975 行）与本仓库的
`skills/product-manager-kit`（64 文件 / 7,913 行）**是两份不同的打包**：

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

# ② 换成仓库里那一份（DSH 侧必须拷贝；只要 Codex/Cursor 用，链接也可以）
./scripts/install.sh --copy

# ③ 确认
ls -la ~/.codex/skills/
```

> `--copy` 会把 7 个 skill 都覆盖成仓库里的版本（只覆盖同名文件，不删多余文件）。
