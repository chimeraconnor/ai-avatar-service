#!/usr/bin/env python3
"""
Main Trading Coordinator
Orchestrates data ingestor, strategy, and execution
"""

import os
import sys
import asyncio
import subprocess
from data_ingestor import ForexDataIngestor
from ma_strategy import MovingAverageStrategy
from ibkr_executor import IBKRExecutor
from dotenv import load_dotenv

load_dotenv('../config/.env')

class TradingCoordinator:
    def __init__(self):
        self.pairs = os.getenv('DEFAULT_PAIRS', 'EUR_USD').split(',')

        # Initialize components
        print("Initializing Trading Coordinator...")

        # Strategy (one per pair)
        self.strategies = {
            pair.strip(): MovingAverageStrategy(pair.strip())
            for pair in self.pairs
        }

        # Executor - Use IBKR
        self.executor = None
        account_id = os.getenv('IBKR_ACCOUNT_ID')
        host = os.getenv('IBKR_HOST', '127.0.0.1')
        port = int(os.getenv('IBKR_PORT', '7497'))

        if account_id:
            self.executor = IBKRExecutor(account_id, host, port)
            print("✅ IBKR Executor initialized (using ib_async)")
        else:
            print("⚠️  No executor configured - skipping trade execution")
            print("   Set IBKR_ACCOUNT_ID, IBKR_HOST, IBKR_PORT in config/.env")

        self.running = False

    def start_data_ingestor(self):
        """Start data ingestor in background"""
        print("\nStarting data ingestor in background...")
        ingestor_proc = subprocess.Popen(
            ['python3', 'data_ingestor.py'],
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        print(f"Data ingestor PID: {ingestor_proc.pid}")
        return ingestor_proc

    def analyze_signals(self):
        """Analyze all pairs for trading signals"""
        signals = []

        for pair, strategy in self.strategies.items():
            result = strategy.analyze()

            print(f"\n[{result['timestamp']}] {result['pair']}:")
            print(f"  Signal: {result['signal'] or 'HOLD'}")
            print(f"  Reasoning: {result['reasoning']}")

            if result['signal']:
                signals.append(result)

        return signals

    async def execute_trades(self, signals):
        """Execute trading signals"""
        if not self.executor:
            print("\n⚠️  No executor configured - skipping trade execution")
            return

        # Connect to IBKR
        if not await self.executor.connect():
            print("❌ Failed to connect to IBKR - skipping execution")
            return

        for signal in signals:
            await self.executor.execute_signal(signal)

        await self.executor.close()

    async def run_loop(self, check_interval=30):
        """Main trading loop"""
        self.running = True

        print(f"\n{'='*50}")
        print("TRADING SYSTEM STARTED")
        print(f"{'='*50}")
        print(f"Monitoring pairs: {self.pairs}")
        print(f"Check interval: {check_interval} seconds")
        print(f"Press Ctrl+C to stop\n")

        try:
            while self.running:
                # Analyze signals
                signals = self.analyze_signals()

                # Execute trades
                if signals:
                    print(f"\n⚠️  Found {len(signals)} signal(s) - Executing...")
                    await self.execute_trades(signals)

                # Wait
                await asyncio.sleep(check_interval)

        except KeyboardInterrupt:
            print("\n\nShutting down gracefully...")
            self.running = False
            if self.executor:
                await self.executor.close()

async def main():
    coordinator = TradingCoordinator()

    # Check if data ingestor is already running
    try:
        result = subprocess.run(['pgrep', '-f', 'data_ingestor.py'], capture_output=True)
        if result.returncode == 0:
            print("Data ingestor already running")
        else:
            coordinator.start_data_ingestor()
            print("Waiting 10 seconds for data collection...")
            await asyncio.sleep(10)
    except:
        coordinator.start_data_ingestor()
        print("Waiting 10 seconds for data collection...")
        await asyncio.sleep(10)

    # Start main loop
    await coordinator.run_loop(check_interval=30)

if __name__ == "__main__":
    asyncio.run(main())
