# Signal Routing and Closure

Load after `maintenance-case` has produced a qualified case record. This reference helps normalize evidence and hand off to the existing governing workflow; it does not select the primary route itself.

## Signal qualification matrix

| Signal | Minimum qualification evidence | Common route input | Required outcome evidence |
|---|---|---|---|
| Active incident | current impact, environment, blast radius, severity authority | `incident-response` | service restored/mitigated, resolution criteria, postmortem actions |
| Non-active defect | deterministic symptom or attributable failure evidence | `bugfix-workflow` | red/green regression, affected suites, actual behavior |
| Security finding | source, affected boundary, severity/confidence, policy | security review plus governing workflow | correction/mitigation evidence and required authority |
| Dependency/platform change | provider notice or verified version/support issue, affected usage | feature/bugfix/spike based on objective | compatibility, tests, migration/rollback evidence |
| Performance regression | baseline, current measurement, environment, threshold | bugfix or feature | measured recovery at the target boundary |
| Reliability risk | failure mode, likelihood/impact evidence, accepted threshold | feature/bugfix/resilience work | resilience test or actual health evidence |
| Cost anomaly | bill/usage source, baseline, attribution, materiality | investigation then feature/bugfix | measured cost outcome and guardrail |
| Data/migration issue | affected data, integrity evidence, scope, recovery constraints | incident, bugfix, or feature | integrity/reconciliation and rollback evidence |
| User/product signal | attributable feedback or metric movement, hypothesis | product validation/experiment | reviewed user/value evidence, not only code delivery |
| Documentation drift | current document and contradictory actual behavior/source | `documentation-assurance` | corrected source plus verification/review |
| Deprecation/removal | supported versions, consumers, authority, timeline | feature/release composition | migration, communication, compatibility, removal evidence |
| Technical debt | inventory entry, impact/interest, ownership | `technical-debt-governance` then approved workflow | bounded paydown result and regression evidence |
| Preventive maintenance | objective, schedule, affected environment, rollback | deployment/feature/operational action | actual action, health, residual risk |

## Active incident boundary

Use active incident handling only when current service or user impact requires mitigation. A historical defect, planned maintenance action, or predicted risk is not an active incident merely because it is important.

```text
active impact + incident authority available
  → incident-response

impact stopped, root defect remains
  → incident postmortem/action item may create a separate bugfix or feature case

unclear current impact
  → NOT_VERIFIED; investigate before choosing the incident route
```

## Route conflict resolution

A case may have many concerns but exactly one primary requested outcome.

Examples:

```text
production outage caused by regression
  primary now: restore service → incident-response
  follow-up after mitigation: correct defect → linked bugfix case

security library advisory with no verified affected usage
  primary now: investigate/qualify, not automatic dependency update

slow page plus broad UX dissatisfaction
  measurable runtime regression → bugfix/performance route
  broad experience direction → separate design audit/redesign case

stale runbook discovered during deployment
  deployment remains primary if delivery action is active
  documentation-assurance is a blocking overlay
```

Do not combine unrelated outcomes into one maintenance case merely because they were discovered together.

## Closure evidence strength

```text
RESOLVED
  direct evidence proves the bounded expected outcome

FOLLOWUP_REQUIRED
  immediate outcome is verified but owned recurrence, risk, or improvement work remains

PARTIAL
  some bounded outcomes are verified and others are explicit non-pass

NOT_VERIFIED
  required outcome evidence is missing or indirect

BLOCKED
  authority, context, dependency, reviewer, documentation, or environment gate prevents progress
```

## Bounded closure checklist

- case identity and governing signal remain attributable;
- one primary route and owner are recorded;
- execution references are inspectable;
- reviews and authorization states are explicit;
- actual outcome evidence matches the stated objective;
- target environment is verified when operational behavior is claimed;
- documentation impact is reconciled;
- residual risks and accepted risks are distinct;
- recurrence/problem-management actions have owners and deadlines when required;
- one next action or observation owner remains;
- case closure does not claim product acceptance or perpetual operational completion.

## Follow-up splitting

Create a linked follow-up case when:

- incident mitigation restores service but permanent correction is separate;
- a defect fix exposes an independent design or architecture improvement;
- a dependency update requires a later deprecation/removal;
- a documentation correction reveals missing product or operational behavior;
- a measured product signal requires an experiment rather than an implementation assumption.

Each follow-up receives its own objective, scope, evidence, route, owner, and closure state.