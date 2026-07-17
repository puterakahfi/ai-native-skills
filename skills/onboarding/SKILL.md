---
name: onboarding
description: Bootstrap agent and engineer context for an existing codebase — harvest architecture, entry points, conventions, test commands, and gotchas. Produces AGENTS.md as primary output.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime-agent/onboarding.contract.yaml
  ai-native-skills.related_skills: "['context-engineering', 'context-manager', 'rule-manager', 'architecture-review']"
---

# Onboarding

## The Core Rule

```
Read before assuming. Every codebase has surprises.

Onboarding output = AGENTS.md that encodes what you discovered,
so the next agent (or engineer) does not have to rediscover it.
```

---

## HARD RULES

- **Read before writing** — never write AGENTS.md before completing all phases
- **Never assume conventions** — extract from code evidence, not intuition
- **Produce AGENTS.md as final output** — that is the deliverable of onboarding

---

## When to Use

- First time working in an unfamiliar codebase
- Agent starting work in a new repo
- New engineer joining a team
- After long absence from a codebase
- Before writing the first line of code in a new project

---

## Phase Overview

| Phase | Name | Load reference |
|---|---|---|
| 1 | Repository Reconnaissance | `references/phases-1-3.md` |
| 2 | Architecture Identification | `references/phases-1-3.md` |
| 3 | Test Command Discovery | `references/phases-1-3.md` |
| 4 | Convention Extraction | `references/phases-4-6.md` |
| 5 | Gotcha Discovery | `references/phases-4-6.md` |
| 6 | Produce AGENTS.md | `references/phases-4-6.md` |

**Always load references before executing phases.**

Load phases 1–3: `skill_view(name='onboarding', file_path='references/phases-1-3.md')`
Load phases 4–6: `skill_view(name='onboarding', file_path='references/phases-4-6.md')`

---

## Onboarding Checklist

- [ ] Top-level structure read?
- [ ] Existing AGENTS.md/CLAUDE.md checked?
- [ ] Architecture style identified from code evidence?
- [ ] Framework and language versions confirmed from manifest?
- [ ] Test command verified working?
- [ ] Branch and commit conventions extracted from git log?
- [ ] Gotchas documented (TODOs, recent fixes, setup quirks)?
- [ ] AGENTS.md draft produced?
- [ ] No assumptions made without code evidence?
