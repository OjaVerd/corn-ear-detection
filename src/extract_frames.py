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

    total_saved = 0

    for video_path in videos:

        print(f"Processing {video_path.name}")

        cap = cv2.VideoCapture(str(video_path))

        frame_count = 0
        saved_count = 0

        while True:

            success, frame = cap.read()

            if not success:
                break

            # Save every 500th frame
            if frame_count % 500 == 0:

                filename = (
                    output_folder /
                    f"{video_path.stem}_frame_{saved_count:03d}.jpg"
                )

                cv2.imwrite(str(filename), frame)

                saved_count += 1

            frame_count += 1

        cap.release()

        total_saved += saved_count

        print(f"  Saved {saved_count} frames")

    return total_saved


# Process 2-ft videos
total_2ft_frames = extract_frames(
    CAMERA_2FT,
    FRAMES_2FT
)

# Process 4-ft videos
total_4ft_frames = extract_frames(
    CAMERA_4FT,
    FRAMES_4FT
)

# Summary
print("\n===== EXTRACTION SUMMARY =====")

print(f"2-ft frames saved: {total_2ft_frames}")
print(f"4-ft frames saved: {total_4ft_frames}")
print(f"Total frames saved: {total_2ft_frames + total_4ft_frames}")