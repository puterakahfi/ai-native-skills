---
name: hermes-profile-bootstrap
description: Bootstrap the Hermes adapter for the Native AI profile-bootstrap contract. Use when creating, generating, templating, or auditing a Hermes profile that should start with AI-native meta-skills, workflows, foundation skills, runtime skills, and verification policy.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime/profile-bootstrap.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Hermes Profile Bootstrap

> **HARD RULES:** Run phases in order. Verify each step before proceeding. This workflow is idempotent — safe to re-run.

## Overview

Use this skill to create or audit the **Hermes adapter implementation** of the Native AI `profile-bootstrap` contract.

The core contract lives in `native-ai-core/contracts/skills/runtime/profile-bootstrap.contract.yaml`. This skill owns the Hermes-specific profile skeleton, commands, paths, install steps, and verification behavior. The profile is a **runtime skeleton**, not a product.

Target command shape:

```bash
hermes-generate profile <profile-name> --preset engineering
```

Until that command exists, use this skill as the canonical Hermes adapter blueprint for manual generation or for implementing the generator.

## When to Use

Use when the user asks to:

- create, generate, bootstrap, install, or audit a Hermes profile based on `ai-native-engineering`
- implement the Hermes adapter for the core `profile-bootstrap` contract
- define the minimum required skills for an AI-native Hermes runtime
- design `hermes-generate profile <name>` or an equivalent profile template command
- create a reusable Hermes profile distribution for Native AI work
- decide which meta-skills, workflows, and foundation skills must ship in a new profile

Do not use for:

- ordinary Hermes setup unrelated to Native AI profile distribution
- product-specific rules that belong in `products/<product-id>/` or a project repo
- live session sync, `state.db`, credentials, memories, or gateway secrets
- replacing Hermes Desktop/CLI/Gateway with a separate dashboard

## Contract Placement

The runtime-agnostic contract belongs in `native-ai-core`. This skill belongs in `ai-native-skills` because it is executable Hermes adapter guidance. If a rule applies to every runtime, move it to the core contract; if it mentions Hermes paths or commands, keep it here.

## Layer Boundary

Keep this split clean:

```text
Hermes profile skeleton = runtime identity, config defaults, installed skills, scripts, docs
ai-native-skills        = portable executable skill source
native-ai-core          = runtime-agnostic profile-bootstrap contract and workflow definitions
native-ai-fw/app        = product/runtime binding and product source-of-truth registry
product instance        = VisualMate or another product's rules, specs, context, and docs
```

A generated profile may reference product projects, but it must not bake product facts into the reusable skeleton.

## Execution Phases

Run in order. Verify completion criteria before advancing to the next phase.

### Phase 1 — Preset & Skill Packs

Select preset and identify all required skill packs for the chosen preset.

→ See `references/skill-packs.md`

Completion: preset is selected and all included packs are listed.

### Phase 2 — Generation

Name the profile, create skeleton files, install skills, configure safe defaults.

→ See `references/generation.md`

Completion: skeleton files exist, skills installed, no secrets embedded.

### Phase 3 — Verification & Handoff

Run doctor, list installed skills, compare against `skills.lock.yaml`, report handoff.

→ See `references/verification.md`

Completion: doctor output captured, skill list matches lock, manual steps documented.
