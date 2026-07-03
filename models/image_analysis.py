from pydantic import BaseModel


class ImageAnalysis(BaseModel):

    description: str
    scene: str
    emotion: str
    importance: int