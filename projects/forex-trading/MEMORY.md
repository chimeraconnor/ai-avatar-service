# Forex Trading Memory - Lessons Learned

## API & Data Lessons

### OANDA Country Restriction (2026-02-28)
**Problem:** OANDA cannot accept new clients from India. Demo account creation is blocked.

**Solution:** Use IBKR (Interactive Brokers) instead.
- IBKR supports India and has paper trading
- IBKR has excellent API with Python wrappers (EasyIB)
- Note: IBKR requires gateway session (Voyz/IBeam docker container)

**Rule:** Always check broker's country restrictions before building prototype. OANDA is not India-friendly.

### IBKR Gateway Session Requirement (2026-02-28)
**Problem:** IBKR API requires a gateway session to be running locally before making API calls.

**Solution:**
1. Run `docker run -p 5000:5000 voyz/ibeam`
2. Gateway listens on http://localhost:5000
3. Python wrapper (EasyIB) connects to gateway, which authenticates with IBKR
4. All API calls go through gateway, not directly to IBKR

**Rule:** IBKR setup is more complex than OANDA. Must have gateway running before any API calls.

## Strategy Lessons
(To be filled as we learn)

## Risk Management Lessons
(To be filled as we learn)

## Common Pitfalls

### Assuming All Brokers Work Globally (2026-02-28)
**Mistake:** Started with OANDA assuming it would work from India.

**Lesson:** Always verify broker's country restrictions first. Different brokers have different geographic limitations.

### Choosing Gateway-Based Solutions in Docker (2026-02-28)
**Mistake:** Started with EasyIB which requires a gateway container (Docker-in-Docker issues).

**Lesson:** In Docker environments, prefer direct API connections (no gateway container). IBKR's `ib_async` is perfect for Docker - connects directly to TWS/Gateway without additional containers.

### EasyIB vs ib_async Decision (2026-02-28)
**Mistake:** Initially chose EasyIB for simplicity, didn't consider Docker constraints.

**Lesson:**
- EasyIB: Requires gateway session (port 5000), problematic in Docker
- ib_async: Direct connection, async-ready, production-tested
- **Use ib_async in Docker environments** - no additional containers needed

---
