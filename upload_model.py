import streamlit as st
import requests

st.set_page_config(page_title="💬 Local LLM Chat", layout="centered")
# this is the hypthothetical title used not the real but used in the code

st.title("🧠 Chat with Local Model (LM Studio)")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:  # skip system prompt
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Get user input
if prompt := st.chat_input("Ask me anything..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the payload
    payload = {
        "model": "local-model",  # LM Studio doesn’t care about this name
        "messages": st.session_state.messages,
        "temperature": 0.7,
    }

    # Call LM Studio’s local API
    try:
        res = requests.post(
            "http://127.0.0.1:1234/v1/chat/completions",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=60
        )
        res.raise_for_status()
        reply = res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"❌ Error talking to model: {e}"

    # Show model reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
