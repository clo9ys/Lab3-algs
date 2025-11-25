import pytest
from src.fibos import fibo, fibo_recursive
from src.factorials import factorial_recursive, factorial

def test_fibo_value_error():
    with pytest.raises(ValueError):
        fibo(-52)

def test_fibo_recursive_value_error():
    with pytest.raises(ValueError):
        fibo_recursive(-52)

def test_factorial_value_error():
    with pytest.raises(ValueError):
        factorial(-52)

def test_factorial_recursive_value_error():
    with pytest.raises(ValueError):
        factorial_recursive(-52)