# Agent Ideas

Illustrative use cases for what agents can do beyond coding. These are patterns, not implementations — adapt them to your own tools and workflows.

---

## Morning Briefing

Start each day with an agent-generated summary:

- **Calendar**: What's on today, any conflicts, prep needed
- **Tasks**: What's due, what's overdue, what's blocked
- **Email**: Unread counts, flagged items, anything urgent
- **Projects**: Recent activity, pending decisions

The agent pulls from your calendar, task manager, and email APIs, synthesizes it into a 2-minute read. You get situational awareness without clicking through five apps.

**Key insight**: The value isn't automation — it's *anticipation*. A good briefing tells you what you didn't think to ask about.

---

## End-of-Day Retrospective

Combat the "what did I even do today?" feeling:

- Agent reviews completed tasks, sent emails, modified files, meeting notes
- Synthesizes into a summary of actual accomplishments
- Helps you recognize productivity you might otherwise discount

Particularly useful if you work across many small tasks or frequently context-switch.

---

## Meeting Notes Processing

Meeting transcripts arrive with generic names. Agent can:

- Read transcript content
- Identify participants and topics
- Propose meaningful filenames
- Extract action items and decisions
- Update relevant project logs

Turns raw transcripts into searchable, actionable records.

---

## Task Triage

Review stale or undated tasks:

- Agent queries your task manager for items without dates or items untouched for weeks
- Presents them for quick triage: defer, schedule, delegate, delete
- Updates the system with your decisions

Good for periodic backlog grooming without manual database archaeology.

---

## Recommendation Letters

When you need to write a letter:

- Agent retrieves candidate materials (CV, prior correspondence)
- Reviews your past letters for style patterns
- Drafts new letter matching your voice
- You edit and finalize

Works for any templated writing where you have prior examples to learn from.

---

## News Digests

For any domain you track:

- Agent pulls from RSS feeds, Slack channels, saved links
- Filters to recent items
- Synthesizes into a narrative summary organized by theme
- Posts to team channel or saves locally

Turns information firehose into a weekly briefing.

---

## Project Setup

When starting new work:

- Agent creates folder structure with standard templates
- Initializes README, LOG, TODO files
- Creates Slack channel (if using)
- Adds to task tracker
- Sets up any integrations

Reduces friction for starting new things. Consistent structure across projects.

---

## Platform Migration

Escape walled gardens:

- Agent exports data from one platform (screenshots, API, scraping)
- Transforms into portable format
- Imports to new platform
- Handles the tedious mapping work

Examples: Microsoft To Do → Notion, Exchange calendar → Google Calendar, proprietary notes → markdown files.

---

## Research Database Building

For literature review or landscape mapping:

- Agent searches for sources on a topic
- Extracts structured metadata
- Verifies and enriches entries
- Organizes into searchable database

Can scale to hundreds of entries across multiple sessions using handoff protocols.

---

## Semantic Corpus Search

Build a searchable index over your research papers:

- Agent indexes PDFs using embeddings (semantic) and keywords (BM25)
- Hybrid search combines conceptual similarity with exact term matching
- Query in natural language: "papers arguing against RLHF"
- Agent reads top hits, synthesizes across sources

**The insight**: Pure keyword search misses conceptual matches. Pure semantic search misses exact terminology. Hybrid (70/30 blend) catches both.

**Multi-phase enrichment**: Beyond basic indexing, agent can:
- Extract structured metadata (authors, topics, key claims)
- Build similarity networks between papers
- Identify thematic clusters
- Generate topic taxonomies

For large corpora (1000+ papers), use the `big-project-planning` skill with pilot runs before full processing.

---

## Writing Assistance

When writing as yourself:

- Agent loads your prior publications and drafts
- Understands your voice, argument patterns, favorite constructions
- Drafts new content matching your style
- You edit for substance

Works better than generic "improve my writing" because it's calibrated to *your* writing.

---

## The Pattern

Most of these share a structure:

1. **Gather context** from multiple sources
2. **Synthesize** into a useful format
3. **Present** for human decision or action
4. **Execute** updates based on direction

The agent handles the tedious gathering and formatting. You make the decisions that matter.

---

## What Doesn't Work (Yet)

- **Anything requiring real-time interaction** with humans
- **Platforms that block API access** or require CAPTCHAs
- **Tasks requiring judgment you can't articulate** — if you can't explain what "good" looks like, the agent can't hit it
- **Highly sensitive operations** without proper sandboxing

---

*These are starting points. The best agent workflows emerge from noticing your own friction points and asking "could an agent do this part?"*
