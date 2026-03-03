#!/usr/bin/env python3
"""
Lead Scoring Script
Scores Reddit leads based on intent signals in title and content
"""

import csv
import re

# High-intent signals (worth $10-20/lead)
HIGH_INTENT_KEYWORDS = [
    'need help', 'looking for', 'recommendations', 'best agency',
    'need agency', 'hiring agency', 'seeking agency', 'want to hire',
    'budget', 'how much', 'pricing', 'urgent', 'asap', 'immediately',
    'struggling with', 'need recommendations', 'need help finding',
    'looking for marketing agency', 'performance based', 'result driven'
]

# Medium-intent signals (worth $2-10/lead)
MEDIUM_INTENT_KEYWORDS = [
    'how to find', 'advice needed', 'help with', 'questions about',
    'thinking about', 'considering', 'comparing', 'difference between',
    'any experience with', 'has anyone used', 'thoughts on',
    'recommendation', 'suggestions', 'ideas'
]

def calculate_intent_score(title, content):
    """
    Calculate intent score based on title and content
    Returns: 'high', 'medium', 'low', or 'unknown'
    """
    text = f"{title} {content}".lower()

    # Check for high-intent signals
    high_count = sum(1 for keyword in HIGH_INTENT_KEYWORDS if keyword.lower() in text)
    if high_count >= 1:
        return 'high'

    # Check for medium-intent signals
    medium_count = sum(1 for keyword in MEDIUM_INTENT_KEYWORDS if keyword.lower() in text)
    if medium_count >= 1:
        return 'medium'

    # If no clear signals, it's low intent
    if len(text.strip()) > 50:  # Has substantial content but no clear intent
        return 'low'

    return 'unknown'

def extract_budget(content):
    """Extract budget information if present"""
    budget_patterns = [
        r'\$\d+[,\d]*(k|K)?',  # $500, $1k, $10,000
        r'\d+\s*(dollars?|usd|eur|gbp)',  # 500 dollars
    ]

    for pattern in budget_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            return matches[0]

    return None

def score_leads(input_file, output_file):
    """Score leads and update the CSV"""
    scored_leads = []

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get('post_title', '')
            content = row.get('post_content', '')

            # Calculate intent score
            intent_score = calculate_intent_score(title, content)
            row['intent_score'] = intent_score

            # Extract budget if present
            budget = extract_budget(content)
            if budget:
                row['notes'] = f"Budget mentioned: {budget}"

            # Add value estimate
            if intent_score == 'high':
                row['value_estimate'] = '$10-20'
            elif intent_score == 'medium':
                row['value_estimate'] = '$2-10'
            elif intent_score == 'low':
                row['value_estimate'] = '$0.50-2'
            else:
                row['value_estimate'] = '$0-0.50'

            scored_leads.append(row)

    # Write back to CSV
    fieldnames = [
        'post_url', 'subreddit', 'post_id', 'post_title', 'post_content',
        'upvotes', 'comments', 'intent_score', 'industry', 'notes',
        'extracted_date', 'value_estimate'
    ]

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scored_leads)

    # Print statistics
    high = sum(1 for lead in scored_leads if lead['intent_score'] == 'high')
    medium = sum(1 for lead in scored_leads if lead['intent_score'] == 'medium')
    low = sum(1 for lead in scored_leads if lead['intent_score'] == 'low')
    unknown = sum(1 for lead in scored_leads if lead['intent_score'] == 'unknown')

    print(f"📊 Lead Scoring Results:")
    print(f"   High intent:    {high} ({high/len(scored_leads)*100:.1f}%)")
    print(f"   Medium intent:  {medium} ({medium/len(scored_leads)*100:.1f}%)")
    print(f"   Low intent:     {low} ({low/len(scored_leads)*100:.1f}%)")
    print(f"   Unknown:        {unknown} ({unknown/len(scored_leads)*100:.1f}%)")
    print(f"   Total:          {len(scored_leads)}")

    # Print sample high-intent leads
    print(f"\n🎯 Sample High-Intent Leads:")
    for lead in scored_leads:
        if lead['intent_score'] == 'high':
            print(f"\n   • {lead['post_title'][:80]}...")
            print(f"     Value: {lead['value_estimate']} | {lead['subreddit']}")
            if len([l for l in scored_leads if l['intent_score'] == 'high']) > 5:
                break  # Only show first 5

    return scored_leads

def main():
    """Main execution"""
    input_file = '/home/node/.openclaw/workspace/leads/sample-marketing-leads-2026-03-03.csv'
    output_file = '/home/node/.openclaw/workspace/leads/scored-leads-2026-03-03.csv'

    print("🔍 Scoring leads...")
    scored_leads = score_leads(input_file, output_file)
    print(f"\n✅ Scored leads saved to {output_file}")

if __name__ == '__main__':
    main()
