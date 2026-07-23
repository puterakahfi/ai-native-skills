# Capability Discovery Catalog

This directory is the machine-readable discovery projection for executable capabilities.

- `manifest.json` declares schema version 2 and the catalog file locations.
- `facets.json` defines domain, lifecycle-stage, concern, and ecosystem values.
- `classifications.json` assigns every executable capability exactly once through group defaults and named overrides.
- `topics.json` provides curated, overlapping browse collections and recommended starting points.
- `job-profiles.json` provides workflow routes, capability groups, evidence, and completion gates for common jobs.

Human-readable guidance and consumer rules live in [`docs/capability-discovery.md`](../../docs/capability-discovery.md).

Validate the catalog with:

```bash
python3 scripts/verify-capability-inventory.py
python3 scripts/verify-capability-discovery.py
```

The discovery catalog does not add an executable type and does not replace workflow routing or the procedures inside each `SKILL.md`. Domains remain ownership-oriented, concerns remain cross-cutting, ecosystems represent technology/runtime contexts, topics remain editorial browse collections, and job profiles remain opinionated execution compositions.
