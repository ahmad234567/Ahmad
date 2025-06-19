import streamlit as st
import requests
from docx import Document
import csv
from datetime import datetime

# Cache the document loading for performance
@st.cache_data
def load_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

# Logging function
def log_interaction(user_input, reply):
    with open("chat_log.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), user_input, reply])

# Load document once
try:
    document_text = load_docx("mydoc.docx")
except Exception as e:
    st.error(f"Failed to load document: {e}")
    document_text = ""

st.set_page_config(page_title="AhmadBot", page_icon="🧠")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm AhmadBot. How can I help you today?"}
    ]

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", placeholder="Type and press Enter", label_visibility="collapsed")
    submitted = st.form_submit_button("Enter")

if submitted and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})

    prompt = f"""
Use the following document to answer the user's question:
{document_text}

User: {user_input}
Answer:
"""

    API_URL = "https://herh2ukwm5ajf4u5ntrgdici.agents.do-ai.run/api/v1/chat/completions"
    API_KEY = "Lheal7C39gJcxf6a0QqkaDHa2kN0KpX4"
    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "provide_citations": False
    }

    with st.spinner("AhmadBot is typing..."):
        response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
    else:
        reply = "⚠️ Error: " + response.text

    st.session_state.messages.append({"role": "assistant", "content": reply})
    log_interaction(user_input.strip(), reply)

# Display chat messages
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
