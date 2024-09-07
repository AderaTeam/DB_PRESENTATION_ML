import json
import pandas as pd
import requests
from constants import IMAGE_GENERATION_SERVICE_LINK, LANGUAGE, TOPIC_MODELLING_SERVICE_LINK

def image_generator_comutator(text: str, max_num_of_topics: int | None = None):
    session = requests.Session()
    session.trust_env = False
    print(text)
    data = {
        'text': text,
        "session_id": "string",
        "num_of_images": 1,
        "width": 256,
        "height": 256
    }
    print(data)
    data = session.post(url=IMAGE_GENERATION_SERVICE_LINK + '/generate_image', data=json.dumps(data), verify=False)
    print('RES:', data.status_code)
    return data.json()