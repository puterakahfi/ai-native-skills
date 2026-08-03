# gh CLI in Hermes Agent Sessions

## Root cause

Hermes agent sessions remap `HOME` to the profile home:
```
/home/puterakahfi/.hermes/profiles/agent-orchestrator/home
```

`gh` reads `~/.config/gh/hosts.yml` from this path — which typically has no `oauth_token`,
even if the real user home (`/home/puterakahfi/.config/gh/hosts.yml`) does.

Result: `gh auth status` returns "not logged in" on every agent session even though
the user auth'd fine before. User gets frustrated by repeated auth prompts.

## Fix — always use GH_CONFIG_DIR

Prefix every `gh` call with the real config dir:

```bash
GH_CONFIG_DIR=/home/puterakahfi/.config/gh gh issue create ...
GH_CONFIG_DIR=/home/puterakahfi/.config/gh gh pr list ...
GH_CONFIG_DIR=/home/puterakahfi/.config/gh gh auth status
```

## If token also missing from real home

User runs once in a real terminal (not agent session):

```bash
GH_CONFIG_DIR=/home/puterakahfi/.config/gh gh auth login --git-protocol ssh
```

## Rule

Do NOT ask the user to re-auth every session.
Do NOT conclude "gh is broken" — it's a HOME remapping issue, not a tool failure.
Try GH_CONFIG_DIR workaround first, always.
