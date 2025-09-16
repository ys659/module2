"""
This is the code for the calculator program.
It will use `operations.py` for arithmetic operations.
"""

from app.operations import (
    add,
    subtract,
    multiply,
    divide,
    mod
)

def calculator():
    
    # Welcome message
    print("Welcome to REPLCalc!")

    while True:

        # Ask for user input
        user_input = input("Enter an operation "
        "(add, subtract, multiply, divide, mod) "
        "and two numbers, or type 'exit' to quit: ")

        # If user wants to quit
        if user_input.lower() == "exit":
            print("Thanks for using REPLCalc!")
            break

        # User inputs data (risky!)  
        try:
            operation, num1, num2 = user_input.split()
            
            operation = operation.lower()
            num1, num2 = float(num1), float(num2)

        # User input invalid data
        except ValueError:
            print("Invalid input. Please follow the "
            "format: <operation> <number1> <number2>")
            continue

        # Operations
        if operation in ("add", "addition"):
            result = add(num1, num2)

        elif operation in ("subtract", "subtraction", "sub"):
            result = subtract(num1, num2)

        elif operation in ("multiply", "mul", "times"):
            result = multiply(num1, num2)

        elif operation in ("divide", "division"):
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                continue

        elif operation in ("mod", "modulus"):
            result = mod(num1, num2)

        else:
            print(
            f"Unknown operation '{operation}'. " 
            "Supported operations: add, subtract, "
            "multiply, divide, mod"
            )
            continue

        # Finally print the result
        print(f"Result: {result}")
