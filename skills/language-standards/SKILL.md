---
name: language-standards
description: Enforces consistent language usage across engineering artifacts — code, commits, PRs, issues, comments, skills, and test cases. The artifact language is product-defined; this skill enforces that the choice is explicit, consistent, and documented.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/governance/language-standards.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Language Standards

## The Core Rule

```
Artifact language      = product_defined (declare it explicitly)
Consistency            = mandatory (one language per artifact type, no mixing)
Team chat language     = product_defined (unconstrained)

This skill does NOT mandate English.
It mandates that your language choice is explicit, consistent, and documented.
```

**Why this matters:** Mixed-language artifacts break search, tooling, and onboarding.
A codebase where half the commits are in English and half in Japanese is worse than either alone.

---

## Step 1: Declare Your Language Standard

Define this in `AGENTS.md` or `engineering-contract.yaml`:

```yaml
language_standard:
  artifact_language: english          # or: japanese, portuguese, indonesian, etc.
  team_communication: unconstrained   # Slack, standup, DMs — any language
  user_facing_copy: localized         # UI strings — per market
  exceptions:
    - artifact: user-facing-error-messages
      language: localized
    - artifact: legal-compliance-docs
      language: product_defined
```

---

## Step 2: Apply Consistently

Once declared, **all** artifacts of that type must use the declared language. No mixing.

### Code identifiers

```php
# declared: english
✅ getUserById(), $userName, class PaymentGateway
❌ getDapatkanUserById(), $namaPengguna

# declared: portuguese
✅ obterUsuarioPorId(), $nomeUsuario
❌ getUserById() mixed with obterUsuario()
```

### Commit messages

```bash
# declared: english
✅ fix(auth): resolve session expiry not clearing cookie [FS-142]
❌ fix: perbaiki bug di halaman login

# declared: indonesian
✅ fix(auth): perbaiki sesi yang tidak terhapus saat expired [FS-142]
❌ fix: fix session bug  ← mixing
```

### PR title & description

Must match declared language. No half-translated PRs.

```markdown
# declared: english — correct
feat(checkout): add promo code validation [RWO-88]

# declared: english — wrong (mixed)
feat: tambah promo code validation [RWO-88]
```

### Code comments

```php
# declared: english
✅ // validate ownership before update — prevents IDOR
❌ // validasi kepemilikan dulu

# declared: indonesian  
✅ // validasi kepemilikan sebelum update — mencegah IDOR
❌ // validate ownership before update ← mixing
```

### Skill & test content

Skill SKILL.md, test triggers, and quality gates must match the declared artifact language.

```yaml
# declared: english
trigger: "Audit this design — what is missing?"  ✅
trigger: "Audit design ini — apa yang kurang?"   ❌

# declared: indonesian
trigger: "Audit design ini — apa yang kurang?"   ✅
trigger: "Audit this design — what is missing?"  ❌
```

---

## Step 3: Commit Message Format

Regardless of language, commit messages must follow the structured format:

```
type(scope): description [TICKET-ID]
```

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

**Type prefixes are always English** — they are part of the Conventional Commits spec and parsed by tooling regardless of declared artifact language.

---

## Enforcement Checklist

Before committing:
- [ ] Language standard declared in `AGENTS.md` or engineering contract?
- [ ] All identifiers consistent with declared language?
- [ ] All code comments consistent?
- [ ] Commit message follows `type(scope): description` format?

Before merging PR:
- [ ] PR title and description in declared language?
- [ ] No mixed-language artifacts in the diff?

Before publishing skill:
- [ ] SKILL.md language matches declared standard?
- [ ] Test triggers in declared language?

---

## Common Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| No language declaration | No baseline to enforce against |
| Half commits in English, half in native language | Mixed → unsearchable, inconsistent |
| Code in English, comments in native language | Split-brain codebase |
| Language standard declared but not written down | Implicit conventions don't survive team changes |
| Type prefix (`feat:`, `fix:`) translated | Breaks tooling that parses Conventional Commits |

---

## Arbiter Default

Arbiter projects (`facility-scheduler`, `rwo`) use:

```yaml
language_standard:
  artifact_language: english
  team_communication: unconstrained
  user_facing_copy: localized
```

This is an Arbiter-level decision — not a universal mandate from this skill.
