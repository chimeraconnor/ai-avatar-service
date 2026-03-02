#!/usr/bin/env python3
"""
Patch for ib_async library to fix event loop issues in Docker
"""

import asyncio
import sys

# Patch before importing ib_async
import ib_async.util as util

_original_getLoop = util.getLoop

def patched_getLoop():
    """Use asyncio.get_running_loop() instead of get_event_loop_policy()"""
    loop = asyncio.get_running_loop()
    if loop is None:
        # Fallback if no loop is running yet
        loop = asyncio.new_event_loop()
    return loop

# Apply the patch
util.getLoop = patched_getLoop

print(f"✅ ib_async patch applied!")
print(f"   - Fixed getLoop() to use asyncio.get_running_loop()")
print(f"   - This should prevent 'event loop is already running' errors in Docker")
print(f"   - Note: Patch is applied to util.getLoop, IB.connect() should work normally")
