# JQ Product Agent Plugin

Package version: `1.1.3`. The install identifier remains `tc-product-agent` for compatibility.

Version 1.1.3 requires every product-stage deliverable, revision, and review reply to start with a visible main-stage position, current action, and actual status. A-F retain stable numbering; substep counts require a maintained plan. Scoped work and Agent iteration use their own task positions. Progress display does not add approval gates and stays outside end-user Demo interfaces. These are instruction changes; consistent model behavior still requires fresh-project observation.

Version 1.1.2 adds continuous A-F navigation, evidence-based stage exit checks, and human review triggered by unresolved product decisions rather than every step. It also includes reusable Figma initialization, user-bound target files, existing-interface input requirements, explicit visual-choice evidence across routes, and per-page direct-edit/generation routing. No new design subagent or Figma account/tool entitlement is installed. Structural checks do not establish behavior gains; evaluate in a fresh project.

Version 1.1.1 adds intent-based routing that distinguishes baseline maintenance, consultation/review, scoped changes and full product design before intake or tool discovery. A/C reuse evidence-labelled scenario cards and business-lifecycle or functional use cases without fixed counts or extra approval gates. C/D/E share a task-based product-type design baseline (reference `25`), preserving existing design systems and treating AI as an additional interaction constraint. The A-F artifact and design-task templates carry these decisions. These are instruction changes; structural checks do not establish model behavior or product-quality gains.

JQ Product Agent helps product and non-product colleagues who understand the business turn a new system, an existing-system iteration, or a small requirement into an evidence-based product baseline, a confirmed flow prototype, a styled operable Demo, and a development handoff package.

It includes an A-F user-facing decision flow, an S1-S7 internal production and audit flow, seven first-level and 48 second-level product capabilities, scoped current-state reconciliation, meeting-minutes intake, staged demos, Figma preflight, engineering handoff, H/P/E mode isolation, and Agent quality scoring. Detailed PRD follows confirmation of visible product behavior; new business decisions and major conflicts still return to a human.

The F-stage handoff consistency check covers broken references, key requirements without directly traceable acceptance, and stale delivery-version claims. It reuses the project's existing mapping and version evidence; ambiguous coverage remains unresolved rather than being reported as passed.

The Demo contract now requires every user-visible screen, message, state, and seeded record to read like the product as used by its intended user, without reviewer-facing explanations or Demo labels in the interface.

Version 1.1.0 adds design-route discovery at startup. After flow and module behavior are confirmed, the full Figma route compares three visual directions on one representative page, expands the selected direction to the delivery scope, refines it with Computer Use, and uses Figma design context and screenshots to implement a styled operable Demo. Existing design systems are preserved unless redesign is authorized. Partial Figma and Codex-only routes report the outputs each route actually produces. A readable design link, a confirmed design, and verified code fidelity are separate states; none proves production readiness.

Version 1.0.3 adds explicit next-step guidance and stage transitions: explain what is complete, who acts next, what to review or provide, and what will be produced. Continue work within existing authorization when inputs are sufficient; do not add repeated approvals, expand scope, or promise background execution. Real-project behavior of this guidance remains to be verified.

Version 1.0.4 bundles the candidate `$jq-product-expert`: concise PM-DEFINE methods, canonical capability IDs, scoped diagnosis, tradeoffs and acceptance evidence. The main Skill retains workflow and fact ownership. Load relevant methods on demand and consult authoritative clauses for key risks, ambiguity and quality gates; frozen standards and quality criteria remain unchanged. No separate global expert Skill is required. Actual judgment quality and cost savings are not yet verified.

Version 1.0.5 requires scoped Demo copy and interaction review before D/E presentation or delivery, followed by corrections and rechecks. Review all user-facing product copy in the delivered scope and actually exercise core and critical-risk interactions; layout checks, screenshots, or a happy-path walkthrough do not prove full coverage. Record copy and interaction conclusions separately, including versions, coverage, evidence and unverified states. Changes receive impact-based regression checks rather than a full capability audit every turn. Blocking/major defects or missing critical interaction evidence prevent the affected readiness claim. The protocol uses the existing Demo Skill and product expert without adding approval gates or changing business rules. Actual model execution of this protocol remains to be verified in another project; reviewed wording is not claimed to be universally optimal.

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
├── skills/jq-product-expert/
├── scripts/validate-expert-kernel.mjs
├── scripts/tests/expert-kernel.test.mjs
├── skills/ui-ux-pro-max/
├── skills/impeccable/
├── third_party/
└── optional/codex-subagent/
```

The Plugin contains eleven discoverable Skills: the main `$tc-product-agent`, one execution contract for each A-F stage, `$jq-demo-quality`, candidate `$jq-product-expert`, and bundled `$ui-ux-pro-max` and `$impeccable`. All eleven install together. The two external Skills are invoked only when D/E visual work needs them, not on every product step. The main Skill owns product decisions, facts and handoffs. A-F can share review windows for small requirements; eleven Skills do not imply eleven meetings. The optional subagent is a separate execution role that invokes these Skills; it is not required and is not installed automatically.

The A-F artifact skeletons are in `skills/tc-product-agent/references/23-AF阶段产物模板.md`. They are content templates, not six mandatory files or a fixed visual style. The fuller PRD, Use Case, design and engineering contracts remain in references `02`, `14`, `15`, and `16`.

`$ui-ux-pro-max` requires Python 3 (standard library only); `$impeccable` v4.0.2 requires Node.js for its local scripts. Both Skills and their data/scripts ship inside the Plugin, so installation does not run their upstream installers or fetch code. The bundled Impeccable context check does not contact its update service by default and cannot override host authorization. See [third-party provenance](third_party/README.md) for pinned sources, licenses and local adaptations. The version number does not imply real-project output quality has been validated.

## Default Delivery

Unless a user explicitly narrows the endpoint, full product-design requests (including small requirements and existing-system iterations) produce three version-aligned deliverables. Maintenance, consultation/review and explicitly scoped changes deliver the agreed task without automatically starting all A-F stages:

1. Product baseline and PRD.
2. An operable flow prototype, visual-design evidence or an explicit Codex route, and a styled operable Demo.
3. The product-to-engineering handoff package with PRD, design references where available, the styled Demo, and traceable acceptance criteria.

The flow prototype must validate core tasks, key branches, necessary states, and return paths. The styled Demo must additionally be checked for user-facing copy, interactions, and design fidelity. Neither is production code or proof of deployment. Actual external delivery, Figma writes, engineering implementation, and deployment require separate authorization and evidence.

## Runtime Modes

- `P`: work on the caller's project; this is the default.
- `H`: improve JQ Product Agent itself without advancing a sample project.
- `E`: run a frozen, isolated evaluation without turning it into project delivery.

## Distribution Boundary

The Plugin contains reusable product capability and frozen standards only. It does not include internal history, sample-project requirements, validation archives, Figma nodes, implementation evidence, or local absolute paths.

The earlier ten-Skill baseline passed structural checks and isolated ZIP installation. Before distribution, run Skill/Plugin structural checks, `node scripts/validate-expert-kernel.mjs`, and `node --test scripts/tests/expert-kernel.test.mjs`; these do not test model reasoning or independent-project behavior. The two bundled visual Skills previously passed limited local runtime checks. Product and non-product user trials, real-project Demo quality, and design/engineering handoff acceptance require their own evidence; do not describe those outcomes as proven.
