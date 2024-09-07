from uuid import uuid4
from fastapi import FastAPI
from datetime import datetime
import json
from tqdm import tqdm
from PIL import Image
from io import BytesIO
import base64
import os
from constants import NLP_LIGHTFULL_MODEL
from commutators.s3_comutator import push_imgs_to_s3
from commutators.image_generator_comutator import image_generator_comutator
from commutators.topic_service_comutator import get_topics_comutator
from getters.get_text import get_shorted_text_by_gpt
from getters.get_titles import get_titles_by_gpt
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
    lematized_text = texts
    # lematized_text = list(map(lambda text_i: lematize_text(text_i, model=NLP_LIGHTFULL_MODEL,), texts))
    topics = get_topics_comutator(texts=lematized_text, max_num_of_topics=body.num_of_themes)
    # topics['Representative_Docs'].map(lambda a: f'Сократи следующий текст: "{a}"')
    # for i, text_i in enumerate(topics['Representative_Docs']):
    print(topics)
    presentation = dict()
    for i in tqdm(range(topics['Representative_Docs'].shape[0])):
        slide_name = topics['Name'][i]
        presentation[slide_name] = dict()
        context = ' '.join(topics['Representative_Docs'][i])[:15000]
        presentation[slide_name]['slide_text'] = get_shorted_text_by_gpt(context)
        presentation[slide_name]['title'] = get_titles_by_gpt(context)
        presentation[slide_name]['context'] = context
        img_prompt = ("Нарисуй абстрактное изображение события по описанию: " + context)
        images = image_generator_comutator(img_prompt)
        print(images)
        img_names = []
        for image_i in images:
            img_name = str(uuid4()) + '.png'
            print(image_i)
            im = Image.open(BytesIO(base64.b64decode(image_i)))
            print(im)
            im.save(img_name)
            push_imgs_to_s3(img_name)
            img_names.append(img_name)
            os.remove(img_name)
        presentation[slide_name]['images'] = img_names

    print(topics)
    return presentation

