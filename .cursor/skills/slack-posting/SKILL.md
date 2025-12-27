---
name: slack-posting
description: Use when posting messages to Slack or reading DMs/files — provides patterns for bot and user token operations
---

# Slack Operations

## Overview

Interact with Slack using the Slack SDK. Two token types:

| Token Type | Prefix | Use For |
|:---|:---|:---|
| **Bot Token** | `xoxb-` | Posting to channels |
| **User Token** | `xoxp-` | Reading DMs, searching, downloading files |

## When to Use

### Posting (Bot Token)
- Send notifications to channels
- Coordinate with team members
- **Only with explicit user instruction**

### Reading (User Token)
- Retrieve DM history
- Search messages
- Download shared files

---

## Posting Messages

```python
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

token = "xoxb-..."  # Load from .cursor/.api_keys.txt
client = WebClient(token=token)

# Find channel ID from name
result = client.conversations_list(types="public_channel,private_channel")
channel_id = None
for c in result["channels"]:
    if c["name"] == "channel-name":
        channel_id = c["id"]
        break

# Post message
client.chat_postMessage(channel=channel_id, text="Your message here")
```

---

## Reading DMs

```python
from datetime import datetime, timedelta
from slack_sdk import WebClient

token = "xoxp-..."  # User token for reading DMs
client = WebClient(token=token)

# Find DM channel with user
convos = client.conversations_list(types='im')
dm_channel = None
for c in convos.get('channels', []):
    if c.get('user') == 'USER_ID':
        dm_channel = c['id']
        break

# Get recent messages
days_ago = datetime.now() - timedelta(days=3)
history = client.conversations_history(
    channel=dm_channel,
    oldest=str(days_ago.timestamp())
)

for msg in history.get('messages', []):
    print(msg.get('text', ''))
```

---

## Downloading Files

```python
import requests

token = "xoxp-..."
headers = {'Authorization': f'Bearer {token}'}

# Get file URL from message or files_list
url = "https://files.slack.com/..."
response = requests.get(url, headers=headers)

with open('filename.pdf', 'wb') as f:
    f.write(response.content)
```

---

## Setup

1. Create a Slack app at https://api.slack.com/apps
2. Add required scopes:
   - Bot: `chat:write`, `channels:read`
   - User: `search:read`, `files:read`, `im:history`
3. Store tokens in `.cursor/.api_keys.txt`:
   ```
   SLACK_BOT_TOKEN=xoxb-xxx
   SLACK_USER_TOKEN=xoxp-xxx
   ```

## Key Principles

- **Never post without explicit user instruction**
- **Use correct token type** (bot for posting, user for reading DMs)
- **Verify channel/user exists** before operations
- **Test token validity** when in doubt
