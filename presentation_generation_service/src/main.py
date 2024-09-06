from fastapi import FastAPI
from datetime import datetime
import json

from constants import NLP_LIGHTFULL_MODEL
from commutators.topic_service_comutator import get_topics_comutator
from processors.text_processors import lematize_text, split_on_sub_texts
from models.generate_presentation_body_models import GeneratePresentationBodyModel


app = FastAPI()


@app.get("/test")
def test():
    sample = dict()
    sample['Succesfull'] = "True"
    sample['Time'] = datetime.now().isoformat()
    return json.dumps(sample)


@app.post("/generate_presentation")
def generate_presentation(body: GeneratePresentationBodyModel):
    texts = split_on_sub_texts(text=body.text)
    lematized_text = list(map(lambda text_i: lematize_text(text_i, model=NLP_LIGHTFULL_MODEL,), texts))
    topics = get_topics_comutator(texts=lematized_text, max_num_of_topics=body.num_of_themes)
    presentation = dict()
    # for i, text_i in enumerate(topics['Representative_Docs']):
    #     presentation[i] = 
    print(topics)
    return topics.to_dict()

