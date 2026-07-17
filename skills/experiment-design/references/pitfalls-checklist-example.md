# Pitfalls, Checklist & Example

## Common Pitfalls

1. **Building the MVP instead of testing.** If the test requires most of the product, it is not the smallest test.
2. **Testing the easiest assumption.** Pick the assumption that kills the opportunity if false.
3. **No failure threshold.** Without FAIL criteria, every result becomes "promising."
4. **Misleading demand signals.** Waitlist signups are weaker than qualified interviews, usage, or payment intent.
5. **Unsafe fake doors.** Do not trick users in ways that harm trust; explain availability or follow-up.
6. **Ignoring guardrails.** Experiments can create brand, privacy, or trust debt even without a product.
7. **Skipping the decision.** Output is not done until PASS/PARTIAL/FAIL maps to next steps.

---

## Verification Checklist

- [ ] Experiment traces to a value hypothesis or value alignment brief.
- [ ] Target segment and qualification criteria are explicit.
- [ ] Riskiest assumption is singular and material.
- [ ] Hypothesis is falsifiable.
- [ ] Experiment type is named.
- [ ] Smallest test says what will and will not be built.
- [ ] Success criteria include PASS, PARTIAL, and FAIL thresholds.
- [ ] Guardrail criteria exist.
- [ ] Duration or sample threshold exists.
- [ ] Data collection plan names signal source, storage, and privacy/consent handling.
- [ ] Decision rule maps every outcome to PRD/MVP, further discovery, pivot, or stop.

---

## Worked Example — Affiliate Product

```markdown
## Hypothesis
Affiliators will join a waitlist for AI-generated campaign kits if the offer promises faster setup and shows realistic examples.

## Riskiest Assumption
Affiliators trust AI-generated campaign assets enough to try them in real campaigns.

## Smallest Test
- Type: landing_page_waitlist
- What we will do: landing page with 3 sample kits, waitlist CTA, interview booking CTA
- What we will not build yet: dashboard, account system, integrations, payment, automated generation

## Success Criteria
- PASS if: 20 qualified signups and 5 interview bookings in 7 days
- PARTIAL if: 8–19 signups or strong qualitative interest with unclear trust objections
- FAIL if: fewer than 8 signups and no repeated pain pattern

## Guardrails
- No unrealistic income claims. Sample copy labeled editable draft. Lead capture must disclose follow-up usage.

## Decision Rule
- PASS → write PRD and MVP slice for campaign kit generator
- PARTIAL → run 5 interviews and narrow value proposition
- FAIL → stop dashboard idea, test a different affiliator pain point
```
