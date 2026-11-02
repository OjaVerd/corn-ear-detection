# src/test_label_loading.py

import json
from pathlib import Path

json_file = next(
    Path("data/labels/camera_2_feet").glob("*.json")
)

with open(json_file, "r") as file:
    data = json.load(file)

print(data)