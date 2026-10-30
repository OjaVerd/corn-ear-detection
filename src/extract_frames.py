from pathlib import Path
import cv2



# Folder containing videos
VIDEO_FOLDER = Path("data/camera_2_feet")

# Folder where extracted images will be stored
OUTPUT_FOLDER = Path("data/frames")

# Create the folder if it doesn't exist
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Get all mp4 files
videos = list(VIDEO_FOLDER.glob("*.mp4"))

print(f"Found {len(videos)} videos")

# Start with the first video
video_path = videos[0]

print("Processing:", video_path.name)

# Open the video
cap = cv2.VideoCapture(str(video_path))

frame_count = 0
saved_count = 0



while True:

    # Read the next frame
    success, frame = cap.read()

    # Stop when no frames remain
    if not success:
        break

    # Save every 30th frame
    if frame_count % 30 == 0:

        filename = OUTPUT_FOLDER / f"frame_{saved_count:03d}.jpg"

        cv2.imwrite(str(filename), frame)

        saved_count += 1

    frame_count += 1

cap.release()

print(f"Saved {saved_count} frames")