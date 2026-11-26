"""Painfully honest but polite out-of-office auto-reply, for make.fun.

Writes the entry sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; deterministic: the same sentence every run.
"""

import os

ENTRY = "I am on leave until Monday: your email has joined 300 others in a pile I call tomorrow, and I will get to it with fresh eyes and no promises."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
