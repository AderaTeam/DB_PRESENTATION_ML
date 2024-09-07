from pydantic import BaseModel

class ReGenerateImageBodyModel(BaseModel):
    context: str
    additioanal_text_params: str = ""
    style: str = ""
    n: int = 5
    width: int = 633
    height: int = 800
