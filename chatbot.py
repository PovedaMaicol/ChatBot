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

mensaje = limpiar_texto(input("Tú: "))


# limpiar_texto("HOla mAicol soy un TEZSTO")

'''=======ANSWERS FOR INTENTION========
se detecta que quiere el usuario

concepto clave --> la intención(intention)
ejm: "hola, buenas, hey" --> intención: saludo'''

intentions = {
    
    "saludo": ["hola", "buenas", "hey", "buenos días", "buenas tardes", "buenas noches"],
    "despedida": ["adiós", "hasta luego", "nos vemos", "chao", "bye"],
    "nombre": ["nombre", "quien eres", "cómo te llamas"],
}

def detectar_intencion(mensaje):
    for intencion, palabras in intentions.items():
        for palabra in palabras:
            if palabra in mensaje:
                return intencion
            return "desconocida"