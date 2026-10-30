from pathlib import Path
import cv2

# Input folders
CAMERA_2FT = Path("data/camera_2_feet")
CAMERA_4FT = Path("data/camera_4_feet")

# Output folders
FRAMES_2FT = Path("data/frames/camera_2_feet")
FRAMES_4FT = Path("data/frames/camera_4_feet")

FRAMES_2FT.mkdir(parents=True, exist_ok=True)
FRAMES_4FT.mkdir(parents=True, exist_ok=True)


def extract_frames(video_folder, output_folder):

    videos = list(video_folder.glob("*.MP4"))

    print(f"\nFound {len(videos)} videos in {video_folder.name}")

    for video_path in videos:

        print(f"Processing {video_path.name}")

        cap = cv2.VideoCapture(str(video_path))

        frame_count = 0
        saved_count = 0

        while True:

            success, frame = cap.read()

            if not success:
                break

            # Save every 100th frame
            if frame_count % 100 == 0:

                filename = (
                    output_folder /
                    f"{video_path.stem}_frame_{saved_count:03d}.jpg"
                )

                cv2.imwrite(str(filename), frame)

                saved_count += 1

            frame_count += 1

        cap.release()

        print(f"  Saved {saved_count} frames")


# Run extraction for both folders
extract_frames(CAMERA_2FT, FRAMES_2FT)
extract_frames(CAMERA_4FT, FRAMES_4FT)

print("\nFinished.")