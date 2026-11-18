#!/usr/bin/env python3
"""make.fun bounty entry: "Sum up 17 November's world news in one image".

Decodes the bundled front-page image (entry.png.b64, base64 text) to
/output/entry.png. The image is stored as base64 text because the
upload path only accepts UTF-8 files. No network access. Deterministic:
decoding fixed text writes the exact same bytes on every run.
"""
import base64
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png.b64")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main():
    with open(SRC, "r", encoding="ascii") as f:
        text = "".join(f.read().split())
    data = base64.b64decode(text, validate=True)
    os.makedirs(DST_DIR, exist_ok=True)
    with open(DST, "wb") as f:
        f.write(data)
    print(f"Wrote {DST} ({len(data)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
