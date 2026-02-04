# backend/main.py
from fastapi import FastAPI
from backend.memory import (
    load_conversation_history as load_history,
    clear_conversation_history as clear_history,
    chat_with_memory as chat
)

from backend.schemas import ChatRequest, ChatResponse

app = FastAPI(title="AI with Memory API")

conversation_history = load_history()


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    reply = chat(request.message, conversation_history)
    return {"response": reply}


@app.post("/clear")
def clear_memory():
    global conversation_history
    conversation_history = []
    clear_history()
    return {"status": "memory cleared"}
