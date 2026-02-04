# frontend/app.py
import streamlit as st
import requests

API_URL = "https://ai-with-memory.onrender.com/chat"


st.set_page_config(page_title="AI with Memory", layout="centered")
st.title("🧠 AI with Memory")

st.markdown("""
### 📌 What does this application do?

This application demonstrates how a conversational AI can **remember previous user inputs**
during a session and use them as context for future responses.

It is built using a **frontend–backend architecture**, similar to real-world AI systems.

---

### ⚙️ How does it work?

**1. Frontend (Streamlit)**
- Takes user input from the browser
- Sends the input to the backend using an API call
- Displays AI responses and conversation history

**2. Backend (FastAPI)**
- Receives user messages through a REST API
- Stores messages in memory during the session
- Generates responses based on stored context
- Returns the response back to the frontend

**3. Memory Handling**
- The backend maintains an in-memory list of messages
- Each new message is added to memory
- Clearing memory resets the conversation context

---

### 🧠 Why is this important?

This pattern is the foundation of:
- Chatbots and virtual assistants
- AI agents with memory
- Production-ready LLM applications
- Scalable ML system design

You're not just chatting with an AI — you're interacting with a **stateful system**.
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    if st.button("Clear Memory"):
        requests.post(f"{API_URL}/clear")
        st.session_state.messages = []
        st.success("Memory cleared")

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    res = requests.post(
        f"{API_URL}/chat",
        json={"message": user_input}
    ).json()

    st.chat_message("assistant").write(res["response"])
    st.session_state.messages.append(
        {"role": "assistant", "content": res["response"]}
    )
