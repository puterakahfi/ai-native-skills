---
name: hermes-fleet-auto-routing
description: Use when dispatching fleet specialists end-to-end.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["hermes-agent-fleet-bootstrap","workflow-router","role-switcher"]'
---

# Hermes Fleet Auto-routing

Covers the full task-time auto-routing lifecycle: plan → dispatch → receipt validation → synthesis → origin return. Use when acting as `agent-orchestrator` executing a cross-specialist task against the native-ai-engineering fleet.

## Load order

Before executing, load in order:
1. `workflow-router` — classify intent, select primary workflow
2. `hermes-agent-fleet-bootstrap:references/auto-routing-contract.md` — contract invariants
3. This skill — dispatch patterns and schema friction

## Routing decision

Emit before any dispatch:

```yaml
workflow_selection: <one primary route>
routing_rationale: <intent evidence>
ambiguity_resolution: resolved | clarification required
```

## Plan emission (STEP 1)

Write `/tmp/plan.yaml` conforming to `task-routing-plan.schema.yaml`:

```yaml
schema_version: "1.0"
plan_id: plan-<slug>-001          # pattern: ^plan-[A-Za-z0-9_-]+$
created_at: "<ISO datetime>"
origin:
  channel: desktop                 # enum: desktop|gateway_telegram|gateway_slack|cli|cron
  session_id: "<session-id>"
  user_ref: "<user>"
orchestrator_action:
  kind: delegated_to_specialist    # no self_handled_category when delegated
primary_workflow: <workflow-name>
workers:
  - worker_id: worker-design-01   # pattern: ^worker-[A-Za-z0-9_-]+$
    profile: agent-design          # pattern: ^agent-[a-z][a-z0-9-]*$
    responsibility: "<one sentence>"
    expected_outputs: []
  - worker_id: worker-frontend-01
    profile: agent-frontend
    responsibility: "<one sentence>"
    depends_on: [worker-design-01]
    inputs: []
    expected_outputs: []
reviewers:
  - reviewer_id: reviewer-1       # pattern: ^reviewer-[A-Za-z0-9_-]+$
    profile: agent-review
    scope: [accessibility, typescript-correctness]
    independence_target: VERIFIED  # VERIFIED when reviewer profile != all worker profiles
    reviews_worker_ids: [worker-frontend-01]
review_policy:
  allow_limited_independence: false
  require_reviewer_per_worker: true
status: planned
```

Validate immediately:
```bash
python3 -c "import yaml,jsonschema; jsonschema.validate(yaml.safe_load(open('/tmp/plan.yaml')), yaml.safe_load(open('/data/www/ai-native-skills/schemas/auto-routing/task-routing-plan.schema.yaml'))); print('VALID')"
```

## Worker dispatch (STEPS 3-5)

Dispatch each worker in dependency order via subprocess:

```bash
START=$(date +%s)
hermes -p agent-design chat -q "..."
echo "TIME:$(($(date +%s)-START))s"
```

Worker prompt must request a `worker_receipt` YAML block at end:

```yaml
worker_receipt:
  schema_version: '1.0'
  receipt_id: worker-receipt-<worker-id>
  plan_id: <plan_id>
  worker_id: <worker_id>
  profile: <profile>
  status: executed
  started_at: '<ISO>'    # REQUIRED — schema enforces this
  completed_at: '<ISO>'  # REQUIRED — schema enforces this
  retries: 0
  evidence:
    evidence_type: artifact
    receipt_inline: '<summary>'    # one of receipt_inline or receipt_uri required
    artifacts: ['<path>']
```

## Synthesis (STEP 6)

**Critical: omit unasserted claims entirely.** Do NOT set `asserted: false` with
`supporting_receipt_ids: []` — schema enforces `minItems: 1` regardless of `asserted`.

```yaml
schema_version: "1.0"
receipt_id: synthesis-<slug>-01
plan_id: <plan_id>
synthesized_at: "<ISO>"
worker_receipt_ids: [worker-receipt-design-01, worker-receipt-frontend-01]
review_receipt_ids: [review-receipt-01]
final_status: reviewed       # 'reviewed' when changes_requested; 'approved' when approved
promoted_claims:
  implemented:
    asserted: true
    supporting_receipt_ids: [worker-receipt-frontend-01]
  reviewed:
    asserted: true
    supporting_receipt_ids: [review-receipt-01]
  # omit 'approved' entirely when review verdict != approved
```

## Origin return receipt

```yaml
schema_version: "1.0"
receipt_id: origin-return-<slug>-01
plan_id: <plan_id>
origin:
  channel: desktop
  session_id: "<session-id>"
  user_ref: "<user>"
delivery_channel: desktop      # must match origin.channel exactly
delivered_at: "<ISO>"
artifact_uri: "file:///tmp/<artifact>"
status: not_verified           # see schema gap below
```

> **#312 FIXED (PR #316)**: `origin-return-receipt` status enum now includes
> `reviewed` and `changes_requested`. Use the correct value — no more `not_verified` workaround.
> Enum: `[delivered, reviewed, changes_requested, blocked, cancelled, not_verified]`

## Review receipt shape (STEP 5)

Emit per reviewer after worker completes:

```yaml
schema_version: "1.0"
receipt_id: review-receipt-<reviewer_id>-<slug>   # pattern: ^review-receipt-[A-Za-z0-9_-]+$
plan_id: <plan_id>
worker_receipt_id: <worker_receipt_id>
reviewer_profile: <agent-xxx>
independence:
  verdict: VERIFIED | LIMITED | NOT_VERIFIED
  compromises: []    # enum values only — see below
reviewed_at: "<ISO 8601>"
verdict: approved | changes_requested | blocked
findings:
  - severity: error | warning | info | blocker   # REQUIRED
    message: "<file:line — description>"          # REQUIRED — combine location+desc here
    evidence: "<suggested fix>"                   # optional
```

**Pitfall — finding shape:** `findings` items only allow `severity`, `message`, `evidence`.
Fields `id`, `location`, `description`, `suggested_fix` are NOT in schema — they cause
`additionalProperties` validation errors. Pack location + description into `message`.

### independence.compromises enum (exact strings only)

```
shared_model | shared_context | shared_tools | shared_repo_access | shared_profile
```

Free-text strings like `"agent-review self-reviewed"` are schema-invalid.
Use `shared_profile` when reviewer profile == any worker profile in the same plan.

**Pitfall — NOT_VERIFIED + approved verdict:** schema enforces via `allOf` that
`NOT_VERIFIED` independence forbids `verdict: approved`. Use `changes_requested`
in negative fixtures testing NOT_VERIFIED independence; document the blocking in
`synthesis_notes` rather than the receipt itself.

## Independence verdict rules

| Reviewer vs workers | `independence.verdict` |
|---|---|
| Reviewer profile != all worker profiles | `VERIFIED`, `compromises: []` |
| Reviewer profile = any worker profile | Must report `shared_profile` → `LIMITED` |
| `LIMITED` + `allow_limited_independence: false` | Cannot promote to `approved` |

### Pitfall: agent-review as both worker AND reviewer

`agent-review` may legitimately appear as a **worker** (producing a QA artifact like `review-report.md`) AND as a **plan reviewer**. When it does, `independence_target` must be `LIMITED` — not `VERIFIED`.

**Wrong:**
```yaml
workers:
  - worker_id: worker-review-01
    profile: agent-review        # agent-review IS a worker
reviewers:
  - profile: agent-review
    independence_target: VERIFIED  # ← WRONG — agent-review reviewed its own output
```

**Correct:**
```yaml
reviewers:
  - profile: agent-review
    independence_target: LIMITED   # shared_profile compromise applies
```

For full `approved` synthesis, add a second reviewer whose profile is absent from all workers (e.g. `agent-orchestrator` reviewing the review report). `VERIFIED` requires empty `compromises` list — it cannot be claimed when `shared_profile` applies.

## Topology (STAR)

```
user -> agent-orchestrator -> agent-design
                           -> agent-frontend (depends on design output)
                           -> agent-review (independent reviewer)
                           <- synthesis <- all receipts
                           -> user
```

Specialists never invoke each other directly. All handoffs through orchestrator.

- `hermes-auto-routing-review-synthesis` (in `ai-native-skills` repo, `skills/hermes-auto-routing-review-synthesis/`) —
  review loop + synthesis: dispatches reviewers, records `review_receipt` per reviewer,
  enforces state ladder (executed→reviewed→approved→delivered→merged→accepted), synthesizes
  promoted claims, emits `synthesis_receipt` + `origin_return_receipt`. (#309)

## Reference files

- `references/auto-routing-schema-friction.md` — schema friction from all dogfood runs:
  F1 (worker timestamps required), F2 (synthesis omit-not-false), F3 (origin return — fixed PR #316),
  F4 (review receipt findings shape), F5 (compromises enum + NOT_VERIFIED constraint),
  F6 (reviewer-as-worker → LIMITED independence), F7-F8 (PR #316 additions),
  F9 (SKILL.md description YAML parse error — quote all descriptions, avoid `→` `—`).

## Related skills

- `hermes-auto-routing-planner` (in `ai-native-skills` repo, `skills/hermes-auto-routing-planner/`) —
  the deterministic planner that composes `workflow-router` + `role-switcher` into a validated
  `task_routing_plan`. Use that skill for the planning step (#307). This skill covers
  dispatch → receipts → synthesis.
- `hermes-auto-routing-dispatch` (in `ai-native-skills` repo, `skills/hermes-auto-routing-dispatch/`) —
  execution bridge: consumes `task_routing_plan`, dispatches worker slots, emits `dispatch_receipt`
  per worker. Two modes: `durable_worker` (Kanban + persistent session) and `temporary_delegation`
  (`hermes -p <profile> chat -q`). `temporary_delegation` is the verified working mode as of
  2026-07-31 (#308). `durable_worker` is target but not fully wired yet → `READY_WITH_LIMITATIONS`.

## Task routing: where skills live

Skills in `ai-native-skills` repo have two distinct categories:

| Category | Example | Published in repo? | Hermes-specific? |
|---|---|---|---|
| Generic reusable | `workflow-router`, `role-switcher` | ✅ | ❌ |
| Hermes fleet-specific | `hermes-auto-routing-planner`, `hermes-agent-fleet-bootstrap` | ✅ | ✅ |

Fleet-specific skills go in the repo (not just `~/.hermes/profiles/`) because:
- Version-controlled alongside schemas and fixtures
- Reviewable via PR
- Can be adopted by other Hermes fleet implementations as reference

Pure Hermes runtime concerns (dispatch subprocess details, session management) stay in
the skill body, not as a separate Hermes profile-only skill.

## GitHub CLI (gh) auth pitfall

`gh auth login --web` approved in the **user's terminal** does NOT reach the Hermes
agent shell session — they run in different processes. `gh auth status` will still
show "not logged in" from the agent side.

**Fix:** After user approves in browser, get the token from their terminal:
```bash
# user runs in their terminal:
gh auth token   # → gho_xxxx...
```
Then use it explicitly in agent commands:
```bash
GH_TOKEN=<token> gh pr create --title "..." --body "..." --base main --head <branch>
GH_TOKEN=<token> gh pr close $pr --comment "Superseded by #EPIC_PR"
```
Do NOT attempt `gh auth login` loop again — it will generate a new code the user
must re-approve, timing out before the poll completes.

## Epic branch rule (ENFORCED by user)

All slices of an epic MUST go into ONE branch (`feat/epic-NNN-slug`) and ONE PR.
Never create separate per-slice branches/PRs for the same epic.

**Recovery when separate slice branches/PRs were already pushed:**
```bash
# 1. Find the branch with all commits (the most complete tip — often the last slice)
git log --oneline feat/slice-last-branch  # verify all commits present

# 2. Create the epic branch from that tip
git checkout feat/slice-last-branch
git checkout -b feat/epic-NNN-slug
git push origin feat/epic-NNN-slug

# 3. Create the single epic PR
GH_TOKEN=<token> gh pr create \
  --title "feat(...): Epic #NNN — ..." \
  --body "Consolidates PRs #N1, #N2, #N3 (being closed).\n\nCloses #issue1, #issue2..." \
  --base main --head feat/epic-NNN-slug

# 4. Close all separate slice PRs with reference
for pr in N1 N2 N3; do
  GH_TOKEN=<token> gh pr close $pr --comment "Superseded by #EPIC_PR (epic branch)"
done
```

## Skill sync model — symlink to ~/.hermes/ai-native-skills/ (resolved #285 core)

Profile skills are **symlinks** pointing to `~/.hermes/ai-native-skills/skills/<name>`.
The repo is cloned at a fixed predictable path (not `/data/www/` which is local-only):

```
~/.hermes/ai-native-skills/          ← git clone of puterakahfi/ai-native-skills
  skills/
    workflow-router/
    hermes-auto-routing-planner/
    ...

~/.hermes/profiles/agent-orchestrator/skills/
  workflow-router → ~/.hermes/ai-native-skills/skills/workflow-router   ← symlink
  hermes-auto-routing-planner → ~/.hermes/ai-native-skills/skills/hermes-auto-routing-planner
```

**To update ALL profile skills at once:**
```bash
cd ~/.hermes/ai-native-skills && git pull
# All profiles auto-reflect latest — no reinstall needed
```

**Bootstrap on a new machine:**
```bash
git clone git@github-arbiter:puterakahfi/ai-native-skills.git ~/.hermes/ai-native-skills
# Then run hermes_fleet.py bootstrap which creates symlinks (not copies)
```

**To verify symlinks are in place:**
```bash
ls -la ~/.hermes/profiles/agent-orchestrator/skills/ | grep '\->'
```

**Pitfall — `ln -s` with trailing slash fails silently:**
When removing a dir before creating a symlink, `rm -rf dir/` (trailing slash) removes
the dir's **contents** but leaves an empty directory. `ln -s` then fails because the
target name already exists as an empty dir. Fix: no trailing slash in `rm -rf`.
```bash
# WRONG — leaves empty dir, ln -s fails silently
rm -rf "$skill_path/"
ln -s "$repo_skill" "$skill_path/"

# CORRECT
rm -rf "$skill_path"
ln -s "$repo_skill" "$skill_path"
```

**Pitfall — `set -e` + bash arithmetic counters:**
`(( counter++ ))` returns exit code 1 when counter == 0, which triggers `set -e` and kills
the script. Fix: use `set +e` before the loop, or `(( counter++ )) || true`.
```bash
set +e   # add before loop with arithmetic counters
converted=0
for ...; do
  (( converted++ ))
done
```

Dynamic resolution + version locking tracked as Epic #285.

## GitHub CLI (gh) in Hermes agent sessions

Hermes remaps `HOME` to the profile home — `gh` reads the wrong `hosts.yml`, no token.
**Do NOT ask user to re-auth every session.** Always use:

```bash
GH_CONFIG_DIR=/home/puterakahfi/.config/gh gh issue create ...
GH_CONFIG_DIR=/home/puterakahfi/.config/gh gh auth status
```

See `references/gh-cli-hermes-session.md` for full diagnosis and one-time fix.

## Pitfall: SKILL.md description field YAML parse error (silent install skip)

If a skill's `description:` contains a colon (`:`) the YAML parser can fail with:
```
Nested mappings are not allowed in compact mappings at line 2, column 14
```
`npx skills add` silently skips it with `⚠ Skipped` — **no error exit code**.

**Fix**: quote the description value:
```yaml
# WRONG — fails when description contains ': '
description: Use when agent-orchestrator needs to run the review loop and synth…

# CORRECT
description: "Use when agent-orchestrator needs to run the review loop and synth…"
```

Affected as of 2026-07-31: `hermes-auto-routing-review-synthesis` (tracked in #309).

## Fleet ADLC readiness

See `references/fleet-gap-tracker.md` for current gap status, specialist profile audit state,
and dispatch mode verification.
