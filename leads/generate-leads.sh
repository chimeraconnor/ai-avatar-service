#!/bin/bash
# Automated Lead Generation Script
# Uses SearXNG to search Reddit for high-intent marketing leads

SEARXNG_URL="http://89.167.66.83:8888"
LEADS_DIR="/home/node/.openclaw/workspace/leads"
TIMESTAMP=$(date +%Y-%m-%d)

# Target subreddits and search queries
declare -A SEARCH_QUERIES=(
    ["marketing"]="site:reddit.com/r/marketing+need+help+with+marketing"
    ["startups"]="site:reddit.com/r/startups+looking+for+agency"
    ["entrepreneur"]="site:reddit.com/r/entrepreneur+need+marketing+help"
    ["seo"]="site:reddit.com/r/SEO+need+SEO+help"
)

echo "🔍 Starting Reddit lead generation..."
echo "📅 Date: $(date)"
echo ""

# Create output directory
mkdir -p "$LEADS_DIR/tmp"

# Counter for search results
search_num=1

for subreddit in "${!SEARCH_QUERIES[@]}"; do
    query="${SEARCH_QUERIES[$subreddit]}"
    output_file="$LEADS_DIR/tmp/search-${subreddit}-${TIMESTAMP}.json"

    echo "📊 Searching r/$subreddit..."
    curl -s "$SEARXNG_URL/search?q=${query}&format=json&results=50" > "$output_file"

    if [ -s "$output_file" ]; then
        result_count=$(jq '.results | length' "$output_file" 2>/dev/null || echo "0")
        echo "   ✅ Found $result_count results"
    else
        echo "   ⚠️  No results found"
    fi

    ((search_num++))
done

echo ""
echo "🎯 Lead generation complete!"
echo "📁 Files saved to: $LEADS_DIR/tmp/"
echo ""
echo "Next steps:"
echo "1. Run: python3 $LEADS_DIR/extract-leads.py"
echo "2. Run: python3 $LEADS_DIR/score-leads.py"
echo "3. Review: $LEADS_DIR/scored-leads-${TIMESTAMP}.csv"
