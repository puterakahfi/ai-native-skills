---
name: threat-modeling
description: Proactive security threat identification before implementation — STRIDE analysis per trust boundary, data flow mapping, mitigation planning, and risk rating. Security gate before any feature goes to code.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/quality-control/threat-modeling.contract.yaml
  ai-native-skills.related_skills: '[''security-review'', ''architecture-review'', ''spec-workflow'', ''adr'']'
---

# Threat Modeling

## The Core Rule

```
security-review  = reactive  — check code that already exists
threat-modeling  = proactive — find threats before a single line is written

Order of operations:
  spec-workflow → threat-modeling → implementation → security-review

Cost of fixing a threat:
  Design phase:        $1
  Implementation:      $10
  Testing:             $100
  Production:          $1000+
```

---

## When to Run Threat Modeling

- Every new feature that handles user data
- Every new API endpoint
- Every change to authentication or authorization
- Every new service or integration
- Any change to trust boundaries

**Trigger:** "What could go wrong with this, before we build it?"

---

## Step 1: Draw the Data Flow Diagram

Map how data moves through the system. Identify every:
- **Process** — code that transforms data
- **Data store** — database, cache, file system
- **External entity** — user, third-party service, another system
- **Data flow** — arrows showing data movement

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
Trust boundaries in the example above:
  1. Internet → API Gateway         (untrusted → trusted)
  2. API → Payment Service          (internal trusted → external third-party)
  3. API → Event Bus                (sync → async, different trust context)
  4. Service → Database             (application → persistence)

Mark every arrow that crosses a trust boundary.
```

---

## Step 3: STRIDE Per Trust Boundary

Apply STRIDE at every trust boundary crossing:

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

S: Can attacker fake user credentials?
   → Threat: credential stuffing
   → Mitigation: rate limiting, MFA, account lockout

T: Can request be tampered in transit?
   → Threat: session token interception
   → Mitigation: HTTPS only, Secure + HttpOnly cookie flags

R: Can login attempts be denied?
   → Threat: no audit trail
   → Mitigation: log all auth events with IP, timestamp, userId

I: Can error messages reveal user existence?
   → Threat: user enumeration via "user not found" vs "wrong password"
   → Mitigation: generic error message for both cases

D: Can login endpoint be flooded?
   → Threat: brute force, DDoS
   → Mitigation: rate limit per IP + per account, CAPTCHA

E: Can attacker bypass auth entirely?
   → Threat: JWT algorithm confusion (none algorithm)
   → Mitigation: whitelist algorithms, validate signature always
```

---

## Step 4: Risk Rating

Rate each threat before deciding mitigation priority:

```
DREAD scoring (or simplified):

  Damage potential:    How bad if exploited? (1-3)
  Reproducibility:     How easy to reproduce? (1-3)
  Exploitability:      How easy to exploit? (1-3)
  Affected users:      How many affected? (1-3)
  Discoverability:     How easy to find? (1-3)

  Score = sum (5-15)
  Critical: 13-15 | High: 10-12 | Medium: 7-9 | Low: 5-6

Or simplified:
  CRITICAL — exploitable, high damage, easy to trigger
  HIGH     — exploitable, significant damage
  MEDIUM   — exploitable with effort, limited damage
  LOW      — hard to exploit, minimal damage
  ACCEPTED — acknowledged, risk accepted with rationale
```

---

## Step 5: Mitigation Plan

Every threat needs one of:
- **Mitigate** — implement a control
- **Transfer** — move risk (e.g. use managed auth service)
- **Avoid** — don't build the feature this way
- **Accept** — document rationale, accept the risk

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

Add threat modeling as a mandatory gate in spec:

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
- [ ] Threat model stored in docs/threat-models/?
- [ ] Threat model linked from ADR if architectural change involved?
