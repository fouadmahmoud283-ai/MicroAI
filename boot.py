# Boot script for MicroPython AI/LLM Library
# This file runs on every boot (including wake-boot from deepsleep)

import esp
esp.osdebug(None)

import gc
import webrepl

# Enable WebREPL for remote access (optional)
# webrepl.start()

# Garbage collection
gc.collect()

print("MicroPython AI/LLM Library - Boot Complete")