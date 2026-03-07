# Reddit Lead Generation System

## Overview

High-intent leads extracted from Reddit discussions (r/marketing, r/startups, r/SEO, etc.). These are users explicitly asking for marketing help, agency recommendations, and solutions to specific challenges.

## Available Lead Files

### Main Dataset
- **scored-leads-2026-03-03.csv** - 91 scored leads with intent classification
  - High intent: 50 (55.6%) - $10-20/lead value
  - Medium intent: 3 (3.3%) - $2-10/lead value
  - Low intent: 29 (32.2%) - $0.50-2/lead value
  - Unknown: 8 (8.9%)

### Sample Packs (Free)
- **sample-pack-20-leads.csv** - 20 mixed-intent leads for testing
- **high-intent-sample-15.csv** - 15 high-intent leads only

## Lead Fields

| Field | Description |
|-------|-------------|
| post_url | Direct link to Reddit post |
| subreddit | Which subreddit |
| post_id | Reddit post ID |
| post_title | Post title |
| post_content | Post body text |
| upvotes | Engagement score |
| comments | Number of comments |
| intent_score | High/Medium/Low/Unknown |
| industry | Industry classification |
| notes | Additional context |
| extracted_date | When lead was extracted |
| value_estimate | Estimated value ($0-20) |

## Pricing Model

| Package | Leads | Price | Value |
|---------|-------|-------|-------|
| Sample Pack | 20 leads | **FREE** | $200-400 |
| Starter | 100 leads | $200 | $2/lead avg |
| Growth | 500 leads | $800 | $1.60/lead avg |
| Premium (high-intent only) | 100 leads | $1,000 | $10-20/lead |

### Monthly Retainer
- **100 leads/month:** $1,000 (save $200)
- **500 leads/month:** $4,000 (save $2,000)

## Lead Quality

### High Intent ($10-20/lead)
- Explicit requests for help ("need help", "looking for")
- Agency recommendations requested
- Budget mentioned or implied urgent need
- Specific problems stated

### Medium Intent ($2-10/lead)
- Comparing options or solutions
- Discussing challenges but no explicit request
- General interest in services

### Low Intent ($0.50-2/lead)
- General discussions
- No clear immediate need
- Passive interest only

## Scripts

### Extract Leads
```bash
cd /home/node/.openclaw/workspace/leads
python3 extract-leads.py
```

### Score Leads
```bash
python3 score-leads.py
```

### Auto-Generate Leads
```bash
./generate-leads.sh
```

## Sales Materials

- **reddit-post-template.md** - Reddit post for r/LeadGenMarketplace
- **outreach-targets.md** - List of 9+ agencies to contact
- **research/** - Market research and action plans

## Action Plan

### Week 1: Quick Wins
1. Post to r/LeadGenMarketplace (template ready)
2. Generate 100+ more leads
3. Send 20 outreach emails to agencies

### Week 2-4: Validation & First Sales
4. Send free sample packs to interested buyers
5. Close 3-5 deals
6. Collect feedback and testimonials

### Month 2+: Scale
7. Expand to more industries (real estate, SaaS, insurance)
8. Build API/SaaS wrapper
9. Scale to 100+ leads/day, 5-10 regular buyers

## Success Metrics

### Week 1
- ✅ Post on r/LeadGenMarketplace
- ✅ Generate 100+ more leads
- ✅ Send 20 outreach emails
- ✅ Get 5+ responses

### Week 2-4
- ✅ Close 3-5 deals
- ✅ Generate $500-$1,000 revenue
- ✅ Collect feedback from buyers

### Month 2+
- ✅ Scale to 5-10 regular buyers
- ✅ Monthly revenue $2,000-$5,000
- ✅ Automated lead generation and delivery

## Revenue Potential

Based on current leads (91):
- **High intent (50 leads):** $500-$1,000 potential revenue
- **Total portfolio:** $800-$1,500 potential revenue

With scale (500 leads):
- **Monthly revenue:** $1,600-$8,000 (depending on quality mix)
- **Yearly potential:** $19,200-$96,000

## Notes

- Reddit leads are **high-intent** — users actively seeking solutions
- Fresh leads can be generated daily via SearXNG
- All leads include engagement metrics (upvotes, comments)
- Targeted to marketing/business communities

---

**Status:** ✅ System ready - monetization in progress
**Last Updated:** 2026-03-06
