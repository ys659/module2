import sys
from io import StringIO
from app.calculator import calculator

# Helper function to capture print statements
def run_calculator_with_input(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input',
                        lambda _: next(input_iterator))

    # Capture the output of the calculator
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__ # Reset stdout
    return captured_output.getvalue()

# Positive tests
def test_addition(monkeypatch):
    inputs = ["add 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output

def test_subtraction(monkeypatch):
    inputs = ["subtract 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 2.0" in output

def test_multiplication(monkeypatch):
    inputs = ["multiply 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 15.0" in output

def test_division(monkeypatch):
    inputs = ["divide 6 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 2.0" in output

# def test_modulus(monkeypatch):
#     inputs = ["mod 5 1", "exit"]
#     output = run_calculator_with_input(monkeypatch, inputs)
#     assert "Result: 0.0" in output

# Negative tests
def test_invalid_operation(monkeypatch):
    inputs = ["modulus 3 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Unknown operation" in output

def test_invalid_input_format(monkeypatch):
    inputs = ["add two three", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert (
        "Invalid input. Please follow the format: "
        "<operation> <number1> <number2>" in output
        )

def test_division_by_zero(monkeypatch):
    inputs = ["divide 5 0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed" in output

# def test_modulus_by_zero(monkeypatch):
#     inputs = ["mod 5 0", "exit"]
#     output = run_calculator_with_input(monkeypatch, inputs)
#     assert "Modulus by zero is not allowed" in output
