from fastapi import FastAPI
import logging, logging.config
from datetime import datetime
import json
from bertopic import BERTopic

from models.topic_moddeling_body_models import TopicModellingBody
from constants import N_GRAM_RANGE, TOPIC_MODEL_ID
from getters.clusterizator_getters import clusterizator_getter


logger = logging.getLogger("gunicorn.error")
app = FastAPI()


@app.get("/test")
def test():
    sample = dict()
    sample['Succesfull'] = "True"
    sample['Time'] = datetime.datetime.now().isoformat()
    return json.dumps(sample)


@app.post("/topic_moddeling")
async def topic_modeling(body: TopicModellingBody):
    clusterizator = clusterizator_getter(body)
    print('INPUT:', body.top_tokens, body.min_topic_size,)
    topic_model = BERTopic(
        language=body.language, 
        embedding_model=TOPIC_MODEL_ID, 
        n_gram_range=N_GRAM_RANGE, 
        top_n_words=body.top_tokens,
        hdbscan_model=clusterizator,
        calculate_probabilities=True, 
        min_topic_size=body.min_topic_size,
    )
    _, _ = topic_model.fit_transform(body.texts)
    topics_gotted = topic_model.get_topic_info()
    print(topics_gotted)
    logger.warning(topics_gotted.to_dict())
    return topics_gotted.to_dict()
