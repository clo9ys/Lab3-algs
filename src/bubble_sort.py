def bubble_sort(arr: list[int]) -> list[int]:
    """
    Сортировка пузырьком.
    Сортирует список на месте.
    """
    for i in range(len(arr) - 1):
        # внутренний проход
        for j in range(len(arr) - i - 1):
            # сравнение соседей
            if arr[j] > arr[j + 1]:
                # обмен местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr # отсортированный список
