# AI Native Skills

[![skills.sh](https://skills.sh/b/puterakahfi/ai-native-skills)](https://skills.sh/puterakahfi/ai-native-skills)

Reusable AI agent skills for the AI-native engineering ecosystem. Compatible with any agent that supports the [skills.sh](https://skills.sh) standard — Claude Code, Hermes, Cursor, Codex, and more.

## Install

```bash
# Install a single skill
npx skills add puterakahfi/ai-native-skills@diagram-architect

# Install all skills
npx skills add puterakahfi/ai-native-skills
```

## Available Skills

| Skill | Description |
|---|---|
| `diagram-architect` | Turn architecture, workflows, and contracts into clear diagrams |
| `master-design` | Senior Product Designer / SaaS UI/UX workflows |
| `master-engineer` | Senior Software Engineer best practices and code quality |
| `native-ai-engineer` | AI-native domain contracts, runtime boundaries, layer placement |
| `native-ai-runtime-agent` | Work inside an ai-native-fw product adapter repository |
| `native-ai-runtime-ops` | Operate a Native AI canonical runtime host |

## Structure

```
skills/
├── diagram-architect/
│   └── SKILL.md
├── master-design/
│   └── SKILL.md
├── master-engineer/
│   └── SKILL.md
├── native-ai-engineer/
│   └── SKILL.md
├── native-ai-runtime-agent/
│   └── SKILL.md
└── native-ai-runtime-ops/
    └── SKILL.md
```

## About

Skills are runtime-agnostic — the same `SKILL.md` works across all supported agents. No adapter layer needed.

- Core contracts live in [ai-native-core](https://github.com/puterakahfi/ai-native-core)
- App/product adapter lives in [ai-native-fw](https://github.com/puterakahfi/ai-native-fw)
