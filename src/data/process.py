from pathlib import Path
from PIL import Image
import uuid

INPUT_DIRS = [
    Path("../../data/raw/d1/images"),
    Path("../../data/raw/d2/images"),
]

OUTPUT_DIR = Path("../../data/raw/processed")

VALID_EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}

# Allow very large images (disables decompression bomb protection)
Image.MAX_IMAGE_PIXELS = None

def random_suffix(n: int = 8) -> str:
    """Return a short random hex string, e.g. 'a3f9d21c'."""
    return uuid.uuid4().hex[:n]

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for in_dir in INPUT_DIRS:
        dataset_name = in_dir.parent.name  # "d1" or "d2"

        for path in in_dir.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in VALID_EXTS:
                continue

            # base name: prefix with dataset to avoid collisions
            base_name = f"{dataset_name}_{path.stem}"

            out_path = OUTPUT_DIR / f"{base_name}.png"

            img = Image.open(path)

            # Keep 16-bit images as 16-bit, otherwise convert to RGB
            if img.mode in ("I;16", "I"):
                # Pillow will preserve 16-bit when saving PNG
                img.save(out_path, format="PNG", compress_level=9)
            else:
                # For grayscale/RGB/RGBA etc.
                if img.mode not in ("RGB", "RGBA"):
                    img = img.convert("RGB")
                img.save(out_path, format="PNG", compress_level=9)

            print(f"{path} -> {out_path}")

if __name__ == "__main__":
    main()