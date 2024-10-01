'''Testing Operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Decimal('16'), Decimal('2'), add)
    assert calculation.perform() == Decimal('18'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation(Decimal('16'), Decimal('2'), subtract)
    assert calculation.perform() == Decimal('14'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = Calculation(Decimal('16'), Decimal('2'), multiply)
    assert calculation.perform() == Decimal('8'), "Multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = Calculation(Decimal('16'), Decimal('2'), divide)
    assert calculation.perform() == Decimal('8'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('16'), Decimal('0'), divide)
        calculation.perform()