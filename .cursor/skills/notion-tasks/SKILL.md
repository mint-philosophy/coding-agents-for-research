---
name: notion-tasks
description: Use when creating, updating, or managing tasks in a Notion database — provides API integration patterns
---

# Notion Tasks

## Overview

Create and manage tasks in a Notion task database. Handle vague user requests by inferring details intelligently.

## When to Use

- User asks to "add a task", "put on Notion", "track this"
- Creating/updating tasks in a task tracker
- Bulk importing tasks

## Core Pattern

### Handling Vague Requests

When user says: *"Add a task to apply for the grant, deadline next week"*

1. **Parse intent**: Grant application task
2. **Choose emoji**: 🎓 (academic)
3. **Determine parent**: Find appropriate parent task
4. **Pick tags**: `Grant-Apps`
5. **Calculate due**: "next week" → +7 days
6. **Status**: `Future` (not started)

Result: `🎓 Apply for [grant name]`

### Python API Pattern

```python
import requests

token = 'YOUR_NOTION_TOKEN'  # Load from .cursor/.api_keys.txt
db_id = 'YOUR_DATABASE_ID'

headers = {
    'Authorization': f'Bearer {token}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}

payload = {
    'parent': {'database_id': db_id},
    'properties': {
        'Task name': {'title': [{'text': {'content': '🎓 Your task title'}}]},
        'Status': {'status': {'name': 'Future'}},
        'Details': {'rich_text': [{'text': {'content': 'Description'}}]},
        'Tags': {'multi_select': [{'name': 'Tag-Name'}]},
        'Due date': {'date': {'start': '2025-12-01'}}
    }
}

resp = requests.post('https://api.notion.com/v1/pages',
                     headers=headers, json=payload, timeout=60)
```

## Quick Reference

| Property | Type | Example |
|:---|:---|:---|
| Task name | title | Required |
| Status | status | Future, Present, Done |
| Details | rich_text | Optional description |
| Due date | date | YYYY-MM-DD |
| Tags | multi_select | Category tags |

### Time Expression Interpretation

| User Says | Interpretation |
|:---|:---|
| "next week" | +7 days |
| "end of week" | Coming Friday |
| "ASAP" | Tomorrow, status `Urgent` |
| "soon" | +3-5 days |
| "whenever" | No due date |

## Setup

1. Create a Notion integration at https://www.notion.so/my-integrations
2. Share your database with the integration
3. Store token in `.cursor/.api_keys.txt`:
   ```
   NOTION_API_KEY=secret_xxx
   ```

## Key Principles

- **Query database schema first** with `GET /v1/databases/{db_id}` to verify property names
- **Never delete** Notion entries without explicit user authorization
- **Always start task titles with an emoji** for visual scanning
- **Infer missing details** from context rather than asking for everything
