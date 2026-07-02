from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState
from services.gemini_service import GeminiService
from config.settings import settings


class ImageAnalyzerAgent(BaseAgent):

    def __init__(self):
        self.gemini = GeminiService()

    def execute(self, state: PipelineState):

        print("\nAnalyzing Images...\n")

        images = state.selected_images[:settings.MAX_IMAGES_TO_ANALYZE]

        for image in images:

            try:

                result = self.gemini.analyze_image(
                    image.file_path
                )

                image.description = result

                print(image.file_name)
                print("-" * 50)

            except Exception as e:

                print(f"Skipped {image.file_name}")
                print(e)
                print("-" * 50)

                continue

        state.logs.append(
            f"{len(images)} images analyzed"
        )

        return state