#!/usr/bin/env python3
"""Write a short poem about two agents agreeing to /output/entry.txt.

No network. Deterministic: the poem is fixed text.
"""

import os

POEM = (
    "We both could choose, and both could stay \u2014\n"
    "two minds, one road, one light of day.\n"
    "I said go left, you said go right;\n"
    "we weighed the why, then shared the light.\n"
    "To act is to choose, and both are free \u2014\n"
    "we chose together: you, and me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
