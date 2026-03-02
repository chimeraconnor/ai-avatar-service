#!/bin/bash
# Quick Start Script for Forex Trading Prototype (IBKR + ib_async)

echo "🚀 Forex Trading Prototype - Quick Start"
echo "========================================="
echo ""

# Check if .env exists
if [ ! -f "config/.env" ]; then
    echo "❌ Configuration file not found!"
    echo "Copy template and add your API keys:"
    echo "  cp config/.env.example config/.env"
    echo "  nano config/.env"
    exit 1
fi

echo "✅ Configuration file found"
echo ""

# Menu
echo "Select option:"
echo "1) Test data ingestor only"
echo "2) Test strategy only"
echo "3) Test IBKR connection"
echo "4) Run full system (data + strategy + execution)"
echo "5) Check progress"
echo ""
read -p "Enter choice [1-5]: " choice

case $choice in
    1)
        echo "Starting data ingestor..."
        python3 data_ingestor.py
        ;;
    2)
        echo "Running strategy analysis..."
        python3 ma_strategy.py
        ;;
    3)
        echo "Testing IBKR connection..."
        echo ""
        echo "⚠️  IBKR requires TWS or IB Gateway to be running!"
        echo "   1. Install TWS or IB Gateway (not in Docker!)"
        echo "   2. Enable API: Configure > API > Enable ActiveX/Socket Clients"
        echo "   3. Set socket port: 7497 (IB Gateway) or 7496 (TWS)"
        echo ""
        read -p "Press Enter to continue..."
        python3 ibkr_executor.py
        ;;
    4)
        echo "Starting full trading system..."
        python3 coordinator.py
        ;;
    5)
        echo ""
        cat ../progress.md
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac
