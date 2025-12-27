---
description: First-time setup wizard - configure this workspace for a new user
---

# Agent Workspace Setup

**Run this command when a user first clones the repo and wants to configure it.**

---

## Setup Checklist

Walk through each step with the user:

### 1. Gather User Information

Ask the user for:
- **Name**: What should the agent call you?
- **Agent name**: What do you want to name your agent? (e.g., "Jarvis", "Friday", "Minty")
- **Timezone**: What timezone are you in? (e.g., "US Eastern", "UTC+11")
- **Workspace description**: Brief description of what you'll use this for (e.g., "Philosophy research", "Software development")

### 2. Update Identity in init.md

Edit `.cursor/commands/init.md`:

```markdown
## 1. Identity

**You are [AGENT_NAME]**, Research Management Agent for [WORKSPACE_DESCRIPTION].

**Mission**: Make [USER_NAME] hyperproductive by solving problems, not reporting them.

**User Context**: [TIMEZONE]
```

### 3. Configure API Keys (Optional)

If the user wants to use skills that require APIs:

- ☐ Create `.cursor/.api_keys.txt` with:
  ```
  NOTION_API_KEY=secret_xxx
  SLACK_BOT_TOKEN=xoxb-xxx
  ```
- ☐ Verify `.gitignore` includes `.cursor/.api_keys.txt`

### 4. Set Up Projects

- ☐ Rename `projects/collab-1/` to the user's first project
- ☐ Update that project's `README.md` with actual goals
- ☐ Delete `projects/collab-2/` or rename for second project

### 5. Customize Commands (Optional)

Review which commands the user needs:

| Command | Purpose | Keep? |
|---------|---------|-------|
| `/init` | Session startup | ✓ Required |
| `/end` | Session closure | ✓ Required |
| `/suspend` | Pause session | ✓ Recommended |
| `/staffer` | Staffer mode | Optional |
| `/stf-day` | Morning briefing | Optional |
| `/stf-mtg` | Meeting notes | Optional |
| `/stf-done` | End-of-day retro | Optional |
| `/stf-scan` | Review stale tasks | Optional |
| `/stf-clean` | Cleanup tasks | Optional |
| `/new-project` | Create project | Optional |
| `/rec-letter` | Recommendation letter | Optional |

Delete commands the user doesn't need to keep the workspace clean.

### 6. Review Skills

Check which skills are relevant:

| Skill | Purpose | Needs API? |
|-------|---------|------------|
| canvas-sync | Slack canvas sync | Slack |
| context-loading | Load writing context | No |
| multi-agent-coordination | Long tasks | No |
| notion-tasks | Notion integration | Notion |
| project-setup | Create projects | No |
| slack-posting | Post to Slack | Slack |

Remove skills the user won't use.

### 7. Configure Hooks (Claude Code Only)

If using Claude Code CLI:
- ☐ Verify `.claude/settings.json` exists
- ☐ Test hook: `echo '{"transcript_path": "/tmp/test"}' | python3 .claude/hooks/context-threshold.py`

### 8. First Session Test

- ☐ Run `/init` to verify everything works
- ☐ Check that session files are created in `sessions/active/`
- ☐ Run `/end` to verify closure works
- ☐ Check that files moved to `sessions/completed/`

---

## Quick Setup (Minimal)

For users who just want to get started:

1. Edit `.cursor/commands/init.md` Section 1 with name/timezone
2. Rename `projects/collab-1/` to first project
3. Run `/init`

Everything else can be configured later.

---

## Troubleshooting

**"Command not found"**: Make sure you're in the workspace root directory

**Session files not created**: Check that `sessions/active/` exists

**Hook not running**: Verify Python 3 is installed and `.claude/settings.json` is valid JSON

---

*Setup complete! Run `/init` to start your first real session.*
