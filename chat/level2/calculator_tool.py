# level2/calculator_tool.py

def calculate(expression: str) -> str:
    """Simple calculator for basic operations."""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception:
        return "Sorry, I couldn't calculate that."
