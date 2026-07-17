---
name: diagram-architect
description: Turns architecture, workflows, runtime state, contracts, ownership, and decision context into clear diagrams. Produces a renderer-agnostic spec first, then renders via Mermaid, SVG, Excalidraw, or ASCII.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/visual-thinking/diagram-architect.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Diagram Architect

## Overview

Use this skill to design diagrams before rendering them.

The core rule:

```text
diagram spec first, renderer second
```

Do not jump straight to Mermaid, SVG, Excalidraw, or ASCII until the diagram intent, view, nodes, edges, boundaries, constraints, and verification checklist are clear.

## When to Use

Use when the user asks to:

- generate a diagram
- visualize an architecture, workflow, runtime, profile sync, or session model
- explain a core/app/skill/runtime boundary visually
- create a contract-to-adapter map
- create a responsibility or ownership map
- choose the right diagram format for a concept

Do not use for pure UI mockups, marketing visuals, or illustration unless a conceptual diagram is needed first.

## Process

1. **Classify intent.** Name the purpose, audience, and smallest useful view.
2. **Build renderer-agnostic spec.** Define boundaries, nodes, edges, legend, constraints, and verification.
3. **Select renderer.** Use the output goal:
   - polished technical architecture -> load/use `architecture-diagram`
   - hand-drawn exploration -> load/use `excalidraw`
   - docs quick view -> Mermaid markdown
   - terminal/compact note -> ASCII
4. **Render only when requested or clearly useful.** If rendering, every visual element must trace to the spec.
5. **Verify.** Check required nodes, edges, boundaries, labels, and constraints are visible and not misleading.

## Diagram Spec Template

```yaml
diagram:
  id: kebab-case-id
  title: Human Title
  type: runtime_topology
  purpose: What this diagram proves or explains
  audience: engineering
  boundaries:
    - id: boundary_id
      label: Boundary Label
      meaning: ownership/runtime/trust/product/lifecycle scope
  nodes:
    - id: node_id
      label: Node Label
      boundary: boundary_id
      kind: runtime|repo|database|client|contract|adapter|workflow|service
      description: Why it exists
  edges:
    - from: source_id
      to: target_id
      label: Flow label
      direction: source_to_target
      kind: data|control|ownership|install|sync|execution|verification
  legend:
    - symbol: dashed boundary
      meaning: non-owning/client/access scope
  constraints:
    - text: no active-active SQLite sync
      reason: prevents state corruption
  verification:
    - check: all sources of truth are labeled
```

## Renderer Handoff

For HTML/SVG architecture diagrams, load `architecture-diagram` and hand it:

- diagram title and subtitle
- boundaries and their meaning
- nodes grouped by boundary
- edges and labels
- constraints/non-goals that must be visible
- summary card content

For Excalidraw, load `excalidraw` and preserve the same spec with hand-drawn styling.

For Mermaid, emit a Mermaid diagram plus a short verification checklist.

## Common Pitfalls

1. **Rendering before thinking.** Always model the diagram first.
2. **Wrong source of truth.** Do not show clients or installers as owning live state unless they really do.
3. **Boundary ambiguity.** Every boundary must say what it means.
4. **Pretty but false.** A beautiful diagram that implies the wrong architecture fails.
5. **Renderer lock-in.** Core diagram spec must be portable across renderers.

## Verification Checklist

- [ ] Purpose, audience, and view are explicit.
- [ ] Nodes, edges, boundaries, legend, constraints, and verification are present.
- [ ] Directionality and source-of-truth ownership are labeled.
- [ ] Renderer was selected after the spec.
- [ ] Rendered output, if created, matches the spec.
