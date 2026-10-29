# JQ Product Agent

面向掌握业务、但不一定有产品经理经验的使用者，帮助其将新系统、存量迭代或小需求逐步形成可审阅的产品定义、可操作 Demo、PRD 与设计/研发交接。最新发布版本为 **[v1.1.2](https://github.com/junqicheng765-oss/jq-product-agent/releases/tag/v1.1.2)**，增强连续流程引导、关键决定确认、阶段产物核对与设计能力初始化；`v1.0.0` 是首个公开基线。发布和版本号不代表真实项目的产出效果已经验证。

本仓库可作为独立 Codex Marketplace 使用，首期可在 Codex 下运行。它包含一个 `tc-product-agent` Plugin，安装后提供产品主 Skill、A–F 六个阶段 Skill、Demo 质量 Skill、候选专家内核，以及默认集成的 UI/UX Pro Max 和 Impeccable，共十一项 Skill。内部安装标识仍为 `tc-product-agent`，以保持旧版兼容；可选 Subagent 配置不自动启用。

## 安装

克隆仓库并进入目录：

```bash
git clone https://github.com/junqicheng765-oss/jq-product-agent.git
cd jq-product-agent
```

注册 Marketplace 并安装 Plugin：

```bash
codex plugin marketplace add https://github.com/junqicheng765-oss/jq-product-agent.git
codex plugin add tc-product-agent@tc-product-agent
```

安装完成后新建一个 Codex 任务，使新 Skill 被发现。输入 `$tc-product-agent`，或直接描述需要完成的产品设计任务。该 Agent 只应读取当前任务获授权的项目资料，不携带本仓库或其他项目的业务事实。

## 更新已安装版本

使用 GitHub 来源安装的用户，可刷新该 Marketplace 并安装最新插件：

```bash
codex plugin marketplace upgrade tc-product-agent
codex plugin add tc-product-agent@tc-product-agent
```

安装后核对版本为 `1.1.2`，再新建会话加载。若桌面端“＋”菜单仍未刷新，完全退出并重新打开 Codex。已经打开的会话不能据安装成功推定为已加载新规则。原先注册本地克隆来源的用户，应先在自己的克隆目录执行 `git pull --ff-only`，再运行插件安装命令；本地来源不会因 GitHub 更新而自动拉取。

## 包内关系

- **Plugin**：推荐分发与安装入口，负责把能力完整装入 Codex。
- **Skill**：实际的方法、A–F 阶段产物模板、七大一级/48 项二级能力和审计标准。外部视觉 Skill 按需用于 Demo 阶段，不接管产品事实或业务判断。
- **Subagent 配置**：可选执行角色，位于 `plugins/tc-product-agent/optional/codex-subagent/`；不随 Plugin 自动启用，也不是使用 Skill 的前提。

## 默认交付

完整产品设计（包括小需求和存量迭代）默认形成以下成果；资料维护、咨询/评审和明确的局部修改按本次约定终点交付，不自动重走全部阶段或探测设计工具。

1. 问题与范围、整体方案、场景与结构的产品基线；
2. 可操作流程原型、视觉方向与有样式 Demo，以及产品给设计的交付物；
3. 根据已确认方案和可见体验展开的 PRD，以及产品给研发和 QA 的交接包。

简单需求可以合并阶段审阅，复杂系统则按风险和依赖展开；模板不是六份必须创建的文件。最终视觉稿、生产代码、部署和实际外发均为条件动作，需要相应授权、工具和回传证据。

## 当前证据边界

v1.1.2 将连续导航和按需确认贯穿 A–F：阶段出口核对产物、覆盖、质量证据、决定依据和版本，复用有效决定，授权内常规工作连续执行。设计阶段先初始化并复用工具配置，绑定用户指定目标；存量迭代先取得有效现状参考，再按页面选择直接编辑或生成后精修。各路线保留视觉选择或有效沿用依据。规则见[流程导航与按需确认](plugins/tc-product-agent/skills/tc-product-agent/references/27-流程导航与按需确认.md)及[设计能力初始化与复用](plugins/tc-product-agent/skills/tc-product-agent/references/26-设计能力初始化与复用.md)。阶段检查是执行合同，不是自动审计器；本次完成结构、引用及既有完整性检查，实际执行效果需在新项目中验证。

v1.1.1 在首轮澄清和工具探测前区分本次任务；A/C 按需提供带依据与未知标记的候选场景卡，复用有效确认和稳定 ID，以真实业务生命周期或功能闭环展开用例；C/D/E 用“主骨架＋叠加约束”连接结构、代表页面与设计展开，AI 不等于固定聊天界面或视觉风格。既有设计系统、产品能力编号、质量门和文案/交互复核继续适用，不新增 Skill 或审批。阶段模板和设计任务包已同步；本次结构、引用与完整性测试不等于真实项目的执行或效果验证。详见 [更新记录](CHANGELOG.md)及[类型设计基线](plugins/tc-product-agent/skills/tc-product-agent/references/25-产品类型设计基线.md)。

v1.0.1 在 F 阶段增加最小交付一致性核对：断开的引用、关键需求缺少直接验收关联、交付材料版本过期。它复用现有映射和版本证据；关联不明确时报告无法判定，不冒充全自动审计，该检查已用一份真实交付包只读回归。v1.0.2 进一步要求 Demo 的全部用户可见内容采用最终用户使用产品的视角，不在界面中加入面向评审者的讲解或 Demo 标签。

v1.0.3 增加阶段衔接与下一步引导：说明已完成范围、推荐下一步、责任方和具体产出；需要人行动时给出业务判断重点及自然回复方式。已有授权且输入足够时连续推进，不要求反复回复“继续”；仅交付方案时可推荐后续验证或承接，但不扩大授权、不增加审批门，也不承诺不存在的后台执行。

v1.0.4 默认集成 `$jq-product-expert` 候选专家内核：复用 PM-DEFINE 的精炼判断方法，对齐既有能力 ID 和质量标尺，按疑点定位主因、做取舍及给出验收依据。主 Agent 仍负责流程与事实，关键风险、定义疑义及正式质量门回查包内正式条款；不需要额外安装全局专家 Skill，原有正式标准未改。

v1.0.4 以标签和 Release 固定分发版本，专家内核仍为候选。十一项 Skill 与 Plugin 结构校验、专家能力映射/引用/冻结标准检查，以及八项完整性测试通过；此前已从 GitHub 安装并核对本机 v1.0.4 插件内容一致。这些不是独立项目的端到端行为试验。专家内核的实际判断质量、误报/漏报及成本收益，和下一步引导效果都仍待试用验证。v1.0.0 曾通过十项 Skill、Plugin、Marketplace 结构校验及隔离安装，两项外部 Skill 完成有限本地脚本检查。尚未获得产品岗/非产品岗效果验证或设计/研发接收测试。

专家内核的打包完整性与负向测试可在 `plugins/tc-product-agent/` 内运行：`node scripts/validate-expert-kernel.mjs` 和 `node --test scripts/tests/expert-kernel.test.mjs`。这些只核对能力映射、引用和冻结标准，不证明大模型实际行为。

v1.0.5 将 Demo 复核固定为“制作完成 → 文案与交互复核 → 修正与复验 → 给人确认”，不要求使用者另行提醒。完整交付检查全部交付范围的用户可见产品文案及核心/关键风险交互；代表页面或链路只声明当前覆盖，后续变更回归受影响项。文案检查业务准确性、易懂性、术语一致性、操作结果和下一步提示；交互需实际核对输入、反馈、状态、异常、取消与返回。复用既有原型或评审记录，分别报告文案、交互状态及未覆盖项。只看布局、截图或主流程不能称整体通过；阻断/重大问题未关闭或关键交互缺动态证据时，不得称对应范围原型就绪。规则见 [Demo 文案与交互复核](plugins/tc-product-agent/skills/tc-product-agent/references/24-Demo文案与交互复核.md)。本次结构、引用及原有完整性测试通过，不代表真实 Demo 已专项审查或 Agent 行为已验证，也不承诺文案是唯一最优。未在本次发布中更新本机插件或执行独立项目试验。

v1.1.0 在项目启动时识别设计执行路线：Figma Agent、Figma MCP、Computer Use、目标权限与现有设计系统分别核对。C/D 先确定结构并走通代表性流程；E 先收敛模块行为，再对同一代表页面比较三套视觉方向，选定后展开页面/状态、精修并还原有样式 Demo。Figma 不适用时可走 Codex 视觉路线，并用本地视觉与操作证据交付；不把本地稿称作 Figma 设计。开发者模式链接、设计稿审阅和代码还原分别留证，不互相代替。Demo 复核补充了视图隐藏及键盘焦点连续性检查。详细变更见 [v1.1.0 记录](CHANGELOG.md)。

本项工作在项目空间曾分别完成限定页面的 Figma Agent 生成与图层精修，以及依据官方 MCP 设计上下文进行的首页 Demo 还原。v1.1.0 发布前另以隔离合成样本跑通 Codex 路线的流程原型、三方向预览、有样式 Demo 和浏览器交互回归。三方向到全范围页面的 Figma 串联路线不属于这次回归的实测结论；用户试用和设计/研发接收仍需按具体项目证据判断。

UI/UX Pro Max 的本地检索需要 Python 3，Impeccable 的本地脚本需要 Node.js。两者的固定上游版本、改动、许可证和通知文本见 [第三方说明](plugins/tc-product-agent/third_party/README.md)。安装 Plugin 本身不运行上游安装器或下载引擎。

## 许可状态

JQ Product Agent 自有内容目前未附开源许可证。公开可见不等于授权复制、修改或再分发；若要允许其他人二次开发或再分发，需要另行确定其许可证。随包第三方内容分别遵循其自带的 MIT 与 Apache-2.0 许可证。
