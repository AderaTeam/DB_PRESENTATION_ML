import json
import pandas as pd
import requests
from constants import LANGUAGE, TOPIC_MODELLING_SERVICE_LINK

def get_topics_comutator(texts: list[str], max_num_of_topics: int | None = None) -> pd.DataFrame:
    session = requests.Session()
    session.trust_env = False
    print(texts)
    print(max_num_of_topics)
    data = json.dumps({
        'texts': texts,
        'language': LANGUAGE,
        'max_num_of_topics': max_num_of_topics,
        "min_topic_size": 2,
        "top_tokens": 5
    }, ensure_ascii=False)
    print(data)
    data = session.post(url=TOPIC_MODELLING_SERVICE_LINK + '/topic_moddeling', 
    data=data, 
    verify=False)
    print('RES:', data.status_code)
    d = json.loads(data.content.decode('utf-8'))
    print(d)
    return pd.DataFrame.from_dict(d)