# Commercial Creative Claim-Lock Validation

This directory contains the contract fixture for the authorized-content and provider-fidelity handoff introduced by `puterakahfi/ai-native-skills#158`.

## Validator

```bash
python scripts/validate-commercial-creative-handoff.py \
  --input validation/commercial-creative-production/provider-handoff-template.json \
  --report /tmp/commercial-creative-handoff-report.json
```

## Focused regression suite

```bash
python -m unittest tests/test_validate_commercial_creative_handoff.py -v
```

## What the validator proves

- exact authorized commercial content is traceable to authority records;
- unknown commercial content defaults to prohibited;
- provider handoff carries required text, marks, product references, fidelity locks, and negative constraints;
- output evidence declares all detected content and hard-gate statuses;
- invented or altered content blocks acceptance and delivery;
- SV9 failure routes to `design-refinement+product-image-production`;
- provider executor and reviewer are distinct.

## What the validator does not prove

- OCR or automated text detection on binary images;
- pixel-level product comparison;
- reviewer identity authenticity;
- semantic truth of supplied authority records;
- production readiness by itself.

Those boundaries remain `NOT_VERIFIED` until actual source/output artifacts and independent review evidence are inspected.
