# level3/translator_tool.py

def translate_to_german(text: str) -> str:
    translations = {
        "Good Morning": "Guten Morgen",
        "Have a nice day": "Einen schönen Tag noch",
        "Sunshine": "Sonnenschein"
    }
    return translations.get(text, f"(Simulated) German translation of '{text}'")
