#!/usr/bin/env python3
"""The Router Confesses — one-line excuse from a home Wi-Fi router.

Writes the router's confession to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

LINE = "I cut the Wi-Fi at the climax because the killer was about to be named and I refuse to be the only one in this house who doesn't know."


def main() -> None:
    if not (1 <= len(LINE) <= 200) or "\n" in LINE.strip():
        raise SystemExit("entry line fails the 1-200 char single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
