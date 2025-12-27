---
name: skill-name-with-hyphens
description: Use when [specific triggering conditions and symptoms] - [what the skill does and how it helps, written in third person]
---

# Skill Name

<!-- INSTRUCTIONS FOR WRITING THIS SKILL -->
<!-- 
Before you start: This template guides you to create a skill that prevents failure modes.
Think about: What common mistake does this skill prevent? What rationalizations do agents use to skip this step?

Delete these instruction comments when you're done writing the skill.
-->

## Overview
<!-- 
INSTRUCTIONS: State the core principle in 1-2 sentences.
- What is this skill fundamentally about?
- What's the "Iron Law" if there is one?

EXAMPLE: "Claiming work is complete without verification is dishonesty, not efficiency. Core principle: Evidence before claims, always."
-->

What is this? Core principle in 1-2 sentences.

## When to Use
<!-- 
INSTRUCTIONS: List specific symptoms/triggers that indicate this skill applies.
- Focus on observable situations, not abstract concepts
- Include "When NOT to use" to prevent misapplication

EXAMPLE:
- Use when about to mark a task as complete
- Use when claiming "it should work now"
- Use when tired and wanting to finish
- NOT for exploratory research where verification isn't possible yet
-->

- Bullet list with SYMPTOMS and use cases
- When NOT to use

## Core Pattern
<!-- 
INSTRUCTIONS: Provide actionable steps or before/after comparison.
- For process skills: Step-by-step numbered list
- For mental model skills: Before/after example
- Include specific commands, questions, or checks

EXAMPLE for verification pattern:
BEFORE claiming completion:
1. Identify: What command proves this claim?
2. Run: Execute the FULL command (fresh, complete)
3. Read: Full output, check exit code
4. Verify: Does output confirm the claim?
5. ONLY THEN: Make the claim
-->

Before/after example or step-by-step process.

## Quick Reference
<!-- 
INSTRUCTIONS: Create a scannable table or bullet list for common operations.
- What are the most frequent use cases?
- What's the fastest way to apply this skill?

EXAMPLE (as table):
| Situation | Required Evidence |
|-----------|------------------|
| Tests pass | Test output showing 0 failures |
| Bug fixed | Test of original symptom now passes |
| Code works | Run command + read output |
-->

Table or bullets for scanning common operations.

## Common Mistakes / Rationalizations
<!-- 
INSTRUCTIONS: This is CRITICAL. List every excuse agents use to skip this skill.
- Think about time pressure, confidence, fatigue
- Include "sounds reasonable" rationalizations
- For each excuse, state why it's wrong

EXAMPLE:
| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification |
| "I'm confident" | Confidence ≠ evidence |
| "Just this once" | No exceptions |
-->

| Excuse | Reality |
|--------|---------|
| "Rationalization here" | Why it's wrong |

## Red Flags - STOP
<!-- 
INSTRUCTIONS: List thought patterns that indicate violation is about to happen.
- These should be mental "trip wires"
- Use exact phrases agents might think
- Make it visceral: "If you catch yourself thinking X, STOP"

EXAMPLE:
- Using "should", "probably", "seems to"
- About to commit without verification
- Tired and wanting work over
- "Just this once"
-->

- List of warning signs
- Thoughts that indicate you're about to violate the skill
- "If you catch yourself thinking X, STOP"

## Key Principles
<!-- 
INSTRUCTIONS: State the fundamental, non-negotiable rules.
- What is absolutely mandatory?
- What is the "spirit of the law"?
- Include "Violating the letter is violating the spirit" if applicable

EXAMPLE:
- Evidence before claims, always
- Fresh verification, not old runs
- No exceptions for "simple" tasks
- "Violating the letter of this rule is violating the spirit"
-->

- Fundamental rules
- Non-negotiable constraints
- "The Iron Law" if applicable

## Real-World Impact (optional)
<!-- 
INSTRUCTIONS: If you have concrete data, include it.
- How many times has this prevented failure?
- What happened when this was violated?
- Specific examples from sessions

Only include if you have real examples. DELETE this section if not applicable.
-->

Concrete results from using this skill.

---

<!-- FINAL CHECKLIST BEFORE SAVING:
- [ ] YAML frontmatter: name (lowercase-with-hyphens), description (starts with "Use when...")
- [ ] Overview: Clear 1-2 sentence principle
- [ ] When to Use: Specific triggers, not abstractions
- [ ] Core Pattern: Actionable steps or clear example
- [ ] Common Rationalizations: Table with real excuses
- [ ] Red Flags: Thought patterns that indicate violation
- [ ] Key Principles: Non-negotiable rules stated clearly
- [ ] Deleted all instruction comments
-->
