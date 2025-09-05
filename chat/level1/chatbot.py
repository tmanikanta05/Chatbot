import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Gemini with API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create a model instance
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_llm(prompt: str) -> str:
    """Send query to Gemini with step-by-step enforced style."""
    system_msg = (
        "You are a smart assistant. Always answer step-by-step.\n"
        "If the user asks for a math calculation, refuse politely and suggest a calculator tool."
    )

    # Send query to Gemini
    response = model.generate_content(f"{system_msg}\nUser: {prompt}")
    return response.text

if __name__ == "__main__":
    print("=== Gemini LLM-Only Chatbot (Level 1) ===")
    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = ask_llm(query)
        print("Bot:", answer)

        # Save logs
        with open("logs/level1_logs.txt", "a", encoding="utf-8") as f:
            f.write(f"Q: {query}\nA: {answer}\n\n")
