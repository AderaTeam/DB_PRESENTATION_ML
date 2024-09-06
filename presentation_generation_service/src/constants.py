import spacy
from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOPIC_MODELLING_SERVICE_LINK = str(getenv('TOPIC_MODELLING_SERVICE_LINK'))
NLP_LIGHTFULL_MODEL = spacy.load("ru_core_news_sm")
LANGUAGE = 'russian'