from typing import Optional

def bucket_sort(a: list[float], buckets: Optional[int] = None) -> list[float]:
    """
    Bucket sort (сортировка корзинами) для массива float.
    Если buckets не указан, используется количество элементов.
    """
    if not a:
        return []
    n = buckets if buckets is not None else len(a)
    buckets_list = [[] for _ in range(n)]
    for x in a:
        idx = min(int(x * n), n - 1)  # на всякий случай
        buckets_list[idx].append(x)
    result = []
    for b in buckets_list:
        result.extend(sorted(b))
    return result