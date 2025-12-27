#!/usr/bin/env python3
"""
Context Threshold Hook for Claude Code
Triggers warning when context usage exceeds threshold (default 90%)

Hook type: UserPromptSubmit
Purpose: Warn Claude to wrap up and run /end when context is nearly full
"""

import json
import sys
from pathlib import Path

# Configuration
CONTEXT_WINDOW_TOKENS = 200000  # Claude's approximate context window
THRESHOLD_PERCENT = 90  # Trigger at 90% usage
CHARS_PER_TOKEN = 4  # Rough approximation


def estimate_tokens(text: str) -> int:
    """Estimate token count from character count."""
    return len(text) // CHARS_PER_TOKEN


def get_transcript_size(transcript_path: str) -> int:
    """Read transcript JSONL and estimate total tokens."""
    path = Path(transcript_path)
    if not path.exists():
        return 0

    total_chars = 0
    try:
        with open(path, 'r') as f:
            for line in f:
                if line.strip():
                    total_chars += len(line)
    except Exception:
        return 0

    return total_chars // CHARS_PER_TOKEN


def main():
    # Read hook input from stdin
    try:
        hook_input = json.load(sys.stdin)
    except json.JSONDecodeError:
        # No input or invalid JSON - allow to proceed
        return 0

    transcript_path = hook_input.get("transcript_path", "")
    if not transcript_path:
        return 0

    # Calculate context usage
    current_tokens = get_transcript_size(transcript_path)
    threshold_tokens = int(CONTEXT_WINDOW_TOKENS * THRESHOLD_PERCENT / 100)
    usage_percent = int(current_tokens / CONTEXT_WINDOW_TOKENS * 100)

    # Check if over threshold
    if current_tokens >= threshold_tokens:
        # Output warning as plain text - Claude Code shows this to the agent
        warning = f"""## CONTEXT THRESHOLD WARNING

Context usage: {usage_percent}% ({current_tokens:,} / {CONTEXT_WINDOW_TOKENS:,} tokens)

**Action required**: You are approaching the context limit. Please:
1. Complete your current task as concisely as possible
2. Update the session log with your progress
3. Run `/end` to properly close this session

Do NOT start new tasks. Wrap up now."""
        # Plain text output is shown to Claude as additional context
        print(warning)
        return 0

    # Under threshold - proceed normally (no output needed)
    return 0

if __name__ == "__main__":
    sys.exit(main())
