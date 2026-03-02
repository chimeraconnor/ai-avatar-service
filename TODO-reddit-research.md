# Reddit Research - How OpenAI Access Works

## The OpenAI-Reddit Partnership (2024)

**What the deal includes:**
- OpenAI accesses Reddit's **Data API** (privileged access to structured data)
- Not just web search - but direct API access
- Enables OpenAI's AI to "better understand and showcase Reddit content"
- Reddit uses OpenAI's platform for AI-powered features
- OpenAI becomes a Reddit advertising partner
- Source: https://openai.com/index/openai-and-reddit-partnership/

## Why search-reddit Works When Reddit API is Blocked

The `search-reddit` skill by arkaydeus uses a clever two-step approach:

**Step 1: OpenAI web_search**
- Uses OpenAI's `/v1/responses` API with `web_search` tool
- Sends prompt: "Find Reddit threads about [topic]"
- **OpenAI searches the open web** (not using Reddit's blocked API)
- Returns URLs, titles, dates from search results
- ✅ No Reddit API key needed
- ✅ Accesses Reddit that regular users see

**Step 2: Reddit JSON Enrichment**
- For each URL returned, fetches Reddit's public JSON endpoint
- `https://www.reddit.com/r/sub/comments/xyz/.json`
- Gets: **Score, comment count, created date, top comments**
- These endpoints still work (read-only, no auth needed for public threads)

## Why This Works While Regular Methods Don't

| Method | Access Level | Why Fails/Works |
|---------|--------------|-------------------|
| **Public API** | Blocked | New apps can't be created |
| **RSS Feeds** | Limited | No engagement data |
| **PRAW** | Blocked | Can't create OAuth app |
| **OpenAI web_search** | ✅ | Partnership gives web access |
| **OpenAI Data API** | ✅ | Partnership gives direct data access |

## The Key Difference

**OpenAI has TWO types of access:**
1. **web_search tool** - Searches the open web (finds Reddit URLs)
2. **Data API access** - Direct Reddit API access via partnership

**Regular users and developers:** Neither access anymore due to Reddit's 2025 API crackdown

**OpenAI AI models:** Both types of access via the partnership

## Implementation Options for Reddit Search

| Option | Cost | Engagement Data | Notes |
|---------|-------|------------------|--------|
| **SearXNG** | Free | ❌ No | Basic search only |
| **reddit-rss-api** | Free | ❌ No | RSS limitation |
| **OpenAI web_search** | Paid | ✅ Yes | Full data, real-time |
| **PRAW (official)** | Free | ✅ Yes | Blocked - can't create apps |

**Recommendation:** Use OpenAI web_search + Reddit JSON for full-featured Reddit search with engagement metrics.

---

**Last Updated:** 2026-02-28
