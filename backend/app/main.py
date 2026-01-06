from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ChatRequest, ChatResponse
from app.memory import get_memory
from app.tutor import tutor_reply

app = FastAPI(title="English Tutor API")

# ✅ CORS SIEMPRE ANTES DE LAS RUTAS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego lo limitamos
    allow_credentials=True,
    allow_methods=["*"],  # 🔥 IMPORTANTE
    allow_headers=["*"],
)


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    memory = get_memory(req.session_id)
    reply = tutor_reply(req.message, memory)

    return {"reply": reply, "memory": memory}
