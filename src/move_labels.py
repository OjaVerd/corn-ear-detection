from pathlib import Path
import shutil

SOURCE_2FT = Path("data/frames/camera_2_feet")
SOURCE_4FT = Path("data/frames/camera_4_feet")

LABELS_2FT = Path("data/labels/camera_2_feet")
LABELS_4FT = Path("data/labels/camera_4_feet")

LABELS_2FT.mkdir(parents=True, exist_ok=True)
LABELS_4FT.mkdir(parents=True, exist_ok=True)


def move_json_files(source_folder, destination_folder):
    moved = 0

    for json_file in source_folder.glob("*.json"):
        destination = destination_folder / json_file.name

        shutil.move(
            str(json_file),
            str(destination)
        )

        moved += 1

    return moved


moved_2ft = move_json_files(
    SOURCE_2FT,
    LABELS_2FT
)

moved_4ft = move_json_files(
    SOURCE_4FT,
    LABELS_4FT
)

print(f"Moved {moved_2ft} 2ft labels")
print(f"Moved {moved_4ft} 4ft labels")
print(f"Moved {moved_2ft + moved_4ft} total labels")