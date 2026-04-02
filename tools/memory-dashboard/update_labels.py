#!/usr/bin/env python3
"""
Read cluster nodes from graph_data.json and generate concise 2-4 word labels.
"""

import json

# Read graph data
with open('/home/node/.openclaw/workspace/tools/memory-dashboard/graph_data.json', 'r') as f:
    data = json.load(f)

# Map cluster IDs to their node samples
cluster_samples = {}
for node in data['nodes']:
    cluster_id = node['cluster']
    if cluster_id not in cluster_samples:
        cluster_samples[cluster_id] = []
    cluster_samples[cluster_id].append({
        'text': node.get('text', ''),
        'title': node.get('title', ''),
        'summary': node.get('summary', '')
    })

# Generate concise labels
label_map = {}

for cluster_id, samples in cluster_samples.items():
    if not samples:
        label_map[cluster_id] = "empty cluster"
        continue

    # Collect titles and summaries
    titles = [s.get('title', '') for s in samples]
    summaries = [s.get('summary', '') for s in samples]

    # Generate label from combined text
    all_text = ' '.join([s for s in summaries if s]) + ' ' + ' '.join([t for t in titles if t])

    # Extract key concepts
    concepts = []
    # Look for common patterns
    text_lower = all_text.lower()

    # Common patterns
    if any(kw in text_lower for kw in ['memory', 'lesson', 'learned']):
        concepts.append('memory')
    if any(kw in text_lower for kw in ['zai', 'glm', 'model', 'api', 'token', 'quota']):
        concepts.append('zai glm')
    if any(kw in text_lower for kw in ['time', 'utc', 'ist', 'timezone']):
        concepts.append('timezone')
    if any(kw in text_lower for kw in ['discord', 'voice', 'tts', 'audio']):
        concepts.append('discord voice')
    if any(kw in text_lower for kw in ['pricing', 'cost', 'price', 'revenue', 'sales', 'lead']):
        concepts.append('pricing revenue')
    if any(kw in text_lower for kw in ['docker', 'setup', 'install', 'config']):
        concepts.append('docker setup')
    if any(kw in text_lower for kw in ['github', 'repo', 'git', 'commit', 'push']):
        concepts.append('github')
    if any(kw in text_lower for kw in ['qmd', 'embedding', 'search', 'semantic']):
        concepts.append('qmd search')
    if any(kw in text_lower for kw in ['dashboard', 'graph', 'brain', 'visualization']):
        concepts.append('brain dashboard')
    if any(kw in text_lower for kw in ['heart', 'reminder', 'check', 'cron']):
        concepts.append('heartbeat reminder')
    if any(kw in text_lower for kw in ['project', 'task', 'todo', 'work']):
        concepts.append('project todo')
    if any(kw in text_lower for kw in ['exec', 'shell', 'command', 'cli']):
        concepts.append('cli commands')
    if any(kw in text_lower for kw in ['searxng', 'search', 'web']):
        concepts.append('web search')
    if any(kw in text_lower for kw in ['bot', 'channel', 'message']):
        concepts.append('discord bot')

    # Create concise 2-4 word label
    if len(concepts) >= 2:
        label = ' / '.join(concepts[:2])
    elif len(concepts) >= 1:
        label = concepts[0] if concepts else 'general'
    else:
        label = 'misc'

    # Special cases for known clusters
    if cluster_id == 0:
        label = 'memory system'
    elif cluster_id == 179:
        label = 'lead generation'
    elif cluster_id == 160:
        label = 'pricing lessons'

    label_map[cluster_id] = label

# Update clusters in data
for cluster in data['clusters']:
    cluster_id = cluster['id']
    if cluster_id in label_map:
        cluster['label'] = label_map[cluster_id]

# Write back to file
with open('/home/node/.openclaw/workspace/tools/memory-dashboard/graph_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Updated {len(label_map)} cluster labels")
