---
name: deployment-workflow
description: Guided deployment workflow — pre-deploy checks, context load, deploy, health verify, confirm or rollback. Security review and approval required before production.
version: 1.0.0
author: puterakahfi
license: MIT
type: workflow
implements: ai-native-core/contracts/workflows/deployment.contract.yaml
skills:
  required:
    - security-review
    - context-manager
  optional:
    - architecture-review
skill_load_order:
  - phase: pre-deploy-check
    load: [security-review, architecture-review]
  - phase: context-load
    load: [context-manager]
---

# Deployment Workflow

## The Core Rule

```
No production deploy without:
1. Security review passed
2. All tests green
3. Explicit approval
4. Rollback plan ready
```

## Prerequisites

Know before starting:
- Target environment (staging | production)
- Deployment provider (product_defined)
- Approval policy (product_defined)
- Rollback strategy (product_defined)

---

## Phase 1: Pre-Deploy-Check
**Gate:** All quality gates must pass before deploy.

Load `security-review` — run full checklist:
- [ ] No secrets in code
- [ ] No injection vectors
- [ ] Dependencies audited
- [ ] Auth/authz checks present

Load `architecture-review` (optional) — confirm no contract violations.

Also verify:
- [ ] All tests passing (CI green or local verified)
- [ ] Code review approved
- [ ] No blocking violations in review verdict

**Done when:** Security verdict = PASS. All tests green. Review approved.

---

## Phase 2: Context-Load
**Gate:** Deployment context must be complete.

Load `context-manager` — resolve deployment context:
- [ ] Target environment confirmed
- [ ] Environment config validated (no missing vars)
- [ ] Secrets available via secret manager (not hardcoded)
- [ ] Rollback plan documented

**Done when:** Deployment context pack complete, rollback plan ready.

---

## Phase 3: Deploy
**Gate:** Production deploy requires explicit approval.

Mechanism is product_defined (Vercel, GitHub Actions, manual SSH, etc).

For **staging**: proceed after Phase 1 + 2.
For **production**: explicit approval required from product owner or tech lead.

```bash
# Example — trigger CI deploy
git push origin main

# Example — manual
./deploy.sh --env production --approved-by <name>
```

**Done when:** Deployment command executed, deployment ID captured.

---

## Phase 4: Verify-Deploy
**Gate:** Health check required after deploy.

- [ ] Application responds to health endpoint?
- [ ] Smoke tests passing?
- [ ] Error monitoring shows no spike?
- [ ] Key user flows working?

```bash
# health check
curl https://<app-url>/health

# smoke test (product_defined)
npm run test:smoke
```

**Done when:** Health check green, no error spike detected.

---

## Phase 5: Rollback-or-Confirm
**Gate:** Explicit confirm or rollback required — no silent ambiguity.

**If healthy:** Confirm deployment. Update status in issue tracker.
**If degraded:** Execute rollback immediately. Do not wait.

```bash
# rollback (product_defined)
./rollback.sh --to <previous-deployment-id>
# or via platform (Vercel, Railway, etc)
```

Document outcome:
```
DEPLOYMENT OUTCOME
──────────────────
Environment: <env>
Status: CONFIRMED | ROLLED BACK
Deployed by: <name>
Approved by: <name>
Deploy ID: <id>
Health: PASS | FAIL
Action taken: <confirm | rollback + reason>
```

---

## Quick Reference

| Phase | Load Skill | Gate |
|---|---|---|
| **1. Pre-deploy** | `security-review`, `architecture-review` | All gates pass |
| **2. Context** | `context-manager` | Context complete |
| **3. Deploy** | — | Approval for production |
| **4. Verify** | — | Health check green |
| **5. Confirm/Rollback** | — | Explicit outcome |
