# frontend/app.py
import streamlit as st
import requests

# ------------------ CONFIG ------------------

st.set_page_config(
    page_title="AI with Memory",
    page_icon="🧠",
    layout="centered"
)

# Backend URL (from Streamlit Secrets or fallback)
BACKEND_URL = st.secrets.get(
    "BACKEND_URL",
    "https://ai-with-memory.onrender.com"
)

CHAT_ENDPOINT = f"{BACKEND_URL}/chat"
CLEAR_ENDPOINT = f"{BACKEND_URL}/clear"

# ------------------ UI HEADER ------------------

st.title("🧠 AI with Memory")

st.markdown("""
### What is this app?
This is a conversational AI assistant that **remembers previous messages**.
You can ask follow-up questions naturally, and the AI keeps context
across the conversation.

### How it works
- Your message is sent to a FastAPI backend
- The backend stores conversation memory
- Each reply uses past context to respond intelligently

Start chatting below 👇
""")

st.divider()

# ------------------ SESSION STATE ------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------ DISPLAY CHAT HISTORY ------------------

for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)

# ------------------ USER INPUT ------------------

user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Send message to backend
    try:
        response = requests.post(
            CHAT_ENDPOINT,
            json={"message": user_input},
            timeout=60
        )
        response.raise_for_status()
        data = response.json()

        # IMPORTANT: backend returns "reply"
        ai_reply = data["reply"]

    except Exception as e:
        ai_reply = f"⚠️ Error communicating with backend: {e}"

    # Show AI message
    st.session_state.chat_history.append(("assistant", ai_reply))
    with st.chat_message("assistant"):
        st.write(ai_reply)

# ------------------ CLEAR MEMORY ------------------

st.divider()

if st.button("🧹 Clear Conversation Memory"):
    try:
        requests.post(CLEAR_ENDPOINT, timeout=10)
    except:
        pass

    st.session_state.chat_history = []
    st.success("Memory cleared. Start a fresh conversation!")
