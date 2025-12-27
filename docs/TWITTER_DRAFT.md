# Twitter Post Draft

## Current Update (December 27, 2025)

---

**Draft 1:**

Updated the agent workspace template with some improvements from the last few weeks.

New: hooks for context management (warns at 90% usage to wrap up), multi-agent coordination patterns (EXECUTION.md protocol for handoffs), and a /setup wizard for first-time users.

The goal is that you can clone, customize a few placeholders, and start using agents for research or knowledge work.

https://github.com/mint-philosophy/coding-agents-for-research

Still experimental — curious what breaks for people with different workflows.

---

**Draft 2:**

A few workflow improvements to the agent workspace template:

— Context threshold hook: warns the agent when it's at 90% capacity, prompting graceful handoff instead of degraded performance
— Multi-agent coordination: patterns for tasks that span multiple sessions
— /setup command: walks new users through configuration

The broader insight: agents are temp workers with ~200k token memory. Session management and handoff protocols matter more than I initially expected.

https://github.com/mint-philosophy/coding-agents-for-research

---

**Draft 3:**

Updated the agent workspace template. Main additions:

1. Context threshold hook — agents degrade as context fills; this prompts them to wrap up at 90%
2. Multi-agent coordination — EXECUTION.md protocol for work spanning multiple sessions
3. Setup wizard — /setup walks through first-time configuration

The repo is now structured so you can clone it, customize the placeholders, and start using it. Includes dummy project structure, session templates, example skills.

https://github.com/mint-philosophy/coding-agents-for-research

Feedback welcome — especially from people doing non-programming knowledge work.

---

## Voice Notes

- No "excited to announce" or "game-changer"
- Specific about what changed
- Acknowledge limitations ("still experimental")
- Invite feedback
- Em-dashes preferred over parentheticals
