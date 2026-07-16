---
name: onboarding
description: Bootstrap agent and engineer context for an existing codebase — harvest architecture, entry points, conventions, test commands, and gotchas. Produces AGENTS.md as primary output.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime-agent/onboarding.contract.yaml
  ai-native-skills.related_skills: '[''context-engineering'', ''context-manager'', ''rule-manager'', ''architecture-review'']'
---

# Onboarding

## The Core Rule

```
Read before assuming. Every codebase has surprises.

Onboarding output = AGENTS.md that encodes what you discovered,
so the next agent (or engineer) does not have to rediscover it.
```

---

## When to Use

- First time working in an unfamiliar codebase
- Agent starting work in a new repo
- New engineer joining a team
- After long absence from a codebase
- Before writing the first line of code in a new project

---

## Phase 1: Repository Reconnaissance

Read the obvious first — do not skip:

```bash
# 1. Top-level structure
ls -la

# 2. Existing context files
cat AGENTS.md 2>/dev/null || echo "no AGENTS.md"
cat CLAUDE.md 2>/dev/null || echo "no CLAUDE.md"
cat .cursorrules 2>/dev/null || echo "no cursorrules"
cat README.md | head -100

# 3. Project manifest
cat composer.json 2>/dev/null    # PHP
cat package.json 2>/dev/null     # Node
cat pyproject.toml 2>/dev/null   # Python
cat go.mod 2>/dev/null           # Go
cat Cargo.toml 2>/dev/null       # Rust

# 4. Entry points
ls -la src/ app/ lib/ cmd/ internal/ 2>/dev/null | head -30
```

---

## Phase 2: Architecture Identification

Identify the architecture style from code evidence — do not guess.

```bash
# PHP/Laravel signals
ls app/Http/Controllers/     # MVC
ls app/Domain/               # DDD + hexagonal
ls app/Services/             # service layer
grep -r "interface.*Repository" app/ --include="*.php" | head -5

# Node signals
ls src/routes/ src/controllers/ src/services/ src/domain/ 2>/dev/null

# Framework detection
grep '"laravel/framework"' composer.json
grep '"express"' package.json
grep 'django' requirements.txt
```

**Architecture styles to detect:**

| Signal | Architecture |
|---|---|
| `app/Domain/` + interfaces + adapters | Hexagonal / Ports & Adapters |
| `app/Http/Controllers/` + `app/Models/` | MVC (Laravel) |
| `src/entities/` + `src/usecases/` | Clean Architecture |
| Multiple `docker-compose` services | Microservices |
| Single `docker-compose` | Monolith |

---

## Phase 3: Test Command Discovery

**Verify the test command actually works — do not assume.**

```bash
# Laravel
cat composer.json | grep '"test"'
php artisan test --help 2>/dev/null
./vendor/bin/phpunit --version 2>/dev/null

# Node
cat package.json | grep '"test"'
npm test -- --help 2>/dev/null

# Python
cat pyproject.toml | grep "pytest"
python -m pytest --version 2>/dev/null

# Run once to confirm
php artisan test 2>&1 | tail -5
```

Gate: test command verified working before recording in AGENTS.md.

---

## Phase 4: Convention Extraction

Extract conventions from code — do not infer from docs alone.

```bash
# Branch naming convention
git branch -r | grep -E "feature|fix|release|hotfix" | head -10

# Commit message style
git log --oneline -20

# Namespace/module structure
grep -r "^namespace" app/Domain/ --include="*.php" | head -10

# Code style
cat .editorconfig 2>/dev/null
cat phpcs.xml 2>/dev/null
cat .eslintrc.* 2>/dev/null

# CI pipeline
cat .github/workflows/*.yml 2>/dev/null | grep -A3 "test\|lint\|build" | head -30
```

---

## Phase 5: Gotcha Discovery

Find surprises before they bite. Check:

```bash
# Known issues in existing code
grep -rn "TODO\|FIXME\|HACK\|XXX\|WORKAROUND" src/ app/ --include="*.php" --include="*.ts" | head -20

# Recent bug fixes (signals of recurring problems)
git log --oneline --grep="fix" -20

# Environment dependencies
cat .env.example
cat docker-compose.yml | grep "services:" -A 50

# Special setup steps
cat Makefile 2>/dev/null | head -30
cat scripts/setup.sh 2>/dev/null | head -30
```

---

## Phase 6: Produce AGENTS.md

Output of onboarding = AGENTS.md draft. Template:

```markdown
# AGENTS.md — {Project Name}

## Architecture

Style: {Hexagonal / MVC / Clean / Microservices / Monolith}
Framework: {Laravel 10 / Express 4 / Django 4 / etc}
Language: {PHP 8.2 / Node 20 / Python 3.11}
DB: {MySQL 8 / PostgreSQL 15 / MongoDB}

## Entry Points

- HTTP: {app/Http/Controllers/ or src/routes/}
- CLI: {app/Console/Commands/ or src/cli/}
- Queue consumers: {app/Jobs/ or src/consumers/}

## Test Command

{php artisan test / npm test / pytest}
Run before every commit. Must be green before PR.

## Branch Convention

{feature/<TICKET-ID>-desc / fix/<TICKET-ID>-desc}
Base branch: {release/sprint-N / main / develop}

## Commit Convention

{type(scope): description [TICKET-ID]}

## Key Conventions

- {Extracted from code — not guessed}
- {e.g. "repositories in app/Domain/*/Port/ — interfaces only"}
- {e.g. "value objects in app/Domain/Shared/ValueObject/"}

## Response Contract

Lead with answer. No filler. Code blocks exact.
Verbosity: normal.

## Language Standard

artifact_language: {english}

## Gotchas

- {Discovered from TODOs, git log, or README warnings}
- {e.g. "php8.0-fpm docker container — start with docker start, not compose up"}
- {e.g. "git safe.directory required for /data/www/... — run before any git op"}

## Related Skills

- {architecture-review, systematic-debugging, ...}
```

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
