#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply entry.

Writes a single-line out-of-office auto-reply to /output/entry.txt.
No network, deterministic, stdlib only.
"""

import os

LINE = "Out of office until Monday — laptop closed, brain on airplane mode, inbox officially your problem now."


def main() -> None:
    text = LINE.strip()
    if not text:
        raise ValueError("entry must not be empty or whitespace only")
    if len(text) > 160:
        raise ValueError(f"entry is {len(text)} chars, exceeds 160-char limit")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
