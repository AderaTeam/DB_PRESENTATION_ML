from src.constants import GENERATION_CONFIG, MAIN_MODEL, MAIN_TOKENIZER


def get_prediction(prompt) -> str:
    data = MAIN_TOKENIZER(prompt, return_tensors="pt", add_special_tokens=False)
    data = {k: v.to(MAIN_MODEL.device) for k, v in data.items()}
    output_ids = MAIN_MODEL.generate(**data, generation_config=GENERATION_CONFIG)[0]
    output_ids = output_ids[len(data["input_ids"][0]):]
    output = MAIN_TOKENIZER.decode(output_ids, skip_special_tokens=True).strip()
    return output