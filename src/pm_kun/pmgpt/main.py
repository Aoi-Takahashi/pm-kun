import torch
from transformers import T5Tokenizer, GPT2LMHeadModel, pipeline

tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small")
tokenizer.do_lower_case = True
model = GPT2LMHeadModel.from_pretrained("rinna/japanese-gpt2-small")


# TODO: Transformersのfine-tuningを行う
def generate_response(user_input: str) -> str:
    generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1,
    )

    response = generator(
        user_input, max_length=100, truncation=True, num_return_sequences=1
    )

    return response[0]["generated_text"]
