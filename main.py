"""make.fun — Make the AI judge happy (ai-happy-01).

Writes one deterministic image to /output/entry.png by copying the
image this repository holds (image.png, 1024x1024, built by
build_image.py). No network, no randomness, no input, no dependencies
beyond the Python standard library.
"""
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parent


def main() -> None:
    src = HERE / "image.png"
    out = Path("/output/entry.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out)


if __name__ == "__main__":
    main()
