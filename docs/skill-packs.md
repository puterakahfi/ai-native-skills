# Skill Packs

Install bundles for common use cases. Each pack installs a workflow plus all skills it depends on.

> **Why packs?** The Agent Skills spec has no native dependency resolution. Skills declare
> `metadata["ai-native-skills.requires"]` for agent-side awareness, but the CLI does not auto-install
> transitive dependencies yet. Packs bridge the gap.

---

## Redesign Pack

Full UI/UX and visual redesign loop — audit, domain review, design system, depth, genre, layout, copy, gates, and verified-case learning promotion.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill redesign-workflow \
  --skill design-foundation \
  --skill design-brand \
  --skill design-genre \
  --skill design-depth \
  --skill design-color \
  --skill design-typography \
  --skill design-spacing \
  --skill design-iconography \
  --skill design-visual \
  --skill design-layout \
  --skill adaptive-component-design \
  --skill design-strategy \
  --skill design-interaction \
  --skill design-system \
  --skill design-audit \
  --skill design-review \
  --skill brand-identity-review \
  --skill design-refinement \
  --skill skill-evolution \
  --skill skill-eval \
  --skill git-workflow \
  --skill master-design \
  --skill macrostructures \
  --skill ui-components \
  --skill composition \
  --skill visual-hierarchy \
  --skill copywriting \
  --skill ux-psychology \
  --skill accessibility \
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

Full product lifecycle — discovery, PRD, spec, implementation, verification, deploy.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill product-development-workflow \
  --skill product-requirements \
  --skill business-value-alignment \
  --skill experiment-design \
  --skill user-research \
  --skill master-design \
  --skill master-engineer \
  --skill spec-workflow \
  --skill threat-modeling \
  --skill code-review-workflow \
  --skill deployment-workflow \
  --skill observability-design \
  -g -y
```

---

## Engineering Quality Pack

Code review, debugging, security, architecture — everything before merge.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill code-review-workflow \
  --skill bugfix-workflow \
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
| `redesign-workflow` | design foundation/brand/genre/depth/color/type/spacing/iconography, adaptive component design, audit/review/refinement, identity reviewer when identity is in scope, learning/eval/git, master-design, composition, hierarchy, copy, UX, accessibility |
| `design-refinement` | design-audit, design-review, governing domain reviewer, master-design, skill-evolution, skill-eval |
| `brand-identity-review` | design-review, design-brand, composition, visual-hierarchy, design-typography, design-color |
| `skill-evolution` | skill-eval, git-workflow |
| `role-switcher` | engineering/design/product/research owners, design-review, brand-identity-review, debugging, architecture/security review, plan |
| `workflow-router` | design audit/refinement/redesign/review, brand-identity-review, feature/bug/review/deploy/product workflows, learning/eval/git, skill-doctor, spec-workflow |
| `product-development-workflow` | product requirements/value/experiment/research, design/engineering owners, spec, threat modeling, code review, deployment, observability |
| `bugfix-workflow` | systematic-debugging, master-engineer, security-review, test-driven-development |
| `code-review-workflow` | master-engineer, architecture-review, security-review, threat-modeling |
| `new-feature-workflow` | master-engineer, master-design, spec-workflow, test-driven-development |
| `deployment-workflow` | master-engineer, observability-design, resilience-engineering |
| `skill-doctor` | skill-eval |