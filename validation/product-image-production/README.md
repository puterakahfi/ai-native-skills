# Product Image Production Validation

This directory contains deterministic binary fixtures for `product-image-production`.

## Evidence classes

```text
synthetic controlled binary fixtures
  proves:
    PNG structure, alpha semantics, clipping, residue, transparent-RGB spill,
    partial-alpha behavior, label-region preservation, declared product bounds,
    upscale limits, and deterministic downstream compositing

  does not prove:
    real product fidelity, provider behavior, photographic retouch quality,
    commercial taste, destination performance, or independent product acceptance
```

A passing fixture suite must therefore retain:

```text
real_product_acceptance: NOT_VERIFIED
provider_backed_execution: NOT_VERIFIED
independent_visual_acceptance: NOT_VERIFIED
production_readiness_claim: false
```

## Validation matrix

| Case | Category | Expected |
|---|---|---|
| `rigid-packaged-pass` | rigid packaged product with label region | PASS |
| `translucent-partial-alpha-pass` | reflective/translucent product | PASS |
| `organic-soft-edge-pass` | irregular soft-edge product | PASS |
| `unsuitable-source-fail` | insufficient source and missing product truth | FAIL_CLOSED |
| `downstream-reuse-pass` | one prepared master reused in catalog and ad composite | PASS |
| `halo-fail` | colored RGB in transparent pixels | FAIL |
| `clipping-fail` | alpha touches canvas edge | FAIL |
| `residue-fail` | isolated alpha components | FAIL |
| `invented-label-fail` | protected label region changed | FAIL |
| `baked-shadow-fail` | undeclared alpha outside authorized product bounds | FAIL |
| `aggressive-upscale-fail` | fine-detail source exceeds declared upscale limit | FAIL_CLOSED |

## Run

```bash
python scripts/validate-product-image-fixtures.py \
  --manifest validation/product-image-production/fixtures/manifest.json \
  --report /tmp/product-image-validation.json \
  --compare docs/receipts/epic-140-creative-production-validation.json
```

The validator uses only the Python standard library. It parses PNG chunks and scanline filters, checks CRC and export structure, calculates alpha/component metrics, compares protected image regions, verifies declared bounds, and reconstructs deterministic composites.

## Adding real-product evidence

Real-product evidence must use authorized source material and record:

- source provenance and identity;
- original source and actual produced/exported artifacts;
- provider/tool and operation record;
- preservation locks and transformation authority;
- source/output product-fidelity comparison;
- actual-size edge, alpha, crop, padding, resolution, and export review;
- downstream catalog and commercial-composite handoff;
- independent `design-review` result;
- limitations and unsupported claims.

Start from `real-product-evidence-template.json`. Do not replace `NOT_VERIFIED` with PASS until all required evidence references are resolvable and the independent reviewer has issued a destination-scoped verdict.
