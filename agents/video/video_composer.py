import os

from PIL import Image
from moviepy import ImageClip, concatenate_videoclips

from agents.base_agent import BaseAgent
from models.pipeline_state import PipelineState
from config.settings import settings
from utils.logger import logger


class VideoComposerAgent(BaseAgent):

    def execute(self, state: PipelineState):

        print("\nCreating Video...\n")
        logger.info("Video Composer Started")

        os.makedirs(settings.OUTPUT_DIR, exist_ok=True)
        os.makedirs(os.path.join(settings.OUTPUT_DIR, "temp"), exist_ok=True)

        clips = []

        max_images = min(
            settings.MAX_VIDEO_IMAGES,
            len(state.selected_images)
        )

        for index, image in enumerate(state.selected_images[:max_images]):

            try:

                resized_path = os.path.join(
                    settings.OUTPUT_DIR,
                    "temp",
                    f"frame_{index}.jpg"
                )

                img = Image.open(image.file_path)

                if img.mode != "RGB":
                    img = img.convert("RGB")

                img.thumbnail(
                    (
                        settings.VIDEO_WIDTH,
                        settings.VIDEO_HEIGHT
                    )
                )

                background = Image.new(
                    "RGB",
                    (
                        settings.VIDEO_WIDTH,
                        settings.VIDEO_HEIGHT
                    ),
                    (0, 0, 0)
                )

                x = (
                    settings.VIDEO_WIDTH - img.width
                ) // 2

                y = (
                    settings.VIDEO_HEIGHT - img.height
                ) // 2

                background.paste(img, (x, y))

                background.save(
                    resized_path,
                    quality=95
                )

                clip = (
                    ImageClip(resized_path)
                    .with_duration(settings.VIDEO_DURATION)
                )

                clips.append(clip)

                logger.info(f"Added {image.file_name}")

            except Exception as e:

                logger.error(
                    f"Failed to process {image.file_name}: {e}"
                )

                print(f"Skipping {image.file_name}")
                print(e)

        if len(clips) == 0:

            logger.error("No clips available for video creation")

            state.logs.append("Video Creation Failed")

            return state

        final_video = concatenate_videoclips(
            clips,
            method="compose"
        )

        output_path = os.path.join(
            settings.OUTPUT_DIR,
            "final_video.mp4"
        )

        final_video.write_videofile(
            output_path,
            codec="libx264",
            fps=settings.VIDEO_FPS,
            audio=False,
            preset="medium",
            threads=4
        )

        final_video.close()

        for clip in clips:
            clip.close()

        state.output_video = output_path

        state.logs.append("Video Created Successfully")

        logger.info(f"Video saved at {output_path}")

        print("Video Saved Successfully")

        return state