# from pydantic_settings import BaseSettings, SettingsConfigDict, Field
from os import getenv
from dotenv import load_dotenv

load_dotenv()

MAIN_MODEL_URL: str = str(getenv('MAIN_MODEL_URL'))
API_KEY: str = str(getenv('API_KEY'))
SECRET_KEY: str = str(getenv('SECRET_KEY'))
AUTH_HEADERS = {
    'X-Key': f'Key {API_KEY}',
    'X-Secret': f'Secret {SECRET_KEY}',
}
