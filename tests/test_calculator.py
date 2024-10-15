'''My Calculator Test'''
import pytest
from calculator import add, subtract, multiply, divide, Calculator
@pytest.fixture

def test_addition():
    '''Test that addition function works'''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works'''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert multiply(2,4) == 8

def test_division():
    '''Test that division function works'''     
    assert divide(2,2) == 1
    
# command #
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(1, 1) == 2
    assert calculator.add(-1, 1) == 0

def test_subtract(calculator):
    assert calculator.subtract(2, 1) == 1
    assert calculator.subtract(0, 5) == -5

def test_multiply(calculator):
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-1, -1) == 1

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(9, 3) == 3

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)
