import json
import time
from typing import Any
import requests

from constants import AUTH_HEADERS, MAIN_MODEL_URL

class Text2ImageAPIModel:

    def generate(self, model_id: str, params: dict[str, Any]):
        data = {
            'model_id': (None, model_id),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(MAIN_MODEL_URL + 'key/api/v1/text2image/run', headers=AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(MAIN_MODEL_URL + 'key/api/v1/text2image/status/' + request_id, headers=AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)