# AI with Memory 🤖🧠
app link:"https://ai-with-memory-jjgyyczkvvpbkxkrnjgjdx.streamlit.app/"
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
