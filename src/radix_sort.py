from src.counting_sort import counting_sort

def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Поразрядная сортировка с параметром base
    """
    # максимум
    max_num = max(a) if a else 0
    exp = 1
    res = a[:]
    while max_num // exp > 0:
        buckets = [[] for _ in range(base)]
        # раскладываем по корзинам
        for num in res:
            digit = (num // exp) % base
            buckets[digit].append(num)
        # сортируем корзины твоей counting_sort и собираем
        res = []
        for bucket in buckets:
            if bucket:
                res.extend(counting_sort(bucket))
        exp *= base
    return res
