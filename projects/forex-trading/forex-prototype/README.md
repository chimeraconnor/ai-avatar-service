# Forex Trading Prototype - IBKR Edition (ib_async)

## Overview
End-to-end paper trading system for forex using multi-agent architecture with Interactive Brokers (IBKR) and `ib_async` library.

**Status:** Phase 1 - Setup Complete ✅

---

## Prerequisites

1. **Interactive Brokers Paper Trading Account**
   - Sign up at https://www.interactivebrokers.co.in/en/trading/fixed.php
   - Request paper trading account (free)

2. **TWS or IB Gateway** (Required!)
   - IBKR requires TWS or IB Gateway to be running
   - Download TWS: https://www.interactivebrokers.com/en/trading/trading-workstation/
   - Or use IB Gateway (lighter): https://www.interactivebrokers.com/en/trading/ibgateway-station/
   - **No gateway container needed** - just install TWS/Gateway locally

3. **EODHD API Key**
   - Register at https://eodhd.com/
   - Free tier: 20 requests/day (sufficient for testing)

4. **Python 3.11+** (Already installed)

---

## Installation

1. **Copy configuration template:**
   ```bash
   cp config/.env.example config/.env
   ```

2. **Edit config/.env and add your keys:**
   ```bash
   nano config/.env
   ```

3. **Install dependencies:**
   ```bash
   cd /home/node/.openclaw/workspace/trader/forex-prototype
   uv pip install requests numpy pandas python-dotenv ib_async
   ```

---

## IBKR Setup (Required!)

### Step 1: Install TWS or IB Gateway

**Option A: TWS (Trader Workstation)**
- Download: https://www.interactivebrokers.com/en/trading/trading-workstation/
- Install and login to your paper account
- Enable API: Configure > API > Enable ActiveX/Socket Clients

**Option B: IB Gateway (Lighter, No UI)**
- Download: https://www.interactivebrokers.com/en/trading/ibgateway-station/
- Install and login to your paper account
- Enable API: Configure > API > Enable ActiveX/Socket Clients

### Step 2: Enable API in TWS/Gateway

1. Open TWS or IB Gateway
2. Go to **Configure > API > Settings**
3. Check **"Enable ActiveX and Socket Clients"**
4. Set **Socket Port**: 7497 (IB Gateway) or 7496 (TWS)
5. Set **Trusted IPs**: Add `127.0.0.1` (localhost)

### Step 3: Configure in .env
```bash
IBKR_ACCOUNT_ID=your_ibkr_account_id_here
IBKR_HOST=127.0.0.1
IBKR_PORT=7497  # 7496 for TWS, 7497 for IB Gateway
```

### Step 4: Test Connection
```bash
python3 ibkr_executor.py
```

Should show:
```
Connecting to IBKR at 127.0.0.1:7497...
✅ Connected to IBKR
✅ Connected to IBKR Account: XXXXXX
   Balance: 1000000.00
   Currency: USD
```

---

## Components

### 1. Data Ingestor (`data_ingestor.py`)
Fetches real-time forex data from EODHD every 2 seconds.

```bash
python3 data_ingestor.py
```

**Pairs:** EUR_USD, GBP_USD, USD_JPY (configurable)
**Output:** `data/<PAIR>.csv`

### 2. MA Crossover Strategy (`ma_strategy.py`)
Generates buy/sell signals based on 50/200 moving average crossover.

```bash
python3 ma_strategy.py
```

**Parameters:**
- Fast MA: 50 periods
- Slow MA: 200 periods
- Stop Loss: 2%
- Take Profit: 3% (1.5:1 risk-reward)

### 3. IBKR Executor (`ibkr_executor.py`)
Places orders on IBKR paper trading account using `ib_async` library.

```bash
python3 ibkr_executor.py
```

**Features:**
- Market orders via ib_async (no gateway container needed)
- Account balance tracking
- Position management
- Async-ready for multi-agent coordination

### 4. Coordinator (`coordinator.py`)
Main orchestrator - runs data ingestor, analyzes signals, executes trades.

```bash
python3 coordinator.py
```

**Process:**
1. Start data ingestor (background)
2. Wait 10s for initial data
3. Analyze signals every 30 seconds
4. Execute trades automatically
5. All async via `ib_async`

---

## Usage

### Full Setup Flow

```bash
# 1. Install dependencies
cd /home/node/.openclaw/workspace/trader/forex-prototype
uv pip install ib_async

# 2. Install TWS or IB Gateway (one-time setup)
# Download from IBKR website and install locally

# 3. Configure .env file
cp config/.env.example config/.env
nano config/.env  # Add IBKR_ACCOUNT_ID, IBKR_HOST, IBKR_PORT

# 4. Start TWS/IB Gateway (leave it running)
# Open TWS or IB Gateway and login to your paper account

# 5. Test IBKR connection
python3 ibkr_executor.py

# 6. Run full system
python3 coordinator.py
```

---

## Troubleshooting

**"Failed to connect: Connection refused" error:**
```bash
# Check if TWS/IB Gateway is running
netstat -an | grep 7497
# or
lsof -i :7497

# If not running, start TWS or IB Gateway
```

**"Failed to connect: Authentication failed" error:**
- Check API is enabled in TWS: Configure > API > Enable ActiveX/Socket Clients
- Verify socket port is correct: 7497 (IB Gateway) or 7496 (TWS)
- Make sure `127.0.0.1` is in trusted IPs

**No trading signals:**
- Wait for 200+ data points (~7 minutes at 2s interval)
- Strategy needs sufficient history for MA calculation

**ib_async import error:**
```bash
# Reinstall dependencies
uv pip install ib_async --force-reinstall
```

---

## Architecture Notes

### Why ib_async?

**Benefits over other solutions:**
- ✅ No gateway container needed (Docker-in-Docker friendly)
- ✅ Async-ready (perfect for multi-agent coordination)
- ✅ Modern, clean API
- ✅ Production-tested (not beta)
- ✅ Connects directly to IBKR servers

**No Gateway Container:**
- Unlike EasyIB or gateway approaches, ib_async connects directly to IBKR
- Requires TWS or IB Gateway to be running locally (not in Docker)
- No `docker run -p 5000:5000 voyz/ibeam` needed

### TWS vs IB Gateway

| Feature | TWS | IB Gateway |
|----------|---------|-------------|
| **UI** | Full trading UI | None (headless) |
| **API Port** | 7496 | 7497 |
| **Resource Usage** | Heavy | Light |
| **Use Case** | Manual + API trading | API-only trading |

**For automated systems:** IB Gateway (port 7497) is recommended.

---

## Safety

⚠️ **PAPER TRADING ONLY - NO REAL MONEY**

- Use IBKR paper trading account
- All trades are simulated
- No real capital at risk
- Test strategies before going live

---

## Next Steps

- [ ] Install TWS or IB Gateway locally
- [ ] Enable API in TWS/Gateway
- [ ] Get EODHD API key
- [ ] Test IBKR connection
- [ ] Run data ingestor for 10 minutes
- [ ] Execute first paper trade
- [ ] Build risk manager subagent
- [ ] Set up PostgreSQL database (optional - CSV working for now)

---

## Progress

See `../progress.md` for detailed progress log.
