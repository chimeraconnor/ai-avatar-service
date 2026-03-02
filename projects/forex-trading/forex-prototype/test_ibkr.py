#!/usr/bin/env python3
"""
IBKR Connection Test with nest_asyncio
Uses nest_asyncio to fix event loop conflicts
"""

import sys
import os
import asyncio
from dotenv import load_dotenv
from nest_asyncio import apply

# Apply nest_asyncio patch BEFORE importing ib_async
apply()
from ib_async import IB

load_dotenv('config/.env')

IBKR_ACCOUNT_ID = os.getenv('IBKR_ACCOUNT_ID')
IBKR_HOST = os.getenv('IBKR_HOST', '127.0.0.1')
IBKR_PORT = int(os.getenv('IBKR_PORT', '7497'))

async def test():
    print(f"🔍 Testing IBKR connection...")
    print(f"   Host: {IBKR_HOST}")
    print(f"   Port: {IBKR_PORT}")
    print(f"   Account ID: {IBKR_ACCOUNT_ID or 'Not set (test mode)'}")
    print(f"")

    ib = IB()

    try:
        print(f"📡 Connecting...")
        await ib.connect(
            host=IBKR_HOST,
            port=IBKR_PORT,
            clientId=1,
            timeout=10
        )
        print(f"✅ Connected successfully!")
        print(f"   IB Gateway is running and accessible!")
        print(f"")
        print(f"📝 Next steps:")
        print(f"   1. Set IBKR_ACCOUNT_ID in config/.env with your actual account ID")
        print(f"   2. Run: ./start.sh and select option 4 (full system)")
        print(f"   3. Or run: python3 coordinator.py")
        print(f"")

        await ib.disconnect()
        print(f"✅ Disconnected")
        return 0
    except Exception as e:
        print(f"❌ Failed: {type(e).__name__}: {e}")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(test())
    sys.exit(exit_code)
