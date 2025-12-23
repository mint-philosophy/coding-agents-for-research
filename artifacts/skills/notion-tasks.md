---
name: notion-tasks
description: Use when creating, updating, or managing tasks in Notion - provides API integration patterns
---

# Notion Tasks Skill

## Overview

Create and manage tasks in a Notion task database. The agent should handle vague requests intelligently: infer appropriate parent tasks, tags, and due dates from context. Always start task titles with a fun emoji 🎯📝🚀💡🎓📊

Credentials should be stored in a `.keys` file (never commit to git).

## When to Use

- When user asks to "add a task", "put on Notion", "track this", etc.
- Creating/updating tasks in the task tracker
- Bulk importing tasks

NOT for:
- Reading task lists (query API works but needs separate implementation)
- Managing other Notion databases

## Core Pattern

### Handling Vague Requests

When user says something like: *"Add a task to apply for the grant, deadline next week"*

1. **Parse intent**: Grant application task
2. **Choose emoji**: 🎓 (education/academic)
3. **Determine parent**: Find appropriate parent task
4. **Pick tags**: `Grant-Apps`
5. **Calculate due**: "next week" → add ~7 days to today
6. **Status**: `Future` (not started yet)

Result: `🎓 Apply for [Grant Name]`

### CLI Tool Pattern

```bash
cd /path/to/your/notion-automation

# Create with parent task
python3 notion_tasks.py create \
  --title "🎓 Apply for grant" \
  --status "Future" \
  --due 2025-12-04 \
  --tag "Grant-Apps" \
  --parent "PARENT_PAGE_ID"

# Update a task
python3 notion_tasks.py update --title "My task" --status "Done"
```

### Direct API Pattern

```python
import requests

token = 'YOUR_NOTION_TOKEN'  # Load from .keys file
db_id = 'YOUR_DATABASE_ID'

headers = {
    'Authorization': f'Bearer {token}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}

payload = {
    'parent': {'database_id': db_id},
    'properties': {
        'Task name': {'title': [{'text': {'content': 'YOUR TASK TITLE'}}]},
        'Status': {'status': {'name': 'Future'}},
        'Details': {'rich_text': [{'text': {'content': 'Description'}}]},
        'Tags': {'multi_select': [{'name': 'Research'}]},
        'Due date': {'date': {'start': '2025-12-01'}}
    }
}

resp = requests.post('https://api.notion.com/v1/pages', headers=headers, json=payload, timeout=60)
```

## Quick Reference

| Property | CLI Flag | Type |
|:---|:---|:---|
| Task name | `--title` | title (required for create) |
| Status | `--status` | status: Future, Urgent, Present, Done |
| Details | `--details` | rich_text |
| Due date | `--due` | date (YYYY-MM-DD) |
| Tags | `--tag` | multi_select (repeat for multiple) |

### Status Options

| Status | Use When |
|:---|:---|
| Future | Not yet started |
| Urgent | High priority, active |
| Present | Currently working on |
| Done | Finished |

### Fun Emoji Guide 🎉

| Context | Emoji Ideas |
|:---|:---|
| Grants/funding | 🎓 💰 📋 |
| Research | 🔬 📊 🧪 💡 |
| Writing | ✍️ 📝 📄 |
| Meetings/people | 🤝 👥 📞 |
| Admin/logistics | 📦 ⚙️ 🗂️ |
| Deadlines | ⏰ 🎯 🚨 |
| Ideas | 💡 🌟 ✨ |
| Done/success | ✅ 🎉 💪 |

## Interpreting Time Expressions

| User Says | Interpretation |
|:---|:---|
| "next week" | +7 days |
| "end of week" | Coming Friday |
| "next month" | 1st of next month |
| "ASAP" | Tomorrow, status `Urgent` |
| "soon" | +3-5 days |
| "whenever" | No due date, status `Future` |

## Common Mistakes / Rationalizations

| Mistake | Correction |
|:---|:---|
| Hardcoding credentials | Always load from `.keys` file |
| Using old Status values | Check current database schema |
| Assuming property names | Query database schema first |

## Red Flags - STOP

- About to commit `.keys` or credentials to git
- Using property names without verifying current schema
- **About to DELETE any Notion entry** — NEVER delete without explicit authorization

## Key Principles

- Credentials in `.keys` file only (never in code/commits)
- API version: `2022-06-28`
- When in doubt, query the database schema first with GET `/v1/databases/{db_id}`

