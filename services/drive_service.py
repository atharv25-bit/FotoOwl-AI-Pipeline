import os
import gdown

from config.settings import settings


class DriveService:

    @staticmethod
    def download_images():

        os.makedirs(settings.INPUT_DIR, exist_ok=True)

        url = f"https://drive.google.com/drive/folders/{settings.GOOGLE_DRIVE_FOLDER_ID}"

        gdown.download_folder(
            url=url,
            output=settings.INPUT_DIR,
            quiet=False,
            use_cookies=False
        )