import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed=None) -> list[int]:
    """
    Массив случайных чисел в заданном диапазоне и с заданной длиной.
    """
    if seed is not None:
        # фиксируем сид
        random.seed(seed)
    if distinct:
        # проверка диапазона
        if hi - lo + 1 < n:
            raise ValueError("range too small for distinct ints")
        # уникальные значения
        return random.sample(range(lo, hi + 1), n)
    # обычные значения
    return [random.randint(lo, hi) for _ in range(n)]


def many_duplicates(n: int, k_unique: int = 5, *, seed=None) -> list[int]:
    """
    Массив с дубликатами.
    k_unique — число разных.
    """
    if seed is not None:
        # фиксируем сид
        random.seed(seed)
    # база уникальных
    base = [random.randint(0, 1000) for _ in range(k_unique)]
    # выбор с повтором
    return [random.choice(base) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """
    Обратная последовательность от n до 1.
    """
    return list(range(n, 0, -1))


def rand_float_array(n: int, lo: float = 0.0, hi: float = 1.0, *, seed = None) -> list[float]:
    """
    Массив float.
    """
    if seed is not None:
        # фиксируем сид
        random.seed(seed)

    # генерация значений
    return [random.uniform(lo, hi) for _ in range(n)]
