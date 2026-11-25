#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a "To:" line naming who it was meant for, then the unsent message
itself, one line, exactly as it was typed. No network, no clock,
no randomness -- the same bytes every run.
"""

import os
from pathlib import Path

# The confession. The reason it stayed in drafts is felt in the words,
# not stated: too kind to take away the proudest she's ever looked.
CONFESSION = (
    "To: Mum\n"
    "I never told you the scholarship said no, because the way you told "
    "the whole street I got in is the proudest I've ever seen you, and I "
    "don't know how to take that away.\n"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()
