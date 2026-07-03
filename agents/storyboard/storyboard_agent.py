from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState
from services.gemini_service import GeminiService
from utils.logger import logger



class StoryboardAgent(BaseAgent):

    def __init__(self):
        self.gemini = GeminiService()

    def execute(self, state: PipelineState):

        print("\nGenerating Storyboard...\n")

        logger.info("Storyboard Agent Started")

        descriptions = ""

        for index, image in enumerate(state.selected_images, start=1):

            if image.description:

                descriptions += (
                    f"Image {index}\n"
                    f"Description : {image.description}\n"
                    f"Scene       : {image.scene}\n"
                    f"Emotion     : {image.emotion}\n"
                    f"Importance  : {image.importance}\n\n"
                )

        if descriptions.strip() == "":

            state.storyboard.append(
                "No valid image analysis found. Storyboard skipped."
            )

            state.logs.append("Storyboard Skipped")

            return state

        try:

            storyboard = self.gemini.create_storyboard(
                descriptions
            )

            state.storyboard.clear()
            state.storyboard.append(storyboard)

            state.logs.append("Storyboard Created")
            logger.info("Storyboard Created")

            print("Storyboard Generated Successfully")

        except Exception as e:

            print("\nStoryboard Generation Failed\n")
            print(e)

            state.storyboard.clear()
            state.storyboard.append(
                "Storyboard generation skipped because the AI service is unavailable."
            )

            state.logs.append("Storyboard Skipped")

        return state