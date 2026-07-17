# Onboarding — Phases 4–6

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
