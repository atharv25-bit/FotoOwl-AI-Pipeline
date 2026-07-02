from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState
from services.image_service import ImageService
from config.settings import settings


class ImageLoaderAgent(BaseAgent):

    def execute(self, state: PipelineState):

        images = ImageService.load_images(settings.INPUT_DIR)

        state.images = images

        state.logs.append(f"{len(images)} images loaded")

        return state