import os
import google.generativeai as genai
from dotenv import load_dotenv
from calculator_tool import calculate

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create Gemini model instance
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_llm(query: str) -> str:
    """Ask Gemini directly (non-math queries)."""
    system_msg = (
        "You are an assistant. "
        "If the query is math, do NOT solve it yourself — leave it for the calculator tool. "
        "If it's general knowledge, answer directly. "
        "Do NOT attempt multi-step tasks yet."
    )
    response = model.generate_content(f"{system_msg}\nUser: {query}")
    return response.text

def handle_query(query: str) -> str:
    # Simple detection for math
    if any(word in query.lower() for word in ["add", "multiply", "times", "+", "*"]):
        expr = query.lower().replace("add", "+").replace("multiply", "*").replace("times", "*")
        expr = "".join([c for c in expr if c.isdigit() or c in "+-* /"])
        return calculate(expr)
    return ask_llm(query)

if __name__ == "__main__":
    print("=== Gemini Chatbot with Calculator Tool (Level 2) ===")
    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = handle_query(query)
        print("Bot:", answer)

        # Save logs
        with open("logs/level2_logs.txt", "a", encoding="utf-8") as f:
            f.write(f"Q: {query}\nA: {answer}\n\n")
