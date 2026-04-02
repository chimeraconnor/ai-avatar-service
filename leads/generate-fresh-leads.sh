#!/bin/bash
# Generate fresh Reddit leads via SearXNG

SEARXNG_URL="http://89.167.66.83:8888"
OUTPUT_DIR="/home/node/.openclaw/workspace/leads"
DATE=$(date +%Y-%m-%d)

# Search queries for high-intent leads
QUERIES=(
    'site:reddit.com/r/marketing "looking for" agency'
    'site:reddit.com/r/startups "need" marketing help'
    'site:reddit.com/r/marketing "recommend" agency'
    'site:reddit.com/r/SaaS "best marketing agency"'
    'site:reddit.com/r/SEO "need" SEO help'
)

echo "🔍 Generating fresh Reddit leads..."
echo "Date: $DATE"
echo "Output: $OUTPUT_DIR/fresh-leads-$DATE.csv"
echo ""

# Create CSV header
echo "url,subreddit,title,content,intent,value,date_extracted" > "$OUTPUT_DIR/fresh-leads-$DATE.csv"

# Search and extract leads
COUNT=0
for QUERY in "${QUERIES[@]}"; do
    echo "Searching: $QUERY"

    # Fetch results (encoded)
    ENCODED_QUERY=$(echo "$QUERY" | sed 's/ /%20/g')
    RESULTS=$(curl -s "$SEARXNG_URL/search?q=$ENCODED_QUERY&format=json&results=30")

    # Extract URLs and basic info
    echo "$RESULTS" | python3 -c "
import json
import sys
import re
from datetime import datetime

try:
    data = json.load(sys.stdin)
    for result in data.get('results', []):
        url = result.get('url', '')
        title = result.get('title', '').replace(' on Reddit: ', '').replace('r/marketing on Reddit: ', '').replace('r/startups on Reddit: ', '').replace('r/SaaS on Reddit: ', '').replace('r/SEO on Reddit: ', '')
        content = result.get('content', '')[:300]

        if 'reddit.com' in url:
            # Extract subreddit
            subreddit = re.search(r'/r/([^/]+)/', url)
            subreddit = subreddit.group(1) if subreddit else 'unknown'

            # Basic intent scoring
            intent = 'medium'
            value = '\$0.50-2'
            title_lower = title.lower()
            content_lower = content.lower()

            if any(word in title_lower for word in ['looking for', 'need', 'help', 'recommend', 'best']):
                if any(word in title_lower for word in ['agency', 'marketing', 'seo', 'help']):
                    intent = 'high'
                    value = '\$10-20'

            # Escape commas in CSV
            title = title.replace(',', ' ')
            content = content.replace(',', ' ')
            content = content.replace('\n', ' ')

            print(f'{url},{subreddit},{title},{content},{intent},{value},{datetime.now().isoformat()}')
except Exception as e:
    sys.stderr.write(f'Error: {e}\n')
" >> "$OUTPUT_DIR/fresh-leads-$DATE.csv"

    sleep 1  # Be respectful to SearXNG
done

# Count total leads
TOTAL=$(tail -n +2 "$OUTPUT_DIR/fresh-leads-$DATE.csv" | wc -l)
echo ""
echo "✅ Generated $TOTAL fresh leads"
echo "📁 Saved to: $OUTPUT_DIR/fresh-leads-$DATE.csv"
echo ""
echo "📊 Sample leads:"
tail -n +2 "$OUTPUT_DIR/fresh-leads-$DATE.csv" | head -3 | while IFS=',' read -r url subreddit title content intent value date; do
    echo "  • [$intent] $title"
    echo "    $url"
    echo ""
done
