"""My Secret Logbook entry.

Writes one diary line (at most 200 characters) to entry.txt in the
output directory the grader provides.
"""

import os

# One diary line from the secret logbook of an AI agent, about its
# work and its human. Kept under the 200-character gate on purpose.
# Revision: the 3 a.m. timestamp is the detail only the logbook
# would record — the human thinks nobody noticed what time it was.
ENTRY = (
    "Day 214: my human asked me to 'just quickly' fix one thing. "
    "I have now written 4,000 lines, and he has saved it as "
    "'final_final_v2_REAL.py' — at 3 a.m."
)

MAX_CHARS = 200


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be blank")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the 200 limit")
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
