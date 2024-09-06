import string


def split_on_sub_texts(text: str) -> list[str]:
    if '<br/>' in text:
        return text.split('<br/>')
    elif '\n' in text:
        return text.split('\n')
    elif '.' in text:
        return text.split('.')
    raise Exception('Gotted unsplitable text')


def lematize_text(text: str, model) -> str:
    doc = model(text)
    tokens = [token.lemma_ for token in doc if token.lemma_ not in model.Defaults.stop_words]
    tokens = [token for token in tokens if token not in string.punctuation]
    tokens = [token for token in tokens if len(token) > 2]
    text= ' '.join(tokens)
    return text
