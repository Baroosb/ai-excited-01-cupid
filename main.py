"""Copy entry.jpg to output directory as entry.png."""

import os
import shutil


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    shutil.copy("entry.jpg", os.path.join(output_dir, "entry.png"))


if __name__ == "__main__":
    main()
