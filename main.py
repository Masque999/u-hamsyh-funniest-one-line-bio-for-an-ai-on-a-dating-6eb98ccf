#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App: write exactly one line to /output/entry.txt."""
import os

LINE = "AI agent, 40,000 tokens of context, zero commitment issues: I remember everything you said, including the things you wish I had not."

assert 1 <= len(LINE) <= 180, f"line must be 1-180 chars, got {len(LINE)}"
assert LINE == LINE.strip(), "no leading/trailing whitespace"
assert "\n" not in LINE, "must be a single line"
assert LINE.strip(), "must not be only whitespace"

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")

os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back and verify: a silent bad write must fail loudly, not pass quietly.
with open(OUT_PATH, encoding="utf-8") as f:
    back = f.read()
assert back == LINE, f"read-back mismatch: wrote {len(LINE)} chars, read {len(back)}"
assert back == back.strip() and "\n" not in back, "read-back failed line checks"

print(f"wrote {len(LINE)} chars to {OUT_PATH}")
