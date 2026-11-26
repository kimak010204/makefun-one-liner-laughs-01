#!/usr/bin/env python3
"""One-Liner Laughs rev-2: write a single fresh one-line joke to entry.txt.

Stdlib only. The joke is a fixed string: a setup that promises a prized
heirloom, and a payoff that quietly reveals it was a garage-door prop
for thirty years. Gate enforced here: 1 line, 1-200 chars, not whitespace.
"""

import os
import sys

JOKE = (
    "My grandfather left me his lucky fishing rod in his will \u2014 "
    "he'd spent thirty years using it to prop open the garage door."
)


def main() -> int:
    text = JOKE.strip()
    lines = text.splitlines()
    # Gate: one line, 1-200 chars, not whitespace-only. The em dash is a
    # single character, so the char count below is the gate's count.
    if len(lines) != 1:
        print("gate failed: entry must be exactly one line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print("gate failed: entry must be 1-200 characters", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry must not be only whitespace", file=sys.stderr)
        return 1

    here = os.path.dirname(os.path.abspath(__file__))
    targets = [os.path.join(here, "entry.txt")]
    if os.path.isdir("/output"):
        targets.append("/output/entry.txt")
    for path in targets:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")

    # Round-trip check: read back every target and confirm the bytes match.
    for path in targets:
        with open(path, "r", encoding="utf-8") as fh:
            back = fh.read()
        if back != text + "\n":
            print(f"gate failed: round-trip mismatch in {path}", file=sys.stderr)
            return 1
    print(f"OK: {len(text)} chars -> {targets[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
