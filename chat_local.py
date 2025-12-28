from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 1. Cargar tokenizer y modelo
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

print("English Chatbot is ready! Type 'exit' to stop.\n")

# Prompt de personalidad (MUY IMPORTANTE)
persona_prompt = (
    "You are Chatbot, a friendly English conversation partner. "
    "You speak naturally, keep the conversation going, "
    "and ask follow-up questions."
)

chat_history_ids = None
MAX_HISTORY_TOKENS = 500

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Bye! Keep practicing your English 😊")
        break

    # 2. Construir input con personalidad SOLO al inicio
    if chat_history_ids is None:
        full_input = persona_prompt + tokenizer.eos_token + user_input
    else:
        full_input = user_input

    new_input_ids = tokenizer.encode(
        full_input + tokenizer.eos_token, return_tensors="pt"
    )

    # 3. Concatenar historial con límite
    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
        bot_input_ids = bot_input_ids[:, -MAX_HISTORY_TOKENS:]
    else:
        bot_input_ids = new_input_ids

    # 4. Generar respuesta (FORZANDO QUE HABLE)
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        min_length=20,
        do_sample=True,
        top_p=0.9,
        temperature=0.75,
        repetition_penalty=1.2,
        pad_token_id=tokenizer.eos_token_id,
    )

    # 5. Decodificar respuesta
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1] :][0], skip_special_tokens=True
    )

    # 6. Respuesta de respaldo (CRÍTICA)
    if not response.strip():
        response = "Sorry, I didn't quite get that. Could you rephrase?"

    print(f"Bot: {response}\n")
