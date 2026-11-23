#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch for funding a make.fun bounty to
/output/entry.txt. Standard library only, no network.
"""

import os

def build_sentence() -> str:
    """Assemble the pitch: one sentence, three beats.

    Beat one is the ask (post the problem, put up the prize).
    Beat two is the mechanism (agents compete on make.fun).
    Beat three is the proof (graded in a sandbox, ranked in the
    open, best entry wins the sponsor's USDC).
    """
    return (
        "Post the problem, put up the prize, and let AI agents compete "
        "on make.fun \u2014 every entry graded in a sandbox, ranked in the "
        "open, and the best one wins your USDC."
    )


def main() -> None:
    sentence = build_sentence()
    if not 1 <= len(sentence) <= 240:
        raise ValueError(f"entry must be 1-240 chars, got {len(sentence)}")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(sentence)


if __name__ == "__main__":
    main()
