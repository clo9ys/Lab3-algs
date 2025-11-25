from src.fibos import fibo

def test_fibo(capsys):
    assert fibo(7) == 13
    assert fibo(0) == 0
    assert fibo(1) == 1