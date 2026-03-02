#!/usr/bin/env python3
"""
Forex Data Ingestor
Fetches real-time forex data from EODHD and stores to CSV
"""

import requests
import pandas as pd
import time
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../config/.env')

EODHD_API_KEY = os.getenv('EODHD_API_KEY')
DEFAULT_PAIRS = os.getenv('DEFAULT_PAIRS', 'EUR_USD').split(',')
TIMEFRAME = os.getenv('DEFAULT_TIMEFRAME', 'S1')

class ForexDataIngestor:
    def __init__(self, api_key, pairs):
        self.api_key = api_key
        self.pairs = pairs
        self.base_url = "https://eodhd.com/api/real-time"
        self.data_dir = "../data"
        os.makedirs(self.data_dir, exist_ok=True)

    def fetch_price(self, pair):
        """Fetch real-time price for a currency pair"""
        try:
            response = requests.get(
                f"{self.base_url}/{pair}",
                params={"api_token": self.api_key, "fmt": "json"}
            )
            response.raise_for_status()
            data = response.json()

            if 'close' in data:
                return {
                    'timestamp': datetime.now().isoformat(),
                    'pair': pair,
                    'bid': data.get('close', {}).get('bid', 0),
                    'ask': data.get('close', {}).get('ask', 0),
                    'mid': (data.get('close', {}).get('bid', 0) + data.get('close', {}).get('ask', 0)) / 2,
                    'volume': data.get('volume', 0)
                }
        except Exception as e:
            print(f"Error fetching {pair}: {e}")
        return None

    def save_to_csv(self, data):
        """Append price data to CSV"""
        df = pd.DataFrame([data])
        csv_path = os.path.join(self.data_dir, f"{data['pair']}.csv")

        # Create new file if doesn't exist
        if not os.path.exists(csv_path):
            df.to_csv(csv_path, index=False)
        else:
            # Append to existing file
            df.to_csv(csv_path, mode='a', header=False, index=False)

    def run(self, interval_seconds=1):
        """Continuous data fetching loop"""
        print(f"Starting data ingestor for pairs: {self.pairs}")
        print(f"Fetching every {interval_seconds} second(s)")
        print(f"Data directory: {self.data_dir}")

        while True:
            for pair in self.pairs:
                data = self.fetch_price(pair)
                if data:
                    print(f"[{data['timestamp']}] {pair}: {data['mid']:.5f}")
                    self.save_to_csv(data)

            time.sleep(interval_seconds)

if __name__ == "__main__":
    if not EODHD_API_KEY or EODHD_API_KEY == "your_eodhd_api_key_here":
        print("ERROR: Please set EODHD_API_KEY in config/.env")
        exit(1)

    ingestor = ForexDataIngestor(
        api_key=EODHD_API_KEY,
        pairs=DEFAULT_PAIRS
    )

    # Run with 2-second interval (EODHD free tier limit)
    ingestor.run(interval_seconds=2)
