#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession (a To: line + the unsent line itself)
to /output/entry.txt. Python 3 stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "To: Kak Ardi\n"
    "i broke your guitar back in 2016 and blamed the cat. "
    "i've practiced saying sorry a hundred times and i still can't say it to your face."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
