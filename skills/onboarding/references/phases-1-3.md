# Onboarding — Phases 1–3

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
