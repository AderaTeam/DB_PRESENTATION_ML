import json
import pandas as pd
import requests
from constants import IMAGE_GENERATION_SERVICE_LINK, LANGUAGE, TOPIC_MODELLING_SERVICE_LINK

def image_generator_comutator(text: str, width: int = 633, height: int = 800, n: int=1):
    session = requests.Session()
    session.trust_env = False
    print(text)
    data = {
        'text': text,
        "session_id": "string",
        "num_of_images": n,
        "width": width,
        "height": height,
    }
    print(data)
    data = session.post(url=IMAGE_GENERATION_SERVICE_LINK + '/generate_image', data=json.dumps(data), verify=False)
    print('RES:', data.status_code)
    return data.json()