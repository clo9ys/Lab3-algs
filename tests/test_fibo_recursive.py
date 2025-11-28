import pytest
from src.fibos import fibo_recursive

@pytest.mark.parametrize("value, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (7, 13)
])
def test_fibo_recursive(value, expected):
    assert fibo_recursive(value) == expected

