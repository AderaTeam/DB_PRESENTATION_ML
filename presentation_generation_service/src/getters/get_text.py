from commutators.gpt_service_comutator import get_gpt_comutator


def get_shorted_text_by_gpt(text: str):
    prompt = f"Очень сильно сократи данный текст: {text}"
    res = get_gpt_comutator(prompt, 10)
    return res