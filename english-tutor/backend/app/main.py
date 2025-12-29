from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.memory import get_memory
from app.tutor import tutor_reply

app = FastAPI(title="English Tutor API")


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    memory = get_memory(req.session_id)
    reply = tutor_reply(req.message, memory)

    return {"reply": reply, "memory": memory}
