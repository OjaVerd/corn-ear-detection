from pathlib import Path

FRAMES_2FT = Path("data/frames/camera_2_feet")
FRAMES_4FT = Path("data/frames/camera_4_feet")

LABELS_2FT = Path("data/labels/camera_2_feet")
LABELS_4FT = Path("data/labels/camera_4_feet")

frames_2ft = len(list(FRAMES_2FT.glob("*.jpg")))
frames_4ft = len(list(FRAMES_4FT.glob("*.jpg")))

labels_2ft = len(list(LABELS_2FT.glob("*.json")))
labels_4ft = len(list(LABELS_4FT.glob("*.json")))

print("\n===== PROJECT STATS =====")
print(f"2-ft frames: {frames_2ft}")
print(f"4-ft frames: {frames_4ft}")
print(f"Total frames: {frames_2ft + frames_4ft}")

print()

print(f"2-ft labels: {labels_2ft}")
print(f"4-ft labels: {labels_4ft}")
print(f"Total labels: {labels_2ft + labels_4ft}")