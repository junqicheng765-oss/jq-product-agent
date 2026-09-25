# JQ Product Agent Plugin

Version: `1.0.1`, a candidate update to the `1.0.0` public baseline. The install identifier remains `tc-product-agent` for compatibility.

JQ Product Agent helps product and non-product colleagues who understand the business turn a new system, an existing-system iteration, or a small requirement into an evidence-based product baseline, an operable product prototype and design handoff, and a development-ready handoff package.

It includes an A-F user-facing decision flow, an S1-S7 internal production and audit flow, seven first-level and 48 second-level product capabilities, scoped current-state reconciliation, meeting-minutes intake, staged demos, Figma preflight, engineering handoff, H/P/E mode isolation, and Agent quality scoring. Detailed PRD follows confirmation of visible product behavior; new business decisions and major conflicts still return to a human.

This candidate adds a focused F-stage handoff consistency check for broken references, key requirements without directly traceable acceptance, and stale delivery-version claims. It reuses the project's existing mapping and version evidence; ambiguous coverage remains unresolved rather than being reported as passed.

## What Installs

```text
tc-product-agent/
├── .codex-plugin/plugin.json
├── skills/tc-product-agent/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── sources/
├── skills/jq-stage-a-scope/SKILL.md
├── skills/jq-stage-b-system/SKILL.md
├── skills/jq-stage-c-structure/SKILL.md
├── skills/jq-stage-d-demo/SKILL.md
├── skills/jq-stage-e-modules/SKILL.md
├── skills/jq-stage-f-handoff/SKILL.md
├── skills/jq-demo-quality/SKILL.md
├── skills/ui-ux-pro-max/
├── skills/impeccable/
├── third_party/
└── optional/codex-subagent/
```

The Plugin contains ten discoverable Skills: the main `$tc-product-agent`, one execution contract for each A-F stage, `$jq-demo-quality`, and bundled `$ui-ux-pro-max` and `$impeccable`. All ten install together. The two external Skills are invoked only when D/E visual work needs them, not on every product step. The main Skill owns product decisions, facts and handoffs. A-F can share review windows for small requirements; ten Skills do not imply ten meetings. The optional subagent is a separate execution role that invokes these Skills; it is not required and is not installed automatically.

The A-F artifact skeletons are in `skills/tc-product-agent/references/23-AF阶段产物模板.md`. They are content templates, not six mandatory files or a fixed visual style. The fuller PRD, Use Case, design and engineering contracts remain in references `02`, `14`, `15`, and `16`.

`$ui-ux-pro-max` requires Python 3 (standard library only); `$impeccable` v4.0.2 requires Node.js for its local scripts. Both Skills and their data/scripts ship inside the Plugin, so installation does not run their upstream installers or fetch code. The bundled Impeccable context check does not contact its update service by default and cannot override host authorization. See [third-party provenance](third_party/README.md) for pinned sources, licenses and local adaptations. The version number does not imply real-project output quality has been validated.

## Default Delivery

Unless a user explicitly narrows the endpoint, project mode produces three version-aligned deliverables:

1. Product baseline and PRD.
2. An operable product prototype plus the product-to-design package.
3. The product-to-engineering handoff package.

The product prototype must validate core tasks, key branches, necessary states, and return paths. It is not final visual design or production code. Actual external delivery, Figma writes, final visual production, engineering implementation, and deployment require separate authorization and evidence.

## Runtime Modes

- `P`: work on the caller's project; this is the default.
- `H`: improve JQ Product Agent itself without advancing a sample project.
- `E`: run a frozen, isolated evaluation without turning it into project delivery.

## Distribution Boundary

The Plugin contains reusable product capability and frozen standards only. It does not include internal history, sample-project requirements, validation archives, Figma nodes, implementation evidence, or local absolute paths.

The ten Skills, Plugin, and Marketplace have passed structural checks and isolated installation from the packaged ZIP. The two bundled visual Skills passed limited local runtime checks. Product and non-product user trials, real-project Demo quality, and design/engineering handoff acceptance have not yet been verified; do not describe those outcomes as proven.
