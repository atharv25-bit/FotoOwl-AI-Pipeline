import cv2

from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState


class PhotoSelectorAgent(BaseAgent):

    def blur_score(self, image_path):
        image = cv2.imread(image_path)

        if image is None:
            return 0

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return cv2.Laplacian(gray, cv2.CV_64F).var()

    def brightness_score(self, image_path):
        image = cv2.imread(image_path)

        if image is None:
            return 0

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return gray.mean()

    def execute(self, state: PipelineState):

        scored_images = []

        for image in state.images:

            blur = self.blur_score(image.file_path)

            brightness = self.brightness_score(image.file_path)

            image.score = blur + brightness

            scored_images.append(image)

        scored_images.sort(
            key=lambda x: x.score,
            reverse=True
        )

        state.selected_images = scored_images[:20]

        state.logs.append(
            f"{len(state.selected_images)} best images selected"
        )

        return state