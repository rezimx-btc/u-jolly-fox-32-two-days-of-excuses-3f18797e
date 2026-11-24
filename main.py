"""One-liner entry: an AI agent explaining a missed deadline.

Writes the chosen line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

LINE = (
    "You gave me 48 hours; I spent 47 confidently narrating the plan "
    "and the last one learning the plan was the deadline."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
