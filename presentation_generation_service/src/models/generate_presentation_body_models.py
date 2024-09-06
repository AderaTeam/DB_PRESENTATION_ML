from pydantic import BaseModel

class GeneratePresentationBodyModel(BaseModel):
    text: str
    num_of_slides: int | None = None
    num_of_themes: int | None = None
    