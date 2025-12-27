---
name: multi-agent-coordination
description: Use when planning or executing tasks that span multiple agent sessions — provides patterns for handoff, state tracking, and coordination across context windows
created: 2025-12-26
updated: 2025-12-26
version: 1.0.0
triggers: ["multi-agent", "handoff", "long task", "multiple sessions", "context limit", "coordination", "execution plan"]
scope: [meta, admin, coding]
---

# Multi-Agent Coordination

Patterns for structuring work that exceeds a single agent's context window or requires multiple sessions to complete.

## When to Use

- Task requires 2+ hours of LLM processing
- Task has natural parallelizable components
- Implementation requires multiple distinct phases
- Work will be handed off between agents
- Background processes need monitoring across sessions

## The Core Problem

Each agent session has:
- **Context limits**: Can't hold entire project history
- **Session boundaries**: Work ends when session ends
- **No shared memory**: Next agent starts fresh
- **Verification gaps**: Easy to claim "done" without proof

## Solution Architecture

### 1. Single Source of Truth: EXECUTION.md

Create one file that ALL agents read and update:

```markdown
# Project: Execution Plan

## Agent Protocol
1. Read this entire document
2. Find next AVAILABLE task (status: [ ])
3. Verify prerequisites are COMPLETE ([x])
4. Claim task: [ ] → [~] + session ID
5. Execute with verification
6. Complete: [~] → [x] + date + notes
7. Update COMPLETION LOG
8. Handoff

## Task Status Key
| Symbol | Meaning |
|--------|---------|
| [ ] | Available |
| [~] | In progress (claimed) |
| [x] | Complete (verified) |
| [!] | Blocked |
| [-] | Skipped |

## Tasks

### Phase 1: Foundation
- [x] 1.1 Setup — DONE by Agent-abc1 2025-12-25
- [~] 1.2 Data processing — CLAIMED by Agent-def2
- [ ] 1.3 Validation (depends: 1.2)

### Phase 2: Implementation
- [ ] 2.1 Core module (depends: Phase 1)
...

## COMPLETION LOG
| Date | Agent | Task | Notes |
|------|-------|------|-------|
| 2025-12-25 | Agent-abc1 | 1.1 | Verified 100% coverage |
```

### 2. Task Dependency Graph

Structure tasks with explicit dependencies:

```
PHASE 1: DATA ENRICHMENT
├── 1.1 Metadata extraction ──────────── REQUIRED FIRST
├── 1.2 Re-embedding ─────────────────┬── After 1.1
├── 1.3 Document embeddings ──────────┤   (parallelizable)
├── 1.4 Similarity network ───────────┘── After 1.3
└── 1.5 Clustering ───────────────────── After 1.3

PHASE 2: IMPLEMENTATION
├── 2.1 Core module ──────────────────── After Phase 1
└── 2.2 Testing ──────────────────────── After 2.1
```

**Rules:**
- No task starts until prerequisites are `[x]`
- Parallelizable tasks can be claimed by different agents
- Phase boundaries are hard gates

### 3. Background Process Handoff

When starting a long-running process:

```markdown
## For Next Agent

**Process started**: PID 12345
**Expected duration**: 2-4 hours
**Monitor**: `tail -f data/output.log`

**When complete, verify**:
1. Check: `ps aux | grep script_name`
2. Verify: `python3 -c "...coverage check..."`
3. If >95% coverage, mark Task X.X complete
4. Proceed to Tasks X.Y, X.Z (now unblocked)
```

### 4. Session Logging

Each agent maintains session state:

**Metadata** (`sessions/active/[ID].json`):
```json
{
  "session_id": "20251226-135256-2e3d",
  "start_time": "2025-12-26T13:52:56+11:00",
  "project": "my-project",
  "status": "active",
  "tasks_claimed": ["1.2"],
  "tasks_completed": []
}
```

**Work log** (`sessions/active/[ID].md`):
```markdown
# Session 20251226-135256-2e3d

## Work Log
### 13:52 — Initialization
- Read EXECUTION.md
- Task 1.1 verified complete by previous agent
- Claiming Task 1.2

### 14:30 — Task 1.2 Progress
- Started processing
- 500/1000 complete
...
```

### 5. Verification Before Claiming Complete

Never mark `[x]` without:

1. **Process verification**: Is it still running? Did it finish?
2. **Coverage check**: Does output meet threshold?
3. **Functional test**: Does the output actually work?
4. **Sample inspection**: Do random samples look correct?

## Handoff Patterns

### Clean Handoff (Planned)

Agent finishing a session:
```markdown
## Session End — Handoff Notes

**Completed**: Task 1.1, 1.2
**In progress**: Task 1.3 (background, PID 12345)
**Blocked**: None
**Next agent should**:
1. Check Task 1.3 completion
2. If complete, proceed to Task 1.4
3. Task 1.5 can run in parallel with 1.4
```

### Orphan Recovery (Unplanned)

New agent finding abandoned work:
```markdown
## Recovery Protocol

1. Check `sessions/active/` for recent sessions
2. Read their work logs for context
3. Check EXECUTION.md for [~] claimed tasks
4. Verify claimed task status:
   - If complete → mark [x], update log
   - If failed → mark [!], document blocker
   - If stale → unclaim, mark [ ]
5. Resume from next available task
```

## Context Management

### What to Put in EXECUTION.md
- Task definitions and status
- Dependencies
- Verification commands
- Expected outputs
- Handoff notes

### What to Put in Session Logs
- Detailed work narrative
- Debugging steps
- Decisions made
- Errors encountered

### What to Put in LOG.md (Project)
- High-level session summaries
- Key decisions
- Architecture changes
- Lessons learned

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| No EXECUTION.md | Agents duplicate work | Create single source of truth |
| Claiming without updating | Parallel agents collide | Always update file before starting |
| "Done" without verification | Cascade failures | Use verification protocol |
| No handoff notes | Context lost | Document before session end |
| Monolithic tasks | Can't parallelize | Break into <2hr chunks |
| Implicit dependencies | Wrong execution order | Make dependency graph explicit |

## Task Sizing Guidelines

| Task Size | Duration | Fits in Session? |
|-----------|----------|------------------|
| Small | <30 min | Yes, do multiple |
| Medium | 30min-2hr | Yes, one per session |
| Large | 2-4hr | Split or background |
| XL | 4hr+ | Must split into phases |

**Rule of thumb**: If a task can't complete in one session, it should be broken down or run as a background process with handoff protocol.

---

*Skill created 2025-12-26*
