---
name: threat-modeling
description: Proactive security threat identification before implementation — STRIDE analysis per trust boundary, data flow mapping, mitigation planning, and risk rating. Security gate before any feature goes to code.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/security/threat-modeling.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: '["security-review", "architecture-review", "spec-workflow", "adr"]'
---

# Threat Modeling

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/security/threat-modeling.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- feature_or_system_description
allowed_outputs:
- threat_model_document
- stride_analysis
- trust_boundary_map
- mitigation_plan
- risk_rating_per_threat
quality_gates:
- threat_modeling_must_happen_before_implementation_not_after
- all_trust_boundaries_must_be_identified
- stride_must_be_applied_per_trust_boundary
- every_threat_must_have_explicit_mitigation_or_accepted_risk
- data_flows_must_be_mapped_including_external_dependencies
- privilege_escalation_paths_must_be_identified
- threat_model_must_be_updated_when_architecture_changes
- risk_rating_must_use_consistent_scoring
```

Start from feature_or_system_description before implementation. Produce the threat model, STRIDE analysis, trust-boundary map, mitigation plan, and consistent risk ratings. Map external dependencies in data flows, identify privilege-escalation paths, and update the model whenever architecture changes.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, security, incident, resilience, or product evidence.


## Order of Operations

```
spec-workflow → threat-modeling → implementation → security-review

Cost of fixing a threat:
  Design phase: $1 | Implementation: $10 | Testing: $100 | Production: $1000+
```

**Trigger:** "What could go wrong with this, before we build it?"

Run threat modeling for: every new API endpoint, auth/authz change, new service/integration, or trust boundary change.

---

## Step 1: Draw the Data Flow Diagram

Map Processes, Data Stores, External Entities, and Data Flows (arrows):

```
[User Browser] → (Login API) → [Session Store]
                              → [User DB]
[User Browser] → (Order API) → [Order DB]
                              → (Payment Service) → [Payment Gateway]
                              → [Event Bus] → (Inventory Service)
```

---

## Step 2: Identify Trust Boundaries

A trust boundary = anywhere data crosses from one trust level to another.

```
1. Internet → API Gateway         (untrusted → trusted)
2. API → Payment Service          (internal trusted → external third-party)
3. API → Event Bus                (sync → async, different trust context)
4. Service → Database             (application → persistence)

Mark every arrow that crosses a trust boundary.
```

---

## Step 3: STRIDE Per Trust Boundary

| Threat | Question | Example |
|---|---|---|
| **S**poofing | Can an attacker impersonate a legitimate entity? | Fake user token, forged service identity |
| **T**ampering | Can data be modified in transit or at rest? | Man-in-the-middle, SQL injection, mass assignment |
| **R**epudiation | Can an actor deny performing an action? | No audit log, unsigned requests |
| **I**nformation Disclosure | Can sensitive data be exposed? | Over-fetching API, verbose error messages, log leakage |
| **D**enial of Service | Can the service be made unavailable? | Unbounded query, missing rate limit, resource exhaustion |
| **E**levation of Privilege | Can an actor gain more access than allowed? | IDOR, broken authorization, JWT algorithm confusion |

```
Example — Trust boundary: Internet → Login API

S: credential stuffing → rate limiting, MFA, account lockout
T: session token interception → HTTPS only, Secure + HttpOnly cookie flags
R: no audit trail → log all auth events with IP, timestamp, userId
I: user enumeration via error message → generic error for both "not found" and "wrong password"
D: brute force/DDoS → rate limit per IP + per account, CAPTCHA
E: JWT algorithm confusion (none algorithm) → whitelist algorithms, validate signature always
```

---

## Step 4: Risk Rating

```
DREAD scoring:
  Damage potential / Reproducibility / Exploitability / Affected users / Discoverability (1-3 each)
  Score = sum (5-15): Critical 13-15 | High 10-12 | Medium 7-9 | Low 5-6

Simplified:
  CRITICAL — exploitable, high damage, easy to trigger
  HIGH     — exploitable, significant damage
  MEDIUM   — exploitable with effort, limited damage
  LOW      — hard to exploit, minimal damage
  ACCEPTED — acknowledged, risk accepted with rationale
```

---

## Step 5: Mitigation Plan

Every threat needs one of: **Mitigate** / **Transfer** / **Avoid** / **Accept**

```yaml
# threat-model.yaml
feature: User Login
date: 2026-07-16
author: platform-team

trust_boundaries:
  - boundary: internet_to_login_api
    threats:
      - id: T001
        stride: Spoofing
        description: Credential stuffing attack
        rating: HIGH
        mitigation: Rate limit 5 attempts/min per IP, account lockout after 10 failures
        status: mitigated

      - id: T002
        stride: Information Disclosure
        description: User enumeration via error message difference
        rating: MEDIUM
        mitigation: Return same error for "user not found" and "wrong password"
        status: mitigated

      - id: T003
        stride: Denial of Service
        description: Login endpoint flood
        rating: HIGH
        mitigation: Rate limiting + CAPTCHA after 3 failures
        status: mitigated
```

---

## Integration with spec-workflow

```markdown
## Spec — Feature: User Login

### Threat Model
[ ] Data flow diagram drawn
[ ] Trust boundaries identified
[ ] STRIDE applied per boundary
[ ] All CRITICAL/HIGH threats mitigated
[ ] Accepted risks documented with rationale
```

---

## Threat Modeling Checklist

Before implementation starts:
- [ ] Data flow diagram complete?
- [ ] All trust boundaries identified?
- [ ] STRIDE applied at every trust boundary?
- [ ] Every threat has risk rating?
- [ ] All CRITICAL and HIGH threats have mitigation?
- [ ] Accepted risks documented with rationale?
- [ ] Threat model stored in `docs/threat-models/`?
- [ ] Threat model linked from ADR if architectural change involved?

> **HARD RULE:** No CRITICAL or HIGH unmitigated threat may enter implementation. Accept only with explicit written rationale.
