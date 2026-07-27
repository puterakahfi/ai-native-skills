# Product Image Production Validation

This directory contains deterministic binary fixtures and real-product evidence contracts for `product-image-production`.

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

## Run binary fixtures

```bash
python scripts/validate-product-image-fixtures.py \
  --manifest validation/product-image-production/fixtures/manifest.json \
  --report /tmp/product-image-validation.json \
  --compare docs/receipts/epic-140-creative-production-validation.json
```

The binary validator uses only the Python standard library. It parses PNG chunks and scanline filters, checks CRC and export structure, calculates alpha/component metrics, compares protected image regions, verifies declared bounds, and reconstructs deterministic composites.

## Real-product acceptance bundle

The repository now provides a fail-closed manifest gate for the remaining real-product acceptance flow:

```text
three authorized product categories
→ attributable provider execution
→ operation and preservation record
→ Product Asset Master export
→ actual-size fidelity, mask, edge, crop, padding, and export review
→ catalog and commercial reuse
→ independent static-visual acceptance
→ integrated readiness claim
```

Start with:

- `real-product-evidence-template.json` for each product case;
- `real-product-acceptance-bundle-template.json` for the three-category integrated bundle.

The required categories are:

1. `rigid_packaged_product`;
2. `reflective_or_translucent_product`;
3. `organic_irregular_soft_edge_product`.

Validate a completed bundle with:

```bash
python scripts/validate-real-product-evidence.py \
  --bundle path/to/real-product-acceptance.json \
  --report /tmp/real-product-acceptance-report.json
```

The validator requires:

- explicit source and provider-processing authorization;
- immutable SHA-256 records for source and three exported roles;
- operation purpose, authority, preservation impact, and evidence references;
- all product-fidelity locks at `PASS`;
- all actual-size mask, edge, clipping, residue, crop, padding, resolution, and export checks at `PASS`;
- Product Asset Master reuse in both catalog and composed commercial outputs;
- an independent reviewer distinct from the provider executor;
- three-category coverage and an explicit production-readiness claim.

The validator checks manifest completeness and cross-reference integrity. It does **not** fetch remote binaries, authenticate reviewers, or replace semantic visual review. Those boundaries remain `NOT_VERIFIED` until independently evidenced.

Repository tests may use `evidence_class: contract_fixture` only with `--allow-contract-fixture`. Contract fixtures must keep `production_readiness_claim: false` and never count as real-product acceptance.

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

Do not replace `NOT_VERIFIED` with `PASS`, enable `production_readiness_claim`, or close issue #145 until all required evidence references are resolvable, every hard gate passes, and the independent reviewer has issued a destination-scoped verdict.
