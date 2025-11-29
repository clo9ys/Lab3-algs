def heapify(a: list[int], n: int, i: int) -> None:
    """
    Просейка кучи.
    a — массив.
    n — размер кучи.
    i — индекс узла.
    """
    # текущий максимум
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # проверка левого
    if l < n and a[l] > a[largest]:
        largest = l

    # проверка правого
    if r < n and a[r] > a[largest]:
        largest = r

    # если нужен обмен
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        # рекурсивная просейка
        heapify(a, n, largest)


def heap_sort(a: list[int]) -> list[int]:
    """
    Кучная сортировка.
    Строит и разбирает кучу.
    """
    n = len(a)
    arr = a.copy()

    # построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # извлечение корня
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr
