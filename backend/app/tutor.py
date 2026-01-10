import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"
TUTOR_NAME = "Neo"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def tutor_reply(user_input: str, memory: dict) -> str:
    lower_input = user_input.lower()

    # Guardar memoria
    if "my name is" in lower_input:
        memory["name"] = user_input.split("is")[-1].strip().capitalize()

    if "i am from" in lower_input or "i'm from" in lower_input:
        memory["country"] = user_input.split("from")[-1].strip().capitalize()

    # Reglas duras
    if lower_input in ["what is your name?", "what's your name?"]:
        return f"My name is {TUTOR_NAME}."

    if lower_input in ["where are you from?", "where are you from"]:
        return (
            "I'm an AI English tutor, so I don't have a country. " "Where are you from?"
        )

    if lower_input in ["what is my name?", "what's my name?"] and memory["name"]:
        return f"Your name is {memory['name']}."

    # Prompt EXACTO
    prompt = (
        "You are an AI English tutor.\n"
        "Always answer in English.\n"
        "If the student makes a mistake, correct it briefly.\n"
        "If the sentence is correct, respond naturally and continue the conversation.\n\n"
    )

    if memory["name"]:
        prompt += f"The student's name is {memory['name']}.\n"

    if memory["country"]:
        prompt += f"The student is from {memory['country']}.\n"

    prompt += f"\nStudent: {user_input}\n" "Tutor: Answer naturally and helpfully.\n"

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            max_new_tokens=80,
            do_sample=True,
            top_p=0.9,
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
