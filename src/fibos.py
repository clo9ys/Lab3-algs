def fibo(n: int) -> int:
    n1, n2 = 0, 1

    if n >= 0:
        for i in range(n):
            n1, n2 = n2, n1 + n2
        return n1

    else:
        raise ValueError("value must be non-negative")


def fibo_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("value must be non-negative")

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)