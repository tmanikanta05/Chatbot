# Chatbot
# 🤖 Python LLM + Agentic Thinking Assignment

This project implements a **multi-level smart assistant** using **Google Gemini API**, with support for:
- LLM-based Q&A
- Calculator tool integration
- Translation tool
- Multi-step reasoning (Agentic AI behavior)
- Streamlit Web Apps

---

## 📂 Project Structure
Chatbot/
│── README.md
│── requirements.txt
│── logs/
│ ├── level1_logs.txt
│ ├── level2_logs.txt
│ └── level3_logs.txt
│
├── level1/
│ ├── chatbot.py
│ └── main1.py
│
├── level2/
│ ├── chatbot_with_tool.py
│ ├── calculator_tool.py
│ └── main2.py
│
└── level3/
├── full_agent.py
├── calculator_tool.py
├── translator_tool.py
└── main3.py

## ⚙️ Setup

### 1. Clone Repo
```bash
git clone <your-repo-link>
cd chatbot
2. Install Dependencies
pip install -r requirements.txt
3. Add API Key
Create a file named .env in the project root:
GEMINI_API_KEY=your-gemini-api-key-here
Get a free key from 👉 Google AI Studio.

▶️ Running the Apps
bash
streamlit run level1/main1.py
streamlit run level2/main2.py
streamlit run level3/main3.py


📝 Example Queries
Level 1
What are the colors in a rainbow?
Tell me why the sky is blue?
Which planet is the hottest?
What is 15 + 23? → ❌ Refuses, suggests calculator tool

Level 2
What is 12 times 7? → ✅ Uses calculator
Add 45 and 30 → ✅ Uses calculator
What is the capital of France? → ✅ Gemini answers
Multiply 9 and 8, and also tell me the capital of Japan. → ❌ Graceful failure

Level 3
Translate 'Good Morning' into German and then multiply 5 and 6.
Add 10 and 20, then translate 'Have a nice day' into German.
Tell me the capital of Italy, then multiply 12 and 12.
Translate 'Sunshine' into German.
Add 2 and 2 and multiply 3 and 3.
What is the distance between Earth and Mars?

📊 Logs
All interactions are automatically saved to:
logs/level1_logs.txt
logs/level2_logs.txt
logs/level3_logs.txt


📦 Requirements
Python 3.9+
Google Gemini API Key

Install dependencies:
google-generativeai>=0.7.0
python-dotenv>=1.0.0
streamlit>=1.36.0


---
