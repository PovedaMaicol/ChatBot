from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 1. Cargar tokenizer y modelo
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

print("English Chatbot is ready! Type 'exit' to stop.\n")

chat_history_ids = None

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Bye! Keep practicing your English 😊")
        break

    # 2. Codificar entrada del usuario
    new_input_ids = tokenizer.encode(
        user_input + tokenizer.eos_token,
        return_tensors="pt"
    )

    # 3. Concatenar historial para mantener contexto
    bot_input_ids = (
        torch.cat([chat_history_ids, new_input_ids], dim=-1)
        if chat_history_ids is not None
        else new_input_ids
    )

    # 4. Generar respuesta
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.9,
        temperature=0.75
    )

    # 5. Decodificar respuesta
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    print(f"Bot: {response}\n")
