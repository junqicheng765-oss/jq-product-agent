---
name: design-thinking-os
description: >-
  Triages any product-design request, identifies the earliest unresolved
  design decision that can materially change the requested output, and calls
  only the necessary research, flow, interaction, UI, visual, motion, or
  validation methods. Use for design execution, optimization, exploration,
  prototype validation, Figma restoration, landing pages, flows, screens,
  redesigns, UI, visual, or motion work.
---

# 设计任务工作流

模拟设计师接到上游任务后的真实工作：先理解产品输入并翻译成设计可使用的语境，再判断需要直接做、分析、调研、设计或验证。方法库不是固定阶段；只有当前决定需要它时才调用。

## 核心规则

> 从「会实质改变本轮产出」的最早未解决决定开始；已确认、冻结、与本轮无关的上游不重做。

决定链回答“现在缺哪个设计决定”；设计语境回答“用户、任务、行业和环境要求这个决定怎样解决”。两者缺一不可。

因此：

- 输入完整、范围局部、风险低：直接制作。
- 问题位置已知但解法未定：从对应设计决定开始。
- 谁用、为何用、怎样算成功不清楚：从问题探索开始。
- 方案已有但不确定是否成立：从验证开始。
- 有准确设计主稿、任务是还原：按主稿制作并做一致性验收，不擅自重设计。

禁止把所有任务强制跑成「用研→流程→交互→UI」；也禁止因用户说了“页面/UI/提升”就直接进入该方法。

## 运行顺序

1. **读取总框架**：Read [framework.md](framework.md)，明确与上游产品流程的边界、输入和回传。
2. **任务分诊与语境翻译**：Read [methods-intake.md](methods-intake.md)；需要设计判断时再 Read [methods-context.md](methods-context.md)，形成上游任务卡、设计语境卡、设计任务定义、任务诊断卡和设计决定链。
3. **确定终点与工作集**：Read [methods-routing.md](methods-routing.md)，先定产出合同、目标决定、必要依赖，再分别建立决定工作、制作动作、证据动作，确定最终设计起点和风险深度。
4. **组装工作包**：Read [methods-dispatch.md](methods-dispatch.md)，按“决定缺口 × 语境要求”选择最小方法组合。
5. **选择产物工具**：Read [methods-tool-routing.md](methods-tool-routing.md)，按最终产物选择 Figma、视觉或动效工具；不按阶段把工具全部调用。
6. **执行路线**：Read [methods-execution.md](methods-execution.md)，逐项执行决定、制作和证据动作，再按工作包读取对应方法文件；`CORE_EVIDENCE` 随研究/测试执行，制作动作按合同执行，成品冻结后再执行 `POST_ARTIFACT_ACCEPTANCE`；`DEFERRED_NEXT_ROUTE` 本轮只准备条件，不得写已验证。
7. **收口与回传**：Read [methods-close.md](methods-close.md)，汇总各证据动作、更新决定状态，并将新证据、风险和待决策项交回上游。

## 设计决定链

按顺序扫描，但不等于每次都执行：

```
D1 问题与价值
→ D2 用户与情境
→ D3 用户/产品结果与成功指标
→ D4 任务流程
→ D5 交互规则、语义反馈与状态
→ D6 UI 信息层级与内容
→ D7 界面视觉系统与资产
→ D8 UI 动效表达
→ D9 验收或验证程序
```

每项只能标：

- `CONFIRMED`：有有效来源，且本轮可复用。
- `FROZEN`：用户明确要求不重开；记录风险但服从范围。
- `TEST_INPUT`：当前方案或假设是本轮测试对象；测试前暂不重开，但不代表已证实。
- `ASSUMPTION`：已有暂定答案；必须写若错影响，并标 `RESOLVE_NOW` 或 `ACCEPT_FOR_NOW`。
- `MISSING`：本轮需要解决，且可通过设计工作补齐。
- `BLOCKED`：必须等待外部事实、只有用户方才有的素材、权限或授权；受影响工作不能继续。通用素材缺失、Figma 未连接、无正式基线都不算 `BLOCKED`（见「问人规则」）。
- `N/A`：本任务不适用。

起点是最早一个同时满足「`MISSING` 或 `ASSUMPTION/RESOLVE_NOW`」和「答案不同会改变本轮产出」的决定。`ASSUMPTION/ACCEPT_FOR_NOW` 不在同一工作包内反复触发；它进入风险和后续验证。遇到会阻断产出的 `BLOCKED` 时停止受影响部分并向责任人取输入。`TEST_INPUT` 在方案验证任务中不触发回溯：先测当前版本，结果再决定状态转换和回到哪一项。

## 工作模式

- **直接制作**：确切修改、有效来源、上游不受影响、验收标准明确。
- **局部优化**：问题位置已知；只在受影响决定内诊断与设计。
- **问题探索**：问题、用户、价值或成功判断不清。
- **方案验证**：方案已存在；标“验证准备”时只准备测试就绪载体和延期合同，标“验证执行”时实际取得理解、可用、可信或价值证据。
- **设计还原/交付**：依据既有主稿、规范或版本做还原与交接。

## 方法文件

- [framework.md](framework.md)：设计师从接收上游任务到交付回传的总框架。
- [methods-context.md](methods-context.md)：将产品用户、问题、行业和约束翻译成设计语境、任务与原则。
- [methods-competitive.md](methods-competitive.md)：分别分析行业竞品、同类操作竞品和服务同类用户的竞品。
- [methods-routing.md](methods-routing.md)：确定本轮终点、产出合同、决定工作集、依赖和证据计划。
- [methods-tool-routing.md](methods-tool-routing.md)：按最终产物选择 Figma、视觉和动效工具并定义交接。
- [methods-execution.md](methods-execution.md)：执行方法、传递产物、控制停止与重路由。
- [methods-research.md](methods-research.md)：问题、用户、情境、证据、价值。
- [methods-flow.md](methods-flow.md)：范围、场景、任务路径。
- [methods-interaction.md](methods-interaction.md)：页面职责、反馈、异常。
- [methods-ui.md](methods-ui.md)：信息层级、组件、状态、文案。
- [methods-visual.md](methods-visual.md)：Figma UI 内的全部界面视觉依据、26+6 风格参数字典（国际化 8 + 国内 8 + 游戏 10 + 通用质感 6）、色字图与候选；融合 IconScout 官方 MCP（`https://mcp.iconscout.com/mcp`）与内置 v3 API 兜底脚本 [scripts/iconscout.py](scripts/iconscout.py)（`Client-ID: 232598791050530`）用于拉取统一风格的 `icon / 3d / lottie / illustration`；只有非界面视觉成品或明确独立资产委托才另走视觉工具。
- [methods-motion.md](methods-motion.md)：UI 反馈、状态转换、空间关系；视频/动态图形和格式特定动画按工具路由执行。
- [methods-prototype.md](methods-prototype.md)：把概念、内容或交互方案准备成可测试版本。
- [methods-close.md](methods-close.md)：按工作模式验收，内置 `QA0`（用户可用性 × 审美与品位 × 设计标准）三大维度审查与 [scripts/ui_geometry_audit.py](scripts/ui_geometry_audit.py) 自动 DOM 几何/对齐/碰撞/头像质检门。
- [templates.md](templates.md)：诊断、工作包和产出模板。
- [walkthrough.md](walkthrough.md)：典型路由回验。

每个方法都必须遵守自己的：触发问题、最低输入、跳过条件、步骤、产出、完成证据、不得替代项。

## 问人规则

默认不问，直接做。设计师能自己拍板的专业判断（风格、配色、组件库、密度、圆角、字体、图标、素材、参考图、版式、首帧、是否先做代表页）一律由 Agent 决定并直接产出。

- 只有以下三种情况才问：
  1. 缺了就无法开工的事实（例如不知道要做什么、给谁用、在哪投放），且无法从上下文合理推断；
  2. 会花钱、对外发布、覆盖或删除正式文件等不可逆或高成本动作；
  3. 存在两条同样合理、结果差异很大的方向，且语境完全无法判断。
- 需要问时，一轮最多合并成 1 个问题，选项 2–3 个，首项是推荐项；不分多轮追问，不逐项确认细节。
- 其余缺口用 `ASSUMPTION:` 按最合理的默认继续，交付时用一句话说明做了哪些选择、想改可以说。
- 不为“走流程”停下来等批准：做完一页可直接铺开，生成完一张可直接继续；用户随时可以叫停或改。
- 0→1 没有品牌规范时，风格库参数和组件库默认值就是依据，Agent 直接采用并标注“可替换为品牌色/品牌字体”，不因此停下来要输入。
- 已有有效答案不重问；用户明确冻结上游时，不擅自重开。
- **素材缺失分两类处理**：
  - 只有用户方才有的素材（品牌 Logo、真实产品图、真实人物照片、真实数据与文案、授权字体、已有设计稿文件）缺失时，才算“缺了就无法开工”，向用户要；其余部分照常推进。
  - 通用素材（图标、3D 图标与道具、徽章、插画、背景、氛围图、虚构角色头像）缺失时不停、不问：先从 IconScout 找，库里没有或风格不匹配就按统一风格 AI 生成。两种情况都不得用占位图、Emoji 或手画简笔替代。
- **工具不可用时换载体，不停工**：有 Figma 且项目以 Figma 为主稿时在 Figma 做；Figma 未连接、或用户要快速看效果/可操作 Demo 时，直接用 HTML/代码按同一套风格参数出界面，并跑 `scripts/ui_geometry_audit.py` 验收。只有用户明确要求必须交 Figma 文件而 Figma 不可用时，才说明情况。
- **“已批准/已确认”的含义**：用户已认可的稿，或 Agent 本轮产出并通过自检的稿，都可以作为下游（视觉、动效、生视频）的冻结输入；不需要单独等用户点头。用户委托做设计即视为允许 Agent 在平台规范、设计系统或风格库范围内探索具体数值。
- 必须问时，问题和选项要用用户一眼能懂的大白话，严禁出现本 Skill 的内部术语（风格编号、六维/6 维参数、参数组合、决策漏斗、token、`V0`、`D1–D9`、`U0`、`QA0` 等）和第三方品牌/产品点名。

## 对用户的默认交付

```markdown
# 任务诊断
- 工作模式：
- 本轮目标：
- 主终点与产出合同：
- 候选起点 / 最终设计起点：
- 上游复用依据：
- 设计语境与关键推导（需要设计判断时）：
- 设计原则与关键矛盾（需要设计判断时）：
- 决定工作 / 制作动作 / 证据动作：
- 风险深度：
- 选用方法及理由：
- 产物工具、职责边界及交接：
- 明确跳过及理由：
- 产出物：
- 完成证据：
- 未知 / 假设 / 风险：

# 设计结果
（只交本轮工作包内的产出）

# 上游回传
- 受影响决定及前后状态：
- 证据动作 ID、动作状态、外部执行状态和 D9-PLAN 版本：
- 证据对象版本、场次或检查记录 ID、情境与适用范围：
- 被支持或推翻的产品/设计假设：
- 需要上游决定的事项及责任人：
- 下一路由节点：
```

嵌入任何上游 Product Agent（如 `jq-product-agent`）时，本 Skill 是设计方法论与执行决策子流程，不替换上游的产品阶段（`A–F`）、唯一事实源、授权和业务决策；本文件内的 `D1–D9` 仅指「内部设计决定链」，不替代上游的 `D 阶段` 或设计就绪门。主 Agent 与阶段 Skill 按需调用本 Skill 完成设计语境翻译、UI 三路分流（`U0/V0`）、26+6 风格参数字典绑定、IconScout 双通道资产调取、双路径生图（`V7`）、三条动效实现链路（`TR5`）及交付前 `QA0`（用户可用性 × 审美与品位 × 设计标准）综合验收与回炉修改。
