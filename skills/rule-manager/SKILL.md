---
name: rule-manager
description: Rule authoring, validation, and enforcement skill — write AGENTS.md, .cursorrules, and per-product rules that constrain AI agents. Ensures rules are specific, traceable, and non-conflicting.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/rule-management/rule-manager.contract.yaml
---

# Rule Manager

## The Core Distinction

```
Rules  = constraints   — what agents MUST NOT do
Skills = procedures    — HOW agents should do something
```

Rules live in `AGENTS.md`, `.cursorrules`, or product rule files.
Skills live in `SKILL.md` files.

**Do not put procedures in rules. Do not put constraints in skills.**

## When to Use

- Writing or updating `AGENTS.md` for a product
- Writing `.cursorrules` for a repo
- Auditing existing rules for conflicts or gaps
- Onboarding a new agent to a product context
- When an agent keeps making the wrong decision — write a rule, not a prompt

---

## 1. Rule Authoring

Good rules are **specific**, **actionable**, and **testable**:

```markdown
# Good rules
- Never push directly to main or release/* branches
- Never hardcode secrets or API keys in source files
- Never add a npm package without updating engineering-contract.yaml
- Always reference a Jira ticket ID in commit messages

# Bad rules (aspirational, not enforceable)
- Write clean code
- Be careful with production
- Follow best practices
- Think before committing
```

**Gate:** Every rule must state what must NOT happen, or what MUST happen — not what "should" happen.

---

## 2. Rule Structure

### AGENTS.md format

```markdown
# AGENTS.md

## Source of Truth
- Engineering contract: products/<product>/engineering-contract.yaml
- Design contract: products/<product>/ui-design-system-contract.yaml

## Hard Rules (never violate)
- Never push to protected branches directly
- Never hardcode credentials
- Never generate UI without consulting design contract
- Never add dependencies without engineering contract update

## Workflow Rules
- Always branch from release/sprint-<N> for bugfix and feature work
- Always reference issue tracker ID in commits
- Always run test suite before opening PR

## Scope Rules
- Do not modify files outside the assigned task scope
- Do not refactor code unrelated to the current task
- Do not create new abstractions without an ADR

## Agent Boundaries
- Do not make architecture decisions — raise a flag instead
- Do not approve your own generated output
- Do not merge without human approval
```

### .cursorrules / per-tool format

```
# Engineering Contract
Stack: <from engineering-contract.yaml>
Architecture: <style from contract>

# Hard Rules
- No direct commits to main
- No new dependencies without contract update
- No hardcoded secrets

# Workflow
- Branch from release/sprint-<N>
- Commit format: type(scope): description [JIRA-ID]
```

---

## 3. Rule Validation Checklist

Before finalizing any rule document:

- [ ] Every rule is specific — not "be careful," "follow standards"?
- [ ] Every rule is traceable to engineering contract or product decision?
- [ ] No rule duplicates what's already in engineering contract?
- [ ] No conflicting rules in the same scope?
- [ ] Hard rules separated from workflow rules?
- [ ] Agent boundary rules explicit — what agent must NOT decide alone?
- [ ] Rules have been reviewed by product owner or tech lead?

---

## 4. Rule Gap Analysis

When auditing existing rules, check for gaps:

```
Missing rule categories:
- [ ] Source control boundaries
- [ ] Secret handling
- [ ] Dependency management
- [ ] Architecture decision authority
- [ ] Scope boundaries per task
- [ ] Approval requirements before merge/deploy
- [ ] Design system compliance
```

For each gap → write a rule or confirm it's covered by engineering contract.

---

## 5. Rule Update Flow

When updating rules:
1. State what changed and why
2. Check for conflicts with existing rules
3. Update both AGENTS.md and any tool-specific rule files
4. Flag for review if it affects agent behavior significantly

**Gate:** Rule change requires review — rules are governance artifacts, not casual notes.

---

## Common Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| "Write good code" as a rule | Not specific, not enforceable |
| Rules that duplicate engineering contract | Creates drift when contract changes |
| No scope boundary rules | Agent modifies files outside task scope |
| Missing approval rule | Agent self-approves generated output |
| Procedures written as rules | Belongs in a skill, not a rule |
| Rules never reviewed | Governance without oversight |
