from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Modelo conversacional
MODEL_NAME = "microsoft/DialoGPT-medium"

print("Cargando tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Cargando modelo...")
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

print("Modelo cargado correctamente ✅")

# Historial de conversación
chat_history_ids = None

while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit", "quit"]:
        break

    # Codificamos la entrada
    new_input_ids = tokenizer.encode(
        user_input + tokenizer.eos_token,
        return_tensors="pt"
    )

    # Unimos historial + mensaje nuevo
    bot_input_ids = (
        torch.cat([chat_history_ids, new_input_ids], dim=-1)
        if chat_history_ids is not None
        else new_input_ids
    )

    # Generamos respuesta
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8
    )

    # Decodificamos solo la respuesta nueva
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    print("Bot:", response)
