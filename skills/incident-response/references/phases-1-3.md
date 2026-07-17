# Incident Response — Phases 1–3

## Phase 1: Detect & Declare

```
Signal sources:
  - Alert fired (observability-design)
  - User report
  - On-call notification
  - Monitoring dashboard

Declare the incident:
  "SEV-2 incident declared — Payments failing for ~30% of users
   Incident commander: @kahfi
   Bridge: #incident-2026-07-16-payments
   Started: 2026-07-16 10:32 UTC"

Role assignment:
  Incident Commander  — coordinates, owns timeline, makes decisions
  Technical Lead      — investigates, implements fixes
  Comms Lead          — updates stakeholders (optional for SEV-3/4)
```

---

## Phase 2: Triage

**Do not fix yet. Understand scope first.**

```
Triage questions (5 minutes max):
  1. What is broken? (feature, service, data)
  2. Who is affected? (% of users, which regions, which plans)
  3. Since when? (from monitoring, git log, deploy history)
  4. What changed recently? (deploy, config, infrastructure)
  5. Can we rollback? (last known good state)

Output: Severity confirmed, blast radius known, rollback feasibility known
```

---

## Phase 3: Mitigate

Restore service first — root cause later.

```
Mitigation options (in order of preference):
  1. Rollback last deploy  ← fastest if deploy caused it
  2. Feature flag off      ← if feature flagged
  3. Redirect traffic      ← if one instance/region affected
  4. Restart service       ← if state corruption
  5. Scale up              ← if resource exhaustion
  6. Apply hotfix          ← last resort, only if above fail

Command:
  git revert <deploy-commit> --no-edit
  git push origin main
  # or: trigger rollback in CI/CD

Status update every 15 minutes during active incident.
```
