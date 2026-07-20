# Skill Packs

Install bundles for common use cases. Each pack installs a workflow plus the capabilities its documented composition expects.

> **Why packs?** The Agent Skills spec has no native dependency resolution. Skills declare
> `metadata["ai-native-skills.requires"]` for agent-side awareness, but the CLI does not auto-install
> transitive dependencies yet. Packs bridge the gap.

Machine-readable pack manifests are being introduced incrementally. The Redesign Pack is currently canonical and CI-validated through `packs/redesign/pack.yaml`; the other commands in this document remain manually maintained until they receive their own manifests.

---

## Redesign Pack

Delegated UI/UX and visual redesign loop — route, explicit design/implementation ownership, verified decision provenance, strategy, comparative visual direction, composition, hierarchy, optional depth, layout, adaptive components, interaction behavior, design system, domain verification, facade review, bounded correction, and learning.

The command below is the manifest's `complete` profile. CI validates the repository coordinate, skill membership, ordering, and final flags against the canonical manifest.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill redesign-workflow \
  --skill role-switcher \
  --skill master-design \
  --skill master-engineer \
  --skill business-value-alignment \
  --skill decision-provenance \
  --skill design-foundation \
  --skill design-brand \
  --skill design-visual \
  --skill design-genre \
  --skill design-depth \
  --skill design-color \
  --skill design-typography \
  --skill design-iconography \
  --skill composition \
  --skill visual-hierarchy \
  --skill readability \
  --skill motion-design \
  --skill design-layout \
  --skill macrostructures \
  --skill responsiveness \
  --skill adaptive-component-design \
  --skill ui-components \
  --skill design-spacing \
  --skill design-strategy \
  --skill content-strategy \
  --skill information-architecture \
  --skill copywriting \
  --skill ux-psychology \
  --skill cro \
  --skill design-interaction \
  --skill ux-ui-patterns \
  --skill ux-patterns-for-developers \
  --skill design-system \
  --skill accessibility \
  --skill dark-light-theming \
  --skill design-audit \
  --skill design-review \
  --skill brand-identity-review \
  --skill design-refinement \
  --skill skill-evolution \
  --skill skill-eval \
  --skill git-workflow \
  -g -y
```

Generate and validate the command from the manifest with:

```text
python scripts/validate-skill-packs.py \
  --pack redesign \
  --profile complete \
  --print-install-command
```

The pack includes contextual visual-direction and anti-slop capabilities, `decision-provenance` for scope/lock/override authority, and the current `brand-identity-review` adapter. Other specialist domains still require their own reviewer when complete domain approval is requested.

---

## Feature Delivery Pack

Verified feature scope, implementation, rendered acceptance, technical review, and explicit merge authorization.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill new-feature-workflow \
  --skill master-engineer \
  --skill master-design \
  --skill decision-provenance \
  --skill spec-workflow \
  --skill test-driven-development \
  --skill design-review \
  --skill code-review-workflow \
  --skill architecture-review \
  --skill security-review \
  --skill threat-modeling \
  -g -y
```

---

## Identity Review Pack

Evidence-backed logo and brand-identity system audit using the `design-review` facade and canonical `BI` gates.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill design-audit \
  --skill design-review \
  --skill brand-identity-review \
  --skill design-brand \
  --skill composition \
  --skill visual-hierarchy \
  --skill design-typography \
  --skill design-color \
  --skill design-refinement \
  -g -y
```

Use for identity audits and acceptance. The pack does not provide legal trademark clearance.

---

## Role Switcher Pack

Auto-compose expert personas from intent — design, identity, engineering, product, and research.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill role-switcher \
  --skill master-engineer \
  --skill master-design \
  --skill product-manager \
  --skill ux-psychology \
  --skill user-research \
  --skill native-ai-engineer \
  --skill diagram-architect \
  --skill design-review \
  --skill brand-identity-review \
  --skill systematic-debugging \
  --skill architecture-review \
  --skill security-review \
  --skill plan \
  -g -y
```

---

## Product Development Pack

Full product lifecycle — discovery, verified PRD/MVP decisions, implementation, product acceptance, release approval, authorized deployment, launch, and learning.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill product-development-workflow \
  --skill product-requirements \
  --skill business-value-alignment \
  --skill experiment-design \
  --skill user-research \
  --skill decision-provenance \
  --skill master-design \
  --skill master-engineer \
  --skill spec-workflow \
  --skill new-feature-workflow \
  --skill design-review \
  --skill threat-modeling \
  --skill code-review-workflow \
  --skill deployment-workflow \
  --skill context-manager \
  --skill security-review \
  --skill architecture-review \
  --skill observability-design \
  --skill resilience-engineering \
  --skill incident-response \
  -g -y
```

---

## Deployment Pack

Immutable release candidate, technical readiness, provenance-backed deployment authorization, direct environment verification, and explicit confirm-or-rollback outcome.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill deployment-workflow \
  --skill decision-provenance \
  --skill context-manager \
  --skill security-review \
  --skill architecture-review \
  --skill code-review-workflow \
  --skill master-engineer \
  --skill observability-design \
  --skill resilience-engineering \
  --skill incident-response \
  -g -y
```

The pack does not define provider commands or environment policy. Product adapters still supply the actual deployment mechanism, protected-environment rules, artifact identity method, health checks, and rollback procedure.

---

## Engineering Quality Pack

Code review, debugging, security, architecture, evidence, risk authority, and merge authorization.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill code-review-workflow \
  --skill bugfix-workflow \
  --skill decision-provenance \
  --skill master-engineer \
  --skill systematic-debugging \
  --skill architecture-review \
  --skill security-review \
  --skill threat-modeling \
  --skill test-driven-development \
  --skill resilience-engineering \
  --skill refactoring \
  --skill skill-evolution \
  --skill skill-eval \
  --skill git-workflow \
  -g -y
```

---

## Full Suite

```bash
npx skills add puterakahfi/ai-native-skills -g -y
```

---

## Dependency Map

| Workflow / Meta-skill | Requires |
|---|---|
| `redesign-workflow` | canonical manifest: `packs/redesign/pack.yaml`; role-switcher; explicit design, implementation, and repository write owners; decision-provenance; master-design visual-direction comparison; design-foundation; design-visual with composition, visual-hierarchy, and active adapters; layout/interaction/system ports; conditional audit/review/refinement; value alignment; learning/eval; governing domain reviewer |
| `design-visual` | resolved foundation and locks; accepted or compared direction; composition + visual-hierarchy for page-level change; concern-specific color/type/depth/iconography/motion/readability adapters |
| `design-refinement` | design-audit, design-review, governing domain reviewer, master-design, skill-evolution, skill-eval |
| `brand-identity-review` | design-review, design-brand, composition, visual-hierarchy, design-typography, design-color |
| `decision-provenance` | authoritative source references, decision-domain owner/policy, previous decision records when applicable |
| `skill-evolution` | skill-eval, git-workflow |
| `role-switcher` | engineering/design/product/research owners, design-review, brand-identity-review, debugging, architecture/security review, plan |
| `workflow-router` | design audit/refinement/redesign/review, brand-identity-review, feature/bug/review/deploy/product workflows, learning/eval/git, skill-doctor, spec-workflow |
| `product-development-workflow` | product requirements/value/experiment/research; decision-provenance for PRD/MVP/risk/release decisions; design/engineering owners; feature workflow; code review; deployment; observability |
| `bugfix-workflow` | systematic-debugging, master-engineer, security-review, test-driven-development |
| `code-review-workflow` | architecture/design/logic/security reviewers; decision-provenance for risk and merge authority |
| `new-feature-workflow` | engineering/design owners; decision-provenance for feature scope/decisions/risks; spec, tests, design review, code review |
| `deployment-workflow` | decision-provenance for candidate/environment/action authority; context-manager; security/code review; immutable candidate identity; observability; resilience; rollback and incident ownership |
| `skill-doctor` | skill-eval |
