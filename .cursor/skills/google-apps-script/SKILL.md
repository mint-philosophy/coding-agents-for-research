---
name: google-apps-script
description: Use when integrating with Google Workspace (Drive, Sheets, Docs, Gmail) — provides patterns for Apps Script and API access
created: 2025-12-27
updated: 2025-12-27
version: 1.0.0
triggers: ["google drive", "sheets", "docs", "gmail", "apps script", "google workspace"]
scope: [admin, coding]
---

# Google Apps Script Integration

Patterns for integrating with Google Workspace via Apps Script and APIs.

## When to Use

- Reading/writing Google Sheets
- Managing Google Drive files
- Processing Gmail
- Automating Google Docs
- Any Google Workspace integration

## Architecture Options

### Option 1: Apps Script (Simpler)

Deploy as web app, call from agent:

```javascript
// In Google Apps Script
function doGet(e) {
  const action = e.parameter.action;

  if (action === 'list_files') {
    const files = DriveApp.getFiles();
    const result = [];
    while (files.hasNext()) {
      const f = files.next();
      result.push({name: f.getName(), id: f.getId()});
    }
    return ContentService.createTextOutput(JSON.stringify(result));
  }
}
```

Deploy: Publish → Deploy as web app → Execute as you → Anyone can access

### Option 2: Service Account (More Control)

Use Google Cloud service account with Python:

```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

creds = service_account.Credentials.from_service_account_file(
    'service-account.json',
    scopes=['https://www.googleapis.com/auth/drive.readonly']
)
drive = build('drive', 'v3', credentials=creds)

results = drive.files().list(pageSize=10).execute()
```

## Common Patterns

### Read Google Sheet

```python
from googleapiclient.discovery import build

sheets = build('sheets', 'v4', credentials=creds)
result = sheets.spreadsheets().values().get(
    spreadsheetId='SHEET_ID',
    range='Sheet1!A:Z'
).execute()
rows = result.get('values', [])
```

### List Drive Folder

```python
drive = build('drive', 'v3', credentials=creds)
results = drive.files().list(
    q=f"'{FOLDER_ID}' in parents",
    fields="files(id, name, mimeType)"
).execute()
```

### Download File

```python
from googleapiclient.http import MediaIoBaseDownload
import io

request = drive.files().get_media(fileId=FILE_ID)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while not done:
    status, done = downloader.next_chunk()
```

## Setup

1. Create project in Google Cloud Console
2. Enable relevant APIs (Drive, Sheets, etc.)
3. Create service account or OAuth credentials
4. Download credentials JSON
5. Store in `.cursor/.api_keys/` (gitignored)

## Key Principles

- **Read-only first**: Start with read-only scopes, add write when needed
- **Batch operations**: Use batch requests for multiple operations
- **Rate limits**: Google APIs have quotas — add delays for large operations
- **Credentials safety**: Never commit credentials files

---

*Google Workspace is often the glue between agent work and shared team resources.*
