---
name: incident-response
description: Structured incident lifecycle and blameless postmortem — detect, triage, mitigate, resolve, postmortem, prevent. 5 Whys to systemic cause, action items with owner and deadline, prevention at class level.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/runtime-ops/incident-response.contract.yaml
related_skills: [systematic-debugging, observability-design, deployment-workflow, adr]
---

# Incident Response

## The Core Rule

```
Mitigation first. Root cause second.

Wrong order:
  Prod is down → find root cause → fix → restore service
  (users suffering while engineers debug)

Right order:
  Prod is down → mitigate (restore service) → root cause → postmortem → prevent
```

---

## Severity Levels

| Severity | Impact | Response Time | Example |
|---|---|---|---|
| SEV-1 | Full service down, all users affected | Immediate | Checkout broken, no orders possible |
| SEV-2 | Partial outage, major feature down | < 15 min | Payments failing for 30% of users |
| SEV-3 | Degraded performance, workaround exists | < 1 hour | Reports slow, manual export works |
| SEV-4 | Minor issue, minimal user impact | Next business day | Cosmetic bug, edge case |

---

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

---

## Phase 4: Resolve & Verify

```
Resolution criteria:
  - Error rate back to baseline
  - Latency back to baseline
  - All affected users can complete their flows
  - No data corruption confirmed

Verification:
  - Monitor dashboards for 30 minutes post-mitigation
  - Smoke test critical paths
  - Confirm with on-call that alerts cleared

Declare resolved:
  "SEV-2 resolved — 2026-07-16 11:47 UTC
   Duration: 1h 15m
   Affected: ~30% of payment attempts
   Mitigation: rolled back deploy abc123
   Postmortem scheduled: 2026-07-17 14:00 UTC"
```

---

## Phase 5: Postmortem (Blameless)

Write within 48 hours while memory is fresh.

### Template

```markdown
# Postmortem — {Incident Title}

**Date:** YYYY-MM-DD
**Severity:** SEV-N
**Duration:** Xh Ym
**Author:** {name}
**Reviewers:** {names}

## Summary

One paragraph. What happened, what was the impact, how was it resolved.

## Timeline

| Time (UTC) | Event |
|---|---|
| 10:32 | Alert fired — payment error rate > 5% |
| 10:35 | Incident declared SEV-2, @kahfi as IC |
| 10:40 | Triage complete — payment service OOM after deploy |
| 10:55 | Rollback initiated |
| 11:02 | Error rate returning to baseline |
| 11:47 | Incident resolved |

## Root Cause (5 Whys)

Why did payments fail?
→ Payment service ran out of memory

Why did it run out of memory?
→ New feature loaded entire transaction history into memory

Why was transaction history loaded into memory?
→ Developer used `->get()` instead of `->chunk()` on unbounded query

Why did this pass review?
→ Code review did not catch unbounded query — no gate for this

Why is there no gate for unbounded queries?
→ architecture-review checklist does not include query complexity check
  [SYSTEMIC CAUSE — stop here]

## What Went Well

- Alert fired within 2 minutes of degradation
- Rollback completed in 7 minutes
- Clear communication in #incident channel

## Contributing Factors

- No load testing with production-scale data
- Unbounded query not caught in code review
- No query complexity gate in CI

## Action Items

| Action | Owner | Deadline | Priority |
|---|---|---|---|
| Add unbounded query detection to architecture-review | @kahfi | 2026-07-23 | P1 |
| Add query complexity check to CI pipeline | @team | 2026-07-30 | P1 |
| Add load test with prod-scale data to staging pipeline | @devops | 2026-08-06 | P2 |

## Prevention

**Class of problem:** Unbounded database queries that pass code review
**Prevention:** Architecture review gate + CI query analysis — catches class, not just this instance
```

---

## 5 Whys — Rules

```
✅ Stop at systemic/process cause — not human error
✅ Each "why" must be a factual statement, not an assumption
✅ Blameless — never name a person as root cause

❌ Wrong final answer: "Developer made a mistake"
   → Every system that can break from one mistake is fragile by design

✅ Right final answer: "No gate existed to catch unbounded queries at review time"
   → Fix the gate, not the person
```

---

## Incident Response Checklist

During incident:
- [ ] Severity declared?
- [ ] Incident commander assigned?
- [ ] Blast radius known before fix attempted?
- [ ] Mitigation attempted before root cause investigation?
- [ ] Status updates every 15 minutes?
- [ ] Resolved criteria confirmed (not just "feels better")?

Postmortem:
- [ ] Written within 48 hours?
- [ ] Timeline reconstructed from logs/alerts (not memory)?
- [ ] 5 Whys reaches systemic cause?
- [ ] Blameless — no individual named as root cause?
- [ ] What went well documented?
- [ ] Action items have owner + deadline?
- [ ] Prevention addresses class of problem, not just this instance?
