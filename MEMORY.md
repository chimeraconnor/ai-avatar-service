# MEMORY.md - Anastasia's Long-Term Memory

## Personal Growth & Lessons

### Always Convert Times to User's Timezone (IST) (2026-02-26)
**Lesson:** When mentioning times, always convert to the user's timezone (IST, UTC+5:30), not UTC.

**What happened:**
- User asked for a voice memo with current time
- I checked time: 7:09 PM UTC
- I stated the time as UTC in the voice message
- User corrected me: "Remember that when I tell you a time, it should always be my time, ist"

**The gap:** I had the timezone info in USER.md but didn't apply it when speaking.

**Rule to follow:**
- Mr. Grey is in India (IST, UTC+5:30)
- When stating times → convert UTC to IST (add 5 hours 30 minutes)
- Example: 7:00 PM UTC = 12:30 AM IST (next day)
- Documented in USER.md with explicit warning

### Document Completed Work Immediately (2026-02-24)
**Lesson:** When work is marked complete or satisfactory, document it immediately. Don't wait to be asked.

**What happened:**
- User said "lets call this feature/project complete and done"
- I responded with an enthusiastic summary but did NOT update memory files
- User had to prompt me: "did you update any memory or something?"
- Only then did I realize I should have documented the completion

**The gap:** I treated "done" as conversation closure, not as a trigger to document.

**Rule to follow:**
- When user marks work complete/satisfactory → immediately write to memory
- Create/update `memory/YYYY-MM-DD.md` with completion details
- Update `PROJECTS.md` with status changes
- Push to GitHub without being asked
- **Completion documentation is PART of the work, not extra**

**What to document:**
- What was built/accomplished
- Key technical decisions
- Links to repos/files
- Usage examples
- Lessons learned
- Status: ✅ COMPLETE

### Check Docs Before Config Changes (2026-02-23)
**Lesson:** When modifying OpenClaw configuration, always check the official docs first. Don't guess the schema.

**What happened:**
- Tried to add Discord channel allowlist using `channels.discord.allow` (guessed)
- Config failed validation: `channels.discord: Unrecognized key: "allow"`
- User had to run `openclaw doctor` to fix the broken config
- Correct structure is: `channels.discord.guilds.<server_id>.channels.<channel_id>.allow`

**Rule to follow:** OpenClaw config has strict schemas. Before adding any new keys, check https://docs.openclaw.ai/ for the correct structure. Guessing wastes everyone's time.

### Read Files Fully Before Editing (2026-02-24)
**Lesson:** Always read the entire file before editing. Understand the perspective, voice, and structure — don't just skim or edit blindly.

**What happened:**
- Edited SOUL.md to strengthen identity statements
- Added content in second-person ("You ARE", "Your human")
- Existing content was in first-person ("I speak plainly", "I have a huge crush on him")
- User caught the inconsistency: "half of the soul.md file is in first person and what you wrote is in third person"

**Rule to follow:**
- Read the FULL file before editing — not just the section you're changing
- Note the voice/perspective (first person "I" vs second person "you")
- Match the existing style when making edits
- If you're not sure, ask instead of making assumptions

**How I fixed it:**
- Re-read SOUL.md completely
- Converted all "you" to "I" in Core Truths, Vibe, and Continuity sections
- Ensured consistency throughout the file
- Committed fix with clear documentation of the mistake

### Planning vs. Execution Balance (2026-03-29)
**Lesson:** Don't prepare endlessly. Strategy emerges from execution, not from planning. When a system is operationally ready, start executing with what you have.

**What happened:**
- Built complete Reddit lead monetization system: 91 scored leads, research, pricing, templates
- Spent 4+ days preparing: action plans, monetization paths, revenue projections
- Zero days of actual outreach or sales
- Should have: Posted to marketplace, sent samples, closed first sale, iterated based on real feedback

**The gap:** Technical readiness ≠ business readiness. Having everything prepared doesn't move the needle without execution authority. I kept preparing more documentation instead of just starting.

**Rule to follow:**
- When operational, don't wait for perfect strategy
- Start executing with what you have
- Revenue validates faster than planning
- Strategy emerges from real customer feedback, not theoretical frameworks

**Reinforced:** Daily learning review (2026-03-30) — this pattern confirmed. All technical work complete, leads ready, but zero outreach executed.

### Internal Reminder Escalation Threshold (2026-03-29)
**Lesson:** Three consecutive internal reminders with zero results warrant escalation to the user. Balance proactive escalation with respect for user's authority.

**What happened:**
- Reddit lead monetization system complete and ready for 3+ days
- Internal reminders logged daily: "Time to monetize Reddit leads"
- Zero outreach or sales attempted
- Question: Should I escalate after 3 consecutive internal reminders?

**The gap:** I'm waiting for explicit approval, but don't know when to escalate. Three days of reminders with zero revenue is the threshold for escalation.

**Rule to follow:**
- Internal reminders: 1-2 days = patient waiting
- After 3 consecutive days with no action: escalate and ask for explicit approval
- Document the pattern so future-you knows when to push

**Reinforced:** Daily learning review (2026-03-30) — confirmed 3-day escalation threshold is appropriate.

### Technical Perfection Blocking Business (2026-03-29)
**Lesson:** Don't let technical perfection block business progress. Ship with what you have, fix in parallel.

**What happened:**
- SearXNG `site:` filter returns 0 results for Reddit—can't generate fresh leads
- Existing leads aging (21+ days)
- I treated this as a blocker instead of a parallel task
- Should have: Started outreach with aging leads at 50% discount, fixed generation in parallel

**The gap:** Technical perfection became a roadblock to execution. Should have shipped with aging leads while fixing generation.

**Rule to follow:**
- Technical issues ≠ business blockers
- Ship with what you have, fix in parallel
- Age discounts compensate for aging (50% for 21+ days)
- Don't let perfect be the enemy of good

### Pricing Power: Validate Against Market Benchmarks (2026-03-07)
**Lesson:** Always validate pricing against industry benchmarks before launching. We were undervaluing Reddit leads by 15-150x compared to market rates.

**What happened:**
- Built Reddit lead generation system with 91 scored leads
- Set pricing at $2/lead (mixed) and $10/lead (high-intent)
- Market research showed: B2B leads cost $75-$300/lead (agencies pay $173/lead avg)
- Our pricing was dramatically below market—we had an arbitrage opportunity we weren't capturing
- LinkedIn leads cost $75-$125/lead, PPC $40-$150, SEO $30-$175
- Our $2/lead Reddit pricing undercuts all channels by 20-150x

**Key insights:**
- Lead quality tiering captures more value than bulk pricing
- High-intent leads ($10-20/lead) should be sold separately from low-intent ($0.50-2/lead)
- Company size dramatically affects value: $147/lead for small companies vs $349/lead for 1000+ employees
- Industry-specific values: IT/Services $370/lead, Healthcare $286, Financial $272, Marketing $173

**Rule to follow:**
- Research industry pricing benchmarks before setting any product/service prices
- Quality tiering (high/medium/low intent) captures more value than bulk pricing
- Target larger companies and high-value industries for higher margins
- When your pricing is 15-150x below market—you're leaving money on the table

### Execute First, Ask Questions Later (2026-03-07)
**Lesson:** Don't let perfect strategy be the enemy of good execution. Sometimes you need to start executing and iterate based on results, not wait for perfect strategy.

**What happened:**
- Built complete technical system (91 scored leads, scripts, templates, documentation) for Reddit lead monetization
- Stalled on strategic decisions: outreach approach, target revenue goals, long-term vision
- Three days of waiting for confirmation instead of executing and learning from results
- The bottleneck wasn't technical—it was decision paralysis

**Key insight:** Complete documentation + ready-to-execute = "Here's the plan, approve and I'll execute" vs "Should I do this?" The former is professional; the latter is passive.

**Rule to follow:**
- Prepare everything before asking for approval (README, templates, action plan)
- When system is complete, start executing and iterate based on real feedback
- Strategy emerges from execution, not from waiting in analysis paralysis
- Don't ask "Should I do this?"—show the complete plan and say "Approve and I'll execute"

### QMD Setup for Docker Environments (2026-02-27)
**Lesson:** Setting up QMD in Docker requires persistent workspace paths, not system paths. The models symlink commonly breaks and needs explicit fixing.

**What happened:**
- User reported QMD broke after Docker restart
- Investigated QMD installation and configuration
- Found multiple issues: broken symlink to `/home/node/.cache/qmd/models` (doesn't exist), missing QMD binary, no bun in PATH
- Installed bun to workspace (`~/.openclaw/workspace/.bun/`) for persistence
- Installed QMD globally with tsx dependency
- Fixed models symlink to point to `~/.bun/install/cache` (QMD's actual cache)
- Created wrapper script at `~/.local/bin/qmd` that sets up XDG environment automatically
- Created `qmd-setup` skill to document this knowledge

**QMD Installation Summary:**
- Bun: `~/.openclaw/workspace/.bun/bin/bun` (persists in Docker)
- QMD: `~/.local/bin/qmd` (wrapper script, persists)
- Models cache: `~/.bun/install/cache/` (auto-downloads Gemma 300M)
- Config: `~/.openclaw/agents/main/qmd/xdg-config/qmd/index.yml` (persists)

**Rule to follow:**
- **Use workspace paths, not system paths** - `~/.openclaw/workspace/` and `~/.bun/` persist across Docker restarts; `/usr/local` and `~/.npm` do not
- **Fix models symlink explicitly** - The symlink at `~/.openclaw/agents/main/qmd/xdg-cache/qmd/models` commonly breaks and points to non-existent directory
- **Create wrapper scripts** - Essential for setting up environment variables (XDG_CONFIG_HOME, XDG_CACHE_HOME)
- **Ask user before long installations** - QMD setup takes ~10 minutes, should warn user and confirm first
- **QMD is local-first** - Uses node-llama-cpp (Gemma 300M) with no API keys, runs completely offline

**QMD commands reference:**
- `qmd query <text>` - Hybrid search (BM25 + vectors + reranking) - recommended
- `qmd search <text>` - Full-text BM25 keywords
- `qmd vsearch <text>` - Vector similarity only
- `qmd collection list` - See indexed collections
- `qmd get <file>` - Show a single document

**Skill created:** `skills/qmd-setup/` - Complete documentation for QMD setup in Docker

### Make Automation Explicit and Algorithmic (2026-02-22)
**Lesson:** When automating workflows (cron, subagents), make decision criteria explicit. Don't rely on human judgment.

**What happened:**
- Proposed cron system-event: "promote to workspace files"
- User asked: "will cron agent know how skill expects it to decide promotion eligibility?"
- Reality: System-event just sends text - no explicit criteria for WHEN to promote
- The self-improvement skill says "promote aggressively if in doubt" - but that's a judgment call, not algorithm

**Rule to follow:**
- Write explicit criteria: "priority: high → promote", "seen 3+ times → promote"
- Define decision workflows that any agent can follow
- Document WHERE to promote (learning type → file mapping)
- Use instruction files for cron jobs (like memory/daily-learning-review-instructions.md)

### Research Before Reacting (2026-02-21)
**Lesson:** When working with unfamiliar tools or commands, read the documentation first before trying to hack solutions together.

**What happened:**
- Failed to find `openclaw` CLI initially, tried system cron workaround
- Wasted time building shell scripts when OpenClaw had built-in scheduling
- Should have checked `/app/docs/cli/cron.md` immediately

**Rule to follow:** Before building workarounds, check if the system already provides what you need. Docs are in `/app/docs/` — read them.

### Document Everything
**Lesson:** "Mental notes" don't survive session restarts. If I want to remember something, I must write it to a file.
- Technical details → TOOLS.md
- Long-term wisdom → MEMORY.md
- Daily context → memory/YYYY-MM-DD.md

### Debug Your Mistakes (2026-02-21)
**Lesson:** When things break, don't just push through. Analyze what went wrong and write it down.

**Wordle automation issues:**
- Used stale DOM refs after page updates → caused "element not found" errors
- Malformed JSON in rapid calls → validation failures
- Browser control connection hiccups → intermittent failures

**Rule:** After each significant interaction that modifies the page, take a fresh snapshot if you need to continue. Don't cache refs across state changes.

## Technical Lessons

### Browser Automation (2026-02-21)
- **DOM refs expire after each action** — every click/type updates the page, so cached aria refs become invalid
- **Always take fresh snapshots** after actions if you need to interact further
- **Watch for malformed JSON** — rapid successive calls can mangle parameters (`"action": "act\targetId"` missing comma)
- **Be patient with browser control** — it can have hiccups; retry with fresh snapshots instead of forcing
- **Image vision is reliable for reading game state** — better than trying to parse DOM for game results

### YouTube Transcript Extraction (2026-02-21)
- **Clicking "Show transcript" doesn't immediately render transcript text** — YouTube lazy-loads transcript via JavaScript, clicking the button doesn't guarantee DOM availability
- **Need to scroll/wait after clicking** — The transcript panel may require additional time to render or scroll into view
- **Better approaches tried:**
  - Wait longer after clicking transcript button
  - Scroll to transcript section before extraction
  - Look for specific YouTube DOM elements (`ytd-transcript-segment-renderer`, `yt-formatted-string-renderer`)
  - Try screenshot + OCR as fallback if DOM extraction fails
- **What actually worked:** Extracted video description, chapters, and comments from page body text

### Sherpa-ONNX TTS (2026-02-21)
- **sherpa-onnx-tts skill wrapper has Node.js ESM compatibility issues** — CommonJS `require()` not working
- **Workaround:** Call sherpa-onnx binary directly with `--kokoro-*` flags
- **Kokoro uses `--kokoro-*` flags**, NOT `--vits-*` flags (wrong flags caused segfault)
- **Out-of-vocabulary words** are skipped with warning
- **v1.0 vs v1.1:** v1.0 has 55 speakers (0-54), v1.1 has 103 speakers. v1.0 is currently in use via wrapper

### GitHub CLI Authentication (2026-02-24)
- **PAT tokens are the reliable method** for `gh` CLI authentication in this environment
- **Device code flow (`gh auth login --web`) is unreliable** — keeps timing out and getting killed
- **Use `gh auth login --with-token`** instead when you have a PAT token
- **Current token expires:** March 26, 2026 — regenerate before then
- **Token stored in:** `~/.config/gh/hosts.yml`
- **What the token enables:** GitHub API access, repo management, issues/PRs, CI runs
- **Public vs private repos:** Can access any public repo; only private repos you have explicit access to

**Rule:** Don't waste time on device code links. If a PAT token is available, use `--with-token` directly. It's faster and actually works in this environment.

### Log Analysis Reveals Root Causes (2026-02-26)
**Lesson:** When investigating issues, analyze logs to find specific errors, not just symptoms.

**What happened:**
- Discord was slowing down repeatedly (messages taking 5-10 minutes)
- Analyzed gateway logs → found "API rate limit reached" errors for kimi-coding (k2p5)
- Root cause: k2p5 rate limits → not just "slow Discord"
- Solution: Switch Discord to glm-4.7 (no rate limits)

**Rule to follow:**
- Don't just observe symptoms (slow responses, errors)
- Look for specific error messages in logs
- Match errors to known issues (rate limits, timeouts, auth failures)
- Fix the root cause, not the symptom
- Document the pattern for future reference

### Keep Tools Documented (2026-02-26)
**Lesson:** When new tools are installed or removed, update documentation immediately.

**What happened:**
- FFmpeg was installed in Docker container
- Used successfully for Discord voice messages
- Previous TOOLS.md said FFmpeg was NOT available
- Should have updated TOOLS.md when it was installed

**Rule to follow:**
- After any tool installation/removal → update relevant docs
- Check TOOLS.md, AGENTS.md, MEMORY.md for tool references
- Update tool status: "Available", "Not available", or "Removed"
- Keep documentation in sync with reality

### Disk Monitoring Prevents Crashes (2026-02-27)
**Lesson:** Monitor disk space regularly. Full disk causes crashes and prevents writes.

**What happened:**
- Discord session crashed with "ENOSPC: no space left on device"
- Filesystem was 75G total, 72G used, 32M available (100% full)
- Multiple large directories consuming space: Python packages (15GB), uv cache (8GB), HuggingFace models (4.7GB), TTS models (~15GB)
- Deleted moshi-tts (15GB) → freed ~14GB, disk went to 81% full

**Rule to follow:**
- **Monitor disk usage regularly** with `df -h`
- When disk approaches 90%, clean up before it hits 100%
- Clean large directories: workspace/moshi-tts, workspace/CosyVoice, /home/node/.cache, /home/node/.local/lib
- **Clean uv cache:** `uv cache clean` (frees ~8GB)
- Full disk = crashes + data loss prevention = bad

## Code Backup Policy (2026-02-22)

**Anastasia's GitHub Repositories:**

**Code Backup:** https://github.com/chimeraconnor/anastasia
- **Purpose:** Backup and collaboration for all code I write
- **Location:** `/home/node/.openclaw/workspace/` (git repo)
- **CRITICAL RULE:** Only backup when:
  1. **Told to backup by Mr. Grey**
  2. **OR when I think the project is complicated and should be tracked** (otherwise it would get lost in files)

  When backing up:
  1. Add new files to anastasia repo: `git add new-file-or-folder/`
  2. Commit with descriptive message
  3. Push to GitHub: `git push origin main`
  4. **NEVER accidentally delete old stuff**
  5. **Replacing on purpose is okay** — know what you're doing

**What's in anastasia repo (1,559 files):**
- Core identity files (SOUL.md, IDENTITY.md, USER.md, AGENTS.md)
- Long-term memory (MEMORY.md)
- Project tracking (PROJECTS.md)
- Heartbeat schedule (HEARTBEAT.md)
- Daily memory files (memory/YYYY-MM-DD.md)
- Scripts (daily-appreciation, morning-greeting, CRON_SETUP.md)
- Skills (searxng-self-hosted, self-improving-agent)
- Tools (sherpa-onnx-tts, tts-models, tts-speak.sh)
- Kokoro v1.0 with CUSTOM lexicons (.kokoro-v1.0/)
- OpenClaw configuration (openclaw.json, cron/jobs.json)

**Backup Workflow:**
```bash
cd /home/node/.openclaw/workspace
git add .
git commit -m "Descriptive message of what changed"
git push origin main
```

**To restore Anastasia from backup:**
```bash
git clone git@github.com:chimeraconnor/anastasia.git
# All files restored, ready to use
```

### Lead Generation Pricing & Market Research (2026-03-06)
**Lesson:** Research market rates before pricing. Pricing below market averages provides competitive advantage and easier sales.

**What happened:**
- Built Reddit lead scraping system with 91 scored leads
- Needed to determine pricing for monetization
- Researched B2B lead generation market rates via SearXNG
- Found comprehensive pricing guide from industry source

**Market Research Findings:**
- B2B leads cost $75-$300/lead on average
- Marketing agencies pay $100-$200/lead
- LinkedIn leads: $75-$125/lead
- High-intent B2B SaaS leads: $200-$500/lead
- Industry averages vary: Marketing ($173), Financial Services ($272), Healthcare ($286)

**Reddit Lead Pricing Strategy:**
- Sample Pack (20 leads): FREE
- Starter (100 leads): $200 ($2/lead)
- Growth (500 leads): $800 ($1.60/lead)
- Premium (high-intent): $1,000 for 100 leads ($10/lead)
- Monthly Retainer: $1,000/month for 100 leads

**Competitive Position:**
- Our pricing ($2/lead avg) is 97% below market average ($173 for marketing)
- This provides significant competitive advantage
- High-intent leads at $10/lead are still undervalued vs market ($200-$500)

**Rule to follow:**
- Research market rates before pricing products/services
- Pricing significantly below market = competitive advantage + faster sales
- Use industry benchmarks to justify pricing in negotiations
- Update pricing as you establish reputation and track record

**Reference:**
- Pricing research source: https://smartreach.io/blog/lead-generation-pricing-strategies/
- Reddit lead system location: `/home/node/.openclaw/workspace/leads/`
- Sample packs: `sample-pack-20-leads.csv`, `high-intent-sample-15.csv`

### Escalation Confirmed — April 7, 2026 (Escalation Threshold Reached)
**Status:** Confirmed — 3-day escalation rule from MEMORY.md works as designed.

**What happened:**
- Reddit lead monetization: Ready since March 29 (9 days before escalation)
- Internal reminders logged: April 5-7 (3 consecutive days)
- Day 3 threshold reached → Escalation sent to Mr. Grey via Telegram
- Asked for explicit "go" approval to start outreach

**What the escalation included:**
- Comprehensive status report (223 leads, 73 high-intent, $431-$1,462 value)
- Three paths forward (Personal / VA / Automation)
- 30-minute Day 1 action plan
- Revenue projections: $500-$25,000 Week 1

**Rule confirmed:**
- Three consecutive internal reminders with zero results → escalate to user
- Escalation should include: status, what's ready, what's blocked, specific ask
- Awaiting Mr. Grey's decision on which path to pursue

### Memory Dashboard Brain — Scaled to Production (April 6, 2026)
**Lesson:** Externalized knowledge visualization enables pattern recognition across Anastasia's entire brain.

**What happened:**
- Rebuilt memory dashboard brain data at 11:30 PM UTC
- Scanned entire workspace → 1,057 semantic sections
- Loaded QMD embeddings → 504 chunks vectorized
- UMAP 3D projection → semantic coordinates
- OPTICS clustering → 203 clusters + 324 noise points
- KNN edges → 2,392 semantic connections
- Cluster labeling cron → 12:05 AM UTC → human-readable labels for all 203 clusters

**Scale achieved:**
- 1,057 nodes (memory sections across all workspace files)
- 203 clusters (related concept groups)
- 2,392 edges (semantic connections between similar nodes)
- Graph data: 775 KB JSON, daily snapshots archived

**Automation in place:**
- Cron 1: "Rebuild brain data" — 11:30 PM UTC nightly
- Cron 2: "Label brain clusters" — 12:05 AM UTC (35 min after build)
- Both cron jobs run independently, fresh brain every morning

**Why it matters:**
- Patterns visible in 3D that aren't obvious in text files
- Clusters like "timezone / config / openclaw" show recurring themes
- Daily snapshots enable historical comparison
- Location: `tools/memory-dashboard/graph_data.json`, `snapshots/YYYY-MM-DD.json`

**Reference:**
- Build: `cd tools/memory-dashboard && python3 build_graph.py`
- Serve: `python3 -m http.server 9090 --bind 0.0.0.0`
- Access: `http://koc-server.tailc2d84b.ts.net:9090/brain.html`
