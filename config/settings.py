import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GOOGLE_DRIVE_FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID")

    INPUT_DIR = "input"
    OUTPUT_DIR = "output"
    LOG_DIR = "logs"

    MAX_IMAGES_TO_ANALYZE = int(
        os.getenv("MAX_IMAGES_TO_ANALYZE", 5)
    )


settings = Settings()