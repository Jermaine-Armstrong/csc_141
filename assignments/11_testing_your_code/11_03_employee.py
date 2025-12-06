import pytest
from employee import Employee

@pytest.fixture
def emp():
    """Return a fresh Employee instance for each test."""
    return Employee('Kendall', 'Hazard', 50000)

def test_give_default_raise(emp):
    emp.give_raise()
    assert emp.annual_salary == 55000

def test_give_custom_raise(emp):
    emp.give_raise(10000)
    assert emp.annual_salary == 60000
