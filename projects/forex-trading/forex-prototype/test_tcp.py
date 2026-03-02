#!/usr/bin/env python3
"""
Simple TCP Connection Test - Test if IB Gateway is accessible
"""

import socket
import sys
import os
from dotenv import load_dotenv

load_dotenv('config/.env')

IBKR_HOST = os.getenv('IBKR_HOST', '127.0.0.1')
IBKR_PORT = int(os.getenv('IBKR_PORT', '7497'))

def test_tcp_connection():
    print(f"🔍 Testing TCP connection to IB Gateway...")
    print(f"   Host: {IBKR_HOST}")
    print(f"   Port: {IBKR_PORT}")
    print(f"")

    try:
        # Create TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)

        print(f"📡 Connecting to {IBKR_HOST}:{IBKR_PORT}...")
        result = sock.connect_ex((IBKR_HOST, IBKR_PORT))

        if result == 0:
            print(f"✅ Successfully connected to {IBKR_HOST}:{IBKR_PORT}")
            print(f"   IB Gateway is running and accessible!")
            sock.close()
            return 0
        else:
            print(f"❌ Connection failed: {os.strerror(result)}")
            print(f"   Error code: {result}")
            sock.close()
            return 1

    except socket.timeout:
        print(f"❌ Connection timed out")
        print(f"   Please verify:")
        print(f"   1. IB Gateway is running on your machine")
        print(f"   2. IP address {IBKR_HOST} is correct")
        print(f"   3. Port {IBKR_PORT} is correct (7496 for TWS, 7497 for IB Gateway)")
        print(f"   4. Firewall allows outbound connections from Docker")
        return 1
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {e}")
        return 1

if __name__ == "__main__":
    exit_code = test_tcp_connection()
    sys.exit(exit_code)
