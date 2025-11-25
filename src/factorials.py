def factorial(n: int) -> int:
    if n < 0:
        raise ValueError
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
