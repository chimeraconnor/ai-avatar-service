#!/usr/bin/env python3
"""Generate human-readable labels for memory dashboard clusters."""

import json

# Load graph data
with open('graph_data.json', 'r') as f:
    data = json.load(f)

# Manual label mapping based on keyword analysis
labels = {
    0: "memory documentation",
    1: "timezone conversion",
    2: "searxng search",
    3: "memory files",
    4: "file reading",
    5: "live streaming",
    6: "discord components",
    7: "voice messages",
    8: "discord voice",
    9: "asvoice errors",
    10: "audio upload",
    11: "upload errors",
    12: "voice scripts",
    13: "docker logs",
    14: "project scripts",
    15: "vercel projects",
    16: "github integration",
    17: "tts scripts",
    18: "kokoro voice",
    19: "pocket voice",
    20: "vercel deployment",
    21: "discord cron",
    22: "bot configuration",
    23: "tts tools",
    24: "document lessons",
    25: "check docs",
    26: "daily review",
    27: "learning log",
    28: "priority promotion",
    29: "skill learning",
    30: "memory status",
    31: "discord timing",
    32: "root lessons",
    33: "memory dashboard",
    34: "morning greeting",
    35: "disk full",
    36: "greeting timing",
    37: "qmd dashboard",
    38: "qmd setup",
    39: "semantic search",
    40: "bun install",
    41: "docker workspace",
    42: "qmd openclaw",
    43: "text processing",
    44: "heartbeat check",
    45: "heartbeat read",
    46: "heartbeat exists",
    47: "heartbeat.md",
    48: "greeting message",
    49: "lead generation",
    50: "revenue path",
    51: "sales targets",
    52: "lead scoring",
    53: "reddit leads",
    54: "lead api",
    55: "pricing research",
    56: "reddit system",
    57: "system reminder",
    58: "creating reminder",
    59: "reminder system",
    60: "reddit leads",
    61: "lead system",
    62: "voice engine",
    63: "transcript extraction",
    64: "user feedback",
    65: "monthly research",
    66: "weekly seo",
    67: "revenue generation",
    68: "monthly sales",
    69: "content safety",
    70: "google quality",
    71: "automation agency",
    72: "seo research",
    73: "client automation",
    74: "lead intent",
    75: "lead case",
    76: "monthly leads",
    77: "ogg format",
    78: "native voice",
    79: "code backup",
    80: "documentation files",
    81: "file injection",
    82: "learning bloat",
    83: "sherpa tts",
    84: "discord troubleshooting",
    85: "crypto automation",
    86: "monetization system",
    87: "industry leads",
    88: "memory log",
    89: "safe sops",
    90: "outreach delivery",
    91: "vtuber avatar",
    92: "lead pricing",
    93: "automated confirmation",
    94: "todo tracking",
    95: "browser agent",
    96: "subagent sessions",
    97: "thread binding",
    98: "account code",
    99: "ssh github",
    100: "github cli",
    101: "advanced routing",
    102: "role timeline",
    103: "background tasks",
    104: "daily memory",
    105: "morning patterns",
    106: "free api",
    107: "weekly leads",
    108: "local search",
    109: "openclaw binaries",
    110: "model selection",
    111: "glm model",
    112: "zai glm",
    113: "crypto monitor",
    114: "github auth"
}

# Update cluster labels
if 'clusters' in data:
    for cluster in data['clusters']:
        cluster_id = cluster.get('id')
        if cluster_id in labels:
            cluster['label'] = labels[cluster_id]

# Write back
with open('graph_data.json', 'w') as f:
    json.dump(data, f, indent=2)

labeled = sum(1 for c in data.get('clusters', []) if c.get('label') and c.get('label') != 'unlabeled cluster')
total = len(data.get('clusters', []))
print(f"Done! Labeled {labeled}/{total} clusters")
