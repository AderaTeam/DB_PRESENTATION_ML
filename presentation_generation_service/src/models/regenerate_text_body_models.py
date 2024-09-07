from pydantic import BaseModel

class ReGenerateTextBodyModel(BaseModel):
    context: str
    additional_info: str = ""
