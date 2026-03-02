#!/usr/bin/env python3
"""
IBKR Paper Trading Executor
Uses ib_async library for direct IBKR connection (no gateway required)
"""

import asyncio
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Apply ib_async patch BEFORE importing ib_async
import ib_async_patch  # This patches util.getLoop()

from dotenv import load_dotenv

load_dotenv('config/.env')

IBKR_ACCOUNT_ID = os.getenv('IBKR_ACCOUNT_ID')
IBKR_HOST = os.getenv('IBKR_HOST', '127.0.0.1')
IBKR_PORT = int(os.getenv('IBKR_PORT', '7497'))

# Now import ib_async - getLoop() is already patched
from ib_async import IB

class IBKRExecutor:
    def __init__(self, account_id, host, port):
        self.account_id = account_id
        self.host = host
        self.port = port
        self.ib = None
        self.connected = False

    async def connect(self):
        """Connect to IBKR TWS or Gateway"""
        print(f"\n📡 Connecting to IBKR at {self.host}:{self.port}...")
        print(f"   Account ID: {self.account_id or 'Not set (test mode)'}")
        print(f"")

        try:
            # Create IB instance
            self.ib = IB()

            # Connect (getLoop() is now patched)
            await self.ib.connect(
                host=self.host,
                port=self.port,
                clientId=1,
                readonly=False,
                timeout=30,  # 30 seconds to establish
                fetchFields=63  # Fetch account data
            )

            # Wait for connection to fully establish
            print(f"⏳ Waiting for IBKR to synchronize account data...")

            # Wait up to 15 seconds for sync
            for i in range(15):
                if self.ib.isConnected():
                    self.connected = True
                    print(f"✅ Connected and synchronized!")
                    return True
                await asyncio.sleep(1)

            print(f"⚠️  Connection established but sync may still be in progress")
            self.connected = True
            return True

        except asyncio.TimeoutError:
            print(f"❌ Connection timed out after 30 seconds")
            print(f"   Please check:")
            print(f"   1. TWS/IB Gateway is running on your machine")
            print(f"   2. API is enabled in TWS: Configure > API > Enable ActiveX/Socket Clients")
            print(f"   3. Socket port is set correctly (7496 for TWS, 7497 for IB Gateway)")
            print(f"   4. Tailscale IP {self.host} is accessible from Docker")
            return False

        except Exception as e:
            print(f"❌ Failed to connect: {type(e).__name__}: {e}")
            print(f"   Please check:")
            print(f"   1. TWS/IB Gateway is running on your machine")
            print(f"   2. API is enabled in TWS: Configure > API > Enable ActiveX/Socket Clients")
            print(f"   3. Socket port is set correctly (7496 for TWS, 7497 for IB Gateway)")
            print(f"   4. Tailscale IP {self.host} is accessible from Docker")
            return False

    async def get_account_info(self):
        """Get account information"""
        if not self.connected:
            print(f"❌ Not connected to IBKR")
            return None

        try:
            # Get account summary
            accounts = await self.ib.get_accounts()

            if accounts and len(accounts) > 0:
                account = accounts[0]
                return {
                    'id': account.account_id,
                    'currency': account.currency,
                    'balance': account.net_liquidation_value,
                    'equity': account.net_liquidation_value,
                    'margin_available': account.available_funds
                }
        except Exception as e:
            print(f"❌ Error fetching account info: {e}")
        return None

    async def get_positions(self):
        """Get current positions"""
        if not self.connected:
            print(f"❌ Not connected to IBKR")
            return []

        try:
            positions = await self.ib.get_positions()
            return positions
        except Exception as e:
            print(f"❌ Error fetching positions: {e}")
            return []

    async def place_market_order(self, symbol, quantity, action='BUY', stop_loss=None, take_profit=None):
        """Place a market order"""
        if not self.connected:
            print(f"❌ Not connected to IBKR")
            return False

        print(f"\n📊 Preparing order...")
        print(f"   Symbol: {symbol}")
        print(f"   Action: {action}")
        print(f"   Quantity: {quantity}")

        try:
            from ib_async.contract import Stock
            from ib_async.order import MarketOrder

            # Create contract (using Stock for simplicity)
            base_currency = symbol.split('_')[0]
            contract = Stock(
                symbol=base_currency,
                currency='USD',
                exchange='SMART'
            )

            # Create market order
            order = MarketOrder(
                action='BUY' if action == 'buy' else 'SELL',
                total_quantity=quantity
            )

            # Submit order
            result = await self.ib.place_order(contract, order)

            if result:
                print(f"✅ Order placed successfully!")
                print(f"   Order ID: {result}")
                return True
            else:
                print(f"❌ Order failed to submit")
                return False

        except Exception as e:
            print(f"❌ Order failed: {type(e).__name__}: {e}")
            # Fallback
            return False

    async def execute_signal(self, signal_data):
        """Execute a trading signal"""
        if not self.connected:
            print(f"❌ Not connected to IBKR - cannot execute signal")
            return False

        pair = signal_data['pair']
        signal = signal_data['signal']
        current_price = signal_data['current_price']
        stop_loss = signal_data.get('stop_loss')
        take_profit = signal_data.get('take_profit')

        print(f"\n{'='*50}")
        print(f"Executing Signal: {signal.upper()} {pair}")
        print(f"{'='*50}")
        print(f"Entry Price: {current_price:.5f}")

        # Position size: 10000 units (0.1 lot) for demo
        quantity = 10000
        action = 'buy' if signal == 'buy' else 'sell'

        success = await self.place_market_order(pair, quantity, action, stop_loss, take_profit)

        return success

    async def get_balance(self):
        """Get account balance and equity"""
        if not self.connected:
            return {
                'balance': 0,
                'equity': 0,
                'margin_available': 0
            }

        account = await self.get_account_info()

        if account:
            return {
                'balance': account.get('balance', 0),
                'equity': account.get('equity', 0),
                'margin_available': account.get('margin_available', 0)
            }
        return {
            'balance': 0,
            'equity': 0,
            'margin_available': 0
        }

    async def close(self):
        """Close IBKR connection"""
        if self.ib and self.connected:
            await self.ib.disconnect()
            self.connected = False
            print("✅ Disconnected from IBKR")

async def test_connection():
    """Test IBKR connection"""

    # Check if IBKR_ACCOUNT_ID is set
    if not IBKR_ACCOUNT_ID or IBKR_ACCOUNT_ID == 'your_ibkr_account_id_here':
        print("⚠️  IBKR_ACCOUNT_ID not set in config/.env")
        print("   For now, we'll test connection without account ID...")
        print("   Please set your actual account ID after we verify connection works.")
        print("")
        account_id = None  # Test without account ID
    else:
        account_id = IBKR_ACCOUNT_ID

    host = IBKR_HOST
    port = IBKR_PORT

    executor = IBKRExecutor(account_id, host, port)

    # Test connection
    print(f"\n{'='*50}")
    print("IBKR Connection Test")
    print(f"{'='*50}")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Account ID: {account_id or 'Not set (test mode)'}")
    print(f"")

    if await executor.connect():
        # Get account info
        account = await executor.get_account_info()

        if account:
            print(f"\n🎉 SUCCESS!")
            print(f"{'='*50}")
            print(f"Account ID: {account.get('id')}")
            print(f"Currency: {account.get('currency')}")
            print(f"Balance: {account.get('balance', 0):.2f}")
            print(f"")
            print(f"📝 Next steps:")
            print(f"   1. Set IBKR_ACCOUNT_ID in config/.env with your actual account ID")
            print(f"   2. Run: ./start.sh and select option 4 (full system)")
            print(f"   3. Or run: python3 coordinator.py")
        else:
            print(f"\n❌ Could not get account info")

    await executor.close()

if __name__ == "__main__":
    # Create new event loop for this script
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        exit_code = loop.run_until_complete(test_connection())
        sys.exit(exit_code)
    finally:
        loop.close()
