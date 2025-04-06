import argparse

def calculate(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("You can not divide by zero!")
        return num1 / num2
    else:
        raise ValueError("Unknown operation! Available options: add, subtract, multiply, divide")