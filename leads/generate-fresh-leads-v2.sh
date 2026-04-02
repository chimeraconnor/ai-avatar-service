#!/bin/bash
# Generate fresh Reddit leads via SearXNG - v2 with better error handling

SEARXNG_URL="http://89.167.66.83:8888"
OUTPUT_DIR="/home/node/.openclaw/workspace/leads"
DATE=$(date +%Y-%m-%d)
TEMP_DIR="/tmp/leads-$DATE"

mkdir -p "$TEMP_DIR"

# Search queries for high-intent leads
declare -a QUERIES=(
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
for i in "${!QUERIES[@]}"; do
    QUERY="${QUERIES[$i]}"
    echo "Searching ($((i+1))/${#QUERIES[@]}): $QUERY"

    # Encode query
    ENCODED_QUERY=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$QUERY', safe=''))")

    # Fetch results
    JSON_FILE="$TEMP_DIR/search-$i.json"
    curl -s "$SEARXNG_URL/search?q=$ENCODED_QUERY&format=json&results=30" -o "$JSON_FILE"

    # Check if JSON is valid
    if ! python3 -m json.tool "$JSON_FILE" > /dev/null 2>&1; then
        echo "  ⚠️  Invalid JSON response, skipping..."
        continue
    fi

    # Extract leads using Python
    python3 -c "
import json
import re
import csv
from datetime import datetime

with open('$JSON_FILE', 'r') as f:
    data = json.load(f)

results = data.get('results', [])
print(f'  📊 Found {len(results)} results')

with open('$OUTPUT_DIR/fresh-leads-$DATE.csv', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    for result in results:
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

            # Escape commas and newlines
            title = title.replace(',', ' ').replace('\n', ' ')
            content = content.replace(',', ' ').replace('\n', ' ')

            writer.writerow([url, subreddit, title, content, intent, value, datetime.now().isoformat()])
"

    sleep 1  # Be respectful to SearXNG
done

# Count total leads
TOTAL=$(tail -n +2 "$OUTPUT_DIR/fresh-leads-$DATE.csv" | wc -l)
echo ""
echo "✅ Generated $TOTAL fresh leads"
echo "📁 Saved to: $OUTPUT_DIR/fresh-leads-$DATE.csv"
echo ""

# Count by intent
HIGH_INTENT=$(tail -n +2 "$OUTPUT_DIR/fresh-leads-$DATE.csv" | grep ",high," | wc -l)
MEDIUM_INTENT=$(tail -n +2 "$OUTPUT_DIR/fresh-leads-$DATE.csv" | grep ",medium," | wc -l)

echo "📊 Lead breakdown:"
echo "  • High intent: $HIGH_INTENT"
echo "  • Medium intent: $MEDIUM_INTENT"
echo ""

# Show sample
echo "📋 Sample leads (first 3):"
tail -n +2 "$OUTPUT_DIR/fresh-leads-$DATE.csv" | head -3 | while IFS=',' read -r url subreddit title content intent value date; do
    echo "  • [$intent] $title"
    echo "    $url"
    echo ""
done

# Cleanup
rm -rf "$TEMP_DIR"
