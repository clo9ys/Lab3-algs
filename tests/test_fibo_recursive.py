import pytest
from src.fibos import fibo_recursive

def test_fibo_recursive():
    assert fibo_recursive(7) == 13
    assert fibo_recursive(0) == 0
    assert fibo_recursive(1) == 1
