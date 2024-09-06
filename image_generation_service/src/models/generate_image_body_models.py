from pydantic import BaseModel


class GenerateImageBody(BaseModel):
    text: str
    session_id: str
    num_of_images: int = 1
    width: int = 1024
    height: int = 1024

    