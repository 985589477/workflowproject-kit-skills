# Ponytail 最小必要变更原则

## 来源

- 项目：Ponytail
- 仓库：`https://github.com/DietrichGebert/ponytail`
- 许可证：MIT
- 本文件用途：作为 WorkflowProject `developer-kit` 的外部思想来源和融合记录。

## 核心启发

Ponytail 的核心不是简单压缩 token，而是改变 AI 编程行为：

- 少写不必要代码。
- 优先复用已有代码。
- 优先使用平台、标准库和已有依赖。
- 不为未来想象出来的需求增加抽象。
- 在保证完整性、安全性和验证的前提下做最小改动。

## 融合到 WorkflowProject 的方式

在本项目中，Ponytail 被融合为：

- `02-roles/developer/minimal-change-guardian.md`
- `04-workflows/developer/minimal-change-governance-workflow.md`
- `06-templates/developer/minimal-change-governance-template.md`
- `11-evaluations/output-scorecards/minimal-change-governance-scorecard.md`

## 本地化原则

### 最小不是随便

最小变更必须先理解影响范围，不能没读代码就压缩方案。

### 少写不是少验证

涉及分支、循环、解析、钱、安全、权限、数据损坏风险或新脚本时，必须保留测试或自检。

### 复用优先

优先顺序：

```text
不做 -> 复用项目已有能力 -> 平台/标准库 -> 已安装依赖 -> 清晰一行 -> 最小新增代码
```

### 不削减底线

不得削减：

- 安全和权限。
- 信任边界校验。
- 防止数据丢失的错误处理。
- 可访问性。
- 用户明确要求。
- 必要测试。

