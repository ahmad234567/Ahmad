import streamlit as st
import requests

# UI
st.title("💬 Chatbot powered by OpenRouter")
user_input = st.text_input("You:", "")

# API stuff
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": st.session_state.messages,
    }

    with st.spinner("Thinking..."):
        res = requests.post(API_URL, headers=HEADERS, json=data)

        if res.status_code == 200:
            reply = res.json()["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": reply})
        else:
            reply = "Error: " + res.text

    st.text_area("Bot:", reply, height=150)

# Show full chat history
for msg in st.session_state.messages:
    st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")

