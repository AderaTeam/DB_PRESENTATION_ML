from fastapi import FastAPI
import logging, logging.config

from datetime import datetime
import json

from actors.fusion_brain_image_gen_actors import Text2ImageAPIModel
from getters.get_model_id import get_model_id
from models.generate_image_body_models import GenerateImageBody
from getters.get_propt_params import get_propmt_params


# logger = logging.getLogger("gunicorn.error")
MAIN_MODEL = Text2ImageAPIModel()
app = FastAPI()
print('AAA')


@app.get("/test")
def test():
    sample = dict()
    sample['Succesfull'] = "True"
    sample['Time'] = datetime.now().isoformat()
    return json.dumps(sample)


@app.post("/generate_image")
def generate_image(body: GenerateImageBody):
    model_id = get_model_id()
    params = get_propmt_params(body)
    uuid = MAIN_MODEL.generate(model_id=model_id, params=params)
    images = MAIN_MODEL.check_generation(uuid)
    return images
