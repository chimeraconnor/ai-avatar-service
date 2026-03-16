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
| Starter | 100 leads | **$500** | $5/lead avg |
| Growth | 500 leads | **$2,000** | $4/lead avg |
| Premium (high-intent only) | 100 leads | **$2,500** | $25/lead |

### Monthly Retainer
- **100 leads/month:** $1,000 (save $200)
- **500 leads/month:** $4,000 (save $2,000)

### Agency/Wholesale Discount
**40% off list price** for agencies reselling to clients:
- Sample Pack (20): FREE
- 100 leads: **$300** (wholesale)
- 500 leads: **$1,200** (wholesale)
- High-intent (100): **$1,500** (wholesale)
- Monthly retainer: **$600/month** (wholesale)

**Market Context:** Average B2B lead costs $200-650. These Reddit leads are high-intent warm leads at 60-90% below market.

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

## Execution Status

### Current Status: ⚠️ READY TO EXECUTE - AWAITING APPROVAL/DIRECTION

**Progress Overview:**
- ✅ **Research Phase:** COMPLETE (March 1-13)
- ✅ **Preparation Phase:** COMPLETE (March 14-16)
- ❌ **Execution Phase:** NOT STARTED (Day 3 of Week 1)

**Key Milestones:**
- March 1-13: Comprehensive market research, competitor analysis, pricing strategy
- March 14-16: Lead scraping (91 leads), scoring, templates, action trackers
- March 16: Cron reminder triggered - system ready, execution pending

**Critical Blocker:** Outreach not initiated. All preparation complete, 0 emails sent, 0 posts made, 0 sales closed.

### Week 1 Progress (March 14-20)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Emails Sent | 9+ | 0 | ❌ Not Started |
| Reddit Posts | 3+ | 0 | ❌ Not Started |
| Sample Packs | 20+ | 0 | ❌ Not Started |
| Responses | 15+ | 0 | ❌ Not Started |
| Sales Closed | 2-5 | 0 | ❌ Not Started |
| Revenue | $3,000-10,000 | $0 | ❌ Not Started |

**Revenue Goals:**
- Conservative (1-2 sales): $500-2,000
- Moderate (3-5 sales): $3,000-10,000
- Aggressive (5-10 sales): $7,500-25,000

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

**Status:** ⚠️ READY TO EXECUTE - AWAITING APPROVAL/DIRECTION
**Last Updated:** 2026-03-16
**Next Actions:**
1. 🚀 EXECUTE: Send 3 Priority 1 emails (Belkins, Callbox, Cleverly)
2. 🚀 EXECUTE: Create LeadSwap seller account
3. 🚀 EXECUTE: Create Fiverr gig for lead sales
4. 🚀 EXECUTE: Generate 50+ fresh leads
5. 🚀 EXECUTE: Post to Reddit communities

---

**See PROJECT-SUMMARY.md** for complete project status and documentation.
