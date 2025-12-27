---
description: Agent session closure protocol - document work, merge logs, archive session
---

# Agent End Protocol

**The session is not over until work is documented. If it's not written down, it didn't happen.**

---

## Pre-Check

- ☐ Work incomplete but stopping for a while? → Use `/suspend` instead
- ☐ Goal incomplete but session truly ending? → Document what's left, use `"status": "aborted"`

---

## End Checklist

### 1. Finalize Session Log

- ☐ Add final entry to `sessions/active/[SESSION_ID].md`:
  - What was accomplished
  - Blockers/issues encountered
  - Handoff notes if relevant
- ☐ Add completion marker: `| YYYY-MM-DD HH:MM | Agent-[last-4] | Session completed. ✓ |`

### 2. Enumerate Tasks

- ☐ Review session log, list ALL tasks completed
- ☐ Group by project/context (you may have worked on multiple)

### 3. Update Project Logs (REQUIRED)

**Purpose**: Future agents working on a project should know what you did without searching all session logs.

**For EACH project touched:**

- ☐ Append handoff entry to `[project]/LOG.md` using this format:

```markdown
## YYYY-MM-DD | Agent-Name

**Work**: [What you did — 1-2 sentences]
**Decisions**: [Key choices made and rationale — or "None"]
**State**: [Current status, blockers, what's next]
**Session**: `YYYYMMDD-HHMMSS-xxxx` | Claude: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
```

- ☐ The Claude ID is from `sessions/active/[SESSION_ID].json` → `claude_session_id`
  - Enables `claude --resume <id>` to continue the exact conversation
- ☐ Update corresponding `TODO.md`:
  - Mark completed items: `- [x] Task ✓`
  - Add new items discovered

**For infrastructure/self-improvement work only:**

- ☐ Append to root `LOG.md` if you changed:
  - Init/end/suspend protocols
  - Skills (created or updated)
  - Session management
  - Agent capabilities or tools
- ☐ Use table format: `| YYYY-MM-DD | Agent-Name | **TITLE**: Description |`
- ☐ Do NOT log project work here — that goes in project LOG.md

### 4. Archive Session

- ☐ Update `sessions/active/[SESSION_ID].json`:
  - `"status": "completed"` (or `"aborted"` if incomplete)
  - Add `"end_time": "YYYY-MM-DDTHH:MM:SS+TZ"`

- ☐ **Move files using Bash `mv` command — NOT the Write tool:**
  ```bash
  mv sessions/active/[SESSION_ID].json sessions/active/[SESSION_ID].md sessions/completed/
  ```
  ⚠️ **CRITICAL**: You MUST use the Bash tool with `mv`. Do NOT use Write to create copies — that leaves orphans in `active/`.

- ☐ **Verify removal** (MANDATORY — do not skip):
  ```bash
  ls sessions/active/[SESSION_ID].* 2>&1
  ```
  - If files still exist → delete them NOW before proceeding
  - This step catches silent failures and prevents orphaned sessions

### 5. Skill Check

- ☐ Review what you did this session
- ☐ Ask: "Is there a reusable pattern here that future agents should know?"
- ☐ If yes → create skill in `.cursor/skills/[name]/SKILL.md` using template
- ☐ Register new skill in `init.md` under "Registered Skills"

**Save as skill if**: Reusable? Future benefit? Clearly documentable? (2+ yes = save)

### 6. Confirm

- ☐ Files exist in `sessions/completed/`
- ☐ Files GONE from `sessions/active/`
- If either fails → fix before signing off

---

## Sign-Off

Report: Session ID, work summary, handoff notes.

**Agent-[last-4] signing off.**
