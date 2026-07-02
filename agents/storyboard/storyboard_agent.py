from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState
from services.gemini_service import GeminiService


class StoryboardAgent(BaseAgent):

    def __init__(self):
        self.gemini = GeminiService()

    def execute(self, state: PipelineState):

        descriptions = ""

        for image in state.selected_images:
            if image.description:
                descriptions += image.description + "\n\n"

        if descriptions.strip() == "":
            state.storyboard.append(
                "Storyboard could not be generated because no image descriptions were available."
            )

            state.logs.append("Storyboard Skipped")

            return state

        try:

            storyboard = self.gemini.create_storyboard(
                descriptions
            )

            state.storyboard.append(storyboard)

            state.logs.append("Storyboard Created")

        except Exception as e:

            print("\nStoryboard Generation Failed\n")
            print(e)

            state.storyboard.append(
                "Storyboard generation skipped because Gemini quota was exceeded."
            )

            state.logs.append("Storyboard Skipped")

        return state