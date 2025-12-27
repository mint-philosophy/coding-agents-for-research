#!/usr/bin/env python3
"""
Canvas Sync Tool - Bidirectional sync between markdown files and Slack canvases.

Usage:
    python sync_canvas.py --project my-project --action check
    python sync_canvas.py --project my-project --action push
    python sync_canvas.py --project my-project --action pull
"""

import os
import sys
import argparse
import requests
from pathlib import Path
from difflib import unified_diff
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing beautifulsoup4. Install with: pip install beautifulsoup4")
    sys.exit(1)

# Project registry - add your projects here
PROJECTS = {
    "my-project": {
        "canvas_id": "F0XXXXXXXXXX",  # Get from Slack canvas URL
        "local_path": "projects/my-project/TODO.md",
        "channel": "proj-my-project"
    }
    # Add more projects as needed
}

def get_token():
    """Load Slack bot token from environment or .api_keys.txt"""
    token = os.environ.get('SLACK_BOT_TOKEN')
    if not token:
        keys_file = Path(__file__).parent.parent.parent / '.api_keys.txt'
        if keys_file.exists():
            for line in keys_file.read_text().splitlines():
                if line.startswith('SLACK_BOT_TOKEN='):
                    token = line.split('=', 1)[1].strip()
                    break
    return token

def read_canvas(client, canvas_id, token):
    """Read canvas content and convert HTML to markdown-ish text."""
    info = client.files_info(file=canvas_id)
    url = info['file']['url_private']
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    lines = []
    seen_headers = set()  # Dedupe duplicate headers
    
    for elem in soup.find_all(['h1', 'h2', 'h3', 'li', 'p', 'hr']):
        if elem.name == 'hr':
            lines.append('---')
        elif elem.name.startswith('h'):
            text = elem.get_text().strip()
            if text not in seen_headers:  # Skip duplicate headers
                seen_headers.add(text)
                level = int(elem.name[1])
                lines.append('')
                lines.append('#' * level + ' ' + text)
                lines.append('')
        elif elem.name == 'li':
            classes = elem.get('class', [])
            checked = 'checked' in classes
            checkbox = '[x]' if checked else '[ ]'
            text = elem.get_text().strip()
            lines.append(f'- {checkbox} {text}')
        elif elem.name == 'p':
            text = elem.get_text().strip()
            if text:
                lines.append(text)
    
    return '\n'.join(lines).strip()

def read_local(path):
    """Read local TODO.md file."""
    workspace_root = Path(__file__).parent.parent.parent.parent
    full_path = workspace_root / path
    if not full_path.exists():
        raise FileNotFoundError(f"Local file not found: {full_path}")
    return full_path.read_text().strip()

def push_to_canvas(client, canvas_id, markdown_content):
    """Push markdown content to canvas."""
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

def normalize_for_comparison(text):
    """Normalize text for comparison (ignore whitespace differences)."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return '\n'.join(lines)

def show_diff(local_content, canvas_content):
    """Show unified diff between local and canvas."""
    local_lines = local_content.splitlines(keepends=True)
    canvas_lines = canvas_content.splitlines(keepends=True)
    
    diff = list(unified_diff(
        canvas_lines, local_lines,
        fromfile='canvas (Slack)',
        tofile='local (TODO.md)',
        lineterm=''
    ))
    
    if diff:
        print('\n'.join(diff))
    else:
        print("No differences found.")
    
    return len(diff) > 0

def main():
    parser = argparse.ArgumentParser(description='Sync TODO.md with Slack canvas')
    parser.add_argument('--project', '-p', required=True, choices=list(PROJECTS.keys()),
                        help='Project to sync')
    parser.add_argument('--action', '-a', required=True, choices=['check', 'push', 'pull'],
                        help='Action: check (show diff), push (local→canvas), pull (canvas→local)')
    parser.add_argument('--force', '-f', action='store_true',
                        help='Skip confirmation prompts')
    
    args = parser.parse_args()
    
    project = PROJECTS[args.project]
    token = get_token()
    
    if not token:
        print("Error: SLACK_BOT_TOKEN not found")
        sys.exit(1)
    
    client = WebClient(token=token)
    
    print(f"📋 Canvas Sync: {args.project}")
    print(f"   Canvas ID: {project['canvas_id']}")
    print(f"   Local: {project['local_path']}")
    print()
    
    # Read both sources
    try:
        canvas_content = read_canvas(client, project['canvas_id'], token)
        print("✓ Read canvas from Slack")
    except Exception as e:
        print(f"✗ Failed to read canvas: {e}")
        sys.exit(1)
    
    try:
        local_content = read_local(project['local_path'])
        print("✓ Read local TODO.md")
    except Exception as e:
        print(f"✗ Failed to read local file: {e}")
        sys.exit(1)
    
    print()
    
    # Compare
    local_normalized = normalize_for_comparison(local_content)
    canvas_normalized = normalize_for_comparison(canvas_content)
    
    has_diff = local_normalized != canvas_normalized
    
    if args.action == 'check':
        print("=== Differences ===")
        show_diff(local_content, canvas_content)
        
    elif args.action == 'push':
        if not has_diff:
            print("No differences - nothing to push.")
            return
        
        print("=== Changes to push (local → canvas) ===")
        show_diff(local_content, canvas_content)
        
        if not args.force:
            confirm = input("\nPush these changes to canvas? [y/N] ")
            if confirm.lower() != 'y':
                print("Aborted.")
                return
        
        push_to_canvas(client, project['canvas_id'], local_content)
        print("✓ Pushed to canvas")
        
    elif args.action == 'pull':
        if not has_diff:
            print("No differences - nothing to pull.")
            return
        
        print("=== Changes to pull (canvas → local) ===")
        show_diff(canvas_content, local_content)
        
        if not args.force:
            confirm = input("\nOverwrite local TODO.md with canvas content? [y/N] ")
            if confirm.lower() != 'y':
                print("Aborted.")
                return
        
        workspace_root = Path(__file__).parent.parent.parent.parent
        full_path = workspace_root / project['local_path']
        full_path.write_text(canvas_content)
        print(f"✓ Updated {project['local_path']}")

if __name__ == '__main__':
    main()

