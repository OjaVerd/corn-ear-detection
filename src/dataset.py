from pathlib import Path
import json

from PIL import Image
from torch.utils.data import Dataset


class CornDataset(Dataset):

    def __init__(self, image_dir, label_dir):

        self.image_dir = Path(image_dir)
        self.label_dir = Path(label_dir)

        self.images = sorted(
            self.image_dir.glob("*.jpg")
        )

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):

        image_path = self.images[index]

        label_path = (
            self.label_dir /
            f"{image_path.stem}.json"
        )

        image = Image.open(image_path)

        with open(label_path, "r") as file:
            annotation = json.load(file)

        boxes = []

        for shape in annotation["shapes"]:

            x1, y1 = shape["points"][0]
            x2, y2 = shape["points"][1]

            boxes.append(
                [x1, y1, x2, y2]
            )

        return image, boxes