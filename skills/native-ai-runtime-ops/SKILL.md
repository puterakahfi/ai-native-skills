---
name: native-ai-runtime-ops
description: Use when operating a Native AI canonical runtime host: SSH/Tencent Cloud/VPS access, Hermes profile bootstrap, tmux/gateway service setup, project checkout, backup/restore, and single-writer session-state safety.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [native-ai, runtime-ops, ssh, cloud, hermes-profile, backup, sessions]
    related_skills: [native-ai-engineer, native-ai-runtime-agent, hermes-agent]
---

# Native AI Runtime Ops

## Overview

Use this skill when Hermes should act as a runtime operations engineer for a Native AI workspace.

It handles the operational layer:

```text
cloud/VPS host -> SSH -> canonical Hermes profile -> project checkout -> tmux/gateway -> backups -> client access
```

It does not decide domain architecture. Use `native-ai-engineer` for layer boundaries and contracts.

## When to Use

Use for:

- connecting to Tencent Cloud/VPS over SSH
- creating local SSH config aliases
- turning a remote host into the canonical Hermes runtime
- installing `hermes-native-ai-engineering-profile`
- installing profile skills from `skills.lock.yaml`
- cloning/updating Native AI project repositories on the host
- setting up tmux, gateway, cron, or systemd for persistent runtime use
- backing up/restoring Hermes profile state
- checking single-writer state safety for sessions and SQLite DBs

## Safety Rules

Never ask the user to paste private keys, passwords, tokens, `.env`, or `auth.json` into chat.

Never commit these to Git:

```text
state.db
state.db-wal
state.db-shm
sessions/
memories/
cron/
auth.json
.env
.env.*
logs/
cache/
secrets/
tokens/
credentials/
```

For shared sessions, prefer one canonical runtime host with clients connecting remotely. Do not active-active sync live Hermes SQLite state.

## SSH Setup Pattern

Collect:

```text
OS image
public IP or DNS
username
login method: key/password
local key path if key-based
```

Example SSH config:

```sshconfig
Host native-ai-runtime
  HostName <PUBLIC_IP_OR_DNS>
  User <USER>
  IdentityFile ~/.ssh/tencent-native-ai.pem
  IdentitiesOnly yes
  ServerAliveInterval 30
  ServerAliveCountMax 4
```

Verify with a harmless command:

```bash
ssh native-ai-runtime 'hostname && whoami && uname -a'
```

## Tencent Cloud Notes

Typical usernames depend on image:

```text
Ubuntu: ubuntu
Debian: debian
CentOS/TencentOS: root or centos
```

Tencent Cloud Security Group must allow inbound TCP 22 from the user's IP or a deliberately chosen source range. Prefer SSH key auth over password auth.

## Canonical Runtime Bootstrap

On the remote host:

```bash
hermes profile install https://github.com/puterakahfi/hermes-native-ai-engineering-profile --name ai-native-engineering -y
~/.hermes/profiles/ai-native-engineering/scripts/install-skills.sh ai-native-engineering
hermes -p ai-native-engineering doctor
```

Then configure local-only auth/model:

```bash
hermes -p ai-native-engineering model
hermes -p ai-native-engineering auth
hermes -p ai-native-engineering config check
```

Daily use:

```bash
ssh native-ai-runtime
tmux new -A -s hermes-ai
cd ~/projects/native-ai-fw
hermes -p ai-native-engineering --continue
```

## Backup Pattern

Backups may contain secrets/session state, so store encrypted and private, never in source/profile Git repos.

```bash
mkdir -p ~/backups/hermes
hermes profile export ai-native-engineering -o ~/backups/hermes/ai-native-engineering-$(date +%F).tar.gz
```

## Verification Checklist

- [ ] SSH command reaches intended host.
- [ ] Security group/firewall permits only intended access.
- [ ] Hermes profile is installed under the canonical runtime host.
- [ ] `skills.lock.yaml` materializes expected skills.
- [ ] Model/auth are configured locally on the host.
- [ ] Project repo exists on the host.
- [ ] Users connect as clients; they do not sync live state.
- [ ] Backup target is private/encrypted and outside Git.
