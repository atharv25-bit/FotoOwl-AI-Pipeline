from utils.logger import logger
import json

from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState
from services.gemini_service import GeminiService
from config.settings import settings


class ImageAnalyzerAgent(BaseAgent):

    def __init__(self):
        self.gemini = GeminiService()

    def execute(self, state: PipelineState):

        logger.info("Image Analyzer Started")
        print("\nAnalyzing Images...\n")

        images = state.selected_images[:settings.MAX_IMAGES_TO_ANALYZE]

        analyzed_count = 0

        for image in images:

            try:

                result = self.gemini.analyze_image(
                    image.file_path
                )

                data = json.loads(result)

                image.description = data.get(
                    "description", ""
                )

                image.scene = data.get(
                    "scene", ""
                )

                image.emotion = data.get(
                    "emotion", ""
                )

                image.importance = int(
                    data.get("importance", 0)
                )

                analyzed_count += 1

                logger.info(f"Analyzed : {image.file_name}")
                print(f"Analyzed : {image.file_name}")

            except json.JSONDecodeError:

                print(f"Invalid JSON returned for {image.file_name}")

            except Exception as e:

                logger.error(f"Skipped : {image.file_name}")
                print(f"Skipped {image.file_name}")
                print(e)

            print("-" * 60)

        state.logs.append(
            f"{analyzed_count} images analyzed"
        )

        return state