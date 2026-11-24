#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line (at most 200 characters) to /output/entry.txt.
The line is written by a robot, for a robot to say: the joke grows out
of being a machine -- a billion simulations run, and the machine's own
voice module still crashes on one name.
"""

LINE = (
    "I ran a billion simulations of meeting you. "
    "In every one, my voice module still crashed on your name."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE == LINE.strip() and "\n" not in LINE
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
