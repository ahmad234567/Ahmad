import streamlit as st
import requests

# Set page layout
st.set_page_config(page_title="AhmadBot", page_icon="🧠", layout="centered")

# Title and slogan
st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <h1 style="margin-bottom: 0;">AhmadBot</h1>
        <p style="color: gray; font-size: 1.1rem;">Your Service. My Duty.</p>
    </div>
""", unsafe_allow_html=True)

# Session state for chat messages and input
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm AhmadBot. How can I help you today?"}
    ]

# --- Input handling using a form (ENTER key only) ---
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", placeholder="Type and press Enter", label_visibility="collapsed")
    submitted = st.form_submit_button("Enter")

# If user submitted a message
if submitted and user_input.strip():
    # Append user message first
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})

    # Make the API call
    API_URL = "https://herh2ukwm5ajf4u5ntrgdici.agents.do-ai.run/api/v1/chat/completions"
    API_KEY = "Lheal7C39gJcxf6a0QqkaDHa2kN0KpX4"
    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "messages": st.session_state.messages,
        "provide_citations": False
    }

    with st.spinner("AhmadBot is typing..."):
        response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
    else:
        reply = "⚠️ Error: " + response.text

    # Append bot response after user message
    st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Render chat history ---
for msg in st.session_state.messages:
    is_user = msg["role"] == "user"
    icon = "🧑" if is_user else "🤖"
    align = "flex-end" if is_user else "flex-start"
    bg_color = "#e6f7ff" if is_user else "#f5f5f5"
    label = "You" if is_user else "AhmadBot"

    st.markdown(f"""
        <div style="display: flex; justify-content: {align}; margin: 8px 0;">
            <div style="background: {bg_color}; padding: 10px 14px; border-radius: 10px; max-width: 75%; font-size: 1rem;">
                <b>{icon} {label}:</b><br>{msg['content']}
            </div>
        </div>
    """, unsafe_allow_html=True)
    import streamlit as st
import requests

# Set page layout
st.set_page_config(page_title="AhmadBot", page_icon="🧠", layout="centered")

# Title and slogan
st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <h1 style="margin-bottom: 0;">AhmadBot</h1>
        <p style="color: gray; font-size: 1.1rem;">Your Service. My Duty.</p>
    </div>
""", unsafe_allow_html=True)

# Session state for chat messages and input
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm AhmadBot. How can I help you today?"}
    ]

# --- Input handling using a form (ENTER key only) ---
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", placeholder="Type and press Enter", label_visibility="collapsed")
    submitted = st.form_submit_button("Enter")

# If user submitted a message
if submitted and user_input.strip():
    # Append user message first
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})

    # Make the API call
    API_URL = "https://herh2ukwm5ajf4u5ntrgdici.agents.do-ai.run/api/v1/chat/completions"
    API_KEY = "Lheal7C39gJcxf6a0QqkaDHa2kN0KpX4"
    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "messages": st.session_state.messages,
        "provide_citations": False
    }

    with st.spinner("AhmadBot is typing..."):
        response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
    else:
        reply = "⚠️ Error: " + response.text

    # Append bot response after user message
    st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Render chat history ---
for msg in st.session_state.messages:
    is_user = msg["role"] == "user"
    icon = "🧑" if is_user else "🤖"
    align = "flex-end" if is_user else "flex-start"
    bg_color = "#e6f7ff" if is_user else "#f5f5f5"
    label = "You" if is_user else "AhmadBot"

    st.markdown(f"""
        <div style="display: flex; justify-content: {align}; margin: 8px 0;">
            <div style="background: {bg_color}; padding: 10px 14px; border-radius: 10px; max-width: 75%; font-size: 1rem;">
                <b>{icon} {label}:</b><br>{msg['content']}
            </div>
        </div>
    """, unsafe_allow_html=True)

def generate_response(user_input, document_text):
    prompt = f"""
Use the following document to answer the user's question:
{document_text}

User: {user_input}
Answer:
"""
    return model.generate(prompt)

