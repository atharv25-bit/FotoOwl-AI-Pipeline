import os

from PIL import Image
from moviepy import ImageClip, concatenate_videoclips

from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState


class VideoComposerAgent(BaseAgent):

    def execute(self, state: PipelineState):

        os.makedirs("output", exist_ok=True)
        os.makedirs("output/temp", exist_ok=True)

        clips = []

        max_images = min(10, len(state.selected_images))

        for index, image in enumerate(state.selected_images[:max_images]):

            resized_path = f"output/temp/frame_{index}.jpg"

            img = Image.open(image.file_path)

            img.thumbnail((1280, 720))

            img.save(resized_path, quality=90)

            clip = ImageClip(resized_path).with_duration(2)

            clips.append(clip)

        if len(clips) == 0:
            state.logs.append("No images available for video")
            return state

        final_video = concatenate_videoclips(
            clips,
            method="compose"
        )

        output_path = "output/final_video.mp4"

        final_video.write_videofile(
            output_path,
            codec="libx264",
            fps=24,
            audio=False,
            threads=4,
            preset="ultrafast"
        )

        state.output_video = output_path

        state.logs.append("Video Created Successfully")

        return state