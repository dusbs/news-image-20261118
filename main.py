"""Entry program for the make.fun news-image-20261118 bounty.

Copies the finished image (entry.png, held in this repository) to the
output directory as entry.png. Deterministic: a byte-for-byte copy, no
timestamps, no randomness, no network.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(here / "out")
    dest = Path(out_dir) / "entry.png"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
