# Optional Codex Subagent

This folder is not part of the Plugin installation contract. It is an optional configuration for a team that already delegates work through Codex subagents.

After the `tc-product-agent` Plugin is installed with both `$tc-product-agent` and `$jq-demo-quality`, an administrator or project owner may copy `tc-product-designer.toml` to one of these Codex configuration locations:

- Personal scope: `~/.codex/agents/`
- Project scope: `.codex/agents/`

The resulting `tc_product_designer` subagent is an execution role that uses the installed Skill. It should be delegated complex, relatively self-contained product-definition and handoff work by a parent Agent. Do not install it merely to make the Skill work: direct Skill invocation remains the default for ordinary use.

Before work begins, the parent should tell the subagent whether the task is project work (`P`) or a controlled evaluation (`E`). The optional role must not modify the Agent package itself unless it is explicitly assigned an `H` task.

The subagent inherits the parent session's permission and tool environment unless its own configuration explicitly changes them. Review its model, permissions, and delegation policy before enabling it in a shared environment.
