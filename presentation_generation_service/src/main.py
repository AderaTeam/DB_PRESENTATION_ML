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
from getters.get_stats import get_hard_stats_data, lightfull_getting_stats
from getters.get_icon import get_icon
from models.regenerate_text_body_models import ReGenerateTextBodyModel
from commutators.gpt_service_comutator import get_gpt_comutator
from getters.get_external import get_external
from processors.text_processors import lematize_text, split_on_sub_texts
from models.generate_presentation_body_models import GeneratePresentationBodyModel
from models.regenerate_image_body_models import ReGenerateImageBodyModel
from random import random


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
    topics = get_topics_comutator(texts=lematized_text, max_num_of_topics=body.num_of_themes)

    presentation = dict()

    for i in body.exogen_data:
        presentation[i] = dict()
        presentation[i]['slide_type'] = 'CHART'
        presentation[i]['IMAGE'] = get_external(i)

    text_tuples = []
    for i in tqdm(range(topics['Representative_Docs'].shape[0])):
        slide_name = topics['Name'][i]
        presentation[slide_name] = dict()

        context = ' '.join(topics['Representative_Docs'][i])[:15000]
        presentation[slide_name]['context'] = context

        numeric_data = lightfull_getting_stats(context)

        presentation[slide_name]['title'] = get_titles_by_gpt(context)
        text_tuples.append(presentation[slide_name]['title'])
        if len(numeric_data) > 2:
            presentation[slide_name]['numbers_data'] = get_hard_stats_data(context)
            presentation[slide_name]['slide_type'] = 'BIG_NUMBERS'
        else:
            presentation[slide_name]['slide_text'] = get_shorted_text_by_gpt(context)
            text_tuples

            if random() > 0.3:
                text_svg_pairs = dict()
                d = presentation[slide_name]['slide_text'].split('. ')
                if len(d) == 2:
                    presentation[slide_name]['slide_type'] = 'TWO_TEXTS'
                elif len(d) == 3:
                    presentation[slide_name]['slide_type'] = 'THREE_TEXTS'
                for i in d:
                    text_svg_pairs[i] = get_icon(i)
                presentation[slide_name]['text_svg_pairs'] = text_svg_pairs
            else:
                presentation[slide_name]['slide_type'] = 'ONE_IMAGE'
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
        text_tuples.append(presentation[slide_name]['slide_text'])
    
    presentation['HEADER'] = dict()
    presentation['HEADER']['title'] = get_gpt_comutator('Составь очень короткий текст для титульного слайда по следующим темам: ' + ', '.join(text_tuples), 20, 0.7, 0.8)
    print(topics)
    return presentation


@app.post("/regenerate_image")
def generate_image(body: ReGenerateImageBodyModel):
    sub_params = f", и {body.additioanal_text_params}" if body.additioanal_text_params else ""
    img_prompt = (f"Нарисуй изображение c {body.style} стилем{sub_params}: " + body.context)
    images = image_generator_comutator(img_prompt, width=body.width, height=body.height, n=body.n)
    print(images)
    img_names = []
    for image_i in images:
        img_name = str(uuid4()) + '.png'
        im = Image.open(BytesIO(base64.b64decode(image_i)))
        im.save(img_name)
        push_imgs_to_s3(img_name)
        img_names.append(img_name)
        os.remove(img_name)
    return {"images": img_names}


@app.post("/regenerate_text")
def generate_presentation(body: ReGenerateTextBodyModel):
    t = f" - и добавь информациию {body.additional_info}"
    prompt = f"Сократи данный текст: {body.context}{t}"
    reses = []
    for _ in range(5):
        res = get_gpt_comutator(prompt, 1000, 0.7, 0.8)
        reses.append(res)
    return reses


# @app.post("/regenerate_slide")
# def generate_presentation(body: ReGenerateTextBodyModel):
#     t = f" - и добавь информациию {body.additional_info}"
#     prompt = f"Сократи данный текст: {body.context}{t}"
#     reses = []
#     for _ in range(5):
#         res = get_gpt_comutator(prompt, 1000, 0.7, 0.8)
#         reses.append(res)
#     return reses
