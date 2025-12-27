# Agent Workspace — Claude Code Instructions

Welcome! This workspace is a template for AI-assisted research and knowledge work.

---

## First Time Setup?

If the user just cloned this repo and needs to configure it:

1. **Run `/setup`** — Read `.cursor/commands/setup.md` and follow its setup wizard
2. This will walk through configuring identity, projects, and API keys

---

## Commands

Commands are instruction files in `.cursor/commands/`. To use them:
- User says `/command-name` (e.g., `/init`, `/end`, `/setup`)
- You READ the corresponding `.cursor/commands/[name].md`
- You FOLLOW the instructions in that file

**Core commands:**
| Command | File | Purpose |
|---------|------|---------|
| `/setup` | `setup.md` | First-time configuration wizard |
| `/init` | `init.md` | Session startup protocol |
| `/end` | `end.md` | Session closure protocol |
| `/suspend` | `suspend.md` | Pause session for later |

---

## Skills

Skills are reusable capabilities in `.cursor/skills/[name]/SKILL.md`. Load them when relevant:
- `multi-agent-coordination` — For tasks spanning multiple sessions
- `context-loading` — For loading context when writing
- `notion-tasks` — For Notion API integration
- `slack-posting` — For Slack messaging

---

## Workspace Structure

```
├── projects/           # Collaborative research projects
├── side-projects/      # Personal experiments
├── corpus/             # Research by others (papers, readings)
├── publications/       # User's published writing
├── research-essays/    # Non-project writing
├── grants/             # Grant applications, admin
├── sessions/active/    # Current session logs
├── sessions/completed/ # Archived sessions
```

Each project has: `README.md` (goals), `LOG.md` (history), `TODO.md` (next steps)

---

## Key Principles

1. **Evidence over claims** — Verify, don't assume
2. **Document everything** — If not written, didn't happen
3. **Persistence over punt-backs** — Try 3+ approaches before asking
4. **Complete the checklist** — All items, not just comfortable ones

---

## For Established Sessions

If the workspace is already configured:
1. Run `/init` to start a session
2. Work on tasks
3. Run `/end` when done

---

*Read `.cursor/commands/init.md` for the full protocol.*
