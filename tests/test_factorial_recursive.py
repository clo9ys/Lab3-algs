from src.factorials import factorial_recursive

def test_factorial_recursive():
    assert factorial_recursive(5) == 120
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
