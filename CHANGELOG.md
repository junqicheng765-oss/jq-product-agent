# JQ Product Agent v1.0.4

发布日期：2026-09-27。首期可在 Codex 下运行；安装标识仍为 `tc-product-agent`。

## 相对 v1.0.0 的更新

- 集成候选产品专家内核 `jq-product-expert`：适配 PM-DEFINE 的精炼方法，沿用包内能力 ID 和质量标尺，按问题给出主因、取舍、修正与验收依据。
- 专家方法按需加载，关键规则、权限、不可逆损失、结果未知、定义疑义及正式质量门回查对应正式条款；正式模型和源文档未改。
- 增加阶段衔接与下一步引导：说明已完成范围、推荐下一步、责任方和产出，减少重复确认，不扩大授权或声称后台自动执行。
- Demo 全部用户可见内容采用最终用户实际使用产品的视角，不在界面加入面向评审者的讲解或 Demo 标签。
- F 阶段增加最小交付一致性核对：断开的引用、关键需求缺少直接验收关联、交付材料版本过期；无法判定时明确报告。

## 安装内容

本版本随 Plugin 提供主 Skill、A-F 六个阶段 Skill、Demo 质量 Skill、候选专家内核，以及 UI/UX Pro Max 和 Impeccable。无需额外安装全局 PM-DEFINE Skill。可选 Subagent 配置不自动启用。

通过仓库 Marketplace 安装，步骤见 [README](https://github.com/junqicheng765-oss/jq-product-agent/blob/v1.0.4/README.md)。GitHub 的 Source code ZIP/TAR 包含该标签的完整分发代码。已安装用户需刷新对应 GitHub Marketplace 并重新安装，再新建 Codex 任务加载更新。

## 检查与限制

- 十一项 Skill、Plugin 结构及 Marketplace 名称校验通过。
- 专家能力 ID/名称、包内相对引用和冻结标准完整性检查通过；八项正/负向完整性测试通过。
- v1.0.4 已完成本机 GitHub 来源安装与缓存内容核对。
- 专家内核仍是候选；尚未完成独立项目的端到端行为试验，判断质量、误报/漏报、用户负担与成本收益未验证。Release 固定分发版本，不等于质量效果已经证明。
- 包内不携带调用者项目事实；业务输入与下游授权仍由具体项目提供。
- 自有内容尚未附开源许可证；随包第三方内容遵循其各自许可证。
