# Forex Trading Prototype - ABANDONED (2026-02-28)

**Status:** ⛔ **PROJECT ARCHIVED - IBKR ILLEGAL IN INDIA**

---

## Quick Summary

**Reason for Abandonment:**
- IBKR is illegal in India
- `ib_async` library has severe event loop conflicts in Docker
- Multiple attempts to fix failed

**Action:** Moved to `projects/forex-trading/` for reference

---

## What Was Built

### ✅ Working Components
- **Data Ingestor** - EODHD integration, CSV storage
- **MA Crossover Strategy** - 50/200 signals, working
- **Coordinator** - Async multi-agent orchestration
- **TCP Connection** - Verified to Tailscale gateway

### ⚠️ Broken Components
- **IBKR Executor** - ib_async library event loop issues, protocol incompatibility

---

## Files

**Location:** `/home/node/.openclaw/workspace/projects/forex-trading/`

```
projects/forex-trading/
├── forex-prototype/
│   ├── data_ingestor.py      # ✅ Works
│   ├── ma_strategy.py          # ✅ Works
│   ├── ibkr_executor.py        # ❌ Broken (IBKR illegal in India)
│   ├── coordinator.py          # ✅ Works (async orchestration)
│   ├── README.md              # ✅ Complete documentation
│   ├── requirements.txt         # ✅ Dependencies
│   └── MEMORY.md             # Lessons learned
├── ABANDONED.md             # Project archive notes
└── requirements.txt
```

---

## Lessons

### 🇮🇳 Country Restrictions are Real
**Lesson:** Always verify broker's geographic availability BEFORE building.

- **OANDA:** ❌ Blocked in India
- **IBKR:** ❌ Illegal in India
- **MetaApi:** ✅ Works with MT4/MT5 brokers in India

### 🐛 IBKR Library Issues
`ib_async` library has event loop conflicts in Docker. Not reliable for production use.

### 📦 For Future Projects
**Use MetaApi** - Cloud-based, works with MT4/MT5 brokers in India
- No local gateway needed
- REST + WebSocket APIs
- Production-tested and stable

---

## Next Steps

For new forex trading in India, research:
1. MetaApi with Indian MT4/MT5 brokers
2. Zerodha (India-based broker)
3. Local India-based brokers with APIs

---

## Time Investment

- Research: 1 hour
- Architecture: 30 minutes
- Implementation: 2.5 hours
- IBKR debugging: 1.5 hours
- **Total:** ~5 hours

---
