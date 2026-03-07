# SEO APIs and MCPs for Production-Ready SEO Writer Agent

**Comprehensive research on APIs, MCPs, and integration patterns for SEO automation**

*Version: 1.0*
*Compiled: March 2026*

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Part 1: Keyword Research APIs](#part-1-keyword-research-apis)
3. [Part 2: SERP Analysis APIs](#part-2-serp-analysis-apis)
4. [Part 3: AI Content Detection APIs](#part-3-ai-content-detection-apis)
5. [Part 4: SEO Checking APIs](#part-4-seo-checking-apis)
6. [Part 5: Content Quality APIs](#part-5-content-quality-apis)
7. [Part 6: Schema Markup APIs](#part-6-schema-markup-apis)
8. [Part 7: OpenClaw MCP Integration](#part-7-openclaw-mcp-integration)
9. [Part 8: Recommendations & Phasing](#part-8-recommendations--phasing)
10. [Appendix: API Code Examples](#appendix-api-code-examples)

---

## Executive Summary

### Key Findings

**For MVP (Minimum Viable Product)**:
- **Keyword Research**: Use SearXNG self-hosted (free) + Ubersuggest free tier
- **SERP Analysis**: Serper.dev ($5/month starter) or DataForSEO (pay-as-you-go)
- **SEO Checking**: PageSpeed Insights API (free)
- **Content Quality**: Built-in grammar checking + readability algorithms

**For Production (Phase 2+)**:
- Ahrefs API ($399/month) - Industry standard for keyword research
- SEMrush API ($499/month) - Comprehensive SEO suite
- SERPAPI ($50/month) - Multi-platform SERP scraping
- Originality.ai ($30/month) - AI content detection
- Grammarly API (custom pricing) - Professional grammar checking

**Total Cost Ranges**:
- MVP setup: **$5-50/month** (minimal APIs)
- Production setup: **$500-1000/month** (full suite)

### Integration Strategy

1. **Phase 1 (MVP)**: Use free/low-cost APIs + manual fallbacks
2. **Phase 2 (Growth)**: Integrate paid APIs as scale demands
3. **Phase 3 (Enterprise)**: Full API suite with enterprise features

All APIs integrate with OpenClaw via:
- HTTP fetch (simple APIs)
- MCP server (complex APIs with streaming)
- Local tools (offline processing)

---

## Part 1: Keyword Research APIs

### 1.1 Paid APIs (Enterprise Grade)

#### Ahrefs API

**Pricing**:
- **Lite**: $399/month (500 requests)
- **Standard**: $999/month (2,000 requests)
- **Advanced**: $1,999/month (5,000 requests)

**Features**:
- Search volume (global and country-specific)
- Keyword Difficulty (KD) score
- CPC (Cost Per Click)
- Traffic potential
- SERP overview
- Backlink data
- Competitor analysis
- Keyword suggestions (from multiple sources)

**Key Endpoints**:
```
GET /v2/keywords
GET /v2/keywords/analysis
GET /v2/keywords/volume
GET /v2/serp/overview
```

**API Documentation**: https://ahrefs.com/api/documentation

**Why It's Industry Standard**:
- Largest backlink index in the industry
- Most accurate KD scores
- Global database with 12B+ keywords
- Fresh data (updated daily)

**Use Cases for SEO Writer**:
- Primary keyword difficulty assessment
- Find related keywords with low competition
- Analyze competitor keyword rankings
- Identify content gaps

**Rate Limits**:
- Lite: 500 requests/month
- Standard: 2,000 requests/month
- Additional requests: $0.50 each

**Sample Request**:
```bash
curl -X GET "https://api.ahrefs.com/v2/keywords?keyword=keyword+research&limit=5" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Sample Response**:
```json
{
  "keyword": "keyword research",
  "volume": 8100,
  "kd": 37,
  "cpc": 2.45,
  "traffic_potential": 4500,
  "serp_features": ["featured_snippet", "people_also_ask"],
  "related_keywords": [...]
}
```

---

#### SEMrush API

**Pricing**:
- **Power**: $499/month (5,000 units)
- **Professional**: $899/month (15,000 units)
- **Enterprise**: Custom pricing

**Pricing Model**: Units-based system
- 1 unit = 1 basic request
- Complex requests cost more units
- Keyword volume: 10 units
- Backlink analysis: 20 units

**Features**:
- Keyword Magic Tool (2M+ keywords per query)
- Keyword Difficulty (0-100)
- Search volume data
- CPC and competition metrics
- SERP analysis
- Position tracking
- Domain analytics
- Backlink audit

**Key Endpoints**:
```
POST /api/v3/keyword_magic/keywords_info
POST /api/v3/domain_overview/organic
POST /api/v3/backlinks/anchor_text
POST /api/v3/url/serp
```

**API Documentation**: https://www.semrush.com/api-docs/

**Unique Features**:
- Keyword Magic Tool with advanced filters
- Historical keyword data (up to 6 years)
- Competitor gap analysis
- Local SEO data (150+ countries)

**Use Cases for SEO Writer**:
- Bulk keyword research with filters
- Keyword gap analysis vs competitors
- Find trending keywords by topic
- Historical trend analysis

**Rate Limits**:
- 1,000 requests/minute
- Monthly units depend on plan

**Sample Request**:
```bash
curl -X POST "https://api.semrush.com/analytics/v1/?type=domain_ranks&domain=example.com&key=YOUR_API_KEY&export_columns=Ph,Po,Nq,Tg" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Sample Response**:
```json
{
  "Domain": "example.com",
  "Database": "us",
  "Updated": "2025-03-01",
  "Rankings": [
    {
      "Keyword": "keyword research",
      "Position": 5,
      "Previous Position": 7,
      "Search Volume": 8100,
      "Traffic (%)": 15.3,
      "Traffic": 1240,
      "Trend": [1.2, 1.3, 1.1, ...],
      "CPC": 2.45
    }
  ]
}
```

---

#### Moz API

**Pricing**:
- **Standard**: $150/month (15,000 rows)
- **Medium**: $250/month (50,000 rows)
- **Large**: $500/month (150,000 rows)

**Pricing Model**: Rows/month
- 1 keyword = 1 row
- Bulk requests use more rows

**Features**:
- Keyword Difficulty (0-100)
- Search volume (via Google data)
- Organic CTR estimates
- SERP features
- Priority score (volume × difficulty)
- Domain Authority (DA)
- Page Authority (PA)
- Link metrics

**Key Endpoints**:
```
POST /v2/url_metrics
POST /v2/keyword_metrics
GET /v2/suggested_keywords
```

**API Documentation**: https://moz.com/products/moz-api

**Unique Features**:
- DA/PA scores (industry standard)
- Priority score for content prioritization
- SERP feature tracking
- Link Explorer integration

**Use Cases for SEO Writer**:
- Quick difficulty assessment (Priority score)
- Keyword suggestions by topic
- SERP feature opportunities
- Authority-based keyword selection

**Rate Limits**:
- 10 requests/second
- Monthly rows based on plan

**Sample Request**:
```bash
curl -X POST "https://lsapi.seomoz.com/v2/keyword_metrics" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data": [{"keyword": "keyword research", "country": "US"}]}'
```

**Sample Response**:
```json
{
  "results": [
    {
      "keyword": "keyword research",
      "monthly_volume": 8100,
      "difficulty": 37,
      "priority": 57.7,
      "organic_ctr": 32.5,
      "serp_features": ["featured_snippet", "people_also_ask"]
    }
  ]
}
```

---

#### Ubersuggest API

**Pricing**:
- **Individual**: $29/month (100 searches/day)
- **Business**: $49/month (unlimited searches)
- **Enterprise**: $99/month (API access)

**Features**:
- Keyword volume and difficulty
- Keyword suggestions
- SERP analysis
- Content ideas
- Backlink data
- Site audit

**Key Endpoints**:
```
GET /api/v2/keyword_ideas
GET /api/v2/serp_lookup
GET /api/v2/content_ideas
```

**API Documentation**: https://neilpatel.com/api/

**Why It's Good for MVP**:
- Affordable entry point
- Simple API design
- Good keyword suggestions
- Includes SERP analysis

**Use Cases for SEO Writer**:
- Keyword research for content
- Find related keywords
- SERP feature tracking
- Content topic suggestions

**Sample Request**:
```bash
curl -X GET "https://api.neilpatel.com/api/v2/keyword_ideas?keyword=keyword+research&country_code=us" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

#### DataForSEO API

**Pricing**:
- **Pay-as-you-go**: No monthly fee
- **Minimum deposit**: $100
- **Usage-based pricing**:
  - Keywords Data: $0.001 per keyword
  - SERP: $0.003 per result
  - Backlinks: $0.002 per backlink

**Features**:
- All-in-one API suite:
  - Keywords Data (volume, difficulty, CPC)
  - SERP API (Google, Bing, Yahoo)
  - Backlinks API
  - On-page API
  - Ranking Tracker
  - Domain Analytics
  - Content Analysis

**Key Endpoints**:
```
POST /v3/keywords_data/google_ads/search_volume/live
POST /v3/serp/google/organic/live/advanced
POST /v3/backlinks/live
POST /v3/on_page/task_post
```

**API Documentation**: https://docs.dataforseo.com/

**Why It's Great for Startups**:
- No monthly commitment
- Comprehensive SEO data
- Fresh data (updated daily)
- Pay only for what you use

**Use Cases for SEO Writer**:
- Complete SEO data pipeline
- Competitor analysis
- Keyword research with metrics
- SERP tracking

**Rate Limits**:
- 1,000 requests/minute
- 20,000 requests/day

**Sample Request**:
```bash
curl -X POST "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live" \
  -H "Authorization: Basic BASE64_ENCODED_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": [{"keyword": "keyword research", "location_code": 2840}]}'
```

**Sample Response**:
```json
{
  "tasks": [
    {
      "result": [
        {
          "keyword": "keyword research",
          "search_volume": 8100,
          "cpc": 2.45,
          "competition": 0.73,
          "competition_index": 73,
          "keyword_information": {
            "last_updated_time": "2025-03-01"
          }
        }
      ]
    }
  ]
}
```

---

### 1.2 Free/Tiered APIs

#### Google Keyword Planner (via Google Ads API)

**Pricing**:
- **Free**: Limited to Google Ads account holders
- **API Access**: Requires Google Ads API developer token

**Features**:
- Monthly search volume
- Competition level (low, medium, high)
- Suggested bid (CPC)
- Keyword suggestions
- Historical data

**Key Endpoints**:
```
GET https://googleads.googleapis.com/v16/keywordPlanIdeas:generateKeywordIdeas
```

**API Documentation**: https://developers.google.com/google-ads/api/fields/v16/keyword_plan_idea

**Limitations**:
- Requires Google Ads account
- API requires developer token approval
- Rate limits apply (10,000 requests/day)
- Data is approximate ranges (not exact)

**Use Cases for SEO Writer**:
- Free keyword research
- Get search volume estimates
- Find related keywords

**Sample Request**:
```bash
curl -X POST "https://googleads.googleapis.com/v16/customers/CUSTOMER_ID/keywordPlanIdeaService:generateKeywordIdeas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -H "developer-token: YOUR_DEVELOPER_TOKEN" \
  -d '{
    "keywordSeed": {
      "keywords": ["keyword research"]
    },
    "keywordPlanNetwork": "GOOGLE_SEARCH",
    "includeAdultKeywords": false
  }'
```

---

#### Google Trends API (via PyTrends)

**Pricing**: **Free**

**Features**:
- Search trend data over time
- Related queries
- Regional interest
- Category-based trends
- Real-time trending topics

**Key Endpoints**:
```
GET https://trends.google.com/trends/api/explore
GET https://trends.google.com/trends/api/widgetdata/multiline
```

**Note**: Not an official API, use Python library (PyTrends)

**PyTrends Documentation**: https://pypi.org/project/pytrends/

**Use Cases for SEO Writer**:
- Identify trending topics
- Seasonal keyword analysis
- Regional interest by location
- Keyword trend comparison

**Python Example**:
```python
from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["keyword research"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='US', gprop='')
interest_over_time_df = pytrends.interest_over_time()
```

---

### 1.3 Free Alternatives (No API)

#### SearXNG Self-Hosted (RECOMMENDED FOR MVP)

**Pricing**: **Free** (self-hosted)

**Features**:
- Keyword suggestion via search autocomplete
- SERP analysis (via search results)
- People Also Ask questions
- Related searches
- Multi-engine aggregation

**How to Use for Keyword Research**:
1. Search primary keyword
2. Extract "People Also Ask" questions
3. Analyze top 10 results
4. Find related search terms

**SearXNG Setup**:
- Already configured in OpenClaw
- URL: http://89.167.66.83:8888
- Self-hosted Docker container
- JSON API output

**Use Cases for SEO Writer**:
- Free keyword research
- SERP analysis without API
- Find PAA questions
- Competitor analysis (via web_fetch)

**Python Example**:
```python
import requests
import json

SEARXNG_URL = "http://89.167.66.83:8888"

def search_keyword(query):
    """Search via SearXNG and return results"""
    response = requests.get(f"{SEARXNG_URL}/search", params={
        "q": query,
        "format": "json",
        "language": "en-US"
    })
    return response.json()

results = search_keyword("keyword research")
print(json.dumps(results, indent=2))
```

---

#### Google Suggest API (Unofficial)

**Pricing**: **Free** (rate limited)

**Endpoint**:
```
GET http://suggestqueries.google.com/complete/search?output=firefox&q=keyword
```

**Features**:
- Autocomplete suggestions
- Fast response
- No API key required

**Limitations**:
- Rate limited (unofficial)
- No search volume or difficulty
- Only suggestions, no metrics

**Use Cases for SEO Writer**:
- Get keyword suggestions quickly
- Generate long-tail ideas
- Free fallback when APIs fail

**Python Example**:
```python
import requests
import json

def get_suggestions(query):
    """Get Google autocomplete suggestions"""
    response = requests.get(
        "http://suggestqueries.google.com/complete/search",
        params={
            "output": "firefox",
            "q": query,
            "hl": "en"
        }
    )
    return response.json()[1]  # Return only suggestions

suggestions = get_suggestions("keyword research")
print(suggestions)
# Output: ['keyword research', 'keyword research tools', 'keyword research seo', ...]
```

---

#### AnswerThePublic (via Web Scraping)

**Pricing**:
- **Free**: 3 searches/day (with signup)
- **Pro**: $9/month (unlimited)

**Features**:
- Visual keyword research
- Question-based keywords
- Preposition keywords
- Comparison keywords
- Alphabetical keywords

**Note**: No official API, requires web scraping

**Use Cases for SEO Writer**:
- Find question-based keywords
- Generate long-tail ideas
- Content gap analysis

**Python Example** (web scraping):
```python
import requests
from bs4 import BeautifulSoup

def answerthepublic_search(query):
    """Scrape AnswerThePublic (simplified)"""
    # This is a conceptual example - actual scraping requires handling
    # anti-bot measures and may violate TOS
    url = f"https://answerthepublic.com/?q={query}"
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 ..."
    })
    # Parse and extract questions...
    return questions
```

---

### 1.4 Comparison Summary

| API | Price/Month | Volume Data | KD Score | Unique Features | Best For |
|-----|------------|-------------|----------|-----------------|----------|
| **Ahrefs** | $399 | ✅ Yes | ✅ Yes | Largest backlink index, accurate KD | Enterprise SEO |
| **SEMrush** | $499 | ✅ Yes | ✅ Yes | Keyword Magic Tool, historical data | Agency work |
| **Moz** | $150 | ✅ Yes | ✅ Yes | DA/PA scores, Priority score | Quick assessment |
| **Ubersuggest** | $29 | ✅ Yes | ✅ Yes | Affordable, simple API | MVP/Startups |
| **DataForSEO** | Pay-as-you-go | ✅ Yes | ✅ Yes | Comprehensive, no commitment | Startups |
| **Google Keyword Planner** | Free | ✅ Yes | ❌ No | Free, official Google data | Free option |
| **SearXNG** | Free | ❌ No | ❌ No | Free SERP analysis | MVP fallback |

---

## Part 2: SERP Analysis APIs

### 2.1 SERP Scraping APIs

#### SERPAPI

**Pricing**:
- **Free**: 100 searches/month
- **Starter**: $50/month (5,000 searches)
- **Pro**: $250/month (25,000 searches)
- **Business**: $500/month (100,000 searches)

**Supported Platforms**:
- Google (all countries)
- Google Images, Google News, Google Shopping
- Google Maps
- YouTube
- Bing
- DuckDuckGo
- Yahoo
- Amazon
- eBay
- Naver
- Baidu

**Key Endpoints**:
```
GET /search (Google)
GET /search.json (Google Images)
GET /search.json (Google News)
GET /search.json (Google Shopping)
GET /search.json (Google Maps)
GET /search.json (Bing)
```

**API Documentation**: https://serpapi.com/

**Features**:
- Organic results
- Featured snippets
- People Also Ask (PAA)
- Related searches
- Knowledge graph
- Local pack
- Images, videos, news
- Shopping results

**Why SERPAPI**:
- Multi-platform support
- Structured JSON output
- Reliable and fast
- Good documentation
- Free tier for testing

**Use Cases for SEO Writer**:
- SERP feature tracking
- Competitor analysis
- Featured snippet opportunities
- PAA question extraction

**Rate Limits**:
- Free: 100 requests/month
- Paid: Depends on plan

**Sample Request**:
```bash
curl -X GET "https://serpapi.com/search?engine=google&q=keyword+research&api_key=YOUR_API_KEY"
```

**Sample Response**:
```json
{
  "organic_results": [
    {
      "position": 1,
      "title": "Keyword Research Guide for Beginners",
      "link": "https://example.com/keyword-research",
      "snippet": "Learn keyword research...",
      "displayed_link": "example.com › keyword-research"
    }
  ],
  "related_questions": [
    {
      "question": "What is keyword research?",
      "snippet": "Keyword research is...",
      "title": "What is keyword research?",
      "link": "https://example.com/what-is-keyword-research"
    }
  ],
  "answer_box": {
    "type": "organic_result",
    "title": "Keyword Research",
    "snippet": "Keyword research is the process of finding..."
  }
}
```

---

#### Serper.dev

**Pricing**:
- **Starter**: $5/month (2,500 searches)
- **Business**: $50/month (50,000 searches)
- **Enterprise**: Custom pricing

**Features**:
- Google Search
- Google Images
- Google Videos
- Google News
- Google Shopping
- Google Maps

**Key Endpoints**:
```
POST /search (Google)
POST /images (Google Images)
POST /news (Google News)
POST /shopping (Google Shopping)
```

**API Documentation**: https://serper.dev/

**Why Serper.dev**:
- Very affordable starter plan ($5/month)
- Fast response times
- Simple API design
- Good documentation

**Use Cases for SEO Writer**:
- SERP analysis
- Featured snippet tracking
- PAA question extraction
- Competitor ranking

**Rate Limits**:
- Depends on plan (2,500-50,000/month)

**Sample Request**:
```bash
curl -X POST "https://google.serper.dev/search" \
  -H "X-API-KEY: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "keyword research", "gl": "us", "hl": "en"}'
```

**Sample Response**:
```json
{
  "organic": [
    {
      "title": "Keyword Research Guide for Beginners",
      "link": "https://example.com/keyword-research",
      "snippet": "Learn keyword research...",
      "position": 1
    }
  ],
  "peopleAlsoAsk": [
    {
      "question": "What is keyword research?",
      "snippet": "Keyword research is...",
      "title": "What is keyword research?",
      "link": "https://example.com/what-is-keyword-research"
    }
  ],
  "answerBox": {
    "title": "Keyword Research",
    "snippet": "Keyword research is the process of finding..."
  }
}
```

---

#### DataForSEO SERP API

**Pricing**: Pay-as-you-go (see Part 1.1)

**Features**:
- Google (all countries and languages)
- Google Images, Google News, Google Shopping
- Google Maps
- Google Pack
- Google Featured Snippets
- Bing
- Yahoo
- Naver
- Baidu
- Yandex
- YouTube

**Key Endpoints**:
```
POST /v3/serp/google/organic/live/advanced
POST /v3/serp/google/images/live
POST /v3/serp/google/news/live
POST /v3/serp/google/maps/live
POST /v3/serp/bing/organic/live
```

**API Documentation**: https://docs.dataforseo.com/v3/serp-api/

**Why DataForSEO**:
- Comprehensive platform support
- Fresh data (updated daily)
- Pay-as-you-go (no monthly)
- Integrates with other DataForSEO products

**Use Cases for SEO Writer**:
- Multi-platform SERP tracking
- International SEO (local SERPs)
- Featured snippet tracking
- Competitor analysis

**Sample Request**:
```bash
curl -X POST "https://api.dataforseo.com/v3/serp/google/organic/live/advanced" \
  -H "Authorization: Basic BASE64_ENCODED_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "keyword research",
    "location_code": 2840,
    "language_code": "en",
    "depth": 100
  }'
```

---

#### Bing Search API

**Pricing**:
- **Free**: 1,000 transactions/month
- **S1**: $7/month (3,000 transactions)
- **S2**: $40/month (20,000 transactions)
- **S3**: $60/month (50,000 transactions)

**Features**:
- Web search
- Image search
- Video search
- News search
- Web pages (HTML)
- Related searches
- Spelling suggestions

**Key Endpoints**:
```
GET https://api.bing.microsoft.com/v7.0/search
GET https://api.bing.microsoft.com/v7.0/images/search
GET https://api.bing.microsoft.com/v7.0/news/search
```

**API Documentation**: https://docs.microsoft.com/en-us/bing/search-apis/

**Why Bing API**:
- Free tier available
- Official Microsoft API
- Reliable and stable
- Good documentation

**Use Cases for SEO Writer**:
- SERP analysis (Bing)
- Cross-platform tracking
- Free option for testing

**Sample Request**:
```bash
curl -X GET "https://api.bing.microsoft.com/v7.0/search?q=keyword+research&count=10" \
  -H "Ocp-Apim-Subscription-Key: YOUR_API_KEY"
```

---

#### Google Custom Search JSON API

**Pricing**:
- **Free**: 100 queries/day
- **CSE 200**: $5/1,000 queries
- **CSE 1000**: $2/1,000 queries
- **CSE 10000**: $0.5/1,000 queries

**Features**:
- Custom search engine configuration
- Web search
- Image search
- Video search
- News search

**Key Endpoints**:
```
GET https://www.googleapis.com/customsearch/v1
```

**API Documentation**: https://developers.google.com/custom-search/v1/overview

**Why Custom Search API**:
- Official Google API
- Free tier for testing
- Configurable (choose sources)
- Reliable

**Use Cases for SEO Writer**:
- SERP analysis
- Competitor tracking
- Free fallback option

**Sample Request**:
```bash
curl -X GET "https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_CSE_ID&q=keyword+research"
```

---

### 2.2 Free Alternatives

#### SearXNG (Self-Hosted)

**Pricing**: **Free** (see Part 1.3)

**Features for SERP Analysis**:
- Multi-engine results
- SERP feature detection (via parsing)
- Featured snippets
- People Also Ask
- Related searches

**Limitations**:
- No structured SERP feature data (must parse HTML)
- Slower than dedicated APIs
- No historical tracking

**Use Cases for SEO Writer**:
- Free SERP analysis
- MVP keyword research
- Competitor research (via web_fetch)

---

#### DuckDuckGo Instant Answer API (Deprecated)

**Status**: No longer publicly available

**Alternative**: Use SearXNG (includes DuckDuckGo results)

---

### 2.3 Comparison Summary

| API | Price/Month | Platforms | SERP Features | Free Tier | Best For |
|-----|------------|-----------|---------------|-----------|----------|
| **SERPAPI** | $50 | 10+ | ✅ Yes | 100 searches | Multi-platform |
| **Serper.dev** | $5 | Google | ✅ Yes | No (trial) | Budget |
| **DataForSEO** | Pay-as-you-go | 10+ | ✅ Yes | No | Startups |
| **Bing API** | $7 | Bing | ❌ Limited | 1,000 queries | Microsoft ecosystem |
| **Google Custom Search** | $5/1,000 | Google | ❌ No | 100 queries/day | Free testing |
| **SearXNG** | Free | 70+ | ❌ Manual | Unlimited | MVP fallback |

---

## Part 3: AI Content Detection APIs

### 3.1 Content Detection APIs

#### Originality.ai

**Pricing**:
- **Pay-as-you-go**:
  - $20 for 20,000 words ($0.001/word)
  - $30 for 30,000 words
  - $200 for 300,000 words

**Features**:
- AI probability score (0-100%)
- Humanization score
- Plagiarism detection (built-in)
- Batch processing
- API access

**Key Endpoints**:
```
POST /api/v1/scan/ai
POST /api/v1/scan/plagiarism
```

**API Documentation**: https://originality.ai/api

**Why Originality.ai**:
- Most accurate AI detector
- Includes plagiarism check
- Simple pricing (per word)
- Good documentation

**Use Cases for SEO Writer**:
- Quality assurance before delivery
- Detect AI-generated content
- Humanization assessment

**Sample Request**:
```bash
curl -X POST "https://api.originality.ai/api/v1/scan/ai" \
  -H "X-OAI-API-KEY: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Your text here...",
    "title": "Keyword Research Guide"
  }'
```

**Sample Response**:
```json
{
  "score": {
    "original": 87,
    "ai": 13
  },
  "ai": false,
  "original": true
}
```

---

#### ZeroGPT

**Pricing**:
- **Free**: 10,000 characters/day
- **Pro**: $9.99/month (150,000 characters)
- **Enterprise**: Custom pricing

**Features**:
- AI probability score
- Batch analysis
- Text highlighting (AI vs human sections)
- Detailed report

**Key Endpoints**:
```
POST /api/v1/detect
```

**API Documentation**: https://zerogpt.com/api

**Why ZeroGPT**:
- Free tier for testing
- Good accuracy
- Detailed reporting

**Use Cases for SEO Writer**:
- AI detection
- Content quality check
- Free option for small volumes

---

#### GPTZero

**Pricing**:
- **Free**: 5,000 characters/month
- **Essential**: $10/month (50,000 characters)
- **Premium**: $25/month (150,000 characters)
- **Professional**: $75/month (500,000 characters)

**Features**:
- AI probability score
- Per-sentence analysis
- Highlight AI sections
- Batch processing
- API access

**Key Endpoints**:
```
POST /api/v1/predict/text
```

**API Documentation**: https://gptzero.me/api

**Why GPTZero**:
- Per-sentence analysis (granular)
- Good documentation
- Multiple pricing tiers

**Use Cases for SEO Writer**:
- Granular AI detection
- Identify AI sections
- Quality assurance

---

#### Turnitin

**Pricing**:
- **Educational**: Custom pricing (per institution)
- **Individual**: Not available directly

**Features**:
- Plagiarism detection
- AI writing detection
- Similarity report
- Extensive database (academic)

**Note**: Turnitin is primarily for educational institutions, not general API access

**Use Cases for SEO Writer**:
- **Not recommended** for SEO content (expensive, institutional)

---

#### Copyleaks

**Pricing**:
- **Subscription**: $9.99/month (100 pages)
- **Pay-as-you-go**: Custom pricing
- **Enterprise**: Custom pricing

**Features**:
- Plagiarism detection
- AI content detection
- Code detection
- Similarity report

**Key Endpoints**:
```
POST /api/v1/scan
```

**API Documentation**: https://api.copyleaks.com/

**Why Copyleaks**:
- Dual detection (plagiarism + AI)
- Good pricing
- Multiple content types

**Use Cases for SEO Writer**:
- Plagiarism check
- AI detection
- Content originality

---

### 3.2 Free Alternatives

#### Built-in Detection (via AI Model)

**Pricing**: **Free**

**How It Works**:
- Use AI model's self-awareness
- Ask AI to identify AI-generated content
- Not as accurate as dedicated tools

**Limitations**:
- Low accuracy
- Model bias
- Not reliable for production

**Use Cases for SEO Writer**:
- Preliminary check
- Free fallback

---

#### OpenAI Content Policy API

**Pricing**: **Free** (included with OpenAI API)

**Features**:
- AI-generated text detection
- Moderation check
- Policy compliance

**Limitations**:
- Not specifically for SEO
- False positives
- Limited accuracy

**Use Cases for SEO Writer**:
- **Not recommended** for SEO quality checks

---

### 3.3 Comparison Summary

| API | Price/Month | Accuracy | Plagiarism Check | Free Tier | Best For |
|-----|------------|----------|------------------|-----------|----------|
| **Originality.ai** | $30 | ⭐⭐⭐⭐⭐ | ✅ Yes | No | Production QA |
| **ZeroGPT** | $9.99 | ⭐⭐⭐⭐ | ❌ No | 10K chars/day | Budget |
| **GPTZero** | $10 | ⭐⭐⭐⭐ | ❌ No | 5K chars/month | Granular analysis |
| **Copyleaks** | $9.99 | ⭐⭐⭐ | ✅ Yes | No | Plagiarism + AI |
| **Turnitin** | N/A | ⭐⭐⭐⭐⭐ | ✅ Yes | No | Education only |

---

## Part 4: SEO Checking APIs

### 4.1 Performance APIs

#### PageSpeed Insights API

**Pricing**: **Free** (with quotas)

**Features**:
- Core Web Vitals (LCP, FID, CLS)
- Performance score (0-100)
- Lab data (Lighthouse)
- Field data (CrUX)
- Recommendations
- Mobile and desktop analysis

**Key Endpoints**:
```
GET https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL
GET https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&strategy=mobile
GET https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&strategy=desktop
```

**API Documentation**: https://developers.google.com/speed/docs/insights/v5/get-started

**Quotas**:
- 25,000 requests/day
- 5 requests/second

**Why PageSpeed Insights API**:
- **Free**
- Official Google API
- Core Web Vitals (important for SEO)
- Reliable and accurate

**Use Cases for SEO Writer**:
- Technical SEO recommendations
- Performance optimization notes
- Mobile-first analysis

**Sample Request**:
```bash
curl -X GET "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=mobile&key=YOUR_API_KEY"
```

**Sample Response**:
```json
{
  "lighthouseResult": {
    "categories": {
      "performance": {
        "score": 0.85
      }
    },
    "audits": {
      "first-contentful-paint": {
        "score": 0.9,
        "displayValue": "1.2s"
      },
      "largest-contentful-paint": {
        "score": 0.85,
        "displayValue": "2.5s"
      }
    }
  }
}
```

---

#### Lighthouse API (via PageSpeed)

**Note**: Lighthouse is built into PageSpeed Insights API

**Features**:
- Performance
- Accessibility
- Best Practices
- SEO
- Progressive Web App (PWA)

**Use Cases for SEO Writer**:
- Comprehensive SEO audit
- Best practices check
- SEO score (0-100)

---

### 4.2 Technical SEO APIs

#### DataForSEO On-Page API

**Pricing**: Pay-as-you-go (see Part 1.1)

**Features**:
- On-page SEO analysis
- Title, meta, H1-H6 analysis
- Content analysis
- Internal/external links
- Keyword usage
- Technical issues

**Key Endpoints**:
```
POST /v3/on_page/task_post
POST /v3/on_page/summary
```

**API Documentation**: https://docs.dataforseo.com/v3/on_page_api/

**Use Cases for SEO Writer**:
- Detailed on-page SEO audit
- Technical SEO recommendations
- Content optimization

---

#### Google Search Console API

**Pricing**: **Free** (Google account required)

**Features**:
- Search performance data
- Indexing status
- Mobile usability
- Core Web Vitals
- Coverage report

**Key Endpoints**:
```
GET https://www.googleapis.com/webmasters/v3/sites/siteUrl/searchAnalytics/query
```

**API Documentation**: https://developers.google.com/webmaster-tools/search-console-api-original

**Why GSC API**:
- **Free**
- Official Google data
- Real search performance
- Core Web Vitals

**Use Cases for SEO Writer**:
- Performance tracking
- Technical SEO insights
- Mobile usability check

**Sample Request**:
```bash
curl -X GET "https://www.googleapis.com/webmasters/v3/sites/https://example.com/searchAnalytics/query" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "startDate": "2025-01-01",
    "endDate": "2025-03-01",
    "dimensions": ["query"]
  }'
```

---

### 4.3 Comparison Summary

| API | Price | Core Web Vitals | Technical SEO | Free Tier | Best For |
|-----|-------|-----------------|---------------|-----------|----------|
| **PageSpeed Insights** | Free | ✅ Yes | ✅ Limited | 25K requests/day | Performance |
| **DataForSEO On-Page** | Pay-as-you-go | ❌ No | ✅ Yes | No | Technical audit |
| **Google Search Console** | Free | ✅ Yes | ✅ Yes | Unlimited | Real data |

---

## Part 5: Content Quality APIs

### 5.1 Grammar & Readability APIs

#### Grammarly API

**Pricing**:
- **Business**: Custom pricing (contact sales)
- **Enterprise**: Custom pricing

**Features**:
- Grammar checking
- Spelling checking
- Punctuation checking
- Style suggestions
- Tone detection
- Clarity improvements

**Key Endpoints**:
```
POST /api/analyze
```

**API Documentation**: https://developer.grammarly.com/

**Why Grammarly**:
- Industry standard
- High accuracy
- Comprehensive rules

**Use Cases for SEO Writer**:
- Grammar checking
- Style improvements
- Professional quality

**Sample Request**:
```bash
curl -X POST "https://api.grammarly.com/v1/analyze" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Your text here...",
    "language": "en-US",
    "category": "general"
  }'
```

---

#### LanguageTool API

**Pricing**:
- **Free**: 20,000 characters/day
- **Premium**: $59/year (unlimited)
- **Enterprise**: Custom pricing

**Features**:
- Grammar checking
- Spelling checking
- Style suggestions
- Punctuation checking
- 25+ languages

**Key Endpoints**:
```
POST /v2/check
```

**API Documentation**: https://languagetool.org/http-api/

**Why LanguageTool**:
- Free tier available
- Open-source option
- Multi-language support

**Use Cases for SEO Writer**:
- Grammar checking (free tier)
- Style improvements
- Alternative to Grammarly

**Sample Request**:
```bash
curl -X POST "https://api.languagetoolplus.com/v2/check" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Your text here...",
    "language": "en-US"
  }'
```

---

### 5.2 Readability APIs

#### Readable API (by WebFX)

**Pricing**:
- **Free**: 5 requests/month
- **Basic**: $9/month (1,000 requests)
- **Pro**: $29/month (5,000 requests)

**Features**:
- Readability score
- Grade level
- Reading time
- Keyword density
- Sentence analysis

**Key Endpoints**:
```
POST /api/readability
```

**API Documentation**: https://www.readable.com/api/

**Use Cases for SEO Writer**:
- Readability check
- Grade level analysis
- Content optimization

---

#### Hemingway App API

**Pricing**:
- **Desktop**: $19.99 one-time
- **API**: Contact for pricing

**Features**:
- Readability score
- Grade level
- Sentence complexity
- Passive voice detection
- Adverb usage

**Note**: Hemingway API is not publicly available

**Use Cases for SEO Writer**:
- Readability improvement (via web scraping or manual analysis)

---

### 5.3 Free Alternatives

#### Built-in Readability Algorithms

**Pricing**: **Free**

**Algorithms**:
- Flesch-Kincaid Grade Level
- Flesch Reading Ease
- Gunning Fog Index
- SMOG Index
- Coleman-Liau Index

**Python Implementation**:
```python
import re
import math

def flesch_kincaid_grade(text):
    """Calculate Flesch-Kincaid Grade Level"""
    words = len(text.split())
    sentences = len(re.split(r'[.!?]+', text)) - 1
    syllables = count_syllables(text)

    return 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59

def count_syllables(word):
    """Simple syllable counter (not perfect)"""
    vowels = "aeiouy"
    syllable_count = 0
    prev_char = None

    for char in word.lower():
        if char in vowels and (not prev_char or prev_char not in vowels):
            syllable_count += 1
        prev_char = char

    if syllable_count == 0:
        syllable_count = 1

    return syllable_count
```

**Use Cases for SEO Writer**:
- Readability scoring (free)
- Grade level analysis
- Content optimization

---

### 5.4 Comparison Summary

| API | Price/Month | Grammar | Style | Readability | Free Tier | Best For |
|-----|------------|---------|-------|-------------|-----------|----------|
| **Grammarly** | Custom | ✅ Yes | ✅ Yes | ❌ No | No | Professional |
| **LanguageTool** | $59/year | ✅ Yes | ✅ Yes | ❌ No | 20K chars/day | Budget |
| **Readable** | $9 | ❌ No | ❌ No | ✅ Yes | 5 requests/month | Readability |
| **Hemingway** | N/A | ❌ No | ✅ Yes | ✅ Yes | No | Manual |
| **Built-in** | Free | ❌ No | ❌ No | ✅ Yes | Unlimited | Free fallback |

---

## Part 6: Schema Markup APIs

### 6.1 Schema Validation APIs

#### Google Structured Data Testing Tool

**Pricing**: **Free**

**Features**:
- Schema validation
- Error reporting
- Rich snippet preview
- Multiple schema types

**Key Endpoints**:
```
POST https://search.google.com/test/rich-results
```

**Note**: API access is limited, use Rich Results Test tool manually

**Use Cases for SEO Writer**:
- Schema validation
- Error detection
- Rich snippet preview

---

#### Schema.org Validator

**Pricing**: **Free**

**Features**:
- Schema validation
- Property checking
- Type validation

**URL**: https://validator.schema.org/

**Use Cases for SEO Writer**:
- Schema validation
- Property checking

---

#### Schema Markup Generator APIs

#### Merkle Schema Generator

**Pricing**: **Free** (web-based, no API)

**Features**:
- Schema markup generation
- Multiple schema types
- JSON-LD output

**URL**: https://technicalseo.com/tools/schema-markup-generator/

**Use Cases for SEO Writer**:
- Generate schema markup
- JSON-LD creation

---

### 6.2 Manual Schema Generation (RECOMMENDED)

**Why Manual Generation**:
- No API needed
- Full control
- Free
- Learn schema structure

**Schema Types for SEO Writer**:
- Article
- BlogPosting
- FAQPage
- HowTo
- Product
- BreadcrumbList
- Organization

**Python Example**:
```python
def generate_article_schema(title, author, description, image, date_published):
    """Generate Article schema markup"""
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "author": {
            "@type": "Person",
            "name": author
        },
        "datePublished": date_published,
        "dateModified": date_published,
        "description": description,
        "image": image
    }
    return schema

# Generate schema
schema = generate_article_schema(
    title="Keyword Research Guide for Beginners",
    author="Anastasia Steele",
    description="Complete keyword research tutorial for beginners...",
    image="https://example.com/image.jpg",
    date_published="2025-03-01"
)

import json
print(json.dumps(schema, indent=2))
```

**Use Cases for SEO Writer**:
- Generate schema for every piece of content
- Custom schema types
- Free and reliable

---

### 6.3 Comparison Summary

| API | Price | Validation | Generation | Free Tier | Best For |
|-----|-------|------------|------------|-----------|----------|
| **Google SDTT** | Free | ✅ Yes | ❌ No | Unlimited | Validation |
| **Schema.org** | Free | ✅ Yes | ❌ No | Unlimited | Validation |
| **Merkle** | Free | ❌ No | ✅ Yes | Unlimited | Generation |
| **Manual (Python)** | Free | ❌ No | ✅ Yes | Unlimited | Full control |

---

## Part 7: OpenClaw MCP Integration

### 7.1 Understanding MCP (Model Context Protocol)

**What is MCP?**
- Open protocol for connecting AI models to external tools
- Standardized interface for API integration
- Enables secure, structured communication
- Developed by Anthropic

**Why MCP Matters for SEO Writer**:
- Standardized API integration
- Secure credential management
- Error handling and retries
- Rate limiting support
- Consistent tool interface

**MCP Components**:
1. **MCP Client**: Runs in OpenClaw (agent side)
2. **MCP Server**: Wraps external APIs
3. **MCP Protocol**: Communication standard

---

### 7.2 OpenClaw MCP Architecture

**Current OpenClaw MCP Support**:
- Built-in MCP client support
- MCP server configuration via config files
- Environment variable support for API keys
- Tool policy control per agent

**MCP Configuration Location**:
- `/root/.openclaw/config.json` (main config)
- Agent-specific config files
- Environment variables

**MCP Server Discovery**:
- `/app/skills/` (skill-based MCPs)
- `/root/.openclaw/mcp-servers/` (custom MCPs)
- Remote MCP servers (via URL)

---

### 7.3 Adding Custom MCP Servers

**Option 1: Create Custom MCP Server**

**Step 1: Create MCP Server Directory**
```bash
mkdir -p ~/.openclaw/workspace/mcp-servers/seo-apis
cd ~/.openclaw/workspace/mcp-servers/seo-apis
```

**Step 2: Create MCP Server Script** (`server.py`)
```python
#!/usr/bin/env python3
"""
SEO APIs MCP Server
Wraps SEO APIs for OpenClaw integration
"""

import json
import os
import requests
from typing import Dict, List, Optional
from mcp.server import Server
from mcp.types import Tool, TextContent

# API Keys (from environment)
AHREFS_API_KEY = os.getenv("AHREFS_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
ORIGINALITY_API_KEY = os.getenv("ORIGINALITY_API_KEY")

# MCP Server
app = Server("seo-apis")

@app.tool()
async def keyword_research(
    keyword: str,
    country: str = "us"
) -> TextContent:
    """
    Research keyword metrics using Ahrefs API

    Args:
        keyword: The keyword to research
        country: Country code (default: us)

    Returns:
        JSON with keyword metrics (volume, difficulty, CPC)
    """
    if not AHREFS_API_KEY:
        return TextContent(
            type="text",
            text=json.dumps({"error": "AHREFS_API_KEY not configured"})
        )

    response = requests.get(
        f"https://api.ahrefs.com/v2/keywords?keyword={keyword}&limit=5",
        headers={"Authorization": f"Bearer {AHREFS_API_KEY}"}
    )

    return TextContent(
        type="text",
        text=json.dumps(response.json(), indent=2)
    )

@app.tool()
async def serp_analysis(
    query: str,
    country: str = "us",
    language: str = "en"
) -> TextContent:
    """
    Analyze SERP using Serper.dev API

    Args:
        query: Search query
        country: Country code (default: us)
        language: Language code (default: en)

    Returns:
        JSON with SERP data (organic results, PAA, featured snippets)
    """
    if not SERPER_API_KEY:
        return TextContent(
            type="text",
            text=json.dumps({"error": "SERPER_API_KEY not configured"})
        )

    response = requests.post(
        "https://google.serper.dev/search",
        headers={
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "q": query,
            "gl": country,
            "hl": language
        }
    )

    return TextContent(
        type="text",
        text=json.dumps(response.json(), indent=2)
    )

@app.tool()
async def ai_content_detection(
    content: str,
    title: str = ""
) -> TextContent:
    """
    Detect AI-generated content using Originality.ai

    Args:
        content: The text content to analyze
        title: Optional title for the content

    Returns:
        JSON with AI detection score
    """
    if not ORIGINALITY_API_KEY:
        return TextContent(
            type="text",
            text=json.dumps({"error": "ORIGINALITY_API_KEY not configured"})
        )

    response = requests.post(
        "https://api.originality.ai/api/v1/scan/ai",
        headers={
            "X-OAI-API-KEY": ORIGINALITY_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "content": content,
            "title": title
        }
    )

    return TextContent(
        type="text",
        text=json.dumps(response.json(), indent=2)
    )

# Run MCP server
if __name__ == "__main__":
    app.run()
```

**Step 3: Create MCP Configuration** (`mcp.json`)
```json
{
  "name": "seo-apis",
  "version": "1.0.0",
  "description": "SEO APIs MCP server for keyword research, SERP analysis, and AI detection",
  "main": "server.py",
  "tools": [
    {
      "name": "keyword_research",
      "description": "Research keyword metrics using Ahrefs API",
      "inputSchema": {
        "type": "object",
        "properties": {
          "keyword": {
            "type": "string",
            "description": "The keyword to research"
          },
          "country": {
            "type": "string",
            "description": "Country code (default: us)"
          }
        },
        "required": ["keyword"]
      }
    },
    {
      "name": "serp_analysis",
      "description": "Analyze SERP using Serper.dev API",
      "inputSchema": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "Search query"
          },
          "country": {
            "type": "string",
            "description": "Country code (default: us)"
          },
          "language": {
            "type": "string",
            "description": "Language code (default: en)"
          }
        },
        "required": ["query"]
      }
    },
    {
      "name": "ai_content_detection",
      "description": "Detect AI-generated content using Originality.ai",
      "inputSchema": {
        "type": "object",
        "properties": {
          "content": {
            "type": "string",
            "description": "The text content to analyze"
          },
          "title": {
            "type": "string",
            "description": "Optional title for the content"
          }
        },
        "required": ["content"]
      }
    }
  ],
  "env": [
    "AHREFS_API_KEY",
    "SERPER_API_KEY",
    "ORIGINALITY_API_KEY"
  ]
}
```

**Step 4: Register MCP Server with OpenClaw**
```bash
# Add to OpenClaw config
openclaw config set mcp.servers.seo-apis.path ~/.openclaw/workspace/mcp-servers/seo-apis

# Set API keys
openclaw config set mcp.servers.seo-apis.env.AHREFS_API_KEY "your_ahrefs_key"
openclaw config set mcp.servers.seo-apis.env.SERPER_API_KEY "your_serper_key"
openclaw config set mcp.servers.seo-apis.env.ORIGINALITY_API_KEY "your_originality_key"
```

**Step 5: Use MCP Tools in Agent**
```python
# In agent code, MCP tools are available via `call_tool`
result = await call_tool("keyword_research", {
    "keyword": "keyword research",
    "country": "us"
})
```

---

**Option 2: Use OpenClaw Built-in Tools**

**For Simple API Calls**:
- Use `exec` tool with `curl`
- Parse JSON output with Python
- No MCP server needed

**Example**:
```bash
# In agent
curl -s "https://google.serper.dev/search" \
  -H "X-API-KEY: $SERPER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "keyword research"}' | \
  python3 -m json.tool
```

---

**Option 3: Create Python Scripts (Recommended for MVP)**

**Why Python Scripts**:
- No MCP server complexity
- Full control over API calls
- Easy to debug
- Can be used with `exec` tool

**Example Script** (`~/.openclaw/workspace/tools/seo-keyword-research.py`):
```python
#!/usr/bin/env python3
"""
Keyword Research Tool
Uses Ahrefs API for keyword research
"""

import json
import os
import sys
import requests

def keyword_research(keyword: str, country: str = "us") -> dict:
    """Research keyword using Ahrefs API"""
    api_key = os.getenv("AHREFS_API_KEY")

    if not api_key:
        return {"error": "AHREFS_API_KEY not set"}

    response = requests.get(
        f"https://api.ahrefs.com/v2/keywords?keyword={keyword}&limit=5",
        headers={"Authorization": f"Bearer {api_key}"}
    )

    return response.json()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: seo-keyword-research.py <keyword> [country]")
        sys.exit(1)

    keyword = sys.argv[1]
    country = sys.argv[2] if len(sys.argv) > 2 else "us"

    result = keyword_research(keyword, country)
    print(json.dumps(result, indent=2))
```

**Usage**:
```bash
export AHREFS_API_KEY="your_key"
python3 ~/.openclaw/workspace/tools/seo-keyword-research.py "keyword research" us
```

---

### 7.4 API Key Management

**Best Practices**:
1. **Never hardcode API keys** in code
2. **Use environment variables**
3. **Store in OpenClaw config** (encrypted)
4. **Rotate keys regularly**
5. **Use separate keys** for dev/prod

**OpenClaw Configuration**:
```bash
# Set API key in config
openclaw config set secrets.AHREFS_API_KEY "your_key"

# Access in agent
import os
api_key = os.getenv("AHREFS_API_KEY")
```

**Environment Variables File** (`.env.seo-apis`):
```bash
AHREFS_API_KEY=your_ahrefs_key
SERPER_API_KEY=your_serper_key
ORIGINALITY_API_KEY=your_originality_key
```

**Load in Agent**:
```python
from dotenv import load_dotenv

load_dotenv("~/.openclaw/workspace/.env.seo-apis")

ahrefs_key = os.getenv("AHREFS_API_KEY")
```

---

### 7.5 Rate Limiting and Error Handling

**Rate Limiting Strategy**:
```python
import time
from typing import Dict, Optional
import requests

class RateLimitedAPI:
    def __init__(self, requests_per_minute: int = 60):
        self.requests_per_minute = requests_per_minute
        self.request_times = []

    def request(self, method: str, url: str, **kwargs) -> Optional[Dict]:
        """Make rate-limited API request"""
        # Rate limiting
        now = time.time()
        self.request_times = [t for t in self.request_times if now - t < 60]

        if len(self.request_times) >= self.requests_per_minute:
            sleep_time = 60 - (now - self.request_times[0])
            time.sleep(sleep_time)

        # Make request
        try:
            response = requests.request(method, url, **kwargs)
            self.request_times.append(time.time())

            if response.status_code == 429:
                # Rate limit hit, wait and retry
                retry_after = int(response.headers.get("Retry-After", 60))
                time.sleep(retry_after)
                return self.request(method, url, **kwargs)

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"API error: {e}")
            return None
```

**Error Handling Pattern**:
```python
def api_call_with_retry(
    func,
    max_retries: int = 3,
    backoff: float = 2.0
):
    """Call API function with exponential backoff"""
    for attempt in range(max_retries):
        try:
            result = func()
            return result
        except Exception as e:
            if attempt == max_retries - 1:
                raise

            wait_time = backoff ** (attempt + 1)
            print(f"Attempt {attempt + 1} failed, retrying in {wait_time}s...")
            time.sleep(wait_time)

    return None
```

---

### 7.6 Caching Strategy

**Why Cache?**
- Reduce API costs
- Faster responses
- Respect rate limits
- Reduce load on external APIs

**Caching Implementation**:
```python
import json
import hashlib
import time
from pathlib import Path
from typing import Optional

class APICache:
    def __init__(self, cache_dir: str = "/tmp/seo-api-cache", ttl: int = 3600):
        self.cache_dir = Path(cache_dir)
        self.ttl = ttl  # Time-to-live in seconds (1 hour default)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_key(self, url: str, params: dict) -> str:
        """Generate cache key from URL and params"""
        key = f"{url}?{json.dumps(params, sort_keys=True)}"
        return hashlib.md5(key.encode()).hexdigest()

    def get(self, url: str, params: dict) -> Optional[dict]:
        """Get cached response if valid"""
        cache_key = self._get_cache_key(url, params)
        cache_file = self.cache_dir / f"{cache_key}.json"

        if not cache_file.exists():
            return None

        with open(cache_file) as f:
            cached = json.load(f)

        # Check TTL
        if time.time() - cached["timestamp"] > self.ttl:
            cache_file.unlink()
            return None

        return cached["data"]

    def set(self, url: str, params: dict, data: dict):
        """Cache response"""
        cache_key = self._get_cache_key(url, params)
        cache_file = self.cache_dir / f"{cache_key}.json"

        with open(cache_file, "w") as f:
            json.dump({
                "timestamp": time.time(),
                "data": data
            }, f)

# Usage
cache = APICache(ttl=3600)  # 1 hour cache

def cached_api_call(url: str, params: dict):
    """API call with caching"""
    # Check cache
    cached = cache.get(url, params)
    if cached:
        print("Cache hit!")
        return cached

    # Make API call
    response = requests.get(url, params=params)
    data = response.json()

    # Cache result
    cache.set(url, params, data)

    return data
```

**Cache TTL Recommendations**:
- Keyword research: **24 hours** (search volume doesn't change often)
- SERP analysis: **1 hour** (results can change)
- AI detection: **Never** (content is unique)
- Technical SEO: **1 hour** (PageSpeed scores)

---

### 7.7 OpenClaw Built-in Tools for SEO

**SearXNG (Self-Hosted)**:
- URL: http://89.167.66.83:8888
- Usage: `web_search` with SearXNG backend
- Free, unlimited queries
- Good for MVP keyword research

**web_fetch Tool**:
- Extract content from URLs
- Use for competitor analysis
- Free, rate limited by remote server
- Good for scraping specific articles

**Python with `exec` Tool**:
- Full Python scripting
- API calls via `requests` library
- Complete control
- Use for complex API integrations

---

### 7.8 Integration Examples

**Example 1: Keyword Research with Ahrefs API**
```python
#!/usr/bin/env python3
"""
Keyword Research Integration
Uses Ahrefs API for keyword metrics
"""

import os
import requests

def get_keyword_metrics(keyword: str) -> dict:
    """Get keyword metrics from Ahrefs"""
    api_key = os.getenv("AHREFS_API_KEY")

    response = requests.get(
        "https://api.ahrefs.com/v2/keywords",
        params={"keyword": keyword, "limit": 5},
        headers={"Authorization": f"Bearer {api_key}"}
    )

    return response.json()

# In SEO Writer agent
metrics = get_keyword_metrics("keyword research")
volume = metrics.get("volume", 0)
difficulty = metrics.get("kd", 0)
cpc = metrics.get("cpc", 0)

print(f"Volume: {volume}, Difficulty: {difficulty}, CPC: ${cpc}")
```

**Example 2: SERP Analysis with Serper.dev**
```python
#!/usr/bin/env python3
"""
SERP Analysis Integration
Uses Serper.dev for SERP data
"""

import os
import requests

def analyze_serp(query: str) -> dict:
    """Analyze SERP for query"""
    api_key = os.getenv("SERPER_API_KEY")

    response = requests.post(
        "https://google.serper.dev/search",
        headers={
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        },
        json={"q": query, "gl": "us", "hl": "en"}
    )

    return response.json()

# Extract PAA questions
serp = analyze_serp("keyword research")
paa_questions = serp.get("peopleAlsoAsk", [])

for question in paa_questions:
    print(f"Q: {question['question']}")
    print(f"A: {question['snippet'][:100]}...")
    print()
```

**Example 3: AI Content Detection with Originality.ai**
```python
#!/usr/bin/env python3
"""
AI Content Detection Integration
Uses Originality.ai for AI detection
"""

import os
import requests

def detect_ai_content(content: str, title: str = "") -> dict:
    """Detect AI-generated content"""
    api_key = os.getenv("ORIGINALITY_API_KEY")

    response = requests.post(
        "https://api.originality.ai/api/v1/scan/ai",
        headers={
            "X-OAI-API-KEY": api_key,
            "Content-Type": "application/json"
        },
        json={
            "content": content,
            "title": title
        }
    )

    return response.json()

# In SEO Writer agent
ai_score = detect_ai_content(content, title)

if ai_score.get("ai", False):
    print("⚠️ Content detected as AI-generated")
    print(f"AI Score: {ai_score['score']['ai']}%")
else:
    print("✅ Content appears human-written")
    print(f"Human Score: {ai_score['score']['original']}%")
```

---

## Part 8: Recommendations & Phasing

### 8.1 MVP (Minimum Viable Product)

**Goal**: Launch SEO Writer with basic functionality at low cost

**Required APIs**:
1. **Keyword Research**: SearXNG (free)
2. **SERP Analysis**: Serper.dev Starter ($5/month) or SearXNG (free)
3. **SEO Checking**: PageSpeed Insights API (free)
4. **Content Quality**: Built-in grammar checking + readability algorithms (free)
5. **Schema Markup**: Manual generation (free)

**Total Monthly Cost**: **$0-5**

**What You Get**:
- Basic keyword research (via SearXNG autocomplete)
- SERP analysis (via Serper.dev or SearXNG)
- Technical SEO recommendations (via PageSpeed Insights)
- Readability scoring (via built-in algorithms)
- Schema markup generation (via Python scripts)

**Limitations**:
- No exact search volume data
- No keyword difficulty scores
- No AI content detection
- Manual SERP feature extraction

**When to Upgrade**:
- When you need accurate metrics (volume, difficulty)
- When you want AI content detection
- When you need competitor analysis at scale

---

### 8.2 Phase 2 (Growth)

**Goal**: Add professional-grade SEO data and quality assurance

**Add These APIs**:
1. **Keyword Research**: Ubersuggest API ($29/month)
2. **SERP Analysis**: SERPAPI Starter ($50/month)
3. **AI Content Detection**: Originality.ai ($30/month)
4. **Content Quality**: LanguageTool ($59/year = ~$5/month)

**Total Monthly Cost**: **$119/month**

**What You Add**:
- Accurate search volume and difficulty
- Structured SERP data with features
- AI content detection
- Professional grammar checking
- Related keyword suggestions

**When to Upgrade**:
- When you need enterprise-grade data
- When you want Ahrefs/SEMrush integration
- When you need historical data

---

### 8.3 Phase 3 (Enterprise)

**Goal**: Full suite of enterprise SEO APIs

**Add These APIs**:
1. **Keyword Research**: Ahrefs API ($399/month) or SEMrush ($499/month)
2. **SERP Analysis**: SERPAPI Business ($500/month)
3. **AI Content Detection**: Originality.ai Pro ($200/month)
4. **Content Quality**: Grammarly Business (custom pricing, ~$100/month)
5. **Technical SEO**: DataForSEO On-Page (pay-as-you-go, ~$50/month)

**Total Monthly Cost**: **$1,249/month**

**What You Add**:
- Largest keyword database (Ahrefs: 12B+ keywords)
- Historical keyword data (6 years)
- Competitor backlink analysis
- Enterprise-grade AI detection
- Professional grammar checking
- Comprehensive on-page SEO audit

---

### 8.4 Implementation Priority

**High Priority (Must Have)**:
1. ✅ SearXNG for keyword research (free, already configured)
2. ✅ Serper.dev for SERP analysis ($5/month)
3. ✅ PageSpeed Insights API (free)
4. ✅ Schema markup generation (free, manual)

**Medium Priority (Should Have)**:
5. Ubersuggest API for keyword metrics ($29/month)
6. Originality.ai for AI detection ($30/month)
7. LanguageTool for grammar checking ($5/month)

**Low Priority (Nice to Have)**:
8. Ahrefs API for enterprise data ($399/month)
9. SEMrush API for comprehensive SEO ($499/month)
10. Grammarly Business for professional editing (~$100/month)

---

### 8.5 Cost vs Value Analysis

| Feature | Free Option | Low-Cost | Enterprise | Value |
|---------|-------------|----------|------------|-------|
| Keyword Research | SearXNG | Ubersuggest ($29) | Ahrefs ($399) | High |
| SERP Analysis | SearXNG | Serper.dev ($5) | SERPAPI ($500) | High |
| AI Detection | None | Originality.ai ($30) | Originality.ai Pro ($200) | Medium |
| Grammar Check | Built-in | LanguageTool ($5) | Grammarly ($100) | Low |
| Technical SEO | PageSpeed (free) | PageSpeed (free) | DataForSEO ($50) | High |

**Recommendation**:
- Start with free/low-cost options
- Upgrade as revenue scales
- Focus on keyword research and SERP analysis first
- AI detection is nice-to-have for quality assurance

---

## Appendix: API Code Examples

### A.1 Keyword Research with Ahrefs API

```python
import os
import requests

def keyword_research_ahrefs(keyword: str, country: str = "us") -> dict:
    """Research keyword using Ahrefs API"""
    api_key = os.getenv("AHREFS_API_KEY")

    if not api_key:
        return {"error": "AHREFS_API_KEY not set"}

    response = requests.get(
        "https://api.ahrefs.com/v2/keywords",
        params={"keyword": keyword, "limit": 5},
        headers={"Authorization": f"Bearer {api_key}"}
    )

    response.raise_for_status()
    return response.json()

# Usage
result = keyword_research_ahrefs("keyword research")
print(result)
```

### A.2 SERP Analysis with Serper.dev

```python
import os
import requests

def serp_analysis_serper(query: str, country: str = "us", language: str = "en") -> dict:
    """Analyze SERP using Serper.dev API"""
    api_key = os.getenv("SERPER_API_KEY")

    if not api_key:
        return {"error": "SERPER_API_KEY not set"}

    response = requests.post(
        "https://google.serper.dev/search",
        headers={
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        },
        json={"q": query, "gl": country, "hl": language}
    )

    response.raise_for_status()
    return response.json()

# Extract PAA questions
def extract_paa_questions(serp_data: dict) -> list:
    """Extract People Also Ask questions from SERP data"""
    return serp_data.get("peopleAlsoAsk", [])

# Usage
serp = serp_analysis_serper("keyword research")
paa = extract_paa_questions(serp)

for question in paa[:5]:
    print(f"Q: {question['question']}")
```

### A.3 AI Content Detection with Originality.ai

```python
import os
import requests

def detect_ai_originality(content: str, title: str = "") -> dict:
    """Detect AI-generated content using Originality.ai"""
    api_key = os.getenv("ORIGINALITY_API_KEY")

    if not api_key:
        return {"error": "ORIGINALITY_API_KEY not set"}

    response = requests.post(
        "https://api.originality.ai/api/v1/scan/ai",
        headers={
            "X-OAI-API-KEY": api_key,
            "Content-Type": "application/json"
        },
        json={"content": content, "title": title}
    )

    response.raise_for_status()
    return response.json()

# Usage
content = """
Keyword research is the process of finding and analyzing search terms...
"""

result = detect_ai_originality(content, "Keyword Research Guide")

if result.get("ai", False):
    print(f"⚠️ AI detected: {result['score']['ai']}%")
else:
    print(f"✅ Human-written: {result['score']['original']}%")
```

### A.4 PageSpeed Insights API

```python
import requests

def pagespeed_insights(url: str, strategy: str = "mobile") -> dict:
    """Get PageSpeed Insights data"""
    api_key = os.getenv("PAGESPEED_API_KEY")  # Optional

    params = {"url": url, "strategy": strategy}
    if api_key:
        params["key"] = api_key

    response = requests.get(
        "https://www.googleapis.com/pagespeedonline/v5/runPagespeed",
        params=params
    )

    response.raise_for_status()
    return response.json()

# Extract Core Web Vitals
def extract_core_web_vitals(psi_data: dict) -> dict:
    """Extract Core Web Vitals from PSI data"""
    lighthouse = psi_data["lighthouseResult"]
    audits = lighthouse["audits"]

    return {
        "lcp": {
            "score": audits["largest-contentful-paint"]["score"],
            "value": audits["largest-contentful-paint"]["displayValue"]
        },
        "fid": {
            "score": audits.get("max-potential-fid", {}).get("score"),
            "value": audits.get("max-potential-fid", {}).get("displayValue")
        },
        "cls": {
            "score": audits["cumulative-layout-shift"]["score"],
            "value": audits["cumulative-layout-shift"]["displayValue"]
        },
        "performance_score": lighthouse["categories"]["performance"]["score"]
    }

# Usage
psi = pagespeed_insights("https://example.com", "mobile")
cwv = extract_core_web_vitals(psi)

print(f"LCP: {cwv['lcp']['value']}")
print(f"FID: {cwv['fid']['value']}")
print(f"CLS: {cwv['cls']['value']}")
print(f"Performance Score: {cwv['performance_score'] * 100:.0f}/100")
```

### A.5 Schema Markup Generation

```python
import json
from datetime import datetime

def generate_article_schema(
    title: str,
    author: str,
    description: str,
    image: str,
    url: str,
    publisher_name: str,
    publisher_logo: str
) -> dict:
    """Generate Article schema markup"""

    date_published = datetime.now().strftime("%Y-%m-%d")

    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "author": {
            "@type": "Person",
            "name": author
        },
        "datePublished": date_published,
        "dateModified": date_published,
        "description": description,
        "image": image,
        "url": url,
        "publisher": {
            "@type": "Organization",
            "name": publisher_name,
            "logo": {
                "@type": "ImageObject",
                "url": publisher_logo
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": url
        }
    }

    return schema

def generate_faq_schema(questions: list) -> dict:
    """Generate FAQPage schema markup"""

    faq_items = []
    for q in questions:
        faq_items.append({
            "@type": "Question",
            "name": q["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": q["answer"]
            }
        })

    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_items
    }

    return schema

# Usage
article_schema = generate_article_schema(
    title="Keyword Research Guide for Beginners",
    author="Anastasia Steele",
    description="Complete keyword research tutorial for beginners...",
    image="https://example.com/image.jpg",
    url="https://example.com/keyword-research",
    publisher_name="SEO Pro",
    publisher_logo="https://example.com/logo.png"
)

print(json.dumps(article_schema, indent=2))

faq_schema = generate_faq_schema([
    {"question": "What is keyword research?", "answer": "Keyword research is the process..."},
    {"question": "How long does keyword research take?", "answer": "Keyword research takes 2-4 hours..."}
])

print(json.dumps(faq_schema, indent=2))
```

### A.6 Readability Scoring

```python
import re
import math

class ReadabilityScorer:
    """Calculate readability scores"""

    @staticmethod
    def count_syllables(word: str) -> int:
        """Count syllables in a word (heuristic)"""
        word = word.lower()
        word = re.sub(r'[^a-z]', '', word)

        if len(word) <= 3:
            return 1

        word = re.sub(r'(?:[^laeiouy]es|ed|[^laeiouy]e)$', '', word)
        word = re.sub(r'^y', '', word)
        matches = re.findall(r'[aeiouy]{1,2}', word)

        return len(matches) if matches else 1

    @staticmethod
    def flesch_reading_ease(text: str) -> float:
        """Calculate Flesch Reading Ease score"""
        sentences = len(re.split(r'[.!?]+', text))
        words = len(text.split())
        syllables = sum(ReadabilityScorer.count_syllables(w) for w in text.split())

        if sentences == 0 or words == 0:
            return 0

        return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

    @staticmethod
    def flesch_kincaid_grade(text: str) -> float:
        """Calculate Flesch-Kincaid Grade Level"""
        sentences = len(re.split(r'[.!?]+', text))
        words = len(text.split())
        syllables = sum(ReadabilityScorer.count_syllables(w) for w in text.split())

        if sentences == 0 or words == 0:
            return 0

        return 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59

    @staticmethod
    def gunning_fog(text: str) -> float:
        """Calculate Gunning Fog Index"""
        sentences = len(re.split(r'[.!?]+', text))
        words = len(text.split())
        complex_words = sum(1 for w in text.split() if ReadabilityScorer.count_syllables(w) >= 3)

        if sentences == 0 or words == 0:
            return 0

        return 0.4 * ((words / sentences) + (100 * complex_words / words))

    @staticmethod
    def analyze(text: str) -> dict:
        """Analyze text readability"""
        return {
            "flesch_reading_ease": ReadabilityScorer.flesch_reading_ease(text),
            "flesch_kincaid_grade": ReadabilityScorer.flesch_kincaid_grade(text),
            "gunning_fog": ReadabilityScorer.gunning_fog(text),
            "word_count": len(text.split()),
            "sentence_count": len(re.split(r'[.!?]+', text))
        }

# Usage
text = """
Keyword research is the process of finding and analyzing search terms that people enter into search engines.
It helps you understand what your audience is looking for and how to create content that meets their needs.
"""

scores = ReadabilityScorer.analyze(text)

print(f"Flesch Reading Ease: {scores['flesch_reading_ease']:.1f}")
print(f"Flesch-Kincaid Grade: {scores['flesch_kincaid_grade']:.1f}")
print(f"Gunning Fog: {scores['gunning_fog']:.1f}")
print(f"Word Count: {scores['word_count']}")
print(f"Sentence Count: {scores['sentence_count']}")
```

---

## Conclusion

This document provides comprehensive research on SEO APIs and MCP integration for the SEO Writer Agent. Key takeaways:

1. **Start with free/low-cost options** (SearXNG, Serper.dev)
2. **Upgrade to paid APIs** as revenue scales
3. **Use OpenClaw built-in tools** where possible (exec, web_search, web_fetch)
4. **Implement caching** to reduce API costs
5. **Handle errors and rate limits** gracefully
6. **Manual schema generation** is free and reliable

**Recommended MVP Setup**:
- Keyword Research: SearXNG (free)
- SERP Analysis: Serper.dev Starter ($5/month)
- Technical SEO: PageSpeed Insights (free)
- Content Quality: Built-in algorithms (free)
- Schema Markup: Manual generation (free)

**Total Cost: $0-5/month**

This setup provides all essential functionality for a production-ready SEO Writer Agent while keeping costs low. Upgrade to enterprise APIs (Ahrefs, SEMrush) when revenue justifies the investment.

---

*Document compiled by Anastasia Steele for the SEO Writer Agent project*
*Date: March 2026*
