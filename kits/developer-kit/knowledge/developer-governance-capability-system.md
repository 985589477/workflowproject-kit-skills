# developer-kit 开发治理能力体系

## 定位

developer-kit 是面向 Codex、Cursor 等 AI 开发工具的协作治理体系。

它不负责替代 AI 的写代码能力，而是负责定义：

- AI 如何接手项目。
- AI 如何理解项目结构。
- AI 如何判断模块边界。
- AI 如何处理产品需求进入开发后的架构影响。
- AI 如何控制变更风险。
- AI 如何完成测试、文档和交付闭环。

## 核心原则

- 护栏优先，不做铁轨。
- 项目本地规则优先于通用规则。
- 小任务轻量执行，高风险任务先分析并确认。
- 模块边界优先于局部方便。
- 改代码必须考虑验证、文档和交付说明。

## 能力地图

| 编号 | 能力 | 说明 |
| --- | --- | --- |
| 01 | 需求入口治理 | 判断需求是否清楚、是否可进入开发 |
| 02 | 项目结构治理 | 建立和维护项目目录、文档、规范 |
| 03 | 模块边界治理 | 定义模块职责、不负责范围和对外能力 |
| 04 | 模块协作设计 | 定义模块之间调用、数据、状态和异常 |
| 05 | 新增模块判断 | 判断新需求是否需要新增模块 |
| 06 | 架构决策记录 | 记录关键设计选择和取舍 |
| 07 | 影响范围分析 | 判断改动影响哪些模块、页面、接口、数据 |
| 08 | 变更风险分级 | 按风险决定执行方式和确认节点 |
| 09 | 数据与状态治理 | 管理数据模型、状态归属和修改权限 |
| 10 | 实现执行工作流 | 稳定完成代码修改 |
| 11 | 测试与验收 | 明确如何验证完成 |
| 12 | 文档同步 | 保证代码、架构、接口和说明同步 |
| 13 | 代码评审 | 检查 bug、风险、边界和可维护性 |
| 14 | 交付说明 | 输出变更说明、测试结果和风险 |
| 15 | AI 协作复盘 | 记录失控点并反哺规则 |
| 16 | 权限与危险操作治理 | 管理高风险命令、文件和操作 |
| 17 | 环境与配置治理 | 管理依赖、env、启动、构建、部署 |
| 18 | 依赖与技术债治理 | 控制新依赖、临时方案和重构 |
| 19 | 观测与问题追踪治理 | 管理日志、错误、问题复现和线上故障 |
| 20 | 版本与发布治理 | 管理发布检查、回滚和上线观察 |
| 21 | 问题定位治理 | 管理报错、白屏、测试失败、性能异常和根因假设 |
| 22 | 数据/API/状态契约治理 | 管理字段、接口、状态归属、错误处理和兼容策略 |
| 23 | 安全与权限治理 | 管理登录、鉴权、角色权限、敏感数据和高风险操作 |
| 24 | 工作流协同编排 | 管理多个开发工作流之间的插入、回退和阶段流转 |

## 新项目启动检查

检查是否存在：

```text
README.md
AGENTS.md
.cursor/rules/
docs/
docs/architecture/
docs/development-standard.md
docs/quality-checklist.md
技术栈入口文件
测试命令
构建命令
环境变量说明
模块目录说明
```

缺失时，先建议补齐，不要直接进入开发堆代码。

## 已有项目接手检查

优先读取：

```text
README.md
AGENTS.md
.cursor/rules/
技术栈入口文件
docs/architecture/
docs/development-standard.md
主要源码目录
测试目录
最近变更记录
```

输出：

```text
项目技术栈
启动方式
测试方式
主要模块
缺失文档
潜在风险
建议补齐内容
```

## 产品需求进入开发后的处理流程

先判断：

- 需求是否清楚。
- 成功标准是否明确。
- 是否有不做范围。
- 是否属于已有模块。
- 是否需要新增模块。
- 是否涉及跨模块协作。
- 是否涉及数据结构变化。
- 是否涉及权限、支付、登录、配置、迁移等高风险区域。
- 是否需要产品确认。

推荐输出：

```text
需求开发简报
影响范围分析
模块变更建议
风险等级
待确认问题
```

## 模块边界标准

每个核心模块应说明：

```text
模块职责
不负责范围
对外能力
输入
输出
依赖模块
被调用方
关键数据结构
边界规则
常见变更点
风险
```

## 新增模块判断

适合新增模块：

- 出现新的稳定业务概念。
- 已有模块职责明显过载。
- 新能力有独立生命周期。
- 新能力会被多个地方复用。
- 新能力有独立数据模型。
- 新能力需要独立测试。

不适合新增模块：

- 只是一个小工具函数。
- 只是页面局部逻辑。
- 只是临时需求。
- 只是为了让文件看起来更整齐。
- 没有独立业务含义。

## 风险分级

| 等级 | 类型 | 执行方式 |
| --- | --- | --- |
| 低风险 | 文案、样式、小 bug、单文件小改 | 可直接执行，简短说明 |
| 中风险 | 单模块功能、局部接口、局部状态 | 先做影响分析，再执行 |
| 高风险 | 跨模块、数据结构、权限、登录、支付、核心流程 | 先给方案，等待确认 |
| 危险变更 | 删除数据、迁移、批量重构、生产配置、破坏性命令 | 必须人工确认 |

## 后续建设顺序

```text
1. project-bootstrap-workflow
2. project-understanding-workflow
3. requirement-to-architecture-workflow
4. module-boundary-analysis-workflow
5. change-risk-assessment-workflow
6. impact-analysis-workflow
7. implementation-workflow
8. testing-verification-workflow
9. documentation-sync-workflow
10. code-review-workflow
11. architecture-decision-record-workflow
12. dependency-and-tech-debt-workflow
13. environment-config-governance-workflow
14. release-and-rollback-workflow
15. ai-collaboration-retrospective-workflow
16. issue-diagnosis-workflow
17. data-api-contract-workflow
18. security-permission-workflow
19. workflow-orchestration-guide
```
