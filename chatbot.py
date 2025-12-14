import re

'''chatbot sin PLN'''
def chatbot():
    print("Bot: Hola, soy un chatbot sin PLN. Escribe 'salir' para terminar.")

    while True:
        user_input = input("Tú: ").lower()

        if user_input == "salir":
            print("Bot: ¡Hasta luego!")
            break
        elif "hola" in user_input:
            print("Bot: ¡Hola! ¿Cómo estás?")
        elif "nombre" in user_input:
            print("Bot: Aún no tengo nombre 😄")
        else:
            print("Bot: No entiendo lo que dices.")

# chatbot()


def limpiar_texto(texto):
    '''Normalización básica del texto'''
    
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúñ\s]", "", texto) 
    return texto

# limpiar_texto("HOla mAicol soy un TEZSTO")