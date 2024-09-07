import pandas as pd
from constants import NLP_LIGHTFULL_MODEL, PUNCTUATION
from commutators.gpt_service_comutator import get_gpt_comutator

def get_numeric_data(df: pd.DataFrame):
    k = None
    t = []
    d = df.copy()
    for i in range(d.shape[0]):
        if k == None:
            if d.iloc[i, 1] == "nummod":
                k = i
                d.iloc[i, 1] = '-'
                t.append(d.iloc[i, 0])
        elif d.iloc[i, 0].text == d.iloc[k, 2]:
            k = i
            d.iloc[i, 1] = '-'
            t.append(d.iloc[i, 0])
    return t


def lightfull_getting_stats(context: str) -> list[str]:
    l = []
    for text_i in context.split('. '):
        d = pd.DataFrame(map(lambda a: (a, a.dep_, a.head.text, ), NLP_LIGHTFULL_MODEL(text_i)))
        n = get_numeric_data(d)
        if len(n):
            l.append(' '.join(map(lambda a: str(a), n)))
    return l


def get_hard_stats_data(context: str) -> list[str]:
    for text_i in context.split('.'):
        res = get_gpt_comutator(f'Выдели численные харрактеристики из текста: {text_i}', max_new_tokens=100)
        res = list(map(lambda a: a.translate(str.maketrans('', '', PUNCTUATION)), res.split('\\\\n\\\\n1.')[1:]))
        data = []
        for j in res:
            sv = j
            n = []
            for k in NLP_LIGHTFULL_MODEL(j):
                if k.dep_ == 'nummod':
                    ks = k.text
                    sv = sv.replace(ks, '')
                    n.append(ks)
            data.append((' '.join(n), sv))
    return data
                



        
