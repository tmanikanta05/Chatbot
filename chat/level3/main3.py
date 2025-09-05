import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from calculator_tool import calculate
from translator_tool import translate_to_german

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def handle_query(query: str) -> str:
    steps = query.split(" then ")
    responses = []

    for step in steps:
        step = step.strip()
        if any(word in step.lower() for word in ["add", "multiply", "times", "+", "*"]):
            expr = step.lower().replace("add", "+").replace("multiply", "*").replace("times", "*")
            expr = "".join([c for c in expr if c.isdigit() or c in "+-* /"])
            responses.append(calculate(expr))
        elif "translate" in step.lower():
            text = step.split("'")[1] if "'" in step else step
            responses.append(translate_to_german(text))
        else:
            system_msg = "Answer step-by-step in clear detail."
            response = model.generate_content(f"{system_msg}\nUser: {step}")
            responses.append(response.text)

    return " | ".join(responses)

# Streamlit UI
st.set_page_config(page_title="Level 3 Full Agent", page_icon="🤖")
st.title("🤖 Level 3: Full Agent with Multi-Step Reasoning")

query = st.text_area("Enter your multi-step query:")

if st.button("Submit") and query.strip():
    answer = handle_query(query)
    st.success(answer)

    os.makedirs("../logs", exist_ok=True)
    with open("../logs/level3_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"Q: {query}\nA: {answer}\n\n")
