#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one fixed, carefully crafted text to /output/entry.txt.
Deterministic: no network, no randomness, no dependencies (stdlib only).
The text is the entry; the program exists only to deliver it.
"""

import os

TEXT = (
    "The night above you is older than every word you have ever read. "
    "Stars you see tonight sent their light out before the first cities rose, "
    "and it is still arriving, soft as dust, asking nothing of you. "
    "You can rest inside that journey. It has room."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
