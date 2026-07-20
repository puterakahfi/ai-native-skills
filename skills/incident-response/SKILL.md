---
name: incident-response
description: Structured incident lifecycle and blameless postmortem — detect, triage, mitigate, resolve, postmortem, prevent. 5 Whys to systemic cause, action items with owner and deadline, prevention at class level.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime/incident-response.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: "['systematic-debugging', 'observability-design', 'deployment-workflow', 'adr']"
---

# Incident Response

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/runtime/incident-response.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- incident_description
allowed_outputs:
- incident_timeline
- triage_decision
- mitigation_steps
- postmortem_document
- action_items
- prevention_recommendations
quality_gates:
- incident_must_be_triaged_before_fix_attempted
- mitigation_before_root_cause_is_acceptable
- postmortem_must_be_blameless
- five_whys_must_reach_systemic_cause_not_human_error
- action_items_must_have_owner_and_deadline
- postmortem_must_include_what_went_well
- prevention_must_address_class_of_problem_not_just_instance
- incident_severity_must_be_declared_explicitly
```

Start from incident_description, declare severity, triage before attempted repair, mitigate to restore service, then produce a timeline, triage decision, mitigation steps, blameless postmortem, owned action items, and class-level prevention. Five Whys must reach a systemic cause rather than human blame, and the postmortem must record what went well as well as failures.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, security, incident, resilience, or product evidence.


## HARD RULES

```
1. Declare severity before acting — blast radius must be known
2. Mitigate first (restore service), root cause second
3. Blameless postmortem always — never name a person as root cause
4. Write postmortem within 48 hours while memory is fresh
5. Prevention must address class of problem, not just this instance
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

## Phase Overview

```
Phase 1 → Detect & Declare  — signal received, severity set, IC assigned
Phase 2 → Triage            — scope blast radius, DO NOT fix yet
Phase 3 → Mitigate          — restore service (rollback preferred)
Phase 4 → Resolve & Verify  — confirm resolution criteria met
Phase 5 → Postmortem        — blameless, 5 Whys to systemic cause
```

---

## References

- **[Phases 1–3](references/phases-1-3.md)** — Detect & Declare, Triage, Mitigate (with commands)
- **[Phases 4–5 + Postmortem](references/phases-4-5-postmortem.md)** — Resolve & Verify, full Postmortem template, 5 Whys rules, Incident Response Checklist
