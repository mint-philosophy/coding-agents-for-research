---
name: big-project-planning
description: Use when setting up large parallelizable projects — creates VISION.md, PLAN.md, EXECUTION.md structure for multi-agent work
created: 2025-12-27
updated: 2025-12-27
version: 1.0.0
triggers: ["big project", "large task", "parallelizable", "multi-phase", "set up project", "plan project", "break down task", "execution plan"]
scope: [meta, admin, research, coding]
---

# Big Project Planning

How to structure large projects for efficient multi-agent execution with maximum parallelization.

## When to Use

- Task requires >4 hours of LLM processing
- Work has natural phases or tiers
- Multiple independent subtasks can run in parallel
- Will require handoffs between agent sessions
- Involves batch processing (many items × same operation)

**NOT for:**
- Quick tasks (<2 hours)
- Linear work with no parallelization opportunity
- Exploratory research without clear deliverables

---

## Critical Design Principles

### 1. Deep Understanding Over Statistics

**Favor semantic understanding over statistical patterns.**

- Use LLM intelligence (subagents) over deterministic programs when there's a choice
- Statistical methods (clustering, embeddings, regex) find geometric patterns but miss meaning
- Always validate that statistical approaches capture what semantic analysis would reveal
- When in doubt, run a pilot with Claude analysis before committing to a statistical pipeline

**Example**: Topic clustering may produce 29 clusters but miss a conceptual theme entirely. Claude semantic analysis on the same documents immediately identifies it.

**Rule**: If the task requires understanding content, use Claude. Only fall back to statistical methods for scale after validating they capture the same insights.

### 2. Quality First During Planning

**During planning**: Assume expense is not an object. Design for quality.

**During execution**: Be cost-conscious. Use the most efficient method that achieves the quality goal.

### 3. Pilot Before Full Run

**Always run a small pilot to validate the approach.**

- Select representative sample (e.g., 25 items from 1000)
- Include edge cases if known
- Run full pipeline on pilot set
- Analyze results for quality and issues
- Iterate if needed before full run

---

## The Three Documents

Every big project needs three planning documents:

| Document | Purpose | When Created |
|:---------|:--------|:-------------|
| **VISION.md** | Why we're doing this, architecture, success metrics | First — sets direction |
| **PLAN.md** | Phases, tiers, execution order, cost estimates | Second — structures work |
| **EXECUTION.md** | Detailed tasks, dependencies, claim protocol | Third — enables multi-agent |

### 1. VISION.md — The "Why"

```markdown
# [Project Name]: Vision

## Problem Statement
[What problem are we solving? Why now?]

## Goals
1. [Primary goal]
2. [Secondary goals]

## Non-Goals
- [What we're explicitly NOT doing]

## Architecture
[High-level approach, key decisions]

## Success Metrics
| Metric | Target |
|:-------|:-------|
| [Metric 1] | [Value] |

## Constraints
- Budget: [if applicable]
- Timeline: [if applicable]
- Dependencies: [external factors]
```

### 2. PLAN.md — The "What"

```markdown
# [Project Name]: Plan

## Current State
[What exists now, what's working, what's not]

## Enhancement Tiers

### Tier 1: Foundation (Immediate)
| Task | Description | Cost | Effort |
|:-----|:------------|:-----|:-------|
| 1.1 | [Task] | [Subagent/API $X] | [Hours] |

### Tier 2: Core Features (Short-term)
[...]

## Recommended Execution Order

**Phase A**: Tier 1 complete
1. Task 1.1 (prerequisite for all)
2. Tasks 1.2, 1.3 (parallelizable)
3. Task 1.4 (depends on 1.2, 1.3)
```

### 3. EXECUTION.md — The "How"

See `multi-agent-coordination` skill for full template. Key elements:
- **Agent Protocol**: Read → Find task → Verify prereqs → Claim → Execute → Complete → Handoff
- **Task Status Key**: `[ ]` Available, `[~]` Claimed, `[x]` Complete, `[!]` Blocked
- **Dependency Graph**: ASCII visualization
- **Verification Commands**: How to confirm each task is done

---

## Task Decomposition

### The 2-Hour Rule

Break tasks so each can complete in ≤2 hours:

| Task Size | Duration | Action |
|:----------|:---------|:-------|
| Small | <30 min | Combine with others |
| Medium | 30min-2hr | Perfect size |
| Large | 2-4hr | Split or run as background |
| XL | 4hr+ | Must split into subtasks |

### Identifying Parallelization

**Parallelizable** (no shared state):
- Processing different files
- Analyzing different documents
- Running independent tests
- Batch operations on disjoint data

**Sequential** (dependencies):
- Task B needs output from Task A
- Database must exist before queries
- Index must be built before search

### Dependency Mapping

Use ASCII diagrams:

```
PHASE 1: DATA ENRICHMENT
├── 1.1 Setup ────────────────────────── REQUIRED FIRST
├── 1.2 Process Type A ─────────────┬── After 1.1
├── 1.3 Process Type B ─────────────┤   (parallelizable)
├── 1.4 Combine results ────────────┘── After 1.2, 1.3
└── 1.5 Analysis ─────────────────────── After 1.4

PHASE 2: IMPLEMENTATION
├── 2.1 Core module ──────────────────── After Phase 1
└── 2.2 Testing ──────────────────────── After 2.1
```

---

## Batch Processing Pattern

For "process N items" tasks:

### 1. Determine Batch Size

```
Total items: 1,000
Parallel agents: 10
Batch size: ceil(1000 / 10) = 100 items each
```

### 2. Create Parallel Dispatch

```markdown
### Task 1.5: Process All Items

**Parallel execution**:
- [ ] Batch 1: items 0-99 — Agent A
- [ ] Batch 2: items 100-199 — Agent B
...
- [ ] Batch 10: items 900-999 — Agent J
```

### 3. Merge Results

```bash
cat output_batch*.jsonl > full_results.jsonl
```

---

## Project Setup Checklist

### Phase 0: Scoping
- [ ] Understand the goal
- [ ] Identify total work volume
- [ ] Estimate if subagents suffice or API needed

### Phase 1: Planning
- [ ] Create VISION.md → PLAN.md → EXECUTION.md
- [ ] Map dependencies, identify parallelization
- [ ] Draw dependency graph

### Phase 2: Plan Verification ⚠️ REQUIRED
- [ ] Present plan to user for sign-off
- [ ] Include: approach, cost estimate, timeline, risks

### Phase 3: Pilot Run ⚠️ REQUIRED
- [ ] Run on small sample (~25 items)
- [ ] Analyze results for quality
- [ ] Iterate if needed
- [ ] Only proceed after pilot validates approach

### Phase 4: Execution
- [ ] Get final authorization
- [ ] Dispatch parallel agents
- [ ] Monitor, verify, handoff

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|:-------------|:--------|:---------|
| No VISION.md | Agents don't understand "why" | Start with goals |
| Monolithic tasks | Can't parallelize | Break into 2-hour chunks |
| Skipping pilot | Costly mistakes at scale | Always pilot first |
| Implicit dependencies | Wrong execution order | Draw explicit graph |
| No verification | "Done" without proof | Add verification per task |

---

## Integration with Other Skills

- **multi-agent-coordination**: EXECUTION.md template and handoff patterns
- **batch-task-verification**: Verification protocol for completed tasks
- **self-improvement**: Learn from project outcomes

---

*The pilot run is where you catch design flaws before they become expensive.*
