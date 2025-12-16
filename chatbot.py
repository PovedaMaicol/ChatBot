import re
import random

""" 1. ===== CHATBOT SIN LNP ====="""


def chatbot():
    print("Bot: Hola, soy un chatbot. Escribe 'salir' para terminar.")

    while True:
        user_input = input("Tú: ").lower()
        mensaje = limpiar_texto(user_input)

        if mensaje == "salir":
            print("Bot: ¡Hasta luego!")
            break
        
        intencion = detectar_intencion(mensaje)
        respuesta = responder(intencion)
        
        print(f"Bot: {respuesta}")


# chatbot()


def limpiar_texto(texto):
    """Normalización básica del texto"""

    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúñ\s]", "", texto)
    return texto



# limpiar_texto("HOla mAicol soy un TEZSTO")

""" 2. =======ANSWERS FOR INTENTION========
se detecta que quiere el usuario

concepto clave --> la intención(intention)
ejm: "hola, buenas, hey" --> intención: saludo"""

intentions = {
    "saludo": [
        "hola",
        "buenas",
        "hey",
        "buenos días",
        "buenas tardes",
        "buenas noches",
    ],
    "despedida": ["adiós", "hasta luego", "nos vemos", "chao", "bye"],
    "nombre": ["nombre", "quien eres", "como te llamas"],
}


def detectar_intencion(mensaje):
    for intencion, palabras in intentions.items():
        for palabra in palabras:
            if palabra in mensaje:
                return intencion
    return "desconocida"


""" 3. ===== INTRODUCTION TO MACHINE LEARNING ====="""
# Datasets
frases = [
    "hola",
    "buenos dias",
    "hey",
    "como te llamas",
    "quien eres",
    "adios",
    "cual es tu nombre",
    "hasta luego",
    "chao"
]

etiquetas = ["saludo", "saludo", "saludo", "nombre", "nombre", "nombre", "despedida", "despedida", "despedida"]

respuestas = {
    "saludo": ["¡Hola!", "¡Buenos días!", "¡Hey! ¿Cómo estás?"],
    "despedida": ["¡Adiós!", "¡Hasta luego!", "¡Nos vemos!"],
    "nombre": ["Soy un chatbot sin nombre.", "Aún no tengo un nombre."],
    "desconocida": ["No entiendo lo que dices."]
}

# Model training
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(frases)


modelo = MultinomialNB()
modelo.fit(x, etiquetas)


# use model in the chatbot
def predecir_intencion(texto):
    X_test = vectorizer.transform([texto])
    return modelo.predict(X_test)[0]


# response to intention
def responder(intencion):
    return random.choice(respuestas[intencion])