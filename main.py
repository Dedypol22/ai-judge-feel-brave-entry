#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to entry.txt in the output directory (the
MAKEFUN_OUTPUT_DIR environment variable when set, otherwise /output).
The text is a small, steady scene: a night train that keeps its full
stopping ritual at an empty station, then carries its light on into
the dark. Standard library only, no network, exits 0.
"""

import os
import sys

TEXT = (
    "The night train slows for the small station where nobody waits. "
    "The driver still opens the doors, still lets the light fall on the "
    "empty platform, still waits the full minute. Then, unhurried, the "
    "train moves on, carrying its light into the dark."
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def output_path() -> str:
    """Absolute path of the file to write; never depends on the cwd."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    if not os.path.isabs(base):
        base = DEFAULT_OUTPUT_DIR
    return os.path.join(base, OUTPUT_NAME)


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
