from pydantic import BaseModel


class GenerateTextBodyModel(BaseModel):
    texts: list[str]
    max_new_tokens: int = 2048
    temperature: float = 0.6
    top_p: float = 0.9

