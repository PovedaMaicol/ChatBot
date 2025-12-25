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


# simple memory for previous interactions
estado = {"intencion_actual": None, "datos": {}}


# detect if the bot is waiting
def manejar_contexto(texto, estado):
    if estado["intencion_actual"] == "playlist" and "cancion" not in estado["datos"]:
        estado["datos"]["cancion"] = texto
        return f"🎶 Listo, agregué '{texto}' a tu playlist."

    return None


# historial
historial = []


# proces mesage
def procesar_mensaje(texto, estado, historial):
    historial.append(("usuario", texto))

    respuesta_contexto = manejar_contexto(texto, estado)
    if respuesta_contexto:
        historial.append(("bot", respuesta_contexto))
        estado["intencion_actual"] = None
        estado["datos"] = {}
        return respuesta_contexto

    intencion_id, confianza = predecir_con_confianza(texto)

    if confianza < 0.6:
        respuesta = "No estoy seguro de entenderte 🤔"
        historial.append(("bot", respuesta))
        return respuesta

    intencion = INTENCIONES[intencion_id]

    if intencion == "playlist":
        estado["intencion_actual"] = "playlist"
        estado["datos"] = {}
        respuesta = "🎵 ¿Qué canción quieres agregar?"
        historial.append(("bot", respuesta))
        return respuesta

    respuesta = random.choice(RESPUESTAS[intencion])
    historial.append(("bot", respuesta))
    return respuesta


# 4. Loop conversational
def chatbot():
    print("🤖 Bot ML: Hola, escribe 'salir' para terminar")

    while True:
        texto = input("Tú: ")

        if texto.lower() == "salir":
            print("🤖 Bot: ¡Hasta luego!")
            break

        respuesta = procesar_mensaje(texto, estado, historial)
        print("🤖 Bot:", respuesta)


# 5. Ejecutar
if __name__ == "__main__":
    chatbot()
