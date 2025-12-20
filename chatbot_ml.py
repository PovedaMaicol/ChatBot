import joblib
import random
import numpy as np

# 1. Lod moodel and vectorizer
modelo = joblib.load("modelo_intenciones.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# 2. Intentions and answers
INTENCIONES = {
    0: "playlist",
    1: "calendar",
    2: "weather",
    3: "alarm",
    4: "location",
    5: "email",
    6: "general",
}

RESPUESTAS = {
    "playlist": [
        "🎵 Puedo ayudarte a agregar o quitar canciones.",
        "🎶 ¿Quieres modificar una playlist?",
    ],
    "calendar": ["📅 Puedo ayudarte con eventos y fechas.", "🗓️ ¿Quieres agendar algo?"],
    "weather": [
        "🌤️ Puedo darte el clima de cualquier ciudad.",
    ],
    "alarm": [
        "⏰ ¿Quieres crear o modificar una alarma?",
    ],
    "location": [
        "📍 Puedo ayudarte a encontrar lugares.",
    ],
    "email": [
        "📨 ¿Quieres enviar o revisar correos?",
    ],
    "general": ["❓ Puedo ayudarte con información general."],
    "desconocida": [
        "No estoy seguro de haberte entendido 🤔",
        "¿Podrías reformular la pregunta?",
    ],
}


# 3. functions for  intention prediction
def predecir_con_confianza(texto):
    X = vectorizer.transform([texto])
    probabilidades = modelo.predict_proba(X)[0]

    indice = np.argmax(probabilidades)
    confianza = probabilidades[indice]

    return indice, confianza


# 4. Loop conversational
def chatbot():
    print("🤖 Bot ML: Hola, escribe 'salir' para terminar")

    while True:
        texto = input("Tú: ")

        if texto.lower() == "salir":
            print("🤖 Bot ML: ¡Hasta luego!")
            break

        intencion_id, confianza = predecir_con_confianza(texto)

        if confianza < 0.6:
            respuesta = random.choice(RESPUESTAS["desconocida"])
        else:
            intencion = INTENCIONES[intencion_id]
            respuesta = random.choice(RESPUESTAS[intencion])
        print(f"🤖 Bot ({confianza:.2f}): {respuesta}")


# 5. Ejecutar
if __name__ == "__main__":
    chatbot()
