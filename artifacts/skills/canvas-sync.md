---
name: canvas-sync
description: Sync TODO.md files with Slack canvases, create canvases as channel tabs
---

# Canvas Sync Skill

## Overview

Bidirectional sync between local TODO.md files and Slack canvases. Also covers creating new canvases as channel tabs. **Critical**: Always read the canvas first before pushing changes to avoid overwriting collaborator edits.

## When to Use

- User asks to "sync to canvas" or "update the canvas"
- User has edited a TODO.md and wants it reflected in Slack
- User wants to pull changes from canvas to local file
- User asks to create a canvas as a channel tab

## Creating a Canvas as a Channel Tab

### Using a Script

```bash
python create_canvas.py <channel> <markdown_file> [--title TITLE]
```

**Examples**:
```bash
# Create canvas from markdown file
python create_canvas.py "proj-myproject" "path/to/TODO.md" --title "Project Plan"

# Using channel ID
python create_canvas.py "C0XXXXXXXXX" "path/to/file.md"
```

### Direct Python Pattern

```python
from slack_sdk import WebClient

token = "xoxb-..."  # Load from .api_keys.txt
client = WebClient(token=token)

# Read markdown content
with open('path/to/file.md', 'r') as f:
    content = f.read()

# Create canvas as channel tab
result = client.conversations_canvases_create(
    channel_id='C0XXXXXXXXX',  # Your channel ID
    document_content={
        'type': 'markdown',
        'markdown': content
    }
)
canvas_id = result['canvas_id']
print(f"Created channel canvas: {canvas_id}")
```

**Important distinctions**:
- `canvases_create` → Creates a standalone canvas (not attached to channel)
- `conversations_canvases_create` → Creates a canvas **as a channel tab** ✓
- `bookmarks_add` → Adds to bookmarks dropdown (NOT the tab bar)

## Syncing Workflow

### Step 1: Read Both Sources

```python
import os
import requests
from slack_sdk import WebClient
from bs4 import BeautifulSoup

token = os.environ.get('SLACK_BOT_TOKEN')
client = WebClient(token=token)

# Read canvas
def read_canvas(canvas_id):
    info = client.files_info(file=canvas_id)
    url = info['file']['url_private']
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    
    # Parse HTML to text
    soup = BeautifulSoup(response.text, 'html.parser')
    
    lines = []
    for elem in soup.find_all(['h1', 'h2', 'h3', 'li', 'p']):
        if elem.name.startswith('h'):
            level = int(elem.name[1])
            lines.append('#' * level + ' ' + elem.get_text().strip())
        elif elem.name == 'li':
            checked = 'checked' in elem.get('class', [])
            checkbox = '[x]' if checked else '[ ]'
            lines.append(f'- {checkbox} {elem.get_text().strip()}')
        else:
            lines.append(elem.get_text().strip())
    
    return '\n'.join(lines)

# Read local TODO.md
def read_local(path):
    with open(path, 'r') as f:
        return f.read()
```

### Step 2: Compare and Identify Differences

Before pushing any changes:
1. Read the current canvas content
2. Read the local TODO.md
3. Compare them line-by-line or section-by-section
4. **Present differences to the user before proceeding**

### Step 3: Discuss with User

Present findings like:

```
📋 Canvas Sync Check for my-project

**Local changes** (TODO.md):
- Marked "Clone repo" as complete
- Added new task under Phase 2

**Canvas changes** (by collaborators):
- Added "Review dataset structure" under Immediate
- Checked off "Locate rubric dataset"

**Conflicts**:
- Phase 1 header differs between local and canvas

How would you like to proceed?
1. Push local → canvas (overwrites canvas changes)
2. Pull canvas → local (overwrites local changes)  
3. Merge manually (I'll help you combine them)
```

### Step 4: Push Changes (Only After Approval)

```python
def push_to_canvas(canvas_id, markdown_content):
    client.canvases_edit(
        canvas_id=canvas_id,
        changes=[{
            'operation': 'replace',
            'document_content': {
                'type': 'markdown',
                'markdown': markdown_content
            }
        }]
    )
```

## Tracking Canvas IDs

Keep a table of known canvases:

| Project | Channel | Canvas ID | Type |
|:---|:---|:---|:---|
| my-project | #proj-myproject | F0XXXXXXXXX | TODO |
| other-project | #proj-other | F0YYYYYYYYY | Plan |

## Red Flags - STOP

- **Never push without reading canvas first**
- **Never overwrite without user confirmation when differences exist**
- If canvas has changes not in local, ALWAYS ask before pushing

## Dependencies

- `slack_sdk`
- `beautifulsoup4` (for parsing canvas HTML)
- `requests`

Install: `pip install slack_sdk beautifulsoup4 requests`

