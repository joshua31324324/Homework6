import pytest
from calculator import Calculator
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    calc = Calculator()
    command = AddCommand(calc, 16, 2)
    assert command.execute() == 18

def test_subtract_command():
    calc = Calculator()
    command = SubtractCommand(calc, 16, 2)
    assert command.execute() == 14

def test_multiply_command():
    calc = Calculator()
    command = MultiplyCommand(calc, 16, 2)
    assert command.execute() == 32

def test_divide_command():
    calc = Calculator()
    command = DivideCommand(calc, 16, 2)
    assert command.execute() == 8

def test_divide_by_zero_command():
    calc = Calculator()
    command = DivideCommand(calc, 10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()
