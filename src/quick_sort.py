def quick_sort(arr: list[int]) -> list[int]:
    """
    Быстрая сортировка.
    Реализация через разбиение.
    """
    if len(arr) <= 1:
        return arr

    elem = arr[len(arr) // 2] # основной элемент

    left = [x for x in arr if x < elem] # меньшие

    mid = [x for x in arr if x == elem] # равные

    right = [x for x in arr if x > elem] # большие

    return quick_sort(left) + mid + quick_sort(right)  # рекурсивный сбор
