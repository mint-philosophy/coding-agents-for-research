---
description: Agent suspension protocol - pause session for later resumption without losing context
---

# Agent Suspend Protocol

**Use this when you need to pause work and come back later — hours or days from now.**

Unlike `/end`, suspending:
- Keeps your session files in `sessions/active/`
- Does NOT merge work to main logs (work is incomplete)
- Marks the session as intentionally paused, not abandoned
- Preserves all context for seamless resumption

---

## When to Suspend vs End

| Situation | Use |
|:----------|:----|
| Work is complete, ready to archive | `/end` |
| Work is incomplete but stopping for now | `/suspend` |
| Switching to a different task entirely | `/end` current, `/init` new |
| Taking a break, will return to same work | `/suspend` |

---

## Suspend Checklist

**Complete ALL steps before signing off.**

### Step 1: Document Current State

1. ☐ **Update your session log** with current status:
   ```markdown
   | YYYY-MM-DD HH:MM | Agent-[last-4] | Session suspended. |
   ```

2. ☐ **Add suspension notes** — What should your future self (or another agent) know?
   - Where exactly did you stop?
   - What's the next step when resuming?
   - Any blockers or waiting-on items?
   - Relevant file paths or context

### Step 2: Update Session Metadata

3. ☐ **Update session JSON** (`sessions/active/[SESSION_ID].json`):
   ```json
   {
     "session_id": "...",
     "start_time": "...",
     "suspended_at": "YYYY-MM-DDTHH:MM:SS+TZ",
     "project": "...",
     "status": "suspended",
     "suspension_note": "Brief description of where work paused and what's next"
   }
   ```

### Step 3: Verify

4. ☐ **Confirm files remain in `sessions/active/`** — do NOT move to completed
5. ☐ **Confirm status is "suspended"** — not "active", "completed", or "aborted"

---

## Resuming a Suspended Session

When the user returns to continue the work:

1. **If same conversation context** (Cursor remembers the chat):
   - Simply continue where you left off
   - Update session JSON: change status back to `"active"`, remove `suspended_at`
   - Add resume note to session log

2. **If new conversation** (fresh context):
   - Run `/init`
   - When checking `sessions/active/`, you'll see your suspended session
   - Read the suspension note and session log to restore context
   - Update the existing session (don't create a new one) — change status to `"active"`

---

## Example Suspension

**Session log entry:**
```markdown
| 2025-12-04 15:30 | Agent-1bdb | Session suspended. |

### Suspension Notes
- **Stopped at**: Finished taxonomy, about to start research plan draft
- **Next step**: Draft Section 4 of research-plan.md
- **Waiting on**: Nothing — ready to continue
- **Key files**: projects/my-project/PLANNING/research-plan.md
```

**Session JSON:**
```json
{
  "session_id": "20251204-102216-1bdb",
  "start_time": "2025-12-04T10:22:16+11:00",
  "suspended_at": "2025-12-04T15:30:00+11:00",
  "project": "my-project",
  "status": "suspended",
  "launch": "cursor",
  "suspension_note": "Finished taxonomy, next: draft Section 4 of research-plan.md"
}
```

---

## The Sign-Off

When suspending, end with a brief status and the suspension marker:

> **Agent-1bdb suspending.** Taxonomy complete, research plan draft next. Session preserved in `sessions/active/`.

No elaborate sign-off — you'll be back.
