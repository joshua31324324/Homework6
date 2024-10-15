from command import Command

class AddCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.add(self.a, self.b)

class SubtractCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.subtract(self.a, self.b)

class MultiplyCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.multiply(self.a, self.b)

class DivideCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.divide(self.a, self.b)

commands = {
    "help": "Displays the help menu",
    "start": "Starts the application",
    "exit": "Exits the application",
    "menu": "Displays the command menu"
}

def display_menu():
    print("Available commands:")
    for command, description in commands.items():
        print(f"{command}: {description}")
