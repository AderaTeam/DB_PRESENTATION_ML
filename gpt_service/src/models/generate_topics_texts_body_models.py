from pydantic import BaseModel


class GenerateTopicsTextsBodyModel(BaseModel):
    texts: dict[str, str]
    max_new_tokens: int = 2048
    temperature: float = 0.6
    top_p: float = 0.9

