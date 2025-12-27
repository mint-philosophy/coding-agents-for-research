#!/usr/bin/env python3
"""
Slack Message Posting Utility

Usage:
    python post_message.py <channel> <message> [--token TOKEN]
    python post_message.py --test [--token TOKEN]

Examples:
    python post_message.py "#general" "Hello from the agent!"
    python post_message.py "proj-my-project" "Update: task complete"
    python post_message.py --test
"""

import os
import sys
import argparse
from typing import Optional
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def get_token(provided_token: Optional[str] = None) -> str:
    """Get Slack token from argument or environment."""
    if provided_token:
        return provided_token
    
    token = os.environ.get('SLACK_BOT_TOKEN')
    if not token:
        print("Error: No Slack token provided.")
        print("Either pass --token or set SLACK_BOT_TOKEN environment variable.")
        sys.exit(1)
    return token


def find_channel_id(client: WebClient, channel_name: str) -> Optional[str]:
    """Find channel ID from channel name."""
    channel_name = channel_name.lstrip('#')
    
    try:
        # Paginate through all channels
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


def post_message(token: str, channel: str, message: str) -> bool:
    """Post a message to a Slack channel.
    
    Args:
        token: Slack Bot Token (xoxb-...)
        channel: Channel name (with or without #) or channel ID
        message: Message text (supports Slack markdown)
        
    Returns:
        True if successful, False otherwise
    """
    client = WebClient(token=token)
    channel_name = channel.lstrip('#')
    
    # If channel starts with C and is alphanumeric, assume it's already an ID
    if channel.startswith('C') and channel[1:].isalnum():
        channel_id = channel
    else:
        channel_id = find_channel_id(client, channel_name)
        if not channel_id:
            print(f"Error: Channel '{channel_name}' not found")
            return False
    
    try:
        result = client.chat_postMessage(channel=channel_id, text=message)
        print(f"✓ Posted to #{channel_name}")
        return True
    except SlackApiError as e:
        error = e.response['error']
        if error == 'not_in_channel':
            print(f"Error: Bot is not a member of #{channel_name}. Please add the bot to the channel first.")
        elif error == 'channel_not_found':
            print(f"Error: Channel '{channel_name}' not found or bot doesn't have access.")
        else:
            print(f"Error posting message: {error}")
        return False


def test_connection(token: str) -> bool:
    """Test the Slack connection and token validity."""
    client = WebClient(token=token)
    
    try:
        result = client.auth_test()
        print(f"✓ Token is valid")
        print(f"  Bot: {result['user']}")
        print(f"  Team: {result['team']}")
        print(f"  URL: {result['url']}")
        return True
    except SlackApiError as e:
        print(f"✗ Token test failed: {e.response['error']}")
        return False


def list_channels(token: str) -> None:
    """List all accessible channels."""
    client = WebClient(token=token)
    
    try:
        result = client.conversations_list(
            types="public_channel,private_channel",
            limit=1000
        )
        
        print("Accessible channels:")
        for channel in sorted(result["channels"], key=lambda c: c["name"]):
            prefix = "🔒" if channel.get("is_private") else "#"
            print(f"  {prefix} {channel['name']}")
            
    except SlackApiError as e:
        print(f"Error listing channels: {e.response['error']}")


def set_channel_topic(token: str, channel: str, topic: str) -> bool:
    """Set a channel's topic.
    
    Args:
        token: Slack Bot Token
        channel: Channel name or ID
        topic: Topic text (max 250 chars)
    
    Returns:
        True if successful
    """
    client = WebClient(token=token)
    
    if not channel.startswith('C'):
        channel_id = find_channel_id(client, channel)
        if not channel_id:
            print(f"Error: Channel '{channel}' not found")
            return False
    else:
        channel_id = channel
    
    try:
        client.conversations_setTopic(channel=channel_id, topic=topic[:250])
        print(f"✓ Set topic for #{channel}")
        return True
    except SlackApiError as e:
        print(f"Error setting topic: {e.response['error']}")
        return False


def set_channel_purpose(token: str, channel: str, purpose: str) -> bool:
    """Set a channel's purpose/description.
    
    Args:
        token: Slack Bot Token
        channel: Channel name or ID
        purpose: Purpose text (max 250 chars)
    
    Returns:
        True if successful
    """
    client = WebClient(token=token)
    
    if not channel.startswith('C'):
        channel_id = find_channel_id(client, channel)
        if not channel_id:
            print(f"Error: Channel '{channel}' not found")
            return False
    else:
        channel_id = channel
    
    try:
        client.conversations_setPurpose(channel=channel_id, purpose=purpose[:250])
        print(f"✓ Set purpose for #{channel}")
        return True
    except SlackApiError as e:
        print(f"Error setting purpose: {e.response['error']}")
        return False


def create_channel(token: str, name: str, description: Optional[str] = None, is_private: bool = False) -> Optional[str]:
    """Create a new Slack channel.
    
    Args:
        token: Slack Bot Token (xoxb-...)
        name: Channel name (without #, will be lowercased and sanitized)
        description: Optional channel description/purpose
        is_private: Whether to create a private channel
        
    Returns:
        Channel ID if successful, None otherwise
    """
    client = WebClient(token=token)
    
    # Sanitize channel name (lowercase, no spaces, max 80 chars)
    clean_name = name.lower().replace(' ', '-').replace('_', '-')[:80]
    
    try:
        result = client.conversations_create(
            name=clean_name,
            is_private=is_private
        )
        channel_id = result['channel']['id']
        print(f"✓ Created channel #{clean_name} ({channel_id})")
        
        # Set description/purpose if provided
        if description:
            try:
                client.conversations_setPurpose(channel=channel_id, purpose=description[:250])
                print(f"  Set purpose: {description[:50]}...")
            except SlackApiError as e:
                print(f"  Warning: Could not set purpose: {e.response['error']}")
        
        return channel_id
        
    except SlackApiError as e:
        error = e.response['error']
        if error == 'name_taken':
            print(f"Error: Channel #{clean_name} already exists")
            # Return existing channel ID
            existing_id = find_channel_id(client, clean_name)
            if existing_id:
                print(f"  Existing channel ID: {existing_id}")
            return existing_id
        else:
            print(f"Error creating channel: {error}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Post messages to Slack channels",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument('channel', nargs='?', help='Channel name (e.g., #agent-kira or proj-agent-kira)')
    parser.add_argument('message', nargs='?', help='Message to post')
    parser.add_argument('--token', '-t', help='Slack Bot Token (or use SLACK_BOT_TOKEN env var)')
    parser.add_argument('--test', action='store_true', help='Test token validity')
    parser.add_argument('--list-channels', action='store_true', help='List accessible channels')
    parser.add_argument('--create-channel', metavar='NAME', help='Create a new channel with this name')
    parser.add_argument('--description', '-d', help='Channel description (for --create-channel)')
    parser.add_argument('--private', action='store_true', help='Create as private channel (for --create-channel)')
    parser.add_argument('--set-topic', nargs=2, metavar=('CHANNEL', 'TOPIC'), help='Set channel topic')
    parser.add_argument('--set-purpose', nargs=2, metavar=('CHANNEL', 'PURPOSE'), help='Set channel purpose/description')
    
    args = parser.parse_args()
    
    token = get_token(args.token)
    
    if args.test:
        sys.exit(0 if test_connection(token) else 1)
    
    if args.list_channels:
        list_channels(token)
        sys.exit(0)
    
    if args.create_channel:
        channel_id = create_channel(token, args.create_channel, args.description, args.private)
        sys.exit(0 if channel_id else 1)
    
    if args.set_topic:
        success = set_channel_topic(token, args.set_topic[0], args.set_topic[1])
        sys.exit(0 if success else 1)
    
    if args.set_purpose:
        success = set_channel_purpose(token, args.set_purpose[0], args.set_purpose[1])
        sys.exit(0 if success else 1)
    
    if not args.channel or not args.message:
        parser.print_help()
        print("\nError: Both channel and message are required.")
        sys.exit(1)
    
    success = post_message(token, args.channel, args.message)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

