from pydantic import BaseModel


class TopicModellingBody(BaseModel):
    texts: list[str]
    language: str
    top_tokens: int = 5
    min_topic_size: int = 2
    max_num_of_topics: int | None = None

    