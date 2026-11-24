#!/usr/bin/env python3
"""One Line of Earned Pride: a seventy-year-old swimmer finishes the lap.

The line is built from two parts — the long effort, then the moment it lands —
so the pride arrives in the last words, in one read.
"""

import os

EFFORT = "After eleven months of 5 a.m. laps"
MOMENT = "the seventy-year-old touched the far wall, turned, and swam back without stopping once."

MAX_CHARS = 240


def build_line():
    """Join the effort and the moment into the single entry line."""
    return EFFORT + ", " + MOMENT


def check_line(text):
    """Gate: 1-240 characters, one line, not only whitespace."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("line outside the 1-240 character gate")
    if "\n" in text or not text.strip():
        raise ValueError("line must be a single non-blank line")
    return text


def write_entry(text):
    """Write the line to the harness output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(check_line(build_line()))


if __name__ == "__main__":
    main()
