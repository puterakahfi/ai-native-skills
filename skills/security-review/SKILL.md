---
name: security-review
description: Security baseline validation skill — detect secrets, injection vectors, auth gaps, and dependency vulnerabilities before merge or deploy. Blocks deployment until security gate passes.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/security/security-review.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Security Review

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/security/security-review.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- code_or_diff
- security_baseline_ref
allowed_outputs:
- security_verdict
- secret_detection_report
- vulnerability_list
- dependency_risk_report
- blocking_violations
- recommendations
quality_gates:
- no_hardcoded_secrets_or_credentials
- no_sql_injection_vectors
- input_sanitization_verified
- output_encoding_verified
- authorization_checks_present
- dependency_vulnerabilities_checked
- no_sensitive_data_in_logs
- security_verdict_required_before_deploy
```

Review code_or_diff against security_baseline_ref and emit a security_verdict, secret report, vulnerability list, dependency risk report, blocking violations, and recommendations. Verify output encoding alongside sanitization and authorization; deployment remains blocked until the verdict is explicit.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, security, incident, resilience, or product evidence.


## The Core Rule

```
No deploy to production without security gate.
AI-generated code is not implicitly secure.
```

## When to Use

- Before any PR merge (especially AI-generated code)
- Before deploying to staging or production
- When adding new dependencies
- When adding new API endpoints or input surfaces
- When handling user data, credentials, or payment info

---

## Checklist

### 1. Secret Detection
- [ ] No hardcoded API keys, tokens, passwords?
- [ ] No credentials in `.env.example` with real values?
- [ ] No sensitive data in git history?
- [ ] Secrets loaded from environment, not source?

```bash
# quick scan
grep -rn "password\|secret\|api_key\|token" --include="*.{js,ts,py,php}" src/
git log --all --full-history -- "*.env"
```

---

### 2. Injection Prevention
- [ ] SQL queries use parameterized statements or ORM?
- [ ] No raw SQL with user input?
- [ ] Command execution uses safe APIs (no `exec(userInput)`)?
- [ ] Template rendering escapes output?

---

### 3. Input Sanitization
- [ ] All user input validated before processing?
- [ ] File uploads restricted by type and size?
- [ ] No direct use of user input in file paths?
- [ ] No XSS vectors in rendered output?

---

### 4. Authorization & Access Control
- [ ] Every endpoint checks authentication?
- [ ] Authorization checks present — not just authentication?
- [ ] No IDOR (Insecure Direct Object Reference) — user can only access their own resources?
- [ ] Admin routes protected separately?

---

### 5. Dependency Security
- [ ] New dependencies scanned for known vulnerabilities?
- [ ] Pinned versions, not floating?
- [ ] No abandoned/unmaintained packages?

```bash
# Node
npm audit

# PHP/Composer
composer audit

# Python
pip-audit
```

---

### 6. Sensitive Data in Logs
- [ ] No passwords, tokens, or PII in log output?
- [ ] Error messages don't expose stack traces to end users?
- [ ] No sensitive data in URLs (query params)?

---

## Verdict Format

```
SECURITY REVIEW VERDICT
───────────────────────
Status: PASS | FAIL | PASS WITH FLAGS

Blocking Violations:
  - [SECRET] Hardcoded API key in src/config.js:14
  - [INJECTION] Raw SQL with user input in UserRepo.php:87

Warnings:
  - [DEPENDENCY] lodash@4.17.15 has known vulnerability — update to 4.17.21

Approved for deploy: YES | NO
```

## Common Anti-Patterns (Auto-Fail)

| Pattern | Why |
|---|---|
| `const KEY = "sk-abc123"` in source | Secret in code |
| `db.query("SELECT * WHERE id=" + userId)` | SQL injection |
| No auth check on `/admin/*` routes | Access control gap |
| `console.log(user.password)` | Sensitive data in logs |
| `npm install` without `npm audit` | Dependency risk ignored |
| "AI generated it, should be secure" | Generated ≠ Secure |
