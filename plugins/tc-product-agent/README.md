# TC Product Agent Plugin

Version: `0.4.0` candidate

TC Product Agent helps company-internal product and non-product colleagues who understand business implementation turn their own complex-system needs into an evidence-based product baseline, an operable product prototype and design handoff, and a development-ready handoff package.

It includes the S1-S7 workflow, seven first-level and 48 second-level product capabilities, source reconciliation, complex-system models, representative Use Cases, product-prototype requirements, Figma preflight, engineering handoff, H/P/E mode isolation, Agent quality scoring, and release hygiene rules.

## What Installs

```text
tc-product-agent/
├── .codex-plugin/plugin.json
├── skills/tc-product-agent/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── sources/
└── optional/codex-subagent/
```

The Plugin installs one discoverable Skill. Users can invoke `$tc-product-agent` or ask Codex to define or review a complex product. The optional subagent is a separate execution role that invokes the Skill; it is not required and is not installed automatically.

## Default Delivery

Unless a user explicitly narrows the endpoint, project mode produces three version-aligned deliverables:

1. Product baseline and PRD.
2. An operable product prototype plus the product-to-design package.
3. The product-to-engineering handoff package.

The product prototype must validate core tasks, key branches, necessary states, and return paths. It is not final visual design or production code. Actual external delivery, Figma writes, final visual production, engineering implementation, and deployment require separate authorization and evidence.

## Runtime Modes

- `P`: work on the caller's project; this is the default.
- `H`: improve TC Product Agent itself without advancing a sample project.
- `E`: run a frozen, isolated evaluation without turning it into project delivery.

## Distribution Boundary

The Plugin contains reusable product capability and frozen standards only. It does not include internal history, sample-project requirements, validation archives, Figma nodes, implementation evidence, or local absolute paths.

This candidate has passed package, Skill, and Plugin structure checks only after those checks are run. It must not be described as independently installable or user-validated until a clean Codex installation and the planned product/non-product user trials have produced evidence.

