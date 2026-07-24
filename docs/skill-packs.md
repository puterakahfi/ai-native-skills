# Skill Packs

Install bundles for common use cases. Each pack installs a workflow plus the capabilities its documented composition expects.

> **Why packs?** The Agent Skills spec has no native dependency resolution. Skills declare
> `metadata["ai-native-skills.requires"]` for agent-side awareness, but the CLI does not auto-install
> transitive dependencies yet. Packs bridge the gap.

Machine-readable pack manifests are being introduced incrementally. The Redesign Pack is currently canonical and CI-validated through `packs/redesign/pack.yaml`; the other commands in this document remain manually maintained until they receive their own manifests.

---

## Redesign Pack

Delegated UI/UX and visual redesign loop — route, explicit design/implementation ownership, verified decision provenance, strategy, comparative visual direction, composition, hierarchy, optional depth, layout, component-family and template consistency, adaptive components, interaction behavior, design system, repository implementation-context discovery, domain and architecture verification, facade review, bounded correction, and learning.

The command below is the manifest's `complete` profile. CI validates the repository coordinate, skill membership, ordering, and final flags against the canonical manifest.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill redesign-workflow \
  --skill role-switcher \
  --skill master-design \
  --skill master-engineer \
  --skill implementation-context-discovery \
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
  --skill component-family-design \
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
  --skill architecture-review \
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

The pack includes `component-family-design` for preserving organism and template identity across route-specific variants, contextual visual-direction and anti-slop capabilities, `implementation-context-discovery` for preserving canonical repository adapters before code, `architecture-review` for independent post-implementation acceptance, `decision-provenance` for scope/lock/dependency/override authority, and the current `brand-identity-review` adapter. Other specialist domains still require their own reviewer when complete domain approval is requested.

---

## Feature Delivery Pack

Verified feature scope, repository implementation-context mapping, implementation, rendered acceptance, architecture/technical review, and explicit merge authorization.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill new-feature-workflow \
  --skill master-engineer \
  --skill master-design \
  --skill implementation-context-discovery \
  --skill decision-provenance \
  --skill spec-workflow \
  --skill test-driven-development \
  --skill architecture-review \
  --skill design-review \
  --skill code-review-workflow \
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

Auto-compose expert personas from intent — design, identity, engineering, product, platform, and research.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill role-switcher \
  --skill master-engineer \
  --skill master-design \
  --skill product-manager \
  --skill ux-psychology \
  --skill user-research \
  --skill native-ai-engineer \
  --skill chatgpt-app-development \
  --skill diagram-architect \
  --skill implementation-context-discovery \
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

Full product lifecycle — discovery, verified PRD/MVP decisions, release-unit and epic/feature/task decomposition, branch/PR topology, implementation-context mapping, implementation, product acceptance, release approval, authorized deployment, launch, and learning.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill product-development-workflow \
  --skill product-requirements \
  --skill business-value-alignment \
  --skill experiment-design \
  --skill user-research \
  --skill delivery-work-breakdown \
  --skill decision-provenance \
  --skill master-design \
  --skill master-engineer \
  --skill implementation-context-discovery \
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

## ChatGPT App Product Pack

End-to-end ChatGPT App product delivery using the existing product lifecycle, release-unit/epic decomposition, plus the Apps SDK/MCP platform specialist. The pack covers product discovery, economic and quota ownership, tool/resource contracts, widget UX and state, native ChatGPT capability handoff, auth/security, repository implementation-context mapping, implementation, actual ChatGPT integration evidence, deployment, and publication readiness.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill workflow-router \
  --skill role-switcher \
  --skill product-development-workflow \
  --skill chatgpt-app-development \
  --skill product-requirements \
  --skill business-value-alignment \
  --skill experiment-design \
  --skill user-research \
  --skill product-manager \
  --skill delivery-work-breakdown \
  --skill decision-provenance \
  --skill native-ai-engineer \
  --skill ai-system-design \
  --skill api-contract \
  --skill master-design \
  --skill adaptive-component-design \
  --skill accessibility \
  --skill master-engineer \
  --skill implementation-context-discovery \
  --skill spec-workflow \
  --skill new-feature-workflow \
  --skill test-driven-development \
  --skill design-review \
  --skill threat-modeling \
  --skill security-review \
  --skill architecture-review \
  --skill code-review-workflow \
  --skill deployment-workflow \
  --skill context-manager \
  --skill observability-design \
  --skill resilience-engineering \
  --skill incident-response \
  -g -y
```

Use this pack when the target product surface is a ChatGPT App, Apps SDK integration, MCP-backed ChatGPT tool, or interactive ChatGPT widget.

The pack does not add a new ChatGPT-specific lifecycle. `workflow-router` selects `product-development-workflow` for a product from zero or `new-feature-workflow` for an existing-product integration, then applies `chatgpt-app-development` as the platform specialist.

The pack also does not guarantee native ChatGPT capability availability for every user. The product must verify current platform documentation, target plan/workspace behavior, and the actual execution path. A product promising user-owned native generation must directly prove that the handoff path does not call a developer-owned model or image API.

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

Architecture and implementation quality loop — repository-context mapping, pragmatic architecture and object-design decisions, internal code quality, testing, debugging, behavior-preserving refactoring, independent architecture/security/code review, and technical-debt governance.

```bash
npx skills add puterakahfi/ai-native-skills \
  --skill implementation-context-discovery \
  --skill master-engineer \
  --skill clean-architecture \
  --skill solid-design \
  --skill clean-code \
  --skill test-driven-development \
  --skill systematic-debugging \
  --skill refactoring \
  --skill architecture-review \
  --skill security-review \
  --skill code-review-workflow \
  --skill technical-debt-governance \
  -g -y
```

`clean-code` is the baseline implementation-quality lens. Load `solid-design` only for material responsibility, extension, substitution, client-interface, or dependency-design pressure. Load `clean-architecture` only for material architecture-style or policy/mechanism boundary decisions; it may correctly return `NOT_JUSTIFIED`. Independent `architecture-review` and `code-review-workflow` remain required acceptance gates.
