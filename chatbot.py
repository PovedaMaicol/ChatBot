import re
import random

""" 1. ===== CHATBOT SIN LNP ====="""
UMBRAL_CONFIANZA = 0.6

def chatbot():
    print("Bot: Hola, soy un chatbot. Escribe 'salir' para terminar.")

    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() == "salir":
            print("Bot: ¡Hasta luego!")
            break
        
        intencion, confianza = predecir_con_confianza(user_input)
        
        if confianza < UMBRAL_CONFIANZA:
            respuesta = random.choice(respuestas["desconocida"])
        else:
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
    texto = limpiar_texto(texto)
    X_test = vectorizer.transform([texto])
    return modelo.predict(X_test)[0]


# response to intention
def responder(intencion):
    return random.choice(respuestas[intencion])

'''VECTORIZACIÓN --> es el proceso de convertir texto en datos numéricos que los modelos de ML pueden entender.'''

'''4. ===== VER QUÉ TAN SEGURO ESTÁ EL MODELO ==== '''
def predecir_con_confianza(texto):
    texto = limpiar_texto(texto)
    X_test = vectorizer.transform([texto])
    
    
    probabilidades = modelo.predict_proba(X_test)[0]
    ''''predict_proba --> devuelve la probabilidad de cada clase para la entrada dada.'''
    clases = modelo.classes_
    
    
    mejor_indice = probabilidades.argmax()
    '''argmax() --> devuelve el índice del valor máximo en una matriz.'''
    intencion = clases[mejor_indice]
    confianza = probabilidades[mejor_indice]
  

    
    return intencion, confianza