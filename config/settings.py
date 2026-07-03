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
        os.getenv("MAX_IMAGES_TO_ANALYZE", 2)
    )

    VIDEO_WIDTH = int(
        os.getenv("VIDEO_WIDTH", 1280)
    )

    VIDEO_HEIGHT = int(
        os.getenv("VIDEO_HEIGHT", 720)
    )

    VIDEO_DURATION = float(
        os.getenv("VIDEO_DURATION", 2)
    )

    VIDEO_FPS = int(
        os.getenv("VIDEO_FPS", 24)
    )

    MAX_VIDEO_IMAGES = int(
        os.getenv("MAX_VIDEO_IMAGES", 10)
    )


settings = Settings()