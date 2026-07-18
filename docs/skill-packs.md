# Skill Packs

Install bundles for common use cases. Each pack installs a workflow plus all skills it depends on.

> **Why packs?** The Agent Skills spec has no native `dependencies` field. Skills declare
> `metadata["ai-native-skills.requires"]` for agent-side awareness, but the CLI won't auto-install
> transitive deps yet. Use the commands below to install a complete, working bundle in one shot.

---

## Redesign Pack
Full UI/UX redesign loop — audit, design system, depth, genre, layout, copy, gates, and automatic verified-case learning promotion.

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

## Role Switcher Pack
Auto-compose expert personas from intent — design, engineering, product, research.

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

## Full Suite (everything)
All 92 entries — skills, workflows, meta-skills, roles, domain, engineering, design.

```bash
npx skills add puterakahfi/ai-native-skills -g -y
```

---

## Dependency Map

| Workflow / Meta-skill | Requires |
|---|---|
| `redesign-workflow` | design-foundation, design-brand, design-genre, design-depth, design-color, design-typography, design-spacing, design-iconography, design-visual, design-layout, adaptive-component-design, design-strategy, design-interaction, design-system, design-audit, design-review, design-refinement, skill-evolution, skill-eval, git-workflow, master-design, macrostructures, ui-components, composition, visual-hierarchy, copywriting, ux-psychology, accessibility |
| `design-refinement` | design-audit, design-review, master-design, skill-evolution, skill-eval |
| `skill-evolution` | skill-eval, git-workflow |
| `role-switcher` | master-engineer, master-design, product-manager, ux-psychology, user-research, native-ai-engineer, diagram-architect, design-review, systematic-debugging, architecture-review, security-review, plan |
| `workflow-router` | redesign-workflow, new-feature-workflow, bugfix-workflow, code-review-workflow, deployment-workflow, product-development-workflow, design-refinement, skill-doctor, spec-workflow |
| `product-development-workflow` | product-requirements, business-value-alignment, experiment-design, user-research, master-design, master-engineer, spec-workflow, threat-modeling, code-review-workflow, deployment-workflow, observability-design |
| `bugfix-workflow` | systematic-debugging, master-engineer, security-review, test-driven-development |
| `code-review-workflow` | master-engineer, architecture-review, security-review, threat-modeling |
| `new-feature-workflow` | master-engineer, master-design, spec-workflow, test-driven-development |
| `deployment-workflow` | master-engineer, observability-design, resilience-engineering |
| `skill-doctor` | skill-eval |
