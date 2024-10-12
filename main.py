import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)
    calculator = Calculator()
    commands = {
        "add": AddCommand,
        "subtract": SubtractCommand,
        "multiply": MultiplyCommand,
        "divide": DivideCommand
    }

    while True:
        user_input = input("Enter command (add, subtract, multiply, divide) and two numbers (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Please provide a command and two numbers.")
            continue

        command_type, a, b = parts[0], float(parts[1]), float(parts[2])
        CommandClass = commands.get(command_type)

        if not CommandClass:
            print(f"Unknown command '{command_type}'. Please use add, subtract, multiply, or divide.")
            continue
        
        try:
            command = CommandClass(calculator, a, b)
            result = command.execute()
            print(f"Result: {result}")
        except ValueError as ve:
            print(ve)

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()