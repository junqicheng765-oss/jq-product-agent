# JQ Product Agent

面向复杂系统产品设计的 Codex Agent 能力包，当前版本为 **v0.4.0 候选版**。

本仓库可作为独立 Codex Marketplace 使用。它包含一个 `tc-product-agent` Plugin；Plugin 内含同名 Skill 和一份可选 Subagent 配置。仓库品牌已命名为 JQ Product Agent，内部标识暂时保留，以保持 v0.4.0 的安装兼容性。

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

安装完成后新建一个 Codex 会话，使新 Skill 被发现。输入 `$tc-product-agent`，或直接描述需要完成的复杂系统产品设计任务。

## 包内关系

- **Plugin**：推荐分发与安装入口，负责把能力完整装入 Codex。
- **Skill**：实际的方法、流程、产出合同、七大一级/48 项二级能力和审计标准。
- **Subagent 配置**：可选执行角色，位于 `plugins/tc-product-agent/optional/codex-subagent/`；不随 Plugin 自动启用，也不是使用 Skill 的前提。

## 默认交付

1. 产品基线与 PRD；
2. 可操作、能验证核心流程与规则的产品原型，以及产品给设计的交付物；
3. 产品给研发的交接包。

最终视觉稿、生产代码、部署和实际外发均为条件动作，需要相应授权、工具和回传证据。

## 当前证据边界

本候选包已通过规则包、Skill、Plugin 和 Marketplace 结构校验。尚未完成独立接收者的真实干净环境安装、产品岗/非产品岗试用、第二轮无辅助试用及设计/研发真实接收测试，因此不能标记为正式稳定版。

## 许可状态

当前仓库未附开源许可证。公开可见不等于授权复制、修改或再分发；待代码与方法论文档的许可方案确认后，再补入正式许可证和版权声明。
