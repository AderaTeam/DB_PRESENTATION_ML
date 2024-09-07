import json
import requests
from constants import IMAGE_GENERATION_SERVICE_LINK, TEXT_GENERATION_SERVICE_LINK


def get_gpt_comutator(texts: str, max_new_tokens=100, temperature=0.6, top_p=0.9) -> list[str]:
    session = requests.Session()
    session.trust_env = False
    print(texts)
    data = json.dumps({
        'text': texts,
        'max_new_tokens': max_new_tokens,
        'temperature': temperature,
        'top_p': top_p
    })
    data = session.post(url=TEXT_GENERATION_SERVICE_LINK + '/generate_text', data=data, verify=False)
    print('RES:', data.status_code)
    return data.content.decode('utf-8')