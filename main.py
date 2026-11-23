#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt. Deterministic, standard library only,
no network, no input read.
"""

import os

LINE = (
    "At 7 a.m. the warung lady slipped an extra krupuk into my bag "
    "and whispered 'for the road' \u2014 I'd never even been there before."
)


def main() -> None:
    # Self-check the house gate before writing: 1-200 characters, not
    # only white space. Fail loudly instead of shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate is 1-200"
    assert LINE.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
