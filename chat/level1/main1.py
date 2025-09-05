import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_llm(prompt: str) -> str:
    system_msg = (
        "You are a smart assistant. Always answer step-by-step.\n"
        "If the user asks for a math calculation, refuse politely and suggest a calculator tool."
    )
    response = model.generate_content(f"{system_msg}\nUser: {prompt}")
    return response.text

# Streamlit UI
st.set_page_config(page_title="Level 1 Chatbot", page_icon="🌈")
st.title("🌈 Level 1: LLM-Only Smart Assistant")

query = st.text_input("Ask me anything:")

if st.button("Submit") and query.strip():
    answer = ask_llm(query)
    st.success(answer)

    os.makedirs("../logs", exist_ok=True)
    with open("../logs/level1_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"Q: {query}\nA: {answer}\n\n")
