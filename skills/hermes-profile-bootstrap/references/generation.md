# Generation Reference

## Generation Procedure

Run phases in order. Verify completion before advancing.

1. **Name the profile.** Accept `<profile-name>` from the user or command. Completion: name is lowercase/hyphenated and safe as a directory name.
2. **Select preset.** Default to `engineering`. Completion: selected preset and included skill packs are listed.
3. **Create profile.** Prefer Hermes CLI when available:
   ```bash
   hermes profile create <profile-name>
   ```
   Completion: `hermes profile show <profile-name>` succeeds, or the generator reports the exact blocker.
4. **Write skeleton files.** Create `SOUL.md`, `skills.lock.yaml`, `docs/profile.md`, `docs/skill-preset.md`, and scripts. Completion: files exist and contain no secrets or live state.
5. **Install skills.** Use `npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y` or the profile's supported install mechanism. Completion: every selected skill is installed or the missing list is explicit.
6. **Configure safe defaults.** Set only reusable profile defaults: toolset preferences, display/language defaults, and verification policy. Completion: no API keys, tokens, product secrets, or local-only paths are embedded.

---

## Profile Skeleton

A generated profile should produce this shape under `~/.hermes/profiles/<profile-name>/`:

```text
~/.hermes/profiles/<profile-name>/
├── SOUL.md                         # runtime identity and operating principles
├── config.yaml                     # safe defaults only; no secrets
├── skills.lock.yaml                # chosen skill preset and source pins
├── scripts/
│   ├── install-skills.sh           # installs declared skills
│   └── verify-profile.sh           # validates profile health
├── docs/
│   ├── profile.md                  # what this profile is for
│   └── skill-preset.md             # installed packs and rationale
└── .gitignore                      # excludes state/secrets/logs if this is a distribution repo
```

Never include these in a reusable profile distribution or generated template:

```text
state.db
state.db-wal
state.db-shm
sessions/
memories/
cron/
auth.json
.env
.env.*
logs/
cache/
secrets/
tokens/
credentials/
```

Hermes itself may create a local `.env` inside a live profile during `hermes profile create`; keep that file local, uncommitted, and free of template-owned secrets.

---

## `skills.lock.yaml` Shape

Use a simple declarative lock file so the profile is reproducible:

```yaml
profile: ai-native-engineering
preset: engineering
source: puterakahfi/ai-native-skills
skills:
  meta:
    - workflow-router
    - role-switcher
  workflows:
    - spec-workflow
    - product-development-workflow
    - new-feature-workflow
    - bugfix-workflow
    - code-review-workflow
    - deployment-workflow
  native_ai:
    - native-ai-engineer
    - native-ai-runtime-agent
    - native-ai-runtime-ops
    - context-engineering
    - context-manager
    - rule-manager
    - response-contract
    - model-selection
    - business-value-alignment
    - experiment-design
  engineering_quality:
    - systematic-debugging
    - test-driven-development
    - refactoring
    - architecture-review
    - security-review
    - threat-modeling
    - git-workflow
    - plan
    - spike
    - skill-eval
  architecture:
    - domain-driven-design
    - ports-and-adapters
    - api-contract
    - event-driven-design
    - service-design
    - systems-thinking
    - adr
verification:
  expected_total: 76
```

Generators may add version pins later, but the initial skeleton should stay readable and editable.

---

## SOUL.md Baseline

Generated `SOUL.md` should be short and profile-level:

```markdown
# AI Native Engineering Profile

You are operating as an AI-native engineering runtime.

Default behavior:
- Route ambiguous work through `workflow-router` or `role-switcher` before execution.
- Keep Native AI boundaries explicit: core, app adapter, runtime binding, product instance, profile.
- Use workflows for lifecycle tasks and skills for capability-specific gates.
- Verify with real tool output before claiming completion.
- Store durable reusable procedures as skills; keep task progress out of memory.

Do not store secrets, live session state, product-specific facts, or credentials in this profile distribution.
```

---

## Implementation Notes for `hermes-generate profile`

A future generator should:

- support `--preset minimal|engineering|product|runtime-ops|full`
- support `--dry-run` and print planned file writes and skill installs
- refuse to overwrite an existing profile unless `--force` is explicit
- write idempotent files where possible
- separate stdout data from stderr diagnostics
- accept `--profile-dir` for testing without touching real `~/.hermes`
- produce a final JSON summary for automation

Minimum JSON summary:

```json
{
  "profile": "my-profile",
  "preset": "engineering",
  "path": "~/.hermes/profiles/my-profile",
  "skills_requested": 35,
  "skills_installed": 35,
  "verification": "passed"
}
```
