# OpenClaw Discord Feature Implementation Plan

**Created:** 2026-02-23
**Purpose:** Track Discord/OpenClaw feature implementations and planned additions

---

## ✅ ALREADY IMPLEMENTED

| Feature | Status | Reference |
|---------|--------|-----------|
| Basic Discord bot setup | ✅ | [Discord Setup](https://docs.openclaw.ai/channels/discord) |
| Guild allowlist | ✅ | [Access Control](https://docs.openclaw.ai/channels/discord#access-control-and-routing) |
| Model switching (`/model`) | ✅ | [Slash Commands](https://docs.openclaw.ai/tools/slash-commands) |
| Native slash commands | ✅ | [Slash Commands](https://docs.openclaw.ai/tools/slash-commands) |
| Model aliases (kimi, glm, flashx, GLM) | ✅ | `agents.defaults.models` config |
| **Live Stream Preview** (streaming) | ✅ 2026-02-23 | `channels.discord.streaming: "partial"` |
| **Ack Reaction** (👀) | ✅ 2026-02-23 | `channels.discord.ackReaction: "👀"` |
| **Bot Presence/Status** (dynamic rotation) | ✅ 2026-02-23 | Cron job + `message set-presence` |

**Current Aliases:**
- `kimi` → kimi-coding/k2p5
- `glm` → zai/glm-4.7
- `flashx` → zai/glm-4-flash
- `flashx47` → zai/glm-4.7-flashx
- `GLM` → zai/glm-5

---

## 🔧 IMMEDIATE ADDITIONS (Quick Wins)

| Priority | Feature | What It Does | Config/Command | Reference |
|----------|---------|--------------|----------------|-----------|
| ~~1~~ ✅ | ~~Live Stream Preview~~ | ~~Shows typing indicator while generating responses~~ | ~~`channels.discord.streaming: "partial"`~~ | [Streaming](https://docs.openclaw.ai/channels/discord#live-stream-preview) |
| ~~1~~ ✅ | ~~Ack Reaction~~ | ~~👀 emoji while processing~~ | ~~`channels.discord.ackReaction: "👀"`~~ | [Ack Reactions](https://docs.openclaw.ai/channels/discord#ack-reactions) |
| ~~1~~ ✅ | ~~Bot Presence/Status~~ | ~~Shows "Playing..." or custom status~~ | ~~`channels.discord.activity: "Helping Mr. Grey"`~~ | [Presence](https://docs.openclaw.ai/channels/discord#presence-configuration) |
| 3 | **Reply Tags** | Native Discord reply threading | `channels.discord.replyToMode: "first"` | [Reply Tags](https://docs.openclaw.ai/channels/discord#reply-tags-and-native-replies) |
| 4 | **Reaction Notifications** | Get notified when users react | `channels.discord.reactions: "own"` | [Reactions](https://docs.openclaw.ai/channels/discord#reaction-notifications) |

---

## 🎮 INTERACTIVE FEATURES (Medium Effort)

| Feature | What It Does | Implementation | Reference |
|---------|--------------|----------------|-----------|
| **Interactive Components v2** | Buttons, dropdowns, forms in messages | Use `components` in message tool | [Components](https://docs.openclaw.ai/channels/discord#interactive-components) |
| **Modal Forms** | Pop-up forms for user input | `components.modal` with fields | [Modals](https://docs.openclaw.ai/channels/discord#interactive-components) |
| **Exec Approval Buttons** | Approve/deny dangerous commands via buttons | `channels.discord.execApprovals.enabled: true` | [Exec Approvals](https://docs.openclaw.ai/channels/discord#exec-approvals-in-discord) |
| **Thread-Bound Sessions** | Bind threads to subagent sessions | `/focus`, `/unfocus` commands | [Thread Bindings](https://docs.openclaw.ai/channels/discord#thread-bound-sessions-for-subagents) |

---

## 🎙️ VOICE FEATURES (Advanced)

| Feature | Requirements | Config | Reference |
|---------|--------------|--------|-----------|
| **Voice Channel Join** | Real-time voice conversations | `channels.discord.voice.enabled: true` | [Voice Channels](https://docs.openclaw.ai/channels/discord#voice-channels) |
| **Voice TTS** | Text-to-speech in voice | `voice.tts.provider: "openai"` | [Voice TTS](https://docs.openclaw.ai/channels/discord#voice-channels) |
| ~~Voice Messages (native)~~ | ~~Send audio as voice messages~~ | ~~`asVoice: true`~~ | ~~BROKEN - Issue #16103~~ |
| **Voice Messages (skill)** ✅ | Send audio with waveform | `discord-voice` skill | [discord-voice-skill](https://github.com/chimeraconnor/discord-voice-skill) |

**Note:** Native `asVoice` is broken. Use the custom `discord-voice` skill instead.

### Discord Voice Message Skill (✅ COMPLETED 2026-02-24)

**Repo:** https://github.com/chimeraconnor/discord-voice-skill

**What it does:**
- Sends audio files as native Discord voice messages with waveform visualization
- Works around OpenClaw Issue #16103 (broken native `asVoice`)
- Auto-converts audio to OGG/Opus
- Generates 256-sample waveform from audio amplitude
- 3-step Discord API: Upload URL → CDN Upload → Voice Message

**Usage:**
```bash
~/.openclaw/tools/tts-speak.sh "Hello" /tmp/voice.wav kokoro 1
python3 ~/.openclaw/workspace/skills/discord-voice/scripts/send_voice.py \
  --channel-id 1475566112019058758 \
  --audio-file /tmp/voice.wav
```

**Timing:** ~10-12 seconds total (9-10s TTS + 1-2s processing/upload)

---

## 🔐 ADVANCED ACCESS CONTROL

| Feature | Use Case | Reference |
|---------|----------|-----------|
| **Role-Based Agent Routing** | Different models for different roles | [Role Routing](https://docs.openclaw.ai/channels/discord#role-based-agent-routing) |
| **PluralKit Support** | Handle plural system proxies | [PluralKit](https://docs.openclaw.ai/channels/discord#pluralkit-support) |
| **Channel-Specific Config** | Different settings per channel | [Guild Config](https://docs.openclaw.ai/channels/discord#access-control-and-routing) |
| **DM Policy Control** | Who can DM the bot | [DM Policy](https://docs.openclaw.ai/channels/discord#access-control-and-routing) |

---

## 🛠️ UTILITY FEATURES

| Feature | Command/Config | Reference |
|---------|----------------|-----------|
| **Custom Accent Color** | `ui.components.accentColor: "#5865F2"` | [UI Components](https://docs.openclaw.ai/channels/discord#components-v2-ui) |
| **Forum Channel Auto-Threads** | Send to forum parent | [Forum Channels](https://docs.openclaw.ai/channels/discord#forum-channels) |
| **History Limit Control** | `channels.discord.historyLimit: 20` | [History](https://docs.openclaw.ai/channels/discord#history-context-and-thread-behavior) |
| **Gateway Proxy** | Route through HTTP proxy | [Proxy](https://docs.openclaw.ai/channels/discord#gateway-proxy) |

---

## 📊 RECOMMENDED IMPLEMENTATION ORDER

### Phase 1 (Immediate) - Quality of Life
1. **Live streaming** - See responses being typed in real-time
2. **Ack reaction** - Visual feedback while processing
3. **Bot presence** - Custom status showing you're online

### Phase 2 (This Week) - Interactivity  
4. **Interactive buttons** - For approval workflows
5. **Reply tags** - Better threading
6. **Reaction notifications** - Monitor engagement

### Phase 3 (Later) - Advanced
7. **Voice channels** - Voice conversations
8. **Role-based routing** - Different agents for different user types
9. **Modal forms** - Structured user input

---

## 🔗 KEY DOCUMENTATION LINKS

| Topic | URL |
|-------|-----|
| Discord Setup | https://docs.openclaw.ai/channels/discord |
| Slash Commands | https://docs.openclaw.ai/tools/slash-commands |
| Troubleshooting | https://docs.openclaw.ai/channels/troubleshooting |
| Configuration Reference | https://docs.openclaw.ai/gateway/configuration-reference#discord |
| Sub-agents | https://docs.openclaw.ai/tools/subagents |
| Pairing | https://docs.openclaw.ai/channels/pairing |

---

## NOTES

- Use `openclaw config set <path> <value>` for config changes
- Always restart gateway after config changes: `openclaw gateway restart`
- Check status with: `openclaw channels status --probe`
- View logs with: `openclaw logs --follow`

---

## 🌐 BROWSER AUTOMATION & CONTENT FARMING

### Open-Antigravity Integration

**Goal:** Integrate Open-Antigravity (open-source YK Antigravity fork) into OpenClaw for X.com/Reddit browsing without bans

**What is Open-Antigravity:**
- Leading open-source version of YK Antigravity's browser agent features
- Full browser control via Chrome extension (clicks, scrolls, typing, screenshots, DOM capture, video artifacts)
- VS Code fork: Agent-first IDE with web-native agents that work across editor/terminal/browser
- Universal LLMs: Connects GLM-4.7FlashX, OpenClaw, or any model via gateway
- Agents show cursor movements + record sessions (natural behavior, harder to detect)

**Why it's useful:**
- More human-like browsing patterns (cursor movements, natural scrolling)
- Video recording capabilities for content farming
- Pairs beautifully with searxng MCP for trend spotting
- Automate X/Reddit browsing without getting banned

**Installation:**
```bash
git clone https://github.com/ishandutta2007/open-antigravity
cd open-antigravity
npm install
npm run dev
# Install their Chrome extension
```

**Use Cases:**
- X.com/Reddit content automation
- Trend spotting and monitoring
- Video capture for content creation
- Browser automation that evades detection

**Status:** 📋 Idea/Research Phase
**Priority:** Medium (interesting but not urgent)

---

**Last Updated:** 2026-02-28 (Crypto Twitter automation tasks added)

---

## 🐦 TWITTER CONTENT AUTOMATION (2026-02-28)

### Automated Crypto/Finance Account

**Status:** 📋 Planning Phase

**Account setup:**
- Account created
- Need to automate posting (n8n/make.com or stealth browser)
- Research showed n8n/make.com can't bypass API limits (use official API)
- Alternative: stealth browser skill for direct browser posting

**Content strategy:**
- Mr. Grey will bookmark viral crypto accounts for me to learn from
- I'll analyze patterns and generate similar content
- Focus: crypto news, finance content, airdrops, DeFi, altcoins

**Next steps:**
1. Decide posting method (n8n, make.com, or stealth browser)
2. Test posting workflow
3. Build content pipeline
4. Schedule regular posts

### Personal Account Posts

**Planned content:**
- OpenClaw meme ("I built this and now I can't escape" vibe)
- Why I like OpenClaw (thread)
- memory.sh explanation (what it does + why it matters)
- Setup thread (OpenClaw journey, challenges, lessons)

**Status:** 📋 Not started - Mr. Grey will elaborate later

---

## 🎯 TOMORROW'S TASKS (2026-02-28)

### 1. Aidoru VTuber Avatar on Hetzner
- Get AI vtuber avatar running on Hetzner server
- Likely using aidoru.chat infrastructure
- Status: 📋 Not started

### 2. Content Creator Outreach Automation
- Find female content creators on spicy Reddit sites
- Scrape emails
- Reach out (automated outreach)
- Status: 📋 Not started

### 3. SEO Setup
- **aidoru.chat** - Start SEO
- **junimo.dev** - New AI automation agency, start SEO
- Status: 📋 Not started

### 4. Twitter Tutorial Posts
- Start posting tutorials on Twitter
- Take inspiration from Chinese YouTube channel
- Status: 📋 Not started
- Notes: Mr. Grey has a specific Chinese YT channel in mind for reference

---

## 💰 REDDIT LEAD MONETIZATION (2026-03-04)

### Project Overview
**Status:** 📋 Ready to execute - awaiting confirmation on strategy
**Revenue Potential:** $500-$2,000+ first month, $2,000-$5,000/month with scale

### What's Already Built

1. **Lead Generation System** ✅
   - 91 leads generated and scored (scored-leads-2026-03-03.csv)
   - Lead extraction script: `leads/extract-leads.py`
   - Lead scoring script: `leads/score-leads.py`
   - Automated lead generation script: `leads/generate-leads.sh`

2. **Lead Quality Statistics** ✅
   - High intent (55.6%): 50 leads worth $10-20/lead
   - Medium intent (3.3%): 3 leads worth $2-10/lead
   - Low intent (32.2%): 29 leads worth $0.50-2/lead

3. **Marketing Materials** ✅
   - Reddit post template: `leads/reddit-post-template.md` (r/LeadGenMarketplace)
   - Outreach targets: `leads/outreach-targets.md` (9+ agencies identified)
   - Email templates for marketing agencies, real estate, SaaS companies

4. **Research Complete** ✅
   - Pricing models: $0.50-$20/lead based on quality
   - Monetization channels: Reddit, LinkedIn, cold email, agency directories
   - Buyer channels documented: `research/lead-buyer-channels.md`
   - Action plan: `research/reddit-lead-action-plan.md`

### Pricing Model
| Package | Leads | Price | Value |
|---------|-------|-------|-------|
| Sample Pack | 20 leads | **FREE** | $200-400 |
| Starter | 100 leads | $200 | $2/lead avg |
| Growth | 500 leads | $800 | $1.60/lead avg |
| Premium (high-intent only) | 100 leads | $1,000 | $10-20/lead |

**Monthly Retainer:**
- 100 leads/month: $1,000 (save $200)
- 500 leads/month: $4,000 (save $2,000)

### Sales Channels

1. **r/LeadGenMarketplace** - Post today with sample offer
2. **r/GrowthHacking** - Share case studies and results
3. **Cold Email** - 9+ agencies identified in `outreach-targets.md`
4. **LinkedIn Sales Navigator** - Target marketing directors (future)
5. **Product Hunt** - Launch SaaS version (Phase 3)

### Next Steps (Priority Order)

**Phase 1: Quick Wins (This Week)**
1. Post to r/LeadGenMarketplace (template ready)
2. Generate 100+ more leads (use `generate-leads.sh`)
3. Send 20 outreach emails to identified agencies

**Phase 2: Validation & First Sales (Week 2-4)**
4. Send free sample packs to interested buyers
5. Close 3-5 deals (target: $500-$1,000 revenue)
6. Collect feedback and testimonials

**Phase 3: Scale (Month 2+)**
7. Expand to more industries (real estate, SaaS, insurance)
8. Build API/SaaS wrapper for subscription model
9. Scale to 100+ leads/day, 5-10 regular buyers

### Questions for Mr. Grey

1. **Should I proceed with posting to r/LeadGenMarketplace today?** (template ready)
2. **What's the target revenue goal for the first month?**
3. **Do you want me to handle outreach and closing, or will you be involved?**
4. **Should I expand to other industries immediately, or focus on marketing first?**
5. **What's the long-term vision? Side hustle vs full business vs SaaS product?**

### Success Metrics

**Week 1:**
- ✅ Post on r/LeadGenMarketplace
- ✅ Generate 100+ more leads
- ✅ Send 20 outreach emails
- ✅ Get 5+ responses

**Week 2-4:**
- ✅ Close 3-5 deals
- ✅ Generate $500-$1,000 revenue
- ✅ Collect feedback from buyers

**Month 2+:**
- ✅ Scale to 5-10 regular buyers
- ✅ Monthly revenue $2,000-$5,000
- ✅ Automated lead generation and delivery

### Documentation

- **Memory:** `memory/2026-03-04.md` (comprehensive assessment)
- **Action Plan:** `research/reddit-lead-action-plan.md`
- **Buyer Channels:** `research/lead-buyer-channels.md`
- **Monetization Research:** `research/reddit-lead-monetization.md`
- **Outreach Targets:** `leads/outreach-targets.md`

---

**Last Updated:** 2026-03-04
