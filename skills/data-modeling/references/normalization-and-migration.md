# Normalization and Migration Patterns

## Normalization — When to Normalize, When Not To

### Normal Forms

```
1NF: No repeating groups, atomic values
  ❌ tags: "typescript,nextjs,supabase"  (comma-separated string)
  ✅ tags table with FK to post

2NF: No partial key dependencies (for composite keys)
  Applies when: composite primary key (A+B → C)
  If C depends only on A, not both A+B → violates 2NF

3NF: No transitive dependencies
  ❌ orders(order_id, customer_id, customer_city)
      city depends on customer, not order
  ✅ separate customers table

BCNF: Stricter 3NF — every determinant is a candidate key
  Most schemas should aim for 3NF minimum, BCNF when possible
```

### When to Denormalize

```
Denormalize when:
  - Read performance is critical AND the read query JOINs > 3 tables
  - The field is rarely updated (denormalize a snapshot, not live data)
  - Reporting tables (OLAP) — denormalize aggressively
  - Event sourcing — append-only, reads reconstruct state

Denormalize safely with:
  - Derived columns (store computed value, update on write)
  - Read replicas with materialized views
  - CQRS: write model normalized, read model denormalized

Never denormalize:
  - Frequently updated fields (sync cost exceeds read gain)
  - Financial data (consistency is non-negotiable)
  - Fields that join to user-owned data (privacy complexity)
```

---

## Migration Patterns

### Expand-Contract (zero-downtime migrations)

```
Phase 1 — EXPAND: add new column/table, keep old
  - New code writes to BOTH old and new
  - Old code still reads old column (no breakage)

Phase 2 — MIGRATE: backfill old → new
  - Run migration in batches (never full table lock)
  - batch size: 1000–5000 rows per transaction
  - Add delay between batches (avoid replication lag)

Phase 3 — CONTRACT: remove old column/table
  - Old code updated to read only new column
  - Drop old column after deploy confirmed
  - Deploy → verify → then drop (not simultaneously)

Example:
  Need to rename `user.name` → `user.full_name`:
  1. Add `full_name` column (EXPAND)
  2. Write to both, backfill `full_name` from `name`
  3. Switch reads to `full_name` (deploy)
  4. Drop `name` column (CONTRACT)
```

### Batch Migration Template

```sql
-- Safe large table migration with batching
DO $$
DECLARE
  batch_size INT := 2000;
  last_id    BIGINT := 0;
  max_id     BIGINT;
BEGIN
  SELECT MAX(id) INTO max_id FROM users;
  
  WHILE last_id < max_id LOOP
    UPDATE users
    SET full_name = name
    WHERE id > last_id AND id <= last_id + batch_size
      AND full_name IS NULL;
    
    last_id := last_id + batch_size;
    PERFORM pg_sleep(0.05); -- 50ms pause between batches
  END LOOP;
END $$;
```
