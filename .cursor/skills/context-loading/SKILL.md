---
name: context-loading
description: Use when loading prior work for writing tasks — provides patterns for judicious context selection to match voice and style
created: 2025-12-27
updated: 2025-12-27
version: 1.0.0
triggers: ["write as me", "match my style", "load context", "prior work", "voice", "drafting"]
scope: [writing, research]
---

# Context Loading

Load relevant prior work before writing tasks to match the user's voice and style.

## Core Principle

Context loading should be **judicious**. Don't load 50 files for every question.

**Heuristic**: If the user is asking you to write *as them* or *for them*, you probably need context. If they're asking you to *do something*, you probably don't.

## When to Load Context

**Load context when:**
- Writing in user's voice (grants, essays, public posts)
- Drafting content about user's projects
- Preparing materials that reference prior work

**Skip context loading when:**
- Task is operational (file management, scripts)
- Task is about external information
- User has provided sufficient context in prompt

---

## Context Sources

### 1. Writing Style & Voice

**When needed**: Drafting grants, essays, public communication

| Source | Path | What It Provides |
|:---|:---|:---|
| Research essay drafts | `research-essays/` | Work-in-progress prose |
| Grant applications | `grants/[name]/` | Compressed, persuasive writing |
| Publications | `publications/` | Polished final versions |

**Process**:
1. Identify the genre (grant, essay, blog post)
2. Find 1-2 examples of the same genre
3. Read opening paragraphs to absorb tone and structure
4. Look for `.md` files first — PDFs are harder to parse

---

### 2. Current Projects

**When needed**: Writing about your research; connecting tasks to themes

| Source | Path | What It Provides |
|:---|:---|:---|
| Project READMEs | `projects/[name]/README.md` | Goals, team, research questions |
| Project logs | `projects/[name]/LOG.md` | Recent decisions, context |
| Project plans | `projects/[name]/PLANNING/` | Detailed designs |

**Process**:
1. List `projects/` to see active work
2. Read the README for relevant projects
3. Check LOG for recent context
4. Check PLANNING for detailed designs

---

### 3. Meeting Notes & Discussions

**When needed**: Understanding recent developments; seeing informal framing

| Source | Path | What It Provides |
|:---|:---|:---|
| Meeting transcripts | Project MEETINGS folders | Discussions, updates, debates |

**Process**:
1. Check filenames for dates — most recent has freshest context
2. Search for project names or keywords
3. Good for understanding *how* user talks about work, not just *what*

---

### 4. Reference Materials

**When needed**: Writing about topics where you have collected research

| Source | Path | What It Provides |
|:---|:---|:---|
| Corpus/readings | `corpus/` | Papers and sources by others |
| Notes | Project-specific notes files | Annotated summaries |

---

## Process Checklist

When a task might benefit from context loading:

1. **Categorize**: Which source type applies?
2. **Minimize**: What's the smallest set of files that provides what you need?
3. **Check format**: Is it markdown (readable) or binary (PDF)?
4. **Load and absorb**: Read relevant files before drafting
5. **Cite sources**: Note what context you drew from

---

## Amount of Context

| Task | Context Amount |
|------|----------------|
| Quick reply in user's voice | 1 example file |
| Short blog post | 2-3 similar posts |
| Grant application | Prior grant + project README |
| Long essay | 3-5 essays in similar genre |

**Rule**: Start with less context, add more if the voice isn't matching.

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Loading everything | Context overload, distraction | Pick 2-3 most relevant files |
| No context for voice tasks | Generic output | Always load examples for "write as me" |
| Loading PDFs when MD exists | Can't read binary | Check for markdown versions |
| Same context for all tasks | Irrelevant info | Match context to task genre |

---

*Judicious context loading: enough to match voice, not so much that it distracts.*
