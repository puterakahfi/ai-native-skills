---
name: hermes-profile-tooling
description: "Use when Hermes profile tooling or Cua Driver GUI input delivery misbehaves."
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: agent-orchestrator
  ai-native-skills.type: skill
  ai-native-skills.runtime: hermes
---

# Hermes Profile Tooling

Use this runbook when Hermes profile sessions or runtime tools behave differently from a normal shell or desktop session. It captures durable fixes that must survive Hermes reinstall, profile bootstrap, and fleet reconciliation.

## Scope

Covers recurring Hermes runtime/profile failure classes:

1. `computer_use` / Cua Driver background delivery returns `background_unavailable` on Linux/X11.
2. Profile-local `HOME` remapping makes CLI tools read the wrong config location.
3. Skill install/frontmatter parsing fails because YAML values are not quoted safely.

Do not use this skill to bypass product, security, operations, routing, or approval gates. Diagnose the runtime/tooling failure first, then return to the governing workflow.

---

## Cua Driver `background_unavailable` on Linux/X11

### Symptom

A `computer_use` action such as `scroll`, `click`, or `type` returns a tool-runtime error/result like:

```text
code: background_unavailable
escalation.recommended: foreground
```

The result may explain that background delivery is not available for the target surface.

### Cause

This is a Cua Driver input-delivery limitation, not a product task failure, chat-routing refusal, Jira/Kanban failure, or direct-chat policy issue. On Linux/X11, some target surfaces (commonly Chrome/Electron/GTK/canvas/native web surfaces) do not expose a focus-free input backend. The remaining XTest/X11 path can only deliver to the globally focused widget.

### Mandatory fallback

For GUI-driving agents, this ladder is non-negotiable:

```text
If computer_use returns code=background_unavailable and escalation.recommended=foreground,
retry the exact same computer_use action once with delivery_mode="foreground".
Do not retry background mode for the same target/action.
After any foreground action that is unverifiable, capture fresh state before continuing.
```

Example fallback for a failed background scroll:

```json
{
  "action": "scroll",
  "direction": "down",
  "amount": 3,
  "delivery_mode": "foreground"
}
```

Example fallback for a failed background click:

```json
{
  "action": "click",
  "element": 14,
  "delivery_mode": "foreground"
}
```

### Diagnosis checklist

1. Confirm the error is from a `computer_use` tool result.
2. Confirm the result has `code: background_unavailable` and `escalation.recommended: foreground`.
3. Retry the same action once with only `delivery_mode` changed to `foreground`.
4. If the foreground result is `confirmed`, continue. Do not repeat successful input.
5. If the foreground result is `unverifiable`, capture fresh state and inspect before any retry.
6. If the recommendation is `page`, use the typed browser rung (`cua_browser_*`) instead of native foreground.
7. If foreground is refused or still fails, stop and report the exact Cua Driver evidence.

### Pitfalls

- Do not loop on background delivery after `background_unavailable`.
- Do not diagnose this as direct-chat restrictions unless the session evidence shows an actual chat/profile-routing refusal.
- Do not diagnose this as a Jira, Kanban, product-intake, or business-task problem.
- Foreground mode briefly activates the target window and restores focus afterward. Mention this trade-off when the user is actively using the desktop.
- Do not click permission dialogs, password prompts, payment UI, or sensitive consent surfaces unless the user explicitly authorized that action.

---

## HOME remapping in Hermes profile sessions

Hermes profile sessions can remap `HOME` to the profile directory, for example:

```text
/home/<user>/.hermes/profiles/<profile>/home
```

CLI tools that store config in `~/.config` may then read the profile home instead of the real user home.

### Symptom

A CLI reports not authenticated or not configured even though the real user shell is already configured.

Common examples:

- `gh` reads `~/.config/gh/hosts.yml`.
- `aws` reads `~/.aws/`.
- `gcloud` reads `~/.config/gcloud/`.
- Other XDG tools read under `~/.config`.

### Durable fix

Symlink the real config directory into each Hermes profile home that needs it:

```bash
mkdir -p /home/<user>/.hermes/profiles/<profile>/home/.config
ln -sfn /home/<user>/.config/gh   /home/<user>/.hermes/profiles/<profile>/home/.config/gh

gh auth status
```

Alternative per-call environment overrides can work but are fragile because every call must carry the override.

---

## YAML frontmatter parse errors during skill install

`npx skills add` parses `SKILL.md` YAML frontmatter. Unquoted characters such as colon-space, unicode arrows, and em-dashes can trigger YAML parser errors.

### Rule

Quote `description:` values when they contain punctuation or are long:

```yaml
# Wrong
description: State ladder: executed→reviewed→approved — no skipping.

# Correct
description: "State ladder: executed->reviewed->approved, no skipping."
```

### Verify

```bash
python3 - <<'PY'
from pathlib import Path
import yaml
text = Path('skills/<skill-name>/SKILL.md').read_text()
yaml.safe_load(text.split('---', 2)[1])
print('YAML OK')
PY
```

## Output contract

When using this runbook, report:

- The exact runtime/tooling symptom.
- The diagnosis and why unrelated routing/product causes were ruled out.
- The fallback or durable profile fix applied.
- Verification output, including the fresh capture/state check after unverifiable GUI input.
