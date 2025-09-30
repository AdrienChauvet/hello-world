"""Simple command-line calculator supporting basic arithmetic operations."""

def get_number(prompt: str) -> float:
    """Prompt the user for a number and return it as a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation() -> str:
    """Prompt the user to choose an arithmetic operation."""
    operations = {"+", "-", "*", "/"}
    while True:
        op = input("Choose an operation (+, -, *, /): ")
        if op in operations:
            return op
        print("Invalid operation. Please choose one of +, -, *, /.")

def calculate(num1: float, num2: float, operation: str) -> float:
    """Perform the calculation based on the chosen operation."""
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    raise ValueError(f"Unsupported operation: {operation}")

def main() -> None:
    print("Welcome to the simple calculator!")
    number1 = get_number("Enter the first number: ")
    number2 = get_number("Enter the second number: ")
    op = get_operation()

    try:
        result = calculate(number1, number2, op)
    except ZeroDivisionError as error:
        print(error)
    else:
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
