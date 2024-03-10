import torch
from transformers import T5Tokenizer, GPT2LMHeadModel, pipeline


# TODO: Transformersのfine-tuningを行う
# 参考URL：https://huggingface.co/docs/transformers/ja/tasks/question_answering
def generate_response(user_input: str, user_context: str) -> str:

    question_answerer = pipeline(
        "question-answering", model="KoichiYasuoka/bert-base-japanese-wikipedia-ud-head"
    )
    answer = question_answerer(
        question=user_input,
        context=user_context,
    ).get("answer")

    return answer
