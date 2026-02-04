# AI with Memory 🤖🧠

A conversational AI application that remembers past interactions using
persistent memory.

## Tech Stack
- FastAPI (Backend)
- Streamlit (Frontend)
- Groq LLM API
- JSON-based memory (upgradeable)

## Features
- Context-aware conversations
- Persistent memory across sessions
- Clean API-based architecture

## Run Locally
```bash
uvicorn backend.main:app --reload
streamlit run frontend/app.py
