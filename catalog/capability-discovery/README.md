# Capability Discovery Catalog

This directory is the machine-readable discovery projection for executable capabilities.

- `manifest.json` declares the schema version and file locations.
- `facets.json` defines domain, lifecycle-stage, and concern values.
- `classifications.json` assigns every executable capability exactly once through group defaults and named overrides.
- `job-profiles.json` provides curated workflow routes and capability groups for common jobs.

Human-readable guidance and consumer rules live in [`docs/capability-discovery.md`](../../docs/capability-discovery.md).

Validate the catalog with:

```bash
python3 scripts/verify-capability-inventory.py
python3 scripts/verify-capability-discovery.py
```

The discovery catalog does not add an executable type and does not replace workflow routing or the procedures inside each `SKILL.md`.
