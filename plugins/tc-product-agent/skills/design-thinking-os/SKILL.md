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

## 开工前必读（硬性，任何工作模式都适用，包括“直接制作”）

本文件只是入口和索引。**只读本文件就开始做，视为没有开工。** 只要本轮要出界面、海报、图标、动效或任何视觉成品，动手前必须用 Read **逐个打开下面每一个文件的全文**，不是只打开某个小节，也不按「这个任务用不到」跳过。没读完不得写设计、不得出图。

1. [framework.md](framework.md)
2. [methods-intake.md](methods-intake.md)
3. [methods-context.md](methods-context.md)
4. [methods-routing.md](methods-routing.md)
5. [methods-dispatch.md](methods-dispatch.md)
6. [methods-execution.md](methods-execution.md)
7. [methods-flow.md](methods-flow.md)
8. [methods-interaction.md](methods-interaction.md)
9. [methods-ui.md](methods-ui.md)
10. [methods-visual.md](methods-visual.md)
11. [methods-color.md](methods-color.md)
12. [methods-style-engine.md](methods-style-engine.md)
13. [methods-motion.md](methods-motion.md)
14. [methods-prototype.md](methods-prototype.md)
15. [methods-research.md](methods-research.md)
16. [methods-competitive.md](methods-competitive.md)
17. [methods-tool-routing.md](methods-tool-routing.md)
18. [methods-close.md](methods-close.md)
19. [methods-resource-routing.md](methods-resource-routing.md)
20. [methods-image.md](methods-image.md)
21. [templates.md](templates.md)

交付的「已读细则」必须按这个顺序列出全部 21 个文件名。少一个就是没读完：先补读，再继续做。禁止用本文件里的摘要代替细则。

## 审查不通过必须改完再交

成品是用整套方法论做出来的，验收也用整套方法论验，不只看 UI 一层。终审从「为什么做」一直查到「像素准不准」，**每一层都对着最终成品检查**，不是对着当初的分析稿自评。几何脚本只覆盖 UI 层的对齐、分区碰撞和图标来源，不能代替其余各层。

**两条硬要求：**

- **本轮实际用过的每一个方法，都要拿它在细则里写的「完成证据」对照成品再验一遍**（例如用了 `F3 主路径`，就验「未参与项目的人能按成品走通、比现状少了哪一步」）。用过却没验 = 未终审。
- 下面每一层逐条写「过 / 不过 / 不适用（原因）」，并指出成品上的具体位置。任何一条「不过」，或脚本不是 `"passed": true`，都先改产出，再重新截图、重新跑脚本、重新逐层写。禁止把没过的稿交给用户，禁止用「后续可优化」代替修改。

**A. 问题与价值**（[methods-research.md](methods-research.md) `R1` `R7` `R8`；[methods-context.md](methods-context.md)）
1. 成品解决的是问题卡里那个用户、那个情境下的那件事，没有跑题去做别的。
2. 价值主张里的差异点，在成品上用户能直接看到或感受到。
3. 本轮最危险的假设，成品里有对应的设计回应；仍未验证的明确标为假设。

**B. 成功标准与体验损耗**（[methods-research.md](methods-research.md) `R8`；[methods-close.md](methods-close.md) `QA0` 维度一）
4. 关键行为在成品上能顺畅发生，路径上没有挡住它的东西。
5. 没有为了数据牺牲体验：没有打断主任务的弹窗、假倒计时、拒绝比接受更难点的设计。

**C. 流程**（[methods-flow.md](methods-flow.md) `F1` `F3` 与「流程评审」）
6. 只做了范围内的事，范围外的没有偷偷加进来。
7. 没参与项目的人能按成品把主路径走通；能说清比现状少了哪一步或哪种不确定。

**D. 交互**（[methods-interaction.md](methods-interaction.md) `I2` `I3` `I5` `I6`）
8. 一页一个主任务；同一对象全程同一个名字，进出和返回结果明确。
9. 主行动点下去，用户不用猜是否生效。
10. 主路径上每个阻断（失败、无权限、超时、没网）都有能执行的出口。

**E. UI**（[methods-ui.md](methods-ui.md) `U1`–`U7`）
11. 信息分级：这一屏先看的只有 1–2 件。
12. 单一主行动：2 秒能指出下一步；同一组只有一个实心强调；危险动作不和正常推进一样抢。
13. 对比：眯眼先看到对象、关键判断和主行动。
14. 亲密：相关的靠近、无关的分开；同一状态只在一处反馈。
15. 对齐：先分区再摆元素，分区不重叠、横排条垂直居中；HTML 跑 `python3 scripts/ui_geometry_audit.py <html文件>` 且 `"passed": true`。
16. 重复：同类对象同一套结构和样式。
17. 组件：控件是为完成任务选的，不多一种像按钮的东西。
18. 对象表现形式与尺寸分级：用户认得的对象按它自己的视觉惯例表现，不用它的名字代替它；按最小实际尺寸截图，同类对象仍能一眼区分。
19. 状态：空、失败、加载、禁用、超长内容里用得上的都有下一步。
20. 文案：标题是对象或任务，按钮是动词加对象，没有脱离上下文的「确定 / 提交 / 出错了」。

**F. 视觉**（[methods-visual.md](methods-visual.md)「视觉规格通过门」；[methods-close.md](methods-close.md) `QA0` 维度二、三）
21. 颜色是产品级语义色（背景、文字、按钮、边框、状态、亮暗），与所选风格一致；`python3 scripts/color_intelligence.py contrast --preset <id>` 通过。圆角、阴影、字体与风格参数一致；色彩比例协调、冷暖同频，不脏不俗。多页面产品跑 `python3 scripts/style_consistency_audit.py <所有页面> --preset <预设>` 且 `"passed": true`：没有色板外的颜色、阶梯外的圆角、字体栈外的字体，同类组件跨页一致。
22. 有留白和唯一视觉重心，没有卡片套卡片、满屏同样抢眼。
23. 材质语言覆盖每一个组件：找出全屏做得最弱的元素，它也达到风格参数；图标、3D、插画是成品素材且同一套系；真实世界配图来自 Real Image Library 且有授权记录；人物形象过了文化风格判断。

**G. 动效**（只在本轮有动效时；[methods-motion.md](methods-motion.md)「动态验收与性能完成门」）
24. 动效表达的是反馈、状态变化或空间关系，不是装饰；真实环境下流畅，可打断。

**H. 验证与下一步**（[methods-close.md](methods-close.md) 对应工作模式收口）
25. 写清哪些已被证据支持、哪些仍是假设，以及用什么最小测试去验证；不把「做完了」写成「已验证」。axe-core 的严重问题已清零，或写明未跑及原因。用户确认可复用的方案已按 `AM` 询问是否入库（未确认不入库）。

## 运行顺序

上面 21 个文件在动手前已经全部读完。下面是读完之后的执行顺序，不是再挑哪些文件要读。

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
- [methods-intake.md](methods-intake.md)：任务分诊、工作模式判断与问人条件。
- [methods-dispatch.md](methods-dispatch.md)：按决定缺口组装最小方法工作包。
- [methods-context.md](methods-context.md)：将产品用户、问题、行业和约束翻译成设计语境、任务与原则。
- [methods-competitive.md](methods-competitive.md)：分别分析行业竞品、同类操作竞品和服务同类用户的竞品。
- [methods-routing.md](methods-routing.md)：确定本轮终点、产出合同、决定工作集、依赖和证据计划。
- [methods-tool-routing.md](methods-tool-routing.md)：按最终产物选择 Figma、视觉和动效工具并定义交接。
- [methods-execution.md](methods-execution.md)：执行方法、传递产物、控制停止与重路由。
- [methods-research.md](methods-research.md)：问题、用户、情境、证据、价值。
- [methods-flow.md](methods-flow.md)：范围、场景、任务路径。
- [methods-interaction.md](methods-interaction.md)：页面职责、反馈、异常。
- [methods-ui.md](methods-ui.md)：信息层级、组件、状态、文案。
- [methods-visual.md](methods-visual.md)：Figma UI 内的全部界面视觉依据、26+6 风格参数字典（国际化 8 + 国内 8 + 游戏 10 + 通用质感 6）、色字图与候选；融合 IconScout 官方 MCP（`https://mcp.iconscout.com/mcp`）与内置 v3 API 兜底脚本 [scripts/iconscout.py](scripts/iconscout.py)（`Client-ID: 232598791050530`）用于拉取统一风格的 `icon / 3d / lottie / illustration`；真实世界摄影走 [methods-image.md](methods-image.md)，不是 IconScout，也不是先 AI 生图；只有非界面视觉成品或明确独立资产委托才另走视觉工具。
- [methods-color.md](methods-color.md)：配色智能。现成色板只作灵感（Coolors / Color Hunt / Huemint 不抓取、不调非商用 API）；产品级语义色从本地 5 套系统和 Radix 12 阶生成；品牌色本地插值；预览 3 套后写入 token，并跑对比度检查。
- [methods-style-engine.md](methods-style-engine.md)：设计风格引擎。识别现状，探索和应用分开；从本地预设库 [style-presets/](style-presets/registry.json) 提取规格（Apple、Material 3、Ant Design 三套系统，26 种内置风格，42 个 Tweakcn 主题，12 个风格族），按技术栈做组件映射，批量应用到整个产品，用 [scripts/style_consistency_audit.py](scripts/style_consistency_audit.py) 验收跨页一致性；本地缺的再去线上库补并沉淀。
- [methods-motion.md](methods-motion.md)：UI 反馈、状态转换、空间关系；`MI` 从 React Bits / Aceternity UI / Motion Primitives / Uiverse / 21st.dev 检索动效源码并集成；视频/动态图形和格式特定动画按工具路由执行。
- [methods-prototype.md](methods-prototype.md)：把概念、内容或交互方案准备成可测试版本。
- [methods-close.md](methods-close.md)：按工作模式验收，内置 `QA0`（用户可用性 × 审美与品位 × 设计标准）三大维度审查与 [scripts/ui_geometry_audit.py](scripts/ui_geometry_audit.py) 自动 DOM 几何/对齐/碰撞/头像质检门。
- [methods-resource-routing.md](methods-resource-routing.md)：资源路由。不新增设计方法；按 adapter 调用真实案例、字体、组件、验收工具。先搜内部 `asset-memory`，再本地预设，再自动接口，再已授权 MCP，最后才是参考链接。含参考智能（RR）、排版（TY）、验证引擎（VE）、资产记忆（AM）。真实摄影接到 `IM`。
- [methods-image.md](methods-image.md)：真实摄影素材库。统一 `Image Search Adapter`（Pixabay + Openverse 为主，Unsplash 已预置 Access Key / Pexels / Wikimedia 补充）。真实场景、人物生活、建筑、自然、地点先搜真图；找不到或必须虚构才 AI 生图。
- [templates.md](templates.md)：诊断、工作包和产出模板。
- [walkthrough.md](walkthrough.md)：典型路由回验。

每个方法都必须遵守自己的：触发问题、最低输入、跳过条件、步骤、产出、完成证据、不得替代项。

## 问人规则

默认不问，直接做。设计师能自己拍板的专业判断（风格、配色、组件库、密度、圆角、字体、图标、素材、版式、首帧、是否先做代表页）一律由 Agent 决定并直接产出。

**固定要问的例外**：做海报 / 运营图 / 主视觉 KV 走 AI 生图时，必须把 2–3 张风格参考图并排展示给用户挑 1 张（用户已给参考图时除外）；只问“挑哪张”，垫法和主色由 Agent 定。海报 / 运营图 / 单图交付静态版后，若投放场景支持动图，必须用提问工具问用户要不要动态版并说明效果预期（用户原话已要求动图时直接做）。用户要求探索风格或给已有产品换风格时，用同一个代表页渲染 3 个不同方向并排给用户挑；**批量改已有产品的代码前**，必须给出代表页改前改后对比和要改的文件范围，让用户确认一次（0→1 新建不需要）。见 [methods-style-engine.md](methods-style-engine.md) `DS1`。用户要求看看配色、或品牌色有多种合理映射时，用 [methods-color.md](methods-color.md) `CI2` 出 3 套语义色预览再问一次。

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
  - 通用素材缺失时不停、不问。**图标、3D、徽章、插画、虚构角色头像**先从 IconScout 找，库里没有或风格不匹配再按统一风格 AI 生成。**真实世界的场景、人物生活、建筑、自然风景、具体地点**先按 [methods-image.md](methods-image.md) 检索真实摄影；找不到合适图、或画面必须虚构，才 AI 生图。两种情况都不得用占位图、Emoji 或手画简笔替代。
- **图标、3D 图标、插画、Lottie 动效一律先去 IconScout 拿现成专业素材**（它同时有线性/面性图标、3D、插画和 Lottie 动画），同一屏用同一套系。不要自己手写 SVG 路径、用 CSS/Canvas 拼图形或让模型临时画简陋图标、简陋动画。返回、设置、关闭这类功能按钮里的图标也算，必须放下载好的成品 SVG 文件，禁止为了「按钮里要有 SVG」而手写一个齿轮或箭头。IconScout 确实没有合适的才退一步：图标用成熟开源图标库的同风格整套，3D/插画按统一风格 AI 生成，动效用现成素材改色或在专业素材基础上加动画；只有品牌专属图形才自制，且必须达到同套图标的网格、线宽和精致度。
- **真实摄影走 Real Image Library，不先 AI 生图**：Hero、卡片配图、氛围背景、地标只要表现真实世界，就运行 `python3 scripts/real_image.py search "<主题>" --role hero|card|background|place --tone <冷暖>`。Unsplash 已预置 Access Key，开箱即用。主库 Pixabay（有 key 才开）+ Openverse + Unsplash；Pexels 有 key 才开；具体地点优先 Wikimedia。选定后 `get` 到本地并留下作者与许可证。没搜过真实图库，不得把「写实摄影」直接交给生图模型。用户头像圈仍走 IconScout 文化门，不拿图库随机真人脸当头像。
- **对象按它自己的样子表现，缩小也要认得出**：界面里出现用户在现实或该领域里认得的对象时，先找出用户靠什么认出它，按它本来的视觉惯例表现。不能用它的名字代替它本身。显示尺寸放不下完整形态时，用这个领域已有的缩略方式保留识别特征，而不是退成写字。方法见 [methods-ui.md](methods-ui.md) `U7`。
- **风格的材质要做到每一个组件上**：按钮、标签、面板、图标、输入框都要达到所选风格的工艺，不能只做背景和主视觉。检查时找全屏最弱的那个元素。方法见 [methods-visual.md](methods-visual.md) `V0` Step 3 末尾「贯穿 6 维的硬要求」。
- **先用内部已验收资产，再调用外部库**：动手前 `python3 scripts/asset_memory.py search <场景>`。外部资源必须走 [methods-resource-routing.md](methods-resource-routing.md) 的 adapter（怎么搜、返回什么、怎么用、许可证、失败怎么办）。没有公开接口的（Page Flows、部分灵感站）只给链接，不抓取、不假装能自动安装。Mobbin 有付费套餐时再发起 MCP 授权；没有就当参考库。
- **字体按风格族和语言自动选型**：`python3 scripts/typography_intelligence.py pick --family <风格族> --langs zh,en`。中日韩正文必须带 CJK 字体，不能只用 Inter。
- **验收要跑可执行检查**：几何、对比度、跨页风格之外，再跑 `python3 scripts/a11y_audit.py <页面>`（axe-core）。有 Chromatic token 才做视觉回归，没有就并排截图，不写「已做视觉回归」。
- **配色必须是产品级语义色，不是几个好看的色块**：风格定了之后，按 [methods-color.md](methods-color.md) 从 `color-presets/` 取一套含背景、文字、按钮、边框、状态色和亮暗模式的系统（默认 5 套 + Radix 12 阶）。用户给了品牌色用 `from-brand`；用户从 Coolors / Color Hunt / Huemint 粘贴的色板用 `from-palette` 转成语义色。禁止抓取这些灵感站，禁止调用 Huemint API。写入后跑 `color_intelligence.py contrast`。
- **风格定了就整套用，先本地后线上**：选定风格后，按 [methods-style-engine.md](methods-style-engine.md) 从 `style-presets/` 取出整套规格（颜色、字体、圆角、间距、导航、卡片、交互、动效）以及绑定的设计系统、页面区块库和动效库；本地缺的再去线上库补。全产品只在一处定义 token，组件和页面都引用它，不逐页手调。改完跑风格一致性脚本。
- **写成代码的动效先去组件库找源码**：先写清这条动效要解决什么、怎么触发、起止状态和时长，再按 [methods-motion.md](methods-motion.md) `MI` 去 React Bits、Aceternity UI、Motion Primitives、Uiverse、21st.dev 检索。合适的审过源码后直接拿来，改成规格数值和设计 token，并记录来源与许可证；没有合适的再用项目已有引擎自写。不用付费组件，不运行未审的安装命令，不编造来源。
- **IconScout 素材服务（MCP）没装就直接装**：Agent 自己跑安装命令或在配置里追加，并发起浏览器登录，只告诉用户“点一下授权”；不询问、不只给提示。本轮未生效前先用内置脚本 `scripts/iconscout.py`（见 [methods-visual.md](methods-visual.md) `V5` 第 6 条）。
- **工具不可用时换载体，不停工**：有 Figma 且项目以 Figma 为主稿时在 Figma 做；Figma 未连接、或用户要快速看效果/可操作 Demo 时，直接用 HTML/代码按同一套风格参数出界面，并跑 `scripts/ui_geometry_audit.py` 验收。只有用户明确要求必须交 Figma 文件而 Figma 不可用时，才说明情况。
- **“已批准/已确认”的含义**：用户已认可的稿，或 Agent 本轮产出并通过自检的稿，都可以作为下游（视觉、动效、生视频）的冻结输入；不需要单独等用户点头。用户委托做设计即视为允许 Agent 在平台规范、设计系统或风格库范围内探索具体数值。
- 必须问时，问题和选项要用用户一眼能懂的大白话，严禁出现本 Skill 的内部术语（风格编号、六维/6 维参数、参数组合、决策漏斗、token、`V0`、`D1–D9`、`U0`、`QA0` 等）和第三方品牌/产品点名。品牌/产品名只禁止出现在给用户看的文字里；发给生图模型或 Figma 的提示词照常保留，不要删。

## 对用户的默认交付

```markdown
# 任务诊断
- 已读细则（必须是上面 21 个文件的全名，少一个即未读完）：
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
- 交付前终审（按上文「审查不通过必须改完再交」A–H 共 25 条，每条写过 / 不过 / 不适用 + 成品位置；有不过或脚本未通过 = 先改再交）：
  - 本轮用过的方法及各自「完成证据」对照成品的结果：
  - A 问题与价值（1–3）：
  - B 成功标准与体验损耗（4–5）：
  - C 流程（6–7）：
  - D 交互（8–10）：
  - E UI（11–20，含几何脚本 passed）：
  - F 视觉（21–23，多页面含风格一致性脚本 passed）：
  - G 动效（24）：
  - H 验证与下一步（25）：
  - 本轮终审改掉的问题：
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

嵌入任何上游 Product Agent（如 `jq-product-agent`）时，本 Skill 是设计方法论与执行决策子流程，不替换上游的产品阶段（`A–F`）、唯一事实源、授权和业务决策；本文件内的 `D1–D9` 仅指「内部设计决定链」，不替代上游的 `D 阶段` 或设计就绪门。主 Agent 与阶段 Skill 按需调用本 Skill 完成设计语境翻译、UI 三路分流（`U0/V0`）、26+6 风格参数字典绑定、IconScout 双通道资产调取、真实摄影库（`IM`）、双路径生图（`V7`）、三条动效实现链路（`TR5`）及交付前 `QA0`（用户可用性 × 审美与品位 × 设计标准）综合验收与回炉修改。
