# Skill: Context Loading

## Purpose

Load relevant files into context to write for and as the user. This skill provides an index of where to find useful context and process advice for when to use it.

**Core principle**: Context loading should be judicious. Don't pull 50 papers for every question. Think first about whether you will benefit from additional context, or whether you can successfully respond to the question without it. A general heuristic: if the user is asking you to write as them or for them, you probably need the context. If they're just asking you to do something operational, you probably do not.

---

## When to Use This Skill

Trigger context loading when the task involves:
- Writing in the user's voice (grants, essays, public communication)
- Understanding the user's research focus or style
- Drafting content about ongoing projects
- Preparing materials that reference prior work

**Skip context loading when**:
- Task is purely operational (file management, script running)
- Task is about external information (web searches, API calls)
- User has already provided sufficient context in the prompt

---

## Context Sources Index

### 1. Writing Style & Voice

**When needed**: Drafting grants, essays, public communication; editing to match user's style

| Source | Path | What It Provides |
|:---|:---|:---|
| Research essay drafts | `Research/Drafting/` | Examples of work-in-progress prose |
| Submitted essays | `Research/Under-Review/` | Polished prose examples |
| Grant abstracts | `Grants/[name]/` | Compressed, persuasive writing |

**Process**:
1. Identify the genre (grant, essay, public piece)
2. Find 1-2 examples of the same genre
3. Read the opening paragraphs to absorb tone and structure
4. Note: PDFs and DOCXs are binary—look for `.md` files first

---

### 2. Current Research Projects

**When needed**: Writing about research; understanding what projects are active

| Source | Path | What It Provides |
|:---|:---|:---|
| Project READMEs | `Projects/[project]/README.md` | Brief project descriptions, research questions |
| Project planning | `Projects/[project]/PLANNING/` | Detailed experimental designs |
| Local repos | `Local-Repos/[project]/` | Code, data, evaluation scripts |

**Process**:
1. List `Projects/` to see all active projects
2. Read the `README.md` for each relevant project
3. If deeper understanding needed, check `PLANNING/` subdirectory
4. For technical details, check corresponding `Local-Repos/[project]/`

---

### 3. Meeting Notes & Discussions

**When needed**: Understanding recent developments; seeing informal discussion

| Source | Path | What It Provides |
|:---|:---|:---|
| Meeting notes | `Meetings/` | Detailed discussions, project updates |

**Process**:
1. Check filenames for dates—most recent have freshest context
2. Search for project names or keywords
3. Rich source for understanding *how* user frames research

---

### 4. Previous Grant Applications

**When needed**: Writing new grants; understanding how user pitches research

| Source | Path | What It Provides |
|:---|:---|:---|
| Grant directories | `Grants/[name]/` | Full application materials |
| Application text | `Grants/[name]/application.md` | Prose responses |
| Budgets | `Grants/[name]/budget.csv` | Budget structures |

---

### 5. Recent Publications

**When needed**: Citing user's work; understanding published positions

| Source | Path | What It Provides |
|:---|:---|:---|
| Publications by year | `Publications/[year]/` | PDFs of published work |

**Process**:
1. List subdirectories by year
2. Note: PDFs are binary—can't read directly
3. Filenames indicate topic

---

## Process Checklist

When a task might benefit from context loading:

1. **Categorize the task**: Which of the above categories applies?
2. **Identify minimum context**: What's the smallest set of files that provides what you need?
3. **Check accessibility**: Is it markdown (readable) or binary (PDF/DOCX)?
4. **Load and absorb**: Read the relevant files before drafting
5. **Cite your sources**: When presenting output, note what context you drew from

---

## Extensibility Notes

**To add new context sources**:
1. Add a new section under "Context Sources Index"
2. Include: When needed, Source table (path + what it provides), Process steps
3. List specific accessible files where possible

---

## Integration with Init

This skill should be triggered early in task planning:

> Before executing a writing or research task, check if context loading would help. If yes, load this skill and follow the process checklist.

