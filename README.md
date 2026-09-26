# JQ Product Agent

面向掌握业务、但不一定有产品经理经验的使用者，帮助其将新系统、存量迭代或小需求逐步形成可审阅的产品定义、可操作 Demo、PRD 与设计/研发交接。当前主分支为 **v1.0.4 候选更新**；`v1.0.0` 仍是首个公开基线。版本号不代表真实项目的产出效果已经验证。

本仓库可作为独立 Codex Marketplace 使用，首期可在 Codex 下运行。它包含一个 `tc-product-agent` Plugin，安装后提供产品主 Skill、A–F 六个阶段 Skill、Demo 质量 Skill、候选专家内核，以及默认集成的 UI/UX Pro Max 和 Impeccable，共十一项 Skill。内部安装标识仍为 `tc-product-agent`，以保持旧版兼容；可选 Subagent 配置不自动启用。

## 安装

克隆仓库并进入目录：

```bash
git clone https://github.com/junqicheng765-oss/jq-product-agent.git
cd jq-product-agent
```

注册 Marketplace 并安装 Plugin：

```bash
codex plugin marketplace add "$(pwd)"
codex plugin add tc-product-agent@tc-product-agent
```

安装完成后新建一个 Codex 任务，使新 Skill 被发现。输入 `$tc-product-agent`，或直接描述需要完成的产品设计任务。该 Agent 只应读取当前任务获授权的项目资料，不携带本仓库或其他项目的业务事实。

## 包内关系

- **Plugin**：推荐分发与安装入口，负责把能力完整装入 Codex。
- **Skill**：实际的方法、A–F 阶段产物模板、七大一级/48 项二级能力和审计标准。外部视觉 Skill 按需用于 Demo 阶段，不接管产品事实或业务判断。
- **Subagent 配置**：可选执行角色，位于 `plugins/tc-product-agent/optional/codex-subagent/`；不随 Plugin 自动启用，也不是使用 Skill 的前提。

## 默认交付

1. 问题与范围、整体方案、场景与结构的产品基线；
2. 代表性可操作 Demo、模块体验，以及产品给设计的交付物；
3. 根据已确认方案与 Demo 展开的 PRD，以及产品给研发和 QA 的交接包。

简单需求可以合并阶段审阅，复杂系统则按风险和依赖展开；模板不是六份必须创建的文件。最终视觉稿、生产代码、部署和实际外发均为条件动作，需要相应授权、工具和回传证据。

## 当前证据边界

v1.0.1 在 F 阶段增加最小交付一致性核对：断开的引用、关键需求缺少直接验收关联、交付材料版本过期。它复用现有映射和版本证据；关联不明确时报告无法判定，不冒充全自动审计，该检查已用一份真实交付包只读回归。v1.0.2 进一步要求 Demo 的全部用户可见内容采用最终用户使用产品的视角，不在界面中加入面向评审者的讲解或 Demo 标签。

v1.0.3 增加阶段衔接与下一步引导：说明已完成范围、推荐下一步、责任方和具体产出；需要人行动时给出业务判断重点及自然回复方式。已有授权且输入足够时连续推进，不要求反复回复“继续”；仅交付方案时可推荐后续验证或承接，但不扩大授权、不增加审批门，也不承诺不存在的后台执行。

v1.0.4 默认集成 `$jq-product-expert` 候选专家内核：复用 PM-DEFINE 的精炼判断方法，对齐既有能力 ID 和质量标尺，按疑点定位主因、做取舍及给出验收依据。主 Agent 仍负责流程与事实，关键风险、定义疑义及正式质量门回查包内正式条款；不需要额外安装全局专家 Skill，原有正式标准未改。

当前候选尚未完成独立项目的端到端行为试验，未创建 v1.0.4 标签或 Release。专家内核的实际判断质量、误报/漏报及成本收益，和下一步引导效果都仍待试用验证。v1.0.0 曾通过十项 Skill、Plugin、Marketplace 结构校验及隔离安装，两项外部 Skill 完成有限本地脚本检查。尚未获得产品岗/非产品岗效果验证或设计/研发接收测试。

专家内核的打包完整性与负向测试可在 `plugins/tc-product-agent/` 内运行：`node scripts/validate-expert-kernel.mjs` 和 `node --test scripts/tests/expert-kernel.test.mjs`。这些只核对能力映射、引用和冻结标准，不证明大模型实际行为。

UI/UX Pro Max 的本地检索需要 Python 3，Impeccable 的本地脚本需要 Node.js。两者的固定上游版本、改动、许可证和通知文本见 [第三方说明](plugins/tc-product-agent/third_party/README.md)。安装 Plugin 本身不运行上游安装器或下载引擎。

## 许可状态

JQ Product Agent 自有内容目前未附开源许可证。公开可见不等于授权复制、修改或再分发；若要允许其他人二次开发或再分发，需要另行确定其许可证。随包第三方内容分别遵循其自带的 MIT 与 Apache-2.0 许可证。
