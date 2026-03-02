# TODO - Tasks for Anastasia & Mr. Grey

---

## 📋 General Todos

| Priority | Task | Added | Notes |
|----------|------|-------|-------|
| High | Give Anastasia Vercel access | 2026-02-25 | Setup Vercel project access |
| Medium | Set up coordinator pattern for Anastasia | 2026-02-25 | Have Anastasia use subagents for complex tasks |

---

## 💡 Ideas to Consider

### Coordinator Pattern
Instead of doing everything directly, Anastasia could spawn subagents for:
- **Complex coding tasks** — Build features, refactor code
- **PR reviews** — Analyze code, provide feedback
- **Background research** — Independent investigation without blocking main session
- **Parallel work** — Multiple subtasks simultaneously

**Benefits:**
- Anastasia stays responsive for direct questions
- Complex work happens in isolated contexts
- Different models/thinking levels per subagent
- Work continues even if session resets (use cron for persistence)

**Current note:** Anastasia already has access to `sessions_spawn` and can create subagents. The coordinator pattern is about *when* and *how* to use them effectively.

---

## 🔍 Reddit Search Setup

| Priority | Task | Added | Notes |
|----------|------|-------|-------|
| High | Set up reddit-cli for Reddit searching | 2026-02-28 | Reddit API now requires auth; need Python venv or alternative |

**Reddit Tools:**
- **reddit-cli** (`gupsammy/reddit-cli`) - Fast, CLI-based Reddit search via PRAW
- **reddl** (`spavaonica/reddl`) - Shell script for browsing subreddits (image-focused)
- ~~readpi~~ - Paid tool, skip

**Current Issue:**
- reddit-cli installation blocked: Python venv requires `python3.11-venv` (needs sudo)
- Reddit's public JSON API now requires authentication
- Need alternative approach or user to set up credentials

**BLOCKED (2026-02-28): Reddit API Crackdown**
- **NEW:** Reddit has silently disabled new developer apps with "Integrations on hold" status
- **API access now requires pre-approval** for ALL apps (including personal projects)
- No new API keys can be created - existing apps may still work
- Reddit helpdesk (reddit.zendesk.com) is also behind Cloudflare
- **Unknown workaround:** Cannot create new OAuth credentials

**Situation (Feb 2025 onward):**
- Self-serve API access has been discontinued
- Manual approval required for all new apps
- Personal projects and bots need to go through approval process
- Existing legacy apps may continue working, but new ones are blocked

**Status:** Reddit search is effectively blocked until Reddit opens API access or we find an alternative method.

**Alternative Found (2026-02-28):**
- **reddit-rss-api.deno.dev** - Free API that fetches Reddit data from RSS feeds
  - No authentication required
  - Returns structured JSON
  - Supports multiple subreddits, filtering, sorting
  - **Limitation:** No score/comment counts (RSS feeds don't include engagement data)
  - **Usage:** `https://reddit-rss-api.deno.dev/r/{subreddits}?count=10`
  - Works for fetching posts, but can't see upvotes or replies

**POTENTIAL SOLUTION (2026-02-28): OpenAI web_search + Reddit JSON Enrichment**
- **Skill:** `search-reddit` by arkaydeus on OpenClaw skills repository
  - https://github.com/openclaw/skills/tree/main/skills/arkaydeus/search-reddit
  - Uses OpenAI's `/v1/responses` API with `web_search` tool
  - AI searches Reddit directly (no Reddit API key needed)
  - Enriches results by fetching Reddit's public JSON endpoint (`/r/sub/comments/xyz/.json`)
  - **Gets engagement data:** Score, comment count, upvote ratio, top comment excerpts
- **How it works:**
  1. Send prompt to OpenAI: "Find Reddit threads about [topic]"
  2. AI returns URLs from web_search
  3. Script fetches Reddit JSON for each post to get score, comments, date
  4. Extracts top 3 comments with scores
- **Advantages:**
  - ✅ Real-time search via OpenAI's built-in Reddit access
  - ✅ Full engagement metrics (upvotes, comments, ratios)
  - ✅ Top comment excerpts for context
  - ✅ No Reddit API keys required
- **Requirements:**
  - OpenAI API key (has costs, unlike SearXNG)
  - Still hits Reddit's public JSON endpoints (potential rate limiting)

**Options for Implementation:**
1. **Use SearXNG** - Free, no engagement data
2. **Use OpenAI web_search + Reddit JSON** - Has costs, full data
3. **Wait for Reddit API to reopen** - Official route, currently blocked

---

**Last Updated:** 2026-02-28
