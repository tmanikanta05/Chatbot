import re

def calculate(expression: str) -> str:
    """Simple and safe calculator for +, -, *, /."""
    try:
        # Keep only numbers and operators
        expr = re.sub(r"[^0-9+\-*/.]", "", expression)

        # Check if expression is valid
        if not expr or all(c not in expr for c in "+-*/"):
            return "Sorry, I couldn't understand the math expression."

        # Evaluate safely
        result = eval(expr, {"__builtins__": None}, {})
        return f"The result is {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception:
        return "Sorry, I couldn't calculate that."
