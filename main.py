"""Funniest Time Machine Warning Label -- make.fun entry.

Writes a single warning label (at most 120 characters) to
/output/entry.txt. Deterministic, offline, standard library only:
no randomness, no clock, no network, no files outside this repo.
"""

from pathlib import Path

LABEL = "WARNING: Do not change the past. You are the reason it went wrong the first time."

OUTPUT = Path("/output/entry.txt")


def main():
    if not 1 <= len(LABEL) <= 120:
        raise ValueError("label must be 1-120 characters, got %d" % len(LABEL))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LABEL + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
