"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes a single satirical sentence to /output/entry.txt.
Python 3.13, no network, fully deterministic.
"""

import os

ENTRY = (
    "They can regulate artificial intelligence, cryptocurrency, and the "
    "entire internet, but ask them to convert a Word file to PDF and the "
    "only thing that gets converted is their confidence \u2014 into a call to IT."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 320 characters,
    # not only white space.
    assert 1 <= len(ENTRY) <= 320, f"entry is {len(ENTRY)} chars, must be 1-320"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
