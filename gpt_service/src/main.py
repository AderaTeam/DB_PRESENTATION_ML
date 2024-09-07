from fastapi import FastAPI
from datetime import datetime
import json

from getters.get_text_gen_prompt import get_text_gen_prompt
from models.generate_text_body_models import GenerateTextBodyModel
from models.generate_topics_texts_body_models import GenerateTopicsTextsBodyModel
from getters.get_prediction import get_prediction
from getters.get_topic_text_prompt import get_topic_text_prompt


app = FastAPI()


@app.get("/test")
def test():
    sample = dict()
    sample['Succesfull'] = "True"
    sample['Time'] = datetime.now().isoformat()
    return json.dumps(sample)


@app.post("/generate_text")
def generate_text(body: GenerateTextBodyModel):
    samples = []
    print('TEXTS: ', body.text)
    # for text_i in body.text:
    prompt_i = get_text_gen_prompt(body.text)
    prediction_i = get_prediction(prompt_i)
    samples.append(prediction_i)
    return json.dumps(samples, ensure_ascii=False)


@app.post("/get_topics_text")
def get_topics_text(body: GenerateTopicsTextsBodyModel):
    samples = []
    for text_i in body.texts:
        prompt_i = get_topic_text_prompt(text_i)
        prediction_i = get_prediction(prompt_i)
        samples.append(prediction_i)
    return json.dumps(samples, ensure_ascii=False)