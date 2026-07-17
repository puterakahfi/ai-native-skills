# Experiment Type Guide

## All 11 Experiment Types

| Experiment type | Use when | Example |
|---|---|---|
| `landing_page_waitlist` | Demand/value proposition needs validation | Landing page + waitlist for AI affiliate campaign kits |
| `prototype_test` | UX or comprehension is uncertain | Clickable prototype with 5 target users |
| `fake_door_test` | Measure interest before building | CTA for "Generate campaign kit" with follow-up invite |
| `concierge_test` | Workflow value can be manually delivered first | Manually create affiliate campaign kits for 5 users |
| `wizard_of_oz` | User sees product behavior but backend is manual | AI-like recommendations generated manually |
| `manual_service_pilot` | Operational value needs validation before automation | Run the service by hand for one cohort |
| `interview_script` | Need qualitative validation before any funnel | Structured interviews around pain and alternatives |
| `smoke_test` | Need fast market signal | Ad/post/email to a landing page |
| `pricing_test` | Willingness to pay is uncertain | Paid beta CTA or pricing page test |
| `content_or_offer_test` | Messaging/positioning is uncertain | Compare value props in posts/landing copy |
| `technical_spike` | Feasibility is the riskiest assumption | Timeboxed API/model/prototype spike |

---

## Choosing the Right Experiment Type

**Demand validation** → `landing_page_waitlist`, `smoke_test`, `fake_door_test`

**Willingness to pay** → `pricing_test`, `concierge_test` (charge upfront)

**UX / comprehension** → `prototype_test`, `wizard_of_oz`

**Operational feasibility** → `manual_service_pilot`, `concierge_test`

**Qualitative insight** → `interview_script`

**Technical feasibility** → `technical_spike`

**Messaging / positioning** → `content_or_offer_test`

---

## Ordering Experiments by Cost

Cheapest → most expensive:
1. `interview_script` — conversations only
2. `smoke_test` — ad spend only
3. `content_or_offer_test` — copy variants
4. `fake_door_test` — UI element, no backend
5. `landing_page_waitlist` — landing page
6. `pricing_test` — requires payment mechanism
7. `prototype_test` — interactive prototype
8. `wizard_of_oz` — manual backend ops
9. `concierge_test` — manual service delivery
10. `manual_service_pilot` — ongoing operations
11. `technical_spike` — engineering time

Pick the cheapest type that can answer the riskiest assumption.
