import requests
from constants import MAIN_MODEL_URL, AUTH_HEADERS

def get_model_id() -> str:
    response = requests.get(MAIN_MODEL_URL + 'key/api/v1/models', headers=AUTH_HEADERS)
    data = response.json()
    return data[0]['id']