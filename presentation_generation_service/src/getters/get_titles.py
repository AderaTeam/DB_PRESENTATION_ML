from commutators.gpt_service_comutator import get_gpt_comutator


def get_titles_by_gpt(text: str):
    prompt = f"Озаглавь данный текст: {text}"
    res = get_gpt_comutator(prompt)
    return res