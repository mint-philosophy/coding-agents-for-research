---
name: canvas-sync
description: Sync markdown files with Slack canvases, create canvases as channel tabs
---

# Canvas Sync

## Overview

Bidirectional sync between local markdown files and Slack canvases. Create canvases as channel tabs.

**Critical**: Always read the canvas first before pushing to avoid overwriting collaborator edits.

## When to Use

- User asks to "sync to canvas" or "update the canvas"
- User has edited a markdown file and wants it reflected in Slack
- User wants to create a canvas as a channel tab

---

## Creating a Canvas as a Channel Tab

```python
from slack_sdk import WebClient

token = "xoxb-..."  # Bot token
client = WebClient(token=token)

# Read markdown content
with open('path/to/file.md', 'r') as f:
    content = f.read()

# Create canvas as channel tab
result = client.conversations_canvases_create(
    channel_id='C0XXXXXXXXXX',
    document_content={
        'type': 'markdown',
        'markdown': content
    }
)
canvas_id = result['canvas_id']
```

**Important distinctions**:
- `canvases_create` → Standalone canvas (not in channel)
- `conversations_canvases_create` → Canvas **as channel tab** ✓
- `bookmarks_add` → Bookmark dropdown, not tab bar

---

## Reading Canvas Content

```python
import requests
from slack_sdk import WebClient
from bs4 import BeautifulSoup

token = "xoxb-..."
client = WebClient(token=token)

# Get canvas info
info = client.files_info(file=canvas_id)
url = info['file']['url_private']

# Download content
headers = {'Authorization': f'Bearer {token}'}
response = requests.get(url, headers=headers)

# Parse HTML to markdown
soup = BeautifulSoup(response.text, 'html.parser')
# Extract text, preserving structure...
```

---

## Sync Workflow

### Step 1: Read Both Sources
- Read current canvas content
- Read local markdown file

### Step 2: Compare
- What changed locally?
- What changed in canvas (by collaborators)?
- Any conflicts?

### Step 3: Present to User

```
📋 Canvas Sync Check

**Local changes**:
- Marked "Task X" as complete
- Added new task under Phase 2

**Canvas changes** (by collaborators):
- Added "Review dataset" task
- Checked off "Setup" task

**Conflicts**:
- Section header differs

How would you like to proceed?
1. Push local → canvas
2. Pull canvas → local
3. Merge manually
```

### Step 4: Push (After Approval)

```python
client.canvases_edit(
    canvas_id=canvas_id,
    changes=[{
        'operation': 'replace',
        'document_content': {
            'type': 'markdown',
            'markdown': new_content
        }
    }]
)
```

---

## Key Principles

- **Never push without reading canvas first**
- **Never overwrite without user confirmation** when differences exist
- **Always ask** before pushing if canvas has changes not in local

## Dependencies

```bash
pip install slack_sdk beautifulsoup4 requests
```
