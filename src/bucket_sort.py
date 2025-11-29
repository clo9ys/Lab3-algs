from typing import Optional

def bucket_sort(a: list[float], buckets: Optional[int] = None) -> list[float]:
    """
    Сортировка корзинами.
    Для float в [0, 1).
    """
    if not a:
        return []

    n = buckets if buckets is not None else len(a)
    buckets_list = [[] for _ in range(n)]

    # раскладка по корзинам
    for x in a:
        # индекс корзины
        idx = min(int(x * n), n - 1)
        buckets_list[idx].append(x)

    result = []
    # сортировка внутри корзин
    for b in buckets_list:
        result.extend(sorted(b))
    return result
