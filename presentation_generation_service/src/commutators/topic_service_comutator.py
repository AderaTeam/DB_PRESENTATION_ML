import pandas as pd
import requests
from constants import LANGUAGE, TOPIC_MODELLING_SERVICE_LINK

def get_topics_comutator(texts: list[str], max_num_of_topics: int | None = None) -> pd.DataFrame:
    session = requests.Session()
    session.trust_env = False
    print(texts)
    data = session.post(url=TOPIC_MODELLING_SERVICE_LINK + '/topic_moddeling', data={
        'texts': texts,
        'laguage': LANGUAGE,
        'max_num_of_topics': max_num_of_topics,
        "min_topic_size": 2,
        "top_tokens": 5
    }, verify=False)
    print('RES:', data.status_code)
    return pd.DataFrame.from_dict(data.content)