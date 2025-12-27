#!/usr/bin/env python3
"""
Create a Slack canvas as a channel tab.

Usage:
    python create_canvas.py <channel> <markdown_file> [--title TITLE]
    python create_canvas.py "proj-my-project" "projects/my-project/TODO.md" --title "Task List"
"""

import os
import sys
import argparse
from pathlib import Path
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


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


def find_channel_id(client, channel_name):
    """Find channel ID from channel name."""
    channel_name = channel_name.lstrip('#')
    
    try:
        cursor = None
        while True:
            result = client.conversations_list(
                types="public_channel,private_channel",
                limit=200,
                cursor=cursor
            )
            
            for channel in result["channels"]:
                if channel["name"] == channel_name:
                    return channel["id"]
            
            cursor = result.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break
                
    except SlackApiError as e:
        print(f"Error listing channels: {e.response['error']}")
        return None
    
    return None


def create_canvas_as_tab(token, channel, markdown_content, title=None):
    """Create a canvas as a channel tab.
    
    Args:
        token: Slack Bot Token
        channel: Channel name (with or without #) or channel ID
        markdown_content: Markdown content for the canvas
        title: Optional title for the canvas
        
    Returns:
        Canvas ID if successful, None otherwise
    """
    client = WebClient(token=token)
    channel_name = channel.lstrip('#')
    
    # Get channel ID if needed
    if not channel.startswith('C') or not channel[1:].isalnum():
        channel_id = find_channel_id(client, channel_name)
        if not channel_id:
            print(f"Error: Channel '{channel_name}' not found")
            return None
    else:
        channel_id = channel
    
    try:
        # Create canvas as channel tab
        result = client.conversations_canvases_create(
            channel_id=channel_id,
            document_content={
                'type': 'markdown',
                'markdown': markdown_content
            }
        )
        
        canvas_id = result.get('canvas_id')
        if canvas_id:
            print(f"✓ Created canvas as channel tab in #{channel_name}")
            print(f"  Canvas ID: {canvas_id}")
            if title:
                print(f"  Title: {title}")
            return canvas_id
        else:
            print(f"Error: No canvas_id in response")
            return None
            
    except SlackApiError as e:
        error = e.response.get('error', 'unknown_error')
        if error == 'not_in_channel':
            print(f"Error: Bot is not a member of #{channel_name}. Please add the bot to the channel first.")
        elif error == 'channel_not_found':
            print(f"Error: Channel '{channel_name}' not found or bot doesn't have access.")
        else:
            print(f"Error creating canvas: {error}")
            print(f"  Full error: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description='Create a Slack canvas as a channel tab',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument('channel', help='Channel name (e.g., #proj-agent-infra or proj-agent-infra) or channel ID')
    parser.add_argument('markdown_file', help='Path to markdown file to upload')
    parser.add_argument('--title', '-t', help='Optional title for the canvas')
    
    args = parser.parse_args()
    
    token = get_token()
    if not token:
        print("Error: SLACK_BOT_TOKEN not found")
        print("Set SLACK_BOT_TOKEN environment variable or add to .cursor/.api_keys.txt")
        sys.exit(1)
    
    # Read markdown file
    markdown_path = Path(args.markdown_file)
    if not markdown_path.is_absolute():
        # Relative to workspace root
        workspace_root = Path(__file__).parent.parent.parent.parent
        markdown_path = workspace_root / args.markdown_file
    
    if not markdown_path.exists():
        print(f"Error: File not found: {markdown_path}")
        sys.exit(1)
    
    try:
        content = markdown_path.read_text()
        print(f"✓ Loaded markdown file ({len(content)} chars)")
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Create canvas
    canvas_id = create_canvas_as_tab(token, args.channel, content, args.title)
    
    if canvas_id:
        print(f"\n✓ Success! Canvas created: {canvas_id}")
        sys.exit(0)
    else:
        print("\n✗ Failed to create canvas")
        sys.exit(1)


if __name__ == '__main__':
    main()
