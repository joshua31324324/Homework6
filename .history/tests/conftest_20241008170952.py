import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def fake_data():
    fake = Faker()
    return {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email()
    }

def test_example(fake_data):
    assert isinstance(fake_data['name'], str)
    assert isinstance(fake_data['address'], str)
    assert isinstance(fake_data['email'], str)



def generate_test_data(num_records):
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        
        # Ensure b is not zero for divide operation to prevent division by zero in expected calculation
        if operation_func == divide:
            b = Decimal('1') if b == Decimal('0') else b
        
        try:
            if operation_func == divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

import pytest
from faker import Faker

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of records to generate")

def pytest_generate_tests(metafunc):
    if 'a' in metafunc.fixturenames and 'b' in metafunc.fixturenames and 'operation' in metafunc.fixturenames and 'expected' in metafunc.fixturenames:
        num_records = metafunc.config.getoption('num_records')
        fake = Faker()
        test_data = []
        for _ in range(num_records):
            a = fake.random_int(min=1, max=100)
            b = fake.random_int(min=1, max=100)
            operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
            if operation == 'add':
                expected = a + b
            elif operation == 'subtract':
                expected = a - b
            elif operation == 'multiply':
                expected = a * b
            elif operation == 'divide':
                expected = a / b if b != 0 else None
            test_data.append((a, b, operation, expected))
        metafunc.parametrize("a,b,operation,expected", test_data)