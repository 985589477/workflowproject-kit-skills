# Codex 使用说明

## 适合 Codex 的场景

Codex 更适合在项目目录中处理产品文档和协作材料，例如：

- 阅读已有需求文档。
- 生成或更新 PRD。
- 保存文档到 `docs/`。
- 对比多个产品文档。
- 同步需求、验收标准和版本规划。

## 推荐启动语句

```text
请使用 product-manager-kit 协助我处理这个产品任务：{任务}。

请先阅读：
1. product-manager-kit/START-HERE.md
2. product-manager-kit/usage-guide.md
3. product-manager-kit/workflows/product-manager/product-manager-workflow.md

请先输出当前阶段、任务判断、使用工作流、是否需要用户确认和下一步。
不要在需求分析完成前直接写 PRD。
```

## Codex 执行原则

- 先判断产品阶段，再选择工作流。
- 保存文件前先判断项目是否已有文档目录。
- 不把 AI 推断写成确定需求。
- 进入 PRD 前确认需求分析是否合格。
- PRD 后继续判断是否需要验收标准、功能规划和版本规划。
- 最终回复必须说明输出位置、待确认问题和下一步。

## 建议的 Codex 输出状态

```text
当前阶段：
任务判断：
使用工作流：
使用模板：
检查标准：
是否需要用户确认：
本轮会读取：
本轮可能保存：
下一步：
```

## 结束格式

```text
完成情况：
输出文档：
待确认问题：
评分或检查结果：
下一步建议：
```
