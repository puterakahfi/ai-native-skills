---
name: git-workflow
description: Source control operations — branching, committing, PR/MR submission, and merge. Branch strategy, naming convention, commit format, and protected branch policy are product-defined.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "delivery-work-breakdown decision-provenance"
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["delivery-work-breakdown","new-feature-workflow","product-development-workflow"]'
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/git-workflow.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Git Workflow

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/engineering/git-workflow.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- intent
allowed_outputs:
- branch_created
- commits_authored
- pr_or_mr_opened
- merge_executed
- conflict_report
quality_gates:
- branch_must_be_created_from_correct_base
- commit_message_must_follow_convention
- no_direct_push_to_protected_branch
- pr_must_reference_issue_before_submit
- conflicts_must_be_resolved_before_merge
- no_force_push_to_shared_branch
```

Treat intent as the operation request and report actual execution state. Do not claim branch creation, commits, PR opening, merge, or conflict resolution unless the corresponding action was completed and evidenced.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


## The Core Rules

```
Never push directly to a protected branch.
Always branch from the correct approved base.
Never infer base or PR target from the repository default.
Consume `delivery-work-breakdown` for product/feature work.
Every PR must reference an issue before submit.
```

## Prerequisites

Know these before starting:
- What is the governing release unit and parent work item?
- What topology record approved this operation?
- What is the explicit base branch? (product_defined)
- What is the explicit PR target? (product_defined)
- What is the branch naming convention? (product_defined)
- What is the commit message convention? (product_defined)
- What issue/ticket does this work reference?

---

## Operations

### 1. Create Branch

Always create from the correct approved base branch — never from stale local state or a guessed default. Epic children start from the approved integration branch.

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
- [ ] Release unit and parent traceability are explicit
- [ ] Base branch and PR target match the approved topology
- [ ] Epic children do not bypass the integration branch
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
| Create branch | From explicit approved base, pulled fresh |
| Choose PR target | Matches the approved release unit and topology |
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
