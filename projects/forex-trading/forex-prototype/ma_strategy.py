#!/usr/bin/env python3
"""
Simple Moving Average Crossover Strategy
Generates buy/sell signals based on 50/200 MA crossover
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

class MovingAverageStrategy:
    def __init__(self, pair, fast_period=50, slow_period=200):
        self.pair = pair
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.data_dir = "../data"
        self.current_position = None  # None, 'long', 'short'

    def load_data(self, limit=None):
        """Load historical data from CSV"""
        csv_path = os.path.join(self.data_dir, f"{self.pair}.csv")

        if not os.path.exists(csv_path):
            print(f"No data file found for {self.pair}")
            return None

        df = pd.read_csv(csv_path)
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        if limit:
            df = df.tail(limit)

        return df

    def calculate_signals(self, df):
        """Calculate MA and generate signals"""
        if df is None or len(df) < self.slow_period:
            return None, "Not enough data"

        # Calculate moving averages
        df['ma_fast'] = df['mid'].rolling(window=self.fast_period).mean()
        df['ma_slow'] = df['mid'].rolling(window=self.slow_period).mean()

        # Get latest values
        latest = df.iloc[-1]
        prev = df.iloc[-2]

        fast_ma = latest['ma_fast']
        slow_ma = latest['ma_slow']
        prev_fast = prev['ma_fast']
        prev_slow = prev['ma_slow']

        # Crossover detection
        signal = None
        reasoning = ""

        # Golden Cross (fast crosses above slow) -> BUY
        if fast_ma > slow_ma and prev_fast <= prev_slow:
            signal = "buy"
            reasoning = f"Golden cross detected: Fast MA ({fast_ma:.5f}) crossed above Slow MA ({slow_ma:.5f})"

        # Death Cross (fast crosses below slow) -> SELL
        elif fast_ma < slow_ma and prev_fast >= prev_slow:
            signal = "sell"
            reasoning = f"Death cross detected: Fast MA ({fast_ma:.5f}) crossed below Slow MA ({slow_ma:.5f})"

        # Trend continuation
        elif fast_ma > slow_ma:
            reasoning = f"Bullish trend: Fast MA ({fast_ma:.5f}) above Slow MA ({slow_ma:.5f})"
        else:
            reasoning = f"Bearish trend: Fast MA ({fast_ma:.5f}) below Slow MA ({slow_ma:.5f})"

        return signal, reasoning

    def get_entry_exit(self, current_price):
        """Calculate stop-loss and take-profit levels"""
        # 2% stop loss, 3% take profit (1.5:1 risk-reward)
        stop_loss = current_price * 0.98 if self.current_position == 'long' else current_price * 1.02
        take_profit = current_price * 1.03 if self.current_position == 'long' else current_price * 0.97

        return stop_loss, take_profit

    def analyze(self):
        """Run analysis and return signal"""
        df = self.load_data()

        if df is None:
            return {
                'pair': self.pair,
                'timestamp': datetime.now().isoformat(),
                'signal': None,
                'reasoning': 'No data available',
                'current_price': None
            }

        signal, reasoning = self.calculate_signals(df)
        latest_price = df.iloc[-1]['mid']

        result = {
            'pair': self.pair,
            'timestamp': datetime.now().isoformat(),
            'signal': signal,
            'reasoning': reasoning,
            'current_price': latest_price,
            'ma_fast': df.iloc[-1]['ma_fast'],
            'ma_slow': df.iloc[-1]['ma_slow']
        }

        if signal:
            stop_loss, take_profit = self.get_entry_exit(latest_price)
            result['stop_loss'] = stop_loss
            result['take_profit'] = take_profit
            result['risk_reward'] = abs((take_profit - latest_price) / (latest_price - stop_loss))
            self.current_position = 'long' if signal == 'buy' else 'short'

        return result

if __name__ == "__main__":
    # Test the strategy
    strategy = MovingAverageStrategy("EUR_USD")

    result = strategy.analyze()
    print(f"Signal for {result['pair']}:")
    print(f"  Signal: {result['signal']}")
    print(f"  Reasoning: {result['reasoning']}")
    print(f"  Current Price: {result['current_price']}")
    print(f"  Fast MA: {result['ma_fast']}")
    print(f"  Slow MA: {result['ma_slow']}")

    if result['signal']:
        print(f"  Stop Loss: {result['stop_loss']}")
        print(f"  Take Profit: {result['take_profit']}")
        print(f"  Risk/Reward: {result['risk_reward']:.2f}")
