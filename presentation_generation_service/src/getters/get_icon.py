import torch
from constants import EMBEDDED_ICONS, INDEXATED_ICONS, SBERT_TOKENIZER, SBERT_VECTORIZER

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return sum_embeddings / sum_mask

def get_icon(text: str):
    encoded_input = SBERT_TOKENIZER([text], padding=True, return_tensors='pt')
    with torch.no_grad():
        model_output = SBERT_VECTORIZER(**encoded_input)
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask']).repeat(EMBEDDED_ICONS.shape[0], 1)
    print(sentence_embeddings.shape, EMBEDDED_ICONS.shape)
    res = torch.nn.functional.cosine_similarity(sentence_embeddings, EMBEDDED_ICONS)
    return INDEXATED_ICONS[str(res.argsort()[-1].item())]
