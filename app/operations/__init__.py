""" These are the operations for the calculator. """

# Addition
def add(a: float, b: float) -> float:
    return a + b

# Subtraction
def subtract(a: float, b: float) -> float:
    return a - b

# Multiplication
def multiply(a: float, b: float) -> float:
    return a * b

# Division
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# Modulus
def mod(a: float, b: float) -> float:
    return a % b
