from typing import List
from pydantic import BaseModel, Field

from models.image import ImageData


class PipelineState(BaseModel):

    images: List[ImageData] = Field(default_factory=list)
    selected_images: List[ImageData] = Field(default_factory=list)

    storyboard: List[str] = Field(default_factory=list)

    music_path: str = ""
    output_video: str = ""

    logs: List[str] = Field(default_factory=list)