# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from backend.memory import (
    load_conversation_history,
    save_conversation_history,
    clear_conversation_history,
    chat_with_memory,
)

from backend.schemas import ChatRequest, ChatResponse

app = FastAPI(
    title="AI with Memory API",
    description="Backend API for a conversational AI that remembers past interactions",
    version="1.0.0",
)


# ----------- Models -----------

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


# ----------- Routes -----------

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "AI with Memory backend is live 🚀",
        "endpoints": {
            "chat": "/chat",
            "clear_memory": "/clear",
            "history": "/history",
            "docs": "/docs"
        }
    }


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    history = load_conversation_history()
    reply = chat_with_memory(request.message, history)
    save_conversation_history(history)
    return {"reply": reply}


@app.get("/history")
def get_history():
    return load_conversation_history()


@app.post("/clear")
def clear_memory():
    clear_conversation_history()
    return {"status": "cleared", "message": "Conversation memory cleared 🧹"}