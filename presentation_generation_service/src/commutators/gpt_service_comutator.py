import requests
from constants import TOPIC_MODELLING_SERVICE_LINK


def get_topics_comutator(texts: list[str]) -> list[str]:
    session = requests.Session()
    session.trust_env = False
    print(texts)
    data = session.post(url=TOPIC_MODELLING_SERVICE_LINK + '/topic_moddeling', data={
        'texts': texts,
        'max_new_tokens': 2024,
        'temperature': 0.6,
        'top_p': 0.9
    }, verify=False)
    print('RES:', data.status_code)
    return data.content