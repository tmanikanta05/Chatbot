import os
import google.generativeai as genai
from dotenv import load_dotenv
from calculator_tool import calculate
from translator_tool import translate_to_german

# Load .env and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create Gemini model instance
model = genai.GenerativeModel("gemini-1.5-flash")

def handle_query(query: str) -> str:
    steps = query.split(" then ")
    responses = []

    for step in steps:
        step = step.strip()
        if any(word in step.lower() for word in ["add", "multiply", "times", "+", "*"]):
            # Math handling
            expr = step.lower().replace("add", "+").replace("multiply", "*").replace("times", "*")
            expr = "".join([c for c in expr if c.isdigit() or c in "+-* /"])
            responses.append(calculate(expr))

        elif "translate" in step.lower():
            # Translation handling
            text = step.split("'")[1] if "'" in step else step
            responses.append(translate_to_german(text))

        else:
            # General knowledge → Gemini
            system_msg = "Answer step-by-step in clear detail."
            response = model.generate_content(f"{system_msg}\nUser: {step}")
            responses.append(response.text)

    return " | ".join(responses)

if __name__ == "__main__":
    print("=== Gemini Full Agent (Level 3) ===")
    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = handle_query(query)
        print("Bot:", answer)

        # Save logs
        with open("logs/level3_logs.txt", "a", encoding="utf-8") as f:
            f.write(f"Q: {query}\nA: {answer}\n\n")
