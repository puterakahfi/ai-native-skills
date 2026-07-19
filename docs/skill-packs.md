# Skill Packs

Install bundles for common use cases. Each pack installs a workflow plus the capabilities its documented composition expects.

> **Why packs?** The Agent Skills spec has no native dependency resolution. Skills declare
> `metadata["ai-native-skills.requires"]` for agent-side awareness, but the CLI does not auto-install
> transitive dependencies yet. Packs bridge the gap.

---

## Redesign Pack

Delegated UI/UX and visual redesign loop — route, explicit design/implementation ownership, strategy, visual direction, layout, adaptive components, interaction behavior, design system, domain verification, facade review, correction, and learning.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill redesign-workflow \
  --skill role-switcher \
  --skill master-design \
  --skill master-engineer \
  --skill business-value-alignment \
  --skill design-foundation \
  --skill design-brand \
  --skill design-visual \
  --skill design-genre \
  --skill design-depth \
  --skill design-color \
  --skill design-typography \
  --skill design-iconography \
  --skill composition \
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

The pack includes the current `brand-identity-review` adapter. Other specialist domains still require their own reviewer when complete domain approval is requested.

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
| `redesign-workflow` | role-switcher; explicit design and implementation owners; strategy/visual/layout/interaction/system ports; audit/review/refinement; value alignment; learning/eval; governing domain reviewer |
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