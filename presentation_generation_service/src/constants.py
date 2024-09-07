import spacy
from os import getenv
from dotenv import load_dotenv
import boto3


load_dotenv()

TOPIC_MODELLING_SERVICE_LINK = str(getenv('TOPIC_MODELLING_SERVICE_LINK'))
IMAGE_GENERATION_SERVICE_LINK = str(getenv('IMAGE_GENERATION_SERVICE_LINK'))
TEXT_GENERATION_SERVICE_LINK = str(getenv('TEXT_GENERATION_SERVICE_LINK'))

NLP_LIGHTFULL_MODEL = spacy.load("ru_core_news_sm")
LANGUAGE = 'russian'
IMAGE_BUCKET_NAME = str(getenv('IMAGE_BUCKET_NAME'))

S3_CLIENT = boto3.client(
    's3',
    endpoint_url = str(getenv('S3_ENDPOINT_URL')),
    aws_access_key_id = str(getenv('S3_AWS_ACCESS_TOKEN_ID')),
    aws_secret_access_key = str(getenv('S3_AWS_ACCESS_KEY')),
)

