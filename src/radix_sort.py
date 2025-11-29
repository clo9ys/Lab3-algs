from src.counting_sort import counting_sort


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Поразрядная сортировка.
    base — основание разрядов.
    """

    max_num = max(a) if a else 0   # максимум
    exp = 1    # текущий разряд
    res = a[:]   # рабочая копия

    # пока есть разряды
    while max_num // exp > 0:
        buckets = [[] for _ in range(base)]   # корзины по цифрам
        # раскладка
        for num in res:
            digit = (num // exp) % base
            buckets[digit].append(num)
        # сбор из корзин
        res = []
        for bucket in buckets:
            if bucket:
                # локальная сортировка
                res.extend(counting_sort(bucket))
        exp *= base  # следующий разряд

    return res
