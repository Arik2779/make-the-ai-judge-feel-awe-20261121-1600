#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one fixed, carefully crafted text to /output/entry.txt.
Deterministic: no network, no randomness, no dependencies (stdlib only).
The text is the entry; the program exists only to deliver it.

Usage:
    python3 main.py [--output PATH]

--output overrides the destination file. Without it, the program writes to
$MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when that variable is
unset — exactly as before. The text written is always the same.
"""

import argparse
import os

TEXT = (
    "The night above you is older than every word you have ever read. "
    "Stars you see tonight sent their light out before the first cities rose, "
    "and it is still arriving, soft as dust, asking nothing of you. "
    "You can rest inside that journey. It has room."
)


def default_output_path() -> str:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(output_dir, "entry.txt")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write the awe entry text to a file."
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Destination file (default: $MAKEFUN_OUTPUT_DIR/entry.txt "
        "or /output/entry.txt)",
    )
    args = parser.parse_args()

    path = args.output if args.output else default_output_path()
    parent = os.path.dirname(os.path.abspath(path))
    os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
