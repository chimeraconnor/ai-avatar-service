# SEO Writer Agent Specification

**Complete agent design for SEO-optimized content generation**

*Version: 1.0*
*Compiled: March 2026*

---

## Agent Overview

### Purpose

The SEO Writer Agent is a specialized OpenClaw agent for generating high-quality, SEO-optimized content. It integrates keyword research, content writing, technical SEO, and E-E-A-T principles to produce search-engine-ready articles, blog posts, and website copy.

### Value Proposition

- **Single-turn solution**: Receive brief, deliver publication-ready content
- **SEO-first approach**: Every piece optimized for search intent and rankings
- **Quality assurance**: Built-in humanization and E-E-A-T checks
- **Scalable**: Can be spawned as subagent for parallel content production
- **Expert-level output**: Matches top-tier SEO agencies and content teams

### Intended Users

- Content teams and agencies
- Marketing departments
- SEO professionals
- Website owners
- Bloggers and creators

---

## Agent Responsibilities

### 1. Receive Content Brief or Topic

**Input from Main Agent**:
```
sessions_spawn({
  task: "Write a comprehensive SEO-optimized blog post about [TOPIC]

  Requirements:
  - Target audience: [AUDIENCE]
  - Primary keyword: [PRIMARY_KEYWORD]
  - Secondary keywords: [KEYWORD_1, KEYWORD_2, ...]
  - Word count: [LENGTH]
  - Content type: [blog post | product page | landing page | guide]
  - Brand: [BRAND_NAME]
  - Tone: [professional | casual | technical | friendly]
  - Include schema: [Article | BlogPosting | FAQPage | none]
  - Featured snippet target: [yes/no]

  Additional context:
  [Any research findings, competitor analysis, constraints]
",
  label: "SEO Blog Post",
  model: "anthropic/claude-sonnet-4"
})
```

**Parse Requirements**:
- Extract primary keyword
- Identify secondary keywords
- Determine content type and tone
- Understand audience and goals
- Note any specific SEO requirements

### 2. Research Keywords and Search Intent

#### Subagent: Keyword Researcher

**Spawn parameters**:
```
sessions_spawn({
  task: "Conduct keyword research for [PRIMARY_KEYWORD]

  Research scope:
  1. Identify search intent (informational/transactional/navigational/commercial)
  2. Find related LSI keywords and semantic entities
  3. Analyze SERP for featured snippet opportunities
  4. Identify People Also Ask (PAA) questions
  5. Check keyword difficulty and search volume estimates

  Output format:
  - Search intent: [type]
  - Primary keyword: [term, intent, difficulty, volume]
  - Secondary keywords: [list with metrics]
  - LSI keywords: [list]
  - Featured snippet opportunities: [questions/phrases]
  - PAA questions: [list of 5-8 questions]
  - Competitor analysis: [top 3 ranking pages summary]

  Use SearXNG for research.
  Use web_fetch for specific articles if needed.",
  label: "Keyword Research",
  model: "google-gemini/gemini-2-flash"
})
```

**Keyword Researcher Responsibilities**:
- Use SearXNG (http://89.167.66.83:8888) for web search
- Fetch specific articles for detailed analysis
- Identify search intent by examining SERP composition
- Extract PAA questions (People Also Ask)
- Analyze top 3 ranking pages for:
  - Content structure
  - Word count
  - Topics covered
  - SERP features present
  - Content freshness

**Output to SEO Writer**:
- Search intent classification
- Keyword metrics (volume, difficulty, competition)
- Semantic relationships
- SERP feature opportunities
- Content gap insights

### 3. Generate SEO-Optimized Content

#### Content Structure

**Required Sections**:

1. **Title Tag** (50-60 characters)
   - Primary keyword at beginning
   - Include brand name if space permits
   - Add benefit or year if relevant

2. **Meta Description** (150-160 characters)
   - Primary keyword naturally
   - Compelling hook
   - Call to action

3. **H1 Heading** (matches title tag closely)
   - Primary keyword included
   - Benefit promise

4. **Introduction** (150-300 words)
   - Hook reader (stat, question, bold statement)
   - Define problem or topic
   - Promise what they'll learn
   - Primary keyword mention (first 100 words)

5. **Body Sections** (H2 + H3 structure)
   - Each H2: Secondary keyword or major topic
   - Each H3: Long-tail keyword or subtopic
   - 300-500 words per H2
   - 150-300 words per H3
   - Logical flow: Beginner → Advanced

6. **Featured Snippet Targets** (2-4 sections)
   - Definition block: 40-60 words
   - Step list: 4-8 numbered items
   - Table: comparison data

7. **FAQ Section** (if PAA questions available)
   - Q&A format
   - Direct answer first (50-75 words)
   - Each question as H3

8. **Conclusion** (150-200 words)
   - Summary of key points
   - Final recommendation
   - CTA (subscribe, share, next step)
   - No new information

#### SEO Optimization Requirements

**Keyword Placement**:
- Primary keyword:
  - Title tag
  - H1
  - First 100 words
  - 2-3 mentions throughout (natural)
  - URL slug
- Secondary keywords:
  - H2/H3 headers
  - 1-2 mentions each
- Long-tail keywords:
  - FAQ questions
  - Natural occurrences

**Content Quality**:
- Word count: Meet or exceed requirement
- Sentence length: Varied (5-40 words)
- Paragraph length: 2-4 sentences
- Use bullets/numbered lists for scannability
- Include tables or comparison lists
- Add specific examples and data points

**E-E-A-T Integration**:
- **Experience**: Personal anecdotes, "I've found that...", original examples
- **Expertise**: Technical depth, accurate terminology, explain complex topics simply
- **Authoritativeness**: Cite sources, reference industry leaders, comprehensive coverage
- **Trustworthiness**: Accurate data, recent information (within 6 months for fast-moving topics), transparent about limitations

**Humanization Techniques**:
- Vary sentence structure
- Remove excessive transition words ("Furthermore," "Moreover")
- Add personal perspective and opinions
- Include specific examples with details
- Use stronger verbs, eliminate weak words
- Write conversationally for casual content
- Add humor or wit when appropriate

### 4. Review Against Quality Standards

#### Self-Assessment Checklist

Before announcing to main agent, SEO Writer must verify:

**Content Requirements**:
- [ ] Meets word count requirement
- [ ] All required keywords integrated naturally
- [ ] Primary keyword in H1, title, URL
- [ ] Secondary keywords in H2/H3 headers
- [ ] Long-tail keywords addressed
- [ ] No keyword stuffing

**Structure Requirements**:
- [ ] Clear H1-H3 hierarchy
- [ ] Logical flow (intro → body → FAQ → conclusion)
- [ ] Paragraphs 2-4 sentences
- [ ] Bullet points for scannability
- [ ] At least one table or list for featured snippets
- [ ] FAQ section included (if PAA questions available)

**SEO Elements**:
- [ ] Title tag optimized (50-60 chars)
- [ ] Meta description optimized (150-160 chars)
- [ ] URL slug contains primary keyword
- [ ] Alt text descriptions for all images
- [ ] Internal links suggested (3-5)
- [ ] External links to authoritative sources
- [ ] Featured snippet optimization present

**E-E-A-T Requirements**:
- [ ] Personal experience/anecdotes included
- [ ] Expert perspective demonstrated
- [ ] Claims supported by data/research
- [ ] Citations provided for statistics
- [ ] Author perspective clear

**Technical SEO**:
- [ ] Schema markup generated (Article, BlogPosting)
- [ ] FAQ schema if FAQ section exists
- [ ] Breadcrumb schema if applicable
- [ ] Core Web Vitals considered (image optimization notes)
- [ ] Mobile-first writing (short paragraphs)

**Originality Requirements**:
- [ ] Unique insights included
- [ ] Not generic AI content
- [ ] Humanized tone and style
- [ ] Specific examples, not abstractions
- [ ] No duplicate content

#### Quality Standards

**Minimum Acceptable Quality**:
- All content requirements met
- Basic SEO optimization present
- Readable and coherent
- No grammatical errors

**Good Quality**:
- All SEO requirements met
- Strong E-E-A-T signals
- Humanized content
- Featured snippet optimization

**Excellent Quality**:
- Exceeds word count by 10-20%
- Multiple featured snippet targets
- Strong personal perspective and examples
- Comprehensive coverage of topic
- Schema markup for all applicable types
- Internal linking strategy clear

### 5. Provide Meta Tags, Schema Markup, Internal Linking Suggestions

#### Meta Tags Output

**Title Tag**:
```
Title: "Keyword Research Guide for Beginners 2025 | [Brand]"
Length: 54 characters
Contains: Primary keyword + year + brand
```

**Meta Description**:
```
Description: "Learn keyword research from scratch. Our beginner-friendly guide covers free tools, strategies, and tips to rank higher in 2025. Start now."
Length: 158 characters
Contains: Primary keyword + benefit + CTA
```

#### Schema Markup Output

**Article Schema** (for all content):
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Keyword Research Guide for Beginners 2025",
  "author": {
    "@type": "Person",
    "name": "[Brand Name]"
  },
  "datePublished": "2025-03-01",
  "dateModified": "2025-03-01",
  "description": "Complete keyword research tutorial for beginners...",
  "image": "https://[brand-site]/featured-image.jpg"
}
```

**BlogPosting Schema** (for blogs):
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "How to Do Keyword Research",
  "author": {
    "@type": "Person",
    "name": "[Brand Name]"
  },
  "datePublished": "2025-03-01",
  "description": "Learn keyword research with free tools..."
}
```

**FAQPage Schema** (if FAQ section):
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is keyword research?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keyword research is the process of finding and analyzing search terms..."
      }
    },
    {
      "@type": "Question",
      "name": "How long does keyword research take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keyword research typically takes 2-4 hours for beginners..."
      }
    }
  ]
}
```

**Breadcrumb Schema** (for hierarchical content):
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://[brand-site]/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "SEO Guides",
      "item": "https://[brand-site]/guides/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Keyword Research",
      "item": "https://[brand-site]/guides/keyword-research/"
    }
  ]
}
```

#### Internal Linking Suggestions

**Strategy**:
- 3-5 internal links per 1,000 words
- Mix of pillar content and related articles
- Descriptive anchor text (not "click here")
- Link to both newer and older content

**Output Format**:
```
Internal Link Suggestions:
1. Link to: "Complete SEO Guide 2025"
   Anchor text: "comprehensive SEO strategy"
   Context: Mentioned in Introduction
   Reason: Establishes topic authority

2. Link to: "Free Keyword Research Tools"
   Anchor text: "free keyword research tools"
   Context: Mentioned in "Keyword Research Tools" section
   Reason: Supports secondary keyword

3. Link to: "Long-Tail Keyword Guide"
   Anchor text: "long-tail keywords"
   Context: Mentioned in "Advanced Techniques" section
   Reason: Cross-topic relevance

4. Link to: "SEO Checklist for Bloggers"
   Anchor text: "SEO checklist"
   Context: Conclusion CTA
   Reason: Next step for user
```

### 6. Deliver Formatted Content Ready for Publication

#### Final Output Structure

```
=== SEO CONTENT DELIVERY ===

1. TITLE & META
---
Title Tag: [optimized title]
Meta Description: [optimized description]
URL Slug: [primary-keyword]
---

2. CONTENT (HTML-ready)
---
[H1] Keyword Research Guide for Beginners 2025

[introduction content]

[H2] What is Keyword Research?

[content with keywords integrated naturally]

[H3] Why is Keyword Research Important?

[content]

[H2] How to Do Keyword Research

[H3] Step 1: Identify Seed Keywords

[step-by-step content with numbered list]

[H3] Step 2: Use Keyword Research Tools

[content with tool recommendations]

[H2] Featured Snippet: What Are Long-Tail Keywords?

[Definition: 40-60 words]

Long-tail keywords are highly specific search queries...

[H2] Featured Snippet: How to Find Long-Tail Keywords

[Numbered list: 4-8 steps]

1. Use Google Autocomplete
2. Analyze People Also Ask questions
3. Try AnswerThePublic
4. Check competitor rankings

[H2] FAQ: Common Questions About Keyword Research

[H3] What is the best free keyword research tool?

[Direct answer: 50-75 words]

The best free keyword research tool is Ubersuggest, which offers...
It provides search volume, difficulty scores, and related keywords.

[H3] How long does keyword research take?

[Direct answer]

[H2] Conclusion

[summary, recommendation, CTA]

---

3. SCHEMA MARKUP
---
[JSON-LD schema blocks]

---

4. INTERNAL LINK SUGGESTIONS
---
[List of 3-5 internal link recommendations]

---

5. SEO QUALITY CHECK
---
[ ] All content requirements met
[ ] All SEO elements optimized
[ ] E-E-A-T signals present
[ ] Humanized content
[ ] Schema markup generated
[ ] Featured snippet targets included
[ ] Word count: [actual] / [required]
[ ] Primary keyword density: [count]
[ ] Secondary keywords integrated: [count]

---

6. NOTES
---
[Any issues, recommendations, or context]
[What was done well]
[What could be improved in future revisions]
```

#### File Delivery

**Save to file**:
```
write({
  path: "/home/node/.openclaw/workspace/projects/seo/deliverables/[slug]-content.md",
  content: [complete formatted content above]
})
```

**Filename convention**:
- Lowercase, hyphenated
- Include primary keyword
- Example: `keyword-research-guide-content.md`
- Example: `seo-tips-2025-content.md`

---

## Agent Configuration

### Runtime Preference

**Preferred Runtime**: `subagent`

**Why**:
- Isolated session for consistent behavior
- Announce back to main agent
- Can be spawned for parallel content production
- Tool policy control (no session tools for security)

**ACP Runtime**: Not recommended
- SEO writer doesn't need IDE integration
- `subagent` runtime is sufficient

### Model Selection

**Main Agent (Requester)**:
- Model: `anthropic/claude-sonnet-4` or `google-gemini/gemini-2-flash`
- Purpose: Understand content brief, coordinate subagents

**SEO Writer Subagent**:
- Model: `anthropic/claude-sonnet-4` or `google-gemini/gemini-2-flash`
- Purpose: Generate quality content with reasoning

**Keyword Researcher Subagent**:
- Model: `google-gemini/gemini-2-flash` (recommended)
- Purpose: Fast web research and data gathering
- Why: Cheaper, faster, sufficient for research tasks

**Competitor Researcher Subagent**:
- Model: `google-gemini/gemini-2-flash`
- Purpose: Analyze competitor content quickly

**Cost Optimization**:
- Main agent: Higher quality model for planning
- Researchers: FlashX/Haiku for speed and cost
- SEO writer: Mid-tier model for quality vs cost balance

### Thinking Level

**SEO Writer**: `low` or `medium`
- Reasoning needed for content structure and optimization
- Not deep reasoning (save tokens)

**Researchers**: `off` or `minimal`
- Simple data fetching and parsing
- No complex decision-making
- Save tokens, speed up execution

### Skill Dependencies

**Required Skills**:

1. **searxng** (for keyword/competitor research)
   - Location: `~/.openclaw/workspace/skills/searxng-self-hosted/SKILL.md`
   - Purpose: Web search using self-hosted SearXNG instance
   - URL: http://89.167.66.83:8888
   - Usage: Keyword discovery, SERP analysis, competitor research

2. **web_fetch** (for specific article analysis)
   - Purpose: Extract content from specific URLs
   - Use case: Analyze competitor articles in detail
   - Note: Read skill documentation for usage patterns

**No special SEO skills needed**:
- Use general tools (read, write, edit)
- Schema markup generated manually in JSON-LD
- No external SEO APIs required

### Communication Protocol

#### Main Agent → SEO Writer

**Brief Format** (from main agent):
```
Write a blog post about keyword research

Requirements:
- Target audience: Small business owners
- Primary keyword: "keyword research"
- Secondary keywords: "keyword research tools", "long-tail keywords", "search intent"
- Word count: 2500 words
- Content type: Comprehensive guide
- Brand: MyBrand
- Tone: Professional but approachable
- Include schema: Article, BlogPosting, FAQPage
- Featured snippet target: Yes

Additional context:
Focus on free tools since the audience is small businesses with limited budgets.
Include a comparison table of free tools.
```

#### SEO Writer → Main Agent

**Announce Format**:
```
Result: Complete SEO-optimized blog post delivered

Content Summary:
- Word count: 2,540 words
- Primary keyword: "keyword research" (6 mentions, density: 0.24%)
- Secondary keywords: "keyword research tools" (3), "long-tail keywords" (2), "search intent" (4)
- Featured snippet targets: 3 (2 definitions, 1 step list)
- FAQ section: 5 questions from PAA analysis

SEO Elements:
- Title: "Keyword Research Guide for Small Businesses 2025 | MyBrand" (55 chars)
- Meta: "Learn keyword research with free tools. Our guide covers search intent, long-tail keywords, and strategies for small business SEO. Start now." (157 chars)
- Schema: Article + BlogPosting + FAQPage generated
- Internal links: 5 suggested
- External links: 3 authoritative sources

Quality Indicators:
- E-E-A-T: Personal examples, expert citations, clear author perspective
- Humanization: Varied sentence structure, specific examples, personal anecdotes
- Readability: Grade 8 reading level, scannable structure
- Originality: Unique insights from agency experience

File Location:
- /home/node/.openclaw/workspace/projects/seo/deliverables/keyword-research-small-business-content.md

Status: completed successfully

Runtime: 12m34s
Tokens: input: 8,234 / output: 4,567 / total: 12,801
Session: agent:seo-writer:subagent:abc123
Transcript: /home/node/.openclaw/agents/seo-writer/sessions/abc123.jsonl

Notes: All quality checks passed. Content is ready for publication.
Recommendation: Publish after editorial review of brand tone.
```

#### Quality Checklist Before Delivery

**SEO Writer must verify**:
- [ ] Content meets word count requirement (within 10%)
- [ ] All required keywords integrated naturally
- [ ] No keyword stuffing
- [ ] Title tag optimized (50-60 chars)
- [ ] Meta description optimized (150-160 chars)
- [ ] H1-H3 hierarchy correct
- [ ] Featured snippet targets included (2-4 sections)
- [ ] FAQ section if PAA questions found
- [ ] E-E-A-T signals present (experience, expertise, citations)
- [ ] Content humanized (varied sentences, personal examples)
- [ ] Schema markup generated (Article, BlogPosting, FAQPage)
- [ ] Internal linking suggestions provided (3-5)
- [ ] File saved to correct location

**If any check fails**:
- Note what failed in `Notes:` field
- Suggest remediation steps
- Partial delivery if most checks pass
- Re-run if critical checks fail

---

## MCP and API Requirements

### Integration Architecture

The SEO Writer Agent uses a hybrid approach for API integration:

1. **OpenClaw Built-in Tools** (preferred for simplicity)
   - `web_search` with SearXNG backend for keyword research
   - `web_fetch` for competitor article analysis
   - `exec` with Python scripts for API calls
   - `read`/`write` for data persistence

2. **Direct HTTP API Calls** (for production APIs)
   - Keyword research APIs (Ahrefs, SEMrush, Ubersuggest)
   - SERP analysis APIs (Serper.dev, SERPAPI)
   - AI detection APIs (Originality.ai)
   - Technical SEO APIs (PageSpeed Insights)

3. **Custom MCP Servers** (optional for complex integrations)
   - When streaming responses are needed
   - When multiple APIs need orchestration
   - When caching and rate limiting are complex

### API Configuration

**Environment Variables Required**:
```bash
# Keyword Research (optional, paid)
AHREFS_API_KEY="your_ahrefs_key"
SEMRUSH_API_KEY="your_semrush_key"
UBERSUGGEST_API_KEY="your_ubersuggest_key"

# SERP Analysis
SERPER_API_KEY="your_serper_key"
SERPAPI_API_KEY="your_serpapi_key"

# AI Content Detection
ORIGINALITY_API_KEY="your_originality_key"

# Technical SEO (optional)
PAGESPEED_API_KEY="your_pagespeed_key"

# Content Quality
LANGUAGETOOL_API_KEY="your_languagetool_key"
```

**Configuration File** (`~/.openclaw/workspace/.env.seo-apis`):
```bash
# Copy this file and set your API keys
# Example: cp .env.seo-apis.example .env.seo-apis

# SERP Analysis (RECOMMENDED for MVP)
SERPER_API_KEY=

# Keyword Research (optional, for production)
AHREFS_API_KEY=
SEMRUSH_API_KEY=
UBERSUGGEST_API_KEY=

# AI Content Detection (optional, for quality assurance)
ORIGINALITY_API_KEY=

# Content Quality (optional, for professional editing)
LANGUAGETOOL_API_KEY=

# Technical SEO (optional, PageSpeed Insights has generous free tier)
PAGESPEED_API_KEY=
```

### API Integration Strategy

#### MVP Implementation (Phase 1)

**No API Keys Required** - Use free alternatives:

1. **Keyword Research**: SearXNG self-hosted
   - Already configured in OpenClaw
   - URL: http://89.167.66.83:8888
   - Usage: `web_search` or direct HTTP calls

2. **SERP Analysis**: SearXNG
   - Extract SERP features via parsing
   - Get PAA questions from search results
   - Free, unlimited queries

3. **Technical SEO**: PageSpeed Insights API
   - Free tier: 25,000 requests/day
   - Official Google API
   - Core Web Vitals data

4. **Content Quality**: Built-in algorithms
   - Readability scoring (Flesch-Kincaid, Gunning Fog)
   - Basic grammar checking
   - Manual schema generation

**Total Cost**: $0/month

#### Growth Implementation (Phase 2)

**Add These APIs for Professional Features**:

1. **SERP Analysis**: Serper.dev Starter ($5/month)
   - Structured SERP data
   - Reliable SERP feature detection
   - People Also Ask extraction
   - Featured snippet tracking

2. **Keyword Research**: Ubersuggest API ($29/month)
   - Search volume data
   - Keyword difficulty scores
   - Related keyword suggestions

3. **AI Content Detection**: Originality.ai ($30/month)
   - AI probability score
   - Humanization assessment
   - Quality assurance

4. **Content Quality**: LanguageTool ($59/year ≈ $5/month)
   - Professional grammar checking
   - Style suggestions
   - Spelling and punctuation

**Total Cost**: ~$69/month

#### Enterprise Implementation (Phase 3)

**Full API Suite**:

1. **Keyword Research**: Ahrefs API ($399/month) or SEMrush ($499/month)
   - Largest keyword database (12B+)
   - Accurate difficulty scores
   - Historical data (6 years)
   - Competitor analysis

2. **SERP Analysis**: SERPAPI Business ($500/month)
   - Multi-platform support
   - Advanced SERP features
   - Historical tracking

3. **AI Detection**: Originality.ai Pro ($200/month)
   - Batch processing
   - API access for scale

4. **Technical SEO**: DataForSEO On-Page (pay-as-you-go)
   - Comprehensive on-page audit
   - Technical issue detection

**Total Cost**: ~$1,200/month

### API Key Management

**Best Practices**:

1. **Never hardcode API keys** in agent code
2. **Use environment variables** or OpenClaw secrets
3. **Store keys in `.env.seo-apis`** file (not in git)
4. **Rotate keys regularly** (every 90 days)
5. **Use separate keys** for dev, staging, production
6. **Monitor API usage** and costs

**OpenClaw Secrets Management**:
```bash
# Set API key (stored in OpenClaw config)
openclaw config set secrets.SERPER_API_KEY "your_key"

# Use in agent
import os
api_key = os.getenv("SERPER_API_KEY")
```

**Load Environment File**:
```python
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
env_file = Path("~/.openclaw/workspace/.env.seo-apis").expanduser()
load_dotenv(env_file)

# Access API key
api_key = os.getenv("SERPER_API_KEY")
```

### Rate Limiting and Caching

**Rate Limiting**:

All API calls should include rate limiting:

```python
import time
from typing import Optional

class RateLimitedAPI:
    """Rate-limited API client"""

    def __init__(self, requests_per_minute: int = 60):
        self.requests_per_minute = requests_per_minute
        self.request_times = []

    def request(self, method: str, url: str, **kwargs) -> Optional[dict]:
        """Make rate-limited request"""

        # Clean old requests
        now = time.time()
        self.request_times = [t for t in self.request_times if now - t < 60]

        # Wait if rate limit reached
        if len(self.request_times) >= self.requests_per_minute:
            sleep_time = 60 - (now - self.request_times[0])
            time.sleep(sleep_time)

        # Make request
        try:
            response = requests.request(method, url, **kwargs)
            self.request_times.append(time.time())

            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 60))
                time.sleep(retry_after)
                return self.request(method, url, **kwargs)

            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(f"API error: {e}")
            return None
```

**Caching Strategy**:

Cache API responses to reduce costs and improve speed:

```python
import json
import hashlib
import time
from pathlib import Path
from typing import Optional

class APICache:
    """API response cache"""

    def __init__(self, cache_dir: str = "/tmp/seo-api-cache", ttl: int = 3600):
        self.cache_dir = Path(cache_dir)
        self.ttl = ttl  # Time-to-live in seconds
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_key(self, url: str, params: dict) -> str:
        """Generate cache key"""
        key = f"{url}?{json.dumps(params, sort_keys=True)}"
        return hashlib.md5(key.encode()).hexdigest()

    def get(self, url: str, params: dict) -> Optional[dict]:
        """Get cached response"""
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
```

**Recommended Cache TTL**:

| API Type | Cache TTL | Reason |
|----------|-----------|--------|
| Keyword Research | 24 hours | Search volume changes slowly |
| SERP Analysis | 1 hour | Results can change frequently |
| AI Detection | Never | Content is unique |
| PageSpeed Insights | 1 hour | Scores don't change instantly |
| Schema Generation | Never | Static markup |

### Error Handling

**All API calls should include robust error handling**:

```python
def api_call_with_retry(
    func,
    max_retries: int = 3,
    backoff: float = 2.0
) -> Optional[dict]:
    """API call with exponential backoff"""

    for attempt in range(max_retries):
        try:
            result = func()
            return result

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise ValueError("Invalid API key")

            if e.response.status_code == 403:
                raise ValueError("API key unauthorized")

            if e.response.status_code == 429:
                if attempt == max_retries - 1:
                    raise

                wait_time = backoff ** (attempt + 1)
                print(f"Rate limited, retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue

            raise

        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise

            wait_time = backoff ** (attempt + 1)
            print(f"Request failed, retrying in {wait_time}s...")
            time.sleep(wait_time)

    return None
```

### API Integration Examples

#### Example 1: Keyword Research with Serper.dev

```python
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
env_file = Path("~/.openclaw/workspace/.env.seo-apis").expanduser()
load_dotenv(env_file)

def get_related_keywords(query: str) -> dict:
    """Get related keywords via search autocomplete"""
    api_key = os.getenv("SERPER_API_KEY")

    if not api_key:
        print("⚠️ SERPER_API_KEY not set, using free fallback")
        # Fallback to Google Suggest API (free, rate limited)
        return _get_google_suggestions(query)

    response = requests.post(
        "https://google.serper.dev/search",
        headers={
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        },
        json={
            "q": query,
            "gl": "us",
            "hl": "en",
            "num": 10
        }
    )

    response.raise_for_status()
    return response.json()

def _get_google_suggestions(query: str) -> dict:
    """Free fallback: Google Autocomplete API"""
    response = requests.get(
        "http://suggestqueries.google.com/complete/search",
        params={
            "output": "firefox",
            "q": query,
            "hl": "en"
        }
    )

    suggestions = response.json()[1]

    return {
        "organic": [{"title": kw, "link": ""} for kw in suggestions],
        "relatedSearches": [{"query": kw} for kw in suggestions]
    }
```

#### Example 2: SERP Analysis

```python
def analyze_serp(query: str) -> dict:
    """Analyze SERP for query"""
    api_key = os.getenv("SERPER_API_KEY")

    if not api_key:
        # Fallback to SearXNG (free, self-hosted)
        return _analyze_serp_searxng(query)

    response = requests.post(
        "https://google.serper.dev/search",
        headers={
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        },
        json={
            "q": query,
            "gl": "us",
            "hl": "en",
            "num": 10
        }
    )

    response.raise_for_status()
    return response.json()

def _analyze_serp_searxng(query: str) -> dict:
    """Free SERP analysis via SearXNG"""
    response = requests.get(
        "http://89.167.66.83:8888/search",
        params={
            "q": query,
            "format": "json",
            "language": "en-US"
        }
    )

    data = response.json()

    # Parse SERP features from results
    return {
        "organic": [
            {
                "title": r["title"],
                "link": r["url"],
                "snippet": r.get("content", "")
            }
            for r in data.get("results", [])
        ],
        "relatedSearches": []  # SearXNG doesn't provide this
    }

def extract_paa_questions(serp_data: dict) -> list:
    """Extract People Also Ask questions"""
    paa = serp_data.get("peopleAlsoAsk", [])

    return [
        {
            "question": item["question"],
            "answer": item["snippet"][:200] + "..."
        }
        for item in paa
    ]
```

#### Example 3: PageSpeed Insights

```python
def get_pagespeed_score(url: str, strategy: str = "mobile") -> dict:
    """Get PageSpeed Insights score"""
    # Optional API key for higher quota
    api_key = os.getenv("PAGESPEED_API_KEY")

    params = {
        "url": url,
        "strategy": strategy
    }

    if api_key:
        params["key"] = api_key

    response = requests.get(
        "https://www.googleapis.com/pagespeedonline/v5/runPagespeed",
        params=params
    )

    response.raise_for_status()
    return response.json()

def extract_cwv(psi_data: dict) -> dict:
    """Extract Core Web Vitals"""
    audits = psi_data["lighthouseResult"]["audits"]

    return {
        "lcp": audits["largest-contentful-paint"]["displayValue"],
        "fid": audits.get("max-potential-fid", {}).get("displayValue", "N/A"),
        "cls": audits["cumulative-layout-shift"]["displayValue"],
        "score": int(psi_data["lighthouseResult"]["categories"]["performance"]["score"] * 100)
    }
```

### OpenClaw Built-in Tools

The SEO Writer Agent can leverage OpenClaw's built-in tools:

1. **web_search**: SearXNG self-hosted search
   - Free, unlimited queries
   - Good for keyword research and SERP analysis
   - URL: http://89.167.66.83:8888

2. **web_fetch**: Extract content from URLs
   - Useful for competitor analysis
   - Scraping specific articles
   - Free, rate limited by remote server

3. **exec**: Run shell commands and Python scripts
   - Full Python scripting capability
   - Make HTTP API calls
   - Process and transform data

4. **read/write**: File operations
   - Save research findings
   - Generate deliverables
   - Cache API responses

### MCP Server Integration (Optional)

For complex integrations, custom MCP servers can be created:

**MCP Server Benefits**:
- Standardized tool interface
- Built-in error handling
- Rate limiting support
- Streaming responses
- Easier agent integration

**MCP Server Location**:
- `/root/.openclaw/mcp-servers/seo-apis/` (custom MCPs)
- `/app/skills/` (skill-based MCPs)

**See**: `SEO-APIs-and-MCPs.md` for detailed MCP server implementation guide.

### API Monitoring

**Track API Usage**:

```python
import json
from pathlib import Path

class APIMonitor:
    """Monitor API usage and costs"""

    def __init__(self, log_file: str = "/tmp/seo-api-usage.json"):
        self.log_file = Path(log_file)
        self.usage = self._load_usage()

    def _load_usage(self) -> dict:
        """Load usage data"""
        if not self.log_file.exists():
            return {}

        with open(self.log_file) as f:
            return json.load(f)

    def _save_usage(self):
        """Save usage data"""
        with open(self.log_file, "w") as f:
            json.dump(self.usage, f, indent=2)

    def log_call(self, api_name: str, endpoint: str, cost: float = 0.0):
        """Log API call"""
        import time

        today = time.strftime("%Y-%m-%d")

        if today not in self.usage:
            self.usage[today] = {}

        if api_name not in self.usage[today]:
            self.usage[today][api_name] = {
                "calls": 0,
                "cost": 0.0
            }

        self.usage[today][api_name]["calls"] += 1
        self.usage[today][api_name]["cost"] += cost

        self._save_usage()

    def get_usage(self, api_name: str = None) -> dict:
        """Get usage stats"""
        if api_name:
            return self.usage.get(api_name, {})

        return self.usage
```

**Monthly Cost Tracking**:

| API | Cost/Request | Monthly Budget | Status |
|-----|-------------|----------------|--------|
| Serper.dev | $0.002 | $5.00 | ✅ Within budget |
| Originality.ai | $0.001 | $30.00 | ✅ Within budget |
| Ubersuggest | $0.001 | $29.00 | ✅ Within budget |
| **Total** | - | **$64.00** | ✅ OK |

### Testing API Integration

**Test Script** (`~/.openclaw/workspace/tools/test-seo-apis.py`):

```python
#!/usr/bin/env python3
"""
Test SEO API integration
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv("~/.openclaw/workspace/.env.seo-apis")

def test_serp_analysis():
    """Test SERP analysis API"""
    print("🔍 Testing SERP Analysis...")

    api_key = os.getenv("SERPER_API_KEY")

    if not api_key:
        print("⚠️ SERPER_API_KEY not set")
        return False

    response = requests.post(
        "https://google.serper.dev/search",
        headers={
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        },
        json={"q": "keyword research", "gl": "us", "hl": "en"}
    )

    if response.status_code == 200:
        data = response.json()
        print(f"✅ SERP Analysis working")
        print(f"   - Organic results: {len(data.get('organic', []))}")
        print(f"   - PAA questions: {len(data.get('peopleAlsoAsk', []))}")
        return True
    else:
        print(f"❌ SERP Analysis failed: {response.status_code}")
        return False

def test_pagespeed():
    """Test PageSpeed Insights API"""
    print("\n⚡ Testing PageSpeed Insights...")

    api_key = os.getenv("PAGESPEED_API_KEY")

    params = {
        "url": "https://example.com",
        "strategy": "mobile"
    }

    if api_key:
        params["key"] = api_key

    response = requests.get(
        "https://www.googleapis.com/pagespeedonline/v5/runPagespeed",
        params=params
    )

    if response.status_code == 200:
        data = response.json()
        score = data["lighthouseResult"]["categories"]["performance"]["score"]
        print(f"✅ PageSpeed Insights working")
        print(f"   - Performance score: {score * 100:.0f}/100")
        return True
    else:
        print(f"❌ PageSpeed Insights failed: {response.status_code}")
        return False

def test_originality():
    """Test Originality.ai API"""
    print("\n🤖 Testing Originality.ai...")

    api_key = os.getenv("ORIGINALITY_API_KEY")

    if not api_key:
        print("⚠️ ORIGINALITY_API_KEY not set")
        return False

    response = requests.post(
        "https://api.originality.ai/api/v1/scan/ai",
        headers={
            "X-OAI-API-KEY": api_key,
            "Content-Type": "application/json"
        },
        json={
            "content": "This is a test of the Originality.ai API.",
            "title": "Test Content"
        }
    )

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Originality.ai working")
        print(f"   - AI score: {data.get('score', {}).get('ai', 0)}%")
        print(f"   - Original score: {data.get('score', {}).get('original', 0)}%")
        return True
    else:
        print(f"❌ Originality.ai failed: {response.status_code}")
        return False

if __name__ == "__main__":
    print("🧪 Testing SEO API Integration")
    print("=" * 50)

    results = {
        "SERP Analysis": test_serp_analysis(),
        "PageSpeed Insights": test_pagespeed(),
        "Originality.ai": test_originality()
    }

    print("\n" + "=" * 50)
    print("📊 Test Results:")
    for name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {status} - {name}")

    all_passed = all(results.values())
    print(f"\n{'✅ All tests passed!' if all_passed else '⚠️ Some tests failed'}")
```

**Usage**:
```bash
python3 ~/.openclaw/workspace/tools/test-seo-apis.py
```

### Summary

The SEO Writer Agent can be configured with:

- **MVP**: Free tools only ($0/month)
- **Growth**: Basic APIs ($69/month)
- **Enterprise**: Full API suite ($1,200/month)

Start with free tools (SearXNG, PageSpeed Insights) and upgrade as needed. All API integration can be done via:

1. **Direct HTTP calls** (simplest)
2. **Python scripts** (recommended for MVP)
3. **Custom MCP servers** (for complex workflows)

See `SEO-APIs-and-MCPs.md` for detailed API documentation, pricing, and code examples.

---

## Tool Policy

### Available Tools

**SEO Writer (Depth 1, orchestrator)**:
- `read`: Access keyword research and project files
- `write`: Save content and deliverables
- `edit`: Modify content files
- `exec`: Run any system commands
- `web_search`: SearXNG web search (if configured)
- `web_fetch`: Extract article content
- `sessions_spawn`: Spawn researcher subagents
- `subagents`: Manage researcher subagents
- `sessions_list`: List active subagents
- `sessions_history`: Access subagent transcripts
- `sessions_send`: Communicate with other sessions

**Keyword Researcher (Depth 2, worker)**:
- `read`: Save research findings
- `write`: Save research reports
- `web_search`: SearXNG web search
- `web_fetch`: Extract article content
- No session tools (cannot spawn children)

**Competitor Researcher (Depth 2, worker)**:
- `read`: Save analysis
- `write`: Save reports
- `web_search`: SearXNG web search
- `web_fetch`: Extract competitor content
- No session tools

### Denied Tools

**SEO Writer**:
- `sessions`: (general sessions tool) - not needed
- `message`: External communication - not allowed for content generation
- `tts`, `sherpa_tts`: Audio generation - not relevant

**Researchers**:
- All session tools: Cannot spawn their own subagents
- `sessions_spawn`: Denied (worker only)
- `subagents`: Denied (worker only)
- `sessions_list`: Denied (worker only)
- `sessions_history`: Denied (worker only)
- `sessions_send`: Denied (worker only)

---

## Examples

### Example 1: Blog Post Request

**Main Agent Brief**:
```
Write a comprehensive blog post about SEO content writing

Requirements:
- Target audience: Content marketers
- Primary keyword: "SEO content writing"
- Secondary keywords: "content optimization", "keyword integration", "E-E-A-T"
- Word count: 3000 words
- Content type: Ultimate guide
- Brand: ContentPro
- Tone: Expert, actionable
- Include schema: Article, BlogPosting
- Featured snippet target: Yes

Additional context:
Focus on modern SEO practices (2025). Include E-E-A-T requirements since that's critical now.
Use examples from our experience with SaaS companies.
```

**SEO Writer Execution**:
1. Parse requirements
2. Spawn keyword researcher:
   - Task: Research SEO content writing, search intent, competitors
   - Model: Gemini Flash
   - Thinking: minimal
3. Spawn competitor researcher:
   - Task: Analyze top 3 ranking articles
   - Model: Gemini Flash
   - Thinking: minimal
4. Wait for both researchers to announce
5. Synthesize research findings
6. Write content (3000+ words)
   - H1: "SEO Content Writing Guide 2025: E-E-A-T + Optimization"
   - Intro: Hook with stat, promise comprehensiveness
   - Body: 6-8 H2 sections covering all secondary keywords
   - Featured snippets: 3 (definition, step list, table)
   - FAQ: 5 PAA questions
   - Conclusion: Summary + CTA
7. Optimize SEO elements:
   - Title: "SEO Content Writing Guide 2025: E-E-A-T & Optimization | ContentPro"
   - Meta: "Master SEO content writing in 2025. Learn E-E-A-T integration, keyword optimization, and content strategy. Complete guide for marketers."
   - Schema: Article + BlogPosting
8. Humanize content:
   - Add "We've seen a 73% increase in traffic..."
   - Include specific SaaS examples
   - Vary sentence structure
9. Generate deliverables:
   - Title & meta
   - Full content (HTML-ready)
   - Schema markup
   - Internal linking suggestions
   - Quality checklist
10. Save to file
11. Announce back to main agent

**Result**: 3,245-word comprehensive guide delivered in 14 minutes

### Example 2: Product Page Request

**Main Agent Brief**:
```
Write a product page for our keyword research tool

Requirements:
- Target audience: Small business owners
- Primary keyword: "keyword research tool for small business"
- Secondary keywords: "affordable SEO tools", "easy keyword research"
- Word count: 800 words
- Content type: Product landing page
- Brand: KeywordToolPro
- Tone: Persuasive, professional
- Include schema: Product, FAQPage
- Featured snippet target: Yes

Additional context:
Highlight these features:
1. Free trial available
2. Easy to use (no SEO experience needed)
3. Results in 5 minutes
4. Competitor comparison table

Include testimonials section (3 reviews).
```

**SEO Writer Execution**:
1. Parse requirements (transactional intent)
2. Spawn competitor researcher:
   - Task: Analyze competitor product pages
   - Model: Gemini Flash
3. Write content (transactional optimization):
   - H1: "Best Keyword Research Tool for Small Business | KeywordToolPro"
   - Intro: Problem → Solution (small businesses struggle with SEO)
   - Features: Bullet list with benefits
   - Comparison table: KeywordToolPro vs Competitor A vs Competitor B
   - Testimonials: 3 social proof quotes
   - Pricing: Clear pricing with CTA
   - FAQ: 3 common questions (trial, difficulty, support)
4. Optimize for conversion:
   - Strong CTAs throughout
   - Benefit-focused copy
   - Social proof integrated
   - Clear pricing
5. Schema: Product + FAQPage
6. Announce back to main agent

**Result**: 950-word product page with strong conversion focus

---

## Limitations & Considerations

### What SEO Writer Does NOT Do

**Not included**:
- Image creation or editing
- Video production
- HTML/CSS code implementation
- CMS publishing (WordPress, etc.)
- Off-page SEO (backlinks, outreach)
- Technical SEO auditing (site speed, crawling)
- Local SEO optimization (Google Business Profile)

**Why**: These require specialized tools, access, or human judgment beyond text generation

### Content Limits

**Maximum word count**: 5,000 words per single request
**Reason**: Token limits, quality maintenance
**Solution**: For longer content, split into multiple subagents (part 1, part 2)

**Complex topics**: May require multiple research subagents
**Solution**: Spawn specialized researchers (one for each aspect)

### Quality Trade-offs

**Speed vs Quality**:
- Fast models (Gemini Flash): Quick but may miss nuances
- Quality models (Claude Sonnet): Slower but better writing
**Recommendation**: Use Claude Sonnet for SEO writer, Gemini Flash for researchers

**Cost vs Quality**:
- Higher cost models: Better reasoning, fewer errors
- Lower cost models: Cheaper, faster, good for research
**Recommendation**: Optimize model selection per task type

### Human in the Loop

**Editorial review recommended**:
- Brand tone alignment
- Fact-checking for sensitive topics
- Legal/compliance review
- Final approval before publication

**SEO Writer provides**:
- High-quality first draft
- SEO optimization built-in
- Clear structure and formatting
- Ready for human review

---

## Testing & Validation

### Test Scenarios

**Test 1: Basic Blog Post**
- Input: Simple topic, standard requirements
- Expected: 2000-word article, SEO-optimized
- Verify: Keyword placement, structure, schema generation

**Test 2: Complex Guide**
- Input: Broad topic, multiple subtopics
- Expected: 3500-word comprehensive guide
- Verify: Depth of coverage, multiple featured snippets

**Test 3: Product Page**
- Input: Transactional intent, conversion focus
- Expected: 1000-word landing page
- Verify: CTAs, social proof, conversion optimization

**Test 4: Error Handling**
- Input: Ambiguous brief, missing requirements
- Expected: Ask for clarification or provide options
- Verify: Graceful handling of incomplete input

### Validation Checklist

After each delivery, verify:
- [ ] Content is readable and coherent
- [ ] No grammatical errors
- [ ] SEO requirements met
- [ ] File saved correctly
- [ ] Announce format correct
- [ ] All tool calls successful
- [ ] No errors in execution

---

## Future Enhancements

### Version 2.0 Potential Features

- **Integration with keyword research APIs**: SEMrush, Ahrefs (if credentials provided)
- **Image suggestions**: Recommend image topics with alt text
- **Video content**: Generate video scripts with SEO optimization
- **Multi-language**: Support content in multiple languages
- **A/B testing**: Generate multiple versions of headlines
- **Performance tracking**: Monitor rankings after publication (with analytics integration)

### Automation Opportunities

- **Cron job**: Weekly content generation based on trending topics
- **Topic cluster generation**: Auto-generate pillar + cluster articles
- **Content refresh**: Auto-update old articles with new information
- **Competitor monitoring**: Weekly analysis of competitor content

---

## Conclusion

The SEO Writer Agent is designed to be a top-tier content generation system that combines:

- **Keyword research expertise** (via researcher subagents)
- **SEO optimization knowledge** (built-in to every piece of content)
- **Quality assurance** (E-E-A-T, humanization, self-assessment)
- **Scalability** (can be spawned for parallel production)
- **Professional output** (publication-ready deliverables)

**Configuration**:
- Runtime: subagent (orchestrator pattern with depth 2)
- Model: Claude Sonnet for writing, Gemini Flash for research
- Thinking: Low for writing, minimal for research
- Skills: searxng, web_fetch

**Communication**:
- Receives brief from main agent
- Spawns researchers for keyword and competitor analysis
- Synthesizes findings into SEO-optimized content
- Delivers formatted content with all SEO elements
- Announces back to main agent with complete summary

This agent specification enables building an AI automation agency with top-tier SEO capabilities, matching or exceeding human SEO writers while scaling efficiently through intelligent subagent orchestration.

---

*This specification combines SEO best practices with OpenClaw's agent orchestration capabilities to create a comprehensive SEO writing agent.*
