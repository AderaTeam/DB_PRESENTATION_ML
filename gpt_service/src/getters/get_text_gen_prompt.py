from constants import DEFAULT_SYSTEM_PROMPT, MAIN_TOKENIZER


def get_text_gen_prompt(text: str) -> str:
    prompt = MAIN_TOKENIZER.apply_chat_template([{
        "role": "system",
        "content": DEFAULT_SYSTEM_PROMPT
    }, {
        "role": "user",
        "content": text,
    }], tokenize=False, add_generation_prompt=True,)
    return prompt
