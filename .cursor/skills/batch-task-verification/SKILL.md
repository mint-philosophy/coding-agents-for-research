---
name: batch-task-verification
description: Use when verifying completion of long-running batch tasks — provides systematic verification patterns for LLM extraction, embedding generation, and other multi-hour processes
created: 2025-12-26
updated: 2025-12-26
version: 1.0.0
triggers: ["verify", "check completion", "batch", "extraction done", "background process", "long-running"]
scope: [admin, coding, data]
---

# Batch Task Verification

Systematic verification of long-running batch tasks that execute in the background (LLM extraction, embedding generation, data processing).

## When to Use

- Previous agent started a background process and left instructions to verify
- Task involves processing 100+ items with LLM calls
- Process expected to run 1+ hours
- Need to confirm a batch task is truly complete before dependent tasks can start

## The Problem

Agents often claim tasks are "done" based on:
- Starting a background process
- Seeing partial progress
- Reading a status field without verifying underlying data

This leads to cascade failures when dependent tasks assume data exists that doesn't.

## Verification Protocol

### Phase 1: Process Status

```bash
# Check if process is still running
pgrep -f "script_name" || echo "Not running"
ps aux | grep -E "(python.*script|extraction)" | grep -v grep

# Check log tail for completion message
tail -50 /path/to/output.log
```

**Look for:**
- "COMPLETE" / "FINISHED" / "Done" messages
- Final count summaries (e.g., "1250/1261 success")
- Error summaries
- Process exit (no longer in ps output)

### Phase 2: Coverage Metrics

Don't trust counts alone. Verify actual data:

```python
import pandas as pd  # or your data library

# Load the output
df = pd.read_json('output.jsonl', lines=True)

# Count populated vs target
for field in ['extracted_field_1', 'extracted_field_2']:
    populated = (df[field].str.len() > 0).sum()
    print(f'{field}: {populated}/{len(df)} ({100*populated/len(df):.1f}%)')
```

**Target thresholds** (typical):
- >95% for extraction tasks (some items legitimately fail)
- 100% for computational tasks (embeddings, transforms)

### Phase 3: Functional Testing

Verify the data actually works, not just exists:

```python
# Test a query (if applicable)
results = search_function(query)
assert len(results) > 0, "Search broken"

# Test cross-table references
ids_in_main = set(main_df['id'])
ids_in_related = set(related_df['id'])
orphans = ids_in_related - ids_in_main
assert len(orphans) == 0, f"Orphan references: {orphans}"
```

### Phase 4: Sample Quality

Randomly sample 3-5 records and inspect:

```python
samples = df.sample(5, random_state=42)
for _, row in samples.iterrows():
    print(f"Title: {row['title'][:50]}")
    print(f"Field 1: {row['field_1']}")
    print(f"Field 2: {row['field_2'][:100]}...")
    # Verify fields make sense
```

**Check for:**
- Sensible values (not garbage/truncated)
- Correct data types
- Consistent formatting
- No obvious extraction errors

## Common Failure Modes

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Count matches but search fails | Null vectors | Re-run embedding step |
| 100% coverage but garbage data | Extraction prompt issue | Inspect failures, fix prompt |
| Process "complete" but low count | Silent failures | Check error log |
| Duplicate IDs | Same source in multiple runs | Dedupe before next step |

## Verification Checklist

```
[ ] Process no longer running (or completed message in log)
[ ] Coverage meets threshold (>95% or 100% as appropriate)
[ ] Functional test passes (search, cross-references)
[ ] Sample quality check (3-5 random records look correct)
[ ] Error count acceptable (logged, not hidden)
```

## Handoff Template

When verifying for a previous agent, document:

```markdown
### Task X.Y Verification

**Verified by**: [session_id]
**Date**: [date]

**Process status**: Complete (finished [time])
**Coverage**: [X]/[Y] ([Z]%)
**Functional tests**: [PASS/FAIL]
**Sample quality**: [PASS/FAIL]
**Errors**: [N] (acceptable/needs attention)

**Verdict**: [VERIFIED COMPLETE / NEEDS WORK]
**Next steps**: [what can proceed / what's blocked]
```

## Anti-Patterns

- Trusting "I started the process" as completion
- Only checking row counts, not data quality
- Skipping functional tests
- Not sampling actual record content
- Ignoring error logs

---

*Verification prevents cascade failures in multi-agent projects.*
