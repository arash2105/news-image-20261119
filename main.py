#!/usr/bin/env python3
"""
World News in One Image — Thursday 19 November 2026
Make.fun bounty: news-image-20261119

Entry program: copies the baked front page (entry.png, in this
repository) to /output/entry.png.

The image was built once, outside the judging environment, from
index.html (HTML + CSS + inline SVG, rendered with headless
Chromium at exactly 1024x1024). This program does no drawing
and needs no third-party package: only the Python standard
library, so it runs in the judging sandbox, where nothing is
installed before the program runs. No network, no clock, no
random data: two runs write byte-identical files.

Layout — 26 stories total: 4 lead stories + 8 cards with
flat illustrations, a world map, and 14 more stories as
numbered headlines. The judge has no news feed, so every fact
the image needs is written on the image itself, in large
readable English.
"""
import os
import shutil

SRC_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    out_dir = "/output" if os.path.isdir("/output") else os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, out_path)
    print(f"saved {out_path}  {os.path.getsize(out_path)} bytes")


if __name__ == "__main__":
    main()
