from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# 1. Cargar modelo y tokenizer
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("English Tutor is ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Tutor: Goodbye! Keep practicing 😊")
        break

    # 2. Prompt instructivo
    prompt = (
        "You are an English tutor.\n"
        "Your task is to reply to the student.\n\n"
        "Student sentence:\n"
        f"{user_input}\n\n"
        "Tutor answer (correct mistakes if any, explain briefly, then continue the conversation):"
    )

    # 3. Tokenizar
    inputs = tokenizer(prompt, return_tensors="pt")

    # 4. Generar respuesta
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        max_new_tokens=80,
        do_sample=True,
        top_p=0.9,
        temperature=0.7,
    )

    # 5. Decodificar
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print(f"Tutor: {response}\n")
