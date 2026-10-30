from pathlib import Path

FRAMES_FOLDER = Path("data/frames")

deleted_count = 0

for image_file in FRAMES_FOLDER.rglob("*.jpg"):
    image_file.unlink()
    deleted_count += 1

print(f"Deleted {deleted_count} frame files")