# Formats, Stop Points, Pitfalls & Verification

## Stop Points

Default stop points:

```text
after_discovery_recommendation
after_prd_draft
after_mvp_plan
after_technical_spec
before_release
after_post_launch_review
```

If the user asks for planning only, stop after PRD/MVP. If the user asks for full execution, ask for approval at each destructive or external side-effect boundary.

---

## Output Format for Planning Mode

Use this format when the user is still exploring the product:

```text
PRODUCT DEVELOPMENT WORKFLOW
Mode: planning
Current phase: discovery | requirements | mvp_slice
Stop point: <stop point>

Target users:
- ...

Top opportunities:
1. ...
2. ...
3. ...

Recommended MVP:
- ...

PRD readiness:
Verdict: READY | NEEDS REVISION | BLOCKED
Blocking gaps:
- ...

Next approval needed:
- ...
```

---

## Output Format for Execution Mode

Use this format when the user wants actual implementation/deploy:

```text
PRODUCT DEVELOPMENT WORKFLOW
Mode: execution
Current phase: <phase>
Gate status: PASS | FAIL | BLOCKED
Evidence:
- <tool output, test result, URL, commit, or artifact path>
Next phase:
- <phase or approval request>
```

---

## Common Pitfalls

1. **Starting with code.** New products start with discovery and PRD unless the user already provides validated requirements.
2. **Skipping non-goals.** Without non-goals, MVP scope expands into full-product fantasy.
3. **Treating deploy as launch.** Deployment is technical availability; launch is user-facing release with messaging, support, analytics, and feedback.
4. **No acceptance evidence.** A checklist without proof is not release readiness.
5. **No stop point.** For vague product ideas, stop after PRD/MVP recommendation for approval before technical spec.
6. **Overloading one response.** For large products, phase output should be concise and gated, not a giant all-in-one document.

---

## Verification Checklist

- [ ] Discovery happened before PRD when idea was vague.
- [ ] PRD exists before technical spec.
- [ ] MVP slice is smaller than full product.
- [ ] Technical spec traces to PRD requirements.
- [ ] Implementation tasks trace to acceptance criteria.
- [ ] Acceptance criteria have evidence before release.
- [ ] Release has notes/version/rollback plan.
- [ ] Deployment health is verified before launch.
- [ ] Launch has support, analytics, and feedback loop.
- [ ] Post-launch learning feeds next PRD or backlog.
