# MCP Integration Guide for SEO Writer Agent

**Complete guide to integrating SEO APIs with OpenClaw via Model Context Protocol (MCP)**

*Version: 1.0*
*Date: March 2026*

---

## Table of Contents

1. [Introduction](#introduction)
2. [Understanding MCP](#understanding-mcp)
3. [Integration Approaches](#integration-approaches)
4. [Option 1: Direct API Calls (Recommended for MVP)](#option-1-direct-api-calls-recommended-for-mvp)
5. [Option 2: Python Scripts (Recommended for Phase 2)](#option-2-python-scripts-recommended-for-phase-2)
6. [Option 3: Custom MCP Servers (Recommended for Enterprise)](#option-3-custom-mcp-servers-recommended-for-enterprise)
7. [Configuration Management](#configuration-management)
8. [Error Handling](#error-handling)
9. [Caching Strategy](#caching-strategy)
10. [Testing and Validation](#testing-and-validation)

---

## Introduction

This guide explains how to integrate SEO APIs with the SEO Writer Agent in OpenClaw. There are three main approaches:

1. **Direct API Calls** - Simple HTTP requests via `exec` tool
2. **Python Scripts** - Reusable scripts with `exec` tool
3. **Custom MCP Servers** - Full MCP server implementation

**Recommendation**: Start with Option 1 or 2 (simplest), upgrade to Option 3 only when needed for complex workflows.

---

## Understanding MCP

### What is MCP?

MCP (Model Context Protocol) is an open protocol for connecting AI models to external tools. It provides:

- **Standardized interface** - Consistent way to call external APIs
- **Secure credential management** - API keys stored securely
- **Error handling** - Built-in retry logic and error handling
- **Rate limiting** - Respect API rate limits automatically
- **Streaming support** - Stream large responses

### MCP Architecture

```
┌─────────────────┐
│   OpenClaw      │
│   Agent         │
└────────┬────────┘
         │
         │ MCP Protocol (JSON-RPC 2.0)
         │
┌────────┴────────┐
│   MCP Server    │  ← Wraps external APIs
│   (Optional)    │
└────────┬────────┘
         │
         │ HTTP/HTTPS
         │
┌────────┴────────┐
│   External     │
│   SEO APIs     │
└─────────────────┘
```

### When to Use MCP

**Use MCP Server when**:
- You need streaming responses
- Complex orchestration of multiple APIs
- Want built-in caching and rate limiting
- Need to share tools across multiple agents

**Skip MCP Server when**:
- Simple API calls (one-off)
- Quick prototypes
- Limited number of APIs
- Learning curve is too steep

---

## Integration Approaches

| Approach | Complexity | Use Case | Best For |
|----------|------------|----------|----------|
| **Direct API Calls** | ⭐ Low | MVP, simple APIs | Testing, prototyping |
| **Python Scripts** | ⭐⭐ Medium | Production, reusable | Most SEO integrations |
| **MCP Servers** | ⭐⭐⭐ High | Enterprise, complex | Multi-agent workflows |

---

## Option 1: Direct API Calls (Recommended for MVP)

### Overview

Make HTTP requests directly using the `exec` tool with `curl`.

### Advantages
- No setup required
- Simple and fast
- Easy to debug
- No dependencies

### Disadvantages
- No caching
- No rate limiting
- Error handling manual
- Not reusable

### Example 1: SERP Analysis with Serper.dev

```bash
# In SEO Writer agent, use exec tool
curl -s "https://google.serper.dev/search" \
  -H "X-API-KEY: $SERPER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "keyword research", "gl": "us", "hl": "en"}' | \
  python3 -m json.tool
```

### Example 2: PageSpeed Insights

```bash
# Get mobile PageSpeed score
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=mobile" | \
  python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"Score: {d['lighthouseResult']['categories']['performance']['score']*100:.0f}/100\")"
```

### Example 3: Keyword Research with SearXNG (Free)

```bash
# Free SERP analysis via SearXNG
curl -s "http://89.167.66.83:8888/search?q=keyword+research&format=json" | \
  python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"Results: {len(d['results'])}\")"
```

### Usage in Agent

```python
# In SEO Writer agent
import subprocess

def serp_analysis(query: str) -> dict:
    """Analyze SERP via Serper.dev"""

    command = f'''
    curl -s "https://google.serper.dev/search" \
      -H "X-API-KEY: $SERPER_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{{"q": "{query}", "gl": "us", "hl": "en"}}'
    '''

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    import json
    return json.loads(result.stdout)
```

---

## Option 2: Python Scripts (Recommended for Phase 2)

### Overview

Create reusable Python scripts that wrap API calls. Execute via `exec` tool.

### Advantages
- Reusable across agents
- Easy to debug
- Full Python ecosystem
- Simple error handling

### Disadvantages
- No streaming
- No built-in rate limiting (must implement)
- Manual caching

### Directory Structure

```
~/.openclaw/workspace/
├── tools/
│   └── seo-apis/
│       ├── __init__.py
│       ├── serp_analysis.py
│       ├── keyword_research.py
│       ├── ai_detection.py
│       ├── pagespeed.py
│       └── config.py
└── projects/seo/
    └── .env.seo-apis
```

### Setup

**Step 1: Create tools directory**

```bash
mkdir -p ~/.openclaw/workspace/tools/seo-apis
cd ~/.openclaw/workspace/tools/seo-apis
```

**Step 2: Create configuration file** (`config.py`)

```python
"""
SEO API Configuration
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
env_file = Path("~/.openclaw/workspace/projects/seo/.env.seo-apis").expanduser()
if env_file.exists():
    load_dotenv(env_file)

# API Keys
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
AHREFS_API_KEY = os.getenv("AHREFS_API_KEY")
SEMRUSH_API_KEY = os.getenv("SEMRUSH_API_KEY")
ORIGINALITY_API_KEY = os.getenv("ORIGINALITY_API_KEY")
LANGUAGETOOL_API_KEY = os.getenv("LANGUAGETOOL_API_KEY")
PAGESPEED_API_KEY = os.getenv("PAGESPEED_API_KEY")

# API URLs
SERPER_URL = "https://google.serper.dev/search"
SERPAPI_URL = "https://serpapi.com/search"
AHREFS_URL = "https://api.ahrefs.com/v2/keywords"
ORIGINALITY_URL = "https://api.originality.ai/api/v1/scan/ai"
PAGESPEED_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

# SearXNG (self-hosted, free)
SEARXNG_URL = "http://89.167.66.83:8888"
```

**Step 3: Create SERP analysis script** (`serp_analysis.py`)

```python
#!/usr/bin/env python3
"""
SERP Analysis Tool
Uses Serper.dev or SearXNG for SERP analysis
"""

import json
import sys
from .config import SERPER_API_KEY, SERPER_URL, SEARXNG_URL

def serp_analysis_serper(query: str, country: str = "us", language: str = "en") -> dict:
    """Analyze SERP using Serper.dev API"""

    import requests

    if not SERPER_API_KEY:
        return {"error": "SERPER_API_KEY not configured"}

    response = requests.post(
        SERPER_URL,
        headers={
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        },
        json={"q": query, "gl": country, "hl": "language", "num": 10}
    )

    response.raise_for_status()
    return response.json()

def serp_analysis_searxng(query: str) -> dict:
    """Free SERP analysis using SearXNG"""

    import requests

    response = requests.get(
        f"{SEARXNG_URL}/search",
        params={
            "q": query,
            "format": "json",
            "language": "en-US"
        }
    )

    response.raise_for_status()
    data = response.json()

    # Transform SearXNG format to standard format
    return {
        "organic": [
            {
                "title": r["title"],
                "link": r["url"],
                "snippet": r.get("content", "")
            }
            for r in data.get("results", [])
        ],
        "query": query
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

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="SERP Analysis")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--source", choices=["serper", "searxng"], default="serper")
    parser.add_argument("--country", default="us")
    parser.add_argument("--language", default="en")

    args = parser.parse_args()

    if args.source == "serper":
        result = serp_analysis_serper(args.query, args.country, args.language)
    else:
        result = serp_analysis_searxng(args.query)

    print(json.dumps(result, indent=2))
```

**Step 4: Create keyword research script** (`keyword_research.py`)

```python
#!/usr/bin/env python3
"""
Keyword Research Tool
Uses Google Suggest API (free) or Ahrefs API (paid)
"""

import json
import sys
import requests
from .config import AHREFS_API_KEY

def keyword_suggestions_google(query: str) -> list:
    """Get keyword suggestions via Google Autocomplete (free)"""

    response = requests.get(
        "http://suggestqueries.google.com/complete/search",
        params={
            "output": "firefox",
            "q": query,
            "hl": "en"
        }
    )

    suggestions = response.json()[1]

    return [
        {
            "keyword": kw,
            "volume": None,
            "difficulty": None
        }
        for kw in suggestions
    ]

def keyword_research_ahrefs(keyword: str, country: str = "us") -> dict:
    """Research keyword using Ahrefs API"""

    if not AHREFS_API_KEY:
        return {"error": "AHREFS_API_KEY not configured"}

    response = requests.get(
        "https://api.ahrefs.com/v2/keywords",
        params={"keyword": keyword, "limit": 5},
        headers={"Authorization": f"Bearer {AHREFS_API_KEY}"}
    )

    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Keyword Research")
    parser.add_argument("keyword", help="Keyword to research")
    parser.add_argument("--source", choices=["google", "ahrefs"], default="google")
    parser.add_argument("--country", default="us")

    args = parser.parse_args()

    if args.source == "google":
        result = keyword_suggestions_google(args.keyword)
    else:
        result = keyword_research_ahrefs(args.keyword, args.country)

    print(json.dumps(result, indent=2))
```

**Step 5: Create AI detection script** (`ai_detection.py`)

```python
#!/usr/bin/env python3
"""
AI Content Detection Tool
Uses Originality.ai API
"""

import json
import sys
from .config import ORIGINALITY_API_KEY, ORIGINALITY_URL

def detect_ai_content(content: str, title: str = "") -> dict:
    """Detect AI-generated content using Originality.ai"""

    import requests

    if not ORIGINALITY_API_KEY:
        return {"error": "ORIGINALITY_API_KEY not configured"}

    response = requests.post(
        ORIGINALITY_URL,
        headers={
            "X-OAI-API-KEY": ORIGINALITY_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "content": content,
            "title": title
        }
    )

    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Content Detection")
    parser.add_argument("content", help="Content to analyze")
    parser.add_argument("--title", default="")

    args = parser.parse_args()

    result = detect_ai_content(args.content, args.title)
    print(json.dumps(result, indent=2))
```

**Step 6: Create PageSpeed script** (`pagespeed.py`)

```python
#!/usr/bin/env python3
"""
PageSpeed Insights Tool
Uses Google PageSpeed Insights API
"""

import json
import sys
from .config import PAGESPEED_API_KEY, PAGESPEED_URL

def get_pagespeed_score(url: str, strategy: str = "mobile") -> dict:
    """Get PageSpeed Insights score"""

    import requests

    params = {
        "url": url,
        "strategy": strategy
    }

    if PAGESPEED_API_KEY:
        params["key"] = PAGESPEED_API_KEY

    response = requests.get(PAGESPEED_URL, params=params)
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

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="PageSpeed Insights")
    parser.add_argument("url", help="URL to analyze")
    parser.add_argument("--strategy", choices=["mobile", "desktop"], default="mobile")

    args = parser.parse_args()

    result = get_pagespeed_score(args.url, args.strategy)
    cwv = extract_cwv(result)

    print(json.dumps(cwv, indent=2))
```

**Step 7: Create environment file** (`.env.seo-apis`)

```bash
# Copy this file and set your API keys
# Location: ~/.openclaw/workspace/projects/seo/.env.seo-apis

# SERP Analysis (RECOMMENDED for MVP)
SERPER_API_KEY=your_serper_key_here

# Keyword Research (optional, for production)
AHREFS_API_KEY=
SEMRUSH_API_KEY=

# AI Content Detection (optional, for quality assurance)
ORIGINALITY_API_KEY=

# Content Quality (optional)
LANGUAGETOOL_API_KEY=

# Technical SEO (optional, PageSpeed has generous free tier)
PAGESPEED_API_KEY=
```

**Step 8: Make scripts executable**

```bash
chmod +x ~/.openclaw/workspace/tools/seo-apis/*.py
```

### Usage in Agent

```python
# In SEO Writer agent
import subprocess
import json
import sys

def serp_analysis(query: str) -> dict:
    """Analyze SERP using Python script"""

    result = subprocess.run(
        [sys.executable, "~/.openclaw/workspace/tools/seo-apis/serp_analysis.py", query],
        capture_output=True,
        text=True
    )

    return json.loads(result.stdout)

def keyword_research(keyword: str) -> dict:
    """Research keyword using Python script"""

    result = subprocess.run(
        [sys.executable, "~/.openclaw/workspace/tools/seo-apis/keyword_research.py", keyword],
        capture_output=True,
        text=True
    )

    return json.loads(result.stdout)

def ai_detection(content: str) -> dict:
    """Detect AI content using Python script"""

    result = subprocess.run(
        [sys.executable, "~/.openclaw/workspace/tools/seo-apis/ai_detection.py", content],
        capture_output=True,
        text=True
    )

    return json.loads(result.stdout)
```

---

## Option 3: Custom MCP Servers (Recommended for Enterprise)

### Overview

Create a full MCP server that wraps SEO APIs. Follows MCP specification.

### Advantages
- Full MCP protocol compliance
- Streaming support
- Built-in caching and rate limiting
- Shareable across agents

### Disadvantages
- High complexity
- Requires MCP server implementation
- Steep learning curve
- Overkill for simple use cases

### When to Use

- You need to share SEO tools across multiple agents
- Complex orchestration of multiple APIs
- Need streaming responses
- Want full MCP compliance

### MCP Server Structure

```
~/.openclaw/workspace/mcp-servers/seo-apis/
├── server.py           # MCP server implementation
├── mcp.json            # MCP configuration
├── tools/
│   ├── keyword_research.py
│   ├── serp_analysis.py
│   └── ai_detection.py
└── README.md
```

### MCP Server Implementation

**Step 1: Create MCP server directory**

```bash
mkdir -p ~/.openclaw/workspace/mcp-servers/seo-apis/tools
cd ~/.openclaw/workspace/mcp-servers/seo-apis
```

**Step 2: Install MCP dependencies**

```bash
pip install mcp
```

**Step 3: Create MCP server** (`server.py`)

```python
#!/usr/bin/env python3
"""
SEO APIs MCP Server
Wraps SEO APIs for OpenClaw integration
"""

import json
import os
import sys
from typing import Dict, List, Optional
from mcp.server import Server
from mcp.types import Tool, TextContent

# Add tools directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools"))

# Import tools
from keyword_research import keyword_research
from serp_analysis import serp_analysis, extract_paa_questions
from ai_detection import detect_ai_content

# Create MCP server
app = Server("seo-apis")

@app.tool()
async def keyword_research_tool(
    keyword: str,
    country: str = "us",
    source: str = "google"
) -> TextContent:
    """
    Research keyword metrics

    Args:
        keyword: The keyword to research
        country: Country code (default: us)
        source: Data source (google, ahrefs)

    Returns:
        JSON with keyword metrics
    """
    if source == "google":
        result = keyword_research(keyword, country)
    else:
        result = keyword_research(keyword, country)

    return TextContent(
        type="text",
        text=json.dumps(result, indent=2)
    )

@app.tool()
async def serp_analysis_tool(
    query: str,
    country: str = "us",
    language: str = "en",
    source: str = "serper"
) -> TextContent:
    """
    Analyze SERP for query

    Args:
        query: Search query
        country: Country code (default: us)
        language: Language code (default: en)
        source: Data source (serper, searxng)

    Returns:
        JSON with SERP data
    """
    result = serp_analysis(query, country, language, source)

    return TextContent(
        type="text",
        text=json.dumps(result, indent=2)
    )

@app.tool()
async def ai_detection_tool(
    content: str,
    title: str = ""
) -> TextContent:
    """
    Detect AI-generated content

    Args:
        content: The text content to analyze
        title: Optional title for the content

    Returns:
        JSON with AI detection score
    """
    result = detect_ai_content(content, title)

    return TextContent(
        type="text",
        text=json.dumps(result, indent=2)
    )

# Run MCP server
if __name__ == "__main__":
    app.run()
```

**Step 4: Create MCP configuration** (`mcp.json`)

```json
{
  "name": "seo-apis",
  "version": "1.0.0",
  "description": "SEO APIs MCP server for keyword research, SERP analysis, and AI detection",
  "main": "server.py",
  "tools": [
    {
      "name": "keyword_research_tool",
      "description": "Research keyword metrics using Google Suggest or Ahrefs API",
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
          },
          "source": {
            "type": "string",
            "description": "Data source (google, ahrefs)"
          }
        },
        "required": ["keyword"]
      }
    },
    {
      "name": "serp_analysis_tool",
      "description": "Analyze SERP using Serper.dev or SearXNG",
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
          },
          "source": {
            "type": "string",
            "description": "Data source (serper, searxng)"
          }
        },
        "required": ["query"]
      }
    },
    {
      "name": "ai_detection_tool",
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
    "SERPER_API_KEY",
    "AHREFS_API_KEY",
    "ORIGINALITY_API_KEY"
  ]
}
```

**Step 5: Register MCP Server with OpenClaw**

```bash
# Add MCP server to OpenClaw config
openclaw config set mcp.servers.seo-apis.path ~/.openclaw/workspace/mcp-servers/seo-apis

# Set API keys
openclaw config set mcp.servers.seo-apis.env.SERPER_API_KEY "your_serper_key"
openclaw config set mcp.servers.seo-apis.env.AHREFS_API_KEY "your_ahrefs_key"
openclaw config set mcp.servers.seo-apis.env.ORIGINALITY_API_KEY "your_originality_key"
```

**Step 6: Test MCP Server**

```bash
# Start MCP server
cd ~/.openclaw/workspace/mcp-servers/seo-apis
python3 server.py
```

### Using MCP Tools in Agent

Once registered, MCP tools are available in agents via `call_tool`:

```python
# In SEO Writer agent
async def research_keyword(keyword: str):
    """Research keyword using MCP tool"""

    result = await call_tool("keyword_research_tool", {
        "keyword": keyword,
        "country": "us",
        "source": "google"
    })

    return json.loads(result.content[0].text)

async def analyze_serp(query: str):
    """Analyze SERP using MCP tool"""

    result = await call_tool("serp_analysis_tool", {
        "query": query,
        "country": "us",
        "language": "en",
        "source": "serper"
    })

    return json.loads(result.content[0].text)
```

---

## Configuration Management

### Environment Variables

**Option 1: OpenClaw Config** (Recommended for production)

```bash
# Set API key in OpenClaw config
openclaw config set secrets.SERPER_API_KEY "your_key"

# Access in agent
import os
api_key = os.getenv("SERPER_API_KEY")
```

**Option 2: .env file** (Recommended for development)

Create `.env.seo-apis` file:

```bash
SERPER_API_KEY=your_key
AHREFS_API_KEY=your_key
ORIGINALITY_API_KEY=your_key
```

Load in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv("~/.openclaw/workspace/projects/seo/.env.seo-apis")

api_key = os.getenv("SERPER_API_KEY")
```

### Secrets Management

**Never commit API keys to git**:

```bash
# Add .env files to .gitignore
echo ".env.seo-apis" >> ~/.openclaw/workspace/.gitignore
```

**Use OpenClaw secrets for production**:

```bash
# Store secret
openclaw config set secrets.SERPER_API_KEY "your_key"

# Use in agent
import os
api_key = os.getenv("SERPER_API_KEY")
```

---

## Error Handling

### Retry Logic

```python
import time
from typing import Callable, Optional

def retry_api_call(
    func: Callable,
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

                retry_after = int(e.response.headers.get("Retry-After", backoff ** (attempt + 1)))
                print(f"Rate limited, retrying in {retry_after}s...")
                time.sleep(retry_after)
                continue

            raise

        except Exception as e:
            if attempt == max_retries - 1:
                raise

            wait_time = backoff ** (attempt + 1)
            print(f"Request failed, retrying in {wait_time}s...")
            time.sleep(wait_time)

    return None
```

### Error Responses

Always check for errors in API responses:

```python
def check_api_response(response: dict) -> bool:
    """Check if API response is valid"""

    if "error" in response:
        print(f"❌ API Error: {response['error']}")
        return False

    if not response.get("data"):
        print("⚠️ No data in response")
        return False

    return True
```

---

## Caching Strategy

### File-Based Cache

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
        self.ttl = ttl
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

# Usage
cache = APICache(ttl=3600)  # 1 hour cache

def cached_api_call(url: str, params: dict):
    """API call with caching"""

    # Check cache
    cached = cache.get(url, params)
    if cached:
        print("✅ Cache hit!")
        return cached

    # Make API call
    response = requests.get(url, params=params)
    data = response.json()

    # Cache result
    cache.set(url, params, data)

    return data
```

### Cache TTL Recommendations

| API Type | Cache TTL | Reason |
|----------|-----------|--------|
| Keyword Research | 24 hours | Search volume changes slowly |
| SERP Analysis | 1 hour | Results can change frequently |
| AI Detection | Never | Content is unique |
| PageSpeed Insights | 1 hour | Scores don't change instantly |
| Schema Generation | Never | Static markup |

---

## Testing and Validation

### Test Script

Create `test-seo-apis.py`:

```python
#!/usr/bin/env python3
"""
Test SEO API integration
"""

import sys
import json
from pathlib import Path

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "tools" / "seo-apis"))

from serp_analysis import serp_analysis, extract_paa_questions
from keyword_research import keyword_suggestions_google
from pagespeed import get_pagespeed_score, extract_cwv

def test_serp_analysis():
    """Test SERP analysis"""
    print("🔍 Testing SERP Analysis...")

    try:
        result = serp_analysis("keyword research")
        print(f"✅ SERP Analysis working")
        print(f"   - Organic results: {len(result.get('organic', []))}")
        print(f"   - PAA questions: {len(extract_paa_questions(result))}")
        return True
    except Exception as e:
        print(f"❌ SERP Analysis failed: {e}")
        return False

def test_keyword_research():
    """Test keyword research"""
    print("\n🔤 Testing Keyword Research...")

    try:
        result = keyword_suggestions_google("keyword research")
        print(f"✅ Keyword Research working")
        print(f"   - Suggestions: {len(result)}")
        return True
    except Exception as e:
        print(f"❌ Keyword Research failed: {e}")
        return False

def test_pagespeed():
    """Test PageSpeed Insights"""
    print("\n⚡ Testing PageSpeed Insights...")

    try:
        result = get_pagespeed_score("https://example.com", "mobile")
        cwv = extract_cwv(result)
        print(f"✅ PageSpeed Insights working")
        print(f"   - Score: {cwv['score']}/100")
        print(f"   - LCP: {cwv['lcp']}")
        return True
    except Exception as e:
        print(f"❌ PageSpeed Insights failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing SEO API Integration")
    print("=" * 50)

    results = {
        "SERP Analysis": test_serp_analysis(),
        "Keyword Research": test_keyword_research(),
        "PageSpeed Insights": test_pagespeed()
    }

    print("\n" + "=" * 50)
    print("📊 Test Results:")
    for name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {status} - {name}")

    all_passed = all(results.values())
    print(f"\n{'✅ All tests passed!' if all_passed else '⚠️ Some tests failed'}")
```

### Run Tests

```bash
python3 ~/.openclaw/workspace/tools/test-seo-apis.py
```

---

## Summary

### Quick Start Guide

1. **MVP (Free)**: Use direct API calls with `curl` via `exec` tool
2. **Phase 2**: Create Python scripts for reusable API integration
3. **Enterprise**: Build custom MCP servers for complex workflows

### Recommended Approach

For most SEO Writer Agent implementations, **Option 2 (Python Scripts)** is recommended:

- ✅ Simple to implement
- ✅ Reusable across agents
- ✅ Easy to debug
- ✅ Full Python ecosystem
- ❌ No streaming (not needed for SEO)
- ❌ Manual rate limiting (easy to add)

### Files Created

```
~/.openclaw/workspace/
├── tools/seo-apis/
│   ├── config.py
│   ├── serp_analysis.py
│   ├── keyword_research.py
│   ├── ai_detection.py
│   └── pagespeed.py
└── projects/seo/
    └── .env.seo-apis
```

### Next Steps

1. Set up `.env.seo-apis` with API keys
2. Test API integration with test script
3. Integrate with SEO Writer agent
4. Monitor usage and costs
5. Add caching for cost optimization

---

*For detailed API documentation, see `SEO-APIs-and-MCPs.md`*
