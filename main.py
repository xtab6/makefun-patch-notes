#!/usr/bin/env python3
"""Real-Life Patch Notes entry: one deadpan changelog line for a bug in
human biology. Writes the line to /output/entry.txt and exits 0."""

import os

ENTRY = (
    "v4.1.0: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2009 every night at 3 a.m."
)


def main():
    assert len(ENTRY) <= 160, "entry exceeds the 160-character limit"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the *contents* of /output; never remove the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
