import os
from PIL import Image

from models.image import ImageData


class ImageService:

    @staticmethod
    def load_images(input_dir: str):

        images = []

        supported_extensions = (".jpg", ".jpeg", ".png", ".webp")

        for file in os.listdir(input_dir):

            if not file.lower().endswith(supported_extensions):
                continue

            file_path = os.path.join(input_dir, file)

            with Image.open(file_path) as img:
                width, height = img.size

            image = ImageData(
                id=file,
                file_name=file,
                file_path=file_path,
                width=width,
                height=height,
                size=os.path.getsize(file_path)
            )

            images.append(image)

        return images