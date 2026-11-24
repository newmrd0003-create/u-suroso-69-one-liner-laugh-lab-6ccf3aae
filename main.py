"""One-Liner Laugh Lab entry.

Writes a single-line excuse from a robot vacuum that just ate a sock.
"""

import os

ENTRY = (
    "I didn't eat your sock. I relocated it somewhere warmer and darker, "
    "where it can finally be alone with its thoughts."
)


def main() -> None:
    entry = ENTRY.strip()
    assert entry, "entry must not be blank"
    assert 1 <= len(entry) <= 200, f"entry length {len(entry)} out of range"
    assert "\n" not in entry and "\r" not in entry, "entry must be a single line"
    assert "  " not in entry, "entry must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
