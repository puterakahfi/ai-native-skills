---
name: context-engineering
description: Institutional context authoring and curation — write AGENTS.md, .cursorrules, and context packs that encode architecture constraints, guardrails, and domain knowledge into the AI workspace.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/context-management/context-engineering.contract.yaml
---

# Context Engineering

## The Core Distinction

```
context-manager    → RESOLVING context before agent runs (what exists?)
context-engineering → AUTHORING context that persists across all agent runs (what should exist?)
```

Context engineering = strategic curation of institutional knowledge injected into the AI workspace.
Bad context = agents that drift, hallucinate conventions, violate architecture.

## When to Use

- Setting up a new repo or product for AI agents
- AGENTS.md is missing, stale, or too vague
- Agents keep making the same wrong decisions
- Onboarding a new agent to an existing codebase
- After a post-mortem where agent violated architecture/rules
- Auditing existing context files for gaps or conflicts

---

## 1. Context Layers

Context lives at multiple levels — author all that apply:

```
repo-level:      AGENTS.md, .cursorrules, CLAUDE.md
product-level:   engineering-contract.yaml, ui-design-system-contract.yaml
task-level:      context pack (built by context-manager per task)
```

**Priority order (highest to lowest):**
1. Task-level context pack
2. Repo-level AGENTS.md
3. Product-level engineering contract

---

## 2. AGENTS.md Authoring

### Structure

```markdown
# AGENTS.md

## Source of Truth
- Engineering contract: <path>
- Design contract: <path>

## Architecture Constraints
- Style: <hexagonal | layered | etc>
- Stack: <explicit list from engineering-contract>
- Patterns: <e.g. "all domain logic in /domain, no framework imports">

## Hard Rules (never violate)
- Never push directly to main or release/* branches
- Never hardcode secrets, API keys, or credentials
- Never add dependencies without updating engineering-contract.yaml
- Never generate UI without consulting design contract
- Never write raw SQL — use ORM or query builder

## Workflow Rules
- Always branch from release/sprint-<N>
- Always reference issue tracker ID in commits
- Always run tests before opening PR

## Agent Boundaries (must escalate to human)
- Architecture decisions beyond current contract
- Security-sensitive code paths
- Breaking changes to public API contracts
- Any change that affects >3 modules simultaneously

## Out of Scope (agent must not touch)
- <explicit list of files/dirs agent must not modify>
```

### Quality Gates for AGENTS.md

- [ ] Architecture style explicitly stated?
- [ ] Hard rules specific — not "write clean code"?
- [ ] Agent boundary rules present — what must escalate to human?
- [ ] Out-of-scope files/dirs explicit?
- [ ] Traces to engineering contract?
- [ ] No duplicate rules that conflict with each other?

---

## 3. .cursorrules / per-tool context

For tool-specific context (Cursor, Windsurf, etc):

```
# Product Context
Architecture: <style>
Stack: <from engineering-contract>
Key patterns: <2-3 bullet points>

# Hard Rules
- No direct commits to main
- No new dependencies without contract update
- No hardcoded secrets
- No raw SQL

# Agent Boundaries
- Escalate: architecture decisions, security paths, breaking changes

# Workflow
- Branch from release/sprint-<N>
- Commit: type(scope): description [JIRA-ID]
- PR required for all changes
```

---

## 4. Context Gap Analysis

Audit existing context files:

```
CONTEXT GAP REPORT
──────────────────
Checked: AGENTS.md, .cursorrules

Missing:
  [ ] Architecture style not stated
  [ ] No hard rules for secret handling
  [ ] Agent boundaries not defined
  [ ] No out-of-scope file list
  [ ] Engineering contract not referenced

Conflicts:
  [ ] Rule A says X, engineering contract says Y
  [ ] .cursorrules duplicates AGENTS.md with different values

Vague (must rewrite):
  [ ] "Write clean, maintainable code" → too vague, remove
  [ ] "Follow best practices" → not enforceable, remove
```

---

## 5. Context Freshness

Context goes stale when:
- Engineering contract updated but AGENTS.md not
- New dependency added but not reflected in stack rules
- Team convention changed but cursorrules unchanged
- Post-mortem identified a gap but context not updated

**Trigger a context review when:**
- Any change to `engineering-contract.yaml`
- Any new dependency or architectural pattern introduced
- Agent repeatedly makes the same incorrect decision
- Post-mortem identifies a rule gap

---

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| "Follow best practices" as a rule | Not specific, not enforceable |
| AGENTS.md without architecture section | Agent has no architecture contract |
| No agent boundary rules | Agent makes architecture decisions alone |
| Context written once, never updated | Stale context = worse than no context |
| Duplicate rules across files with different values | Agent gets contradictory instructions |
| "Be careful with production" as a rule | Not actionable — write the actual constraint |
