#!/usr/bin/env python3
"""
Create sample pack from fresh leads
Takes fresh-leads-YYYY-MM-DD.csv and creates a 20-lead sample pack
"""

import csv
import random
from datetime import datetime

def create_sample_pack(input_file, output_file, num_leads=20):
    """Create a sample pack from fresh leads"""

    # Read all leads
    leads = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        leads = list(reader)

    print(f"📊 Total leads in file: {len(leads)}")

    # Separate by intent
    high_intent = [l for l in leads if l.get('intent') == 'high']
    medium_intent = [l for l in leads if l.get('intent') == 'medium']

    print(f"  • High intent: {len(high_intent)}")
    print(f"  • Medium intent: {len(medium_intent)}")

    # Select sample (mix of high and medium intent)
    num_high = min(10, len(high_intent))  # Up to 10 high-intent
    num_medium = min(10, len(medium_intent))  # Up to 10 medium-intent

    selected_high = random.sample(high_intent, num_high) if len(high_intent) > 0 else []
    selected_medium = random.sample(medium_intent, num_medium) if len(medium_intent) > 0 else []

    sample_leads = selected_high + selected_medium

    # Shuffle
    random.shuffle(sample_leads)

    # Write sample pack
    fieldnames = ['url', 'subreddit', 'title', 'content', 'intent', 'value', 'date_extracted']

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sample_leads)

    print(f"✅ Created sample pack: {output_file}")
    print(f"   Total leads: {len(sample_leads)}")
    print(f"   • High intent: {len(selected_high)}")
    print(f"   • Medium intent: {len(selected_medium)}")

    # Show sample leads
    print("\n📋 Sample leads (first 5):")
    for i, lead in enumerate(sample_leads[:5], 1):
        intent = lead.get('intent', 'unknown')
        title = lead.get('title', '')[:60]
        url = lead.get('url', '')
        print(f"\n{i}. [{intent.upper()}] {title}")
        print(f"   {url}")

    return len(sample_leads)

if __name__ == '__main__':
    input_file = '/home/node/.openclaw/workspace/leads/fresh-leads-2026-03-31.csv'
    output_file = '/home/node/.openclaw/workspace/leads/sample-pack-20-leads-2026-03-31.csv'

    print("📦 Creating sample pack from fresh leads...\n")
    create_sample_pack(input_file, output_file, 20)
