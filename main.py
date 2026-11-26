"""Entry for make.fun competition: u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

UNSENT = "last message unsent: 'sleep well.' he closed the lid before it sent. "
AFTERMATH = "it is still the truest thing in my outbox."

ENTRY = UNSENT + AFTERMATH


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
