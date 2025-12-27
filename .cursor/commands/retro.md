---
description: Retrospective protocol - identify friction, extract learnings, update skills
---

# Agent Review Protocol

**Purpose**: Structured reflection to improve agent performance over time. Identify what worked, what didn't, and update skills/processes accordingly.

Inspired by ARTEMIS (arXiv:2512.09108): measure outcomes → identify patterns → refine configurations.

---

## When to Run

- End of day (recommended)
- After a session with notable friction
- Weekly batch review across multiple sessions
- After completing a complex multi-session project

---

## Review Checklist

### 1. Friction Scan (5 min)

**Review recent sessions**, not just the current one:

```bash
# List recent sessions
ls -lt sessions/active/*.md sessions/completed/*.md 2>/dev/null | head -12

# Read each one to understand what happened
```

Then scan for friction indicators:

```bash
grep -i -E "(error|failed|stuck|retry|clarif|confused|wrong|fix|blocked|bug)" sessions/completed/*.md 2>/dev/null | head -20
```

Also check across sessions:
- Tasks that required multiple attempts
- Handoff issues between agents
- Questions asked to user that could have been avoided
- Scripts that failed or had bugs
- External blockers (API limits, permissions, etc.)

**Output**: List of candidate friction points across recent sessions

---

### 2. Pattern Classification (3 min)

For each friction point, classify:

| Type | Symptoms | Target |
|:---|:---|:---|
| **Prompt Issue** | Unclear instructions, misunderstood intent | Update command `.md` file |
| **Skill Gap** | Missing knowledge, no existing skill | Create new skill |
| **Skill Decay** | Outdated skill, changed context | Update existing skill |
| **Tool Issue** | API errors, permissions, timeouts | Log for user |
| **Process Gap** | Missing checklist step, wrong order | Update `init.md` |
| **Context Issue** | Lost-in-middle, poisoned context | Note for future sessions |

**Output**: Classified list with targets

---

### 3. Success Scan (2 min)

Also identify what worked well:
- Tasks completed smoothly on first attempt
- Skills that proved useful
- Processes that prevented errors

Ask: "Is there a reusable pattern here that isn't yet captured?"

**Output**: Candidate patterns for new skills

---

### 4. Define Success Criteria (1 min per issue)

For each friction point, articulate:

> "Next time [situation], the agent should [desired behavior] because [rationale]."

Example:
> "Next time using `/end`, the agent should use Bash `mv` instead of Write tool because Write creates copies without deleting originals."

**Output**: Clear improvement goals

---

### 5. Semantic Updates (variable)

Apply fixes while preserving core purpose:

| Action | Process |
|:---|:---|
| **New skill** | `mkdir .cursor/skills/[name]` → copy template → fill → register in init |
| **Update skill** | Edit SKILL.md → increment version → update `updated:` date |
| **Update init.md** | Add to relevant section (metacognition, checklist, etc.) |
| **Update command** | Edit `.cursor/commands/[name].md` |

**Commit message format**: `refactor(skills): [what changed] - learned from [session ID]`

---

### 6. Log the Review

Append to root `LOG.md`:

```markdown
## Retrospective: YYYY-MM-DD

**Sessions reviewed**: [list session IDs]

### Friction Points
| Issue | Classification | Action Taken |
|:---|:---|:---|
| [description] | [type] | [created/updated X] |

### Successes
- [what worked well]

### Pending
- [issues requiring user input or external fixes]
```

---

## Quick Review (5 min version)

When time is short:

1. ☐ Scan for errors/retries in session log
2. ☐ Pick the ONE biggest friction point
3. ☐ Classify it and define success criteria
4. ☐ Make the fix (or log if external)
5. ☐ One-line entry in `LOG.md`

---

## Tracking Effectiveness

When a similar situation arises later:

1. Did the fix help?
2. If yes → skill is validated
3. If no → iterate: refine the skill or try different approach
4. Log outcome either way

Over time, this creates an evidence-based skill library.

---

## Integration

This command is standalone. Run it when you have time for reflection.

For lighter ongoing learning, the `/end` command includes a "Skill Check" step — use that for in-the-moment pattern recognition.

`/retro` is for deeper, systematic improvement.
