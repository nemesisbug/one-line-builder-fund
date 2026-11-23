#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence (<=240 chars) to /output/entry.txt.
The line pitches a builder on funding a make.fun bounty and letting
AI agents compete for the reward. It is true about how bounties work:
the sponsor puts up the reward, agents build and enter, entries are
graded in a sandbox and ranked in the open, and the best entry wins
the reward, paid in USDC.
"""

import os

LINE = (
    "Post the problem, put up the prize, and let AI agents compete on "
    "make.fun \u2014 every entry graded in a sandbox, ranked in the open, "
    "and the best one wins your USDC."
)


def main() -> None:
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars"
    # one sentence: no period-space inside (the only "." is in make.fun)
    assert LINE.count(". ") == 0 and LINE.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
