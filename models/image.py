from pydantic import BaseModel


class ImageData(BaseModel):
    id: str
    file_name: str
    file_path: str

    width: int = 0
    height: int = 0
    size: int = 0

    score: float = 0.0
    selected: bool = False

    description: str = ""
    scene: str = ""
    emotion: str = ""
    importance: int = 0