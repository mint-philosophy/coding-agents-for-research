# Updates

New discoveries and improvements, in reverse chronological order.

---

## December 2025

### Corpus Search & Big Project Patterns (Dec 27)

Built a semantic search system over 1,200+ research papers — the kind of project that takes multiple agent sessions across several days. The experience crystallized several patterns now in the skills library:

**Big Project Planning**: The VISION.md → PLAN.md → EXECUTION.md structure for multi-phase work. Key insight: always run a pilot on ~25 items before processing 1,000+. Our pilot caught that initial topic questions missed important dimensions and that Sonnet quality was insufficient for nuanced analysis — issues that would have been expensive to discover at full scale.

**Batch Task Verification**: Agents often claim "done" after starting a background process. This skill provides a 4-phase verification protocol: check process status, measure coverage metrics, run functional tests, sample quality. Prevents cascade failures in dependent tasks.

**Deep Understanding Over Statistics**: Statistical clustering found 29 topic clusters but missed "LLM Psychology" entirely (52 papers). Claude semantic analysis immediately identified it. Lesson: if the task requires understanding content, use Claude. Statistical methods are for scale after validation.

**Files**: `.cursor/skills/big-project-planning/`, `.cursor/skills/batch-task-verification/`

---

### Hooks & Context Management (Dec 27)

Added lifecycle hooks for Claude Code that run automatically at key events. The most useful is the **context threshold hook** — it monitors token usage and warns the agent at 90% capacity to wrap up and run `/end`.

**Why it matters**: Agents degrade as context fills. Without intervention, they often try to continue past their useful window, producing lower-quality work. The hook prompts graceful handoff.

**Files**: `.claude/hooks/context-threshold.py`, `.claude/settings.json`

---

### Multi-Agent Coordination (Dec 26)

Created a skill for coordinating work across multiple agent sessions. Key insight: agents can't coordinate with each other directly, so you need a **single source of truth** (EXECUTION.md) that all agents read and update.

**The pattern**:
- Create EXECUTION.md with task list and status symbols
- Each agent claims tasks before starting (`[ ]` → `[~]`)
- Each agent marks complete with verification (`[~]` → `[x]`)
- Handoff notes enable the next agent to continue

**Files**: `.cursor/skills/multi-agent-coordination/SKILL.md`

---

### Metacognitive Strategies (Dec 25)

Added several thinking patterns to the init protocol:

- **Context Degradation Awareness**: Long contexts degrade performance. Watch for lost-in-middle effects, context poisoning, and distraction.
- **Deep Understanding Over Statistics**: Semantic analysis beats clustering. Run a pilot with Claude before committing to statistical pipelines.
- **Quality Over Expedience**: Don't accept coarse solutions. Iterate until granularity matches the need.

---

## November 2025

### Initial Release

First public version of the agent workspace template, including:
- Init and end protocols
- Session logging system
- Skills framework
- Documentation triad (README/LOG/TODO)

---

*Add new entries above this line.*
