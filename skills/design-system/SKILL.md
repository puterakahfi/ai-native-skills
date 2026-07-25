---
name: design-system
description: Design token decisions and system construction — maps accepted repository tokens first for existing products, or declares a new semantic token system for net-new products when authorized. Produces token maps, semantic assignments, violations, and gate scores before visual production.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-system.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: "['master-design', 'ux-ui-patterns', 'accessibility', 'design-review', 'implementation-context-discovery']"
---

# Design System Port

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/design-system.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs:
- color_palette
- type_scale_intent
allowed_outputs:
- token_map
- semantic_role_assignments
- token_violation_list
- design_system_gate_scores
quality_gates:
- one_token_one_semantic_role
- no_token_collapse
- spacing_multiples_of_base_unit
```

Return the token map, semantic assignments, violations, and gate scores. Spacing tokens must be multiples of the declared base unit rather than arbitrary values.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

> This skill doubles as **Port 5: Design System & Accessibility** — the systematic cross-cutting layer.
> Load this for tokens, theming, and accessibility concerns.
> Adapter skills: `dark-light-theming`, `accessibility`

---

# Design System Skill

## Repository precedence gate

Determine the artifact context before declaring or changing tokens.

```text
existing repository or product
→ load implementation-context-discovery
→ inspect accepted component, token, typography, icon, and theme systems
→ document the canonical repository token map
→ reuse or make a bounded extension through verified authority
→ never invent a route-local or feature-local design system

net-new product or explicitly approved system replacement
→ declare a new token table
→ design within that table
→ verify ownership, migration, and adoption scope
```

For existing repositories, “declare the token table” means **record the accepted repository token map and semantic roles**. It does not mean create a new palette, spacing scale, type scale, theme, or token namespace for the current screen.

Required repository-backed handoff:

```yaml
design_system_repository_handoff:
  repository_ref: <ref>
  canonical_system_status: canonical | migration_target | accepted_but_local | unknown
  canonical_token_sources: []
  canonical_component_sources: []
  semantic_role_map: []
  allowed_extensions: []
  prohibited_parallel_systems: []
  authority_refs: []
  evidence_gaps: []
  decision: reuse | bounded_extension | migrate | blocked
```

If canonicality, coverage, or authority is unknown, return `NOT_VERIFIED` or `BLOCKED` before visual production.

## Hard rules

```text
RULE 1 — Existing repository decisions take precedence
  ❌ create a route-local theme because the current screen needs different colors
  ✅ consume the accepted repository tokens and component variants

RULE 2 — One semantic token = one role only, NEVER collapse
  ❌ --accent used for: logo + hover + status + CTA → semantic collapse
  ✅ each token has a single, unambiguous job

RULE 3 — Use the accepted spacing base and scale
  ❌ invent raw spacing values or a second scale in an existing product
  ✅ use the repository scale; for a net-new system, declare spacing as multiples of its base unit

RULE 4 — Use the accepted typography roles and scale
  ❌ create a route-local type scale
  ✅ map page title, section title, body, label, and metadata to repository roles

RULE 5 — Declare or document the token table before visual production
  ❌ design first and justify tokens later
  ✅ existing product: document accepted tokens; net-new product: declare authorized tokens
```

---

## Core principle

```text
Design system = decisions made once, applied everywhere.

Without it: every screen is a new negotiation between color, space, and type.
With it:    every screen is an instance of the same vocabulary.
```

Before designing a screen:

```text
1. classify existing-repository vs net-new-system work
2. existing repository → map canonical implementation context
3. net-new system → declare the token table with authority
4. design only within the accepted or declared system
5. record violations, bounded extensions, and evidence gaps
```

Never hardcode a value that should be owned by the accepted design system.

---

## 6-Step Token Declaration Overview

For existing repositories, these steps inventory and map accepted sources. For net-new authorized systems, they declare the new sources.

| Step | Category | Reference File | Load Instruction |
|------|----------|----------------|------------------|
| 1 | Color Tokens | `references/color-spacing.md` | Load for semantic roles, theme defaults, color decision protocol |
| 2 | Spacing Tokens | `references/color-spacing.md` | Load for base-unit scale and spacing decisions |
| 3 | Typography Tokens | `references/typography-elevation.md` | Load for type scale, weights, line heights, and letter spacing |
| 4 | Elevation Tokens | `references/typography-elevation.md` | Load for elevation hierarchy |
| 5 | Motion Tokens | `references/typography-elevation.md` | Load for durations, easings, and reduced-motion patterns |
| 6 | Layout Tokens | `references/layout-checklist.md` | Load for container widths, radius, and layout philosophy |

> Load only the references needed by the current concern. Repository evidence remains authoritative for existing product implementation.

---

## Step-by-Step Quick Reference

### Step 1 → Color Tokens
Map accepted semantic color roles first. Declare new color roles only for an approved net-new system or bounded extension.

### Step 2 → Spacing Tokens
Use the repository spacing scale. For a net-new system, declare a base unit and scale before use.

### Step 3 → Typography Tokens
Map accepted semantic type roles before considering a bounded extension. Do not create a route-local scale.

### Step 4 → Elevation Tokens
Use accepted elevation roles and hierarchy; do not add decorative shadow levels without a semantic role.

### Step 5 → Motion Tokens
Use accepted durations/easings and preserve reduced-motion behavior.

### Step 6 → Layout Tokens
Use accepted containers and radius philosophy; repeated organisms and templates also route through component-family design.

---

## Token Declaration Checklist

```text
□ artifact classified as existing repository or net-new system
□ implementation-context discovery completed for repository-backed work
□ canonical token/component/typography sources recorded
□ color tokens have one semantic role
□ spacing uses the accepted or declared base scale
□ typography uses accepted or declared semantic roles
□ elevation and motion roles are explicit
□ border radius and layout roles are explicit
□ bounded extensions include authority and migration/adoption scope
□ prohibited parallel systems are recorded
```

## Failure conditions

```text
FAIL: route-local or feature-local theme/token system when canonical coverage exists
FAIL: document-root theme mutation used to install a feature theme
FAIL: canonical component/token system bypassed without a proven gap and authority
FAIL: any hardcoded value that should be owned by the accepted token system
FAIL: same token used for multiple unrelated semantic roles
FAIL: spacing or typography scale invented locally in an existing repository
BLOCKED: canonicality, coverage, or extension authority remains unknown
```
