# Agent Workspace

A deployable template for working with AI coding agents (Claude, Cursor, etc.) on research and knowledge work.

**[Read the guide →](docs/guide.md)** | **[Agent ideas →](docs/agent-ideas.md)** | **[Recent updates →](docs/updates.md)**

---

## Quick Start

```bash
# Clone this repo
git clone https://github.com/yourusername/agent-workspace.git
cd agent-workspace

# Open in Cursor or run with Claude Code
cursor .
# or
claude

# Run the setup wizard
/setup
```

The `/setup` command walks you through configuration. Or do it manually — see [Configuration](#configuration) below.

## What's Here

```
agent-workspace/
├── .cursor/
│   ├── commands/          # Slash commands (/init, /end, /setup, etc.)
│   └── skills/            # Reusable capabilities
│
├── .claude/
│   ├── settings.json      # Hook configuration for Claude Code CLI
│   └── hooks/             # Lifecycle hooks (context-threshold, etc.)
│
├── projects/              # Collaborative research projects
│   ├── collab-1/          # Template with README, LOG, TODO
│   └── collab-2/
│
├── side-projects/         # Personal experiments
│   └── side-proj-1/
│
├── corpus/                # Research by others (papers, readings)
├── publications/          # Your published writing
├── research-essays/       # Non-project writing, explorations
├── grants/                # Grant applications, admin
│
├── local-repos/           # Git clones (gitignored)
├── scripts/               # Global automation
│
├── sessions/              # Agent session logs
│   ├── active/
│   ├── completed/
│   └── SESSION_TEMPLATE.md
│
├── docs/
│   ├── guide.md           # Full documentation
│   └── updates.md         # Changelog
│
├── CLAUDE.md              # Claude Code workspace instructions
└── README.md              # This file
```

## Key Concepts

### The Documentation Triad

Every project has three files:
- **README.md** — Static goals, who's involved, research questions
- **LOG.md** — Session history, decisions made, what happened
- **TODO.md** — Immediate next steps

Agents read these on startup to understand project state.

### Session Management

Agents are temp workers with ~200k token memory. The `/init` and `/end` commands ensure:
- Each session creates logs (`sessions/active/`)
- Work is documented before session ends
- Handoff notes enable the next agent to continue

### Skills System

Skills are reusable patterns in `.cursor/skills/`. Instead of re-explaining how to post to Slack or create Notion tasks, agents load the relevant skill.

### Hooks (Claude Code)

Lifecycle hooks in `.claude/hooks/` run automatically. The included `context-threshold.py` warns when context usage hits 90%, prompting the agent to wrap up.

## Setup

### Guided Setup

Run `/setup` in the agent chat — the agent will walk you through configuration.

### Manual Setup

**For Cursor Users:**
1. Open this folder in Cursor
2. Edit `.cursor/commands/init.md` with your details
3. Run `/init` to start

**For Claude Code Users:**
1. Navigate to this folder in terminal
2. Run `claude` to start
3. Edit `.cursor/commands/init.md` with your details
4. Run `/init` to start

### Configuration

**Required edits in `.cursor/commands/init.md`:**
- `[Agent Name]` → Your agent's name (e.g., "Jarvis", "Friday")
- `[Your Workspace]` → Your workspace description
- `[user]` → Your name
- `[Your timezone]` → Your timezone

**API Keys** (for skills that need them):
```bash
# Create .cursor/.api_keys.txt (gitignored)
NOTION_API_KEY=secret_xxx
SLACK_BOT_TOKEN=xoxb-xxx
```

## Customization

### Adding Projects

```bash
cp -r projects/collab-1 projects/my-new-project
# Edit the README.md, LOG.md, TODO.md
```

### Adding Skills

```bash
mkdir .cursor/skills/my-skill
cp .cursor/skills/SKILL_TEMPLATE.md .cursor/skills/my-skill/SKILL.md
# Follow the template structure
# Register in init.md under "Registered Skills"
```

### Adding Commands

Create `.cursor/commands/my-command.md` following the init.md structure.

## Tools

- **[Cursor](https://cursor.sh)** — IDE with agent integration
- **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** — CLI agent from Anthropic
- **[Imbue Sculptor](https://sculptor.imbue.com)** — Agent forking for parallelization

## Resources

*This section is a living document — we add sources as we find useful ideas. See the `self-improvement` skill for our protocol.*

### Conceptual Foundations

- [Steve Newman on Hyperproductivity](https://secondthoughts.ai/p/hyperproductivity) — The case for agents in knowledge work
- [Xu et al. on Context Engineering](https://arxiv.org/abs/2512.05470) — Systematic approach to agent context
- [Shah et al. on Human Context Protocol](https://ssrn.com/abstract=5403981) — Providing human context to agents

### Agent Architecture

- [ARTEMIS (arXiv:2512.09108)](https://arxiv.org/abs/2512.09108) — Measure outcomes → identify patterns → refine configurations
- [Anthropic Agent Skills](https://github.com/anthropics/agent-skills) — Context degradation patterns (lost-in-middle, poisoning, distraction, clash)

### Workflow Repos

- [cursor.directory](https://cursor.directory/) — Community cursor rules collection
- [Simon Willison on Claude Skills](https://simonwillison.net/2025/Oct/16/claude-skills/) — Skills pattern, "maybe bigger than MCP"
- [Simon Willison: Async Code Research](https://simonwillison.net/2025/Nov/6/async-code-research/) — Using public repos with agents
- [simonw/research](https://github.com/simonw/research) — Example research repo for agent experiments

*Found something useful? Add it here and credit the source.*

## About

Created by [Seth Lazar](https://twitter.com/sethlazar), philosopher working on AI ethics at [MINT Lab](https://github.com/mint-research).

Contributions and improvements welcome.

---

*Last updated: December 2025*
