---
name: cursor-claude-sync
description: Use when syncing commands/skills between Cursor and Claude Code — ensures workflow changes are visible across both surfaces
created: 2025-12-26
updated: 2025-12-26
version: 1.0.0
triggers: ["sync commands", "interoperability", "cursor claude", "command sync", "workflow update"]
scope: [admin, meta]
---

# Cursor ↔ Claude Code Sync

Ensure commands and workflow configurations are consistent across Cursor Agent and Claude Code CLI.

## The Problem

If you use both Cursor (IDE) and Claude Code (CLI), you have two entry points to the same workspace. Commands need to work from both.

## Architecture

```
.cursor/commands/          ← GROUND TRUTH (full command definitions)
    ├── init.md
    ├── end.md
    └── ...

.claude/commands/           ← STUBS (point to Cursor commands)
    ├── init.md             → "Read .cursor/commands/init.md"
    ├── end.md              → "Read .cursor/commands/end.md"
    └── ...
```

**Cursor is ground truth.** Claude Code commands are thin stubs that redirect to the Cursor command files.

## When to Sync

Run sync check when:
- Creating a new command
- Renaming a command
- Deleting a command
- During `/end` protocol
- After any workflow updates

## Sync Check Protocol

### 1. List Commands in Both Locations

```bash
# Cursor commands (ground truth)
ls -1 .cursor/commands/*.md | xargs -I {} basename {} .md | sort

# Claude Code commands (stubs)
ls -1 .claude/commands/*.md | xargs -I {} basename {} .md | sort
```

### 2. Find Discrepancies

```bash
# Commands in Cursor but not Claude Code (MISSING STUBS)
comm -23 <(ls -1 .cursor/commands/*.md | xargs -I {} basename {} .md | sort) \
         <(ls -1 .claude/commands/*.md | xargs -I {} basename {} .md | sort)

# Commands in Claude Code but not Cursor (ORPHAN STUBS)
comm -13 <(ls -1 .cursor/commands/*.md | xargs -I {} basename {} .md | sort) \
         <(ls -1 .claude/commands/*.md | xargs -I {} basename {} .md | sort)
```

### 3. Create Missing Stubs

For each missing command, create a stub in `.claude/commands/`:

```markdown
# [Command Title]

Read and follow the protocol from:

**`.cursor/commands/[name].md`**

[One-line description of what the command does.]
```

### 4. Remove Orphan Stubs

Delete any Claude Code stubs that no longer have a corresponding Cursor command.

## Creating a New Command

When creating a new command:

1. **Create in Cursor first**: `.cursor/commands/[name].md` with full definition
2. **Create Claude Code stub**: `.claude/commands/[name].md` pointing to Cursor file
3. **Update init.md** if command should be listed
4. **Test both surfaces**: Run command from Cursor Agent and Claude Code CLI

## Stub Template

```markdown
# [Human-Readable Title]

Read and follow the protocol from:

**`.cursor/commands/[filename].md`**

[Brief description — what this command does in one sentence.]
```

## Skills Sync

Skills live only in `.cursor/skills/` — Claude Code accesses them through the same filesystem. No duplication needed.

However, if a skill should be **invocable as a slash command** in Claude Code, create a stub in `.claude/commands/` that loads the skill.

## Quick Sync Script

```bash
echo "=== CURSOR COMMANDS ==="
ls -1 .cursor/commands/*.md | xargs -I {} basename {} .md | sort

echo ""
echo "=== CLAUDE CODE COMMANDS ==="
ls -1 .claude/commands/*.md | xargs -I {} basename {} .md | sort

echo ""
echo "=== MISSING STUBS (need to create in .claude/commands/) ==="
comm -23 <(ls -1 .cursor/commands/*.md | xargs -I {} basename {} .md | sort) \
         <(ls -1 .claude/commands/*.md | xargs -I {} basename {} .md | sort)

echo ""
echo "=== ORPHAN STUBS (exist in .claude but not .cursor) ==="
comm -13 <(ls -1 .cursor/commands/*.md | xargs -I {} basename {} .md | sort) \
         <(ls -1 .claude/commands/*.md | xargs -I {} basename {} .md | sort)
```

---

*Keep one source of truth. Stubs just redirect.*
