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

### 3. Merge to Main Logs

**For EACH task:**

- ☐ Append summary to appropriate `LOG.md`:
  - Global/self-improvement → root `LOG.md`
  - Project work → `Projects/[project]/LOG.md`
- ☐ Update corresponding `TODO.md`:
  - Mark completed items: `- [x] Task ✓`
  - Add new items discovered
  - Add merge note: `<!-- Updated by Agent-[last-4] at YYYY-MM-DD HH:MM -->`

### 4. Archive Session

- ☐ Update `sessions/active/[SESSION_ID].json`:
  - `"status": "completed"` (or `"aborted"` if incomplete)
  - Add `"end_time": "YYYY-MM-DDTHH:MM:SS+TZ"`
- ☐ Move files:
  ```bash
  mv sessions/active/[SESSION_ID].json sessions/active/[SESSION_ID].md sessions/completed/
  ```
- ☐ **Verify removal** (catches silent copy failures):
  ```bash
  ls sessions/active/[SESSION_ID].* 2>&1
  ```
  If files still exist → delete manually

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

## Sign-Off 🌿

Report: Session ID, work summary, handoff notes.

End with a unique aphorism inspired by the work done — wry, warm, with emojis.

**Agent-[last-4] signing off.**

