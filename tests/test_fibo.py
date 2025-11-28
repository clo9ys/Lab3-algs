from src.fibos import fibo
import pytest

@pytest.mark.parametrize("value, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (10, 55)
])
def test_fibo(value, expected):
    assert fibo(value) == expected