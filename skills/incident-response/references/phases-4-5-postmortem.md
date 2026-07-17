# Incident Response — Phases 4–5 & Postmortem

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
