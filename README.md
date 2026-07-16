# ai-native-skills

Reusable agent skills for AI-native engineering. Works with any agent that supports the [skills.sh](https://skills.sh) standard — Hermes, Claude Code, Cursor, Codex, and more.

## What is AI-native?

AI-native is a software paradigm where AI agents are first-class citizens — not bolted on top, but built into the engineering workflow from the ground up. This repo provides the skills that power that workflow.

```
ai-native-core    → domain contracts and philosophy
ai-native-skills  → agent skills implementing those contracts  ← you are here
ai-native-fw      → app/product adapters
```

## Install

```bash
# Single skill
npx skills add puterakahfi/ai-native-skills@diagram-architect

# Pick from interactive list
npx skills add puterakahfi/ai-native-skills

# All skills, no prompt
npx skills add puterakahfi/ai-native-skills -g -y
```

## Skills

### `native-ai-engineer`
Domain contract architect for AI-native systems — layer placement, runtime boundaries, adapter design, and mapping AI runtimes to abstract ports.

> Use when deciding where something belongs: core, app adapter, skill, product instance, or runtime binding.

```bash
npx skills add puterakahfi/ai-native-skills@native-ai-engineer -g -y
```

---

### `native-ai-runtime-agent`
Runtime agent skill for ai-native-fw product adapters — loads repo context, product bindings, source-of-truth files, workflow rules, and verification policy before execution.

> Use when working inside an ai-native-fw product repository.

```bash
npx skills add puterakahfi/ai-native-skills@native-ai-runtime-agent -g -y
```

---

### `native-ai-runtime-ops`
Ops skill for AI-native runtime hosts — SSH/VPS access, agent profile bootstrap, gateway service setup, project checkout, backup/restore, and session-state safety.

> Use when operating or onboarding a Native AI runtime server.

```bash
npx skills add puterakahfi/ai-native-skills@native-ai-runtime-ops -g -y
```

---

### `master-engineer`
Senior Software Engineer and architect for system design, architecture decisions, design patterns, refactoring strategy, over-engineering checks, and engineering contracts.

> Use when making architecture decisions or reviewing system design.

```bash
npx skills add puterakahfi/ai-native-skills@master-engineer -g -y
```

---

### `master-design`
Senior Product Designer and SaaS UI/UX specialist for product design, wireframes, mockups, interaction contracts, design systems, and SaaS dashboard critique.

> Use when designing product UI, wireframes, or critiquing existing interfaces.

```bash
npx skills add puterakahfi/ai-native-skills@master-design -g -y
```

---

### `diagram-architect`
Turns architecture, workflows, runtime state, contracts, ownership, and decision context into clear diagrams. Produces a renderer-agnostic spec first, then renders via Mermaid, SVG, Excalidraw, or ASCII.

> Use when visualizing any system, contract, or architecture before building.

```bash
npx skills add puterakahfi/ai-native-skills@diagram-architect -g -y
```

---

## Related

- [ai-native-core](https://github.com/puterakahfi/ai-native-core) — domain contracts and philosophy
- [ai-native-fw](https://github.com/puterakahfi/ai-native-fw) — Engineering OS app and product adapters
- [skills.sh](https://skills.sh) — open agent skills ecosystem
