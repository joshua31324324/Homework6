from calculator import Calculator1
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def main():
    calculator = Calculator1()
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

if __name__ == "__main__":
    main()
