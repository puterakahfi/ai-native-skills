---
name: git-workflow
description: Source control operations — branching, committing, PR/MR submission, and merge. Branch strategy, naming convention, commit format, and protected branch policy are product-defined.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/source-control/git-workflow.contract.yaml
---

# Git Workflow

## The Core Rules

```
Never push directly to a protected branch.
Always branch from the correct base.
Every PR must reference an issue before submit.
```

## Prerequisites

Know these before starting:
- What is the base branch? (product_defined)
- What is the branch naming convention? (product_defined)
- What is the commit message convention? (product_defined)
- What issue/ticket does this work reference?

---

## Operations

### 1. Create Branch

Always create from the correct base branch — never from stale local state.

```bash
git checkout <base-branch>
git pull origin <base-branch>
git checkout -b <branch-name>
```

Branch naming convention is product_defined. Common patterns:
- `feat/<issue-id>-short-description`
- `fix/<issue-id>-short-description`
- `release/sprint-<N>`
- `hotfix/<issue-id>`

---

### 2. Commit

Commit message convention is product_defined. Common patterns:

```bash
# Conventional commits
git commit -m "feat(scope): short description"
git commit -m "fix(scope): short description"

# Issue-referenced
git commit -m "fix: short description [#issue-id]"
```

**Gates:**
- [ ] Message follows declared convention
- [ ] One logical change per commit
- [ ] No secrets or credentials in diff
- [ ] No debug/temporary code committed

---

### 3. Keep Branch Updated

Before submitting, sync with base:

```bash
git fetch origin
git rebase origin/<base-branch>
# or
git merge origin/<base-branch>
```

Resolve conflicts before proceeding. Never submit a PR with unresolved conflicts.

---

### 4. Submit PR / MR

Mechanism is product_defined (GitHub PR, GitLab MR, Gerrit patch, etc).

Checklist before submit:
- [ ] Branch is up to date with base
- [ ] All commits follow convention
- [ ] References issue/ticket
- [ ] No unrelated changes bundled
- [ ] CI/lint passing (if product_defined as required)

---

### 5. After Approval — Merge

Merge strategy is product_defined (merge commit, squash, rebase).

```bash
# via CLI if product allows
git checkout <base-branch>
git merge --no-ff <branch-name>
git push origin <base-branch>

# or via platform (GitHub/GitLab merge button)
```

**Never force push to a shared or protected branch.**

---

## Quick Reference

| Operation | Gate |
|---|---|
| Create branch | From correct base, pulled fresh |
| Commit | Convention followed, no secrets |
| Sync | Rebase/merge before submit |
| Submit | Issue referenced, CI green |
| Merge | Approved, strategy followed |

## Extending This Skill

Product-specific implementations should declare `extends` in their frontmatter:

```yaml
name: arbiter-git-workflow
extends: puterakahfi/ai-native-skills@git-workflow
```

Then override only what's product-specific: base branch, naming convention, issue tracker, merge strategy.
