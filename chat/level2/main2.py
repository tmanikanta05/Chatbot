import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from calculator_tool import calculate

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_llm(query: str) -> str:
    system_msg = (
        "You are an assistant. "
        "If the query is math, do NOT solve it yourself — leave it for the calculator tool. "
        "If it's general knowledge, answer directly. "
        "Do NOT attempt multi-step tasks yet."
    )
    response = model.generate_content(f"{system_msg}\nUser: {query}")
    return response.text

def handle_query(query: str) -> str:
    if any(word in query.lower() for word in ["add", "multiply", "times", "+", "*"]):
        expr = query.lower().replace("add", "+").replace("multiply", "*").replace("times", "*")
        expr = "".join([c for c in expr if c.isdigit() or c in "+-* /"])
        return calculate(expr)
    return ask_llm(query)

# Streamlit UI
st.set_page_config(page_title="Level 2 Chatbot", page_icon="🧮")
st.title("🧮 Level 2: Chatbot with Calculator Tool")

query = st.text_input("Ask me a question (math or general knowledge):")

if st.button("Submit") and query.strip():
    answer = handle_query(query)
    st.success(answer)

    os.makedirs("../logs", exist_ok=True)
    with open("../logs/level2_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"Q: {query}\nA: {answer}\n\n")
