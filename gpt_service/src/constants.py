import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

MODEL_NAME = "IlyaGusev/saiga_llama3_8b"
DEFAULT_SYSTEM_PROMPT = "Ты — Сайга, русскоязычный автоматический ассистент. Ты разговариваешь с людьми и помогаешь им."

MAIN_MODEL = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
#     load_in_8bit=True,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
MAIN_MODEL.eval()
MAIN_TOKENIZER = AutoTokenizer.from_pretrained(MODEL_NAME)
GENERATION_CONFIG = GenerationConfig.from_pretrained(MODEL_NAME)
