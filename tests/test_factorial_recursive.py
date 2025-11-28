from src.factorials import factorial_recursive
import pytest

@pytest.mark.parametrize("value, expected", [
    (1, 1),
    (0, 1),
    (2, 2),
    (3, 6),
    (5, 120),
])
def test_factorial_recursive(value, expected):
    assert factorial_recursive(value) == expected
