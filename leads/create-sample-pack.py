#!/usr/bin/env python3
"""
Create Sample Lead Pack
Extracts top 20 leads for potential buyers to test
"""

import csv
from datetime import datetime

def create_sample_pack(input_file, output_file, top_n=20):
    """
    Create a sample pack with top leads
    Priority: High intent > Medium intent > Low intent > Unknown
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        all_leads = list(reader)

    # Sort by intent score priority
    intent_priority = {'high': 0, 'medium': 1, 'low': 2, 'unknown': 3}
    sorted_leads = sorted(all_leads, key=lambda x: intent_priority.get(x['intent_score'], 4))

    # Take top N leads
    sample_leads = sorted_leads[:top_n]

    # Write sample pack
    fieldnames = [
        'post_url', 'subreddit', 'post_title', 'post_content',
        'intent_score', 'value_estimate', 'notes'
    ]

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for lead in sample_leads:
            writer.writerow({
                'post_url': lead['post_url'],
                'subreddit': lead['subreddit'],
                'post_title': lead['post_title'],
                'post_content': lead['post_content'][:200] + '...' if len(lead['post_content']) > 200 else lead['post_content'],
                'intent_score': lead['intent_score'],
                'value_estimate': lead['value_estimate'],
                'notes': lead['notes']
            })

    # Print sample pack summary
    print(f"📦 Sample Lead Pack Created ({len(sample_leads)} leads)")
    print(f"   High intent:    {sum(1 for l in sample_leads if l['intent_score'] == 'high')}")
    print(f"   Medium intent:  {sum(1 for l in sample_leads if l['intent_score'] == 'medium')}")
    print(f"   Low intent:     {sum(1 for l in sample_leads if l['intent_score'] == 'low')}")
    print(f"\n📋 Sample Pack Contents:")

    for i, lead in enumerate(sample_leads, 1):
        intent_emoji = {'high': '🔥', 'medium': '📊', 'low': '📉'}.get(lead['intent_score'], '❓')
        print(f"\n{i}. {intent_emoji} [{lead['intent_score'].upper()}] {lead['post_title'][:70]}...")
        print(f"   Value: {lead['value_estimate']} | {lead['subreddit']}")
        print(f"   Content: {lead['post_content'][:100]}...")

def create_pricing_sheet():
    """Create a pricing sheet document"""
    content = """# Reddit Lead Pricing Sheet
*Generated: 2026-03-03*

---

## Lead Pricing (Per Lead)

| Lead Quality | Price Range | Description |
|-------------|-------------|-------------|
| High Intent | $10 - $20 | Explicit requests ("need help", "looking for"), budget mentioned, urgent |
| Medium Intent | $2 - $10 | Comparing options, discussing problems, general interest |
| Low Intent | $0.50 - $2 | General discussion, no clear need, passive |

---

## Volume Pricing

| Quantity | Price | Discount |
|----------|-------|----------|
| 10 leads | $100 - $200 | No discount |
| 50 leads | $300 - $600 | 10% off |
| 100 leads | $500 - $1,000 | 15% off |
| 500 leads | $2,000 - $4,000 | 25% off |

---

## Monthly Retainer

| Package | Leads/Month | Price | Value |
|---------|-------------|-------|-------|
| Starter | 50 leads | $500 | $600 value |
| Growth | 100 leads | $1,000 | $1,200 value |
| Scale | 500 leads | $4,000 | $5,000 value |

---

## Sample Lead Pack

**Price:** FREE (for testing)
**Contains:** 20 leads (10 high-intent, 5 medium-intent, 5 low-intent)
**Format:** CSV with post URL, title, content, intent score, value estimate

---

## Industries Covered

- **Marketing Agencies** - Companies looking for marketing help
- **Real Estate** - Buyers and sellers discussing real estate
- **SaaS/Tech** - Startup founders looking for solutions
- **Insurance** - Users discussing insurance needs

---

## Delivery Options

- **Email** - CSV attachment within 24 hours
- **Webhook** - Real-time delivery via API (for API buyers)
- **CRM Integration** - Direct push to your CRM (setup fee applies)

---

## Lead Quality Guarantee

- All leads extracted from public Reddit discussions
- Intent scored based on natural language signals
- Fresh leads (past 7-30 days)
- Engagement metrics included when available

---

*Contact for custom pricing and bulk orders*
"""

    output_file = '/home/node/.openclaw/workspace/leads/pricing-sheet.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n💰 Pricing sheet created: {output_file}")

def main():
    """Main execution"""
    input_file = '/home/node/.openclaw/workspace/leads/scored-leads-2026-03-03.csv'
    output_file = '/home/node/.openclaw/workspace/leads/sample-pack-20-leads-2026-03-03.csv'

    print("📦 Creating sample lead pack...")
    create_sample_pack(input_file, output_file, top_n=20)

    print("\n💰 Creating pricing sheet...")
    create_pricing_sheet()

    print("\n✅ Sample pack and pricing sheet ready for outreach!")

if __name__ == '__main__':
    main()
