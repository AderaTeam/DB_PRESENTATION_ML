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
