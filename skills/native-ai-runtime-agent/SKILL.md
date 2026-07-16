---
name: native-ai-runtime-agent
description: Runtime agent skill for ai-native-fw product adapters — loads repo context, product bindings, source-of-truth files, workflow rules, and verification policy before execution.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/runtime-agent/native-ai-runtime-agent.contract.yaml
---

# Native AI Runtime Agent

## Overview

Use this skill to operate Hermes as the runtime adapter for `native-ai-fw`.

The important separation is:

```text
Hermes Agent     = runtime, dashboard, tool execution surface
native-ai-core   = public core/domain contracts, workflows, rules, methodology skills, philosophy
native-ai-app/fw = app/product/runtime adapter implementing native-ai-core contracts; public or private by implementer choice
native-ai-skills = runtime skill adapters implementing native-ai-core skill contracts
Product instance = product-specific source of truth, e.g. VisualMate
```

Do not turn `native-ai-fw` into a replacement Hermes dashboard. Use Hermes Desktop/CLI/Gateway as the execution surface. Use `native-ai-fw`/app adapters to bind product context, runtime policy, core contracts, and installed runtime skills.

## When to Use

Use this skill when:

- The user works in `/data/puterakahfi/project/native-ai-fw`.
- The task mentions Native AI Framework, VisualMate, runtime binding, product instance, product contract, workflow, or Hermes runtime adapter.
- The user asks Hermes to plan, design, engineer, verify, deploy, review, or capture learning for a product instance.
- The user asks how to package or share a Native AI Hermes profile across devices, e.g. an `ai-native-engineering` profile distribution.
- You need to make Hermes behavior repeatable rather than relying only on chat context.

Do not use this skill for:

- Generic Hermes configuration not related to `native-ai-fw` or product runtime binding.
- One-off code edits in unrelated repositories.
- Building a separate native-ai-fw dashboard unless the user explicitly asks for platform UI work.

## Runtime Boot Sequence

Before product work, do this compact boot sequence:

1. **Identify product id.**
   - Use explicit user input if present.
   - Default to `visualmate` only when the task clearly targets VisualMate.
   - Completion: product id is known or you ask the user only if the task cannot proceed without it.

2. **Load repo context.**
   - Read `.hermes.md` if current session context may be stale.
   - Completion: core/product/runtime boundary is clear.

3. **Load product config.**
   - Read `products/<product-id>/project.config.yaml`.
   - Follow its source-of-truth files relevant to the task.
   - Completion: product authority files for the task are known.

4. **Load runtime binding.**
   - Read `products/<product-id>/runtime.binding.yaml`.
   - Confirm `runtime_binding.runtime` is `hermes`.
   - Resolve `framework.core.local_path` for core contracts and workflows.
   - Resolve `hermes.skills.runtime_adapters` for executable runtime skills; `installed_as` should match an entry in `hermes.skills.hermes_profile_skills`.
   - Completion: profile, toolsets, workflows, approval policy, verification policy, learning policy, core source, and runtime skill adapter sources are known.

5. **Validate when changing or relying on binding.**
   - For VisualMate, run:
     ```bash
     pnpm --filter @native-ai-fw/console build
     node platform/apps/console/dist/index.js validate-config visualmate
     ```
   - Completion: command reports a valid binding, or the validation errors are fixed/reported.

6. **Select the smallest workflow and skills.**
   - Use product-specific workflows when listed in the binding; otherwise use framework workflows.
   - Load relevant Hermes skills only when they match the task.
   - Completion: execution path is clear and not over-scoped.

7. **Execute with evidence.**
   - Inspect before editing.
   - Use file/terminal/browser tools according to the binding.
   - Respect approval gates for destructive, dependency, architecture, database, deployment, and public publishing actions.
   - Completion: requested artifact or change exists and has been verified.

8. **Report and learn.**
   - Report actual command/browser/tool output.
   - Put reusable procedures into skills; stable product facts into the right product docs or memory; task progress stays in session/kanban.
   - Completion: result is traceable and future-useful knowledge is stored in the right layer.

## Lean Scope Rule

Default to the lean Hermes-first architecture:

```text
Hermes does the operating.
native-ai-fw defines the operating contract.
VisualMate provides product truth.
```

Avoid these unless explicitly requested:

- A separate native-ai-fw runtime dashboard.
- A second task runner duplicating Hermes sessions/cron/gateway.
- Heavy SDK abstractions before the YAML/docs/skills are being used repeatedly.
- Product OS UI work when the user is still clarifying runtime behavior.

## File Responsibilities

| File or folder | Responsibility |
|---|---|
| `.hermes.md` | Hermes-specific repo entrypoint and boundary rules |
| `docs/hermes-runtime-agent.md` | Runtime operating protocol |
| `docs/hermes-runtime-binding.md` | Binding contract explanation |
| `core/` | Vendored/synced `native-ai-core` contract source |
| `products/<id>/project.config.yaml` | Product source-of-truth registry |
| `products/<id>/runtime.binding.yaml` | Product-to-Hermes runtime policy, core source, and runtime skill adapter declarations |
| `context-packs/<id>.yaml` | Condensed product context |
| `products/<id>/...` | Product-specific contracts, workflows, rules, and skills |
| `core/workflows/`, `core/rules/`, `core/skills/` | Product-agnostic core methodology artifacts |
| `hermes.skills.runtime_adapters` | Source-of-truth links to runtime skill implementations such as `native-ai-skills` |
| Hermes profile skills | Runtime-executable skills installed in Hermes |
| Hermes profile distribution repo | Private reusable profile shape (`distribution.yaml`, `SOUL.md`, config defaults, skills, MCP/cron placeholders); see `references/hermes-profile-distribution-sync.md` |

## Verification Checklist

- [ ] Product id identified.
- [ ] `.hermes.md` and `runtime.binding.yaml` were used when task is product/runtime scoped.
- [ ] Product config/source-of-truth files were read before broad changes.
- [ ] Runtime binding validation was run when binding/schema/config changed.
- [ ] Relevant commands/tests/lint/typecheck/browser checks were executed before claiming done.
- [ ] No native-ai-fw web/dashboard expansion was introduced unless explicitly requested.
- [ ] Core/product/runtime boundaries stayed clean.
- [ ] Reusable learning was captured as skill/doc/runtime binding rather than chat-only context.

## Common Pitfalls

1. **Assuming Hermes automatically knows every YAML file.** It only knows what is loaded into the session context or project instructions. Read or validate the binding when it matters.

2. **Turning runtime binding into a platform project.** Keep it as a small policy contract until repeated use proves a need for more automation.

3. **Committing VisualMate-specific behavior into core.** Put VisualMate facts under `products/visualmate/` or `context-packs/visualmate.yaml`.

4. **Skipping verification because the change is documentation-like.** YAML and CLI wiring still need parse/build checks. If the verification gate says no canonical command was detected for a binding/template/snippet change, create a focused `/tmp/hermes-verify-*` ad-hoc verifier, run it, remove it, and label the result as ad-hoc rather than suite green. See `references/ad-hoc-runtime-binding-verification.md`.

5. **Replacing Hermes dashboard with native-ai-fw UI.** The Hermes app is already the runtime surface; native-ai-fw should guide it, not duplicate it.

6. **Confusing visibility with responsibility.** App adapters implement core contracts and may be public or private. Do not describe `native-ai-app` as inherently private; classify artifacts by core contract, app adapter, product context, or runtime skill adapter.

7. **Forgetting the skills repo leg.** Core skill contracts belong in `native-ai-core`; executable Hermes `SKILL.md` implementations belong in `native-ai-skills` or the Hermes profile. App runtime binding should declare both the core contract path and runtime adapter source/compat manifest.

8. **Subtree sync ambiguity.** If `git subtree pull --prefix core ... --squash` is unreliable after a fresh split, prefer preserving the clean app working tree first, then manually sync the small vendored docs/contracts and commit the adapter repo with clear references rather than blocking the runtime binding update.

9. **Treating profile distribution as session sync.** A Hermes profile distribution repo should sync reusable shape (`distribution.yaml`, `SOUL.md`, config defaults, skills, MCP/cron placeholders), not live `state.db`, `.env`, `auth.json`, sessions, or memories. For same-chat-on-every-device behavior, use a canonical Hermes runtime/profile and connect devices as clients. See `references/hermes-profile-distribution-sync.md`.
