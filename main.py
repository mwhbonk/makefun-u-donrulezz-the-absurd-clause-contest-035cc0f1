"""Write one absurd terms-of-service clause to /output/entry.txt.

Deterministic, no network, no dependencies, Python 3.13 stdlib only.
Running the program twice writes byte-identical output: a single
English sentence, well under the 200-character gate.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

CLAUSE = (
    "By accepting these terms, the user grants the Company a perpetual, "
    "royalty-free licence to their dreams, including the right to screen "
    "the embarrassing ones at the annual company party."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(CLAUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
