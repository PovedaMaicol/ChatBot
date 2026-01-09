import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# ==============================
# 1. Cargar modelo y tokenizer
# ==============================
MODEL_NAME = "google/flan-t5-small"
TUTOR_NAME = "Neo"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

print("English Tutor is ready! Type 'exit' to stop.\n")

# ==============================
# 2. Memoria simple del estudiante
# ==============================
memory = {
    "name": None,
    "country": None,
}

# Identidad fija del tutor (CONTROLADA EN CÓDIGO)


# ==============================
# 3. Loop de conversación
# ==============================
while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "exit":
        print("Tutor: Goodbye! Keep practicing your English 😊")
        break

    lower_input = user_input.lower()

    # ==============================
    # 4. Guardar memoria del estudiante
    # ==============================
    if "my name is" in lower_input:
        memory["name"] = user_input.split("is")[-1].strip().capitalize()

    if "i am from" in lower_input or "i'm from" in lower_input:
        memory["country"] = user_input.split("from")[-1].strip().capitalize()

    # ==============================
    # 5. Respuestas CONTROLADAS (hard rules)
    # ==============================
    if lower_input in ["what is your name?", "what's your name?"]:
        print(f"Tutor: My name is {TUTOR_NAME}.\n")
        continue

    if lower_input in ["where are you from?", "where are you from"]:
        print(
            "Tutor: I'm an AI English tutor, so I don't have a country. "
            "Where are you from?\n"
        )
        continue

    if lower_input in ["what is my name?", "what's my name?"] and memory["name"]:
        print(f"Tutor: Your name is {memory['name']}.\n")
        continue

    # ==============================
    # 6. Construir prompt LIMPIO
    # ==============================
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

    prompt += "\nConversation:\n" f"Student: {user_input}\n" "Tutor:"

    # ==============================
    # 7. Generar respuesta
    # ==============================
    inputs = tokenizer(prompt, return_tensors="pt")

    # outputs = model.generate(
    #     input_ids=inputs["input_ids"],
    #     max_new_tokens=80,
    #     do_sample=True,
    #     top_p=0.9,
    # )
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            max_new_tokens=80,
            do_sample=True,
            top_p=0.9,
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print(f"Tutor: {response}\n")
