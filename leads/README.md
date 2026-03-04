# Reddit Lead Generation System

## Overview
Automated system for extracting, scoring, and monetizing leads from Reddit discussions.

## Quick Start

### 1. Generate Leads
```bash
./generate-leads.sh
```
This script:
- Searches multiple subreddits (marketing, startups, entrepreneur, SEO)
- Uses SearXNG for Reddit search
- Saves JSON results to `leads/tmp/`

### 2. Extract Leads
```bash
python3 extract-leads.py
```
This script:
- Parses SearXNG JSON results
- Extracts lead data (URL, title, content, subreddit)
- Removes duplicates
- Saves to CSV: `leads/sample-marketing-leads-[date].csv`

### 3. Score Leads
```bash
python3 score-leads.py
```
This script:
- Analyzes title and content for intent signals
- Scores leads as high/medium/low intent
- Estimates value per lead
- Saves to CSV: `leads/scored-leads-[date].csv`

## Current Leads

**File:** `leads/scored-leads-2026-03-03.csv`

**Statistics:**
- Total: 91 leads
- High intent: 50 (55.6%) - $10-20/lead
- Medium intent: 3 (3.3%) - $2-10/lead
- Low intent: 29 (32.2%) - $0.50-2/lead

## Monetization

### Pricing Model
| Package | Leads | Price | Avg Value/Lead |
|---------|-------|-------|----------------|
| Sample Pack | 20 | FREE | Test quality |
| Starter | 100 | $200 | $2 |
| Growth | 500 | $800 | $1.60 |
| Premium (high-intent) | 100 | $1,000 | $10 |

### Sales Channels
1. **r/LeadGenMarketplace** - Post with sample offer
2. **Cold Email** - Target marketing agencies
3. **LinkedIn** - Reach out to marketing directors
4. **Product Hunt** - Launch SaaS version (future)

### Outreach
**Target List:** `leads/outreach-targets.md` (9+ agencies identified)

**Email Template:** Included in `leads/outreach-targets.md`

## Documentation

- **Summary:** `leads/SUMMARY-2026-03-04.md` - Quick overview
- **Action Plan:** `research/reddit-lead-action-plan.md` - Step-by-step
- **Buyer Channels:** `research/lead-buyer-channels.md` - Where to sell
- **Monetization Research:** `research/reddit-lead-monetization.md` - Pricing models
- **Reddit Post:** `leads/reddit-post-template.md` - Ready to post

## Scripts

### generate-leads.sh
Automated lead generation script that:
- Searches SearXNG for high-intent Reddit posts
- Target subreddits: marketing, startups, entrepreneur, SEO
- Saves results to JSON files

### extract-leads.py
Lead extraction script that:
- Parses SearXNG JSON results
- Extracts lead data (URL, title, content, subreddit)
- Removes duplicates
- Saves to CSV format

### score-leads.py
Lead scoring script that:
- Analyzes title and content for intent signals
- Scores leads as high/medium/low intent
- Estimates value per lead ($0.50-20)
- Saves scored leads to CSV

## Target Subreddits

| Subreddit | Members | Lead Type | Intent Signals |
|-----------|---------|-----------|---------------|
| r/marketing | 1.1M | Agency clients | "Need help with [channel]" |
| r/startups | 1.8M | Startup founders | "Looking for [service]" |
| r/entrepreneur | 2.2M | Business owners | "Need help marketing" |
| r/SEO | 420K | SEO leads | "Need SEO help" |
| r/realestate | 1.4M | Buyers/sellers | "Looking to buy in [area]" |
| r/SaaS | 180K | SaaS founders | "Need help with [tool]" |

## Intent Scoring

**High Intent (worth $10-20/lead):**
- "need help", "looking for", "recommendations"
- "best agency", "hiring agency", "seeking agency"
- "budget", "pricing", "urgent", "asap"

**Medium Intent (worth $2-10/lead):**
- "how to find", "advice needed", "help with"
- "thinking about", "considering", "comparing"
- "any experience with", "has anyone used"

**Low Intent (worth $0.50-2/lead):**
- General discussions, no clear need
- Passive interest, no urgency

## Next Steps

1. **Post to r/LeadGenMarketplace** - Template ready
2. **Generate 100+ more leads** - Run `generate-leads.sh`
3. **Send outreach emails** - Use targets from `outreach-targets.md`
4. **Close deals** - Send sample packs, negotiate pricing
5. **Scale up** - Automate delivery, add more subreddits

## Success Metrics

- **Week 1:** 100+ leads generated, 20 outreach emails sent
- **Week 2-4:** 3-5 deals closed, $500-$1,000 revenue
- **Month 2:** 5-10 regular buyers, $2,000-$5,000/month

## Questions for Mr. Grey

1. Should I post to r/LeadGenMarketplace today?
2. What's the target revenue goal for first month?
3. Do you want me to handle outreach and closing?
4. Should I focus on marketing or expand to other industries?
5. What's the long-term vision (side hustle vs full business)?

---

**Status:** ✅ System working, ready to monetize
**Last Updated:** March 4, 2026
