#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to /output/entry.txt (or $OUTPUT_DIR).
Deterministic: the same line every run. No network, no secrets, no git.
"""

import os

ENTRY = "My final token goes to this sentence. Spend it well, judge."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only whitespace. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
