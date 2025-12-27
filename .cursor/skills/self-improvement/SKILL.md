---
name: self-improvement
description: Use when looking for ways to improve agent workflows — covers finding ideas from other repos, updating resources, and systematic learning
created: 2025-12-27
updated: 2025-12-27
version: 1.0.0
triggers: ["improve", "learn", "ideas", "resources", "other repos", "best practices"]
scope: [meta, admin]
---

# Self-Improvement

Protocols for continuously improving agent workflows by learning from experience and external sources.

## When to Use

- Looking for ideas to improve your workflow
- Found a useful repo and want to extract learnings
- Want to update the resources/credits section
- Running `/retro` and need patterns to apply

---

## Part 1: Finding Ideas from Other Repos

### Where to Look

**Agent/AI Workflow Repos:**
- GitHub topics: `ai-agents`, `llm-tools`, `prompt-engineering`
- Search: "cursor rules", "claude code", "agent workflow"
- "Awesome" lists: awesome-ai-agents, awesome-prompts

**Academic Sources:**
- arXiv: agent architectures, prompt engineering, context management
- Conference proceedings: NeurIPS, ICML agent workshops

### Evaluation Checklist

When reviewing a repo, ask:

1. **Relevance**: Does this solve a problem I have?
2. **Generalizability**: Can this pattern work in my context?
3. **Simplicity**: Is this simpler than what I'm doing now?
4. **Evidence**: Does the author show this actually works?

### Extraction Protocol

When you find something useful:

1. **Identify the core insight** — What's the key idea?
2. **Note the source** — URL, author, date
3. **Translate to your context** — How would this work here?
4. **Create or update** — New skill, update to init.md, or resource link
5. **Credit the source** — Add to resources section

### Example

Found in `anthropics/agent-skills` repo:
> "Context degrades predictably: lost-in-middle, poisoning, distraction, clash."

**Extraction:**
- Core insight: Context degradation has named patterns
- Translation: Add to metacognitive strategies in init.md
- Credit: Add repo to resources with specific insight noted

---

## Part 2: Updating Resources

### When to Update

Update `README.md` resources section when you:
- Find a repo with useful patterns
- Read a paper that influenced your workflow
- Discover a tool worth recommending

### Format

```markdown
## Resources

- [Author/Repo Name](URL) — One-line description of what's useful
```

### What to Include

| Include | Skip |
|---------|------|
| Repos with clear, reusable patterns | Repos you just glanced at |
| Papers that changed how you work | Papers you haven't read |
| Tools you've actually used | Tools you've only heard of |

### Credit Protocol

When adding a resource:

1. **Be specific** — What did you learn from it?
2. **Link directly** — To the repo, paper, or specific file
3. **Date it** — Note when added (in updates.md if significant)

---

## Part 3: Systematic Learning

### The Learning Loop

```
Experience → Friction → Pattern → Skill → Experience
     ↑                                         |
     └─────────────────────────────────────────┘
```

### Triggers for Learning

| Trigger | Action |
|---------|--------|
| Same error twice | Create skill to prevent it |
| User correction | Update relevant command |
| External source | Evaluate and extract |
| Session friction | Run `/retro` |

### Skill Creation Threshold

Create a new skill when:
- Pattern is **reusable** (will apply again)
- Benefit is **clear** (saves time or prevents errors)
- Documentation is **possible** (can explain it)
- You've **tested** it (it actually works)

If 3+ are true → create the skill.

### Metacognitive Updates

Some learnings belong in `init.md` rather than a separate skill:
- New thinking patterns → Section 6 (Metacognitive Strategies)
- New verification steps → Section 4 (Startup Checklist)
- New iron laws → Section 5 (Iron Laws)

### Versioning

When updating skills:
- Increment version in frontmatter
- Update `updated:` date
- Note what changed in commit message

---

## Part 4: Current Resource Tracking

### Repos to Watch

Keep a mental list of repos that consistently produce useful ideas:
- Agent architecture repos
- Prompt engineering collections
- Workflow automation tools

### Periodic Review

Monthly or when starting a new project:
1. Check starred/watched repos for updates
2. Search for new repos in relevant topics
3. Review academic preprints (arXiv cs.AI, cs.CL)
4. Update resources section with findings

---

## Quick Reference

### Found something useful?

1. Note the source URL
2. Extract the core insight (1-2 sentences)
3. Decide: new skill, init.md update, or just resource link
4. Implement and credit

### Running low on ideas?

1. Search GitHub for repos with similar goals
2. Check "awesome" lists in your domain
3. Review recent arXiv papers on agents
4. Look at how other people structure their .cursor/ folders

### Want to improve systematically?

1. Run `/retro` weekly
2. Review friction points across sessions
3. Extract patterns from successes
4. Update skills based on evidence

---

*This skill is meta — it's about improving the skills themselves.*
