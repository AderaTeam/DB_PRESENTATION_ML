from commutators.gpt_service_comutator import get_gpt_comutator


def get_shorted_text_by_gpt(text: str):
    prompt = f"Сократи данный текст: {text}"
    res = get_gpt_comutator(prompt, 10)
    return res