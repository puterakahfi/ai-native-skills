---
name: hermes-auto-routing-skill-ops
description: "Use when installing or patching auto-routing skills."
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["hermes-fleet-auto-routing","hermes-agent-fleet-bootstrap"]'
---

# Hermes Auto-Routing Skill Ops

Operational playbook for installing, updating, and verifying skills from `puterakahfi/ai-native-skills` into Hermes profiles.

## Install a skill from the repo

```bash
npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y
```

Verify symlink landed:
```bash
ls /home/puterakahfi/.hermes/profiles/agent-orchestrator/skills/ | grep <skill-name>
```

PromptScript "Failed to install" in the output is **not an error** — Hermes symlink still succeeds. Only care about `symlinked: Hermes Agent`.

## Pitfall: YAML frontmatter special characters

Descriptions containing `→`, `—` (em-dash), or bare colons break YAML compact mapping parsing. Error:

```
Skipped <skill>/SKILL.md — YAML parse error: Nested mappings are not allowed in compact mappings at line 2, column 14
```

**Fix**: wrap description in double quotes AND replace Unicode chars with ASCII:

```yaml
# WRONG — will silently skip during npx skills add
description: State ladder: executed→reviewed→approved — no skipping.

# CORRECT
description: "State ladder: executed->reviewed->approved, no skipping."
```

Verify before pushing:
```bash
python3 -c "import yaml; yaml.safe_load(open('SKILL.md').read().split('---')[1]); print('YAML OK')"
```

Fix → commit → push → re-run `npx skills add`.

## Sync installed skills after repo patch

No auto-sync exists. After merging a patch to `puterakahfi/ai-native-skills`:

```bash
cd /data/www/ai-native-skills && git pull origin main
npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y
```

## Fleet skill status (as of 2026-07-31)

Auto-routing skills installed in `agent-orchestrator`:
- `hermes-auto-routing-planner` — planning phase, contract enforcement
- `hermes-auto-routing-review-synthesis` — review loop + synthesis
- `hermes-fleet-auto-routing` — dispatch patterns, receipt schema
