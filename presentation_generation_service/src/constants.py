import string
import pandas as pd
import spacy
from os import getenv
from dotenv import load_dotenv
import boto3
import torch
from transformers import AutoModel, AutoTokenizer
import json

load_dotenv()
with open('../datasets/indexated_icons.json', 'r') as f:
    INDEXATED_ICONS = json.load(f)
EMBEDDED_ICONS = torch.load('../datasets/embedded_icons.pt')
SBERT_TOKENIZER = AutoTokenizer.from_pretrained("ai-forever/sbert_large_nlu_ru")
SBERT_VECTORIZER = AutoModel.from_pretrained("ai-forever/sbert_large_nlu_ru")

TOPIC_MODELLING_SERVICE_LINK = str(getenv('TOPIC_MODELLING_SERVICE_LINK'))
IMAGE_GENERATION_SERVICE_LINK = str(getenv('IMAGE_GENERATION_SERVICE_LINK'))
TEXT_GENERATION_SERVICE_LINK = str(getenv('TEXT_GENERATION_SERVICE_LINK'))

NLP_LIGHTFULL_MODEL = spacy.load("ru_core_news_sm")
LANGUAGE = 'russian'
IMAGE_BUCKET_NAME = str(getenv('IMAGE_BUCKET_NAME'))
EXTERNAL_BUCKET_NAME = str(getenv('EXTERNAL_BUCKET_NAME'))
PUNCTUATION = string.punctuation + '«»'
S3_CLIENT = boto3.client(
    's3',
    endpoint_url = str(getenv('S3_ENDPOINT_URL')),
    aws_access_key_id = str(getenv('S3_AWS_ACCESS_TOKEN_ID')),
    aws_secret_access_key = str(getenv('S3_AWS_ACCESS_KEY')),
)


def get_json_data(d: str) -> pd.DataFrame:
    with open(d) as f:
        return pd.DataFrame(json.load(f))


def get_xlsx_data(d: str) -> pd.DataFrame:
    return pd.read_excel(d)


FILE_PROCESSORS = {
    'json': get_json_data,
    'csv': pd.read_csv,
    'xlsx': get_xlsx_data
}



