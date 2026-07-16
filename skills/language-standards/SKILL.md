---
name: language-standards
description: Enforces English as the lingua franca for all engineering artifacts — code, commits, PRs, issues, comments, skills, and test cases. Team communication language is product-defined; artifact language is not.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/rule-management/language-standards.contract.yaml
---

# Language Standards

## The Core Rule

```
Team communication language  = product_defined (can be any language)
Engineering artifact language = English, always

Why: artifacts outlive team members, agents, and conversations.
     A commit message in Bahasa Indonesia is unreadable to the next engineer,
     the next agent, and the next tool in the pipeline.
```

---

## What Must Be English

| Artifact | English Required | Example |
|---|---|---|
| Variable / function / class names | ✅ | `getUserById()`, not `getDapatkanUserById()` |
| Code comments | ✅ | `// validate ownership before update` |
| Commit messages | ✅ | `fix: resolve null pointer in checkout flow` |
| PR title & description | ✅ | `feat: add JWT refresh token rotation` |
| Issue / ticket titles | ✅ | `Bug: user balance goes negative after refund` |
| Acceptance criteria | ✅ | `Given a logged-in user, when...` |
| Skill SKILL.md content | ✅ | All skill bodies, descriptions, gates |
| Test case triggers | ✅ | `"Audit this design — what is missing?"` |
| AGENTS.md / .cursorrules | ✅ | All rule content |
| ADR (Architecture Decision Records) | ✅ | Full document |
| API error messages (user-facing) | ⚡ product_defined | May need localization |
| Log messages | ✅ | `logger.error("Payment gateway timeout")` |

## What Can Be Team Language

| Artifact | Language |
|---|---|
| Slack/Teams messages | product_defined |
| Sprint ceremonies (standup, retro) | product_defined |
| Internal wiki pages | product_defined |
| User-facing UI copy | product_defined (localized) |
| Jira ticket comments | product_defined |

---

## Commit Message Standard

Format: `type(scope): short description [TICKET-ID]`

```bash
# ✅ correct
git commit -m "fix(auth): resolve session expiry not clearing cookie [FS-142]"
git commit -m "feat(checkout): add promo code validation [RWO-88]"
git commit -m "refactor(user): extract ownership check to service layer"
git commit -m "docs: update API endpoint reference for v2 payment"

# ❌ wrong — not English
git commit -m "fix: perbaiki bug di halaman login"
git commit -m "feat: tambah fitur promo code"

# ❌ wrong — too vague
git commit -m "fix: bug fix"
git commit -m "update stuff"
git commit -m "changes"
git commit -m "wip"
```

### Commit Types

| Type | Use For |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code restructure without behavior change |
| `test` | Adding or updating tests |
| `docs` | Documentation only |
| `chore` | Build, config, dependency updates |
| `perf` | Performance improvement |
| `revert` | Reverting a previous commit |

---

## PR Title & Description Standard

```markdown
# PR Title
feat(scope): short description [TICKET-ID]

# PR Description template
## What
<!-- What changed and why -->

## How
<!-- How the change was implemented -->

## Testing
<!-- How this was tested -->

## Checklist
- [ ] Tests pass
- [ ] No hardcoded secrets
- [ ] Ticket updated
```

---

## Issue / Ticket Title Standard

```
# ✅ correct
Bug: user balance goes negative after concurrent refund requests
Feat: add bulk export for facility schedules
Chore: upgrade PHP from 8.0 to 8.2

# ❌ wrong
Bug: saldo user jadi minus waktu refund
Feat: tambah fitur export massal
```

---

## Code Comment Standard

```php
// ✅ correct
// Validate ownership before allowing update — prevents IDOR
if ($booking->getUserId() !== $currentUser->getId()) {
    throw new UnauthorizedException();
}

// ❌ wrong
// Validasi kepemilikan dulu sebelum update
if ($booking->getUserId() !== $currentUser->getId()) {
    throw new UnauthorizedException();
}
```

**Rule:** If you can't explain it in English, the code is not clear enough yet.

---

## Skill & Test Case Standard

```yaml
# ✅ correct trigger
trigger: "Audit this design — what is missing or broken?"

# ❌ wrong trigger
trigger: "Audit design ini — apa yang kurang?"
```

All `SKILL.md` content, `quality_gates`, test case `triggers`, `must_contain`, and `must_not_contain` must be in English.

---

## Enforcement Checklist

Before committing:
- [ ] All commit messages in English with correct type prefix?
- [ ] All variable/function/class names in English?
- [ ] All code comments in English?
- [ ] PR title and description in English?
- [ ] No mixed-language code comments?

Before merging PR:
- [ ] Issue/ticket title in English?
- [ ] Acceptance criteria in English?
- [ ] ADR (if any) in English?

Before publishing skill:
- [ ] SKILL.md body in English?
- [ ] All test case triggers in English?
- [ ] Contract quality_gates in English?

---

## Common Anti-Patterns

| Anti-Pattern | Correct |
|---|---|
| `// validasi input dulu` | `// validate input before processing` |
| `fix: perbaiki bug login` | `fix(auth): resolve login redirect loop [FS-99]` |
| `$namaPengguna` | `$userName` |
| Test trigger in Bahasa | Test trigger in English |
| PR description: "sudah fix bugnya" | PR description: "Resolves null pointer in user session cleanup" |
