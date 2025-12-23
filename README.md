# Coding Agents for Research

A practitioner's guide to using AI coding agents for philosophy and philosophy-adjacent research—or really, any knowledge work that doesn't involve traditional programming.

## What's Here

This repository contains documentation and configuration files from my experience using coding agents (primarily Claude in Cursor and Claude Code) for research tasks. The focus is practical: what worked, what didn't, and artifacts you can adapt for your own workflow.

**[Read the full post →](BRAIN_DUMP_ORGANIZED.md)**

## Quick Start

The most valuable artifacts, in order:

1. **[init.md](artifacts/init.md)** — The initialization prompt that tells agents how to work. Start here.
2. **[end.md](artifacts/end.md)** — Session closure protocol for continuity across agents.
3. **[SKILL_TEMPLATE.md](artifacts/SKILL_TEMPLATE.md)** — How to document reusable capabilities.

## Artifacts

```
artifacts/
├── init.md                    # Agent initialization protocol
├── end.md                     # Session closure protocol
├── SKILL_TEMPLATE.md          # Template for new skills
├── example-session-log.md     # What session logs look like
├── example-news-summary.md    # Example of agent-generated output
└── skills/
    ├── notion-tasks.md        # Notion API integration
    ├── canvas-sync.md         # Slack canvas synchronization
    └── context-loading.md     # Loading context for writing tasks
```

## Key Concepts

**Context Engineering**: The problem of giving agents enough context to be useful without overwhelming their context window. Solved through directory structure, documentation protocol (README/LOG/TODO per project), and initialization prompts.

**Session Management**: Each agent is a temp worker. Session logs track what happened; `/end` commands ensure handoff documentation.

**Skills**: Reusable patterns that agents can draw on instead of reinventing the wheel. Each skill includes scripts, API patterns, and clear recipes.

## Tools Mentioned

- **[Cursor](https://cursor.sh)** — IDE with agent integration. Good for multi-project work.
- **[Claude Code](https://anthropic.com)** — CLI agent. Best for hard tasks.
- **[Imbue Sculptor](https://imbue.com)** — Agent forking. Unique for parallelization.
- **[Tailscale](https://tailscale.com)** + **[Termius](https://termius.com)** — Remote access from phone.

## Resources

- [Steve Newman on Hyperproductivity](https://secondthoughts.ai/p/hyperproductivity)
- [Zhiming Lu on Context Engineering](https://ssrn.com/abstract=5403981)
- [Kirk et al. on Human Context Protocol](https://arxiv.org/abs/2512.05470)

## Adapting This

The artifacts here are sanitized—IDs, paths, and credentials replaced with placeholders. To use them:

1. Copy the `artifacts/` folder to your workspace
2. Replace placeholders like `[Your Projects]`, `YOUR_DATABASE_ID`, `C0XXXXXXXXX`
3. Adjust paths to match your directory structure
4. Add your own skills as you develop them

## About

I'm Seth Lazar, a philosopher working on AI ethics and normative computing. This grew out of running [MINT Lab](https://github.com/mint-research) where we use agents extensively for research coordination.

If you've built something similar or have improvements to suggest, I'd like to hear from you: [@sethlazar](https://twitter.com/sethlazar)

---

*Last updated: December 2025*
