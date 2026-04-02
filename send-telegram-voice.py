#!/usr/bin/env python3
"""Send audio file as voice message to Telegram."""

import sys
import requests
import json

# Read bot token from OpenClaw config
try:
    with open('/home/node/.openclaw/openclaw.json', 'r') as f:
        config = json.load(f)
    bot_token = config['channels']['telegram']['botToken']
except Exception as e:
    print(f"Error reading config: {e}", file=sys.stderr)
    sys.exit(1)

CHAT_ID = sys.argv[1]
AUDIO_FILE = sys.argv[2]
CAPTION = sys.argv[3] if len(sys.argv) > 3 else ""

# Send voice message
url = f"https://api.telegram.org/bot{bot_token}/sendVoice"

with open(AUDIO_FILE, 'rb') as audio:
    files = {'voice': audio}
    data = {'chat_id': CHAT_ID}
    if CAPTION:
        data['caption'] = CAPTION

    response = requests.post(url, files=files, data=data)

if response.status_code == 200:
    print(f"Voice message sent successfully: {AUDIO_FILE}")
else:
    print(f"Error: {response.status_code} - {response.text}", file=sys.stderr)
    sys.exit(1)
