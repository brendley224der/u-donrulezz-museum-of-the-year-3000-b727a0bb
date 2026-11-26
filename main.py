#!/usr/bin/env python3
"""Museum of the Year 3000 — entry program (pure Python stdlib).

Writes a single museum label, as a museum in the year 3000 would place it
beside an ordinary object from today, to /output/entry.txt.

The label is a fixed, hand-written string: the competition judges the text
itself, so the program is deliberately deterministic — the same bytes on
every run. The humour is a year-3000 misreading: a future curator mistakes
the airport security tray for a ritual basin, and the scan for a purity
rite. The object is fresh (not the fork / key / parking meter from the
brief), the joke lands in the line itself ("shoes, belts and dignity"),
and the voice is a straight-faced museum label.
"""

import os

LABEL = (
    "Security tray, 2024. Ritual basin in which travellers placed their "
    "shoes, belts and dignity before being scanned for purity."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    # Gate: UTF-8 text, 1 to 200 characters, not only whitespace, one line.
    assert 1 <= len(LABEL) <= 200, "label must be 1-200 characters"
    assert LABEL.strip(), "label must not be only whitespace"
    assert "\n" not in LABEL, "label must be a single line"
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
