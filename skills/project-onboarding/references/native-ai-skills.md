# native-ai-skills — Project Context

## Identity
- **Hermes Project ID**: p_2a02a913 (slug: native-ai-skills)
- **GitHub**: https://github.com/puterakahfi/ai-native-skills
- **Local path**: /data/www/ai-native-skills
- **Remote**: git@github-arbiter:puterakahfi/ai-native-skills.git
- **Default branch**: main

## Tech stack
- YAML + Markdown (skill definitions, schemas, contracts)
- Python scripts (fleet tooling, validators)
- Shell scripts (hermes-fleet runner)
- JSON (fixtures, presets, capability maps)
- No framework — pure file-based skill package system

## Repo structure
```
catalog/        — skill catalog index
compat/         — compatibility shims
contracts/      — auto-routing contracts and fixtures
  fixtures/auto-routing/  — positive-*.yaml / negative-*.yaml
docs/           — capability discovery, skill packs, taxonomy
examples/
packs/          — installable skill packs
schemas/        — JSON schemas per receipt type
  auto-routing/ — 7 receipt schemas (task-routing-plan, worker-receipt, etc.)
scripts/        — fleet bootstrap, model sync, acceptance runners
skills/         — skill source (hermes-agent-fleet-bootstrap, etc.)
tests/
```

## Active epics & issues (as of 2026-07-31)
| # | Title | Status |
|---|---|---|
| #304 | [Epic] Hermes agent auto-routing via durable specialist workers | Open |
| #307 | [Task] Compose workflow and role outputs into auto-routing plans (auto-planner) | Open |
| #308 | [Task] Execute durable specialist worker dispatch | Open |
| #309 | [Task] Review and orchestrator synthesis loop | Open |
| #310 | [Task] Runtime acceptance fixtures + user docs | Open |
| #312 | Auto-routing contract iteration: 7 findings from dogfood run | Open |

## Key recent PRs
- **#311 (merged)**: feat(hermes): auto-routing contract and evidence receipts [#305]

## Notes
- No Jira — GitHub Issues is the tracker
- 102 skills · 13 workflows · 7 meta-skills in catalog
- Fleet profiles: agent-orchestrator, agent-product, agent-architecture, agent-design, agent-frontend, agent-backend, agent-review
