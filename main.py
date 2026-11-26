# SPDX-License-Identifier: MIT
"""One-line entry: the comment a developer left above fragile production code."""
from pathlib import Path

LINE = "// do not touch: this works because nobody knows why, and the last person who asked is now a farmer."

CAP = 200  # this bounty gates the entry at 1 to 200 characters

if __name__ == "__main__":
    assert 1 <= len(LINE) <= CAP
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")
