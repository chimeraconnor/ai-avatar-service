#!/usr/bin/env python3
"""
Reddit Lead Extractor
Extracts lead data from SearXNG search results and creates CSV files
"""

import json
import csv
import urllib.parse
from datetime import datetime

def extract_post_id(url):
    """Extract Reddit post ID from URL"""
    # URL format: https://www.reddit.com/r/subreddit/comments/abcdef/title/
    parts = url.strip('/').split('/')
    if 'comments' in parts:
        idx = parts.index('comments')
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return ""

def extract_subreddit(url):
    """Extract subreddit from URL"""
    parts = url.strip('/').split('/')
    if 'r' in parts:
        idx = parts.index('r')
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return ""

def parse_searxng_results(json_file):
    """Parse SearXNG JSON results and extract lead data"""
    with open(json_file, 'r') as f:
        data = json.load(f)

    leads = []

    for result in data.get('results', []):
        url = result.get('url', '')
        title = result.get('title', '').replace('r/marketing on Reddit: ', '').replace('r/startups on Reddit: ', '')
        content = result.get('content', '')

        if not url or 'reddit.com' not in url:
            continue

        lead = {
            'post_url': url,
            'subreddit': extract_subreddit(url),
            'post_id': extract_post_id(url),
            'post_title': title,
            'post_content': content[:500],  # First 500 chars
            'upvotes': 0,  # Not available in SearXNG results
            'comments': 0,  # Not available in SearXNG results
            'intent_score': 'unknown',  # Will be scored manually
            'industry': 'marketing',  # Default, will be updated
            'notes': '',
            'extracted_date': datetime.now().isoformat()
        }

        leads.append(lead)

    return leads

def save_leads_to_csv(leads, filename):
    """Save leads to CSV file"""
    fieldnames = [
        'post_url', 'subreddit', 'post_id', 'post_title', 'post_content',
        'upvotes', 'comments', 'intent_score', 'industry', 'notes', 'extracted_date'
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leads)

    print(f"✅ Saved {len(leads)} leads to {filename}")

def main():
    """Main execution"""
    # Parse all search result files
    all_leads = []

    for i in range(1, 4):  # We have 3 search result files
        json_file = f'/tmp/leads-search-{i}.json'
        try:
            leads = parse_searxng_results(json_file)
            all_leads.extend(leads)
            print(f"📊 Parsed {len(leads)} leads from {json_file}")
        except FileNotFoundError:
            print(f"⚠️  {json_file} not found, skipping")
        except Exception as e:
            print(f"❌ Error parsing {json_file}: {e}")

    # Remove duplicates based on post_url
    seen_urls = set()
    unique_leads = []
    for lead in all_leads:
        if lead['post_url'] not in seen_urls:
            seen_urls.add(lead['post_url'])
            unique_leads.append(lead)

    print(f"\n🎯 Total unique leads: {len(unique_leads)}")

    # Save to CSV
    output_file = '/home/node/.openclaw/workspace/leads/sample-marketing-leads-2026-03-03.csv'
    save_leads_to_csv(unique_leads, output_file)

    # Print sample leads
    print("\n📋 Sample leads:")
    for i, lead in enumerate(unique_leads[:3], 1):
        print(f"\n{i}. {lead['subreddit']} - {lead['post_title']}")
        print(f"   URL: {lead['post_url']}")
        print(f"   Content: {lead['post_content'][:100]}...")

if __name__ == '__main__':
    main()
